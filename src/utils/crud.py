from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.sql import select, delete, update, insert
from sqlalchemy.orm import class_mapper, RelationshipProperty, Mapper
from sqlalchemy import inspect
from pydantic import BaseModel

from src.config.db import database


async def paginate(model: DeclarativeMeta, skip: int = 0, limit: int = 100):
    """ Paginate """
    model_mapper = class_mapper(model)
    if model_mapper.relationships:
        return await _paginate_nested_relations(model, model_mapper, skip,limit)
    return await _paginate_simple(model, skip,limit)


async def _paginate_simple(model: DeclarativeMeta, skip: int = 0, limit: int = 100):
    """ Paginate no relationships """
    query = select([model]).offset(skip).limit(limit)
    return await database.fetch_all(query)


async def _paginate_nested_relations(model: DeclarativeMeta, model_mapper: Mapper, skip: int = 0, limit: int = 100):
    """ Paginate no relationships """ 
    subqueries = []
    nested_rel = {}
    for key, column in model_mapper.relationships.items():
        subquery_model = column.argument()
        subquery_columns = subquery_model.__table__.columns.keys()
        subquery_selected_columns = [ getattr(subquery_model, col).label(f'{key}.{col}') for col in subquery_columns]
        nested_rel[key] = subquery_columns
        subqueries.append(select(subquery_selected_columns).where(column.primaryjoin).lateral())
    query = select([model, *subqueries]).offset(skip).limit(limit)

    result = []
    async for row in database.iterate(query=query):
        result.append({ **row, **{ key: { col: row.get(f'{key}.{col}', None) for col in columns } for key, columns  in nested_rel.items()}})
    return result



async def find_one(model: DeclarativeMeta, pk_param: int, pk_attr: str = 'id'):
    """ Find one """
    model_mapper = class_mapper(model)
    if model_mapper.relationships:
        return await _fetch_one_nested_relations(model, model_mapper, pk_param, pk_attr)
    return await _fetch_one_simple(model, pk_param, pk_attr)


async def _fetch_one_simple(model: DeclarativeMeta, pk_param: int, pk_attr: str = 'id'):
    """ Fetch no relationships """
    query = select([model]).where(pk_param == getattr(model, pk_attr))
    return await database.fetch_one(query)


async def _fetch_one_nested_relations(model: DeclarativeMeta, model_mapper: Mapper, pk_param: int, pk_attr: str = 'id'):
    """ Paginate no relationships """
    subqueries = []
    nested_rel = {}
    for key, column in model_mapper.relationships.items():
        subquery_model = column.argument()
        subquery_columns = subquery_model.__table__.columns.keys()
        subquery_selected_columns = [ getattr(subquery_model, col).label(f'{key}.{col}') for col in subquery_columns]
        nested_rel[key] = subquery_columns
        subqueries.append(select(subquery_selected_columns).where(column.primaryjoin).lateral())
    query = select([model, *subqueries]).where(pk_param == getattr(model, pk_attr))
    row = await database.fetch_one(query=query)
    return { **row, **{ key: { col: row.get(f'{key}.{col}', None) for col in columns } for key, columns  in nested_rel.items()}}


async def delete_one(model: DeclarativeMeta, pk_param: int, pk_attr: str = 'id'):
    """ delete one """
    query = delete(model).where(pk_param == getattr(model, pk_attr))
    await database.execute(query)


async def update_one(model: DeclarativeMeta, obj: BaseModel, pk_param: int, pk_attr: str = 'id'):
    """ Update one """
    query = update(model).where(pk_param == getattr(model, pk_attr)).values(obj.dict())
    await database.execute(query)
    return {**obj.dict(), pk_attr: pk_param}


async def insert_one(model: DeclarativeMeta, obj: BaseModel, pk_attr: str = 'id'):
    """ Create a classe section """
    query = insert(model).values(obj.dict())
    last_record_id = await database.execute(query)
    return {**obj.dict(), pk_attr: last_record_id}
