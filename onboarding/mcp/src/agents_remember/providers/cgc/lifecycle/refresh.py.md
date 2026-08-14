# mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`refresh.py` owns the CodeGraphContext refresh lifecycle: it builds compose plans,
performs per-layout preflight and live refreshes, records refresh state, and
aggregates refresh-all results.

## Code Commentary

### Logic

`cgc_refresh_command` selects the settings-backed layouts and builds a compose
plan for the runner's `index` command, using the layout's
`container_code_repo_root`. `cgc_refresh_dry_result` returns the provider,
repository, working-directory, environment, and command in a dry-run payload.

`cgc_refresh_preflight` returns the dry-run result without executing the live
command, or starts the configured backend and runs `cgc_doctor` before a live
refresh. `cgc_refresh` runs the compose plan with `UNLIMITED_TIMEOUT` and
passes the result to `cgc_write_refresh_state`, which records the return code,
duration, and UTC update time.

`cgc_refresh_all` starts the configured watchers, returns early on a backend
failure, creates one dry-run result per layout when requested, and otherwise
uses the parallel layout action helper. Its final payload includes the watcher
result, the parallel marker, and `cgc_index_concurrency` for the selected
layout count.

### Invariants And Boundaries

- Settings-backed refreshes use the backend and doctor preflight before the
  live compose command; dry-run returns before those live actions.
- Live index execution uses `UNLIMITED_TIMEOUT`.
- Refresh state is written only after a live compose result is available.
- Layout arguments are typed as `CgcRuntimeLayout`, and refresh-all uses the
  shared watcher, parallel-action, aggregation, and concurrency helpers.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The per-layout compose command plan. | `cgc_refresh_command` | mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:34-50 |
| The dry-run payload and backend/doctor preflight. | `cgc_refresh_dry_result`; `cgc_refresh_preflight` | mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:53-63; mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:92-103 |
| Refresh state records the live command result. | `cgc_write_refresh_state` | mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:75-89 |
| The live refresh uses the uncapped command runner. | `cgc_refresh` | mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:106-143 |
| Refresh-all combines watcher startup, parallel layout actions, and aggregation. | `cgc_refresh_all` | mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:175-214 |
| Refresh-all reports the selected concurrency. | "indexConcurrency" | mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:213-213 |

## Update History
- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 4 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-01T00:00+02:00 — `cgc_refresh_all` now imports `cgc_index_concurrency` and reports `indexConcurrency` in the all-root refresh result payload. Updated Logic and cross-reference.
- 2026-05-31T12:50+02:00 — Re-typed the `layout` param of `cgc_refresh_command`, `cgc_refresh_dry_result`, `cgc_refresh_backend`, `cgc_write_refresh_state`, and `cgc_refresh_preflight` from bare `Any` to `CgcRuntimeLayout` (newly imported from `lifecycle.core`); behavior-preserving, added a layout-type note to Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented that `cgc index --force` refresh commands now run with `UNLIMITED_TIMEOUT` (never-cap-indexing run); added the uncapped-index invariant. Verified against `825a172`.
- 2026-05-29T18:35+02:00: `cgc_refresh_preflight` `command` parameter typed `dict[str, Any]` (the compose plan it forwards); behavior-preserving (commit `0549b28`).
- 2026-05-29T07:19+02:00: Updated after the `cgc index` repo argument switched to the driveless container path (`container_code_repo_root`) for Windows-host support.
- 2026-05-26T12:51+02:00: Updated after CGC refresh moved into the Docker runner.
- 2026-05-25T21:14+02:00: Split from `process.py` so refresh orchestration is separate from watcher process control and bounded queries.
