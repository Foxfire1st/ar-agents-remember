# mcp/src/agents_remember/mcp/tools/worktree.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/mcp/tools/worktree.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-06-10T09:56+02:00     |
| lastVerifiedCommitHash | `a69b72e101d09423601916c03d4f59ecdee7dda6`                                       |
| lastVerifiedCommitDate | 2026-06-11T11:08:18+02:00|
| governingOverview      | `overview.md`                                   |

## Purpose

Worktree lifecycle payload builders.

## Code Commentary

### Logic

Holds `worktree_start_payload`, `worktree_attach_payload`,
`worktree_status_payload`, `worktree_closeout_preview_payload`,
`worktree_closeout_apply_payload`, `worktree_integrate_payload`,
`worktree_cleanup_payload`, and `worktree_abandon_payload`. Each forwards typed
arguments to the matching `controllers.worktree_tools` function and returns
through `base._tool_payload`. The former `direct_closeout_preview_payload` /
`direct_closeout_apply_payload` builders were removed with the direct-closeout
tool surface (issue #62): closeout is worktree-only.

`worktree_start_payload` now wraps its controller result with
`summarize_command_logs` (imported from `providers.lifecycle.log_capture`)
before returning, trimming large stdout/stderr from provider setup output that
would otherwise make the response too large to render.

`worktree_cleanup_payload` now accepts and forwards `teardown_providers`
(default `True`).

`worktree_abandon_payload` is newly added; it forwards `contract_path`,
`dry_run`, and `force` to `worktree_abandon_tool`.

`worktree_start_payload` forwards `retry_provider_setup` to the controller — the relaunch path for a failed or stale background provider setup (GitHub #53). It also forwards `stale_base_choice` — the stale-base preflight recovery selector (GitHub #54). `worktree_sync_payload` is newly added (GitHub #54 sub-task D), forwarding `contract_path`/`memory_sync_choice`/`dry_run` to `worktree_sync_tool`.

### Invariants And Boundaries

- Transport-thin: worktree/closeout behavior lives in
  `controllers.worktree_tools` and `worktrees/modules`.
- Closeout/apply builders carry the explicit `intent_note` commit-approval
  argument through to the controller.
- `worktree_start_payload`/`worktree_integrate_payload`/`worktree_cleanup_payload`/`worktree_abandon_payload`
  default `dry_run=False` (act-by-default); the `*_closeout_apply` builders keep
  `dry_run=False` paired with their `*_preview` builders. `dry_run=true` previews.

## Update History

- 2026-06-11T06:47+02:00 — Removed `direct_closeout_preview_payload` / `direct_closeout_apply_payload` and their controller imports (issue #62 worktree-only closeout); module docstring no longer mentions direct closeout.
- 2026-06-10T09:56+02:00 — Added `worktree_sync_payload` (GitHub #54 sub-task D); plumbing only.
- 2026-06-10T09:30+02:00 — `worktree_start_payload` forwards `stale_base_choice` (GitHub #54 stale-base preflight recovery); plumbing only.
- 2026-06-10T07:30+02:00 — `worktree_start_payload` forwards the new `retry_provider_setup` flag to the controller (GitHub #53 async setup recovery path).
- 2026-06-01T00:00+02:00 — `worktree_start_payload` now applies `summarize_command_logs`; `worktree_cleanup_payload` gained `teardown_providers`; `worktree_abandon_payload` newly added.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the worktree payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
