from pydantic_settings import BaseSettings
import os 
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_DAYS: int = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")
    ALGORITHM: str = os.getenv("ALGORITHM")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '..', '.env')


settings = Settings()