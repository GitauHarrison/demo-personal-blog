"""allow comment field in web forms table

Revision ID: 8697b3a19a5e
Revises: 4ce2d137ebad
Create Date: 2021-05-12 12:51:48.679638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8697b3a19a5e'
down_revision = '4ce2d137ebad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flask_web_forms_post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('allowed_comment', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flask_web_forms_post', schema=None) as batch_op:
        batch_op.drop_column('allowed_comment')

    # ### end Alembic commands ###