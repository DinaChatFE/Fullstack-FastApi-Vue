import datetime
from logging import log
from re import split
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from crud import CRUDBase
from schemas import CreateUserSchema, UpdateUserSchema, LoginUserSchema
from models.user import User
from core import AuthHandler
from core import settings
from starlette.requests import Request
from pony.orm import commit
from core import Base64ToFile

auth_handler = AuthHandler()


class UserCrud(CRUDBase[User, CreateUserSchema, UpdateUserSchema]):
    def get_user_by_email(self, email):
        return self.model.get(email=email)

    @classmethod
    def upload_image_base64(cls, data):
        if data and (len(data)> 40):
            return Base64ToFile(data).filename
        return data

    def create_user(self,
                    obj_in: CreateUserSchema):
        # if email has already taken return none
        if self.is_email_exist(email=obj_in.email):
            return None
        # then continue process, hash password into databases"""
        obj_in.password = auth_handler.get_password_hash(
            password=obj_in.password)
        obj_out = jsonable_encoder(obj_in)
        obj_out['profile'] = self.upload_image_base64(obj_in.profile)
        del obj_out['confirm_password']
        model = self.model(**obj_out)
        commit()
        model.flush()

        return model

    def update_user(self, obj_in: UpdateUserSchema, user_id):
        obj_in.profile = self.upload_image_base64(obj_in.profile)
            
        dict_obj = obj_in.dict()
        dict_obj['updated_at'] = datetime.datetime.now()
        model = self.model[user_id].set(**dict_obj)
        return self.model[user_id]

    def is_email_exist(self, email):
        if self.get_user_by_email(email=email):
            raise HTTPException(status_code=403, detail="Email has been taken")
        return False

    def authenticate(self, *, obj_in: LoginUserSchema):
        get_user = self.get_user_by_email(email=obj_in.email)
        if (get_user is None) or (not auth_handler.verify_password(
                obj_in.password, get_user.password) or (get_user.role != obj_in.role)):
            return False
        return True

    def generate_authorization(self,
                               obj_in: LoginUserSchema) -> Optional[dict]:
        if self.authenticate(obj_in=obj_in):
            return {
                "token": auth_handler.encode_token(obj_in.email),
                "expire_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES
            }
        return None

    def authenticate_by_token(self,
                              request: Request,
                              email: str = Depends(auth_handler.auth_wrapper)):
        with request.pony_session:
            user_authenticate = self.get_user_by_email(email=email)
            if not user_authenticate:
                return None
            return user_authenticate

    @classmethod
    def get_credential_by_token(cls, token):
        return auth_handler.authorize_with_no_header(token)


user_crud = UserCrud(User)
