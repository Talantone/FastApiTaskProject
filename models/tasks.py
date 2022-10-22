import datetime
from typing import Optional, Any, List

from beanie import Document
from pydantic import BaseModel
from .user import UserOut, User


class Task(Document):
    title: str = None
    description: Optional[str] = None
    completed: bool = False
    user: UserOut

    @property
    def created(self) -> datetime:
        """Datetime task was created from ID"""
        return self.id.generation_time


class TaskUpdate(BaseModel):
    title: str
    description: Optional[str]
    completed: Optional[bool]


class TaskCreate(BaseModel):
    title: str
