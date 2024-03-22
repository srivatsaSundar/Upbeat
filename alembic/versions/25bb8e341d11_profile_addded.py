"""profile addded

Revision ID: 25bb8e341d11
Revises: c77e17e1e327
Create Date: 2024-03-22 21:03:16.879596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25bb8e341d11'
down_revision: Union[str, None] = 'c77e17e1e327'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
