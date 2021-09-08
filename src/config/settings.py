import logging
from typing import List

from pydantic import BaseSettings as PydanticBaseSettings, PostgresDsn


class BaseSettings(PydanticBaseSettings):
    app_name: str = "Apollo"
    app_version: str = "0.1.0-alpha"
    jwt_secret: str
    reset_password_secret: str
    db_url: PostgresDsn


class DevSettings(BaseSettings):
    env: str = "DEV"
    log_level: int = logging.DEBUG
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"

    class Config:
        env_file = ".env"


class ProdSettings(BaseSettings):
    env: str = "PRODUCTION"
    app_name: str = "FastAPI Boilerplate Production"


settings = {"DEV": DevSettings(), "PROD": ProdSettings()}
