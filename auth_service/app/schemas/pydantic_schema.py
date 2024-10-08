import datetime

from pydantic import BaseModel , Field , EmailStr
from fastapi import Form


class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: int

class Message(BaseModel):
    message: str = "user was created"

class Error_message(BaseModel):
    detail: str = "something went wrong"

class UserAdd(BaseModel):
    username: str = Form()
    email: EmailStr = Form()
    password: str = Form()

class UserGet(UserAdd):
    id: int = Field()

# class ContentAdd(BaseModel):
#     title: str = Field(min_length = 50)
#     main_content: str = Field()

# class ContentGet(ContentAdd):
#     id: int = Field()
#     user_id: int = Field()
#     created_at: datetime.datetime = Field()

# class UserRel(UserAdd):
#     content: list["ContentGet"]

# class ContentRel(ContentGet):
#     user: "UserGet"