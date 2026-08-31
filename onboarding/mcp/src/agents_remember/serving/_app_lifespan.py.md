# mcp/src/agents_remember/serving/_app_lifespan.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_lifespan.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-31T04:50+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`                                        |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[serving overview](overview.md)

## Purpose

Composes serving-process startup and background loops. It migrates all recognized control-plane
identity logs, including the serving-owned notifier log, before accepting clients, and prevents
metrics-loop shutdown from returning while an already-started worker thread can still write.

## Code Commentary

### Logic

`_to_thread_drained_on_cancel` starts one `asyncio.to_thread` worker as a task and shields it from
caller cancellation. If the lifespan task is cancelled, it awaits the worker to completion before
re-raising `CancelledError`. `_metrics_loop` uses that boundary for sampling, record, degradation
evaluation, and compaction, so shutdown cannot race a still-running metrics write.

The lifespan first runs `migrate_control_plane_identity_logs` in a worker thread, then performs
compaction/priming and starts the existing projection, liveness, metrics, agent-notifier, and
diagnostic loops. Shutdown cancels and awaits those tasks through the established lifecycle.

Each enabled agent-notifier iteration refreshes the terminal catalog through the one liveness
sweeper immediately before evaluating delivery. Dashboard HTTP polling may perform the same refresh
for display, but headless message progress no longer depends on a browser requesting terminal state.
Both that refresh and the following notifier sweep use `_to_thread_drained_on_cancel`: lifespan
cancellation cannot return while either worker thread is still reading or mutating durable state.

### Conventions

Startup ordering is the compatibility boundary: migrate once before strict current readers.

### Invariants And Boundaries

- Serving owns the notifier-log migration.
- Migration completes before clients or sweeps can parse current rows.
- No live fallback reader accepts both schemas.
- Cancelling the metrics loop propagates cancellation only after its current worker-thread call is
  drained; no metrics mutation may outlive lifespan shutdown.
- The drain does not turn cancellation into success and does not create a detached fallback worker.
- Agent-notifier delivery evaluates current control/turn liveness even when no dashboard client is
  polling; the lifespan reuses the canonical liveness owner rather than duplicating probe logic.
- Notifier cancellation drains an in-flight liveness refresh or sweep before propagating
  `CancelledError`; no notifier mutation outlives server shutdown.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Worker-thread cancellation is shielded, drained, and then re-raised. | `_to_thread_drained_on_cancel` | mcp/src/agents_remember/serving/_app_lifespan.py:57-70 |
| Every blocking metrics operation uses the drained cancellation boundary. | `_metrics_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:73-95 |
| The serving lifespan performs migration before compaction and loop startup, then cancels and awaits every background task. | `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:195-243 |
| The regression holds cancellation open until an in-flight metrics write completes and then observes the committed sample. | `test_cancellation_drains_an_inflight_metrics_write_before_returning` | mcp/tests/test_serving_app_background_loops.py:224-255 |
| The notifier refreshes liveness before each sweep and drains an in-flight refresh on cancellation. | `_agent_notifier_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:140-181 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260821-CLIVE Notifier Registration Wiring

`_agent_notifier_context` binds the serving runtime's inbox execution registrar to the configured
coordination root and passes it into each notifier sweep. The existing startup, cancellation, and
background-loop ordering remains intact; the new seam ensures registration happens before inbox
reconciliation/compaction rather than adding a parallel cleanup loop.

## Update History

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: extended the existing
  shield-and-drain cancellation owner to both notifier liveness refresh and notifier evaluation,
  preventing post-shutdown background mutation. Verification remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 made each headless notifier sweep refresh canonical terminal liveness before delivery evaluation, removing dashboard polling as an accidental progress dependency. Verification remains closeout-owned.

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 parameter-specification migration in `_to_thread_drained_on_cancel` and confirmed that cancellation draining and lifespan ownership remain as documented. Verification remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded lifespan wiring for task-owned inbox execution evidence. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-14T12:31:43+02:00 — R44 curator: documented the shield-and-drain boundary for all
  blocking metrics operations and corrected the governing overview link. Verification remains
  closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_app_lifespan.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
