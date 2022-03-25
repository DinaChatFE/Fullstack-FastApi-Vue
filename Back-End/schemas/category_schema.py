import datetime
from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    created_at: Optional[datetime.datetime] = datetime.datetime.now()
    # updated_at: Optional[datetime.datetime]


class CreateCategory(BaseModel):
    name: str
    class Config:
        orm_mode = True


class UpdateCategory(CategoryBase):
    class Config:
        orm_mode = True


class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_mode = True
