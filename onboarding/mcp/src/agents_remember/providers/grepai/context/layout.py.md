# mcp/src/agents_remember/providers/grepai/context/layout.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/layout.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:33+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/layout.py` owns GrepAI memory-root models, provider-owned runtime layout expansion, requirements pin writing, and mirrored index-root syncing.

## Code Commentary

### Logic

It defines `GrepaiMemoryRoot` and `GrepaiRuntimeLayout`, builds the provider runtime/data/config/log/home/cache paths from settings, validates configured memory roots, optionally maps them into provider-owned mirror roots, creates runtime directories, and refreshes mirror roots with `.git`, `.grepai`, and `__pycache__` ignored.

### Invariants And Boundaries

- Runtime state stays under coordinator provider roots such as `providers/runners/grepai` and `providers/data/grepai/postgres`.
- Indexed roots can be mirrored into provider-owned paths so Docker sees stable project paths without writing artifacts into durable memory roots.
- Root paths with unresolved placeholders, missing directories, or sync targets outside the runtime root raise `ContextProviderError`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Workspace YAML rendering consumes `GrepaiRuntimeLayout` and its normalized roots. | [workspace.py](workspace.py.md) |
| Lifecycle GrepAI backend and runner code use this layout through the public context facade. | [backend.py](../lifecycle/backend.py.md); [runner.py](../lifecycle/runner.py.md) |

## Update History

- 2026-05-25T19:33+02:00: Created when GrepAI runtime layout and mirror syncing were split out of `grepai/core.py`.
