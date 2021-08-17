from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from . import settings

TORTOISE_ORM = {
    "connections": {
        "default": settings.db_url
    },
    "apps": {
        "models": {
            "models": settings.model_directories,
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True,
    )
