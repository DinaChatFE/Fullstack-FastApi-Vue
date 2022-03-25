from models.event_preference import *
from models.user import *
from models.event import *
from models.news_preference import *
from models.news import *
from models.registration import *
from models.category import *


db.generate_mapping(create_tables=True)
