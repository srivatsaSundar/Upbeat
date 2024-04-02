"""empty message

Revision ID: e07a1a5bcc35
Revises: 2c0d2a75363d
Create Date: 2024-04-02 17:52:06.981714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e07a1a5bcc35'
down_revision: Union[str, None] = '2c0d2a75363d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
