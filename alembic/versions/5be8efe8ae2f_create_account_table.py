"""create account table

Revision ID: 5be8efe8ae2f
Revises: 8de300ce3123
Create Date: 2024-04-02 17:04:51.013146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5be8efe8ae2f'
down_revision: Union[str, None] = '8de300ce3123'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
