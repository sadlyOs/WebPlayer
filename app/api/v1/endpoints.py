from typing import Annotated

import sqlalchemy
from fastapi import Depends , APIRouter , HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.api.v1.dependencies import get_users_service
from app.schemas.pydantic_schema import UserAdd, Message, Error_message
from app.services.user_services import UserService

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/v1/login")
@router.post(
    "/register",
    response_model = Message,
    responses = {
        200: {
            "status_code": 200,
            "model": Message,
            "description": "User was successfully registered",
        },
        400: {
            "status_code": 400,
            "model": Error_message,
            "description": "Email or username is already registered",

        },
    },
)
async def register(user_data: UserAdd, service: Annotated[UserService, Depends(get_users_service)]):
    try:
        await service.create_user(user_data)
        return {"message": "user was created"}
    except sqlalchemy.exc.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Email or username is already registered")

# @router.post("/login")
# async def login_user(form_data = Depends(login)):
#     return form_data
#
@router.delete("/delete", responses = {
    200: {
            "status_code": 200,
            "description": "User was successfully deleted",
        },
    404: {
            "status_code": 404,
            "description": "User not found",
        },
    },
)
async def delete(email: str, service: Annotated[UserService, Depends(get_users_service)]):
    await service.delete_user(email)
    return {"status_code": 200}
#
# @router.get("/me")
# async def read_user_me(current_user: dict = Depends(oauth2_scheme)):
#     return current_user