"""totp new allowed field

Revision ID: 4c7ccb6401b7
Revises: d23fc7b2c0b0
Create Date: 2021-05-03 03:15:22.413683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c7ccb6401b7'
down_revision = 'd23fc7b2c0b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tot_p2fa_post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('allowed_comment', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tot_p2fa_post', schema=None) as batch_op:
        batch_op.drop_column('allowed_comment')

    # ### end Alembic commands ###