"""changes in model

Revision ID: de3ae0ef5e47
Revises: 29490f139295
Create Date: 2024-04-01 23:07:24.165220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de3ae0ef5e47'
down_revision: Union[str, None] = '29490f139295'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
