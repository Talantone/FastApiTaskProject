import datetime
from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel
from .user import UserOut


class Task(Document):
    title: str
    description: Optional[str] = None
    completed: bool = False
    user: UserOut

    @property
    def created(self) -> datetime:
        """Datetime task was created from ID"""
        return self.id.generation_time

