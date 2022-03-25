import models
from models import Event
from crud.base import CRUDBase
from pony.orm import commit
from models import User, EventPreference
from schemas import CreateEventSchema, UpdateEventSchema
from core import Base64ToFile
import schemas


class CategoryCrud(CRUDBase[models.Category, schemas.CreateCategory, schemas.UpdateCategory]):
    pass


category_crud = CategoryCrud(models.Category)