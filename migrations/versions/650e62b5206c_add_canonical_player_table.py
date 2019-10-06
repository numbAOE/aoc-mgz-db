"""add canonical player table

Revision ID: 650e62b5206c
Revises: 5f04067e5e7d
Create Date: 2019-09-22 14:04:13.641944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '650e62b5206c'
down_revision = '5f04067e5e7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('canonical_players',
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('platform_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id', 'platform_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('canonical_players')
    # ### end Alembic commands ###
