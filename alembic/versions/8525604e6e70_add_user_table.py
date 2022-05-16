"""add user table

Revision ID: 8525604e6e70
Revises: ee2ea45a6db7
Create Date: 2022-05-16 13:29:29.360224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8525604e6e70'
down_revision = 'ee2ea45a6db7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
