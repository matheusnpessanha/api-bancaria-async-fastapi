from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    ENVIRONMENT: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"
        env_file_encoding="utf-8"

settings = Settings()

