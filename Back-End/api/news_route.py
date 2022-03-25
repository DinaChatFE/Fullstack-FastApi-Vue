import typing
from datetime import datetime
from typing import List
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from crud import user_crud, news_crud
from starlette.requests import Request
import models
import schemas
from schemas.news_schema import NewsWithOwner, UpdateNewsSchema, CreateNewsSchema
from dependencies import common_parameters
from database import db_session
from core.upload_instance import upload_base64

news_router = APIRouter(prefix="/news", tags=["news"])


@news_router.get('/', response_model=schemas.NewsPaginate)
async def read_data(request: Request, commons: dict = Depends(common_parameters)):
    with request.pony_session:
        page = commons['page']
        page_size = commons['page_size']
        order = commons['order']
        order_by = commons['order_by']

        request_args = dict(request.query_params)
        user = request_args.get('user', '')
        offset = (page - 1) * page_size
        query = news_crud.query_and_equal_dict(request, request_args=request_args,
                                               add_some_extra=f'ORDER BY {order_by} {order} '
                                                              f'LIMIT {page_size} OFFSET {offset}')
        # if user: get_user_email = user_crud.get_credential_by_token(user)

        data_news_preference = []
        for q in query['data']:
            obj = q
            obj.is_interested = False
            if 'user' in request.query_params.keys():
                for i in q.interested:
                    pass
                    # if i.email == get_user_email:
                    #     obj.is_interested = True

            data_news_preference.append(obj)

        return schemas.NewsPaginate(current_page=page, page_count=query['count'], data=data_news_preference)


@news_router.get('/by-categories')  # , response_model=List[NewsWithOwner]
def read_by_categories(request: Request, cat_id: int, page: typing.Optional[int] = 1, page_size: typing.Optional[int] = 12):
    with db_session:
        query = news_crud.get_by_categories(categories=cat_id, page=page, pagesize=page_size)
        list_events = query['data']
        count_page = query['count']
        result = [NewsWithOwner.from_orm(p) for p in list_events]
        return schemas.NewsPaginate(current_page=page, page_count=count_page, data=result)


@news_router.get('/by-user')
def read_by_categories(request: Request, user_id: int, page: typing.Optional[int] = 1, page_size: typing.Optional[int] = 12):
    with db_session:
        query = news_crud.get_by_users(user=user_id, page=page, pagesize=page_size)
        list_events = query['data']
        count_page = query['count']
        result = [NewsWithOwner.from_orm(p) for p in list_events]
        return schemas.NewsPaginate(current_page=page, page_count=count_page, data=result)


@news_router.get('/own', response_model=List[NewsWithOwner])
async def read_own_data(request: Request, current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        return list(news_crud.get_own_data(user=current_user))


@news_router.get('/{news_id}', response_model=NewsWithOwner)
async def read_one_data(news_id: int, request: Request):
    with request.pony_session:
        response = news_crud.get(id=news_id)
        if not response:
            raise HTTPException(status_code=404, detail="Event couldn't match the record")
        return response


@news_router.post('/', response_model=NewsWithOwner)
async def write_data(schema: CreateNewsSchema,
                     request: Request,
                     current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        return news_crud.create_with_owner(created_by=current_user, obj_in=schema)


'''delete event belong user login'''


@news_router.delete('/{news_id}')
async def delete_data(news_id: int, request: Request, force: typing.Optional[bool] = True,
                      current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        obj = news_crud.get_force_entry(id=news_id)

        if not obj:
            raise HTTPException(status_code=404, detail="Couldn't found a record")
        if obj.created_by.id != current_user.id:
            raise HTTPException(status_code=403, detail="Unfortunately, you attempt to edit items not belongs to you")
        if (not news_crud.soft_delete(id=news_id)) and not force:
            raise HTTPException(status_code=404, detail="Can't delete, make sure the id provided is correct")
        if force:
            news_crud.remove(id=news_id)
            return {"message": "Record has been delete, you couldn't recover it later"}
        return {"message": "Record has been delete, you can recover it some days"}


'''update event belong to user login'''


@news_router.put("/{news_id}", response_model=NewsWithOwner)
async def update_data(news_id: int, schema: UpdateNewsSchema, request: Request,
                      current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        obj = news_crud.get(id=news_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Couldn't found any resource")
        if obj.created_by.id != current_user.id:
            raise HTTPException(status_code=403, detail="Unfortunately, you attempt to edit items not belongs to you")
        # remove category and re-create
        for c in list(obj.categories):
            obj.categories.remove(c)

        obj.flush()
        for i in schema.categories:
            obj.categories.add(models.Category[i])
        # update column updated at
        schema.thumbnail = upload_base64.upload_image_base64(schema.thumbnail)
        obj.updated_at = datetime.now()
        del schema.categories
        return news_crud.update(db_obj=obj, obj_in=schema)


@news_router.post('/restore/{news_id}')
async def restore_data(news_id: int, request: Request, current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        obj = news_crud.get_force_entry(id=news_id)
        # if obj couldn't found or delete is not soft, raise some errors
        if obj.created_by.id != current_user.id:
            raise HTTPException(status_code=403, detail="Unfortunately, you attempt to edit items not belongs to you")
        if not obj or (obj.deleted_at is None):
            raise HTTPException(status_code=404, detail="Couldn't found any record to proceed restore operations")
        # otherwise continue to proceed operations
        news_crud.restore(id=news_id)
        return {"message": "Record has been restored"}


@news_router.get('/preference/{news_id}')
async def post_preference(news_id: int, request: Request, is_interested: bool = True,
                          current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        if not news_crud.post_preference(news_id=news_id, user_id=current_user.id, is_interested=is_interested):
            raise HTTPException(status_code=404, detail="Didn't found any record")
        return {"message": "event has been stored preference record"}
