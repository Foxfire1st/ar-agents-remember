# mcp/src/agents_remember/providers/grepai/seed.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/seed.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2`                         |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`seed.py` owns GrepAI workflow-local database clone support for worktree and benchmark warm-starts.

## Code Commentary

### Logic

The module resolves a source and target `grepai-memory` provider from explicit settings, starts both Postgres backends through lifecycle calls, and clones the source database into the target with `pg_dump` piped through a temporary SQL file into `psql`. `GrepaiCloneContext` carries the resolved project id, source/target coordination roots, backend containers, database names, users, passwords, and settings files. Dry-runs return the planned dump/restore commands without touching Docker.

### Invariants And Boundaries

- Source and target GrepAI backend containers must be different; same-container clone requests are skipped instead of mutating the live provider in place.
- The clone is database-level warm-start, not a text rewrite of indexed chunks. The watcher reconciles active-project file changes after target settings point at the workflow-local memory root.
- Source provider settings may come from the current settings file when source and target coordination roots match, or from an explicit source settings path for benchmark/workflow-local copies.
- The module starts backends only; watcher refresh and provider-level sequencing stay in `grepai/setup.py` and `provider_setup.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Isolated GrepAI settings define the target roots and workflow-local backend names used by clone operations. | [isolated.py](isolated.py.md) |
| GrepAI setup calls clone before refresh when seed options are present. | [setup.py](setup.py.md) |
| Provider setup threads source/target settings into GrepAI seed options for worktrees and benchmarks. | [../provider_setup.py](../provider_setup.py.md) |
| Tests cover dry-run clone planning and benchmark-style target settings. | [../../../../../tests/test_provider_setup.py](../../../../../tests/test_provider_setup.py.md) |

## Update History

- 2026-05-29T18:35+02:00: Narrowed the `GrepaiCloneContext | dict` union via `isinstance` and removed the dead `_is_clone_skip`; behavior-preserving (commit `0549b28`).
- 2026-05-27T18:10:12+02:00: Created for GrepAI provider warm-start support.
