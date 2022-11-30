from pydantic import BaseSettings
from decouple import config


class Setting(BaseSettings):
    
    # database connection config
    DB_CONNECTION :str = config("DB_CONNECTION")
    DB_HOST : str = config("DB_HOST")
    DB_PORT : str = config("DB_PORT")
    DB_NAME : str = config("DB_NAME")
    DB_USER : str = config("DB_USER")
    DB_PASSWORD : str = config("DB_PASSWORD")
    # access token security
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    APP_NAME: str = config("APP_NAME")
    SERVER_NAME: str = config("SERVER_NAME")
    SERVER_HOST: str = config("SERVER_HOST")
    SERVER_PORT: str = config("SERVER_PORT", default=8001)
    DEFAULT_PARAMS_USE = ['page', 'page_size', 'order', 'order_by', 'user']

    class Config:
        case_sensitive = True


settings = Setting()
