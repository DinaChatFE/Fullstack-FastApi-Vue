from fastapi import APIRouter, HTTPException, Depends
from models.user import User
from schemas import CreateUserSchema, UserProfileOut, LoginUserSchema, event_schema
from schemas.auth_user_schema import UserProfile
from starlette.requests import Request
from crud.crud_user import user_crud
import schemas
from typing import List, Optional
from database import db_session
# ======initialize api route schema============
auth_router = APIRouter(prefix="/auth", tags=["user"])
"""get profile by passing the token"""


@auth_router.get('/user-profile', response_model=UserProfileOut)
def profile_user(current_user=Depends(user_crud.authenticate_by_token)):
    if not current_user:
        return HTTPException(
            status_code=404,
            detail="Your input incorrect request, try another one")

    response_data = UserProfileOut(code=0,
                                   message="well done",
                                   data=current_user)
    return response_data


"""register new users, raise error if email already taken"""


@auth_router.post('/register', response_model=schemas.UserProfile)
def register_user(schema: CreateUserSchema, request: Request):
    with request.pony_session:
        user = user_crud.create_user(obj_in=schema)
        if not user:
            raise HTTPException(status_code=422,
                                detail="Email has already been taken")
        return user


"""Login user if email and password matches"""


@auth_router.put('/update/{user_id}', response_model=schemas.UserProfile)
def update_user(user_id: int, schema: schemas.UpdateUserSchema,
                request: Request):
    with db_session:
        user = user_crud.update_user(obj_in=schema, user_id=user_id)
        return user


@auth_router.post('/login')
def login_user(schema: LoginUserSchema, request: Request):
    with request.pony_session:
        user = user_crud.generate_authorization(obj_in=schema)
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Unauthentication, please verify email and password")
        user['user'] =  schemas.UserProfile.from_orm(user_crud.model.get(email=schema.email))
        return user


@auth_router.get("/justtest", response_model=UserProfile)
def testing(request: Request, id: int):
    with request.pony_session:
        return user_crud.get(id=id)


@auth_router.get('/all', response_model=List[schemas.UserProfile])
def all_author(request: Request, all_role: Optional[bool] = False):
    with request.pony_session:
        if all_role:
            return list(user_crud.model.select().order_by(lambda x: x.created_at))
        return list(user_crud.model.select(role='admin').order_by(lambda x: x.created_at))
