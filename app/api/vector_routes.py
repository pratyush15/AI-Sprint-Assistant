
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.vector_service import (
    find_similar_tickets
)

router = APIRouter(
    prefix="/vector",
    tags=["Vector Search"]
)


class SearchRequest(BaseModel):
    query: str


@router.post("/search")
def search(request: SearchRequest):

    return {
        "results": find_similar_tickets(
            request.query
        )
    }