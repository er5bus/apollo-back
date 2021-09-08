"""
Generic REST recources
"""
import enum

from typing import List, Tuple
from fastapi import APIRouter, status, Response
from pydantic import BaseModel

from src.services.base_service import BaseService


class Method(enum.Enum):
    """
    HTTP method
    """
    POST = 1
    GET = 2
    PUT = 3
    DELETE = 4


default_collection_router = (Method.GET, Method.POST)
default_document_router = (Method.GET, Method.PUT, Method.DELETE)


def include_generic_collection_document_router(router: APIRouter, service_obj: BaseService,
            include_document_routers:Tuple[int]=default_document_router,
            include_collection_routers: Tuple[int]=default_collection_router):
    """
    Generic resources to handle list and single of records
    """
    include_generic_collection_router(router, service_obj, include_collection_routers)
    include_generic_document_router(router, service_obj, include_document_routers)


def include_generic_collection_router(router: APIRouter, service_obj: BaseService,
                                            include_routers: Tuple[int]=default_collection_router):
    """
    Generic collection resources to handle list of record
    """

    # generic schema type
    SchemaClassOut = service_obj.schema_class_out
    SchemaClassIn = service_obj.schema_class_in

    if Method.GET in include_routers:
        @router.get("", response_model=List[SchemaClassOut], status_code=status.HTTP_200_OK)
        async def paginate(skip: int = 0, limit: int = 100):
            """ Get all Objects """
            return await service_obj.paginate(skip, limit)

    if Method.POST in include_routers:
        @router.post("", response_model=SchemaClassOut, status_code=status.HTTP_200_OK)
        async def insert_one(obj: SchemaClassIn):
            """ Create a classe section """
            return await service_obj.insert_one(obj)


def include_generic_document_router(router: APIRouter, service_obj: BaseService,
                                        include_routers: Tuple[int] = default_document_router):
    """
    Generic document resources to handle single record
    """

    # generic schema type
    SchemaClassOut = service_obj.schema_class_out
    SchemaClassIn = service_obj.schema_class_in

    if Method.GET in include_routers:
        @router.get("/{param_id}", response_model=SchemaClassOut, status_code=status.HTTP_200_OK)
        async def find_one(param_id: int):
            """ Get one obj """
            return await service_obj.find_one(param_id)

    if Method.DELETE in include_routers:
        @router.delete("/{param_id}", response_class=Response,
                       status_code=status.HTTP_204_NO_CONTENT)
        async def delete_one(param_id: int):
            """ Get one section """
            await service_obj.delete_one(param_id)

    if Method.PUT in include_routers:
        @router.put("/{param_id}", response_model=SchemaClassOut, status_code=status.HTTP_200_OK)
        async def update_one(param_id: int, obj: SchemaClassIn):
            """ Update one section """
            return await service_obj.update_one(obj, param_id)
