from database import db
from pony.orm import *
from datetime import datetime


class Category(db.Entity):
    _table_ = "categories"
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    news = Set("News", volatile=True)
    event = Set("Event")
    created_at = Optional(datetime, default=datetime.now())
    updated_at = Optional(datetime, volatile=True)
    deleted_at = Optional(datetime)

