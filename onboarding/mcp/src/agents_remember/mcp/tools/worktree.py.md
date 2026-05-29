# mcp/src/agents_remember/mcp/tools/worktree.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember-md                              |
| path                   | `mcp/src/agents_remember/mcp/tools/worktree.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `23f4d7681f7fcd729049c5f27878c84bbb8f8e58`                                       |
| lastVerifiedCommitDate | 2026-05-29T20:24:00+02:00|
| governingOverview      | `overview.md`                                   |

## Purpose

Worktree lifecycle and direct-closeout payload builders.

## Code Commentary

### Logic

Holds `worktree_start_payload`, `worktree_attach_payload`,
`worktree_status_payload`, `worktree_closeout_preview_payload`,
`worktree_closeout_apply_payload`, `direct_closeout_preview_payload`,
`direct_closeout_apply_payload`, `worktree_integrate_payload`, and
`worktree_cleanup_payload`. Each forwards typed arguments to the matching
`controllers.worktree_tools` function and returns through `base._tool_payload`.

### Invariants And Boundaries

- Transport-thin: worktree/closeout behavior lives in
  `controllers.worktree_tools` and `worktrees/modules`.
- Closeout/apply builders carry the explicit `intent_note` commit-approval
  argument through to the controller.
- `worktree_start_payload`/`worktree_integrate_payload`/`worktree_cleanup_payload`
  default `dry_run=False` (act-by-default); the `*_closeout_apply` builders keep
  `dry_run=False` paired with their `*_preview` builders. `dry_run=true` previews.

## Update History

- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the worktree payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
