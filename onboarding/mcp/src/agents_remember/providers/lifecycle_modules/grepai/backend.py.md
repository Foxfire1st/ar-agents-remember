# mcp/src/agents_remember/providers/lifecycle_modules/grepai/backend.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_modules/grepai/backend.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`backend.py` owns the managed GrepAI PostgreSQL/pgvector Docker backend.

## Code Commentary

### Logic

The module waits for Postgres readiness with both `pg_isready` and `SELECT 1`,
creates the `vector` extension, reports backend status, removes mismatched
containers, creates or reuses the Postgres container, connects it to the shared
network, records backend state, and writes the backend image lock.

### Invariants And Boundaries

- GrepAI backend data must live under provider-managed data roots.
- The backend container must be connected to the managed GrepAI Docker network.
- Health is not just container running; database query readiness is required.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Backend settings and Docker network name are derived in GrepAI core. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/core.py) |
| Tests require the Postgres wait helper to run both `pg_isready` and a database query. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI PostgreSQL backend lifecycle extracted out of provider lifecycle.
