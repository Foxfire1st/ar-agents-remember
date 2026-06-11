# mcp/src/agents_remember/providers/setup_progress.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/setup_progress.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00                     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[providers overview](overview.md)

## Purpose

Durable phase-progress reporting for background provider setup (GitHub #53):
the observable that lets a model (or dashboard) watch a running setup instead
of holding a multi-minute tool call open.

## Code Commentary

### Logic

`SetupProgress` is the no-op sink interface provider setup announces through:
`phase_start(provider, action, note=, seed_fallback=)`, `phase_update(metrics)`
(reserved for future per-item indexing progress — `itemsDone/itemsTotal/
percent/unit`; nothing fills it yet because subprocess output is captured at
completion, not streamed), and `phase_done(result)`.

`SetupProgressFile` persists every event as JSON (schema
`ar-provider-setup-progress/v1`) with top-level identity fields
(`repoName`, `taskName`, `worktreeGroup`) so dashboards need not parse paths.
A daemon ticker thread refreshes `updatedAt` every `HEARTBEAT_SECONDS` (15s)
while setup runs; `finish(state, error=, summary=)` stops the ticker and
records the terminal state. The clock is injectable for tests. Write errors
are remembered (`progressWriteError`) instead of raised: progress reporting
must never fail the setup it observes.

`read_setup_progress(path)` returns the dict or None (absent/unreadable/not
schema v1). `progress_status(progress)` projects the compact status shape the
tools report: `running` carries `currentPhase` (+`elapsedSeconds`),
`heartbeatAgeSeconds`, `seedFallback`, and compact `completedPhases` lines; a
heartbeat older than `STALE_AFTER_SECONDS` (90s = six missed beats) projects
as `stale` — the writer died, so readers should offer retry rather than wait.
Terminal states pass through (`ok`, `ready-with-failed-phases`, `failed`,
`failed-unchecked` — the `setup_reporting.setup_state` vocabulary) with
`failedPhases` lines.

### Invariants And Boundaries

- Progress reporting must never raise into the provider setup chain.
- `stale` is a READER projection of a fresh-state `running` file, never a
  written state; the heartbeat is the only liveness signal.
- The schema is dashboard-facing: identity fields and the reserved
  `currentPhase.metrics` shape must stay forward-compatible (bump the schema
  version on breaking changes).
- `seedFallback` is written the moment the fallback phase starts, not after it
  finishes — surfacing the seconds→minutes expectation change is the point.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup functions announce phases through `setup_progress_from(args)`. | [setup_common.py](setup_common.py.md) |
| The worktree launcher creates the file and finishes it from the setup payload. | [provider_async.py](../worktrees/modules/provider_async.py.md) |
| Unit tests cover the event lifecycle, heartbeat, staleness, and projections. | [test_setup_progress.py](agents-remember/mcp/tests/test_setup_progress.py) |

## Update History

- 2026-06-10T07:30+02:00 — Created for GitHub #53: durable, heartbeat-stamped phase progress for background worktree provider setup, with the dashboard-ready schema (identity fields + reserved metrics) the developer requested.
