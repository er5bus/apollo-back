from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import accounts, classes, posts

from .config.db import database
from .config import settings



def create_app() -> FastAPI:
    """
    Create fastapi app
    """

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Learning Center",
        redoc_url=settings.redoc_url,
        docs_url=settings.docs_url,
        openapi_url=settings.openapi_url,
    )

    origins, methods, headers = ["*"], ["*"], ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=methods,
        allow_headers=headers,
    )

    app.include_router(accounts.authrouter, prefix="/api/auth", tags=["Auth"])
    app.include_router(accounts.authresetpasswordrouter, prefix="/api/auth", tags=["Auth"])

    app.include_router(accounts.usersrouter, prefix="/accounts", tags=["Accounts"])
    app.include_router(accounts.registerrouter, prefix="/accounts", tags=["Accounts"])

    app.include_router(classes.section_router)
    app.include_router(classes.classe_router)
    app.include_router(classes.level_router)

    app.include_router(posts.comment_router)
    app.include_router(posts.post_router)
    app.include_router(posts.page_router)


    @app.on_event("startup")
    async def startup():
        await database.connect()


    @app.on_event("shutdown")
    async def shutdon():
        await database.disconnect()

    return app
