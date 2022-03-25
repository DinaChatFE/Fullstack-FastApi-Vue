import datetime

from database import db
from pony.orm import *


class Registration(db.Entity):
    _table_ = "registrations"
    id = PrimaryKey(int, auto=True)
    event = Required("Event", column='event_id')
    user = Required("User", column='user_id')
    check_in = Required(bool, default=False)
    created_at = Required(datetime.datetime, default=datetime.datetime.now())
    updated_at = Optional(datetime.datetime)
    
