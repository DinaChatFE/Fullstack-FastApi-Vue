from fastapi import APIRouter
from starlette.requests import Request
from pony.orm import commit
import models
import schemas

route = APIRouter(prefix="/test_log")


@route.get('/interested/{event_id}/{user_id}', response_model=schemas.EventWithOwner)
async def interested_event(event_id: int, user_id: int, request: Request):
    with request.pony_session:
        event = models.Event[event_id]
        models.PostPreference(post=models.Event[event_id], user=models.User[user_id], model_type="event", is_interested=True)
        commit()
        event.flush()
        return event


@route.get('/preference/interested', response_model=schemas.EventWithOwner)
async def get_preference(event_id: int, request: Request):
    with request.pony_session:
        event_model = models.Event[event_id]
        return event_model
