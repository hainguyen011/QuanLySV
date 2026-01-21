from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480
    MONGODB_URL: str
    DATABASE_NAME: str = "quanlysv"

    class Config:
        env_file = ".env"

settings = Settings()
