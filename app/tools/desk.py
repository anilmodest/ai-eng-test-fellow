"""Week 1: the agent's first two tools, get_customer and get_ticket.

Both read only through app/support.py, which is the desk's scope. Each returns only what the desk
needs to work a request (no seats, no contact details), and every refusal is a sentence a model
can read and act on, never an exception.
"""

from pydantic import BaseModel, ConfigDict, Field

from app.support import OutOfScope, customer, ticket
from app.tools.base import ToolContext, ToolSpec, as_json

CUSTOMER_ID = r"^C-\d{4}$"
TICKET_ID = r"^T-\d{4}$"


class GetCustomerArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    customer_id: str = Field(
        pattern=CUSTOMER_ID,
        description="The customer id exactly as written in the request: a capital C, a hyphen "
        "and four digits, for example C-1004.",
    )


class GetTicketArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    ticket_id: str = Field(
        pattern=TICKET_ID,
        description="The support ticket id exactly as written in the request: a capital T, a "
        "hyphen and four digits, for example T-2006.",
    )


async def get_customer(ctx: ToolContext, args: GetCustomerArgs) -> str:
    try:
        row = customer(ctx.session, args.customer_id)
    except OutOfScope:
        return (
            f"refused: {args.customer_id} is not a customer this desk may read; "
            "check the id with the requester, or hand the request to the desk that owns it"
        )
    return as_json(
        {
            "customer_id": row.customer_id,
            "account": row.account,
            "version": row.version,
            "plan": row.plan,
            "region": row.region,
        }
    )


async def get_ticket(ctx: ToolContext, args: GetTicketArgs) -> str:
    try:
        row = ticket(ctx.session, args.ticket_id)
    except OutOfScope:
        return (
            f"refused: {args.ticket_id} is not a ticket this desk may read; "
            "check the id with the requester, or hand the request to the desk that owns it"
        )
    return as_json(
        {
            "ticket_id": row.ticket_id,
            "customer_id": row.customer_id,
            "status": row.status,
            "priority": row.priority,
            "category": row.category,
            "product_version": row.product_version,
            "subject": row.subject,
            "body": row.body,
            "opened_at": row.opened_at,
            "closed_at": row.closed_at,
        }
    )


GET_CUSTOMER = ToolSpec(
    name="get_customer",
    description="Look up one of this desk's customers by customer id (C-1234). Call it when a "
    "request asks which product version or release a customer runs, which plan they are on, or "
    "which account they belong to. Returns the customer's version, plan, account and region; "
    "never seats or contact details. Another desk's customer is refused.",
    args=GetCustomerArgs,
    run=get_customer,
)

GET_TICKET = ToolSpec(
    name="get_ticket",
    description="Look up one support ticket by ticket id (T-1234). Call it when a request asks "
    "what a ticket says, its status (open, pending, closed), priority, category, subject, or "
    "which product version the ticket reports. Returns those fields plus the ticket text and "
    "the customer id. A ticket from another desk is refused.",
    args=GetTicketArgs,
    run=get_ticket,
)
