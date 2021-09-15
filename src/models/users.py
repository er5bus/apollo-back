from datetime import datetime
import enum
from sqlalchemy import Column, String, Integer, Date, DateTime, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_users.db import SQLAlchemyBaseUserTable

from src.config.database import Base


class UserType(enum.Enum):
    STUDENT = 1
    ADMIN = 2
    TEACHER = 3

class User(Base, SQLAlchemyBaseUserTable):
    __tablename__ = 'users'
    user_type = Column(Integer, Enum(UserType))
    permissions = Column(Integer)
    modules = Column(Integer)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role", foreign_keys=[role_id])
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    profile = relationship("Profile", backref='account', foreign_keys=[profile_id])

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    birth_date = Column(Date)
    about_me = Column(Text)
    address = Column(Text)
    member_since = Column(DateTime, default=datetime.utcnow)

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    permissions = Column(Integer)
    modules = Column(Integer)

class Modules:
    """ App modules """
    CLASSE= 1
    COURSE=2
    QUIZ=4
    HOMEWORK=8
    PASS_QUIZE=16
    PASS_HOMEWORK=32

class Permission:
    """ Perissions for each module """
    CREATE=1
    UPDATE=2
    DELETE=4
    READ=8
