"""empty message

Revision ID: 994f5d4ced41
Revises: bb9c397a99f0
Create Date: 2024-04-02 18:41:54.186075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '994f5d4ced41'
down_revision: Union[str, None] = 'bb9c397a99f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
