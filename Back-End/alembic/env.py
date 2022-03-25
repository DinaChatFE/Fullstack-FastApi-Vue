from logging.config import fileConfig
from alembic.config import Config
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from database.connect import database_connect

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
#  ======= Just added by dina on 17 nov 21==========
alembic_cfg = Config()
alembic_cfg.set_main_option("sqlalchemy.url", "postgresql://dina:password@localhost/event_news")
# ======== ended =========


# =============this is example of using config in alembic sql connections==============
# sqlalchemy.url = postgresql://dina:password@localhost/event_news

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # ======replace it once using alembic with config
    url = database_connect.get_db()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    
    # ====== also this one as well, calling database_connect method get db to use========
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = database_connect.get_db()
    connectable = engine_from_config(
        configuration, prefix="sqlalchemy.", poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
