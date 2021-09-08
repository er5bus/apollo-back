from pydantic import BaseModel
from typing import Optional


class SectionIn(BaseModel):
    name: str


class SectionOut(SectionIn):
    id: int


class LevelIn(BaseModel):
    name: str


class LevelOut(SectionIn):
    id: int


class ClasseIn(BaseModel):
    name: str
    section_id: int
    level_id: int
    description: Optional[str] = None


class ClasseOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    section: Optional[SectionOut] = None
    level: Optional[LevelOut] = None

    class Config:
        orm_mode = True
