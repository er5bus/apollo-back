from typing import List

from pydantic import BaseSettings as PydanticBaseSettings, PostgresDsn


class BaseSettings(PydanticBaseSettings):
    app_name: str = "Apollo"
    app_version: str = "0.1.0-alpha"
    jwt_secret: str
    reset_password_secret: str
    db_url: PostgresDsn

    model_directories: List[str] = [
        "app.accounts.models",
        "aerich.models"
    ]
