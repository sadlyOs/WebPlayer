import datetime

from app.repositories.user_repository import UserRepository
from app.schemas.pydantic_schema import UserAdd
from app.utils.jwt_token import JWT

class UserService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    async def create_user(self, user_data: UserAdd):
        await self.__repository.create_user(user_data)

    async def delete_user(self, user_email: str):
        await self.__repository.delete_user(user_email)

    async def get_user_by_username(self, user_name: str):
        return await self.__repository.get_user_by_username(user_name)

    async def create_access_token(self, data: dict, expires: datetime.timedelta):
        return await JWT.create_access_token(data = data, expires_delta = expires)