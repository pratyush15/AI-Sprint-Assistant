from sqlalchemy.orm import Session
from app.database.models import Ticket
from app.vector_db.chroma_store import (
    add_document,
    search_documents,
    document_exists
)


def index_all_tickets(db: Session):
    tickets = db.query(Ticket).all()
    for ticket in tickets:

        if document_exists(str(ticket.id)):
            continue

        text = f"""
        Title:
        {ticket.title}

        Description:
        {ticket.description}

        Priority:
        {ticket.priority}

        Status:
        {ticket.status}
        """

        add_document(
            str(ticket.id),
            text
        )




def find_similar_tickets(query: str):
    docs = search_documents(query)
    results = []
    for doc, score in docs:

        similarity = round(
            (1 / (1 + score)) * 100,
            2
        )

        results.append(
            {
                "ticket": doc.page_content,
                "similarity": similarity
            }
        )

    return results