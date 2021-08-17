from .base import BaseSettings


class ProdSettings(BaseSettings):
    env: str = "PRODUCTION"
    app_name: str = "FastAPI Boilerplate Production"


settings = ProdSettings()
