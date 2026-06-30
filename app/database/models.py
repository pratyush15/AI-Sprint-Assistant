from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from datetime import datetime, timezone
from app.database.db import Base


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    priority = Column(String(30), default="Medium")
    status = Column(String(30), default="To Do")
    story_points = Column(Integer, nullable=True)
    sprint = Column(String(50), nullable=True)
    assignee = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))