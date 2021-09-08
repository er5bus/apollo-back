from typing import List
from fastapi import APIRouter, status, Response

from src.config.db import database
from ..models.quizzes import Quiz, QuizCompleted, Question ,Answer,QuestionAnswer
from ..schemas.quizzes import QuizIn, QuizOut, QuizCompletedIn, QuizCompletedOut, QuestionIn, QuestionOut, AnswerIn, AnswerOut, QuestionAnswerIn, QuestionAnswerOut

from ..utils.crud import (paginate, find_one, update_one, insert_one, delete_one)


quizzes_router = APIRouter(prefix="/api/quizzes", tags=["quizzes"])

quizzes_completed_router = APIRouter(prefix="/api/quizzes_completed", tags=["quizzes_completed"])

questions_router = APIRouter(prefix="/api/questions", tags=["questions"])

answers_router = APIRouter(prefix="/api/answers", tags=["answers"])

question_answer_router = APIRouter(prefix="/api/question_answer", tags=["question_answer"])


##############################################################     quizzes_router   ##################################################################################


@quizzes_router.get("", response_model=List[QuizOut], status_code=status.HTTP_200_OK)
async def read_sections(skip: int = 0, limit: int = 100):
    """ Get all quizzes """
    return await paginate(Quiz, skip, limit)


@quizzes_router.get("/{quiz_id}", response_model=QuizOut, status_code=status.HTTP_200_OK)
async def read_section(quiz_id: int):
    """ Get one quiz """
    return await find_one(Quiz, quiz_id)


@quizzes_router.delete("/{quiz_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_section(quiz_id: int):
    """ Get one quiz """
    await delete_one(Quiz, quiz_id)


@quizzes_router.put("/{quiz_id}", response_model=QuizOut, status_code=status.HTTP_200_OK)
async def update_section(quiz_id: int, quiz: QuizIn):
    """ Update one quiz """
    return await update_one(Quiz, quiz, quiz_id)


@quizzes_router.post("", response_model=QuizOut, status_code=status.HTTP_200_OK)
async def create_section(quiz: QuizIn):
    """ Create a classe quiz """
    return await insert_one(Quiz, quiz)


###########################################################       quizzes_completed_router    ###########################################################################


@quizzes_completed_router.get("", response_model=List[QuizCompletedOut], status_code=status.HTTP_200_OK)
async def read_classes(skip: int = 0, limit: int = 100):
    """ Get all quizzes completed """
    return await paginate(QuizCompleted, skip, limit)


@quizzes_completed_router.get("/{quiz_completed_id}", response_model=QuizCompletedOut, status_code=status.HTTP_200_OK)
async def read_classe(quiz_completed_id: int):
    """ Get one quiz completed """
    return await find_one(QuizCompleted, quiz_completed_id)


@quizzes_completed_router.delete("/{quiz_completed_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_classe(quiz_completed_id: int):
    """ Get one quiz completed """
    await delete_one(QuizCompleted, quiz_completed_id)


@quizzes_completed_router.put("/{quiz_completed_id}", response_model=QuizCompletedOut, status_code=status.HTTP_200_OK)
async def update_classe(quiz_completed_id: int, quiz_completed: QuizCompletedIn):
    """ Update one quiz completed """
    return await update_one(QuizCompleted, quiz_completed, quiz_completed_id)


@quizzes_completed_router.post("", response_model=QuizCompletedOut, status_code=status.HTTP_200_OK)
async def create_classe(quiz_completed: QuizCompletedIn):
    """ Create a classe quiz completed """
    return await insert_one(QuizCompleted, quiz_completed)


######################################################        questions_router         #############################################################################


@questions_router.get("", response_model=List[QuestionOut], status_code=status.HTTP_200_OK)
async def read_classes(skip: int = 0, limit: int = 100):
    """ Get all questions """
    return await paginate(Question, skip, limit)


@questions_router.get("/{question_id}", response_model=QuestionOut, status_code=status.HTTP_200_OK)
async def read_classe(question_id: int):
    """ Get one question """
    return await find_one(Question, question_id)


@questions_router.delete("/{question_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_classe(question_id: int):
    """ Get one question """
    await delete_one(Question, question_id)


@questions_router.put("/{question_id}", response_model=QuestionOut, status_code=status.HTTP_200_OK)
async def update_classe(question_id: int, question: QuestionIn):
    """ Update one question """
    return await update_one(Question, question, question_id)


@questions_router.post("", response_model=QuestionOut, status_code=status.HTTP_200_OK)
async def create_classe(question: QuestionIn):
    """ Create a classe question """
    return await insert_one(Question, question)


#######################################################        answers_router      #############################################################


@answers_router.get("", response_model=List[AnswerOut], status_code=status.HTTP_200_OK)
async def read_classes(skip: int = 0, limit: int = 100):
    """ Get all answers """
    return await paginate(Answer, skip, limit)


@answers_router.get("/{answer_id}", response_model=AnswerOut, status_code=status.HTTP_200_OK)
async def read_classe(answer_id: int):
    """ Get one answer """
    return await find_one(Answer, answer_id)


@answers_router.delete("/{answer_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_classe(answer_id: int):
    """ Get one answer """
    await delete_one(Answer, answer_id)


@answers_router.put("/{answer_id}", response_model=AnswerOut, status_code=status.HTTP_200_OK)
async def update_classe(answer_id: int, answer: AnswerIn):
    """ Update one answer """
    return await update_one(Answer, answer, answer_id)


@answers_router.post("", response_model=AnswerOut, status_code=status.HTTP_200_OK)
async def create_classe(answer: AnswerIn):
    """ Create a classe answer """
    return await insert_one(Answer, answer)


########################################################     question_answer_router      #######################################################


@question_answer_router.get("", response_model=List[QuestionAnswerOut], status_code=status.HTTP_200_OK)
async def read_classes(skip: int = 0, limit: int = 100):
    """ Get all quesion answers """
    return await paginate(QuestionAnswer, skip, limit)


@question_answer_router.get("/{question_answer_id}", response_model=QuestionAnswerOut, status_code=status.HTTP_200_OK)
async def read_classe(question_answer_id: int):
    """ Get one quesion answer """
    return await find_one(QuestionAnswer, question_answer_id)


@question_answer_router.delete("/{question_answer_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_classe(question_answer_id: int):
    """ Get one quesion answer """
    await delete_one(QuestionAnswer, question_answer_id)


@question_answer_router.put("/{question_answer_id}", response_model=QuestionAnswerOut, status_code=status.HTTP_200_OK)
async def update_classe(question_answer_id: int, answer: QuestionAnswerIn):
    """ Update one quesion answer """
    return await update_one(QuestionAnswer, answer, question_answer_id)


@question_answer_router.post("", response_model=QuestionAnswerOut, status_code=status.HTTP_200_OK)
async def create_classe(question_answer_id: QuestionAnswerIn):
    """ Create a classe quesion answer """
    return await insert_one(QuestionAnswer, question_answer_id)