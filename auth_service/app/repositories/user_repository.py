from sqlalchemy import delete , select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import User
from app.utils.hash_password import create_hash_password


class UserRepository:
    def __init__(self, async_session_maker: AsyncSession):
        self.__async_session_maker = async_session_maker

    async def create_user(self, user_data):
        password = user_data.password
        user_data.password = await create_hash_password( password )
        execute = User( username = user_data.username , email = user_data.email , hash_password = user_data.password )
        self.__async_session_maker.add( execute )
        await self.__async_session_maker.commit()

    async def delete_user(self, user_email):
        execute = delete(User).filter(User.email == user_email)
        await self.__async_session_maker.execute( execute )
        await self.__async_session_maker.commit()

    async def get_user_by_username(self, username):
        user = select(User).filter(User.username == username)
        execute = await self.__async_session_maker.execute(user)
        result = execute.scalars().all()
        return result

    async def get_user_by_email(self, email: str):
        user = select(User).filter(User.email == email)
        execute = await self.__async_session_maker.execute(user)
        result = execute.scalars().all()
        return result

    async def update_user_password(self, password: str, email: str):
        user = await self.get_user_by_email(email)
        user[0].hash_password = await create_hash_password(password)
        await self.__async_session_maker.commit()