# mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py

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

## Evidence

### Repo-Internal References

- The per-layout compose command plan. [1]
- The dry-run payload and backend/doctor preflight. [2]
- Refresh state records the live command result. [3]
- The live refresh uses the uncapped command runner. [4]
- Refresh-all combines watcher startup, parallel layout actions, and aggregation. [5]
- Refresh-all reports the selected concurrency. [6]
