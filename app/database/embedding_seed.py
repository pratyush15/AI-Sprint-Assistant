from app.database.db import SessionLocal

from app.services.vector_service import (
    index_all_tickets
)


def seed_embeddings():
    db = SessionLocal()
    index_all_tickets(db)

    db.close()