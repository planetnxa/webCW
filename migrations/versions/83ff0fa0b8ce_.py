"""empty message

Revision ID: 83ff0fa0b8ce
Revises: a30f4d50ff17
Create Date: 2023-12-13 14:44:00.435679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83ff0fa0b8ce'
down_revision = 'a30f4d50ff17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item_init',
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], )
    )
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_index('ix_order_stock_bought')
        batch_op.drop_column('stock_bought')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stock_bought', sa.VARCHAR(length=500), nullable=True))
        batch_op.create_index('ix_order_stock_bought', ['stock_bought'], unique=False)

    op.drop_table('item_init')
    # ### end Alembic commands ###