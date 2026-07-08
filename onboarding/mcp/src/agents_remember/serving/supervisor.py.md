# mcp/src/agents_remember/serving/supervisor.py

| Field                  | Value                                         |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                   |
| path                   | `mcp/src/agents_remember/serving/supervisor.py`  |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-08T23:15+02:00                            |
| lastVerifiedCommitHash | `69314ba144d9461a0daec43f1d1aa5ce1ab18946`        |
| lastVerifiedCommitDate | 2026-07-08T09:40:32+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`supervisor.py` is the deterministic supervisor sweep (260707-HFX2-L2), now also the P-15 tier-3
escalation-ladder + dead-man-respawn host (260707-HFX2-L4): P-15 tiers 1-3 as a pure, zero-token,
zero-model loop hosted in the serving daemon. "The model is never the polling layer" — every
intervention the pilot run needed (empty composer post-boot, stacked paste chips, "esc to
interrupt", modal dialogs, expectation-row expiry, turn-report staleness, unacked redelivery,
seat-liveness drift, an unacked signal climbing renudge -> skip-level -> developer attention, a
persistently silent seat being respawned rather than waited on, a dead owner's seat being detected
and its grandparent signaled) is detectable by a mechanical predicate over an authoritative store,
and this module evaluates those predicates every sweep and acts — redeliver, auto-nudge,
signal-emit, escalate-rung, signal-grandparent — logging every action as an observer event.
Level-triggered by design: any event lost anywhere (a dropped push, a crashed dispatch call) is
caught by the NEXT sweep, the backstop even protocol-grade push (A2A/MCP) needs (the Inngest
Oct-2025 incident is the reference case for "at-least-once push still needs a reconciliation
sweep").

## Code Commentary

### Logic

**R3 (#22 root-cause rule, non-negotiable and structurally enforced by import discipline, not a
runtime guard):** every predicate takes a store/catalog object directly — `TerminalCatalog`,
`OperatorInboxStore`, `ExpectationRowStore`, `OrchestrationNudgeStore` — and this module imports
nothing from `serving/projector.py` or `observer/reducer.py`. The projection is a consumer of the
`orchestration.supervisor.*` events this module emits, never a source.

**`SupervisorContext`** is the one seam every predicate/action function reads through: catalog,
host, paster, the four stores, the heartbeat store, `coordination_root`, plus tunables —
`stale_seat_seconds` (seat-liveness grace, derived by the caller as `4x` the sweep interval floored
at 60s), `redeliver_rate_limit_seconds` (passed straight to `OperatorInboxStore
.list_redeliverable`, `None` inherits that store's own default), and — since 260707-HFX2-L4 —
`escalation_sla_seconds`/`escalation_rung_seconds`/`respawn_after_rung`: the ladder's own knobs as
plain primitives (dicts/int), NOT a typed `EscalationSettings` object, matching the existing
`stale_seat_seconds`-style decoupling from the kernel settings loader; `serving/app.py`'s
`_supervisor_context()` resolves the real `settings.escalation.*` values in. A new predicate family
or a store swap is added as a new `evaluate_*_findings` function plus a branch in `act_on_finding` —
never by reaching into the projection.

**R2 predicates** (`evaluate_predicates` runs all seven every sweep, concatenating their findings):

- `evaluate_pane_findings` (R2a) — every `RUNNING` `kind == "harness"` catalog row's captured pane
  text through `pane_signals.classify_pane_signal`; a `normal` classification produces no finding.
- `evaluate_expectation_findings` (R2b) — `ExpectationRowStore.overdue(now=)` filtered to
  `briefed-by`/`verdict-by`/`ack-by` (`_INACTIVE_EXPECTATION_KINDS`); `turn-report-by` is handled
  separately below since it needs a second artifact check.
- `evaluate_turn_report_findings` (R2c) — for each overdue `turn-report-by` row, resolves the
  standard worker turn-report path via `turn_report_path_for_leaf_key` (splitting the qualified
  `repo/master/leaf-id` key and calling `orchestration_artifacts.turn_report_artifact` against
  `coordination_root/tasks/<repo>/<master>`) and fires only when `missing_artifact()` — its FIRST
  caller, `controlplane/orchestration_nudges.py:112-114` — confirms the artifact is truly
  missing/empty, so a worker who wrote the report before the row was consumed does not trip a false
  stale-report action.
- `evaluate_inbox_findings` (R2d) — `OperatorInboxStore.list_redeliverable(now=,
  rate_limit_seconds=)` directly.
- `evaluate_seat_liveness_findings` (R2e) — the L5 hysteresis + L8 turn-state join with graceful
  degradation: a row the L8 prober has classified fires when `turn_state == "stale"` past
  `stale_seconds`; a row it has NEVER classified (legacy/degraded) falls back to the L5 primitive
  alone — `liveness_failures > 0` on an otherwise-`running` row.
- `evaluate_escalation_findings` (260707-HFX2-L4, R2) — every pending, unacked
  `OperatorInboxStore` row due for its NEXT ladder rung, per `escalation_ladder.rung_due` (the
  per-`message_kind` SLA at rung 0, that rung's own re-anchored dwell thereafter).
- `evaluate_dead_upstream_findings` (260707-HFX2-L4, R4 — P-6 made mechanical) — every live
  (`status == "running"`) spawned worker/manager catalog row whose OWN recorded
  `spawned_by_session` is dead (`signal_routing.is_seat_dead`); a row with NO recorded provenance at
  all is a legacy/unrouted row, not a dead-owner case, and is skipped.

**R4 actions** (`act_on_finding` dispatches by `finding.kind`):

- `inbox-redeliverable` → `_redeliver`: calls `serving.inbox_delivery.deliver_inbox_entry` (the
  current injector entry point over `TerminalPaster`); on a failing redeliver past
  `PERSISTENT_FAILURE_ATTEMPTS` (5), calls `_escalate_inbox_entry` (`OperatorInboxStore
  .mark_escalated` — a distinct, rung-agnostic "this row is now escalatable" stamp; the ladder's own
  rung transitions go through the separate `advance_rung`, not this call).
- `expectation-overdue` / `turn-report-stale` → `_auto_nudge`: derives the owner via
  `signal_routing.derive_signal_owner`, records through `OrchestrationNudgeStore.record` (the
  EXISTING per-target rate limit — `missing_artifact()` finally gets its caller here too, via the
  nudge reason mapping `_nudge_reason`), posts an owner-addressed inbox row via `_post_owner_signal`,
  and calls `_mark_expectation_missed` (the sweep is the reserved caller of
  `ExpectationRowStore.mark_missed`, idempotent every sweep the row stays overdue — per
  `expectation_rows.py:93-97`'s own docstring: "this leaf only reserves the transition — the L2
  sweep is the actual caller").
- `pane-signal` / `seat-liveness` → `_signal_emit`: derives the owner, posts an owner-addressed
  `escalation`-kind inbox row via the same `_post_owner_signal` helper.
- `escalation-due` → `_escalate_rung` (260707-HFX2-L4, R2/R3): calls `escalation_ladder.next_step`
  for the row's next rung/owner (skipping the action entirely if nothing is routable), posts the
  signal via `_post_owner_signal` (rung 1 reuses `message_kind="nudge"`, rung 2/3 reuse
  `"escalation"` — no new `InboxMessageKind` values were added, kept distinguishable via the
  `orchestration.escalation.rung` event's own `rung`/`action` fields), then calls
  `OperatorInboxStore.advance_rung` to durably stamp the transition. As a side effect of the SAME
  transition (not a separate finding) — once the row reaches `respawn_after_rung` AND
  `escalation_ladder.seat_is_suspect` confirms the addressee seat is actually dead/stalled — it
  calls `_respawn_suspect`.
- `dead-upstream` → `_signal_dead_upstream` (260707-HFX2-L4, R4): signals the seat's grandparent via
  the SAME two-hop, dead-node-skipping walk (`signal_routing.derive_skip_level_owner`) rung 2 uses —
  doctrine carried verbatim into the action's `ask` text: "a spawned seat NEVER absorbs its dead
  owner's role — it continues its own brief and escalates."
- Anything else → a `"none"`/`"skipped"` no-op result (defensive default, not currently reachable
  from `evaluate_predicates`'s seven kinds).

`_respawn_suspect(ctx, agent_id, *, now)` (260707-HFX2-L4, R3, called from inside `_escalate_rung`,
not dispatched via `act_on_finding` — it is a side effect of a rung transition, not its own
finding): derives the suspect seat's owner (or the orchestrator, for a manager — the EXISTING
one-hop `derive_signal_owner` already resolves this, no special-casing needed), gathers the seat's
pending inbox queue (`OperatorInboxStore.list_pending`), retires the husk via HFX-L8's
`serving/retire.py::retire_entry`, and posts a respawn-directive signal carrying the pending-queue
ids for the successor to re-deliver. If the retired seat's `spawn_role == "manager"`, its still-
running workers are gathered via the new `orphan_policy.find_orphaned_workers` and surfaced in the
SAME respawn event (`orphanedWorkers`) — never auto re-parented, never absorbing the dead manager's
role (R4 doctrine).

Every action calls `_log_event` to append one `orchestration.supervisor.redeliver` /
`.escalate` / `.signal` / `.respawn` / `.dead-upstream` event (or the dedicated
`orchestration.escalation.rung` event for `_escalate_rung`, or the existing `orchestration.nudge`
kind for auto-nudge, matching that tool's own event shape) via `EventStore.append` — so the
dashboard river shows what code did on whose behalf with no separate reporting path.

**`run_supervisor_sweep(ctx, *, now)`** is the sweep entry point: evaluate every predicate, act on
every finding, then tick `ctx.heartbeat_store.tick(now=now)` LAST and UNCONDITIONALLY — even a
zero-finding sweep proves supervisor liveness (R5). Returns a `SupervisorSweepResult` (findings +
actions + `swept_at`).

### Conventions

Frozen dataclasses throughout (`SupervisorFinding`, `SupervisorActionResult`,
`SupervisorSweepResult`, `SupervisorContext`) matching the project's `McpRuntimeConfig`-style
convention. Private action helpers are prefixed `_` and take `ctx`/`finding`/`now` uniformly.

### Invariants And Boundaries

- **R3 is enforced by import discipline, not a runtime guard** — this module's imports are the
  contract; keep any new predicate reading a store directly, never the projection.
- **Level-triggered, not edge-triggered:** every predicate re-evaluates the CURRENT store state
  every sweep; a missed action on one sweep is simply re-found and re-acted-on the next.
- **The escalation ladder's logic lives in `controlplane/escalation_ladder.py`, not here.** This
  module is the sole caller (`evaluate_escalation_findings`/`_escalate_rung`) that reads the pure
  walker's `rung_due`/`next_step`/`seat_is_suspect` and performs the delivery + durable
  `advance_rung` stamp; no ladder decision logic is duplicated in this file.
- **`_respawn_suspect` is a side effect of a rung transition, not its own dispatched finding** —
  it fires from inside `_escalate_rung` once `respawn_after_rung` + `seat_is_suspect` both hold,
  never from a separate `evaluate_*_findings` entry.
- **`_mark_expectation_missed` is idempotent-by-design, not gated behind an action-failure count** —
  matches `expectation_rows.py`'s own documented contract for that transition.
- **Every action is logged, whether it "succeeds" or is skipped** (e.g. "no routable owner") —
  `_log_event` calls happen inside the action helpers themselves, not conditionally at the call
  site, except where an action short-circuits before attempting delivery (`"skipped"` results with
  no source id / no pending entry do not log, since nothing was attempted).
- **Pure functions over injected stores** — every predicate/action function is independently
  testable against fixture stores with no supervisor-loop scaffolding required (see
  `test_supervisor.py`).

### Todos

No known follow-up in this file itself. Two gaps documented in this leaf's builder report (not
follow-ups against THIS module, but scope boundaries this module's callers should know): rung 3's
developer surfacing rides the existing dashboard-visible `OperatorInboxStore` row
(`recipientRole="developer"`) rather than a dedicated attention-queue tile, since the 260628
developer-notification seam does not exist in this repo; and `orphan_policy.find_orphaned_workers`
is detection/surfacing only — no leaf yet auto-reparents an orphaned worker to a respawned manager.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
supervisor-sweep-specific behavior; this is same-repository control-plane plumbing whose design
source is the pilot-observer log (P-15) and the leaf task doc, not an external spec.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this sweep; the P-15 pilot-run predicate list and the leaf task doc (R1-R6) are the source of truth. | L1-L470 | [supervisor.py](supervisor.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `supervisor_loop`/`_supervisor_context` in `app.py` construct one `SupervisorContext` per sweep iteration and call `run_supervisor_sweep` via `asyncio.to_thread` on the settings-driven interval. | `supervisor_loop`; `_supervisor_context` | [app.py](app.py.md) |
| The pane classifier `evaluate_pane_findings` calls per running harness row. | `classify_pane_signal` | [pane_signals.py](pane_signals.py.md) |
| The heartbeat store `run_supervisor_sweep` ticks unconditionally at the end of every sweep, and the staleness helpers built on top of it. | `SupervisorHeartbeatStore` | [supervisor_heartbeat.py](supervisor_heartbeat.py.md) |
| The expectation-row store R2b/R2c read directly, including the reserved `mark_missed` transition this module is the caller of. | `ExpectationRowStore.overdue`; `mark_missed` | [../controlplane/expectation_rows.py](../controlplane/expectation_rows.py) |
| The operator inbox store R2d/R4a/R4c read and write directly, including the reserved `mark_escalated` transition and the ladder's own `advance_rung` transition. | `OperatorInboxStore.list_redeliverable`; `mark_escalated`; `advance_rung` | [../controlplane/operator_inbox_store.py](../controlplane/operator_inbox_store.py) |
| The pure escalation-ladder walker `_escalate_rung` reads for the row's next rung/owner. | `rung_due`; `next_step`; `seat_is_suspect` | [../controlplane/escalation_ladder.py](../controlplane/escalation_ladder.py.md) |
| The two-hop, dead-node-skipping owner derivation `_escalate_rung`'s rung-2 branch and `_signal_dead_upstream` both call, plus the liveness check `evaluate_dead_upstream_findings`/`seat_is_suspect` use. | `derive_skip_level_owner`; `is_seat_dead` | [../controlplane/signal_routing.py](../controlplane/signal_routing.py.md) |
| The orphan-detection hook `_respawn_suspect` calls when the retired seat was a manager. | `find_orphaned_workers` | [../controlplane/orphan_policy.py](../controlplane/orphan_policy.py.md) |
| The HFX-L8 retirement primitive `_respawn_suspect` calls to retire a confirmed-suspect seat's husk. | `retire_entry` | [retire.py](retire.py.md) |
| `missing_artifact()` gets its first real caller here (R2c) — previously an uncalled function. | `missing_artifact` | [../controlplane/orchestration_nudges.py](../controlplane/orchestration_nudges.py) |
| The standard turn-report artifact path helper `turn_report_path_for_leaf_key` resolves against, reused rather than re-derived. | `turn_report_artifact` | [../controlplane/orchestration_artifacts.py](../controlplane/orchestration_artifacts.py) |
| The owner-derivation helper both `_auto_nudge` and `_signal_emit` call before posting an owner-addressed inbox row. | `derive_signal_owner` | [../controlplane/signal_routing.py](../controlplane/signal_routing.py) |
| The current injector entry point `_redeliver`/`_post_owner_signal` deliver through. | `deliver_inbox_entry` | [inbox_delivery.py](inbox_delivery.py.md) |
| The terminal catalog every pane/seat-liveness predicate reads directly (R3). | `TerminalCatalog.list` | [terminal_catalog.py](terminal_catalog.py.md) |
| Failing-first predicate unit tests (one per family) plus one seeded-drift sweep integration test asserting the full finding→action chain, heartbeat tick included. | `SupervisorTests`; sweep integration test | [../../../tests/test_supervisor.py](../../../tests/test_supervisor.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local sweep; the level-triggered-reconciliation design rationale cites an external incident (Inngest, Oct 2025) only as research justification, not a code boundary. | — | — |

## Update History

- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (P-15 tier 3, escalation ladder + dead-man respawn,
  R1-R6): two new predicates (`evaluate_escalation_findings`/`evaluate_dead_upstream_findings`) and
  two new actions (`_escalate_rung`/`_signal_dead_upstream`), calling through the new
  `controlplane/escalation_ladder.py` walker and `signal_routing.derive_skip_level_owner`/
  `is_seat_dead`. `_escalate_rung` durably stamps rung transitions via the new
  `OperatorInboxStore.advance_rung` and, past `respawn_after_rung`, calls new `_respawn_suspect`
  (retires the husk via HFX-L8's `retire_entry`, re-delivers the pending queue to the successor via
  the signal payload, and surfaces any now-orphaned workers via new `orphan_policy
  .find_orphaned_workers` when the retired seat was a manager). `SupervisorContext` gained the
  `escalation_sla_seconds`/`escalation_rung_seconds`/`respawn_after_rung` plain-primitive knobs,
  resolved per-use by `serving/app.py`'s `_supervisor_context()`. No new `InboxMessageKind` values
  were added (rung 1 reuses `"nudge"`, rung 2/3/respawn/dead-upstream reuse `"escalation"`) —
  distinguishable via the dedicated `orchestration.escalation.rung`/`.respawn`/`.dead-upstream`
  observer events and the row's own `rung` field. Two gaps documented, not silently absorbed: rung
  3 surfaces via the existing dashboard-visible inbox row (no 260628 developer-notification seam
  exists in this repo yet); orphan re-parenting is detection/surfacing only (no auto-reparent
  action). Verification metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T18:45+02:00 — Created for 260707-HFX2-L2 (supervisor sweep + predicates, R1-R6): the
  deterministic sweep — `SupervisorContext`, the five R2 predicate families
  (`evaluate_pane_findings`/`evaluate_expectation_findings`/`evaluate_turn_report_findings`/
  `evaluate_inbox_findings`/`evaluate_seat_liveness_findings`), the R4 action dispatcher
  (`act_on_finding` → `_redeliver`/`_auto_nudge`/`_signal_emit`, each logging an
  `orchestration.supervisor.*` event), and `run_supervisor_sweep` (evaluate → act → tick heartbeat
  unconditionally, R5). Gives `missing_artifact()` its first caller and
  `ExpectationRowStore.mark_missed`/`OperatorInboxStore.mark_escalated` their reserved-transition
  caller. Builds no escalation ladder itself (HFX2-L4's job) and touches no
  `terminal_paste.py` internals (HFX2-L3's job) — calls through their current public surfaces only.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
