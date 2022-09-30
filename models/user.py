
import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from beanie import Document, Indexed


class UserAuth(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    """Updatable user fields"""
    name: Optional[str]
    email: Optional[EmailStr]


class UserOut(UserUpdate):
    """User fields returned to the client"""

    email: Indexed(EmailStr, unique=True)
    disabled: bool = False


class User(Document, UserOut):
    """Database user representation"""
    password: str
    email_confirmed_at: Optional[datetime.datetime]

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def created(self) -> datetime:
        """Datetime user was created from ID"""
        return self.id.generation_time

    @classmethod
    async def by_email(cls, email: str) -> "User":
        """Get a user by email"""
        return await cls.find_one(cls.email == email)

