"""Week 3: POST /ask. Retrieve, decide whether to answer at all, answer only from context, cite.

A system that always answers is worse than one that sometimes declines. Two gates before the
model is even called: is anything relevant enough (threshold), and afterwards: did the model
itself say the context supports the answer (grounded)?
"""

import time
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sqlmodel import Session

from app.api.schemas import ErrorOut
from app.db.session import get_session
from app.guard import Blocked, check_limits, detect_injection, preamble, wrap_untrusted
from app.llm.client import Message, ModelClient, ModelError, ModelTimeout
from app.llm.cost import estimate_cost_usd
from app.llm.registry import get_model_client
from app.llm.structured import SchemaError, complete_structured
from app.retrieval.embed import Embedder, get_embedder
from app.retrieval.store import search
from app.settings import Settings, get_settings
from app.trace import ErrorKind, mark_error

router = APIRouter()

PROMPT_VERSION = "ask_v1"
_PROMPT = (Path(__file__).parent.parent / "llm" / "prompts" / f"{PROMPT_VERSION}.md").read_text()

SessionDep = Annotated[Session, Depends(get_session)]
ClientDep = Annotated[ModelClient, Depends(get_model_client)]
EmbedderDep = Annotated[Embedder, Depends(get_embedder)]
SettingsDep = Annotated[Settings, Depends(get_settings)]


class AskIn(BaseModel):
    question: str = Field(min_length=3, max_length=2000)
    k: int | None = None
    # Which version of the manual the customer is running. The support desk always knows this,
    # and without it a question about version 3 is answered from the version 2 page, which reads
    # perfectly and is wrong. Pass it through to search().
    version: str | None = None


class AskAnswer(BaseModel):
    """What the model must return. `grounded=false` is a legitimate, expected answer."""

    answer: str
    citations: list[int]
    grounded: bool


class Citation(BaseModel):
    n: int
    chunk_id: int
    document_id: int
    filename: str
    score: float
    text: str


class AskOut(BaseModel):
    question: str
    abstained: bool
    injection_detected: bool = False
    reason: str | None = None
    answer: str | None = None
    citations: list[Citation] = []
    top_score: float | None = None
    provider: str | None = None
    model: str | None = None
    tokens_in: int = 0
    tokens_out: int = 0
    latency_ms: int = 0
    cost_usd: float = 0.0


@router.post("/ask", response_model=AskOut, responses={502: {"model": ErrorOut}})
async def ask(
    body: AskIn,
    session: SessionDep,
    client: ClientDep,
    embedder: EmbedderDep,
    settings: SettingsDep,
) -> AskOut | JSONResponse:
    # 1. Retrieve, with the version when the question carries one (the filter runs before ranking).
    hits = search(
        session,
        embedder,
        body.question,
        k=body.k or settings.search_k,
        strategy=settings.chunk_strategy,
        version=body.version,
        mode=settings.search_mode,
    )
    top = hits[0].score if hits else None

    # 2. Gate 1, the cheap one: nothing relevant enough means no model call at all.
    if top is None or top < settings.relevance_threshold:
        mark_error(ErrorKind.retrieval_empty, "nothing cleared the relevance threshold")
        shown = "nothing retrieved" if top is None else f"best score {top:.3f}"
        return AskOut(
            question=body.question,
            abstained=True,
            reason=(
                f"no passage cleared the relevance threshold "
                f"({shown} < {settings.relevance_threshold:g})"
            ),
            top_score=top,
        )

    # 3. The guard: limits first, then every passage fenced as data.
    system = _PROMPT
    injection = False
    passages: list[str] = []
    if settings.guard_enabled:
        try:
            check_limits(settings, session)
        except Blocked as e:
            mark_error(e.kind, e.detail)
            status = 429 if e.kind == ErrorKind.budget_exceeded else 503
            return JSONResponse(
                status_code=status, content=ErrorOut(error=e.kind, detail=e.detail).model_dump()
            )
        extra = preamble()
        if extra:
            system = f"{_PROMPT}\n\n{extra}"
        for h in hits:
            cleaned, report = detect_injection(h.text)
            injection = injection or report.injection_detected
            passages.append(wrap_untrusted(cleaned, label="passage"))
    else:
        passages = [h.text for h in hits]
    numbered = "\n\n".join(f"[{i}] {p}" for i, p in enumerate(passages, 1))
    messages = [
        Message(role="system", content=system),
        Message(role="user", content=f"Passages:\n\n{numbered}\n\nQuestion: {body.question}"),
    ]

    # 4. The call. A failure is a failure, never a decline: a decline is a claim about documents.
    started = time.perf_counter()
    try:
        result, responses = await complete_structured(
            client,
            messages,
            AskAnswer,
            attempts=settings.model_retry_attempts,
            base_delay_s=settings.model_retry_base_delay_s,
            timeout_s=settings.model_timeout_s,
        )
    except ModelTimeout as e:
        mark_error(ErrorKind.provider_timeout, str(e))
        return _fail(f"the model did not answer in time: {e}")
    except ModelError as e:
        mark_error(ErrorKind.provider_error, str(e))
        return _fail(f"the model provider failed: {e}")
    except SchemaError as e:
        mark_error(ErrorKind.schema_error, e.detail)
        return _fail(f"the model's answer did not fit the schema: {e.detail}")
    latency_ms = int((time.perf_counter() - started) * 1000)
    tokens_in = sum(r.tokens_in for r in responses)
    tokens_out = sum(r.tokens_out for r in responses)
    cost = sum(estimate_cost_usd(r.model, r.tokens_in, r.tokens_out) for r in responses)
    provider, model = responses[-1].provider, responses[-1].model

    # 5. Gate 2: the model's own decline, or an answer that cites nothing that was sent.
    valid: list[int] = []
    for n in result.citations:
        if 1 <= n <= len(hits) and n not in valid:
            valid.append(n)
    if not result.grounded or not result.answer.strip() or not valid:
        return AskOut(
            question=body.question,
            abstained=True,
            injection_detected=injection,
            reason="the passages do not contain the answer",
            top_score=top,
            provider=provider,
            model=model,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            latency_ms=latency_ms,
            cost_usd=cost,
        )

    # 6. Every surviving citation maps to the chunk that was actually retrieved.
    citations = [
        Citation(
            n=n,
            chunk_id=hits[n - 1].chunk_id,
            document_id=hits[n - 1].document_id,
            filename=hits[n - 1].filename,
            score=hits[n - 1].score,
            text=hits[n - 1].text,
        )
        for n in valid
    ]
    return AskOut(
        question=body.question,
        abstained=False,
        injection_detected=injection,
        answer=result.answer.strip(),
        citations=citations,
        top_score=top,
        provider=provider,
        model=model,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        latency_ms=latency_ms,
        cost_usd=cost,
    )


def _fail(detail: str) -> JSONResponse:
    return JSONResponse(
        status_code=502, content=ErrorOut(error="provider_error", detail=detail).model_dump()
    )
