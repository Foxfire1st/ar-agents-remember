# mcp/src/agents_remember/providers/provider_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/provider_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T23:46+02:00                     |
| lastVerifiedCommitHash | `7a12e014c773612105fb91e897c94c9808a61527` |
| lastVerifiedCommitDate | 2026-05-23T23:56:58+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`provider_setup.py` prepares configured context providers from package-local MCP
code. It owns provider dependency install orchestration, worktree CGC seed
preparation, isolated CGC settings generation, and CGC bundle path rewriting.

## Code Commentary

### Logic

The module requires provider authority from an explicit settings file and no
longer falls back to `<coordinationRoot>/system/settings.json`.
`ProviderSetupRequest` is the service front door used by MCP-adjacent callers,
with typed CGC seed and isolated-runtime options for worktree and benchmark
flows. The CLI remains a dev/operator wrapper that parses arguments into the
same request shape and requires `--from-settings`.

### Invariants And Boundaries

- MCP worktree provider setup must pass `--from-settings`; it must not depend on
  coordinator `system/settings.json`.
- `run_provider_setup(ProviderSetupRequest)` is the package service entry point;
  worktree and benchmark callers should not rebuild provider setup CLI `argv`.
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

- 2026-05-23T23:46+02:00: Updated after Phase 05 F-05 made provider setup require explicit settings and added the typed `ProviderSetupRequest` service front door.
- 2026-05-23T13:46+02:00: Added when provider setup moved from the deleted source `scripts/` route into the MCP package.
