"""product

Revision ID: 4f52d4dd6ea1
Revises: 635c6ffc9b10
Create Date: 2022-07-07 18:15:07.986636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f52d4dd6ea1'
down_revision = '635c6ffc9b10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shopholder', sa.Column('contactno', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shopholder', 'contactno')
    # ### end Alembic commands ###
