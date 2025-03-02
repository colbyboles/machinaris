"""empty message

Revision ID: 5ea0ec1d8711
Revises: bdfe8db75307
Create Date: 2021-07-29 17:21:19.447778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ea0ec1d8711'
down_revision = 'bdfe8db75307'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pools',
    sa.Column('unique_id', sa.String(length=255), nullable=False),
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=True),
    sa.Column('launcher_id', sa.String(length=255), nullable=False),
    sa.Column('pool_state', sa.String(), nullable=False),
    sa.Column('updated_at', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('unique_id')
    )
    op.add_column('workers', sa.Column('displayname', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workers', 'displayname')
    op.drop_table('pools')
    # ### end Alembic commands ###


def upgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

