"""empty message

Revision ID: 7a66cdc8385a
Revises: 013b8bed94b0
Create Date: 2021-10-24 19:57:59.559539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a66cdc8385a'
down_revision = '013b8bed94b0'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stat_netspace_size', sa.Column('hostname', sa.String(), nullable=True))
    op.add_column('stat_plot_count', sa.Column('hostname', sa.String(), nullable=True))
    op.add_column('stat_plots_size', sa.Column('hostname', sa.String(), nullable=True))
    op.add_column('stat_plots_total_used', sa.Column('hostname', sa.String(), nullable=True))
    op.add_column('stat_plotting_total_used', sa.Column('hostname', sa.String(), nullable=True))
    op.add_column('stat_plotting_total_used', sa.Column('blockchain', sa.String(length=64), nullable=True))
    op.add_column('stat_time_to_win', sa.Column('hostname', sa.String(), nullable=True))
    op.add_column('stat_total_chia', sa.Column('hostname', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade_stats():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stat_total_chia', 'hostname')
    op.drop_column('stat_time_to_win', 'hostname')
    op.drop_column('stat_plotting_total_used', 'blockchain')
    op.drop_column('stat_plotting_total_used', 'hostname')
    op.drop_column('stat_plots_total_used', 'hostname')
    op.drop_column('stat_plots_size', 'hostname')
    op.drop_column('stat_plot_count', 'hostname')
    op.drop_column('stat_netspace_size', 'hostname')
    # ### end Alembic commands ###

