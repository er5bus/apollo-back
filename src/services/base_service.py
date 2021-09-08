"""
Base Service class
"""
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Mapper
from pydantic import BaseModel

from src.utils.dao import DAO
from src.utils.exceptions import raise_not_found_exception, raise_unprocessable_entity_exception

class BaseService:
    """ Base service class """

    schema_class_out: BaseModel
    pk_attr: str = 'id'
    schema_class_in: BaseModel
    model_class: DeclarativeMeta
    model_mapper: Mapper

    def __init__(self):
        self.dao_obj = DAO(model_class=self.model_class, pk_attr=self.pk_attr)

    async def paginate(self, skip: int = 0, limit: int = 100):
        """ Get all Objects """
        return await self.dao_obj.paginate(skip, limit)

    async def find_one(self, param_id: int):
        """ Get one obj """
        obj = await self.dao_obj.find_one(param_id)
        if obj is None:
            raise_not_found_exception()
        return obj

    async def delete_one(self, param_id: int):
        """ Get one section """
        result = await self.dao_obj.delete_one(param_id)
        if result is False:
            raise_not_found_exception()

    async def update_one(self, obj: object, param_id: int):
        """ Update one section """
        result = await self.dao_obj.update_one(obj, param_id)
        if result is None:
            raise_not_found_exception()

    async def insert_one(self, obj: object):
        """ Create a classe section """
        result = await self.dao_obj.insert_one(obj)
        if result is None:
            raise_unprocessable_entity_exception()
