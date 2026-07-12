"""Shared data helpers — the only sanctioned way to touch orders.

``query()`` binds every value as a driver-level parameter, so SQL
injection is structurally impossible. ``money()`` formats an integer
number of cents as currency without floating-point rounding. Business
code uses these helpers rather than rolling its own.
"""

import sqlite3

DB_PATH = "orders.db"


def query(sql, params=()):
    """Run *sql* with *params* bound by the driver; return all rows."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute(sql, params).fetchall()


def money(cents):
    """Format an integer number of *cents* as currency, e.g. 1299 → '$12.99'."""
    return f"${cents // 100}.{cents % 100:02d}"
