"""changes in model

Revision ID: 29490f139295
Revises: 6e28c613e32c
Create Date: 2024-04-01 22:50:41.148586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29490f139295'
down_revision: Union[str, None] = '6e28c613e32c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
