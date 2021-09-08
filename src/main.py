"""
    Create fastapi app
"""
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from src.routers import routers

from src.config.database import database
from src.config import settings


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
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

for router_kwargs in routers:
    app.include_router(**router_kwargs)

@app.on_event("startup")
async def startup():
    """ on start the app """
    await database.connect()


@app.on_event("shutdown")
async def shutdon():
    """ on shutdon the app """
    await database.disconnect()


@app.get("/", tags=["Index"])
async def index():
    """
    API-index
    """
    return {
        "version": settings.app_version
    }
