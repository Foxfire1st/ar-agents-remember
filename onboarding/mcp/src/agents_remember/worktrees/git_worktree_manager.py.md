# mcp/src/agents_remember/worktrees/git_worktree_manager.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/git_worktree_manager.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:46+02:00                     |
| lastVerifiedCommitHash | `d445e83e7d28e3c34b15d8299d279d65ab9183b9` |
| lastVerifiedCommitDate | 2026-05-23T05:45:38+02:00                 |
| governingOverview      | `../../../overview.md`                     |

## Purpose

`git_worktree_manager.py` is the package-local C-09 worktree lifecycle
implementation behind MCP worktree tools.

## Code Commentary

### Logic

The module creates and attaches code/memory worktrees, writes task contracts,
reports lifecycle status, performs closeout, integrates completed branches, and
cleans up registered worktrees. During `start`, provider setup now calls
package-local `provider_setup.action_payload()` with a generated provider
settings path supplied by the MCP controller.

### Invariants And Boundaries

- Worktree provider setup must not invoke `<coordinationRoot>/scripts`.
- Provider enablement and roots come from MCP-derived provider settings, not
  coordinator `system/settings.json`.
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

- 2026-05-23T13:46+02:00: Documented the MCP-owned provider setup path and removal of coordinator-local script execution.
