from datetime import date, datetime
from pony.orm import PrimaryKey, Required, Set, Optional, LongStr
from database import db
from .event import *


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    last_name = Optional(str)
    role = Required(str, default="client")
    profile = Optional(str)
    date_of_birth = Optional(date)
    password = Required(str)
    email = Required(str)
    phone_number = Optional(str)
    created_at = Required(datetime, default=datetime.now)
    updated_at = Optional(datetime, volatile=True)
    deleted_at = Optional(datetime)
    email_verification_at = Optional(datetime)
    event = Set("Event")
    news = Set("News")
    event_preference = Set("EventPreference")
    news_preference = Set("NewsPreference")
    registrations = Set("Registration")
    address = Optional(str)
    school_work = Optional(str)
    bio = Optional(LongStr)
    gender= Optional(str) 

    @property
    def full_name(self):
        return self.first_name  + ' ' + self.last_name

    @property
    def with_post(self):
        return self.news.get(id=9).id
    
