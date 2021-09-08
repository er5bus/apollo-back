from typing import List
from fastapi import APIRouter, status, Response

from src.config.db import database
from ..models.classes import Classe, Section, Level
from ..schemas.classes import ClasseOut, ClasseIn, SectionIn, SectionOut, LevelOut, LevelIn

from ..utils.crud import (paginate, find_one, update_one, insert_one, delete_one)


classe_router = APIRouter(prefix="/api/classes", tags=["Classe"])

section_router = APIRouter(prefix="/api/sections", tags=["Section"])

level_router = APIRouter(prefix="/api/levels", tags=["Level"])


@section_router.get("", response_model=List[SectionOut], status_code=status.HTTP_200_OK)
async def read_sections(skip: int = 0, limit: int = 100):
    """ Get all sections """
    return await paginate(Section, skip, limit)


@section_router.get("/{section_id}", response_model=SectionOut, status_code=status.HTTP_200_OK)
async def read_section(section_id: int):
    """ Get one section """
    return await find_one(Section, section_id)


@section_router.delete("/{section_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_section(section_id: int):
    """ Get one section """
    await delete_one(Section, section_id)


@section_router.put("/{section_id}", response_model=SectionOut, status_code=status.HTTP_200_OK)
async def update_section(section_id: int, section: SectionIn):
    """ Update one section """
    return await update_one(Section, section, section_id)


@section_router.post("", response_model=SectionOut, status_code=status.HTTP_200_OK)
async def create_section(section: SectionIn):
    """ Create a classe section """
    return await insert_one(Section, section)


@classe_router.get("", response_model=List[ClasseOut], status_code=status.HTTP_200_OK)
async def read_classes(skip: int = 0, limit: int = 100):
    """ Get all classes """
    return await paginate(Classe, skip, limit)


@classe_router.get("/{classe_id}", response_model=ClasseOut, status_code=status.HTTP_200_OK)
async def read_classe(classe_id: int):
    """ Get one classe """
    return await find_one(Classe, classe_id)


@classe_router.delete("/{classe_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_classe(classe_id: int):
    """ Get one classe """
    await delete_one(Classe, classe_id)


@classe_router.put("/{classe_id}", response_model=ClasseOut, status_code=status.HTTP_200_OK)
async def update_classe(classe_id: int, classe: ClasseIn):
    """ Update one classe """
    return await update_one(Classe, classe, classe_id)


@classe_router.post("", response_model=ClasseOut, status_code=status.HTTP_200_OK)
async def create_classe(classe: ClasseIn):
    """ Create a classe classe """
    return await insert_one(Classe, classe)


@level_router.get("", response_model=List[LevelOut], status_code=status.HTTP_200_OK)
async def read_levels(skip: int = 0, limit: int = 100):
    """ Get all levels """
    return await paginate(Level, skip, limit)


@level_router.get("/{level_id}", response_model=LevelOut, status_code=status.HTTP_200_OK)
async def read_level(level_id: int):
    """ Get one level """
    return await find_one(Level, level_id)


@level_router.delete("/{level_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_level(level_id: int):
    """ Get one level """
    await delete_one(Level, level_id)


@level_router.put("/{level_id}", response_model=LevelOut, status_code=status.HTTP_200_OK)
async def update_level(level_id: int, level: LevelIn):
    """ Update one level """
    return await update_one(Level, level, level_id)


@level_router.post("", response_model=LevelOut, status_code=status.HTTP_200_OK)
async def create_level(level: LevelIn):
    """ Create a classe level """
    return await insert_one(Level, level)
