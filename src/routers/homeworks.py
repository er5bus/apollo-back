from fastapi import APIRouter, Depends
from typing import List

from src.utils.crud_router import include_generic_collection_document_router
from src.dependencies import current_active_user
from src.services.homeworks import HomeworkService, HomeworkCompletedService

dependencies: List[Depends] = [Depends(current_active_user)]


homework_service: HomeworkService = HomeworkService()
homework_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/homeworks", tags=["Homework"])
include_generic_collection_document_router(homework_router, homework_service)


homework_completed_service: HomeworkCompletedService = HomeworkCompletedService()
homework_completed_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/homeworks-completed", tags=["HomeworkCompleted"])
include_generic_collection_document_router(homework_completed_router, homework_completed_service)

