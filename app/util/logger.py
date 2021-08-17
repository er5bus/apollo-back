import sys
import logging

from app.config import settings

console = logging.StreamHandler(stream=sys.stdout)
console.setFormatter(
    logging.Formatter("{levelname}/{name} [{filename}:{lineno}]: {message}", style="{")
)

logger = logging.getLogger("application")
logger.propagate = False
logger.addHandler(console)
logger.setLevel(settings.log_level)
