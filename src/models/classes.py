from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property



from src.config.db import Base


class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Level(Base):
    __tablename__ = 'levels'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Classe(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(String)

    section_id = Column(Integer(), ForeignKey('sections.id'))
    section = relationship('Section', foreign_keys=[section_id], lazy='joined', primaryjoin="Classe.section_id==Section.id", backref='classes')

    level_id = Column(Integer(), ForeignKey('levels.id'))
    level = relationship('Level', foreign_keys=[level_id], lazy='joined', primaryjoin="Classe.level_id==Level.id", backref='classes')

    #posts = relationship('Post', backref='classe', lazy='dynamic')
    #homeworks = relationship('Homework', backref='classe', lazy='dynamic')
    #quizes = relationship('Quiz', backref='classe', lazy='dynamic')
