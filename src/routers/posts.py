from fastapi import APIRouter, Depends
from typing import List

from src.utils.crud_router import include_generic_collection_document_router
from src.dependencies import current_active_user
from src.services.posts import CommentService, PostService, PageService


dependencies: List[Depends] = [Depends(current_active_user)]


comment_service: CommentService = CommentService()
comment_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/comments", tags=["Comment"])
include_generic_collection_document_router(comment_router, comment_service)


post_service: PostService = PostService()
post_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/posts", tags=["Post"])
include_generic_collection_document_router(post_router, post_service)


page_service: PageService = PageService()
page_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/pages", tags=["Page"])
include_generic_collection_document_router(page_router, page_service)
