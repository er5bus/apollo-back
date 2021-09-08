from src.models.quizzes import Quiz
from sqlalchemy.sql.sqltypes import DateTime
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class QuizIn(BaseModel):
    name : str
    description : str

class QuizOut(QuizIn):
    id: int


class QuestionIn(BaseModel):
    name : str
    description : str
    quiz_id : int

class QuestionOut(BaseModel):
    id: int
    name : str
    description : str
    Quiz : Optional[QuizOut] = None


class AnswerIn(BaseModel):
    name : str
    is_the_correct_anwser : bool

class AnswerOut(AnswerIn):
    id: int


class QuizCompletedIn(BaseModel):

    timestamp : Optional[datetime]=None
    user_id : int

class QuizCompletedOut(BaseModel):
    id: int
    timestamp : Optional[datetime]=None
      

class QuestionAnswerIn(BaseModel):

    timestamp : Optional[datetime]=None
    question_id : int
    answer_id : int
    quiz_id : int
    quiz_completed_id : int

class QuestionAnswerOut(BaseModel):
    id: int
    quiz_completed : Optional[QuizCompletedOut] = None



    class Config:
        orm_mode = True