# mcp/src/agents_remember/providers/grepai/lifecycle/backend.py

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

## Evidence

### Repo-Internal References

- Backend settings and Docker network name are derived in GrepAI core. [1]
- Tests require the Postgres wait helper to run both "test: [\"CMD-SHELL\", \"pg_isready -U grepai -d grepai\"]" and a database query. [2]
- Shared Compose helpers provide unmanaged container and network migration. [3]
