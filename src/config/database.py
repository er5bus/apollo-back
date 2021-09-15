import databases

from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from . import settings


database = databases.Database(settings.db_url, min_size=5, max_size=20)

Base: DeclarativeMeta = declarative_base()
