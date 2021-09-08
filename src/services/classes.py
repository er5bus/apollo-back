from .base_service import BaseService

from src.schemas.classes import ClasseOut, ClasseIn, SectionIn, SectionOut, LevelOut, LevelIn
from src.models.classes import Section, Level, Classe


class SectionService(BaseService):
    model_class: Section = Section
    schema_class_in: SectionIn = SectionIn
    schema_class_out: SectionOut = SectionOut


class LevelService(BaseService):
    model_class: Level = Level
    schema_class_in: LevelIn = LevelIn
    schema_class_out: LevelOut = LevelOut


class ClasseService(BaseService):
    model_class: Classe = Classe
    schema_class_in: ClasseIn = ClasseIn
    schema_class_out: ClasseOut = ClasseOut
