"""changes in pkl

Revision ID: 6e28c613e32c
Revises: f843da4c3688
Create Date: 2024-04-01 22:27:42.559951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e28c613e32c'
down_revision: Union[str, None] = 'f843da4c3688'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
