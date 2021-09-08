from typing import List
from fastapi import APIRouter, status, Response

from src.config.db import database
from ..models.posts import Comment, Post, Page
from ..schemas.posts import CommentOut, CommentIn, PostlIn, PostOut, PageOut, PageIn

from ..utils.crud import (paginate, find_one, update_one, insert_one, delete_one)


comment_router = APIRouter(prefix="/api/comments", tags=["Comment"])

post_router = APIRouter(prefix="/api/posts", tags=["Post"])

page_router = APIRouter(prefix="/api/pages", tags=["Page"])


@comment_router.get("", response_model=List[CommentOut], status_code=status.HTTP_200_OK)
async def read_comments(skip: int = 0, limit: int = 100):
    """ Get all comments """
    return await paginate(Comment, skip, limit)


@comment_router.get("/{comment_id}", response_model=CommentOut, status_code=status.HTTP_200_OK)
async def read_comment(comment_id: int):
    """ Get one comment """
    return await find_one(Comment, comment_id)


@comment_router.delete("/{comment_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(comment_id: int):
    """ Get one comment """
    await delete_one(Comment, comment_id)


@comment_router.put("/{comment_id", response_model=CommentOut, status_code=status.HTTP_200_OK)
async def update_comment(comment_id: int, comment: CommentIn):
    """ Update one comment """
    return await update_one(Comment, comment, comment_id)


@comment_router.post("", response_model=CommentOut, status_code=status.HTTP_200_OK)
async def create_comment(comment: CommentIn):
    """ Create a classe comment """
    return await insert_one(Comment, comment)


@post_router.get("", response_model=List[PostOut], status_code=status.HTTP_200_OK)
async def read_posts(skip: int = 0, limit: int = 100):
    """ Get all posts """
    return await paginate(Post, skip, limit)


@post_router.get("/{post_id}", response_model=PostOut, status_code=status.HTTP_200_OK)
async def read_post(post_id: int):
    """ Get one post """
    return await find_one(Post, post_id)


@post_router.delete("/{post_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    """ Get one post """
    await delete_one(Post, post_id)


@post_router.put("/{post_id}", response_model=PostOut, status_code=status.HTTP_200_OK)
async def update_post(post_id: int, post: PostlIn):
    """ Update one post """
    return await update_one(Post, post, post_id)


@post_router.post("", response_model=PostOut, status_code=status.HTTP_200_OK)
async def create_post(post: PostlIn):
    """ Create a classe post """
    return await insert_one(Post, post)


@page_router.get("", response_model=List[PageOut], status_code=status.HTTP_200_OK)
async def read_pages(skip: int = 0, limit: int = 100):
    """ Get all pages """
    return await paginate(Page, skip, limit)


@page_router.get("/{page_id}", response_model=PageOut, status_code=status.HTTP_200_OK)
async def read_page(page_id: int):
    """ Get one page """
    return await find_one(Page, page_id)


@page_router.delete("/{page_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_page(page_id: int):
    """ Get one page """
    await delete_one(Page, page_id)


@page_router.put("/{page_id}", response_model=PageOut, status_code=status.HTTP_200_OK)
async def update_page(page_id: int, page: PageIn):
    """ Update one page """
    return await update_one(Page, page, page_id)


@page_router.post("", response_model=PageOut, status_code=status.HTTP_200_OK)
async def create_page(page: PageIn):
    """ Create a classe page """
    return await insert_one(Page, page)
