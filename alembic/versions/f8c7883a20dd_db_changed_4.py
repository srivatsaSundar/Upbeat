"""DB changed 4

Revision ID: f8c7883a20dd
Revises: f5ed00903cb5
Create Date: 2024-03-22 23:03:09.398437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8c7883a20dd'
down_revision: Union[str, None] = 'f5ed00903cb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
