"""DB changed 5

Revision ID: 2563a40906eb
Revises: f8c7883a20dd
Create Date: 2024-03-22 23:15:35.635797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2563a40906eb'
down_revision: Union[str, None] = 'f8c7883a20dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
