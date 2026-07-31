# mcp/src/agents_remember/providers/setup_progress.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/setup_progress.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                              |

## Governing Overview

[providers overview](../../../overview.md)

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

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/providers/setup_progress.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 12 line(s) with no token change whatsoever.
  Checked by parsing both revisions and comparing the abstract syntax trees (identical) and the
  comment tokens (identical), so no symbol, signature, default, decorator, control-flow branch,
  docstring, or assertion this card describes has moved, and every claim this card makes about its
  own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-10T07:30+02:00 — Created for GitHub #53: durable, heartbeat-stamped phase progress for background worktree provider setup, with the dashboard-ready schema (identity fields + reserved metrics) the developer requested.
