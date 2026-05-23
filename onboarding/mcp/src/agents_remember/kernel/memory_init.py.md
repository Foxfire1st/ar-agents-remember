# mcp/src/agents_remember/kernel/memory_init.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/memory_init.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:09+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`memory_init.py` provides the package-owned C-00 memory scaffold behavior used
by the `memory_init` MCP tool.

## Code Commentary

### Logic

`initialize_memory()` resolves the repo through `McpRuntimeConfig`, plans or
creates the external memory root, standard `system/`, `onboarding/`, and `docs/`
folders, seed system files, and an optional Git repository initialization.

### Invariants And Boundaries

- The memory root comes from the trusted MCP config, not a tool argument.
- Unknown repo ids are rejected before filesystem work starts.
- `dry_run` reports directories, files, and Git initialization without mutating.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `memory_init` is wired through the Phase 04 controller. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| MCP config defines repository memory roots. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |

## Update History

- 2026-05-23T13:09+02:00: Created for MCP-owned memory initialization.
