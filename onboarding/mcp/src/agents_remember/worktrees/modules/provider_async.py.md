# mcp/src/agents_remember/worktrees/modules/provider_async.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/provider_async.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00                     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Background provider setup for worktree start (GitHub #53): `worktree_start`
returns within seconds once worktrees and contract exist; the provider chain
runs on a daemon thread observable through a `SetupProgressFile`.

## Code Commentary

### Logic

`launch_provider_setup(request=, contract=, write_state_file=,
settings_cleanup=, runner=, thread_factory=)` creates the progress file at
`setup_progress_path(worktree_group)` (`provider-runtime/setup-progress.json`)
with `progress_identity(contract)`, starts a daemon thread, and immediately
returns the `starting` payload (`progressFile`, `pollTool: worktree_status`,
and the seed-vs-reindex `expectation` text). The thread runs
`run_provider_setup(request, progress)`, writes the provider-state file via the
injected callback when the payload is ok (recorded in the finish summary as
`providerStateFile`), finishes the progress with the payload's `state`, and —
critically — unlinks `settings_cleanup` in its `finally`: the controller's temp
lifecycle settings file must outlive the controller call, so ownership
transfers to this thread. The thread boundary catches the same exception set
`provider_setup.main` treats as reportable (`RuntimeError`, `OSError`,
`TimeoutExpired`, `BadZipFile`, `JSONDecodeError`) and records them as a
`failed` finish; anything else escapes to the threading excepthook (stderr is
safe — stdout is the MCP transport) and surfaces as a stale heartbeat.

`provider_setup_status(contract)` is the status projection: None when this
contract never ran background setup, `{"state": "prepared"}` when only the
legacy provider-state.json exists, otherwise `progress_status(...)` plus
`progressFile`, and on `failed`/`failed-unchecked`/`stale` a ready-to-use
`retryArgs` (`worktree_start` with `retry_provider_setup=true`;
`worktree_name` derives from `contract.code_worktree.name`).
`provider_setup_running(contract)` is True only for a live fresh-heartbeat
setup — the guard `worktree_cleanup`/`worktree_abandon` use so teardown never
races the setup thread.

### Invariants And Boundaries

- The launcher must return before any provider work happens; everything slow
  belongs on the thread.
- The contract must already be written when the launcher is called (it is the
  durable anchor the poll surfaces project from); `start_result` owns that
  ordering.
- `runner` and `thread_factory` are injectable test seams; production callers
  pass neither.
- A dead server mid-setup leaves a `running` file whose heartbeat goes stale;
  `retry_provider_setup` is the recovery path — never block teardown on a
  stale heartbeat.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Progress file format, heartbeat, and staleness projection. | [setup_progress.py](../../providers/setup_progress.py.md) |
| `start_result` writes the contract first, then launches through this module. | [start.py](start.py.md) |
| `status_payload` exposes the projection; cleanup/abandon use the running guard. | [guidance.py](guidance.py.md) |
| Launcher, projection, ordering, retry, and guard unit tests. | [test_provider_async.py](agents-remember/mcp/tests/test_provider_async.py) |

## Update History

- 2026-06-10T07:30+02:00 — Created for GitHub #53: daemon-thread launcher with durable progress, settings-file ownership transfer, status projection with retryArgs, and the live-setup teardown guard.
