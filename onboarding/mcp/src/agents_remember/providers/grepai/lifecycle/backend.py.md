# mcp/src/agents_remember/providers/grepai/lifecycle/backend.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/backend.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`backend.py` owns the managed GrepAI PostgreSQL/pgvector Docker backend.

## Code Commentary

### 260731-EFA-L2 Backend Context

`grepai_backend_start_context(args)` returns the frozen **`GrepaiBackendContext(settings_path,
provider_settings, layout, backend, network_name)`** instead of a tuple — which settings file the
invocation read, the provider entry it found, the runtime layout, the resolved backend settings,
and the docker network the backend joins. Every backend command needs all of it. Host
reconciliation before the container comes up is reported through `BackendStartReconciliation`
(`network` / `migration` / `forced_remove`) from `lifecycle/compose_runtime.py`.

### Logic

The module waits for Postgres readiness with both `pg_isready` and `SELECT 1`,
creates the `vector` extension, reports backend status, removes mismatched
containers, reuses the host port mapping from an already-running backend,
starts Postgres through the package Compose project, records backend state, and
writes the backend image lock. For new `auto` host-port allocations it prefers
`GREPAI_POSTGRES_DEFAULT_PORT` (`61432`) while keeping the container-side
Postgres port at `5432`. Status includes a normalized Docker container
state summary so MCP provider status can report backend state and uptime.
Before Compose startup, it performs GrepAI project migration: old unmanaged
Postgres, Ollama, watcher containers, and the old unmanaged network are removed
only when Docker labels do not show the expected Compose project.

### Invariants And Boundaries

- GrepAI backend data must live under provider-managed data roots.
- The backend container and network are owned by the GrepAI Compose project
  after migration.
- Health is not just container running; database query readiness is required.
- Existing Compose-managed backend port mappings are reused on repeated starts
  rather than reallocated from host socket availability.
- The preferred host port avoids neighboring Postgres services; the container
  port remains the actual Postgres service port.
- Backend status should expose enough Docker state for current provider status
  without requiring callers to inspect containers themselves.
- The `layout` parameter threaded through these helpers is the shared
  `GrepaiRuntimeLayout` dataclass (re-exported via the `core` wildcard import),
  not an untyped object; callers rely on its `backend_root`,
  `backend_data_root`, `backend_state_file`, and `coordination_root` attributes.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Backend settings and Docker network name are derived in GrepAI core. | `grepai_backend_settings`, `grepai_network_name` | mcp/src/agents_remember/providers/grepai/lifecycle/core.py:148-152; mcp/src/agents_remember/providers/grepai/lifecycle/core.py:339-362 |
| Tests require the Postgres wait helper to run both `pg_isready` and a database query. | `pg_isready` | mcp/tests/test_provider_lifecycle.py:1139-1139 |
| Shared Compose helpers provide unmanaged container and network migration. | `remove_unmanaged_compose_container`, `remove_unmanaged_compose_network` | mcp/src/agents_remember/providers/lifecycle/compose_runtime.py:252-269; mcp/src/agents_remember/providers/lifecycle/compose_runtime.py:272-289 |

## Update History

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 2 citation rows; scoped citation fixing regenerated the source ranges.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `grepai_backend_start_context` now returns `GrepaiBackendContext`, and the host-reconciliation
  trio travels as `BackendStartReconciliation`. Emitted payloads are unchanged. Verification
  metadata pinned until closeout stamps the L2 commit.
- 2026-06-25T09:55+02:00 — `auto` host-port selection now uses the centralized GrepAI Postgres preferred host port (`61432`) instead of preferring host `5432`; existing mappings and explicit configured ports still win.
- 2026-06-10T07:30+02:00 — No content impact: import path updated to `providers/context_common.py` (shared helpers moved out of the facade package, GitHub #58); documented behavior unchanged.
- 2026-06-10T05:30+02:00 — Leaf imports replace the `providers.context` aggregator import (circular-import fix; see core.py 2026-06-10 entry).
- 2026-05-31T12:50+02:00 — `layout` params (and the `grepai_backend_start_context` return tuple) re-typed `Any` -> `GrepaiRuntimeLayout` across the backend helpers; behavior-preserving type-only tightening, added an Invariants note that `layout` is the shared `GrepaiRuntimeLayout` dataclass (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `grepai_backend_dry_run_result` `commands` -> `list[dict[str, Any]]`; `raise_postgres_timeout` -> `NoReturn`; behavior-preserving (commit `0549b28`).
- 2026-05-28T12:32+02:00: Updated after GrepAI backend status began including normalized container-state summaries.
- 2026-05-27T00:25+02:00: Updated after GrepAI backend startup added
  project-wide pre-Compose migration and existing-port reuse for Compose
  restarts.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI PostgreSQL backend lifecycle extracted out of provider lifecycle.
