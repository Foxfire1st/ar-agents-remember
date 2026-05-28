# mcp/src/agents_remember/controllers/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `9680d150ac9d2e6c1ae04dbab42eac0088dceef8` |
| lastVerifiedCommitDate | 2026-05-28T15:55:29+02:00                  |
| governingOverview      | `overview.md`                              |

## Purpose

`__init__.py` marks `agents_remember.controllers` as an importable package.

## Code Commentary

The file currently contains no exported controller facade. Public MCP payload
builders import controller functions directly from their domain modules such as
`provider_tools.py`, `worktree_tools.py`, `memory_tools.py`, and
`coordination_tools.py`.

## Invariants And Boundaries

- Keep this package initializer empty unless there is a concrete import-surface
  requirement.
- Do not use it to recreate the old `skill_tools.py` mass facade.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The route overview documents the split controller package layout. | [overview.md](overview.md) |
| Public payload builders import controllers from their owning modules. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |

## Update History

- 2026-05-28T19:52+02:00: Created when the controllers route overview made the package initializer part of the explicit route coverage.
