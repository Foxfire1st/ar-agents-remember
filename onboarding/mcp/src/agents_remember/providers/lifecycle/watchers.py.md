# mcp/src/agents_remember/providers/lifecycle/watchers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/watchers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T12:32+02:00                     |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00|
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
a durable process namespace. CGC aggregate status now includes FalkorDB backend
status, and the provider-level `ok` flag requires both backend health and all
configured repo watchers to be ok.

### Invariants And Boundaries

- Watcher aggregation should not perform provider-specific Docker or CGC work
  itself.
- CGC watcher status must include the shared backend status so current provider
  state can distinguish repo watcher health from FalkorDB health.
- Start/stop/shutdown actions must respect durable process namespace checks.
- Partial provider failures should be reported as structured lifecycle results,
  not hidden.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI watcher behavior lives in the Docker runner module. | [grepai/runner.py](agents-remember/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py) |
| CGC start/stop/status behavior lives in the CGC process-control and installation modules. | [cgc/process_control.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py); [cgc/installation.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/installation.py) |
| CGC backend status is reported through the backend module and folded into watcher aggregate status. | [cgc/backend.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| Tests cover aggregate watcher partial result and recovery-action behavior. | [test_provider_lifecycle.py](agents-remember/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-28T12:32+02:00: Updated after CGC watcher status began including FalkorDB backend health in aggregate status packets.
- 2026-05-26T12:51+02:00: Updated after watcher CGC args stopped carrying a Python executable and references moved to process-control/status modules.
- 2026-05-25T19:09+02:00: Updated references after CGC and GrepAI modules moved under package subfolders.
- 2026-05-25T19:01+02:00: Created from watcher aggregation logic extracted out of provider lifecycle.
