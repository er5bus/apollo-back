from fastapi import APIRouter, Depends
from typing import List

from src.utils.crud_router import include_generic_collection_document_router
from src.dependencies import current_active_user
from src.services.courses import CourseService, CourseSectionService

dependencies: List[Depends] = [Depends(current_active_user)]


course_service: CourseService = CourseService()
course_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/courses", tags=["Course"])
include_generic_collection_document_router(course_router, course_service)


course_section_service: CourseSectionService = CourseSectionService()
course_section_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/course-section", tags=["CourseSection"])
include_generic_collection_document_router(course_section_router, course_section_service)
