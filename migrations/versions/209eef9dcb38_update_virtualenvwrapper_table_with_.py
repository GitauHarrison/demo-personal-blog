"""update virtualenvwrapper table with richtext 

Revision ID: 209eef9dcb38
Revises: cf6706cc0239
Create Date: 2020-10-24 03:49:13.003460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '209eef9dcb38'
down_revision = 'cf6706cc0239'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('virtualenvwrapper_post', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('virtualenvwrapper_post', 'body_html')
    # ### end Alembic commands ###
