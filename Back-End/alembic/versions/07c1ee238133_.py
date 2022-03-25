"""initialize app, create users tables

Revision ID: 07c1ee238133
Revises: 
Create Date: 2021-11-16 13:03:43.141585

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '07c1ee238133'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('first_name',sa.String(50) , nullable=True,), 
                    sa.Column('last_name', sa.String(50), nullable=True),
                    sa.Column('role', sa.String(50), nullable=False, default="client"),
                    sa.Column('profile', sa.String, nullable=True),
                    sa.Column('date_of_birth', sa.DateTime, nullable=True),
                    sa.Column('email_verification_at', sa.TIMESTAMP, nullable=True),
                    sa.Column('password', sa.String, nullable=True),
                    sa.Column('email' , sa.String, nullable=False, unique=True),
                    sa.Column('phone_number', sa.String, nullable=True),
                    sa.Column('created_at', sa.TIMESTAMP, nullable=True),
                    sa.Column('updated_at', sa.TIMESTAMP, nullable=True)
    )

def downgrade():
    op.drop_table('users')
