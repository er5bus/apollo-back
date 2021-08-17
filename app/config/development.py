import logging

from .base import BaseSettings


class DevSettings(BaseSettings):
    env: str = "DEV"
    log_level: int = logging.DEBUG
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"

    class Config:
        env_file = ".env"


settings = DevSettings()
