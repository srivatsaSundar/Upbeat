"""DB changed 2

Revision ID: 616950bcadf9
Revises: 25bb8e341d11
Create Date: 2024-03-22 21:06:22.973460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '616950bcadf9'
down_revision: Union[str, None] = '25bb8e341d11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
