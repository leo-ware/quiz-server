"""Recreate database

Revision ID: 969ce4905e41
Revises: 
Create Date: 2020-06-16 13:58:29.216788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '969ce4905e41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=128), nullable=True),
    sa.Column('options', sa.PickleType(), nullable=True),
    sa.Column('correct', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_question'), 'question', ['question'], unique=True)
    op.create_table('quiz',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quiz_name'), 'quiz', ['name'], unique=True)
    op.create_table('questions',
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('quiz_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], ),
    sa.PrimaryKeyConstraint('question_id', 'quiz_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_index(op.f('ix_quiz_name'), table_name='quiz')
    op.drop_table('quiz')
    op.drop_index(op.f('ix_question_question'), table_name='question')
    op.drop_table('question')
    # ### end Alembic commands ###