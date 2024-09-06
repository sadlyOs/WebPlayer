"""add user_id

Revision ID: f834f360e5a8
Revises: f1db5a87da21
Create Date: 2024-08-02 07:42:01.790518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f834f360e5a8'
down_revision: Union[str, None] = 'f1db5a87da21'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
