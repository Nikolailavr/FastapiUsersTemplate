"""init1

Revision ID: 45e816ebc5c2
Revises: f569fce560fb
Create Date: 2025-04-13 00:39:22.071649

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "45e816ebc5c2"
down_revision: Union[str, None] = "f569fce560fb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("phone", sa.String(), nullable=False))
    op.create_unique_constraint(op.f("uq_users_phone"), "users", ["phone"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f("uq_users_phone"), "users", type_="unique")
    op.drop_column("users", "phone")
