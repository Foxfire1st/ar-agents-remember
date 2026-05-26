# mcp/src/agents_remember/providers/lifecycle/watchers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/watchers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `2e2117a194ab1576c860dbca39b6acff0d1c20fa` |
| lastVerifiedCommitDate | 2026-05-26T14:55:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`watchers.py` aggregates enabled provider watcher lifecycle operations across
GrepAI and CodeGraphContext.

## Code Commentary

### Logic

The module reads provider enablement from lifecycle settings, maps generic
watcher actions to provider-specific actions, calls GrepAI or CGC lifecycle
functions, normalizes provider errors into structured results, and collects
recovery actions from partial failures. Non-dry-run long-running actions require
a durable process namespace.

### Invariants And Boundaries

- Watcher aggregation should not perform provider-specific Docker or CGC work
  itself.
- Start/stop/shutdown actions must respect durable process namespace checks.
- Partial provider failures should be reported as structured lifecycle results,
  not hidden.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI watcher behavior lives in the Docker runner module. | [grepai/runner.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py) |
| CGC start/stop/status behavior lives in the CGC process-control and installation modules. | [cgc/process_control.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py); [cgc/installation.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/installation.py) |
| Tests cover aggregate watcher partial result and recovery-action behavior. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-26T12:51+02:00: Updated after watcher CGC args stopped carrying a Python executable and references moved to process-control/status modules.
- 2026-05-25T19:09+02:00: Updated references after CGC and GrepAI modules moved under package subfolders.
- 2026-05-25T19:01+02:00: Created from watcher aggregation logic extracted out of provider lifecycle.
