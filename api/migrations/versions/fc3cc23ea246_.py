"""empty message

Revision ID: fc3cc23ea246
Revises: ce840f016302
Create Date: 2021-08-11 16:39:10.975245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc3cc23ea246'
down_revision = 'ce840f016302'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plots', sa.Column('type', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('plots', 'type')
    # ### end Alembic commands ###


def upgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

