"""stripe in flask table

Revision ID: 8c7dda6a8a7c
Revises: e3d2b6c1025a
Create Date: 2021-03-28 06:08:40.041968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c7dda6a8a7c'
down_revision = 'e3d2b6c1025a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stripe_in_flask_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=500), nullable=True),
    sa.Column('body_html', sa.String(length=500), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stripe_in_flask_post_timestamp'), 'stripe_in_flask_post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stripe_in_flask_post_timestamp'), table_name='stripe_in_flask_post')
    op.drop_table('stripe_in_flask_post')
    # ### end Alembic commands ###