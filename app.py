"""Order lookup service — PRGuard demo (Python).

A minimal slice of a shop backend. All data access goes through the
shared helpers in ``src/db.py``: ``query()`` for parameter-bound SQL and
``money()`` for currency formatting — business code never rolls its own.
"""

from src.db import money, query


def get_order(order_id):
    """Fetch a single order by primary key."""
    rows = query(
        "SELECT id, total_cents, status FROM orders WHERE id = ?",
        (order_id,),
    )
    return rows[0] if rows else None


def order_total(order_id):
    """Return the formatted total for an order, or None if it is missing."""
    order = get_order(order_id)
    return money(order["total_cents"]) if order else None
