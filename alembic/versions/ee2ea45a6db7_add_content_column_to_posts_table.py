"""add content column to posts table

Revision ID: ee2ea45a6db7
Revises: 9ae34435e23c
Create Date: 2022-05-16 13:23:29.793614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee2ea45a6db7'
down_revision = '9ae34435e23c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
