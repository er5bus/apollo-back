from typing import List
from fastapi import APIRouter, status, Response

from src.config.db import database
from ..models.courses import Course, CourseSection
from ..schemas.courses import CourseIn, CourseOut, CourseSectionIn, CourseSectionOut

from ..utils.crud import (paginate, find_one, update_one, insert_one, delete_one)


courses_router = APIRouter(prefix="/api/courses", tags=["Course"])

courses_section_router = APIRouter(prefix="/api/courses_section", tags=["courses_section"])


@courses_router.get("", response_model=List[CourseOut], status_code=status.HTTP_200_OK)
async def read_sections(skip: int = 0, limit: int = 100):
    """ Get all courses """
    return await paginate(Course, skip, limit)


@courses_router.get("/{course_id}", response_model=CourseOut, status_code=status.HTTP_200_OK)
async def read_section(course_id: int):
    """ Get one course """
    return await find_one(Course, course_id)


@courses_router.delete("/{course_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_section(course_id: int):
    """ Get one course """
    await delete_one(Course, course_id)


@courses_router.put("/{course_id}", response_model=CourseOut, status_code=status.HTTP_200_OK)
async def update_section(course_id: int, section: CourseIn):
    """ Update one course """
    return await update_one(Course, section, course_id)


@courses_router.post("", response_model=CourseOut, status_code=status.HTTP_200_OK)
async def create_section(course: CourseIn):
    """ Create a classe course """
    return await insert_one(Course, course)


@courses_section_router.get("", response_model=List[CourseSectionOut], status_code=status.HTTP_200_OK)
async def read_classes(skip: int = 0, limit: int = 100):
    """ Get all courses section """
    return await paginate(CourseSection, skip, limit)


@courses_section_router.get("/{course_section_id}", response_model=CourseSectionOut, status_code=status.HTTP_200_OK)
async def read_classe(course_section_id: int):
    """ Get one course section """
    return await find_one(CourseSection, course_section_id)


@courses_section_router.delete("/{course_section_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_classe(course_section_id: int):
    """ Get one course section """
    await delete_one(CourseSection, course_section_id)


@courses_section_router.put("/{course_section_id}", response_model=CourseSectionOut, status_code=status.HTTP_200_OK)
async def update_classe(course_section_id: int, course_section: CourseSectionIn):
    """ Update one course section """
    return await update_one(CourseSection, course_section, course_section_id)


@courses_section_router.post("", response_model=CourseSectionOut, status_code=status.HTTP_200_OK)
async def create_classe(course_section: CourseSectionIn):
    """ Create a classe course section """
    return await insert_one(CourseSection, course_section)
