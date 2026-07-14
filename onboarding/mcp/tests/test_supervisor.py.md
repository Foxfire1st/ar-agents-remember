# test_supervisor.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_supervisor.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T19:49+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b`|
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`.

## Purpose

`test_supervisor.py` covers the deterministic supervisor sweep (`serving/supervisor.py` +
`serving/supervisor_heartbeat.py`, 260707-HFX2-L2 R2-R6): one unit test per predicate family, the
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

Twenty-five tests (sixteen original R2/R6 tests plus nine new 260707-HFX2-L4 tests), `NOW =
datetime(2026, 7, 8, 12, 0, 0, tzinfo=UTC)` as the shared fixed clock:

- **Pane predicate (R2a):** `test_mid_turn_pane_fires_a_finding`, `test_normal_pane_fires_nothing`,
  `test_terminal_kind_rows_are_never_pane_classified` (a `kind="terminal"` row is skipped
  regardless of its captured text — the predicate only ever classifies `kind="harness"` rows).
- **Expectation predicate (R2b):** `test_overdue_briefed_by_row_fires`,
  `test_not_yet_due_row_is_silent` (a row whose deadline has not yet passed produces no finding).
- **Turn-report predicate (R2c):** `test_missing_report_fires_when_row_is_overdue`,
  `test_present_report_does_not_fire` (an overdue row whose artifact DOES exist and has content is
  silent — pins that `missing_artifact()` is a real second check, not a rubber stamp on
  overdue-ness), `test_malformed_leaf_key_is_skipped_not_guessed`
  (`turn_report_path_for_leaf_key` returns `None` for a key not in the `repo/master/leaf-id` shape,
  and the predicate skips rather than guessing a path).
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
  ladder through `run_supervisor_sweep` end-to-end, not the pure predicates in isolation —
  `test_silent_seat_climbs_rung_one_then_two_then_three` runs four successive sweeps over one
  unacked row and asserts it climbs rung 1 -> 2 -> 3 exactly on schedule, then proves rung 3 is a
  hard ceiling (a fifth sweep, far past every threshold, still reads rung 3).
  `test_dead_intermediate_manager_is_skipped_at_rung_two` seeds a row already at rung 1 whose
  addressee's manager is `terminated`, and asserts the rung-2 transition's owner event lands on the
  ORCHESTRATOR, never the dead manager. `test_dead_manager_with_live_workers_respawns_and_surfaces_
  orphans` is the R3+orphan-policy fixture: a manager-addressed row past the respawn threshold with
  the manager's OWN turn-state stale triggers `_respawn_suspect` — the manager's catalog row flips
  to `terminated`, a SINGLE `orchestration.supervisor.respawn` event carries both live workers under
  `orphanedWorkers`, and the workers themselves are asserted UNCHANGED (`status == "running"`) —
  proving they are surfaced, never auto-retired or re-parented themselves.
  `test_dead_upstream_signals_the_grandparent` seeds the same dead-manager-with-live-worker shape
  and asserts the sweep's OWN `dead-upstream` finding (not the ladder) fires for the worker and the
  `orchestration.supervisor.dead-upstream` event names the orchestrator as `grandparentAgentId`.
- **Sweep integration:** `test_seeded_drift_produces_expected_actions_and_ticks_heartbeat` seeds
  drift across pane-signal, expectation-overdue, inbox-redeliverable, AND seat-liveness
  simultaneously in one sweep and asserts the expected action set, delivery outcomes, the
  `mark_missed` side effect, and the heartbeat tick — the R6-mandated "seeded drift → expected
  actions" integration case. HFX2-L8 adds a dead-seat terminal integration asserting the row becomes
  durable `ladder-resolved`, emits one supervisor observer event, and is not redelivered, plus a
  budget integration asserting a low `redeliver_budget` caps attempts while heartbeat backlog metrics
  still tick. HFX2-L9 adds four more sweep/action regressions:
  `test_repeated_seat_liveness_sweeps_emit_one_signal_per_cooldown` posts one owner signal during
  the cooldown and a second only after 901 seconds;
  `test_mid_turn_pane_signal_is_observed_without_owner_inbox_noise` proves `pane-signal: mid-turn`
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
`Literal` aliases (`TerminalSessionKind`/`TerminalSessionStatus`/`SeatTurnState`) per `pyright`'s
finding during this leaf.

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
- The HFX2-L9 signal-cooldown tests use a real temp-rooted `SupervisorSignalCooldownStore`; they do
  not fake the cooldown decision.
- `LadderWalkIntegrationTests` deliberately drives the FULL sweep (`run_supervisor_sweep`), not the
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines the supervisor sweep; the leaf task doc (R1-R6) and the P-15 pilot-observer log are the source of truth this suite pins. | L1-L449 | [test_supervisor.py](test_supervisor.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test: every predicate, the action dispatcher, and the sweep entry point. | whole module | [../src/agents_remember/serving/supervisor.py](../src/agents_remember/serving/supervisor.py) |
| The heartbeat store the zero-drift and second-sweep tests exercise directly. | `SupervisorHeartbeatStore` | [../src/agents_remember/serving/supervisor_heartbeat.py](../src/agents_remember/serving/supervisor_heartbeat.py) |
| The catalog entry fixture builder's typed fields come from this module's `Literal` aliases. | `TerminalCatalogEntry` | [../src/agents_remember/serving/terminal_catalog.py](../src/agents_remember/serving/terminal_catalog.py) |
| The fake-host casting convention this suite reuses rather than inventing its own duck-typing idiom. | `cast(TerminalHost, fake)` | [test_terminal_ws.py](test_terminal_ws.py.md) |
| The pure ladder walker the escalation predicate/integration tests exercise indirectly through the sweep. | `rung_due`; `next_step`; `seat_is_suspect` | [../src/agents_remember/controlplane/escalation_ladder.py](../src/agents_remember/controlplane/escalation_ladder.py.md) |
| The orphan-detection hook the dead-manager-with-live-workers fixture asserts surfaces both workers. | `find_orphaned_workers` | [../src/agents_remember/controlplane/orphan_policy.py](../src/agents_remember/controlplane/orphan_policy.py.md) |
| The operator-inbox terminal state and compaction semantics used by the L8 sweep tests. | `mark_ladder_resolved`; `list_redeliverable` | [../src/agents_remember/controlplane/operator_inbox_store.py](../src/agents_remember/controlplane/operator_inbox_store.py.md) |
| The persisted signal cooldown store used by the HFX2-L9 repeated-sweep regressions. | `SupervisorSignalCooldownStore` | [../src/agents_remember/controlplane/supervisor_signals.py](../src/agents_remember/controlplane/supervisor_signals.py.md) |
| The F1 regression pin proves hosted-delivery failures stay below the generic ladder until persistent retry exhaustion. | L759-L789 | [test_supervisor.py](agents-remember/mcp/tests/test_supervisor.py) |
| The production predicate and its public escalation-evaluation call site are the behavior the F1 test mutation-pins. | L477-L505 | [supervisor.py](agents-remember/mcp/src/agents_remember/serving/supervisor.py) |
| HFX2-L9 tests cover signal cooldown, mid-turn suppression, restart non-burst before the 900-second floor, and one-second sweeps without per-second signal rows. | L531-L636 | [test_supervisor.py](agents-remember/mcp/tests/test_supervisor.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Sweep-local behavior only. | — | — |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History
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
