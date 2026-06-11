# mcp/src/agents_remember/providers/cgc/lifecycle/backend.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/backend.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T06:20+02:00|
| lastVerifiedCommitHash | `6beccd0545a2d5c161059715d5ed7830917eba03` |
| lastVerifiedCommitDate | 2026-06-09T22:39:28+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`backend.py` owns the managed CodeGraphContext FalkorDB Docker backend.

## Code Commentary

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC backend settings are derived in the CGC core module. | [core.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/core.py) |
| Shared Docker and Compose helpers provide port inspection/allocation, data mount checks, FalkorDB ping polling, and unmanaged migration. | [docker_runtime.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/docker_runtime.py); [host_ports.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/host_ports.py); [compose_runtime.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/compose_runtime.py) |

## Update History

- 2026-06-10T06:20+02:00 — Body-quality pass: merged the `dataDestination` mount-verification and migration mechanics into Logic and extended the container-reuse invariant with the destination-sync rule (documentation only).
- 2026-06-09T22:10+02:00 — Mount verification (`cgc_backend_runtime_details`, `cgc_backend_remove_mismatched_container`) now checks the mount at the configured backend `dataDestination` instead of hardcoded `/data`; an existing container mounted at the old destination is treated as mismatched and recreated on the next backend start (the built-in migration path for the persistence fix).
- 2026-05-31T12:50+02:00 — Re-typed `layout` params and `layouts` lists from bare `Any` to `CgcRuntimeLayout` (newly imported from `agents_remember.providers.context`) across the backend helpers; behavior-preserving, added a layout-type note to Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Fixed `cgc_backend_dry_run_result` `commands` type to `list[dict[str, Any]]` (compose-plan dicts, not arg lists); behavior-preserving (commit `0549b28`).
- 2026-05-28T12:32+02:00: Updated after backend status began including normalized container-state summaries.
- 2026-05-27T00:25+02:00: Updated after CGC backend startup added
  project-wide pre-Compose migration and existing-port reuse for repeated
  Compose starts.
- 2026-05-26T13:58+02:00: Updated after CGC backend start/status began ensuring and reporting the shared CGC Docker network for runner-to-FalkorDB connectivity.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from the CGC backend lifecycle portion of provider lifecycle and refactored below Radon B complexity.
