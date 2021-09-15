from fastapi import APIRouter, Depends
from typing import List

from src.utils.crud_router import include_generic_collection_document_router
from src.dependencies import current_active_user
from src.services.quizzes import QuizService, QuizCompletedService, QuestionService, AnswerService, QuestionAnswerService


dependencies: List[Depends] = [Depends(current_active_user)]


quiz_service: QuizService = QuizService()
quiz_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/quizzes", tags=["Quiz"])
include_generic_collection_document_router(quiz_router, quiz_service)


quiz_completed_service: QuizCompletedService = QuizCompletedService()
quiz_completed_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/quizzes-completed", tags=["QuizCompleted"])
include_generic_collection_document_router(quiz_completed_router, quiz_completed_service)


question_service: QuestionService = QuestionService()
question_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/questions", tags=["Question"])
include_generic_collection_document_router(question_router, question_service)


answer_service: AnswerService = AnswerService()
answer_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/answers", tags=["Answer"])
include_generic_collection_document_router(answer_router, answer_service)


question_answer_service: QuestionAnswerService = QuestionAnswerService()
question_answer_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/question-answer", tags=["QuestionAnswer"])
include_generic_collection_document_router(question_answer_router, question_answer_service)
