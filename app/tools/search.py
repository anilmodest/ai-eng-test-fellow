"""Week 2: search_docs, the agent's second tool.

Retrieval becomes a tool the agent calls, with an argument the first tool supplied: get_customer
says the customer runs v3, so search_docs is called with version "v3" and can only ever return
version 3 pages and the pages that apply to every version. The version filter in
app/retrieval/versions.py is what makes that true; this tool is how the agent reaches it.

The version is required on purpose: an optional version is one the model leaves out, and then
the version trap is back. k is bounded so a call cannot fill the context window with noise.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.retrieval.embed import get_embedder
from app.retrieval.store import search
from app.tools.base import ToolContext, ToolSpec, as_json


class SearchDocsArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(
        min_length=2,
        max_length=300,
        description="What to look up in the product manual, in plain words or an exact setting "
        "name or error code, for example 'default connection timeout' or 'E1104'.",
    )
    version: Literal["v2", "v3"] = Field(
        description="The product version the customer runs, v2 or v3, taken from get_customer "
        "(its version field) or from the ticket's product_version. Only that version's pages, "
        "and pages that apply to every version, come back.",
    )
    k: int = Field(
        default=3,
        ge=1,
        le=10,
        description="How many passages to return, from 1 to 10; 3 is usually enough.",
    )

    @field_validator("query")
    @classmethod
    def query_has_words(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("the query is empty; say what to look up")
        return v.strip()


async def search_docs(ctx: ToolContext, args: SearchDocsArgs) -> str:
    embedder = ctx.embedder or get_embedder()
    hits = search(
        ctx.session,
        embedder,
        args.query,
        k=args.k,
        strategy=ctx.settings.chunk_strategy,
        version=args.version,
        mode=ctx.settings.search_mode,
    )
    if not hits:
        return (
            f"no results: nothing in the {args.version} manual matches {args.query!r}; "
            "try other words or an exact setting name, or say the manual does not cover it"
        )
    results = [
        {
            "rank": i,
            "filename": h.filename,
            "version": h.version or "all versions",
            "score": round(h.score, 3),
            "text": h.text,
        }
        for i, h in enumerate(hits, 1)
    ]
    return as_json({"query": args.query, "version": args.version, "results": results})


SEARCH_DOCS = ToolSpec(
    name="search_docs",
    description="Search the product manual for passages that answer a question, restricted to "
    "one product version. Call it when a request asks how a setting works, what a default or "
    "limit is, or what an error means, after you know the customer's version (get_customer or "
    "get_ticket). Returns the best passages, each with its filename and version so the answer "
    "can cite it, or 'no results' in words.",
    args=SearchDocsArgs,
    run=search_docs,
)
