from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    REDIS_HOST: str
    REDIS_PORT: str
    SMTP_USER: str
    SMTP_PASSWORD: str

    @property
    def DB_URI(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def CELERY_BROKER_URLS(self):
        return { 0: self.REDIS_HOST, 1: self.REDIS_PORT}



    model_config = SettingsConfigDict( env_file = ".env" )

settings = Settings()