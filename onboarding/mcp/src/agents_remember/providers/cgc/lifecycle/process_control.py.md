# mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `45214435fd2de65765a8230ceb1dcfe188d1944d` |
| lastVerifiedCommitDate | 2026-05-27T00:09:33+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`process_control.py` owns CodeGraphContext watcher container start/stop
lifecycle and all-root start/stop aggregation.

## Code Commentary

### Logic

The module builds dry-run Docker watcher commands, starts the managed FalkorDB
backend when settings-backed roots require it, detects already-running watcher
containers, starts `cgc watch` inside the CGC runner image, records provider
state, removes watcher containers on stop, marks stopped state, and aggregates
start/stop results across configured roots.

### Invariants And Boundaries

- Long-running watcher start/stop operations require a durable process
  namespace even though Docker owns the actual watcher lifetime.
- Backend lifecycle is delegated to `backend.py`.
- Refresh and bounded query behavior live in sibling lifecycle modules.
- Host PIDs are not a managed CGC contract; watcher state is tracked by Docker
  container name.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared process helpers provide durable namespace checks and command execution. | [process_status.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/process_status.py); [command_runner.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/command_runner.py) |
| CGC backend startup is delegated to the backend module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| Docker watcher command construction lives in the runner module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |

## Update History

- 2026-05-26T12:51+02:00: Updated after watcher start/stop moved from host PIDs to Docker watcher containers.
- 2026-05-25T21:14+02:00: Split from `process.py` so watcher process control is separate from refresh and bounded query commands.
