from typing import Annotated , AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session
from app.repositories.music_repository import MusicRepository
from app.services.music_service import MusicService


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def get_music_repository(session: Annotated[AsyncSession, Depends(get_async_session)]) -> MusicRepository:
    return MusicRepository(session)

async def get_music_services(repository: Annotated[MusicRepository, Depends(get_music_repository)]) -> MusicService:
    return MusicService(repository)