from datetime import timedelta
from typing import Annotated

import loguru
import sqlalchemy
from fastapi import Depends , APIRouter , HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from app.api.v1.dependencies import get_users_service
from app.schemas.pydantic_schema import UserAdd, Message, Error_message, Token
from app.services.user_services import UserService
from app.utils.hash_password import check_hash_password

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

@router.post("/login",responses = {
    200: {
            "status_code": 200,
            "model": Token,
            "description": "User was successfully logged in",
        },
    401: {
            "status_code": 401,
            "model": Error_message,
            "description": "Incorrect username or password",
        },
    },
)
async def login_user(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        service: Annotated[UserService, Depends(get_users_service)]
):
    user = await service.get_user_by_username(form_data.username)
    if not user:
        raise HTTPException (status_code = 401 , detail = "Incorrect username or password")
    if not await check_hash_password(form_data.password, user[0].hash_password):
        raise HTTPException (status_code = 401 , detail = "Incorrect username or password")
    access_token_expires = timedelta(minutes=30)
    access_token = await service.create_access_token(data={"sub": user[0].id, "username": user[0].username}, expires=access_token_expires)
    user[0].token = access_token
    return Token(access_token=access_token, token_type="bearer")

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

@router.get("/me")
async def read_user_me(service: Annotated[UserService, Depends(get_users_service)], current_user: dict = Depends(oauth2_scheme)):
    loguru.logger.info(current_user)
    return await service.decode_access_token(current_user)