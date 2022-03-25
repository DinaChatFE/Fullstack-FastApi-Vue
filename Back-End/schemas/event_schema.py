from datetime import datetime
from typing import Optional, List, Union
from pydantic import BaseModel

import models
from schemas import UserProfile
import schemas
from schemas.base_schema import WithPaginate


class EventBaseSchema(BaseModel):
    title: str
    # description: str
    thumbnail: str
    location: str
    description: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    mode: Optional[str] = "offline"
    status: str


class CreateEventSchema(EventBaseSchema):
    # created_by: int
    categories: List[int]
    pass


class UpdateEventSchema(EventBaseSchema):
    categories: List[int]
    pass


class Test(BaseModel):
    user_id: int


class PostPreferenceSchema(BaseModel):
    model_type: str
    # id: int
    user: UserProfile

    class Config:
        orm_mode = True


# return event with owner object
class EventWithOwner(EventBaseSchema):
    id: int
    created_by: Optional[UserProfile]
    interested: List[UserProfile]
    uninterested: List[UserProfile]
    # start_date_format: Optional[str]
    # end_date_format: Optional[str]

    #
    class Config:
        orm_mode = True


class EventPaginateWithoutInterest(WithPaginate):
    data: List[EventWithOwner]
class EventOwnerWithInterested(EventWithOwner):
    is_interested: Optional[bool] = False
    start_date_format: Optional[str]
    end_date_format: Optional[str]
    register_member: List[UserProfile] = []
    


class EventWithRegister(EventBaseSchema):
    id: int
    register_member: List[UserProfile]

    class Config:
        orm_mode = True

class EventInterestedFilter(EventOwnerWithInterested):
    is_interested: Optional[bool] = True

class EventPaginate(WithPaginate):
    data: List[EventOwnerWithInterested]
class EventPaginateInterested(WithPaginate):
    data: List[EventInterestedFilter]



class CheckIn(BaseModel):
    register_id: int

    class Config:
        orm_mode = True
