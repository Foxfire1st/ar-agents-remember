# mcp/tests/test_liveness_simulations.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_liveness_simulations.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T13:03+02:00                     |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce` |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

New file (260707-HFX2-L5, R3/S4): the P-15 "predicate fixture zoo" mandate realized as focused,
END-TO-END liveness simulations of the whole L1-L4 supervisor stack (expectation rows → supervisor
sweep → paste injector → escalation ladder). HFX2-L8 extends the suite with the dead-seat storm
simulation: 12 tests across 9 named incident classes, including a >=2000-row terminal-dead-seat
backlog proving the supervisor sweep returns, heartbeat metrics advance, redeliverable rows converge
to empty, and compaction bounds the inbox file.

## Code Commentary

### 260707-HFX2-L13 Current-Manager Simulation

The dead-manager respawn simulation now continues through the next supervisor tick after a successor
manager appears. Orphan/dead-upstream signals must name and target that current manager, proving that
address-time hierarchy repair replaces stale manager provenance instead of skipping directly upward.

### Logic

**260707-HFX2-L15 coverage.** Simulation delivery fakes now provide log-backed acceptance context.
The obsolete empty-composer and stacked-chip supervisor scenarios were removed, and a busy pane
without a matching log record is explicitly unconfirmed rather than treated as accepted.

Drives `run_supervisor_sweep` (`serving/supervisor.py`) across MULTIPLE simulated ticks per named
incident, reusing the exact `SupervisorContext`/store-fixture shape `test_supervisor.py`'s
`LadderWalkIntegrationTests` already establishes rather than inventing a second harness. Nine test
classes, one per incident:

- **`NeverBriefedSeatTests`** (P-5/P-14) — an overdue `briefed-by` expectation row nudges, then
  escalates to rung 3 within 6 simulated ticks (~12 min).
- **`ChipStackedDeliveryStallTests`** (P-16) — **hybrid**: classification is proven at the
  predicate-unit layer (`classify_pane_signal` / `evaluate_pane_findings` with an injected
  capturer), then the routed `delivery-stalled` finding is fed through the real `act_on_finding` and
  escalates to rung 3 within 2 sim-ticks — proven because `evaluate_predicates` (called by
  `run_supervisor_sweep`) hardcodes a real `tmux capture-pane` with no injectable capturer through
  `SupervisorContext` today.
- **`NoHostedSessionTests`** (#16) — 5 redelivery attempts along the real backoff ladder
  (30s→60s→300s→900s→3600s) escalate at `PERSISTENT_FAILURE_ATTEMPTS`; each tick reads the entry's
  own `nextAttemptAt` back from the store rather than hardcoding `now` deltas.
- **`ManagerMidTurnSignalLandsTests`** — the injector's harness-aware busy-marker corroboration
  (HFX2-L3) classifies a delivery into a busy pane as `acked` on the very first sweep tick, not lost
  or endlessly redelivered.
- **`DeadManagerLiveWorkersTests`** (P-6 + ladder walk) — extends (does not duplicate)
  `test_supervisor.py::LadderWalkIntegrationTests::test_dead_manager_with_live_workers_respawns_and_surfaces_orphans`
  with a second real sweep tick proving the orphaned workers themselves independently fire
  `dead-upstream` and signal the grandparent orchestrator.
- **`KilledSupervisorDaemonTests`** — the self-heartbeat store ticks twice then stops; the staleness
  banner is `None` at 60s stale, fires fail-loud text at 10 min stale (120s cutoff); a companion test
  proves a heartbeat that never ticked is deliberately silent (not a false alarm).
- **`CodexQuotaModalTests`** (#20) — every one of 5 redelivery attempts against a permanently
  modal-showing pane classifies `blocked`/`codex-quota-limit`, never `failed`/silently dropped, and
  escalates at attempt 5 with `NEEDS-ATTENTION` in the durable detail — driving the sweep itself, not
  just `test_injector.py`'s classification-only modal tests.
- **`FalseDeadSeatHysteresisTests`** (#17) — a flicker at t+10s and t+45s (recovers inside the 60s
  window) never fires `seat-liveness`/`signal-emit`/respawn; a control case confirms a REAL
  stale-past-window seat still fires, proving the HFX-L5 hysteresis holds when consumed through the
  supervisor's own R2e predicate (on top of the existing probe-layer proof in
  `test_terminal_liveness.py`).
- **`DeadSeatStormTests`** (HFX2-L8) — seeds 2000 terminal-rung, no-hosted-session rows addressed to
  retired/dead seats and asserts within a wall-clock bound that the sweep returns and increments
  `sweepCount`, no redelivery is attempted, rows transition to `ladder-resolved`, the redeliverable
  set converges to empty, the heartbeat never goes stale and reports backlog/duration metrics, and
  compaction reduces `operator-inbox.jsonl` to the bounded live set.

Shared fixtures: `_entry()` builds a `TerminalCatalogEntry`; `_FakeHost` is a reachable-by-default
tmux host a scenario can flip to unreachable (#16); `_landing_paster()` is the healthy-delivery
capture-verified paste every non-stuck scenario reuses; `_StubPaster` returns one fixed
`PasteResult` for scenarios needing the same pane state on every attempt (a stuck modal, a busy
pane); `_LivenessSimulationCase` is the shared `SupervisorContext` scaffolding base class. HFX2-L9
adds `SupervisorSignalCooldownStore` to that scaffolding so the multi-tick supervisor contexts
match the production context shape after signal cooldown landed; it does not add a new liveness
scenario in this file.

### Conventions

`unittest.TestCase` per incident class, `NOW` a shared fixed-clock constant
(`datetime(2026, 7, 8, 12, 0, 0, tzinfo=UTC)`), temp-rooted stores per test via the shared base
class — matching the project's existing fixture conventions (`test_supervisor.py`,
`test_escalation_ladder.py`).

### Invariants And Boundaries

- Two rows (`ChipStackedDeliveryStallTests`, and the pane-classified half of never-briefed) are
  explicitly hybrid, not full end-to-end sweep coverage — documented in both the test docstrings and
  the liveness report, not silently overclaimed. **The one thing a future editor of
  `evaluate_predicates`/`run_supervisor_sweep` must know:** there is no way to inject a fake pane
  capturer today; threading a capturer parameter through `SupervisorContext`/`evaluate_predicates` is
  the natural follow-up leaf that would let these two scenarios convert to full sweep-driven E2E.
- `DeadManagerLiveWorkersTests` deliberately builds ON TOP of (does not duplicate)
  `test_supervisor.py`'s existing unit fixture — a second real sweep tick, not a second copy of the
  first.
- `FalseDeadSeatHysteresisTests`' control case (`test_seat_actually_stale_past_the_window_still_fires`)
  is the regression a naive "flicker never fires" implementation would fail — hysteresis holding must
  never become "never fires at all."
- `DeadSeatStormTests` is intentionally wall-clock bounded because its regression is supervisor loop
  liveness under backlog, not just row semantics. It still uses temp-rooted stores and fake catalog
  rows; no real daemon, tmux session, or operator inbox is touched.

### Todos

None recorded by this leaf; the pane-capturer injection gap above is tracked as a follow-up leaf,
not a TODO in this file.

## Docs References

No external documentation applies; this is a same-repository integration-test suite proving the
P-15 fixture-zoo mandate (leaf task doc R3) and the liveness report
(`notes/reports/260707-HFX2-L5-liveness-report.md`) it gates.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines the liveness-simulation scope under test; the leaf task doc and liveness report are authoritative. | whole module | [test_liveness_simulations.py](test_liveness_simulations.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The sweep entry point every scenario drives across multiple ticks. | `run_supervisor_sweep`, `evaluate_predicates`, `act_on_finding` | [../src/agents_remember/serving/supervisor.py](../src/agents_remember/serving/supervisor.py.md) |
| The pane-signal classifier the two hybrid scenarios call directly (capturer not injectable through the sweep). | `classify_pane_signal` | [../src/agents_remember/serving/pane_signals.py](../src/agents_remember/serving/pane_signals.py.md) |
| The escalation ladder every incident's rung-3 assertion walks through. | `rung_due`/`next_step` | [../src/agents_remember/controlplane/escalation_ladder.py](../src/agents_remember/controlplane/escalation_ladder.py.md) |
| The self-liveness heartbeat store and staleness banner `KilledSupervisorDaemonTests` drives. | `SupervisorHeartbeatStore`, `supervisor_staleness_banner` | [../src/agents_remember/serving/supervisor_heartbeat.py](../src/agents_remember/serving/supervisor_heartbeat.py.md) |
| The unit-level fixture `DeadManagerLiveWorkersTests` extends rather than duplicates. | `LadderWalkIntegrationTests` | [test_supervisor.py](test_supervisor.py.md) |
| The terminal state and compaction semantics the HFX2-L8 storm simulation proves at scale. | `OperatorInboxStore.compact`; `mark_ladder_resolved`; `redeliverable` | [../src/agents_remember/controlplane/operator_inbox_store.py](../src/agents_remember/controlplane/operator_inbox_store.py.md) |
| The shared simulation context now wires the supervisor signal cooldown store expected by `SupervisorContext`. | L162-L190 | [test_liveness_simulations.py](agents-remember/mcp/tests/test_liveness_simulations.py) |

## Cross-Repo References

No sibling repository evidence is needed for this same-repository test suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository integration-test suite only. | — | — |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: aligned simulations with harness-log acceptance and
  removed the retired `never-briefed`/`delivery-stalled` pane predicates. Verification metadata
  remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: extended the respawn simulation through
  successor-manager targeting for orphan signals. Verification metadata remains pinned until closeout
  stamps the eventual L13 code commit.

- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: updated the shared liveness-simulation context to wire
  `SupervisorSignalCooldownStore` into `SupervisorContext`; no scenario semantics changed in this
  file. Verification metadata pinned until closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R5): added
  `DeadSeatStormTests.test_dead_seat_storm_terminates_and_compacts_without_stale_heartbeat`, seeding
  2000 dead/no-hosted-session terminal-rung rows and asserting bounded wall-clock sweep completion,
  sweep-count advancement, redeliverable convergence to empty, fresh heartbeat backlog/duration
  metrics, and bounded inbox after compaction. Verification metadata pinned until closeout stamps
  the 260707-HFX2-L8 commit.
- 2026-07-08T23:59+02:00 — Created for 260707-HFX2-L5 (R3/S4): 11 new tests across 8 named P-15
  incident classes, driving `run_supervisor_sweep` across multiple simulated ticks; 6/8 fully
  end-to-end, 2/8 honestly hybrid (predicate-unit classify + real downstream sweep response) because
  `evaluate_predicates` hardcodes a non-injectable real `tmux capture-pane` — documented as a
  follow-up leaf, not worked around. Gated by
  `notes/reports/260707-HFX2-L5-liveness-report.md`. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L5 commit.
