# mcp/src/agents_remember/providers/provider_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/provider_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:46+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`provider_setup.py` prepares configured context providers from package-local MCP
code. It owns provider dependency install orchestration, worktree CGC seed
preparation, isolated CGC settings generation, and CGC bundle path rewriting.

## Code Commentary

### Logic

The module loads provider authority from an explicit MCP-derived settings file
when one is supplied, otherwise from the coordination root for benchmark-local
legacy fixtures. `action_payload()` coordinates `install` and `prepare` flows by
calling package-local `provider_lifecycle.main()` through command capture rather
than invoking coordinator-local Python scripts.

### Invariants And Boundaries

- MCP worktree provider setup must pass `--from-settings`; it must not depend on
  coordinator `system/settings.json`.
- CGC worktree seed uses the original MCP-derived source settings when the seed
  source and target share a coordination root, and isolated target settings for
  the worktree runtime.
- Child subprocess helpers use `stdin=subprocess.DEVNULL` so provider children
  cannot consume the MCP stdio transport.
- This module is a typed provider setup facade, not a generic shell runner.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Worktree start calls provider setup with MCP-derived provider settings. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Benchmark preparation calls package-local provider setup instead of a source script. | [runner.py](agents-remember-md/mcp/src/agents_remember/benchmarks/runner.py) |
| Provider lifecycle calls are captured through package-local command capture. | [command_capture.py](agents-remember-md/mcp/src/agents_remember/mcp/command_capture.py) |

## Update History

- 2026-05-23T13:46+02:00: Added when provider setup moved from the deleted source `scripts/` route into the MCP package.
