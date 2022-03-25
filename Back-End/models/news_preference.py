from database import db
from pony.orm import *
from datetime import datetime


class NewsPreference(db.Entity):
    _table_ = "news_preference"
    id = PrimaryKey(int, auto=True)
    news = Required("News", column="news_id")
    is_interested = Required(bool, default=True)
    user = Required("User", column="user_id")
    created_at = Optional(datetime, default=datetime.now())
    updated_at = Optional(datetime)
