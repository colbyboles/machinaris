"""empty message

Revision ID: 241cf86f57bd
Revises: bf024c5e1aea
Create Date: 2021-10-15 16:34:08.470608

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '241cf86f57bd'
down_revision = 'bf024c5e1aea'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plots')
    op.create_table('plots',
        sa.Column('hostname', sa.String(length=255), primary_key=True),
        sa.Column('blockchain', sa.String(length=255), nullable=True),
        sa.Column('displayname', sa.String(length=255), nullable=True),
        sa.Column('plot_id', sa.String(length=16), primary_key=True),
        sa.Column('type', sa.String(length=32), nullable=True),
        sa.Column('dir', sa.String(length=255), nullable=False),
        sa.Column('file', sa.String(length=255), nullable=False),
        sa.Column('size', sa.Integer, nullable=False),
        sa.Column('created_at', sa.String(length=64), nullable=False),
        sa.Column('updated_at', sa.DateTime(), onupdate=func.now()),
        sa.PrimaryKeyConstraint('hostname', 'plot_id')
    )
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plots')
    op.create_table('plots',
        sa.Column('hostname', sa.String(length=255), primary_key=True),
        sa.Column('blockchain', sa.String(length=255), nullable=True),
        sa.Column('plot_id', sa.String(length=16), primary_key=True),
        sa.Column('type', sa.String(length=32), nullable=True),
        sa.Column('dir', sa.String(length=255), nullable=False),
        sa.Column('file', sa.String(length=255), nullable=False),
        sa.Column('size', sa.Integer, nullable=False),
        sa.Column('created_at', sa.String(length=64), nullable=False),
        sa.Column('updated_at', sa.DateTime(), onupdate=func.now()),
        sa.PrimaryKeyConstraint('hostname', 'plot_id')
    )
    # ### end Alembic commands ###


def upgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

