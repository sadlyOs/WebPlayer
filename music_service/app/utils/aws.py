import asyncio
from contextlib import asynccontextmanager

import loguru
from aiobotocore.session import get_session
from app.core.config import settings
class AWS:
    aws_access_key_id: str = settings.AWS_ACCESS_KEY_ID
    aws_secret_access_key: str = settings.AWS_SECRET_ACCESS_KEY
    endpoint_url: str = settings.ENDOINT_URL
    __config: dict = {
        "aws_access_key_id": aws_access_key_id,
        "aws_secret_access_key": aws_secret_access_key,
        "endpoint_url": endpoint_url,
    }
    __session = get_session()

    @classmethod
    @asynccontextmanager
    async def get_client (cls) :
        async with cls.__session.create_client( "s3" , **cls.__config ) as client:
            yield client

    @classmethod
    async def upload_file (cls, file: bytes, file_name: str, bucket_name: str):
        async with cls.get_client() as s3:
            await s3.put_object(Bucket=bucket_name, Key=file_name, Body=file)


