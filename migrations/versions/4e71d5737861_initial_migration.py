"""Initial migration.

Revision ID: 4e71d5737861
Revises: 
Create Date: 2021-03-05 11:18:33.984585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e71d5737861'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('camara',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('lens', sa.Integer(), nullable=True),
    sa.Column('azimuth', sa.Float(), nullable=True),
    sa.Column('elevation', sa.Float(), nullable=True),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('ground_elevation', sa.Integer(), nullable=True),
    sa.Column('start_record_datetime', sa.DateTime(), nullable=True),
    sa.Column('stop_record_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('camara')
    # ### end Alembic commands ###
