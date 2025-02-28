"""empty message

Revision ID: ce840f016302
Revises: f529fc25f0d6
Create Date: 2021-08-11 10:15:42.883128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce840f016302'
down_revision = 'f529fc25f0d6'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pools', sa.Column('login_link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pools', 'login_link')
    # ### end Alembic commands ###


def upgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

