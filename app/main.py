from fastapi import FastAPI

from .config import settings
from .config.db import init_db

from app import accounts

from app.util.logger import logger

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Learning Center",
    redoc_url=settings.redoc_url,
    docs_url=settings.docs_url,
    openapi_url=settings.openapi_url,
)

app.include_router(accounts.authrouter, prefix="/auth", tags=["Auth"])
app.include_router(accounts.authresetpasswordrouter, prefix="/auth", tags=["Auth"])

app.include_router(accounts.usersrouter, prefix="/accounts", tags=["Accounts"])
app.include_router(accounts.registerrouter, prefix="/accounts", tags=["Accounts"])

# Hooks for startup
@app.on_event("startup")
async def startup_event():
    logger.debug("App startup!")
    init_db(app)


# Hooks for shutdown
@app.on_event("shutdown")
async def shutdown_events():
    logger.debug("Shutdown!")


@app.get("/", tags=["Index"])
async def index():
    """
    API-index
    """
    return {
        "version": settings.app_version
    }
