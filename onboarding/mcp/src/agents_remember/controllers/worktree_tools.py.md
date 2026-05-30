# mcp/src/agents_remember/controllers/worktree_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/worktree_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T21:33+02:00                     |
| lastVerifiedCommitHash | `825a172bdf0d4ee3489ae25dbcc19c4e9c7b9493` |
| lastVerifiedCommitDate | 2026-05-30T17:31:45+02:00|
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
- `worktree_start_tool`/`worktree_integrate_tool`/`worktree_cleanup_tool` default
  `dry_run=False` (act-by-default); the `*_closeout_apply` controllers keep
  `dry_run=False` paired with their `*_preview` tools. `dry_run=true` previews.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Worktree service behavior is owned by the worktree manager and modules. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Worktree response models define the public tool envelopes and context summary. | [worktree.py](agents-remember-md/mcp/src/agents_remember/models/worktree.py) |

## Update History

- 2026-05-30T21:33+02:00: Re-verified against `825a172` after the 0.9.x provider/worktree run; the controller surface (start, attach, status, closeout preview/apply, direct closeout preview/apply, integrate, cleanup), its coordination-containment rules, and the act-by-default `dry_run` behavior still match the source. References (`git_worktree_manager.py`, `models/worktree.py`) verified present.
- 2026-05-28T19:52+02:00: Created when worktree MCP controllers moved into their own domain module.
