from decouple import config

pg_sql_connect = {'provider': config('DB_CONNECTION'), 'host': config('DB_HOST'), 'user': config('DB_USER'),
                  'password': config('DB_PASSWORD'), 'db': config('DB_NAME'), 'port': config('DB_PORT')}


class DatabaseConnection:
    def get_db(self):
        return "%s://%s:%s@%s/%s" % (
            config('DB_CONNECTION'),
            config("DB_USER", "vagrant"),
            config("DB_PASSWORD", "vagrant"),
            config("DB_HOST", "db"),
            config("DB_NAME", "vagrant"),
        )


database_connect = DatabaseConnection()
