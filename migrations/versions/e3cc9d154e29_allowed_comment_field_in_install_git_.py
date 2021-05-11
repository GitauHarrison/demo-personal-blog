"""allowed comment field in install git table

Revision ID: e3cc9d154e29
Revises: 6ee66bda73f2
Create Date: 2021-05-11 15:37:19.181178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3cc9d154e29'
down_revision = '6ee66bda73f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('install_git_post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('allowed_comment', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('install_git_post', schema=None) as batch_op:
        batch_op.drop_column('allowed_comment')

    # ### end Alembic commands ###
