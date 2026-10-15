"""Week 1: POST /documents/{id}/extract. The exercise is in weeks/1/README.md.

Everything you need is already imported below. The tests in tests/weeks/test_week1.py are the
contract. Nothing in this file may name a provider, a model or an SDK.
"""

import time
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

from app.api.schemas import DocumentExtract, ErrorOut, ExtractOut
from app.db.models import Document, Extraction
from app.db.session import get_session
from app.llm.client import Message, ModelClient, ModelError, ModelTimeout
from app.llm.cost import estimate_cost_usd
from app.llm.registry import get_model_client
from app.llm.structured import SchemaError, complete_structured
from app.settings import Settings, get_settings

router = APIRouter()

# Bump this when the prompt changes: it is part of the idempotency key.
PROMPT_VERSION = "extract_v1"
_PROMPT = (
    Path(__file__).resolve().parent.parent / "llm" / "prompts" / f"{PROMPT_VERSION}.md"
).read_text(encoding="utf-8")

SessionDep = Annotated[Session, Depends(get_session)]
ClientDep = Annotated[ModelClient, Depends(get_model_client)]
SettingsDep = Annotated[Settings, Depends(get_settings)]


def _error(status: int, code: str, detail: str) -> JSONResponse:
    """Every failure leaves through here: a stable code and a human detail, never a stack trace."""
    return JSONResponse(
        status_code=status, content=ErrorOut(error=code, detail=detail).model_dump()
    )


@router.post(
    "/documents/{doc_id}/extract",
    response_model=ExtractOut,
    responses={404: {"model": ErrorOut}, 502: {"model": ErrorOut}, 504: {"model": ErrorOut}},
)
async def extract_document(
    doc_id: int, session: SessionDep, client: ClientDep, settings: SettingsDep
) -> ExtractOut | JSONResponse:
    doc = session.get(Document, doc_id)
    if doc is None:
        return _error(404, "not_found", f"no document {doc_id}")

    stored = session.exec(
        select(Extraction).where(
            Extraction.document_id == doc_id,
            Extraction.provider == client.name,
            Extraction.model == client.model,
            Extraction.prompt_version == PROMPT_VERSION,
        )
    ).first()
    if stored is not None:
        return _out(stored, cached=True)

    body = (doc.text or "")[: settings.max_input_chars]
    messages = [
        Message(role="system", content=_PROMPT),
        Message(role="user", content=f"Document:\n{body or '(empty)'}"),
    ]
    started = time.perf_counter()
    try:
        extract, responses = await complete_structured(
            client,
            messages,
            DocumentExtract,
            attempts=settings.model_retry_attempts,
            base_delay_s=settings.model_retry_base_delay_s,
            timeout_s=settings.model_timeout_s,
        )
    except ModelTimeout as e:
        return _error(504, "provider_timeout", str(e))
    except ModelError as e:
        return _error(502, "provider_error", str(e))
    except SchemaError as e:
        return _error(502, "schema_error", f"model output did not fit the schema: {e.detail}")
    latency_ms = int((time.perf_counter() - started) * 1000)

    tokens_in = sum(r.tokens_in for r in responses)
    tokens_out = sum(r.tokens_out for r in responses)
    row = Extraction(
        document_id=doc_id,
        provider=client.name,
        model=client.model,
        prompt_version=PROMPT_VERSION,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        latency_ms=latency_ms,
        cost_usd=sum(estimate_cost_usd(r.model, r.tokens_in, r.tokens_out) for r in responses),
        result_json=extract.model_dump_json(),
    )
    session.add(row)
    session.commit()
    session.refresh(row)
    return _out(row, cached=False)


def _out(row: Extraction, *, cached: bool) -> ExtractOut:
    return ExtractOut(
        document_id=row.document_id,
        cached=cached,
        provider=row.provider,
        model=row.model,
        prompt_version=row.prompt_version,
        tokens_in=row.tokens_in,
        tokens_out=row.tokens_out,
        latency_ms=row.latency_ms,
        cost_usd=row.cost_usd,
        extract=DocumentExtract.model_validate_json(row.result_json),
    )
