from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker , AsyncSession
from app.core.config import settings
from typing import AsyncGenerator

async_engine = create_async_engine(
    url = settings.DB_URI,
    echo = True
)

async_session = async_sessionmaker(async_engine, class_ = AsyncSession)

