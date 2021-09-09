from .base_service import BaseService

from ..models.posts import Comment, Post, Page
from ..schemas.posts import CommentOut, CommentIn, PostlIn, PostOut, PageOut, PageIn

class CommentService(BaseService):
    model_class: Comment = Comment
    schema_class_in: CommentIn = CommentIn 
    schema_class_out: CommentOut = CommentOut


class PostService(BaseService):
    model_class: Post = Post
    schema_class_in: PostlIn = PostlIn
    schema_class_out: PostOut = PostOut


class PageService(BaseService):
    model_class: Page = Page
    schema_class_in: PageIn = PageIn
    schema_class_out: PageOut = PageOut
