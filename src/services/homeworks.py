from .base_service import BaseService

from ..models.homeworks import Homework, HomeworkCompleted
from ..schemas.homeworks import HomeworkIn, HomeworkOut, HomeworkCompletedIn, HomeworkCompletednOut

class HomeworkService(BaseService):
    model_class: Homework = Homework
    schema_class_in: HomeworkIn = HomeworkIn
    schema_class_out: HomeworkOut = HomeworkOut


class HomeworkCompletedService(BaseService):
    model_class: HomeworkCompleted = HomeworkCompleted
    schema_class_in: HomeworkCompletedIn = HomeworkCompletedIn
    schema_class_out: HomeworkCompletednOut = HomeworkCompletednOut


