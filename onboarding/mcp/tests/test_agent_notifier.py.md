# test_agent_notifier.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_agent_notifier.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`.

## Purpose

`test_agent_notifier.py` covers the deterministic agent-notifier sweep (`serving/agent_notifier.py` +
`serving/agent_notifier_heartbeat.py`, 260707-HFX2-L2 R2-R6): one unit test per predicate family, the
heartbeat's own read/tick/staleness behavior, and one integration test that seeds drift across every
predicate simultaneously and asserts the full finding→action→heartbeat chain — no model in the loop
anywhere; every fixture is a plain store write or a fake pane capturer/paster. 260707-HFX2-L4 (R2-R6)
adds the escalation ladder's two new predicate families plus a dedicated `LadderWalkIntegrationTests`
suite: the R6-mandated silent-seat, dead-intermediate, and dead-manager-with-live-workers fixtures.
260707-HFX2-L8 adds terminal-dead-seat and budget/backlog coverage for the dead-seat storm fix.
260707-HFX2-L9 adds regressions for the 900-second redelivery floor, repeated signal cooldown,
mid-turn pane suppression, and fast sweep cadence without per-second owner inbox noise.
Positional HFX2-L19 adds the F1 regression pin that keeps hosted-delivery failures in redelivery
until the persistent-attempt threshold is exhausted, before the generic unacked ladder may fire.

## Code Commentary

### 260707-HFX2-L17 Pair-Scoped Supervisor Regressions

Tests prove same-leaf findings for different seat roles do not coalesce, current binding identity
drives suspect/orphan/owner behavior, and injected sweep time reaches delivery records. The
fixed-point ceiling changes from `seeded*8` to `seeded*9` because pair-scoped rows add one bounded
snapshot per seed; reviewer O4 correctly classifies this as informational, not divergence.

### 260713-TES-L4 Expectation-Fixture Kind Swap

`ExpectationPredicateTests` (deleted by 260713-TES-L5) had renamed its overdue fixtures from
`ack-by` to `verdict-by` (N16: ack-by retires with the consume demotion and no post writes one
anymore). The class no longer exists: expectation rows produce no findings at all.

### 260707-HFX2-L13 Chain, Ladder, And Manager-First Regressions

Supervisor tests now prove an unbound reviewer's progress suppresses stale leaf inactivity and
escalation, the rung walk respects the five-minute floor between transitions, duplicated due
findings cannot advance one row twice in one sweep, and dead-upstream signals address the successor
manager. These are full predicate/action/sweep assertions rather than isolated helper tests. Current
coverage intentionally does not credit an unbound worker during its active phase; that accepted S1
gap is routed to HFX2-L14 S7.

### 260707-HFX2-L12 CS-6 Update

`Cs6SweepScalingTests` now pins the supervisor CS-6 floor: signal-cooldown reads stay at most one per sweep across many findings, expectation-store reads stay flat across overdue rows, and `escalation_budget` caps rung emissions under backlog.

### Logic

**Positional HFX2-L19 F1 regression pin.**
`test_delivery_failure_waits_for_retry_exhaustion_before_escalating` drives the public
`evaluate_escalation_findings` boundary with two past-SLA `no-hosted-session` rows: the row at
`PERSISTENT_FAILURE_ATTEMPTS - 1` remains silent, while the row at
`PERSISTENT_FAILURE_ATTEMPTS` is the sole `escalation-due` finding. The call supplies no catalog,
so chain-progress suppression cannot accidentally satisfy the assertion; removing or bypassing
`_delivery_failure_still_retrying` makes the pre-exhaustion row appear and fails the test.

**260707-HFX2-L15 coverage.** A declared unbound replacement suppresses false inactivity for its
named leaf, and the redelivery sweep processes one row under the default budget instead of
multiplying the calibrated synchronous log wait across a backlog. Delivery fakes use log evidence,
not pane movement.

The suite uses `NOW = datetime(2026, 7, 8, 12, 0, 0, tzinfo=UTC)` as the shared fixed clock:

- **Pane predicate (R2a):** `test_mid_turn_pane_fires_a_finding`, `test_normal_pane_fires_nothing`,
  `test_terminal_kind_rows_are_never_pane_classified` (a `kind="terminal"` row is skipped
  regardless of its captured text — the predicate only ever classifies `kind="harness"` rows).
- **Expectation predicate (R2b):** `test_overdue_ack_by_row_fires` (renamed from the
  briefed-by case, 260713-TES-L2),
  `test_not_yet_due_row_is_silent` (a row whose deadline has not yet passed produces no finding).
- **Retired dispatch expectations (260713-TES-L2):** `RetiredDispatchExpectationTests` proves
  an overdue `turn-report-by` row AND an overdue `briefed-by` row are both silent
  (`evaluate_expectation_findings` returns `[]`) — the artifact-presence/SLA predicates no
  longer drive any finding on the worker→manager path (R6).
- **Inbox predicate (R2d + HFX2-L8):** `test_pending_row_with_no_next_attempt_is_immediately_redeliverable`
  plus terminal-ladder coverage proving a pending row at the final rung for a provably dead/no-hosted
  seat fires `inbox-ladder-terminal` instead of redelivery.
- **Seat-liveness predicate (R2e):** `test_stale_turn_state_past_cutoff_fires`,
  `test_recently_stale_does_not_fire_yet` (stale but still inside the grace window is silent),
  `test_degraded_row_with_no_turn_state_uses_liveness_failures` (the graceful-degradation path: a
  row the L8 prober never classified falls back to the L5 `liveness_failures > 0` signal alone).
- **Escalation predicate (260707-HFX2-L4, R2):** `EscalationPredicateTests` —
  `test_delivery_failure_waits_for_retry_exhaustion_before_escalating` (a past-SLA hosted-delivery
  failure below the persistent-attempt threshold stays in redelivery while the exhausted row alone
  becomes escalation-due),
  `test_pending_row_past_sla_fires` (a rung-0 row past its per-kind SLA fires an `escalation-due`
  finding naming its own entry id), `test_not_yet_due_row_is_silent` (a row still inside its SLA
  window is silent).
- **Dead-upstream predicate (260707-HFX2-L4, R4):** `DeadUpstreamPredicateTests` —
  `test_worker_with_dead_manager_fires` (a live worker whose recorded owner is `terminated` fires a
  `dead-upstream` finding naming the WORKER's own session id, not the dead owner's),
  `test_live_owner_does_not_fire` (a live owner is silent), `test_no_provenance_at_all_does_not_fire`
  (a row with no `spawned_by_session` recorded at all is a legacy/unrouted case, not a dead-owner
  case, and stays silent).
- **Ladder walk integration (260707-HFX2-L4, R6 fixtures):** `LadderWalkIntegrationTests` drives the
  ladder through `run_agent_notifier_sweep` end-to-end, not the pure predicates in isolation —
  `test_silent_seat_climbs_rung_one_then_two_then_three` runs four successive sweeps over one
  unacked row and asserts it climbs rung 1 -> 2 -> 3 exactly on schedule, then proves rung 3 is a
  hard ceiling (a fifth sweep, far past every threshold, still reads rung 3).
  `test_dead_intermediate_manager_is_skipped_at_rung_two` seeds a row already at rung 1 whose
  addressee's manager is `terminated`, and asserts the rung-2 transition's owner event lands on the
  ORCHESTRATOR, never the dead manager. `test_dead_manager_with_live_workers_respawns_and_surfaces_
  orphans` is the R3+orphan-policy fixture: a manager-addressed row past the respawn threshold with
  the manager's OWN turn-state stale triggers `_respawn_suspect` — the manager's catalog row flips
  to `terminated`, a SINGLE `orchestration.agent-notifier.respawn` event carries both live workers under
  `orphanedWorkers`, and the workers themselves are asserted UNCHANGED (`status == "running"`) —
  proving they are surfaced, never auto-retired or re-parented themselves.
  `test_dead_upstream_signals_the_grandparent` seeds the same dead-manager-with-live-worker shape
  and asserts the sweep's OWN `dead-upstream` finding (not the ladder) fires for the worker and the
  `orchestration.agent-notifier.dead-upstream` event names the orchestrator as `grandparentAgentId`.
- **Sweep integration:** `test_seeded_drift_produces_expected_actions_and_ticks_heartbeat` seeds
  drift across pane-signal, expectation-overdue, inbox-redeliverable, AND seat-liveness
  simultaneously in one sweep and asserts the expected action set, delivery outcomes, the
  `mark_missed` side effect, and the heartbeat tick — the R6-mandated "seeded drift → expected
  actions" integration case. HFX2-L8 adds a dead-seat terminal integration asserting the row becomes
  durable `ladder-resolved`, emits one supervisor observer event, and is not redelivered, plus a
  budget integration asserting a low `redeliver_budget` caps attempts while heartbeat backlog metrics
  still tick. HFX2-L9 adds four more sweep/action regressions:
  `test_repeated_seat_liveness_sweeps_coalesce_into_one_signal_row` renews the same durable signal
  row with a newer timestamp after the cooldown;
  `test_diagnostic_pane_signal_is_not_actionable` proves `pane-signal: mid-turn`
  returns skipped with no inbox row;
  `test_pending_backlog_does_not_burst_redeliver_before_floor_after_restart` seeds delivered rows at
  +900s and proves a +60s restarted sweep performs no redelivery; and
  `test_one_second_sweeps_do_not_emit_per_second_signal_rows` runs 180 one-second sweeps and still
  has one signal row while the heartbeat reaches sweep count 180.
- **Edge cases:** `test_finding_with_no_routable_owner_skips_its_action` (a finding whose owner
  cannot be derived produces a `"skipped"`/`"no routable owner"` result rather than raising —
  covers `_signal_emit`'s no-owner branch specifically, added after the CRAP-Calculator flagged its
  low coverage), `test_zero_drift_sweep_still_ticks_the_heartbeat` (R5: a sweep with zero findings
  still ticks), `test_second_sweep_bumps_sweep_count`.

`_entry(...)` is the shared `TerminalCatalogEntry` fixture builder, typed against the catalog's own
`Literal` aliases (`TerminalSessionKind`/`TerminalSessionStatus`). Since 260731-EFA-L2 it supplies
only what **identifies** the seat: turn state comes from the row's own `with_turn_state(...)` and
everything else from `replace(...)`, because `TerminalCatalogEntry` already carries every field and
a builder that mirrored the row's shape was a second copy of it. The `turn_state`,
`turn_state_changed_at` and `liveness_failures` parameters (and the `SeatTurnState` import) are
gone.

### Conventions

Standard suite bootstrap (`MCP_SRC` path insert), `tempfile` for every store (`ExpectationRowStore`,
`OperatorInboxStore`, `OrchestrationNudgeStore`, `EventStore`) so no test touches real coordination
state. `cast(TerminalHost, fake)` for the duck-typed fake host, matching the existing project
convention from `test_terminal_ws.py`.

### Invariants And Boundaries

- No test touches the real coordination root or a real tmux session; every store is temp-rooted and
  every pane capturer/paster is a fixture double.
- The integration test's fake `TerminalPaster` tracks a MONOTONICALLY-GROWING chip counter (not a
  single shared landed/not-landed boolean) precisely because the sweep can issue two INDEPENDENT
  deliveries (redeliver + the auto-nudge's owner-signal post) against one fake instance in the same
  sweep — a shared boolean made the second delivery's origin capture already show the first
  delivery's chip, masking growth detection (a live instance of the F-V/N1 problem
  `terminal_paste.py`'s own docstring documents). Any future test adding a third concurrent delivery
  path must preserve this per-call-plus-monotonic counting, not regress to a shared flag.
- Predicate-family tests are independent of the integration test — each can fail in isolation and
  point at exactly one `evaluate_*_findings` function.
- The HFX2-L19 F1 test deliberately omits a terminal catalog. Its retrying-row assertion therefore
  pins `_delivery_failure_still_retrying` itself rather than receiving accidental suppression from
  leaf-chain progress; the threshold row must be the only emitted finding.
- The L8 terminal-dead-seat tests deliberately require both terminal ladder rung and proven dead seat;
  live seats and rows still climbing remain protected by the older redelivery/escalation tests.
- The HFX2-L9 signal-cooldown tests use a real temp-rooted `AgentNotifierSignalCooldownStore`; they do
  not fake the cooldown decision.
- `LadderWalkIntegrationTests` deliberately drives the FULL sweep (`run_agent_notifier_sweep`), not the
  isolated `_escalate_rung`/`_respawn_suspect` action functions directly — the R6 fixtures are about
  proving the finding→action→durable-row-stamp chain end to end, matching the existing
  `SweepIntegrationTests` posture for the other five predicate families.

### Todos

No known follow-up in this file. The builder report's "Issues Hit" documents two now-resolved
findings from writing this suite (the fake-paster chip-sharing bug above, and `_signal_emit`'s
initial 11% coverage/CRAP-threshold trip) — both fixed in the version this sidecar documents, not
open follow-ups.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; this is a
same-repository unit/integration-test suite for internal control-plane plumbing with no external
spec.

| Finding | Anchor | Source |
| --- | --- | --- |
<!-- No external/domain document defines the agent-notifier sweep; task provenance is not a source citation. -->

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test: the fact predicates, the action dispatcher, and the sweep entry point. | "def evaluate_predicates(  # pragma: no cover"; "def act_on_finding("; `run_agent_notifier_sweep` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:689-689; mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:350-350; mcp/src/agents_remember/serving/agent_notifier.py:95-182 |
| The heartbeat store the zero-drift and second-sweep tests exercise directly. | `AgentNotifierHeartbeatStore` | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:63-109 |
| The terminal catalog declares the typed `Literal` aliases. | "TerminalSessionKind = Literal"; "TerminalSessionStatus = Literal" | mcp/src/agents_remember/models/terminal_catalog.py:22-22; mcp/src/agents_remember/models/terminal_catalog.py:24-24 |
| The supervisor test's `_entry` builder consumes typed catalog fields. | `_entry` | mcp/tests/test_agent_notifier.py:49-73 |
| The fake-host casting convention this suite reuses rather than inventing its own duck-typing idiom. | `_FakeTerminalHost`; "class TerminalHost:" | mcp/src/agents_remember/serving/terminal.py:109-109; mcp/tests/test_terminal_ws.py:227-387 |
| The operator-inbox terminal state and compaction semantics used by the sweep tests (the ladder transitions are deleted; legacy `ladder-resolved` rows stay parse-compat). | `list_redeliverable`; `reconcile_and_compact` | mcp/src/agents_remember/controlplane/operator_inbox_store.py:153-173; mcp/src/agents_remember/controlplane/operator_inbox_store.py:234-234 |
| The persisted signal cooldown store used by the HFX2-L9 repeated-sweep regressions. | `AgentNotifierSignalCooldownStore` | mcp/src/agents_remember/controlplane/agent_notifier_signals.py:71-220 |
| The quiescence pin proves an absent-developer backlog reaches a fixed point through the grace path (no escalation rungs, 260713-TES-L5). | `test_unacked_backlog_reaches_a_fixed_point_with_absent_developer` | mcp/tests/test_agent_notifier_ladder.py:691-750 |
| The production predicates and the fact-only finding kinds are the behavior the demolition suite mutation-pins. | `evaluate_predicates`; `FindingKind` | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:330-380; mcp/src/agents_remember/serving/agent_notifier_models.py:26-50 |
| HFX2-L9 tests cover signal cooldown and diagnostic-pane non-actionability. | `test_repeated_seat_liveness_sweeps_coalesce_into_one_signal_row`; `test_diagnostic_pane_signal_is_not_actionable` | mcp/tests/test_agent_notifier_seat.py:367-404; mcp/tests/test_agent_notifier_seat.py:538-560 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sweep-local behavior only. | — | — |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## 260713-TES-L5 Current Delta — Expectation And Ladder Predicate Tests Demolished

`ExpectationPredicateTests` and `RetiredDispatchExpectationTests` are deleted, and
`InboxPredicateTests` drops the ladder-terminal case (`evaluate_ladder_terminal_findings` is
gone). No suite in this file imports `write_expectation_row` or
`evaluate_expectation_findings` anymore; expectation rows are an owner-visible deadline
surface and the sweep never evaluates them.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_agent_notifier.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the deletion of the
  expectation/ladder predicate test classes and the fact-only inbox-predicate surface.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `ExpectationPredicateTests`
  fixture kind swap from `ack-by` to `verdict-by` (ack-by retired with N16; verdict-by remains
  an active expectation kind). Verification metadata pinned until closeout stamps the
  260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the expectation-fixture rename
  (ack-by), the deletion of the turn-report staleness tests, and the new
  `RetiredDispatchExpectationTests` silence pins. Verification metadata pinned until closeout
  stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T12:41:53+00:00 — 260731-EFA-L6 S18-B09 curator: split terminal-catalog aliases from the consuming supervisor fixture builder; the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2: recorded the `_entry` rewrite this leaf already made to
  the body. The fixture no longer mirrors `TerminalCatalogEntry`'s shape, so its `turn_state`,
  `turn_state_changed_at` and `liveness_failures` parameters (and the `SeatTurnState` import) are
  gone; callers now use the row's own `with_turn_state(state, changed_at=…)` or `replace(...)`. The
  rest of the source diff is parameter-object adoption at fixture call sites —
  `Expectation`/`ExpectationSubject` for expectation rows, `InboxMessage`/`InboxRouting`/
  `InboxAddress`/`InboxPoster`/`InboxSubject` for `create_operator_inbox_entry`, and
  `schedule=EscalationSchedule(...)` for `evaluate_escalation_findings` — plus `ruff format`
  reflow. Every class and every test name is identical and no predicate, ladder, respawn or sweep
  assertion changed, but the file lost 24 lines, so both in-file citations were re-anchored (the F1
  pin L759-L789 → L747-L777 and the HFX2-L9 sweep block L531-L636 → L526-L621).
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T19:49+02:00 — Positional 260707-HFX2-L19 F1: documented the public-boundary
  regression that keeps a past-SLA `no-hosted-session` row silent below
  `PERSISTENT_FAILURE_ATTEMPTS` and emits only the exhausted counterpart. Recorded why the
  no-catalog fixture mutation-pins `_delivery_failure_still_retrying`. Verification metadata remains
  pinned until manager-owned closeout stamps the eventual L19 code commit.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: covered pair-scoped findings/coalescing/routing and
  sweep-clock delivery; recorded the bounded O4 fixed-point adjustment.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: covered replacement-leaf progress suppression and the
  one-row redelivery budget on the log-confirmed delivery path. Verification metadata remains pinned
  until closeout stamps the eventual L15 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: added chain-progress suppression,
  rung-floor/same-sweep guard, and current-manager dead-upstream regressions; recorded the unbound-
  worker S1 follow-up. Verification metadata remains pinned until closeout stamps the eventual L13
  code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: added supervisor regressions for one signal per cooldown,
  mid-turn pane-signal suppression with no owner inbox row, restart/backlog non-burst before the
  900-second floor, and one-second sweeps that tick heartbeat without minting per-second signal
  rows. Verification metadata pinned until closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R1/R2/R4/R6): added terminal-ladder
  predicate/integration tests proving dead/no-hosted-session terminal-rung rows become
  `ladder-resolved` and are not redelivered, plus a redeliver-budget integration proving attempts are
  capped per sweep while heartbeat backlog/duration metrics advance. Verification metadata pinned
  until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (escalation ladder + dead-man respawn, R2-R6): added
  `EscalationPredicateTests` (SLA-due/not-yet-due), `DeadUpstreamPredicateTests` (dead-owner fires,
  live-owner and no-provenance stay silent), and `LadderWalkIntegrationTests` — the R6 fixtures: a
  silent seat climbing all three rungs then hitting the rung-3 ceiling, a dead intermediate manager
  skipped at rung 2, a dead manager with live workers triggering respawn + orphan surfacing (workers
  themselves asserted unchanged), and the dead-upstream sweep signaling the grandparent. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T18:45+02:00 — Created for 260707-HFX2-L2 (supervisor sweep + predicates, R2-R6):
  sixteen tests — one per predicate family (pane/expectation/turn-report/inbox/seat-liveness, each
  with its fire + silent + edge-case variants), one seeded-drift sweep integration test asserting
  the full finding→action→heartbeat chain, a no-routable-owner edge case, and two heartbeat-specific
  cases (zero-drift still ticks; sweep count increments). Documents the fake-paster
  monotonic-chip-counter fix (a live F-V/N1 instance found while writing this suite) as a preserved
  invariant for future test additions. Verification metadata pinned until closeout stamps the
  260707-HFX2-L2 commit.
