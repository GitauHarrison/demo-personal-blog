"""github ssh table

Revision ID: 0da674f89468
Revises: 286b98e52b84
Create Date: 2021-03-27 06:46:27.177079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0da674f89468'
down_revision = '286b98e52b84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('github_ssh_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=500), nullable=True),
    sa.Column('body_html', sa.String(length=500), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_github_ssh_post_timestamp'), 'github_ssh_post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_github_ssh_post_timestamp'), table_name='github_ssh_post')
    op.drop_table('github_ssh_post')
    # ### end Alembic commands ###