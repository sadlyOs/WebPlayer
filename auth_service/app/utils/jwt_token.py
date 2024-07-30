import jwt
from app.core.security import get_private_key
from datetime import timedelta , datetime
from fastapi import HTTPException


class JWT:
    @staticmethod
    async def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes = 1)):
        try:
            data = data.copy()
            expire = datetime.utcnow() + expires_delta
            data.update({"exp": expire})
            key = await get_private_key()
            encode = jwt.encode(payload = data, key = key, algorithm = "RS256")
            return encode
        except Exception as e:
            raise HTTPException(status_code=400, detail="An error occurred while creating the access token")