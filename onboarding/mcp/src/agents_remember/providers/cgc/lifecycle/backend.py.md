# mcp/src/agents_remember/providers/cgc/lifecycle/backend.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/backend.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T13:58+02:00                     |
| lastVerifiedCommitHash | `45214435fd2de65765a8230ceb1dcfe188d1944d` |
| lastVerifiedCommitDate | 2026-05-27T00:09:33+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`backend.py` owns the managed CodeGraphContext FalkorDB Docker backend.

## Code Commentary

### Logic

The module reports backend status, validates runtime details, removes stale
containers whose data mount no longer matches the configured backend data root,
ensures the shared CGC Docker network exists, connects reused backend containers
to that network, allocates host ports, builds `docker run` commands, starts or
reuses the FalkorDB container, waits for `redis-cli ping`, records backend
state, and writes the backend image lock.

### Invariants And Boundaries

- Managed CGC backend mode must be `falkordb-remote` with Docker.
- Existing containers are reused only when running and mounted to the expected
  provider data root.
- The FalkorDB backend must be attached to the same Docker network used by CGC
  runner and watcher containers.
- Backend state and image lock writes belong here after successful validation.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC backend settings are derived in the CGC core module. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/core.py) |
| Shared Docker helpers provide port allocation, container inspection, data mount checks, and FalkorDB ping polling. | [docker_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/docker_runtime.py); [host_ports.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/host_ports.py) |

## Update History

- 2026-05-26T13:58+02:00: Updated after CGC backend start/status began ensuring and reporting the shared CGC Docker network for runner-to-FalkorDB connectivity.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from the CGC backend lifecycle portion of provider lifecycle and refactored below Radon B complexity.
