"""empty message

Revision ID: f38223e26838
Revises: 
Create Date: 2020-03-05 13:59:18.273516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f38223e26838'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('company_name', sa.String(length=30), nullable=False),
    sa.Column('area_of_business', sa.String(length=40), nullable=False),
    sa.Column('office_address', sa.String(length=40), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('company_role', sa.String(length=20), nullable=False),
    sa.Column('num_employees', sa.Integer(), nullable=False),
    sa.Column('num_departments', sa.Integer(), nullable=False),
    sa.Column('register_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('results__data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('result', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results__data')
    op.drop_table('question')
    op.drop_table('admin')
    # ### end Alembic commands ###