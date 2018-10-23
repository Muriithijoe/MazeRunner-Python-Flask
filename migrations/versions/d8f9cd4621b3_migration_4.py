"""Migration 4

Revision ID: d8f9cd4621b3
Revises: a7fea2dcaf54
Create Date: 2018-10-23 10:47:45.022474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8f9cd4621b3'
down_revision = 'a7fea2dcaf54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('button1', sa.String(), nullable=True))
    op.add_column('questions', sa.Column('button2', sa.String(), nullable=True))
    op.add_column('questions', sa.Column('div', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'div')
    op.drop_column('questions', 'button2')
    op.drop_column('questions', 'button1')
    # ### end Alembic commands ###