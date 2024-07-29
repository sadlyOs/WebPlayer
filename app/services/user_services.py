from app.repositories.user_repository import UserRepository
from app.schemas.pydantic_schema import UserAdd


class UserService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    async def create_user(self, user_data: UserAdd):
        await self.__repository.create_user(user_data)

    async def delete_user(self, user_email: str):
        await self.__repository.delete_user(user_email)