"""changes in model2

Revision ID: 8de300ce3123
Revises: de3ae0ef5e47
Create Date: 2024-04-01 23:07:32.894662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8de300ce3123'
down_revision: Union[str, None] = 'de3ae0ef5e47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
