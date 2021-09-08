from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


from src.config.database import Base


class Quiz(Base):
    __tablename__ = 'quizes'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(Text)


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(Text)

    quiz_id = Column(Integer(), ForeignKey('quizes.id'))
    quiz = relationship('Quiz', foreign_keys=[quiz_id], backref='questions')


class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    is_the_correct_anwser = Column(Boolean)


class QuestionAnswer(Base):
    __tablename__ = 'question_and_answer'
    id = Column(Integer, primary_key=True)

    timestamp = Column(DateTime, default=datetime.utcnow())
    question_id = Column(Integer(), ForeignKey('questions.id'))
    answer_id = Column(Integer(), ForeignKey('answers.id'))
    quiz_id = Column(Integer(), ForeignKey('quizes.id'))

    quiz_completed_id = Column(Integer(), ForeignKey('quizes_completed.id'))
    quiz_completed = relationship('QuizCompleted', foreign_keys=[quiz_completed_id], backref='questions_and_answers')


class QuizCompleted(Base):
    __tablename__ = 'quizes_completed'
    id = Column(Integer, primary_key=True)

    timestamp = Column(DateTime, default=datetime.utcnow())
    user_id = Column(Integer(), ForeignKey('users.id'))
