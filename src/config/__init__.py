import os

from .settings import settings as env_settings

DEFAULT_ENV = 'DEV'

env = os.getenv('ENVIRONMENT', DEFAULT_ENV)

settings = env_settings.get(env, DEFAULT_ENV)
