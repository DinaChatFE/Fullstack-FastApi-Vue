from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException

import crud
from crud import user_crud
from pony.orm import commit
from starlette.requests import Request
import models
from models import registration
from models import event
import schemas

register_route = APIRouter(prefix='/registration', tags=['Registration'])


@register_route.post('/check-in/{event_id}/{user_id}')
async def check_in(request: Request,
                   event_id: int,
                   user_id: int,
                   current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        event = models.Event.get(id=event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        if event.start_date > datetime.now():
            raise HTTPException(status_code=403, detail='Event overdue')

        register = models.Registration.get(event=models.Event[event_id],
                                           user=models.User[user_id])
        if not register:
            raise HTTPException(status_code=404,
                                detail="Couldn't found any record")

        register.set(check_in=True)
        commit()
        return {"message": "Register has checked"}


@register_route.get('/{event_id}', response_model=schemas.EventWithRegister)
async def read_data(
        event_id: int,
        request: Request,
        current_user=Depends(user_crud.authenticate_by_token),
):
    with request.pony_session:
        return crud.event_crud.get(id=event_id)


@register_route.post('/{event_id}', response_model=schemas.EventWithRegister)
async def write_data(event_id: int,
                     request: Request,
                     current_user=Depends(user_crud.authenticate_by_token)):
    with request.pony_session:
        event = crud.event_crud.get(id=event_id)

        if not event:
            raise HTTPException(
                status_code=404,
                detail="event you looking for was not match the datastore")

        # delete last registration if there are register multiple times
        registration = models.Registration.get(event=event_id,
                                               user=current_user.id)
        if registration:
            registration.delete()

        models.Registration(event=event, user=models.User[current_user.id])
        commit()
        event.flush()
        return event

@register_route.get('/{event_id}/{user_id}')
async def check_register_status(event_id: int, user_id: int, request: Request):
    with request.pony_session:
        model = models.Registration.get(event=event_id, user=user_id)
        if model:
            return {'check_in': True}
        return {'check_in': False}