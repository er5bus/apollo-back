from datetime import datetime

import fastapi_users

from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


from src.config.database import Base


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)

    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow())

    author_id = Column(fastapi_users.db.sqlalchemy.GUID(), ForeignKey('users.id'))
    author = relationship('User', foreign_keys=[author_id])

    post_id = Column(Integer(), ForeignKey('posts.id'))
    post = relationship('Post', foreign_keys=[post_id], backref='comments')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)

    title = Column(String)
    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow())

    author_id = Column(fastapi_users.db.sqlalchemy.GUID(), ForeignKey('users.id'))
    author = relationship('User', foreign_keys=[author_id])

    page_id = Column(Integer(), ForeignKey('pages.id'))
    page = relationship('Page', foreign_keys=[page_id], backref='posts')


class Page(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow())

    author_id = Column(fastapi_users.db.sqlalchemy.GUID(), ForeignKey('users.id'))
    author = relationship('User', foreign_keys=[author_id])
