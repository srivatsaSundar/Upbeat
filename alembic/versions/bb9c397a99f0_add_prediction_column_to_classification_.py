"""Add prediction column to Classification mental health table

Revision ID: bb9c397a99f0
Revises: 28126f0a2c7d
Create Date: 2024-04-02 17:13:48.119778

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb9c397a99f0'
down_revision: Union[str, None] = '28126f0a2c7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('classification_mental_health', sa.Column('prediction', sa.String(length=255), nullable=True))


def downgrade() -> None:
    pass
