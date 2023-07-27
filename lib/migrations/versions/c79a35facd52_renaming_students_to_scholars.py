"""Renaming students to scholars

Revision ID: c79a35facd52
Revises: 791279dd0760
Create Date: 2023-07-27 00:04:49.370184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c79a35facd52"
down_revision = "791279dd0760"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students", "scholars")


def downgrade() -> None:
    op.rename_table("scholars", "students")
