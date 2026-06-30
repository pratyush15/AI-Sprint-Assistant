from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str = "Medium"
    status: str = "To Do"
    story_points: Optional[int] = None
    sprint: Optional[str] = None
    assignee: Optional[str] = None
    
class TicketUpdate(BaseModel):
    title: str
    description: str
    priority: str
    status: str
    story_points: int | None = None
    sprint: str | None = None
    assignee: str | None = None

class TicketResponse(TicketCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True