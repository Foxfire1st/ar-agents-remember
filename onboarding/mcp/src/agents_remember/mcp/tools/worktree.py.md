# mcp/src/agents_remember/mcp/tools/worktree.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember-md                              |
| path                   | `mcp/src/agents_remember/mcp/tools/worktree.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-06-01T00:00+02:00|
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0`                                       |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
| governingOverview      | `overview.md`                                   |

## Purpose

Worktree lifecycle and direct-closeout payload builders.

## Code Commentary

### Logic

Holds `worktree_start_payload`, `worktree_attach_payload`,
`worktree_status_payload`, `worktree_closeout_preview_payload`,
`worktree_closeout_apply_payload`, `direct_closeout_preview_payload`,
`direct_closeout_apply_payload`, `worktree_integrate_payload`,
`worktree_cleanup_payload`, and `worktree_abandon_payload`. Each forwards typed
arguments to the matching `controllers.worktree_tools` function and returns
through `base._tool_payload`.

`worktree_start_payload` now wraps its controller result with
`summarize_command_logs` (imported from `providers.lifecycle.log_capture`)
before returning, trimming large stdout/stderr from provider setup output that
would otherwise make the response too large to render.

`worktree_cleanup_payload` now accepts and forwards `teardown_providers`
(default `True`).

`worktree_abandon_payload` is newly added; it forwards `contract_path`,
`dry_run`, and `force` to `worktree_abandon_tool`.

### Invariants And Boundaries

- Transport-thin: worktree/closeout behavior lives in
  `controllers.worktree_tools` and `worktrees/modules`.
- Closeout/apply builders carry the explicit `intent_note` commit-approval
  argument through to the controller.
- `worktree_start_payload`/`worktree_integrate_payload`/`worktree_cleanup_payload`/`worktree_abandon_payload`
  default `dry_run=False` (act-by-default); the `*_closeout_apply` builders keep
  `dry_run=False` paired with their `*_preview` builders. `dry_run=true` previews.

## Update History

- 2026-06-01T00:00+02:00 — `worktree_start_payload` now applies `summarize_command_logs`; `worktree_cleanup_payload` gained `teardown_providers`; `worktree_abandon_payload` newly added.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the worktree payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
