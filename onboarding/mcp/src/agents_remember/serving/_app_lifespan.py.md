# mcp/src/agents_remember/serving/_app_lifespan.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_lifespan.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-15T13:19+02:00 |
| lastVerifiedCommitHash | `163ba8a9798228b7f912eec05646f31e79f6b26e`                                        |
| lastVerifiedCommitDate | 2026-09-15T13:37:09+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[serving overview](overview.md)

## Purpose

Composes serving-process startup and background loops. It migrates all recognized control-plane
identity logs, including the serving-owned notifier log, before accepting clients, and prevents
metrics-loop shutdown from returning while an already-started worker thread can still write. It also
owns the serving lifetime's steady-state clock that keeps terminal catalog truth current.

## Code Commentary

### Logic

`_to_thread_drained_on_cancel` starts one `asyncio.to_thread` worker as a task and shields it from
caller cancellation. If the lifespan task is cancelled, it awaits the worker to completion before
re-raising `CancelledError`. `_metrics_loop` uses that boundary for sampling, record, degradation
evaluation, and compaction, so shutdown cannot race a still-running metrics write.

The lifespan first runs `migrate_control_plane_identity_logs` in a worker thread, then performs
compaction/priming and starts the existing projection, terminal-observation, liveness, metrics,
agent-notifier, and diagnostic loops. Shutdown cancels and awaits those tasks through the established
lifecycle.

`_terminal_observation_loop` is the serving lifetime's one steady-state terminal-catalog observer.
Each iteration awaits `runtime.liveness_sweeper.refresh` through `_to_thread_drained_on_cancel` and
sleeps `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` only after that call returns, which makes the
cadence completion-relative: a slow pass delays the next attempt instead of queueing nominal ticks,
and two attempts can never overlap. It reads no settings and needs no route, so a closed dashboard,
a headless process, or a disabled agent notifier cannot keep catalog turn truth from advancing. The
loop owns only the attempt cadence; the sweeper's own one-second starting-row window and ten-second
full-sweep limit stay inside `TerminalCatalogLivenessSweeper.refresh`.

Each enabled agent-notifier iteration refreshes the terminal catalog through the one liveness
sweeper immediately before evaluating delivery. Dashboard HTTP polling may perform the same refresh
for display, but headless message progress no longer depends on a browser requesting terminal state.
Both that refresh and the following notifier sweep use `_to_thread_drained_on_cancel`: lifespan
cancellation cannot return while either worker thread is still reading or mutating durable state.
The notifier's own inline refresh is unchanged and pre-dates the serving-owned observer; whether it
should remain a second recurring caller is not decided here.

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
- Serving owns exactly one steady-state terminal-observation caller. It is created unconditionally
  and registered in the same background collection as the other loops, so no HTTP request, open
  dashboard, model turn, or notifier setting is a prerequisite for catalog turn truth.
- That caller owns only the attempt cadence, and the cadence is completion-relative and
  non-overlapping: the sleep follows each attempt, including a failed one. The sweeper's
  starting-row and full-sweep clocks remain the sweeper's.
- A failed observation attempt neither marks success nor changes cadence: the loop logs and
  re-sleeps, and cancellation still ends the task because `asyncio.CancelledError` derives from
  `BaseException` and is not caught by that boundary. Pass-failure retry and error *semantics* are a
  separate concern this file does not claim.
- Whether the notifier's pre-existing inline refresh should remain a second recurring caller is an
  open decision; this file's observation contract does not depend on it either way.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Worker-thread cancellation is shielded, drained, and then re-raised. | `_to_thread_drained_on_cancel` | mcp/src/agents_remember/serving/_app_lifespan.py:60-73 |
| The serving lifetime owns one completion-relative, non-overlapping terminal-observation caller that goes off-loop through the drained helper and sleeps after each attempt. | `_terminal_observation_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:76-93 |
| Every blocking metrics operation uses the drained cancellation boundary. | `_metrics_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:96-118 |
| The observer reads the sweeper's own starting-row interval constant as its attempt cadence. | `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` | mcp/src/agents_remember/serving/terminal_liveness.py:57-57 |
| The serving lifespan performs migration before compaction and loop startup, registers the observer task, then cancels and awaits every background task. | `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:232-284 |
| The notifier refreshes liveness before each sweep and drains an in-flight refresh on cancellation. | `_agent_notifier_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:163-204 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260821-CLIVE Notifier Registration Wiring

`_agent_notifier_context` binds the serving runtime's inbox execution registrar to the configured
coordination root and passes it into each notifier sweep. The existing startup, cancellation, and
background-loop ordering remains intact; the new seam ensures registration happens before inbox
reconciliation/compaction rather than adding a parallel cleanup loop.

## Update History

- 2026-09-15T13:19+02:00 — 260831-LOCR-L01 curator (uncommitted change set on `ar/260831-locr-l01`,
  base `67b21aeb`): this file now also owns `_terminal_observation_loop`, the serving lifetime's
  single steady-state caller of the existing `TerminalCatalogLivenessSweeper.refresh`. Recorded the
  current ownership boundary rather than the change: terminal catalog observation is a serving
  lifespan responsibility that needs no HTTP request, no open dashboard, no model turn, and no
  enabled agent notifier, and the loop owns only a completion-relative, non-overlapping attempt
  cadence while both sweeper clocks stay in the sweeper. Added the failure boundary (a failed
  attempt logs and re-sleeps; cancellation is not caught because `CancelledError` is a
  `BaseException`) and the explicit statement that pass-failure retry/error semantics are not
  claimed here. Every line anchor was re-derived against the 309-line candidate
  (`_serving_lifespan` `195-243` → `232-284`, `_agent_notifier_loop` `140-181` → `163-204`,
  `_metrics_loop` `73-95` → `96-118`, `_to_thread_drained_on_cancel` `57-70` → `60-73`) and the two
  stray single-row reference blocks were merged into one table. Verification metadata remains
  closeout-owned; no stamp advanced.

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
