# mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`process_control.py` owns CodeGraphContext watcher process start/stop lifecycle
and all-root start/stop aggregation.

## Code Commentary

### Logic

The module builds dry-run watch commands, starts the managed FalkorDB backend
when settings-backed roots require it, detects already-running managed PIDs,
starts detached `cgc watch`, records provider state, validates stop PIDs, marks
stopped state, and aggregates start/stop results across configured roots.

### Invariants And Boundaries

- Long-running watcher start/stop operations require a durable process
  namespace.
- Backend lifecycle is delegated to `backend.py`.
- Refresh and bounded query behavior live in sibling lifecycle modules.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared process helpers provide durable namespace checks and detached command startup. | [process_status.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/process_status.py); [command_runner.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/command_runner.py) |
| CGC backend startup is delegated to the backend module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |

## Update History

- 2026-05-25T21:14+02:00: Split from `process.py` so watcher process control is separate from refresh and bounded query commands.
