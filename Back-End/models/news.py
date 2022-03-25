from datetime import datetime
from pony.orm import *
from database import db
from .user import *
from decouple import config


class News(db.Entity):
    _table_ = "news"
    id = PrimaryKey(int, auto=True)
    title = Optional(str, volatile=True)
    description = Optional(LongStr)
    thumbnail = Optional(str)
    content = Optional(LongStr)
    created_at = Required(datetime, default=datetime.now)
    updated_at = Optional(datetime, volatile=True)
    deleted_at = Optional(datetime)
    categories = Set('Category')
    user = Optional("User", column='created_by')
    news_preference = Set("NewsPreference")

    @property
    def created_by(self):
        return self.user

    @property
    def interested(self):
        for li in self.news_preference.select(is_interested=True):
            yield li.user

    @property
    def categories_props(self):
        for c in list(self.categories):
            yield c


    @property
    def uninterested(self):
        for li in self.news_preference.select(is_interested=False):
            yield li.user

    @property
    def created_at_format(self):
        return self.created_at.strftime(config('DEFAULT_FORMAT_DATE'))