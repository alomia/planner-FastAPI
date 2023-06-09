from typing import Optional, List
from beanie import Document, Link

from pydantic import BaseModel, EmailStr
from typing import Optional, List

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "user-email@email.com",
                "password": "userPassword",
                "username": "userName",
                "events": [],
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
