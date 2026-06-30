from sqlalchemy.orm import Session

from app.database.models import Ticket
# from app.api.schemas import TicketCreate
from app.api.schemas import (
    TicketCreate,
    TicketUpdate
)


def get_all_tickets(db: Session):
    return db.query(Ticket).all()


def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def create_ticket(db: Session, ticket: TicketCreate):
    new_ticket = Ticket(**ticket.model_dump())

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


def update_ticket(
    db: Session,
    ticket_id: int,
    ticket_data: TicketUpdate
):

    ticket = get_ticket(
        db,
        ticket_id
    )

    if ticket is None:
        return None

    for key, value in ticket_data.model_dump().items():

        setattr(
            ticket,
            key,
            value
        )

    db.commit()
    db.refresh(ticket)

    return ticket


def delete_ticket(db: Session, ticket_id: int):
    ticket = get_ticket(db, ticket_id)

    if ticket is None:
        return None

    db.delete(ticket)
    db.commit()

    return ticket