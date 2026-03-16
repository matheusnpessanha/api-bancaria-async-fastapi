from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    ENVIRONMENT: str
    JWT_SECRET: str
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"
        env_file_encoding="utf-8"

settings = Settings()

