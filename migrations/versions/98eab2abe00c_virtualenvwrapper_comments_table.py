"""virtualenvwrapper comments table

Revision ID: 98eab2abe00c
Revises: 5ca8760663f8
Create Date: 2020-10-23 13:31:50.894436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98eab2abe00c'
down_revision = '5ca8760663f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('virtualenvwrapper_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=500), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_virtualenvwrapper_post_timestamp'), 'virtualenvwrapper_post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_virtualenvwrapper_post_timestamp'), table_name='virtualenvwrapper_post')
    op.drop_table('virtualenvwrapper_post')
    # ### end Alembic commands ###
