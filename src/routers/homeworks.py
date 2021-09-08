from typing import List
from fastapi import APIRouter, status, Response

from src.config.db import database
from ..models.homeworks import Homework, HomeworkCompleted
from ..schemas.homeworks import HomeworkIn, HomeworkOut, HomeworkCompletedIn, HomeworkCompletednOut

from ..utils.crud import (paginate, find_one, update_one, insert_one, delete_one)


homeworks_router = APIRouter(prefix="/api/homeworks", tags=["homeworks"])

homeworks_completed_router = APIRouter(prefix="/api/homeworks_completed", tags=["homeworks_completed"])


@homeworks_router.get("", response_model=List[HomeworkOut], status_code=status.HTTP_200_OK)
async def read_sections(skip: int = 0, limit: int = 100):
    """ Get all homeworks """
    return await paginate(Homework, skip, limit)


@homeworks_router.get("/{homework_id}", response_model=HomeworkOut, status_code=status.HTTP_200_OK)
async def read_section(homework_id: int):
    """ Get one homework """
    return await find_one(Homework, homework_id)


@homeworks_router.delete("/{homework_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_section(homework_id: int):
    """ Get one homework """
    await delete_one(Homework, homework_id)


@homeworks_router.put("/{homework_id}", response_model=HomeworkOut, status_code=status.HTTP_200_OK)
async def update_section(homework_id: int, homework: HomeworkIn):
    """ Update one homework """
    return await update_one(Homework, homework, homework_id)


@homeworks_router.post("", response_model=HomeworkOut, status_code=status.HTTP_200_OK)
async def create_section(homework: HomeworkIn):
    """ Create a classe homework """
    return await insert_one(Homework, homework)


@homeworks_completed_router.get("", response_model=List[HomeworkCompletednOut], status_code=status.HTTP_200_OK)
async def read_classes(skip: int = 0, limit: int = 100):
    """ Get all homeworks completed """
    return await paginate(HomeworkCompleted, skip, limit)


@homeworks_completed_router.get("/{homeworks_completed_id}", response_model=HomeworkCompletednOut, status_code=status.HTTP_200_OK)
async def read_classe(homeworks_completed_id: int):
    """ Get one homework completed """
    return await find_one(HomeworkCompleted, homeworks_completed_id)


@homeworks_completed_router.delete("/{homeworks_completed_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_classe(homeworks_completed_id: int):
    """ Get one homework completed """
    await delete_one(HomeworkCompleted, homeworks_completed_id)


@homeworks_completed_router.put("/{course_section_id}", response_model=HomeworkCompletednOut, status_code=status.HTTP_200_OK)
async def update_classe(homeworks_completed_id: int, homeworks_completed: HomeworkCompletedIn):
    """ Update one homework completed """
    return await update_one(HomeworkCompleted, homeworks_completed, homeworks_completed_id)


@homeworks_completed_router.post("", response_model=HomeworkCompletednOut, status_code=status.HTTP_200_OK)
async def create_classe(homeworks_completed: HomeworkCompletedIn):
    """ Create a classe homework completed """
    return await insert_one(HomeworkCompleted, homeworks_completed)
