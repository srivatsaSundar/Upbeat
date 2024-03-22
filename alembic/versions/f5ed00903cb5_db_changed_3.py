"""DB changed 3

Revision ID: f5ed00903cb5
Revises: 616950bcadf9
Create Date: 2024-03-22 22:56:59.751138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5ed00903cb5'
down_revision: Union[str, None] = '616950bcadf9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
