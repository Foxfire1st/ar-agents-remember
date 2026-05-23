# mcp/src/agents_remember/worktrees/git_worktree_manager.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/git_worktree_manager.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T00:35+02:00                     |
| lastVerifiedCommitHash | `ddf6fcd5981664813c915e94e1c5229b542a28a4` |
| lastVerifiedCommitDate | 2026-05-24T00:25:39+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`git_worktree_manager.py` is the package-local C-09 worktree lifecycle
implementation behind MCP worktree tools.

## Code Commentary

### Logic

The module creates and attaches code/memory worktrees, writes task contracts,
reports lifecycle status, performs closeout, integrates completed branches, and
cleans up registered worktrees. During `start`, provider setup now calls
package-local `provider_setup.run_provider_setup()` with a typed
`ProviderSetupRequest` and the generated provider settings path supplied by the
MCP controller.

The MCP path calls result-returning service functions such as `start_result()`,
`closeout_result()`, `integrate_result()`, and `cleanup_result()`. CLI command
functions remain print adapters over those payloads, so MCP controllers no
longer need to run `main(argv)` and parse stdout.

### Invariants And Boundaries

- Worktree provider setup must not invoke `<coordinationRoot>/scripts`.
- Provider enablement and roots come from MCP-derived provider settings, not
  coordinator `system/settings.json`.
- Worktree provider setup should pass typed provider setup options directly and
  should not round-trip through provider setup CLI parsing.
- MCP worktree tools should call result-returning functions directly; CLI
  commands should remain adapters for operator use.
- Git subprocesses use `stdin=subprocess.DEVNULL` so they cannot consume MCP
  stdio.
- Contract paths and worktree roots must stay inside the resolved coordination
  workflow model.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP worktree start writes temporary lifecycle settings and passes them to this module. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Provider setup performs isolated CGC seed and runtime preparation. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |
| Worktree contract serialization lives in the package worktree contract module. | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## Update History

- 2026-05-23T23:46+02:00: Updated after worktree provider setup stopped rebuilding provider setup CLI `argv` and switched to `ProviderSetupRequest`.
- 2026-05-24T00:35+02:00: Updated after MCP worktree controllers switched from `main(argv)` capture to result-returning service functions.
- 2026-05-23T13:46+02:00: Documented the MCP-owned provider setup path and removal of coordinator-local script execution.
