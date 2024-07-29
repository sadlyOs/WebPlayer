from passlib.context import CryptContext
pwd = CryptContext(schemes = ["bcrypt"])
async def create_hash_password(password: str):
    return pwd.hash(password)