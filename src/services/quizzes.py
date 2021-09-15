from .base_service import BaseService

from ..models.quizzes import Quiz, QuizCompleted, Question ,Answer,QuestionAnswer
from ..schemas.quizzes import QuizIn, QuizOut, QuizCompletedIn, QuizCompletedOut, QuestionIn, QuestionOut, AnswerIn, AnswerOut, QuestionAnswerIn, QuestionAnswerOut

class QuizService(BaseService):
    model_class: Quiz = Quiz
    schema_class_in: QuizIn = QuizIn
    schema_class_out: QuizOut = QuizOut


class QuizCompletedService(BaseService):
    model_class: QuizCompleted = QuizCompleted
    schema_class_in: QuizCompletedIn = QuizCompletedIn
    schema_class_out: QuizCompletedOut = QuizCompletedOut


class QuestionService(BaseService):
    model_class: Question = Question
    schema_class_in: QuestionIn = QuestionIn
    schema_class_out: QuestionOut = QuestionOut

class AnswerService(BaseService):
    model_class: Answer = Answer
    schema_class_in: AnswerIn = AnswerIn
    schema_class_out: AnswerOut = AnswerOut


class QuestionAnswerService(BaseService):
    model_class: QuestionAnswer = QuestionAnswer
    schema_class_in: QuestionAnswerIn = QuestionAnswerIn
    schema_class_out: QuestionAnswerOut = QuestionAnswerOut

