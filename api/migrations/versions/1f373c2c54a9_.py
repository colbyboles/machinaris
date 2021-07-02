"""empty message

Revision ID: 1f373c2c54a9
Revises: cc75568c1716
Create Date: 2021-06-28 17:31:17.107779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f373c2c54a9'
down_revision = 'cc75568c1716'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallets')
    op.create_table('wallets',
        sa.Column('hostname', sa.String(length=255), nullable=False),
        sa.Column('blockchain', sa.String(length=64), nullable=False),
        sa.Column('details', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('hostname', 'blockchain')
    )
    op.drop_table('blockchains')
    op.create_table('blockchains',
        sa.Column('hostname', sa.String(length=255), nullable=False),
        sa.Column('blockchain', sa.String(length=64), nullable=False),
        sa.Column('details', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('hostname', 'blockchain')
    )
    op.drop_table('connections')
    op.create_table('connections',
        sa.Column('hostname', sa.String(length=255), nullable=False),
        sa.Column('blockchain', sa.String(length=64), nullable=False),
        sa.Column('details', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('hostname', 'blockchain')
    )
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    p.drop_table('wallets')
    op.create_table('wallets',
        sa.Column('hostname', sa.String(length=255), nullable=False),
        sa.Column('blockchain', sa.String(length=64), nullable=True),
        sa.Column('details', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('hostname')
    )
    op.drop_table('blockchains')
    op.create_table('blockchains',
        sa.Column('hostname', sa.String(length=255), nullable=False),
        sa.Column('blockchain', sa.String(length=64), nullable=True),
        sa.Column('details', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('hostname')
    )
    op.drop_table('connections')
    op.create_table('connections',
        sa.Column('hostname', sa.String(length=255), nullable=False),
        sa.Column('blockchain', sa.String(length=64), nullable=True),
        sa.Column('details', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('hostname')
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


def upgrade_chiadog():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_chiadog():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
