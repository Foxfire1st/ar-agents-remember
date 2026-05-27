# mcp/src/agents_remember/providers/grepai/lifecycle/backend.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/backend.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-27T00:25+02:00                     |
| lastVerifiedCommitHash | `f20f75e3e3c6da0c56a6ccfdedfa9d859d7329b7` |
| lastVerifiedCommitDate | 2026-05-27T18:11:35+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`backend.py` owns the managed GrepAI PostgreSQL/pgvector Docker backend.

## Code Commentary

### Logic

The module waits for Postgres readiness with both `pg_isready` and `SELECT 1`,
creates the `vector` extension, reports backend status, removes mismatched
containers, reuses the host port mapping from an already-running backend,
starts Postgres through the package Compose project, records backend state, and
writes the backend image lock. Before Compose startup, it performs GrepAI
project migration: old unmanaged Postgres, Ollama, watcher containers, and the
old unmanaged network are removed only when Docker labels do not show the
expected Compose project.

### Invariants And Boundaries

- GrepAI backend data must live under provider-managed data roots.
- The backend container and network are owned by the GrepAI Compose project
  after migration.
- Health is not just container running; database query readiness is required.
- Existing Compose-managed backend port mappings are reused on repeated starts
  rather than reallocated from host socket availability.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Backend settings and Docker network name are derived in GrepAI core. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/core.py) |
| Tests require the Postgres wait helper to run both `pg_isready` and a database query. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |
| Shared Compose helpers provide unmanaged container and network migration. | [compose_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/compose_runtime.py) |

## Update History

- 2026-05-27T00:25+02:00: Updated after GrepAI backend startup added
  project-wide pre-Compose migration and existing-port reuse for Compose
  restarts.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI PostgreSQL backend lifecycle extracted out of provider lifecycle.
