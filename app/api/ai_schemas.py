
from pydantic import BaseModel


class AIRequest(BaseModel):
    task: str
    title: str
    description: str
    question: str = ""


class AIResponse(BaseModel):
    task: str
    content: str