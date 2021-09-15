from .base_service import BaseService

from ..models.courses import Course, CourseSection
from ..schemas.courses import CourseIn, CourseOut, CourseSectionIn, CourseSectionOut


class CourseService(BaseService):
    model_class: Course = Course
    schema_class_in: CourseIn = CourseIn
    schema_class_out: CourseOut = CourseOut


class CourseSectionService(BaseService):
    model_class: CourseSection = CourseSection
    schema_class_in: CourseSectionIn = CourseSectionIn
    schema_class_out: CourseSectionOut = CourseSectionOut


