from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    APP_NAME: str = "FastAPI App"

    class Config:
        env_file = ".env"

settings = Settings()
