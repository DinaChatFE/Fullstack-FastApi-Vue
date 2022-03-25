import os
from typing import *


def get_db_url():
    return "%s://%s:%s@%s/%s" % (
        os.getenv('DB_CONNECTION'),
        os.getenv("DB_USER", "vagrant"),
        os.getenv("DB_PASSWORD", "vagrant"),
        os.getenv("DB_HOST", "db"),
        os.getenv("DB_NAME", "vagrant"),
    )


async def common_parameters(page: Optional[int] = 1, page_size: Optional[int] = 10,
                            order_by: Optional[str] = "created_at",
                            order: Optional[str] = "DESC", ):
    return {'page': page, 'page_size': page_size, 'order_by': order_by, 'order': order}
