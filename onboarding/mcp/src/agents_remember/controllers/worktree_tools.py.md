# mcp/src/agents_remember/controllers/worktree_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/worktree_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`worktree_tools.py` is the controller surface for worktree start, attach,
status, closeout preview/apply, direct closeout preview/apply, integration,
and cleanup tools.

## Code Commentary

The module resolves allowed repositories and coordination-contained paths from
`McpRuntimeConfig`, builds worktree namespaces, and delegates lifecycle work to
`worktrees.git_worktree_manager`. Worktree start can include provider setup by
writing MCP-derived lifecycle settings and handing a package-local provider
setup config to the worktree manager.

## Invariants And Boundaries

- Repo IDs must resolve through MCP settings.
- Contract paths and memory/source paths must stay under the configured
  coordination root unless a specific tool owns a setup target.
- Worktree operations call package services directly; CLI entrypoints remain
  print adapters.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Worktree service behavior is owned by the worktree manager and modules. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Worktree response models define the public tool envelopes and context summary. | [worktree.py](agents-remember-md/mcp/src/agents_remember/models/worktree.py) |

## Update History

- 2026-05-28T19:52+02:00: Created when worktree MCP controllers moved into their own domain module.
