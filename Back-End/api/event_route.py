from datetime import datetime
import typing
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends, Query
from pydantic.main import SchemaExtraCallable
from api.registration import check_in
import models
import schemas
from crud import user_crud, event_crud
from starlette.requests import Request
from schemas.event_schema import EventWithOwner, UpdateEventSchema, CreateEventSchema
from typing import *
from database import db_session
from pony.orm import *
from dependencies import common_parameters
from core.upload_instance import upload_base64
import crud

event_router = APIRouter(prefix="/event", tags=["event"])


@event_router.get('/admin', response_model=schemas.EventPaginate)
async def read_data(request: Request,
                    commons: dict = Depends(common_parameters)):
    with request.pony_session:
        page = commons['page']
        page_size = commons['page_size']
        order = commons['order']
        order_by = commons['order_by']
        request_args = dict(request.query_params)
        offset = (page - 1) * page_size
        query = event_crud.query_and_equal_dict(
            request,
            request_args=request_args,
            add_some_extra=f'ORDER BY {order_by} {order} '
            f'LIMIT {page_size} OFFSET {offset}')

        return schemas.EventPaginate(current_page=page,
                                     page_count=query['count'],
                                     data=query['data'])


@event_router.get('/by-interested', response_model=schemas.EventPaginate)
async def filter_by_interested(request: Request,
                               user: str,
                               commons: dict = Depends(common_parameters)):
    with request.pony_session:
        page = commons['page']
        page_size = commons['page_size']

        get_user_email = ''
        if user: get_user_email = user_crud.get_credential_by_token(user)
        query = models.EventPreference.select(
            lambda x: x.user.email == get_user_email)

        count = len(list(query))
        result = query.page(int(page), pagesize=int(page_size))
        event = []
        for i in list(result):
            event.append(i.event)

        return schemas.EventPaginateInterested(current_page=page,
                                               page_count=count,
                                               data=event)


@event_router.get('/', response_model=schemas.EventPaginate)
async def read_data(request: Request,
                    commons: dict = Depends(common_parameters)):
    with request.pony_session:
        page = commons['page']
        page_size = commons['page_size']
        order = commons['order']
        order_by = commons['order_by']

        request_args = dict(request.query_params)
        user = request_args.get('user', '')
        offset = (page - 1) * page_size
        query = event_crud.query_and_equal_dict(
            request,
            request_args=request_args,
            add_some_extra=f'ORDER BY {order_by} {order} '
            f'LIMIT {page_size} OFFSET {offset}')
        get_user_email = ''
        if user: get_user_email = user_crud.get_credential_by_token(user)

        data_event_preference = []
        for q in query['data']:
            obj = q
            obj.is_interested = False
            if 'user' in request.query_params.keys():
                for i in q.interested:
                    if i.email == get_user_email:
                        obj.is_interested = True

            data_event_preference.append(obj)

        return schemas.EventPaginate(current_page=page,
                                     page_count=query['count'],
                                     data=data_event_preference)


@event_router.get('/own', response_model=List[schemas.EventWithRegister])
async def read_own_data(request: Request,
                        current_user=Depends(user_crud.authenticate_by_token)):
    return list(event_crud.get_own_data(user=current_user))


@event_router.get('/{event_id}',
                  response_model=schemas.EventOwnerWithInterested)
async def read_one_data(event_id: int, request: Request, token: str = ''):
    with request.pony_session:
        user = ''
        if token:
            user = token
        get_user_email = ''
        if user: get_user_email = user_crud.get_credential_by_token(user)
        response = event_crud.get(id=event_id)

        response.is_interested = False
        for i in response.interested:
            if i.email == get_user_email:
                response.is_interested = True

        if not response:
            raise HTTPException(status_code=404,
                                detail="Event couldn't match the record")
        return response


@event_router.get('/admin/{event_id}',
                  response_model=schemas.EventOwnerWithInterested)
async def read_one_data(event_id: int, request: Request):
    with request.pony_session:
        response = event_crud.get(id=event_id)

        if not response:
            raise HTTPException(status_code=404,
                                detail="Event couldn't match the record")
        return response


@event_router.get('/admin/{event_id}',
                  response_model=schemas.EventWithRegister)
async def read_admin_detail(event_id: int, request: Request):
    with request.pony_session:
        response = event_crud.get(id=event_id)

        if not response:
            raise HTTPException(status_code=404,
                                detail="Event couldn't match the record")
        return response


@event_router.post('/', response_model=EventWithOwner)
async def write_data(schema: CreateEventSchema,
                     request: Request,
                     current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        return event_crud.create_with_owner(created_by=current_user,
                                            obj_in=schema)


'''delete event belong user login'''


@event_router.delete('/{event_id}')
async def delete_data(event_id: int,
                      request: Request,
                      force: typing.Optional[bool] = True,
                      current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        obj = event_crud.get_force_entry(id=event_id)

        if not obj:
            raise HTTPException(status_code=404,
                                detail="Couldn't found a record")
        if obj.created_by.id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail=
                "Unfortunately, you attempt to edit items not belongs to you")
        if (not event_crud.soft_delete(id=event_id)) and not force:
            raise HTTPException(
                status_code=404,
                detail="Can't delete, make sure the id provided is correct")
        if force:
            event_crud.remove(id=event_id)
            return {
                "message":
                "Record has been delete, you couldn't recover it later"
            }
        return {
            "message": "Record has been delete, you can recover it some days"
        }


'''update event belong to user login'''


@event_router.put("/{event_id}")
async def update_data(event_id: int,
                      schema: UpdateEventSchema,
                      request: Request,
                      current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        obj = event_crud.get(id=event_id)
        if not obj:
            raise HTTPException(status_code=404,
                                detail="Couldn't found any resource")
        if obj.created_by.id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail=
                "Unfortunately, you attempt to edit items not belongs to you")
        # remove category and re-create
        for c in list(obj.categories):
            obj.categories.remove(c)

        obj.flush()
        for i in schema.categories:
            obj.categories.add(models.Category[i])
        schema.thumbnail = upload_base64.upload_image_base64(schema.thumbnail)
        obj.updated_at = datetime.now()

        del schema.categories
        return event_crud.update(db_obj=obj, obj_in=schema)


@event_router.post('/restore/{event_id}')
async def restore_data(event_id: int,
                       request: Request,
                       current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        obj = event_crud.get_force_entry(id=event_id)
        # if obj couldn't found or delete is not soft, raise some errors
        if obj.created_by.id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail=
                "Unfortunately, you attempt to edit items not belongs to you")
        if not obj or (obj.deleted_at is None):
            raise HTTPException(
                status_code=404,
                detail="Couldn't found any record to proceed restore operations"
            )
        # otherwise continue to proceed operations
        event_crud.restore(id=event_id)
        return {"message": "Record has been restored"}


@event_router.get('/preference/{event_id}')
async def post_preference(event_id: int,
                          request: Request,
                          is_interested: bool = True,
                          current_user=Depends(
                              user_crud.authenticate_by_token)):
    with request.pony_session:
        if not event_crud.post_preference(event_id=event_id,
                                          user_id=current_user.id,
                                          is_interested=is_interested):
            raise HTTPException(status_code=404,
                                detail="Didn't found any record")
        return {"message": "event has been stored preference record"}


@event_router.get('/dashboard/all')
def dashboard_all_user():
    with db_session:
        member = len(crud.user_crud.model.select())
        event = len(crud.event_crud.model.select())
        news = len(crud.news_crud.model.select())
        female = len(crud.user_crud.model.select(gender='female'))
        male = len(crud.user_crud.model.select(gender='male'))
        current_active_event = len(
            crud.event_crud.model.select(
                lambda x: x.start_date > datetime.now()))
        pass_due_event = len(
            crud.event_crud.model.select(
                lambda x: x.start_date < datetime.now()))
        member_register = len(models.Registration.select())
        uncheck = len(models.Registration.select(check_in=False))
        check = len(models.Registration.select(check_in=True))
        client = len(crud.user_crud.model.select(role='client'))
        admin = len(crud.user_crud.model.select(role='admin'))
        client_avg= 0
        admin_avg= 0
        calc_per_male= 0
        calc_per_female= 0
        check_average = 0
        if member != 0:
            client_avg = round(client * 100 / member)
            admin_avg = round(admin * 100 / member)
            calc_per_male = round(male * (100 / member))
            calc_per_female = round(female * (100 / member))
        if member_register !=0:
            check_average = round(check * (100 / member_register))
        return {
            'member': member,
            'event': event,
            'news': news,
            'current_active_event': current_active_event,
            'pass_due_event': pass_due_event,
            'member_register_all_event': member_register,
            'check_average': f"{check_average}%",
            'gender': {
                'female': f"{ calc_per_female }%",
                'female_raw': calc_per_female,
                'male_raw': calc_per_male,
                'male': f"{calc_per_male}%"
            },
            'role': {
                'client': f"{ client_avg }%",
                'client_raw': client_avg,
                'admin_raw': admin_avg,
                'admin': f"{admin_avg}%"
            }
        }
