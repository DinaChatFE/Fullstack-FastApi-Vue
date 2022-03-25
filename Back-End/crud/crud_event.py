import models
from crud.base import CRUDBase
from pony.orm import commit
from models import User, EventPreference, Event, Category
from schemas import CreateEventSchema, UpdateEventSchema
from core import Base64ToFile
import schemas


class EventCrud(CRUDBase[Event, CreateEventSchema, UpdateEventSchema]):
    @classmethod
    def upload_image_base64(cls, data):
        if data or len(data) > 18:
            return Base64ToFile(data).filename
        return data

    def create_with_owner(self, created_by, obj_in: CreateEventSchema):
        obj_in.thumbnail = self.upload_image_base64(obj_in.thumbnail)
        # event = Event[event_id]
        # event.user = User[user_id]
        categories = obj_in.categories
        del obj_in.categories
        event_obj = self.model(**obj_in.dict())
        for i in categories:
            event_obj.categories.add(models.Category.get(id=i))

        # noted: user can not call directly from authorization token obj, reason: session separately
        user = User[created_by.id]
        event_obj.user = user
        commit()
        event_obj.flush()
        return event_obj

    def get_own_data(self, user):
        return self.model.select(deleted_at=None, user=user.id)

    def post_preference(self, event_id, user_id, is_interested):
        event = self.model.get(id=event_id)
        if not event:
            return None
        has_event = event.event_preference.select(user=User[user_id])
        if has_event:
            has_event.delete()
            commit()

        if is_interested:
            EventPreference(event=self.model[event_id],
                            user=User[user_id],
                            is_interested=is_interested)

        commit()
        event.flush()
        return event



event_crud = EventCrud(Event)
