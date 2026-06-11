# mcp/src/agents_remember/kernel/memory_init.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/memory_init.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `23f4d7681f7fcd729049c5f27878c84bbb8f8e58` |
| lastVerifiedCommitDate | 2026-05-29T20:24:00+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`memory_init.py` provides the package-owned `c-00-initialize-memory-repo` skill memory scaffold behavior used
by the `memory_init` MCP tool.

## Code Commentary

### Logic

`initialize_memory()` resolves the repo through `McpRuntimeConfig`, plans or
creates the external memory root, standard `system/`, `onboarding/`, and `docs/`
folders, seed system files, and an optional Git repository initialization.

### Invariants And Boundaries

- The memory root comes from the trusted MCP config, not a tool argument.
- Unknown repo ids are rejected before filesystem work starts.
- `dry_run` defaults to `False` (act-by-default): a plain call creates the
  scaffold; `dry_run=true` reports directories, files, and Git initialization
  without mutating.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `memory_init` is wired through the Phase 04 controller. | [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |
| MCP config defines repository memory roots. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |

## Update History

- 2026-05-29T18:35+02:00: Extracted `_create_missing_dirs`, `_create_missing_files`, and `_git_init_result` from `initialize_memory` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-23T13:09+02:00: Created for MCP-owned memory initialization.
