from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


from src.config.db import Base


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)

    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow())

    author_id = Column(Integer(), ForeignKey('users.id'))

    post_id = Column(Integer(), ForeignKey('posts.id'))
    post = relationship('Post', foreign_keys=[post_id], backref='comments')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)

    title = Column(String)
    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow())

    author_id = Column(Integer(), ForeignKey('users.id'))
