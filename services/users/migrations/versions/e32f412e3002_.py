"""empty message

Revision ID: e32f412e3002
Revises: d19f9403b6ad
Create Date: 2020-08-21 17:54:34.149450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e32f412e3002'
down_revision = 'd19f9403b6ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pasword', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pasword')
    # ### end Alembic commands ###