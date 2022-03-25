from typing import *
from pydantic import BaseModel

DisplaySchemaType = TypeVar("DisplaySchemaType")


class WithPaginate(BaseModel, Generic[DisplaySchemaType]):
    data: List[DisplaySchemaType]
    page_count: int
    current_page: int
