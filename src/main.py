from . import create_app

from src.config import settings

app = create_app()

@app.get("/", tags=["Index"])
async def index():
    """
    API-index
    """
    return {
        "version": settings.app_version
    }
