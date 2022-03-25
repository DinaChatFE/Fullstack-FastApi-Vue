"""Added events s

Revision ID: 78b3e8d167e2
Revises: 07c1ee238133
Create Date: 2021-11-19 18:25:58.751779

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '78b3e8d167e2'
down_revision = '07c1ee238133'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'events', sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(150), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('created_by', sa.Integer, sa.ForeignKey("users.id")),
        sa.Column('thumbnail', sa.String(100), nullable=True),
        sa.Column('location', sa.String, nullable=True),
        sa.Column('start_date', sa.TIMESTAMP, nullable=False),
        sa.Column('end_date', sa.TIMESTAMP, nullable=False),
        sa.Column('mode', sa.String(100), nullable=False),
        sa.Column('status',
                  sa.String(100),
                  nullable=False,
                  server_default="open"),
        sa.Column('created_at',
                  sa.TIMESTAMP,
                  server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP, nullable=True))


def downgrade():
    op.drop_table('events')
