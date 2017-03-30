"""downstream_map

Revision ID: 51cb05927271
Revises: 8302d3bb5f68
Create Date: 2017-02-16 13:46:47.809476

"""

# revision identifiers, used by Alembic.
revision = '51cb05927271'
down_revision = '8302d3bb5f68'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('downstream_map',
    sa.Column('key', sa.String(length=255), nullable=False),
    sa.Column('value', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('key')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('downstream_map')
    # ### end Alembic commands ###