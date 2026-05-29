# mcp/src/agents_remember/providers/cgc/lifecycle/backend.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/backend.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
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
writes the backend image lock. Status includes a normalized Docker container
state summary so MCP provider status can report backend state and uptime.
Before Compose startup, it performs CGC project migration: old unmanaged
FalkorDB and watcher containers plus the old unmanaged network are removed only
when Docker labels do not show the expected Compose project.

### Invariants And Boundaries

- Managed CGC backend mode must be `falkordb-remote` with Docker.
- Existing containers are reused only when running and mounted to the expected
  provider data root.
- The FalkorDB backend and network are owned by the CGC Compose project after
  migration.
- Backend state and image lock writes belong here after successful validation.
- Existing Compose-managed backend port mappings are reused on repeated starts
  rather than reallocated from host socket availability.
- Backend status should expose enough Docker state for current provider status
  without requiring callers to inspect containers themselves.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC backend settings are derived in the CGC core module. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/core.py) |
| Shared Docker and Compose helpers provide port inspection/allocation, data mount checks, FalkorDB ping polling, and unmanaged migration. | [docker_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/docker_runtime.py); [host_ports.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/host_ports.py); [compose_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/compose_runtime.py) |

## Update History

- 2026-05-29T18:35+02:00: Fixed `cgc_backend_dry_run_result` `commands` type to `list[dict[str, Any]]` (compose-plan dicts, not arg lists); behavior-preserving (commit `0549b28`).
- 2026-05-28T12:32+02:00: Updated after backend status began including normalized container-state summaries.
- 2026-05-27T00:25+02:00: Updated after CGC backend startup added
  project-wide pre-Compose migration and existing-port reuse for repeated
  Compose starts.
- 2026-05-26T13:58+02:00: Updated after CGC backend start/status began ensuring and reporting the shared CGC Docker network for runner-to-FalkorDB connectivity.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from the CGC backend lifecycle portion of provider lifecycle and refactored below Radon B complexity.
