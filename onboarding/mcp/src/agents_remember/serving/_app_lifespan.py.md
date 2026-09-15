# mcp/src/agents_remember/serving/_app_lifespan.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_lifespan.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-15T20:42+02:00 |
| lastVerifiedCommitHash | `e9678c56e7f441371584ad8a18e2b9380cb38cf0`                                        |
| lastVerifiedCommitDate | 2026-09-15T20:50:53+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[serving overview](overview.md)

## Purpose

Composes serving-process startup and background loops. It migrates all recognized control-plane
identity logs, including the serving-owned notifier log, before accepting clients, and prevents
metrics-loop shutdown from returning while an already-started worker thread can still write. It also
owns the serving lifetime's steady-state clock that keeps terminal catalog truth current, and it takes
one contained terminal-catalog observation prime before the projection is built, so already-readable
adapter truth enters the initial projection without a request and without waiting for the first
scheduled tick. Every completed observation attempt — the prime's included — publishes the observer
stage's own health through the runtime's accumulator, and the served payload is read back at response
time by `_terminal_observer_health_payload`.

## Code Commentary

### Logic

`_to_thread_drained_on_cancel` starts one `asyncio.to_thread` worker as a task and shields it from
caller cancellation. If the lifespan task is cancelled, it awaits the worker to completion before
re-raising `CancelledError`. `_metrics_loop` uses that boundary for sampling, record, degradation
evaluation, and compaction, so shutdown cannot race a still-running metrics write.

The lifespan startup order is migrate → compact → start the serving-lifetime observer-health
accumulator and attempt its initial record → one observation prime → projection prime → create the
background loops → yield. It first runs `migrate_control_plane_identity_logs` in a worker thread,
then compacts the workspace river, then begins the observer-health lifetime (which is what makes the
prime's own outcome the first published transition rather than an unstarted state), then takes the
contained observation prime, then primes the projection, and only then starts the existing
projection, terminal-observation, liveness, metrics, agent-notifier, and diagnostic loops. Shutdown
cancels and awaits those tasks through the established lifecycle.

`_observe_terminal_catalog(runtime, phase)` is the one wrapper that makes a completed observer call
publish that stage's own health (`LOCR-R17@v1`). It stamps the call's start from the runtime's
serving clock, awaits `runtime.liveness_sweeper.refresh` through `_to_thread_drained_on_cancel`, and
then publishes exactly one transition: `record_success` on return, `record_failure(err, phase=…)`
and re-raise on `Exception`. Publication therefore sits on the observer CALL itself and not on any
failure boundary — a steady pass that SUCCEEDS has to be as observable as one that fails, which is
the whole point of the record — and R11's `except Exception` containment still owns containment
only, publishing nothing of its own. `phase` is `"startup"` at the prime and `"steady-state"` in the
recurring owner, and it is the ONLY input the failure category and summary are selected from.
Cancellation is deliberately not recorded: a cancelled call is incomplete and `CancelledError` is
not an `Exception`.

`_prime_terminal_observation` is the one pre-serve terminal-catalog observation attempt. It calls
`_observe_terminal_catalog(runtime, "startup")`, which is the same `runtime.liveness_sweeper.refresh`
the steady-state owner calls, through the same `_to_thread_drained_on_cancel` boundary, so it adds no
startup-only reader, cursor, catalog or write path: a fresh sweeper's prime is a due full sweep and
inherits the sweeper's own rate limit, batch and lock order. It is invoked exactly once, after
migration and compaction and after the observer-health lifetime has begun, and before
`runtime.projector.prime()` and before the first `asyncio.create_task`, which is what makes both the
initial projection and the first notifier sweep read a catalog a pass has already committed. Its
`except Exception` containment is deliberate: observation degradation must not become a serving
outage, so a raised prime still lets the projection prime and every recurring loop start, and the
level-triggered steady-state owner retries from the unchanged durable evidence on its first cadence.
Because the boundary catches `Exception` and not `BaseException`, `asyncio.CancelledError` still
propagates and the drain keeps owning thread teardown.

`_terminal_observation_loop` is the serving lifetime's one steady-state terminal-catalog observer.
Each iteration awaits `_observe_terminal_catalog(runtime, "steady-state")` and sleeps
`DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` only after that call returns, which makes the cadence
completion-relative: a slow pass delays the next attempt instead of queueing nominal ticks, and two
attempts can never overlap. It reads no settings and needs no route, so a closed dashboard, a
headless process, or a disabled agent notifier cannot keep catalog turn truth from advancing. The
loop owns only the attempt cadence; the sweeper's own one-second starting-row window and ten-second
full-sweep limit stay inside `TerminalCatalogLivenessSweeper.refresh`. The prime is one pre-serve
attempt, not a second recurring owner: the recurrence is the loop's.

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
- Serving takes exactly one pre-serve observation prime per lifespan. It is positioned after
  migration and workspace-river compaction and strictly before `runtime.projector.prime()`, before
  the first `asyncio.create_task`, and before the lifespan `yield`; a second invocation, a prime moved
  after the projection prime or after the recurring tasks, and a prime that never runs are each a
  contract violation, not an acceptable variation.
- The prime attempts only; it is not an availability gate. Its `except Exception` containment is the
  requirement, so a recoverable observation failure must leave serving startup, the projection prime,
  and every recurring loop intact. Turning that containment into startup refusal is forbidden
  overreach, and so is any startup-only parser, cursor, catalog or mutation used to force admission.
- The prime is the same canonical pass as every later one — same sweeper, evidence readers, cursor
  rules, rate limit, batch and lock order — and the prime is a due full sweep, not an extra one.
- Negative knowledge, recorded rather than implied: the containment boundary's cancellation property
  (`except Exception`, so `CancelledError` propagates into the drain) is asserted by the source and
  the design, but the delivered proof set does **not** falsify a widened boundary — re-running the
  L18 pair with `except BaseException` leaves every case green (`L18-RV-2`, measured by the leaf's
  independent review). Treat that property as reasoned-but-unfalsified until a case cancels the
  lifespan while the prime is parked in its worker thread.
- **Superseded (was: "R18 defines no health or readiness payload. A prime outcome is not published to
  any diagnostic surface by this file.").** That was true of R18's own change set and is no longer
  the current contract: `LOCR-R17@v1` landed the observer stage's own health, so a prime outcome IS
  published — `_observe_terminal_catalog(runtime, "startup")` writes the `startup-refresh-failed`
  category and `startup terminal observation failed` summary on a raised prime, and the steady owner
  writes the `steady-state-refresh-failed` pair. What remains true is the boundary: this file owns
  publication of the observer's own reading and nothing else — no readiness payload, no gate, and no
  cursor, marker, queue, catalog or task-authoring authority is derived from it.
- The publication rides the observer CALL, never a failure boundary: R11's `except Exception`
  containment publishes nothing of its own, and a SUCCESSFUL steady pass must be as observable as a
  failed one. The serving-lifetime accumulator is begun by `start_lifetime()` immediately before the
  prime, so a failed initial write costs the counters nothing and the served key is simply omitted
  until a later legitimate observation write succeeds.
- The notifier's pre-existing inline `runtime.liveness_sweeper.refresh` is a completed sweeper call
  that publishes no health transition, so with a dead observer loop beside a live notifier the
  record ages into `stale` although a sweeper call did complete (`L17` review observation, recorded
  for the L14 owner ruling rather than as a defect here). The direction is conservative: a notifier
  tick can never produce `healthy`, so "do not use notifier ticks as observer-success evidence" is
  honoured either way.
- Migration and compaction keep their existing precedence over the prime. The delivered ordering
  witness does not constrain prime-versus-migration/compaction (`L18-RV-3`): moving the prime before
  the compaction step also leaves every case green, so the production straight-line order at
  `_serving_lifespan` is the authority for that edge, not the fixture.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Worker-thread cancellation is shielded, drained, and then re-raised. | `_to_thread_drained_on_cancel` | mcp/src/agents_remember/serving/_app_lifespan.py:64-77 |
| A completed observer call publishes this stage's own health for BOTH outcomes, and only the phase separates a startup-prime failure from a steady-pass one. | `_observe_terminal_catalog` | mcp/src/agents_remember/serving/_app_lifespan.py:80-107 |
| The serving lifetime owns one completion-relative, non-overlapping terminal-observation caller that goes off-loop through the drained helper and sleeps after each attempt. | `_terminal_observation_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:109-126 |
| One contained pre-serve terminal-catalog observation attempt through the same drained helper, whose only failure handling is an `except Exception` that logs and returns. | `_prime_terminal_observation` | mcp/src/agents_remember/serving/_app_lifespan.py:129-149 |
| Every blocking metrics operation uses the drained cancellation boundary. | `_metrics_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:152-174 |
| The observer reads the sweeper's own starting-row interval constant as its attempt cadence. | `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` | mcp/src/agents_remember/serving/terminal_liveness.py:57-57 |
| The serving lifespan runs migration, then workspace-river compaction, then the observer-health lifetime start and its initial record, then the one observation prime, then the projection prime, then registers the recurring tasks, then cancels and awaits every background task. | `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:288-352 |
| The notifier refreshes liveness before each sweep and drains an in-flight refresh on cancellation; that inline refresh publishes no observer-health transition. | `_agent_notifier_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:219-261 |
| The served observer-health reader: the current lifetime's persisted row at response time, or `None` to omit the tail key, with the cutoff taken from the configured sweep cadence. | `_terminal_observer_health_payload` | mcp/src/agents_remember/serving/_app_lifespan.py:376-394 |
| The separate notifier heartbeat reader the observer-health reading sits beside. | `_agent_notifier_heartbeat_payload` | mcp/src/agents_remember/serving/_app_lifespan.py:354-374 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260821-CLIVE Notifier Registration Wiring

`_agent_notifier_context` binds the serving runtime's inbox execution registrar to the configured
coordination root and passes it into each notifier sweep. The existing startup, cancellation, and
background-loop ordering remains intact; the new seam ensures registration happens before inbox
reconciliation/compaction rather than adding a parallel cleanup loop.

## Update History

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, `_app_lifespan.py` +63/−2): the observer call became the publication point for the
  observer stage's own health, so this card's current contract was corrected in the body rather than
  annotated, and one earlier invariant was explicitly superseded. New seam
  `_observe_terminal_catalog(runtime, phase)`: it stamps the call start from the runtime's serving
  clock, awaits `liveness_sweeper.refresh` through the drained helper, and publishes exactly one
  transition — `record_success` on return, `record_failure(…, phase=…)` plus re-raise on `Exception`
  — so publication rides the observer CALL and not R11's containment boundary, which still publishes
  nothing of its own. `_terminal_observation_loop` calls it with `"steady-state"`,
  `_prime_terminal_observation` with `"startup"`, and `_serving_lifespan` now begins the serving
  lifetime's accumulator (`start_lifetime()`, which also attempts the initial record) immediately
  before the prime. Startup order is therefore migrate → compact → **observer-health lifetime start +
  initial record** → observation prime → projection prime → recurring tasks → yield. **Superseded
  invariant:** the previous entry "R18 defines no health or readiness payload; a prime outcome is not
  published to any diagnostic surface by this file" was true of R18's own change set and is no longer
  the contract — a prime outcome IS published now, while the boundary that this file derives no
  readiness payload, gate, cursor or queue authority from it remains. Recorded as negative knowledge:
  cancellation is deliberately not a transition, and the notifier's inline refresh publishes nothing,
  so a live notifier beside a dead observer loop ages the record into `stale` (conservative
  direction; recorded for the L14 owner ruling, not as a defect here). Every line anchor was
  re-derived against the 394-line candidate (`_to_thread_drained_on_cancel` `60-73` → `64-77`,
  `_terminal_observation_loop` `76-93` → `109-126`, `_prime_terminal_observation` `96-116` →
  `129-149`, `_metrics_loop` `119-141` → `152-174`, `_agent_notifier_loop` `186-227` → `219-261`,
  `_serving_lifespan` `255-310` → `288-352`) and two rows were added. Verification metadata remains
  closeout-owned; no stamp advanced.

- 2026-09-15T15:02+02:00 — 260831-LOCR-L18 curator (uncommitted change set on `ar/260831-locr-l18`,
  base `d868486c`, `_app_lifespan.py` +26/−0, sha256
  `81b4ef317545927bc115ecf2ddfa74b5e6bc641d170e1f31cb90022ae762c378`): the lifespan gained one
  pre-serve observation seam, so this card's current contract was corrected in the body rather than
  annotated. The startup order is now migrate → compact → **one contained observation prime** →
  `runtime.projector.prime()` → recurring tasks → `yield`, and the card records why the prime exists
  (initial projection and first notifier sweep must read a catalog a pass has already committed,
  without a browser request and without depending on the first scheduled tick) together with the
  boundaries that make it safe: the prime is an attempt and not an availability gate, its
  `except Exception` containment is the requirement rather than a defect, it is the same canonical
  sweeper pass with no startup-only reader or mutation, and it is a due full sweep rather than an
  extra one. Two negative facts are recorded because they are non-obvious and expensive to
  rediscover, both measured by this leaf's independent review rather than assumed: the boundary's
  cancellation property is **not falsified** by the delivered proof set (widening the boundary to
  `except BaseException` leaves every case green — `L18-RV-2`), and the delivered ordering witness
  does **not** constrain prime-versus-migration/compaction (moving the prime before compaction also
  leaves every case green — `L18-RV-3`). Every line anchor was re-derived against the 335-line
  candidate (`_metrics_loop` `96-118` → `119-141`, `_agent_notifier_loop` `163-204` → `186-227`,
  `_serving_lifespan` `232-284` → `255-310`) and the new `_prime_terminal_observation` row was added
  at `96-116`. Verification metadata remains closeout-owned; no stamp advanced.

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
