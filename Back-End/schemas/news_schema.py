from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from schemas import UserProfile
from .category_schema import  CategoryOut
from .base_schema import WithPaginate


class NewsBaseModel(BaseModel):
    title: str
    description: str
    thumbnail: str
    content: str
    

class CreateNewsSchema(NewsBaseModel):
    categories: List[int]
    pass


class UpdateNewsSchema(NewsBaseModel):
    categories: List[int]
    # created_by: int
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
class NewsWithOwner(BaseModel):
    id: int
    created_by: Optional[UserProfile]
    interested: List[UserProfile]
    uninterested: List[UserProfile]
    title: str
    description: str
    thumbnail: str
    content: str
    created_at_format: Optional[str]
    categories_props: Optional[List[CategoryOut]]

    #
    class Config:
        orm_mode = True


class NewsPaginate(WithPaginate):
    data: List[NewsWithOwner]
