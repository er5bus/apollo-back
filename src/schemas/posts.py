from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PageIn(BaseModel):
    name: str
    author_id = int
    description: Optional[str] = None


class PageOut(BaseModel):
    id: int
    name: str
    author_id = int
    description: Optional[str] = None


class PostlIn(BaseModel):
    title: str
    body: str
    author_id = str
    page_id = int
    timestamp:Optional[datetime]=None


class PostOut(BaseModel):
    id: int
    title: str
    body: str
    timestamp:Optional[datetime]=None
    page: Optional[PageOut] = None


class CommentIn(BaseModel):
    body: str
    author_id = str
    post_id = int


class CommentOut(BaseModel):
    id: int
    body: str
    author_id = str
    timestamp:Optional[datetime]=None
    post: Optional[PostOut] = None


    class Config:
        orm_mode = True