from passlib.context import CryptContext
pwd = CryptContext(schemes = ["bcrypt"])
async def create_hash_password(password: str):
    return pwd.hash(password)

async def check_hash_password(password: str, hash_password: str):
    return pwd.verify(password, hash_password)