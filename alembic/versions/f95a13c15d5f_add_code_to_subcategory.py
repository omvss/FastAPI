from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer
from typing import Union, Sequence

# revision identifiers
revision: str = 'f95a13c15d5f'
down_revision: Union[str, Sequence[str], None] = '4411a6472b78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add column as nullable first
    op.add_column('subcategories', sa.Column('code', sa.String(), nullable=True))

    # Reference table
    subcategories = table('subcategories',
                          column('id', Integer),
                          column('code', String))

    # Populate existing rows with unique codes
    conn = op.get_bind()
    rows = conn.execute(sa.select(subcategories.c.id)).fetchall()
    for i, row in enumerate(rows, start=1):
        conn.execute(
            subcategories.update()
            .where(subcategories.c.id == row.id)
            .values(code=f"subcat_{i}")
        )

    # Alter column to NOT NULL
    op.alter_column('subcategories', 'code', nullable=False)

    # Create unique index
    op.create_index(op.f('ix_subcategories_code'), 'subcategories', ['code'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_subcategories_code'), table_name='subcategories')
    op.drop_column('subcategories', 'code')
