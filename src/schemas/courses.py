from pydantic import BaseModel
from typing import Optional


class CourseIn(BaseModel):
    name : str
    subject : str


class CourseOut(CourseIn):
    id: int

class CourseSectionIn(BaseModel):
    order : str
    title : str
    body : str
    course_id : int
    author_id : int


class CourseSectionOut(BaseModel):
    id: int
    order : str
    title : str
    body : str
    course : Optional[CourseOut] = None


    class Config:
        orm_mode = True
