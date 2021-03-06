"""empty message

Revision ID: 9f6335e94904
Revises: fd92700d5801
Create Date: 2020-01-21 15:48:55.997715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f6335e94904'
down_revision = 'fd92700d5801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Actor', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Movie', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Movie', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Actor', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
