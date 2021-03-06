"""empty message

Revision ID: 4bd70d9c0760
Revises: 3c89c15d292d
Create Date: 2021-03-06 18:09:35.171563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bd70d9c0760'
down_revision = '3c89c15d292d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('completed', sa.Boolean(), nullable=True))
    op.execute('UPDATE todolists SET completed = False WHERE completed IS NULL;')
    # ### end Alembic commands ###

    op.alter_column('todolists', 'completed', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todolists', 'completed')
    # ### end Alembic commands ###
