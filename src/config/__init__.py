import os

from . import development, production

env = os.getenv('ENVIRONMENT', 'DEV')

settings = development.settings if env == "DEV" else production.settings
