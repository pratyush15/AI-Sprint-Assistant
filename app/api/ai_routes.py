
from fastapi import APIRouter

from app.api.ai_schemas import (
    AIRequest,
    AIResponse
)

from app.services.graph_service import (
    run_ai_task
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post(
    "/run",
    response_model=AIResponse
)
def run(request: AIRequest):

    return run_ai_task(
        request.task,
        request.title,
        request.description,
        request.question
    )