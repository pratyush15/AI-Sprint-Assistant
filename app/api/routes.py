from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db import get_db
from app.api.schemas import (
    TicketCreate,
    TicketUpdate,
    TicketResponse
)

from app.services.ticket_service import (
    get_all_tickets,
    get_ticket,
    create_ticket,
    delete_ticket, 
    update_ticket
)

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.get("/", response_model=list[TicketResponse])
def read_tickets(db: Session = Depends(get_db)):
    return get_all_tickets(db)


@router.get("/{ticket_id}", response_model=TicketResponse)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = get_ticket(db, ticket_id)

    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


@router.post("/", response_model=TicketResponse)
def add_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(db, ticket)


@router.put(
    "/{ticket_id}",
    response_model=TicketResponse
)
def edit_ticket(
    ticket_id: int,
    ticket: TicketUpdate,
    db: Session = Depends(get_db)
):

    updated = update_ticket(
        db,
        ticket_id,
        ticket
    )

    if updated is None:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return updated


@router.delete("/{ticket_id}")
def remove_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = delete_ticket(db, ticket_id)

    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {"message": "Ticket deleted successfully"}