from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


from src.config.database import Base


class Homework(Base):
    __tablename__ = 'homeworks'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    subject = Column(Text)

    deadline = Column(DateTime)


class HomeworkCompleted(Base):
    __tablename__ = 'homeworks_completed'
    id = Column(Integer, primary_key=True)

    timestamp = Column(DateTime, default=datetime.utcnow())
    answer = Column(Text)
    deposit_date = Column(DateTime)

    homework_id = Column(Integer(), ForeignKey('homeworks.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))

