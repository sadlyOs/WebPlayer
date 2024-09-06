"""add relationship between playlist and music

Revision ID: f1db5a87da21
Revises: 3b848d40d554
Create Date: 2024-08-02 07:26:24.234177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1db5a87da21'
down_revision: Union[str, None] = '3b848d40d554'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
