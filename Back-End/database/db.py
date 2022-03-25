from pony.orm import *
from database.connect import pg_sql_connect


db = Database()

db.bind(provider=pg_sql_connect['provider'], host=pg_sql_connect['host'], user=pg_sql_connect['user'], password=pg_sql_connect['password'],
        database=pg_sql_connect['db'], port=pg_sql_connect['port'])
print('DB_factory')
