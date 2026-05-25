# mcp/src/agents_remember/providers/lifecycle_modules/cgc/process.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_modules/cgc/process.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`process.py` owns CodeGraphContext process and bounded-command lifecycle
actions.

## Code Commentary

### Logic

The module starts and stops `cgc watch`, records and validates managed process
state, runs all-root start/stop/refresh operations from settings, refreshes CGC
indexes, runs bounded native CGC commands, and starts visualization servers via
explicit lifecycle actions. It uses detached process helpers for long-running
watch/visualize processes and foreground command helpers for bounded runs.

### Invariants And Boundaries

- Long-running CGC watcher/server actions require a durable process namespace.
- Bounded `cgc run` may execute inside an ephemeral namespace but must reject
  visualizer server commands.
- Backend lifecycle is delegated to `backend.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared process helpers provide durable namespace checks and detached command startup. | [common.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/common.py) |
| CGC status and patch state are provided by the installation module. | [installation.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/installation.py) |
| Tests cover visualizer rejection, dry-run visualize command construction, and bounded `cgc run`. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from CGC process, refresh, run, and visualize logic extracted out of provider lifecycle.
