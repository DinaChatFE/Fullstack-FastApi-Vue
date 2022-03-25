from datetime import datetime
from pony.orm import *
from database import db
from .user import *
from .event_preference import EventPreference
from decouple import config


class Event(db.Entity):
    _table_ = "events"
    id = PrimaryKey(int, auto=True)
    title = Optional(str, volatile=True)
    description = Optional(LongStr)
    thumbnail = Optional(str)
    location = Optional(str)
    start_date = Optional(datetime, volatile=True)
    end_date = Optional(datetime, volatile=True)
    mode = Required(str, default="offline")
    status = Required(str, default="open")
    created_at = Required(datetime, default=datetime.now)
    updated_at = Optional(datetime, volatile=True)
    deleted_at = Optional(datetime)
    user = Optional("User", column='created_by')
    categories = Set('Category')
    # user = Optional('User', column='created_at') 
    event_preference = Set("EventPreference")
    registrations = Set("Registration")

    @property
    def created_by(self):
        return self.user

    @property
    def interested(self):
        for li in self.event_preference.select(is_interested=True):
            yield li.user

    @property
    def start_date_format(self):
        return self.start_date.strftime(config('DEFAULT_FORMAT_DATE'))

    @property
    def end_date_format(self):
        return self.end_date.strftime(config('DEFAULT_FORMAT_DATE'))

    @property
    def uninterested(self):
        for li in self.event_preference.select(is_interested=False):
            yield li.user

    @property
    def register_member(self):
        for register in self.registrations.select().without_distinct():
            member = register.user
            setattr(member, 'check_in', register.check_in)
            yield member
    
    ''' @property
    def register_member_with_check(self):
        for register in self.registrations.select().without_distinct():
            member = dict(register.user)
            member['check_in'] = register.check_in '''
            
    @property
    def is_user_interested(self):
        return self.interested
