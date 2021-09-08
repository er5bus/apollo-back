import time

from typing import Any, List, Dict
from fastapi import Depends, APIRouter, status, Response
from sqlalchemy.ext.declarative import DeclarativeMeta
from pydantic import BaseModel

from src.schemas.users import UserOut as User
from src.dependencies import current_active_user
from src.utils.dao import DAO


def rest_api_router(dao_obj: DAO, **kwargs: Dict[str, Any]):
    """
    Default methods for rest endpoint
    """

    router: APIRouter = APIRouter(dependencies=[Depends(current_active_user)], **kwargs)

    print(vars(router))

    # generic schema type
    SchemaClassOut = dao_obj.schema_class_out
    SchemaClassIn = dao_obj.schema_class_in

    @router.get("", response_model=List[SchemaClassOut], status_code=status.HTTP_200_OK)
    async def paginate(skip: int = 0, limit: int = 100):
        """ Get all Objects """
        return await dao_obj.paginate(skip, limit)


    @router.get("/{param_id}", response_model=SchemaClassOut, status_code=status.HTTP_200_OK)
    async def find_one(param_id: int):
        """ Get one obj """
        return await dao_obj.find_one(param_id)


    @router.delete("/{param_id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
    async def delete_one(param_id: int):
        """ Get one section """
        await dao_obj.delete_one(param_id)


    @router.put("/{param_id}", response_model=SchemaClassOut, status_code=status.HTTP_200_OK)
    async def update_one(param_id: int, obj: SchemaClassIn):
        """ Update one section """
        return await dao_obj.update_one(obj, param_id)


    @router.post("", response_model=SchemaClassOut, status_code=status.HTTP_200_OK)
    async def insert_one(obj: SchemaClassIn):
        """ Create a classe section """
        return await dao_obj.insert_one(model_class, obj)


    return router
