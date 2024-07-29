from typing import AsyncGenerator , Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session
from app.repositories.user_repository import UserRepository
from app.services.user_services import UserService


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def get_users_repository(sesssion: Annotated[AsyncSession, Depends(get_async_session)]):
    return UserRepository(sesssion)

async def get_users_service(repository = Depends(get_users_repository)):
    return UserService(repository)