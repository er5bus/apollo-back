from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


from src.config.db import Base


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    subject = Column(String)


class CourseSection(Base):
    __tablename__ = 'course_section'
    id = Column(Integer, primary_key=True)

    order = Column(Integer)
    title = Column(String)
    body = Column(Text)

    course_id = Column(Integer(), ForeignKey('courses.id'))
    course = relationship('Course', foreign_keys=[course_id], backref='course_sections')

    author_id = Column(Integer(), ForeignKey('users.id'))

