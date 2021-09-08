from typing import Dict, List, Optional

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.sql import select, delete, update, insert
from sqlalchemy.orm import Mapper
from pydantic import BaseModel

from src.config.database import database


class DAO:
    """
    DEFAULT DATA ACESS OBJECT
    """

    model_class: DeclarativeMeta
    model_mapper: Mapper
    pk_attr: str = 'id'
    has_nested_relationships: bool = False

    def __init__(self, model_class: DeclarativeMeta, pk_attr: str = 'id'):
        self.model_class = model_class
        self.pk_attr = pk_attr
        self.model_mapper = self.model_class.__mapper__
        self.has_nested_relationships = self.model_mapper.relationships

    async def paginate(self, skip: int = 0, limit: int = 100) -> List[Dict]:
        """ Paginate """
        if self.has_nested_relationships:
            return await self._paginate_nested_relations(skip,limit)
        return await self._paginate_simple(skip,limit)

    async def _paginate_simple(self, skip: int = 0, limit: int = 100) -> List[Dict]:
        """ Paginate no relationships """
        query = select([self.model_class]).offset(skip).limit(limit)
        return await database.fetch_all(query)

    async def _paginate_nested_relations(self, skip: int = 0, limit: int = 100) -> List[Dict]:
        """ Paginate no relationships """
        subqueries = []
        nested_rel = {}
        for key, column in self.model_mapper.relationships.items():
            print(column)
            subquery_model = column.argument()
            subquery_columns = subquery_model.__table__.columns.keys()
            subquery_selected_columns = [ getattr(subquery_model, col).label(f'{key}.{col}')\
                                         for col in subquery_columns]
            nested_rel[key] = subquery_columns
            subqueries.append(select(subquery_selected_columns).where(column.primaryjoin).lateral())
        query = select([self.model_class, *subqueries]).offset(skip).limit(limit)

        result = []
        async for row in database.iterate(query=query):
            result.append({**row, **{key: {col: row.get(f'{key}.{col}', None) for col in columns}\
                                     for key, columns  in nested_rel.items()}})
        return result

    async def find_one(self, pk_param: int) -> Optional[Dict]:
        """ Find one """
        if self.has_nested_relationships:
            return await self._fetch_one_nested_relations(pk_param)
        return await self._fetch_one_simple(pk_param)

    async def _fetch_one_simple(self, pk_param: int) -> Optional[Dict]:
        """ Fetch no relationships """
        query = select([self.model_class])\
            .where(pk_param == getattr(self.model_class, self.pk_attr))
        return await database.fetch_one(query)

    async def _fetch_one_nested_relations(self, pk_param: int) -> Optional[Dict]:
        """ Paginate no relationships """
        subqueries = []
        nested_rel = {}
        for key, column in self.model_mapper.relationships.items():
            subquery_model = column.argument()
            subquery_columns = subquery_model.__table__.columns.keys()
            subquery_selected_columns = [ getattr(subquery_model, col).label(f'{key}.{col}')\
                                         for col in subquery_columns]
            nested_rel[key] = subquery_columns
            subqueries.append(select(subquery_selected_columns).where(column.primaryjoin).lateral())
        query = select([self.model_class, *subqueries])\
            .where(pk_param == getattr(self.model_class, self.pk_attr))
        row = await database.fetch_one(query=query)
        return { **row, **{ key: { col: row.get(f'{key}.{col}', None) for col in columns }\
                           for key, columns  in nested_rel.items()}}

    async def delete_one(self, pk_param: int) -> bool:
        """ delete one """
        query = (
            delete(self.model_class)
            .where(pk_param == getattr(self.model_class, self.pk_attr))
            .returning(getattr(self.model_class, self.pk_attr))
        )
        record_id = await database.execute(query)
        if record_id == pk_param:
            return True
        return False

    async def update_one(self, obj: BaseModel, pk_param: int) -> Optional[Dict]:
        """ Update one """
        query = (
            update(self.model_class)
            .where(pk_param == getattr(self.model_class, self.pk_attr))\
            .values(obj.dict())
            .returning(getattr(self.model_class, self.pk_attr))
        )
        record_id = await database.execute(query)
        if record_id == pk_param:
            return {**obj.dict(), self.pk_attr: pk_param}

    async def insert_one(self, obj: BaseModel) -> Optional[Dict]:
        """ Create a classe section """
        query = (
            insert(self.model_class)
            .values(obj.dict())
            .returning(getattr(self.model_class, self.pk_attr))
        )
        last_record_id = await database.execute(query)
        if last_record_id:
            return {**obj.dict(), self.pk_attr: last_record_id}
