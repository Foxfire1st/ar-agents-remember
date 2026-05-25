# mcp/src/agents_remember/providers/lifecycle_modules/cgc/backend.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_modules/cgc/backend.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`backend.py` owns the managed CodeGraphContext FalkorDB Docker backend.

## Code Commentary

### Logic

The module reports backend status, validates runtime details, removes stale
containers whose data mount no longer matches the configured backend data root,
allocates host ports, builds `docker run` commands, starts or reuses the
FalkorDB container, waits for `redis-cli ping`, records backend state, and
writes the backend image lock.

### Invariants And Boundaries

- Managed CGC backend mode must be `falkordb-remote` with Docker.
- Existing containers are reused only when running and mounted to the expected
  provider data root.
- Backend state and image lock writes belong here after successful validation.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC backend settings are derived in the CGC core module. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/core.py) |
| Shared Docker helpers provide port allocation, container inspection, data mount checks, and FalkorDB ping polling. | [common.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/common.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from the CGC backend lifecycle portion of provider lifecycle and refactored below Radon B complexity.
