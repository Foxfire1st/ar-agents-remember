# mcp/src/agents_remember/providers/lifecycle_modules/watchers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_modules/watchers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
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
| GrepAI watcher behavior lives in the Docker runner module. | [grepai/runner.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/runner.py) |
| CGC start/stop/status behavior lives in the CGC process module. | [cgc/process.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/process.py) |
| Tests cover aggregate watcher partial result and recovery-action behavior. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-25T19:09+02:00: Updated references after CGC and GrepAI modules moved under package subfolders.
- 2026-05-25T19:01+02:00: Created from watcher aggregation logic extracted out of provider lifecycle.
