from fastapi import APIRouter, Depends
from typing import List

from src.utils.crud_router import include_generic_collection_document_router
from src.dependencies import current_active_user
from src.services.classes import SectionService, LevelService, ClasseService


dependencies: List[Depends] = [Depends(current_active_user)]


section_service: SectionService = SectionService()
section_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/sections", tags=["Section"])
include_generic_collection_document_router(section_router, section_service)


classe_service: ClasseService = ClasseService()
classe_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/classes", tags=["Classe"])
include_generic_collection_document_router(classe_router, classe_service)


level_service: LevelService = LevelService()
level_router: APIRouter = APIRouter(dependencies=dependencies,
                              prefix="/api/levels", tags=["Level"])
include_generic_collection_document_router(level_router, level_service)
