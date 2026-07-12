# Context file — PRGuard demo (Python)

## About this service

A tiny order-lookup API: `app.py` holds the business logic, `src/db.py`
holds the sanctioned data helpers (parameter-bound SQL and money formatting).

## Standards

- **Secrets.** Credentials are never committed. A key that reaches a
  commit is *compromised*: it must be rotated with the provider, not
  merely moved to an environment variable.
- **Money.** Amounts are stored as an integer number of cents and are
  formatted only through the shared `money()` helper — see @ref:src/db.py.
  Never build a currency string by hand: dividing cents by 100 uses
  floating point, which loses precision and drops trailing zeros.
  Treat violations of this rule as WARNING severity — a correctness
  risk to fix, not a blocking security error.
- Functions stay small and single-purpose.

## Out of scope

- Performance tuning
- Test coverage
