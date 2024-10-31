from fastapi import FastAPI
app = FastAPI()
import uuid
from pydantic import BaseModel, Field, field_validator
from typing import Optional

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bycrypt'], deprecated='auto')
class User(BaseModel):
    id: int
    email: str
    username: Optional[str]
    password: str = Field(..., min_length=8)

    @field_validator("password", mode="before")
    def hashed_password(cls, password):
        return pwd_context(hash(password))

@app.get('/')
def home_view():
    return {"Hello": "Hello Tony."}


@app.post('users/register')
def register_user():
    pass
