from fastapi import APIRouter , Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import UserAdd
from auth.utils import login, delete_user, register_operation
from database import get_async_session


router = APIRouter(
    prefix = "/user",
    tags = ["User Registration"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/user/login")
@router.post("/register")
async def register(user_data: UserAdd, session: AsyncSession = Depends(get_async_session)):
    return await register_operation(session, user_data)

@router.post("/login")
async def login_user(form_data = Depends(login)):
    return form_data

@router.delete("")
async def delete(email: str, session: AsyncSession = Depends(get_async_session)):
    await delete_user(email, session)
    return {"status_code": 200}

@router.get("/me")
async def read_user_me(current_user: dict = Depends(oauth2_scheme)):
    return current_user