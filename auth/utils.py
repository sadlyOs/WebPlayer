from pathlib import Path

import jwt

from datetime import timedelta , datetime

import sqlalchemy
from fastapi import HTTPException , Depends
from sqlalchemy import select , delete
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import UserAdd
from auth.models import User
from auth.tasks import send_email
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from database import get_async_session

# Hash password using bcrypt
pwd = CryptContext(schemes = ["bcrypt"])


async def create_hash_password(password: str):
    return pwd.hash(password)


# JWT
class JWT:
    @staticmethod
    async def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes = 1)):
        try:
            data = data.copy()
            expire = datetime.utcnow() + expires_delta
            data.update({"exp": expire})
            key: Path = Path(__file__).parent / "keys" / "jwt-private.pem"
            encode = jwt.encode(payload = data, key = key.read_text(), algorithm = "RS256")
            return encode
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="An error occurred while creating the access token")
            # raise HTTPException(status_code=400, detail="There is not some data")
#Register user
async def register_operation(session: AsyncSession, user_data: UserAdd) -> dict:
    try:
        password = user_data.password
        user_data.password = await create_hash_password(password)
        execute = User(username=user_data.username, email=user_data.email, hash_password=user_data.password)
        session.add(execute)
        await session.commit()
        send_email.delay( username = user_data.username , email = user_data.email )
        return {"message": "User registration successful"}
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=400, detail="Email or username already exists")

#Login user
async def login(user_data=Depends(OAuth2PasswordRequestForm), session: AsyncSession = Depends(get_async_session)):
    user = select(User).filter(User.username == user_data.username)
    execute = await session.execute(user)
    result = execute.scalars().all()
    if not result:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not pwd.verify(user_data.password, result[0].hash_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=30)
    access_token = await JWT.create_access_token(
        data={
            "sub": result[0].id,
            "username": user_data.username,
        },
        expires_delta=access_token_expires
    )
    user.token = access_token

    return {"access_token": access_token, "token_type": "bearer"}

async def delete_user(user_email, session: AsyncSession):
    execute = delete(User).filter(User.email == user_email)
    await session.execute(execute)
    await session.commit()