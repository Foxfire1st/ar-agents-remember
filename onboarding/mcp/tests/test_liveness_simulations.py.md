# mcp/tests/test_liveness_simulations.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_liveness_simulations.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-09T06:48+02:00                     |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840` |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

New file (260707-HFX2-L5, R3/S4): the P-15 "predicate fixture zoo" mandate realized as focused,
END-TO-END liveness simulations of the whole L1-L4 supervisor stack (expectation rows → supervisor
sweep → paste injector → escalation ladder). HFX2-L8 extends the suite with the dead-seat storm
simulation: 12 tests across 9 named incident classes, including a >=2000-row terminal-dead-seat
backlog proving the agent-notifier sweep returns, heartbeat metrics advance, redeliverable rows converge
to empty, and compaction bounds the inbox file.

## Code Commentary

### 260707-HFX2-L13 Current-Manager Simulation

The dead-manager respawn simulation now continues through the next supervisor tick after a successor
manager appears. Orphan/dead-upstream signals must name and target that current manager, proving that
address-time hierarchy repair replaces stale manager provenance instead of skipping directly upward.

### 260713-TES-L4 Terminal-Honesty Conversions

`NeverAckedSeatTests` became the N3 attempt-ceiling scenario: a live-but-silent seat's row
resolves `unresolved`/`attempt-limit` after `PERSISTENT_FAILURE_ATTEMPTS` (delivery evidence
intact, no `escalatedAt`, no `orchestration.escalation.rung` event) instead of climbing rungs —
the verdict-by expectation still nudges the owner exactly once. `NoHostedSessionTests` likewise
ends `unresolved` instead of escalating. `DeadSeatStormTests` now resolves the capped survivors
`expired` via `rebind-expired` (no replacement past the grace), stays inspectable for the 48h
marker window, and compacts away after 49h. `DeadManagerLiveWorkersTests` seeds a replacement
manager BEFORE the grace expires: tick 1 rebinds the pending row to `manager-2` (same durable
row, no new post, attempt clock reset) and tick 2 fires dead-upstream for the orphaned workers.

### Logic

**260707-HFX2-L15 coverage.** Simulation delivery fakes now provide log-backed acceptance context.
The obsolete empty-composer and stacked-chip supervisor scenarios were removed, and a busy pane
without a matching log record is explicitly unconfirmed rather than treated as accepted.

Drives `run_agent_notifier_sweep` (`serving/agent_notifier.py`) across MULTIPLE simulated ticks per named
incident, reusing the exact `AgentNotifierContext`/store-fixture shape `test_agent_notifier.py`'s
`LadderWalkIntegrationTests` already establishes rather than inventing a second harness. Nine test
classes, one per incident:

- **`NeverAckedSeatTests`** (N3) — an overdue `verdict-by` expectation row nudges the owner
  exactly once while the original row hits the 5-attempt ceiling and resolves `unresolved`
  (never a ladder rung).
- **`ChipStackedDeliveryStallTests`** (P-16) — **hybrid**: classification is proven at the
  predicate-unit layer (`classify_pane_signal` / `evaluate_pane_findings` with an injected
  capturer), then the routed `delivery-stalled` finding is fed through the real `act_on_finding` and
  escalates to rung 3 within 2 sim-ticks — proven because `evaluate_predicates` (called by
  `run_agent_notifier_sweep`) hardcodes a real `tmux capture-pane` with no injectable capturer through
  `AgentNotifierContext` today.
- **`NoHostedSessionTests`** (#16) — 5 redelivery attempts along the real backoff ladder
  (30s→60s→300s→900s→3600s) resolve `unresolved` at `PERSISTENT_FAILURE_ATTEMPTS` (N3); each tick
  reads the entry's own `nextAttemptAt` back from the store rather than hardcoding `now` deltas.
- **`ManagerMidTurnSignalLandsTests`** — the injector's harness-aware busy-marker corroboration
  (HFX2-L3) classifies a delivery into a busy pane as `acked` on the very first sweep tick, not lost
  or endlessly redelivered.
- **`DeadManagerLiveWorkersTests`** (N14) — the replacement manager appears before the grace
  expires: tick 1 rebinds the dead-manager row to `manager-2` (same row, no new post), and tick 2
  fires `dead-upstream` for the orphaned workers against the current manager.
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
  agent-notifier's own R2e predicate (on top of the existing probe-layer proof in
  `test_terminal_liveness.py`).
- **`DeadSeatStormTests`** (HFX2-L8, re-based on N2/§9) — seeds 2000 no-hosted-session rows
  addressed to retired/dead seats and asserts within a wall-clock bound that the sweep returns and
  increments `sweepCount`, no redelivery is attempted, rows transition to `expired`
  (`rebind-grace-expired`), the redeliverable set converges to empty, terminal markers keep their
  48h window before physical eviction, the heartbeat never goes stale and reports backlog/duration
  metrics, and compaction bounds the log.

Shared fixtures: `_entry(session_id, *, leaf_key)` builds one fixed shape — a `running` `harness`
`TerminalCatalogEntry` — and scenarios vary the frozen row with `replace(...)` or with
`entry.with_turn_state(state, changed_at=…)` rather than through builder parameters; `_FakeHost`
is a reachable-by-default tmux host a scenario can flip to unreachable (#16);
`_landing_paster()` is the healthy-delivery
capture-verified paste every non-stuck scenario reuses; `_StubPaster` returns one fixed
`PasteResult` for scenarios needing the same pane state on every attempt (a stuck modal, a busy
pane); `_LivenessSimulationCase` is the shared `AgentNotifierContext` scaffolding base class. HFX2-L9
adds `AgentNotifierSignalCooldownStore` to that scaffolding so the multi-tick agent-notifier contexts
match the production context shape after signal cooldown landed; it does not add a new liveness
scenario in this file.

### Conventions

`unittest.TestCase` per incident class, `NOW` a shared fixed-clock constant
(`datetime(2026, 7, 8, 12, 0, 0, tzinfo=UTC)`), temp-rooted stores per test via the shared base
class — matching the project's existing fixture conventions (`test_agent_notifier.py`,
`test_escalation_ladder.py`). Seeded rows are built through parameter objects: expectation rows
via `write_expectation_row(store, Expectation(kind, source_id, subject=ExpectationSubject(...)),
row_id=…, now=…, sla_seconds=…)`, and inbox entries via
`create_operator_inbox_entry(InboxMessage(ask, response, message_kind), entry_id=…, now=…,
routing=InboxRouting(address=InboxAddress(...)), poster=InboxPoster(...))`.

### Invariants And Boundaries

- Two rows (`ChipStackedDeliveryStallTests`, and the pane-classified half of never-briefed) are
  explicitly hybrid, not full end-to-end sweep coverage — documented in both the test docstrings and
  the liveness report, not silently overclaimed. **The one thing a future editor of
  `evaluate_predicates`/`run_agent_notifier_sweep` must know:** there is no way to inject a fake pane
  capturer today; threading a capturer parameter through `AgentNotifierContext`/`evaluate_predicates` is
  the natural follow-up leaf that would let these two scenarios convert to full sweep-driven E2E.
- `DeadManagerLiveWorkersTests` deliberately builds ON TOP of (does not duplicate)
  `test_agent_notifier.py`'s existing unit fixture — a second real sweep tick, not a second copy of the
  first.
- `FalseDeadSeatHysteresisTests`' control case (`test_seat_actually_stale_past_the_window_still_fires`)
  is the regression a naive "flicker never fires" implementation would fail — hysteresis holding must
  never become "never fires at all."
- `DeadSeatStormTests` is intentionally wall-clock bounded because its regression is agent-notifier loop
  liveness under backlog, not just row semantics. It still uses temp-rooted stores and fake catalog
  rows; no real daemon, tmux session, or operator inbox is touched.

### Todos

None recorded by this leaf; the pane-capturer injection gap above is tracked as a follow-up leaf,
not a TODO in this file.

## Docs References

No external documentation applies; this is a same-repository integration-test suite proving the
P-15 fixture-zoo mandate (leaf task doc R3) and the liveness report
(`notes/reports/260707-HFX2-L5-liveness-report.md`) it gates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines the liveness-simulation scope under test; the leaf task doc and liveness report are authoritative. | `_LivenessSimulationCase` | mcp/tests/test_liveness_simulations.py:134-192 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The sweep entry point every scenario drives across multiple ticks. | `run_agent_notifier_sweep`; "def evaluate_predicates(  # pragma: no cover"; "def act_on_finding(" | mcp/src/agents_remember/serving/_agent_notifier_actions.py:972-972; mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:474-474; mcp/src/agents_remember/serving/agent_notifier.py:117-219 |
| The pane-signal classifier the two hybrid scenarios call directly (capturer not injectable through the sweep). | `classify_pane_signal` | mcp/src/agents_remember/serving/pane_signals.py:80-97 |
| The escalation ladder every incident's rung-3 assertion walks through. | `rung_due`; `next_step` | mcp/src/agents_remember/controlplane/escalation_ladder.py:94-120; mcp/src/agents_remember/controlplane/escalation_ladder.py:123-152 |
| The self-liveness heartbeat store and staleness banner `KilledSupervisorDaemonTests` drives. | `AgentNotifierHeartbeatStore`; `agent_notifier_staleness_banner` | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:63-109; mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:141-157 |
| The unit-level fixture `DeadManagerLiveWorkersTests` extends rather than duplicates. | `LadderWalkIntegrationTests` | mcp/tests/test_agent_notifier_ladder.py:241-629 |
| The terminal state and compaction semantics the HFX2-L8 storm simulation proves at scale. | `OperatorInboxStore` | mcp/src/agents_remember/controlplane/operator_inbox_store.py:53-251 |
| The shared simulation context (`_ctx`) wires the agent-notifier signal cooldown store expected by `AgentNotifierContext`. | "signal_cooldown_store=" | mcp/tests/test_liveness_simulations.py:165-165 |

## Cross-Repo References

No sibling repository evidence is needed for this same-repository test suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository integration-test suite only. | — | — |

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the terminal-honesty conversions —
  attempt-ceiling `unresolved` (NeverAcked/NoHostedSession), dead-seat storms resolving `expired`
  with 48h marker retention (N2/§9), and replacement-mid-flight rebinding to the current manager
  (N14). Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the scenario rename
  `NeverBriefedSeatTests` → `NeverAckedSeatTests` (fixture kind now `ack-by`, matching the
  retired briefed-by finding surface). Verification metadata pinned until closeout stamps the
  260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-03T03:06:10+02:00 — W3-B05 curator: resolved 3 Tier-2 table findings with exact anchors and current source paths; fixer generated all final ranges.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: corrected the shared-fixture description and the
  self-file citation. `_entry` lost five parameters (`kind`, `status`, `turn_state`,
  `turn_state_changed_at`, `liveness_failures`) and now mints only a `running` `harness` row from
  `session_id`/`leaf_key`; scenarios reach the rarer shapes with `replace(...)` or the entry's own
  `with_turn_state(state, changed_at=…)`, which is what `FalseDeadSeatHysteresisTests` now uses
  for its stale-flicker and stale-past-window rows. Row seeding also moved onto parameter
  objects — `write_expectation_row` takes an `Expectation`/`ExpectationSubject` pair and
  `create_operator_inbox_entry` takes `InboxMessage` plus `routing=InboxRouting(address=…)` and
  `poster=InboxPoster(...)` — recorded under Conventions. The Repo-Internal citation for the
  shared simulation context was re-derived and verified: the `_ctx` builder is L151-L176 (it was
  cited L162-L190, which had drifted off the helper's start). All twelve tests keep their names
  and assertions, so every incident-class claim and invariant above still holds.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

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
