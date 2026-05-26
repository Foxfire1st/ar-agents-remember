# mcp/src/agents_remember/providers/cgc/context/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/context/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T13:58+02:00                     |
| lastVerifiedCommitHash | `2e2117a194ab1576c860dbca39b6acff0d1c20fa` |
| lastVerifiedCommitDate | 2026-05-26T14:55:50+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/core.py` owns CodeGraphContext runtime layout derivation, Docker runner
layout fields, provider-owned config writing, source artifact detection, and
stale runtime cleanup.

## Code Commentary

### Logic

It defines `CgcRuntimeLayout`, builds layouts from direct parameters or provider
settings, derives FalkorDB host/port from provider settings plus backend state,
derives Docker runner image/build/lock/container paths, tracks the backend
container name and shared Docker network name for runner connectivity, writes
managed `.cgcignore`, config, and `.env` files, detects source-tree CGC
artifacts, and removes only generated or obsolete provider runtime artifacts
inside validated provider roots. Runtime directory creation no longer creates
provider venv directories.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.
- Managed CGC execution is Docker-owned; host venv fields may be parsed from
  old settings but are not created as runtime directories.
- Docker runner command builders consume layout-level backend container and
  network names; layout derivation must keep those synchronized with backend
  settings.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Lifecycle CGC modules use these layout and cleanup helpers before running or installing CGC. | [core.py](../lifecycle/core.py.md); [installation.py](../lifecycle/installation.py.md); [process_control.py](../lifecycle/process_control.py.md); [runner.py](../lifecycle/runner.py.md) |

## Update History

- 2026-05-26T13:58+02:00: Updated after CGC layouts gained backend container and Docker network fields for runner connectivity.
- 2026-05-26T12:51+02:00: Updated after CGC layout gained Docker runner fields and stopped creating host venv directories.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
