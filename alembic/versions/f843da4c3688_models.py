"""models

Revision ID: f843da4c3688
Revises: 2563a40906eb
Create Date: 2024-03-30 19:45:41.687554

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f843da4c3688'
down_revision: Union[str, None] = '2563a40906eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
