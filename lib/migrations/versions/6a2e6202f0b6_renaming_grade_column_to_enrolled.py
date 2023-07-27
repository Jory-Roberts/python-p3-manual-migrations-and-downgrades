"""Renaming grade column to enrolled

Revision ID: 6a2e6202f0b6
Revises: c79a35facd52
Create Date: 2023-07-27 00:16:48.091897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6a2e6202f0b6"
down_revision = "c79a35facd52"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("scholars", "grade", new_column_name="enrolled")


def downgrade() -> None:
    op.alter_column("scholars", "enrolled", new_column_name="grade")
