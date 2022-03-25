from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pony.orm.core import commit
from pony.orm import *
from core import settings

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
        # self.soft is attribute to predefine if table is has soft delete or not
        self.soft = hasattr(self.model, 'deleted_at')
        self.setting = settings

    def get(self, id: Any):
        return self.model.get(id=id, deleted_at=None)

    # get all from tables, although it has been soft delete
    def get_force_entry(self, id: Any):
        return self.model.get(id=id)

    def get_multi(self,
                  *,
                  page: int = 1,
                  with_offset=False,
                  page_size: int = 10):
        query = self.model.select(lambda x: x.deleted_at is None)
        if with_offset:
            return query.limit(page_size, offset=page_size * page)
        return query.page(page, pagesize=page_size)

    def scope_get_multi(self):
        return self.model.select(lambda x: (x.deleted_at is None))

    def create(self, *, obj_in: CreateSchemaType):

        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        commit()
        db_obj.flush()

        return db_obj

    def update(self, db_obj: ModelType,
               obj_in: Union[UpdateSchemaType, Dict[str, Any]]):

        db_obj.set(**obj_in.dict())
        self.model.set(db_obj)
        commit()
        db_obj.flush()
        return db_obj

    def remove(self, *, id: int):
        self.model[id].delete()
        commit()
        return True

    def has_soft_delete(self):
        return self.soft

    def soft_delete(self, id: int):
        obj = self.get_force_entry(id=id)
        if not self.has_soft_delete() or (obj.deleted_at is not None):
            return False
        self.model.get(id=id).set(
            deleted_at=datetime.now())
        commit()
        return True

    def restore(self, id: int):

        obj = self.get_force_entry(id=id)
        if not self.has_soft_delete() or (obj.deleted_at is None):
            return False
        self.model[id].set(deleted_at=None)
        commit()

        return True

    def page_count(self):
        return self.model.select(lambda x: x.deleted_at is None).count()

    def clean_default_params(self, request_args, request):
        for params in self.setting.DEFAULT_PARAMS_USE:
            if params in request.query_params.keys(): request_args.pop(params)

    def query_and_equal_dict(self, request, request_args, add_some_extra='', count=False):
        # remove default params out of sql query
        if not count: self.clean_default_params(request_args, request)
        table_name = self.model._table_
        sql_command = f"SELECT * FROM {table_name} "
        if len(request_args) > 0:
            sql_command += "WHERE "

        for k, key in enumerate(request_args):
            value = request_args[key]
            sql_command += f"{key}='{value}'"
            if k is not (len(request_args) - 1):
                sql_command += " AND "

        # sql_command += " AND WHERE deleted_at IS NULL "
        before_len = len(self.model.select_by_sql(sql_command))
        sql_command += add_some_extra
        query = self.model.select_by_sql(sql_command)

        return {'data': query, 'count': before_len}
