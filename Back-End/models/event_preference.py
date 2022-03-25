from database import db
from pony.orm import *
from datetime import datetime


class EventPreference(db.Entity):
    _table_ = "event_preference"
    id = PrimaryKey(int, auto=True)
    event = Required("Event", column="event_id")
    is_interested = Required(bool, default=True)
    user = Required("User", column="user_id")
    created_at = Optional(datetime, default=datetime.now())
    updated_at = Optional(datetime)
