from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVICE_ACCOUNT_KEY: str
    class Config:
        env_file = ".env"