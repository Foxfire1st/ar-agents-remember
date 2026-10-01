# mcp/src/agents_remember/providers/cgc/lifecycle/backend.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`backend.py` owns the managed CodeGraphContext FalkorDB Docker backend.

## Code Commentary

### 260731-EFA-L2 Backend Context And Port Identity

`cgc_primary_backend_context(args)` and `cgc_backend_start_context(args)` now return the frozen
**`CgcBackendContext(settings_path, provider_settings, layouts, backend)`** instead of a
five-tuple. `context.layout` is a property returning `layouts[0]` — the primary layout the backend
commands act through, since the FalkorDB backend is shared across every configured repo layout.
Every backend command needs the whole context, so unpacking is gone.

Published ports are named rather than spelled out per call. **`CgcBackendPort(state_key, host_key,
host_port_key, container_port_key)`** exists because a published port is spread across three
dictionaries — the recorded backend state, the resolved backend settings, and the container
inspect data — under a different key in each, so **the key set is the port's identity**. The two
module-level instances `FALKORDB_PORT` and `BROWSER_PORT` are what `cgc_backend_endpoint(state,
backend, inspect_data, port)` is called with. **`CgcHostPorts(falkordb, browser)`** names the host
ports one backend container publishes. Host reconciliation before a start is reported through
`BackendStartReconciliation` (from `lifecycle/compose_runtime.py`).

### Logic

The module reports backend status, validates runtime details, removes stale
containers whose data mount no longer matches the configured backend data root,
reuses already-running backend host port mappings, starts FalkorDB through the
package Compose project, waits for `redis-cli ping`, records backend state, and
writes the backend image lock. Mount verification
(`cgc_backend_runtime_details`, `cgc_backend_remove_mismatched_container`)
checks the data mount at the backend settings' configured `dataDestination` —
the container path the backend image actually persists to
(`/var/lib/falkordb/data` for FalkorDB v4, which ignores the legacy `/data`) —
rather than a hardcoded path. A container still mounted at an old destination
is therefore classified as mismatched and recreated on the next backend start,
which doubles as the in-place migration path for hosts that ran the
pre-persistence-fix layout. Status includes a normalized Docker container
state summary so MCP provider status can report backend state and uptime.
Before Compose startup, it performs CGC project migration: old unmanaged
FalkorDB and watcher containers plus the old unmanaged network are removed only
when Docker labels do not show the expected Compose project.

### Invariants And Boundaries

- Managed CGC backend mode must be `falkordb-remote` with Docker.
- Existing containers are reused only when running and mounted to the expected
  provider data root at the configured `dataDestination`; keep that destination
  synchronized with where the backend image version actually writes, or
  persistence silently lands in the container's ephemeral layer.
- The FalkorDB backend and network are owned by the CGC Compose project after
  migration.
- Backend state and image lock writes belong here after successful validation.
- Existing Compose-managed backend port mappings are reused on repeated starts
  rather than reallocated from host socket availability.
- Backend status should expose enough Docker state for current provider status
  without requiring callers to inspect containers themselves.
- Layout parameters and layout lists are typed as `CgcRuntimeLayout` (imported
  from `agents_remember.providers.context`), not bare `Any`.

## Evidence

### Repo-Internal References

- CGC backend settings are derived in the CGC core module. [1]
- Shared Docker and Compose helpers provide port inspection/allocation, data mount checks, FalkorDB ping polling, and unmanaged migration. [2]
