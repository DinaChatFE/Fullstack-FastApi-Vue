"""add interested post

Revision ID: e1dc3144ae6b
Revises: 78b3e8d167e2
Create Date: 2021-11-25 14:42:57.625474

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression 


# revision identifiers, used by Alembic.
revision = 'e1dc3144ae6b'
down_revision = '78b3e8d167e2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'post_preference',
        sa.Column('post_id', sa.Integer, nullable=False),
        sa.Column('model_type', sa.String(40), nullable=False),
        sa.Column('is_interested', sa.Boolean, server_default=expression.false()),
        sa.Column('user_id', sa.Integer ,  sa.ForeignKey("users.id")),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True)
    )

def downgrade():
    op.drop_table('post_preference')
