import jwt
from app.core.security import get_public_key
from fastapi import HTTPException

class JWT:
    @staticmethod
    async def decode_access_token(token: str):
        try:
            key = await get_public_key()
            decode = jwt.decode(jwt = token, key = key, algorithms = ["RS256"])
            return decode
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")