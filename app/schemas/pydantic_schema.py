import datetime

from pydantic import BaseModel , Field , EmailStr

class Message(BaseModel):
    message: str = "user was created"

class Error_message(BaseModel):
    message: str = "something went wrong"

class UserAdd(BaseModel):
    username: str = Field(max_length = 50)
    email: EmailStr = Field()
    password: str = Field(min_length = 8)

class UserGet(UserAdd):
    id: int = Field()

class ContentAdd(BaseModel):
    title: str = Field(min_length = 50)
    main_content: str = Field()

class ContentGet(ContentAdd):
    id: int = Field()
    user_id: int = Field()
    created_at: datetime.datetime = Field()

class UserRel(UserAdd):
    content: list["ContentGet"]

class ContentRel(ContentGet):
    user: "UserGet"