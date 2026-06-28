# mcp/src/agents_remember/mcp/tools/worktree.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/mcp/tools/worktree.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-06-10T09:56+02:00     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                                       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

`worktree_start_payload` forwards `retry_provider_setup` to the controller — the relaunch path for a failed or stale background provider setup (GitHub #53). It also forwards `stale_base_choice` — the stale-base preflight recovery selector (GitHub #54). `worktree_sync_payload` is newly added (GitHub #54 sub-task D), forwarding `contract_path`/`memory_sync_choice`/`dry_run` to `worktree_sync_tool`. `worktree_attach_payload` forwards a new `on_unsaved` argument to `worktree_attach_tool` (slice 2c — the save-gate decision when attaching over an unsaved fleeting lifecycle); plumbing only.

### Invariants And Boundaries

- Transport-thin: worktree/closeout behavior lives in
  `controllers.worktree_tools` and `worktrees/modules`.
- Closeout/apply builders carry the explicit `intent_note` commit-approval
  argument through to the controller.
- `worktree_start_payload`/`worktree_integrate_payload`/`worktree_cleanup_payload`/`worktree_abandon_payload`
  default `dry_run=False` (act-by-default); the `*_closeout_apply` builders keep
  `dry_run=False` paired with their `*_preview` builders. `dry_run=true` previews.

## Series-Contract Notes

Worktree payload builders keep closeout/integration path-explicit while start/attach/status can resolve a leaf enclosure from `task_name`, optional `parent_task`, and optional `leaf_id`.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree payload builders now include `parent_task` and `leaf_id` for start/attach/status, matching the new resolver contract while closeout/integration continue taking explicit enclosure paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: `worktree_attach_payload` forwards a new `on_unsaved` argument to `worktree_attach_tool` (the save-gate decision); plumbing only. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-11T06:47+02:00 — Removed `direct_closeout_preview_payload` / `direct_closeout_apply_payload` and their controller imports (issue #62 worktree-only closeout); module docstring no longer mentions direct closeout.
- 2026-06-10T09:56+02:00 — Added `worktree_sync_payload` (GitHub #54 sub-task D); plumbing only.
- 2026-06-10T09:30+02:00 — `worktree_start_payload` forwards `stale_base_choice` (GitHub #54 stale-base preflight recovery); plumbing only.
- 2026-06-10T07:30+02:00 — `worktree_start_payload` forwards the new `retry_provider_setup` flag to the controller (GitHub #53 async setup recovery path).
- 2026-06-01T00:00+02:00 — `worktree_start_payload` now applies `summarize_command_logs`; `worktree_cleanup_payload` gained `teardown_providers`; `worktree_abandon_payload` newly added.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the worktree payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
