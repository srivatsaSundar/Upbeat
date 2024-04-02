"""create account table

Revision ID: 2c0d2a75363d
Revises: 5be8efe8ae2f
Create Date: 2024-04-02 17:06:36.963709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c0d2a75363d'
down_revision: Union[str, None] = '5be8efe8ae2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
