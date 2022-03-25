import datetime
import typing
from typing import Optional
from pydantic import BaseModel, validator
import re
from database.base_class import Base
from enum import Enum
from decouple import config


# enumerations

class RoleEnum(str, Enum):
    client = "client"
    admin = "admin"


class UserProfile(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    role: Optional[RoleEnum] = RoleEnum.client
    profile: Optional[str]
    date_of_birth: Optional[datetime.date]
    full_name: Optional[str]
    email: str
    address: Optional[str] =""
    # bio: Optional[str] = ""
    school_work: Optional[str] = ""
    phone_number: Optional[str] =""
    check_in: Optional[bool] = False

    class Config:
        orm_mode = True


class UserProfileRegister(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    role: Optional[RoleEnum] = RoleEnum.client
    profile: Optional[str]
    date_of_birth: Optional[datetime.date]
    full_name: Optional[str]
    email: str
    address: Optional[str] =""
    # bio: Optional[str] = ""
    school_work: Optional[str] = ""
    phone_number: Optional[str] =""
    with_check_in_specialize: Optional[str] = ''

    class Config:
        orm_mode = True
        
class UserProfileOut(BaseModel):
    code: int
    message: str
    data: UserProfile

    class Config:
        orm_mode = True


class UserBaseSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    profile: Optional[str]
    date_of_birth: Optional[datetime.date]
    role: RoleEnum
    password: str = "password"
    confirm_password: str = "password"
    email: str = "email@example.com"
    phone_number: str
    gender: Optional[str] = 'male'

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    @validator('confirm_password')
    def validate_password(cls, v, values, **kwargs):
        if v != values['password']:
            raise ValueError('password doesn\'t match')
        if len(values['password']) < 8:
            raise ValueError("password could not less than 8 charactors")
        return v

    @validator('email')
    def validate_email(cls, v):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.search(regex, v):
            raise ValueError('incorrect email, email should contains .,  @')
        return v


class UpdateUserSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    profile: Optional[str]
    date_of_birth: Optional[datetime.date]
    phone_number: Optional[str]
    address: Optional[str] = ""
    school_work: Optional[str] = ""
    bio: Optional[str] = ""

    class Config:
        orm_mode = True




class LoginUserSchema(BaseModel):
    email: str
    password: str
    role: Optional[str] = 'client'
