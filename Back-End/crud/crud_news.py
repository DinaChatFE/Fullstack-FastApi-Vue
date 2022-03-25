from models import Event
from crud.base import CRUDBase
from pony.orm import commit
from models import User, News, NewsPreference
from schemas import CreateNewsSchema, UpdateNewsSchema
import models
from core.helper.base64_to_file import Base64ToFile
from pony.orm import db_session


class NewsCrud(CRUDBase[News, CreateNewsSchema, UpdateNewsSchema]):
    @classmethod
    def upload_image_base64(cls, data):
        if data or len(data) > 40:
            return Base64ToFile(data).filename
        return data

    @classmethod
    def get_by_categories(cls, categories, page: int, pagesize: int):
        query = models.Category[categories].news
        return {'data': query.page(page, pagesize=pagesize), 'count': query.count()}

    def get_by_users(self, user, page: int, pagesize: int):
        query = self.model.select(lambda x: x.created_by.id == user)
        return {'data': query.page(page, pagesize=pagesize), 'count': query.count()}

    def create_with_owner(self, created_by, obj_in: CreateNewsSchema):
        categories = obj_in.categories
        obj_in.thumbnail = self.upload_image_base64(obj_in.thumbnail)
        del obj_in.categories
        news_obj = self.model(**obj_in.dict())
        for i in categories:
            news_obj.categories.add(models.Category.get(id=i))
        # noted: user can not call directly from authorization token obj, reason: session separately
        user = User[created_by.id]
        news_obj.user = user
        commit()
        news_obj.flush()

        return news_obj

    def get_own_data(self, user):
        return self.model.select(deleted_at=None, user=user.id)

    def post_preference(self, news_id, user_id, is_interested):
        news = self.model.get(id=news_id)
        if not news:
            return None
        has_event = news.news_preference.select(user=User[user_id])
        if has_event:
            has_event.delete()
            commit()
        NewsPreference(news=self.model[news_id], user=User[user_id],
                       is_interested=is_interested)
        commit()
        news.flush()
        return news


news_crud = NewsCrud(News)
