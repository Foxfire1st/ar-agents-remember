# mcp/src/agents_remember/serving/agent_notifier.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`agent_notifier.py` is the deterministic agent-notifier sweep (260707-HFX2-L2): a pure,
zero-token, zero-model loop hosted in the serving daemon. "The model is never the polling layer"
— every intervention the pilot run needed (pane state, unacked redelivery, seat-liveness drift,
a dead owner's seat detected and its grandparent signaled, and a worker turn ending or a
non-reacting seat reaching its owner) is detectable by a mechanical predicate over an
authoritative store, and this module evaluates those predicates every sweep and relays facts —
redeliver, owner signal, state-signal, compound-idle, non-reaction, boundary drain — logging
every action as an observer event. **260713-TES-L5** removes the judgment layer outright: no
suspect classification, no escalation rungs, no respawn, and no expectation interpretation —
the timed escalation ladder is deleted, not dormant. **260713-TES-L4** (retained) adds the
deliver-until-LANDED sweep semantics: the formal terminal vocabulary fold
(`_fold_legacy_landed`), the N14 rebind/grace/expiry action family, the N3 attempt-ceiling
`unresolved` terminal, and the §9 pending-TTL expiry.
HFX2-L9 makes the sweep safe at fast observation cadence: redelivery calls pass the configured
900-second floor into the delivery path, repeated pane/seat-liveness signals use persisted
cooldown state before minting another owner inbox row, and `pane-signal: mid-turn` is treated as a
busy observation rather than immediate escalation noise.
Level-triggered by design: any event lost anywhere (a dropped push, a crashed dispatch call) is
caught by the NEXT sweep, the backstop even protocol-grade push (A2A/MCP) needs (the Inngest
Oct-2025 incident is the reference case for "at-least-once push still needs a reconciliation
sweep").

## Code Commentary

Current sweep authority is `run_agent_notifier_sweep` (source lines 96–190), composed with `_agent_notifier_evaluation.evaluate_predicates` (381–433). The predicate set contains redelivery, structural owner facts, rebind/expiry, state signals, compound idle, non-reaction and boundary drain; it contains no pane-action, expectation-overdue, respawn or ladder evaluator. Older milestones below explain previous mechanisms and must not re-enable them.
Since 260713-TES-L3 the sweep also hosts the compound-idle relay to orchestrators (one
`state-signal` per manager+all-workers idle set) and exports its constants/helpers on the
facade `__all__`.

### 260713-TES-L3 Compound-Idle Relay Wiring

The sweep now composes `evaluate_compound_idle_findings` inside `evaluate_predicates`
(after `evaluate_state_signal_findings`, before `evaluate_non_reaction_findings`) and maps
`compound-idle-due` → `_emit_compound_idle` in `_FINDING_ACTIONS` (see
`_agent_notifier_actions.py.md`). Delivery rides the existing state-signal boundary gate and
landed terminality unchanged — no new mechanism.

The facade `__all__` cit:([`__all__`], mcp/src/agents_remember/serving/agent_notifier.py:213-258) now exports `COMPOUND_IDLE_SWEEP_LATENCY_SECONDS`,
`compound_idle_response`, `compound_idle_signature`, `evaluate_compound_idle_findings`, and
`_emit_compound_idle` alongside the L2 relay surface; `test_facade_surface.py` pins the
surface. `NON_REACTION_WINDOW_SECONDS` stays exported (reused by the manager residue path).

### 260713-TES-L4 Deliver-Until-LANDED Sweep Wiring

`run_agent_notifier_sweep` cit:([`run_agent_notifier_sweep`], mcp/src/agents_remember/serving/agent_notifier.py:93-195) now calls `_fold_legacy_landed` after
reconcile/compact and before predicate evaluation: pre-migration rows that satisfied the
retired by-rule landing predicate (`state-signal` + `delivered` + `accepted`) gain the formal
`landed` state exactly once through the lock-held latest-fold transition, and the sweep's
snapshot is refreshed from the returned entry (F1). The action map gains the
`rebind-due`/`rebind-expired`/`inbox-ttl-expired` family (see `_agent_notifier_actions.py.md`);
`evaluate_rebind_findings`/`evaluate_pending_expiry_findings` join `evaluate_predicates`, and
the facade `__all__` cit:([`__all__`], mcp/src/agents_remember/serving/agent_notifier.py:229-271) exports `_rebind_due`, `_rebind_expired`, `_expire_pending`,
`evaluate_rebind_findings`, and `evaluate_pending_expiry_findings` alongside the existing relay
surface. A landed row produces no retry, nudge, or escalation of any kind (N16 regression).

### 260713-TES-L5 Judgment Demolition Wiring

The sweep no longer composes `evaluate_expectation_findings`, `evaluate_escalation_findings`, or
`evaluate_ladder_terminal_findings`, and `_FINDING_ACTIONS` carries no
`expectation-overdue`/`inbox-ladder-terminal`/`escalation-due` handlers. The facade `__all__`
cit:([`__all__`], mcp/src/agents_remember/serving/agent_notifier.py:228-253) drops every deleted
symbol (`_auto_nudge`, `_escalate_rung`, `_respawn_suspect`, `_rung_entry`,
`_resolve_ladder_terminal`, `_mark_expectation_missed`, `_ladder_terminal_and_dead`,
`_delivery_failure_still_retrying`, `EscalationSchedule`, `_INACTIVE_EXPECTATION_KINDS`,
`evaluate_expectation_findings`, `evaluate_escalation_findings`,
`evaluate_ladder_terminal_findings`, `DEFAULT_ESCALATION_*`). The `AgentNotifierContext` no
longer carries `nudge_store`/`nudge_rate_limit_seconds`/`escalation_sla_seconds`/
`escalation_rung_seconds`/`respawn_after_rung`; `escalation_budget` (250) survives as the
per-sweep owner-signal load-shed cap. `_fold_legacy_landed` and the confirmed-gone reclamation
fold still write/accept the legacy `ladder-resolved` terminal state (reviewer F4).

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### 260713-TES-L1 Rename Window

This module is renamed from `supervisor.py` (internal-only rename, no wire/persisted surface);
every `Supervisor*`/`_supervisor_*`/`run_agent_notifier_sweep` identifier is now
`AgentNotifier*`/`_agent_notifier_*`/`run_agent_notifier_sweep`, and the sweep is hosted by
`_agent_notifier_loop`/`_agent_notifier_context` in `_app_lifespan.py`. The compatibility window
carries four seams, all code-level and all removed with the window at TES master integration:

- **Events:** every action logs through `_log_event` under `orchestration.agent-notifier.*` AND
  the legacy `orchestration.supervisor.*` prefix (constants `AGENT_NOTIFIER_EVENT_PREFIX` +
  `LEGACY_SUPERVISOR_EVENT_PREFIX` in `_agent_notifier_actions.py`); non-notifier events
  (`orchestration.nudge`, `orchestration.escalation.rung`) are not duplicated.
- **Durable row values:** NEW inbox rows write `createdBy="agent-notifier"` and the ask prefix
  `"Agent notifier observed ..."`; readers (`_find_coalescible`,
  `_inactivity_signal_chain_progressed`, `inbox_reclamation._eligible`) accept both legacy and
  current values.
- **Ask identity:** `_seat_liveness_ask_identity` treats both seat-liveness ask prefixes as ONE
  identity, so a new-format re-fire renews a legacy-prefix pending row (fix round 1, reviewer F1).
- **Retained durable names:** `supervisor-heartbeat.json`, `supervisor-signals.jsonl`,
  `ar-supervisor-signal/v1`, and `store="supervisor-signals"` stay byte-identical until their
  owned migrations.

### 260712-TRH-L5 Confirmed-Gone Inbox Reclamation

Before predicates and redelivery, `run_agent_notifier_sweep` passes one folded inbox snapshot through
`reconcile_and_compact`. The narrow resolver considers only pending agent-notifier-created nudge or
escalation rows with a subject id; catalog `terminated` is direct proof, while a compacted
tombstone needs one successful exact-name `ar-<subject-id>` tmux snapshot. Running, landed,
exited, tmux-present, and tmux-command-failed evidence keeps rows. Resolved rows use the existing
`ladder-resolved` state and `subject-session-confirmed-gone` reason, then disappear in the same
sweep before redelivery is selected. The body-free aggregate `inbox-compacted` event reports
counts and evidence only, and is silent when a sweep has no physical removals or resolutions;
the existing TTL/cap fallback remains in force. `_log_inbox_compaction` owns only that aggregate
event assembly; extracting it from `run_agent_notifier_sweep` changes no predicate, transaction,
ordering, or event payload and keeps the sweep below the hard 100-line function limit.

Since 260731-EFA-L16 the callback's catalog read is hoisted BEFORE the inbox transaction:
`run_agent_notifier_sweep` fetches `ctx.catalog.list(include_terminated=True)` outside the lock and
the reconcile closure consumes that pre-fetched `catalog_entries`, so the lock-held callback
performs at most one deduplicated tmux snapshot and no catalog read. The callback remains
deliberately store-independent because the inbox lock can still be held for up to the tmux's
5-second timeout; future callbacks must not re-enter the store.

### 260707-HFX2-L17 Pair-Scoped AgentNotifier (historical milestone)

Every finding carries `seat_role`; expectations, inbox rows, signal cooldowns, coalescing, events,
and owner posts preserve the pair. Same-text findings on the same leaf coalesce only when the role
also matches, current discovery uses binding identity, and unbound replacements retain their
declared leaf. Redelivery and owner-signal writes now receive the sweep's injected timestamp, so
simulation and production retention decisions share one clock. Reviewer O4 is informational and
test-only: pair-scoped coalescing requires one extra bounded fixed-point snapshot, reflected by the
test limit moving from `seeded*8` to `seeded*9`; it is not an unbounded-growth signal.

### 260707-HFX2-L13 Manager-First Wake And Chain-Aware Suppression (historical milestone)

Expectation, missing-report, seat-liveness, redelivery, and escalation predicates now consult
leaf-chain progress before re-firing stale work. AgentNotifier-created inactivity rows preserve
`leafKey`/`subjectAgentId`; renewals readdress the current manager. Auto-nudge, signal emission, and
dead-upstream handling resolve the leaf's current manager first, with later upward movement left to
the timed ladder. Completion wake itself is posted through the MCP tool path documented separately.

`_SweepState.escalated_entry_ids` prevents duplicated findings from advancing one row twice in a
single sweep, complementing the persistent rung timestamps. This narrowly scoped guard is necessary
because multiple predicates can report the same durable row from one pre-sweep snapshot. Current
chain credit includes exact-leaf seats/current manager/unbound reviewer or curator in the same
worktree, but not unbound workers; the accepted S1 active-phase false-inactivity residual is routed to
HFX2-L14 S7. Manager targeting, five-minute rung floor, cooldowns, and completion wake are current
L13 truth.

### 260707-HFX2-L12 CS-6 Update (historical milestone)

The agent-notifier sweep now compacts and snapshots signal-cooldown and expectation stores once per sweep, threads those snapshots into cooldown and mark-missed actions, and caps escalation-rung findings by `escalation_budget` while leaving deferred rows level-triggered.

### 260713-TES-L2 Worker-State Relay Wiring

The sweep now hosts the worker→manager state-signal relay: `evaluate_predicates` composes the
three relay families (see R2 bullets), `_FINDING_ACTIONS` maps them to `_emit_state_signal`,
`_emit_non_reaction`, and `_drain_boundary`, and the owner-signal posting primitives
(`OwnerSignal`, `_find_coalescible`, `_post_owner_signal`) are re-exported from
`serving/owner_signals.py` for existing callers. `NON_REACTION_WINDOW_SECONDS` rides the module
`__all__`. The retired `turn-report-stale` finding/action and `turn_report_path_for_leaf_key`
are gone from the facade; `test_facade_surface.py` declares them in `REMOVED_FACADE_NAMES`.
No model consume exists anywhere on this path — state-signals create no ack-by expectations.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

### Logic

**260707-HFX2-L15 bounded redelivery.** The sweep's redelivery path now delegates to a
harness-log-confirmed input that may synchronously consume three calibrated windows. The configured
default budget is therefore one inbox row per sweep; deferred rows remain level-triggered for later
sweeps. Chain-progress suppression also recognizes an unbound worker/reviewer/curator only through
the explicit same-manager `replacementForLeaf` discriminator, never shared cwd.

**R3 (#22 root-cause rule, non-negotiable and structurally enforced by import discipline, not a
runtime guard):** every predicate takes a store/catalog object directly — `TerminalCatalog`,
`OperatorInboxStore`, `ExpectationRowStore`, `OrchestrationNudgeStore`,
`AgentNotifierSignalCooldownStore` — and this module imports
nothing from `serving/projector.py` or `observer/reducer.py`. The projection is a consumer of the
`orchestration.agent-notifier.*` events this module emits, never a source.

**`AgentNotifierContext`** is the one seam every predicate/action function reads through: catalog,
host, paster, the control-plane stores, the heartbeat store, `coordination_root`, plus tunables —
`stale_seat_seconds` (seat-liveness grace, derived by the caller as `4x` the sweep interval floored
at 60s), `redeliver_rate_limit_seconds` (passed straight to `OperatorInboxStore
.list_redeliverable` and `deliver_inbox_entry`, `None` inherits that store's own default),
`signal_cooldown_seconds` (passed to `AgentNotifierSignalCooldownStore.in_cooldown` before owner signal
posts), and — since 260707-HFX2-L4 —
`escalation_sla_seconds`/`escalation_rung_seconds`/`respawn_after_rung`: the ladder's own knobs as
plain primitives (dicts/int), NOT a typed `EscalationSettings` object, matching the existing
`stale_seat_seconds`-style decoupling from the kernel settings loader; `serving/app.py`'s
`_agent_notifier_context()` resolves the real `settings.escalation.*` values in. A new predicate family
or a store swap is added as a new `evaluate_*_findings` function plus a branch in `act_on_finding` —
never by reaching into the projection.

**260707-HFX2-L8 (dead-seat storm fix)** adds `_SweepState`, a mutable per-sweep inbox index with
the configured redelivery budget, pre-action pending count, and pre-action redeliverable list.
Inbox-mutating actions update this index after appending snapshots, so one sweep folds
`operator-inbox.jsonl` once instead of refolding the whole log for each finding. The sweep result
and heartbeat tick now carry pending/redeliverable inbox counts and last-sweep wall-clock duration.

**R2 predicates** (`evaluate_predicates` runs all ten every sweep, concatenating their findings):

- `evaluate_pane_findings` (R2a) — every `RUNNING` `kind == "harness"` catalog row's captured pane
  text through `pane_signals.classify_pane_signal`; a `normal` classification produces no finding.
- `evaluate_expectation_findings` (R2b) — `ExpectationRowStore.overdue(now=)` filtered to
  `verdict-by`/`ack-by` (`_INACTIVE_EXPECTATION_KINDS`); `turn-report-by` and `briefed-by` no
  longer drive any notifier finding on the worker→manager path (260713-TES-L2).
- `evaluate_state_signal_findings` (260713-TES-L2) — a running worker seat at `turn-ended` with
  a completed/interrupted terminal outcome not yet relayed emits one `state-signal-due` finding
  (evidence-id dedupe).
- `evaluate_compound_idle_findings` (260713-TES-L3) — a manager seat whose whole master-scoped
  live worker set is at a turn boundary and not yet relayed emits one `compound-idle-due`
  finding (episode-signature dedupe; zero-worker and unbound managers never form sets).
- `evaluate_non_reaction_findings` (260713-TES-L2, L3) — a seat still `turn-ended` with landed
  rows older than `NON_REACTION_WINDOW_SECONDS` relays the non-reaction residue fact
  (worker→manager AND manager→orchestrator since L3, one per episode).
- `evaluate_boundary_drain_findings` (260713-TES-L2) — pending rows whose target crossed a turn
  boundary after the last attempt are pushed (N15), bounded by the redelivery budget.
- `evaluate_inbox_findings` (R2d) — `OperatorInboxStore.list_redeliverable(now=,
  rate_limit_seconds=)` directly; in the real sweep L8 feeds it from `_SweepState` and schedules at
  most `AgentNotifierContext.redeliver_budget` delivery attempts.
- `evaluate_ladder_terminal_findings` (260707-HFX2-L8, R1) — pending rows already at the terminal
  ladder rung whose concrete `agentId` is dead/absent per `signal_routing.is_seat_dead`; live-seat,
  still-climbing, and role-only rows are not terminated.
- `evaluate_seat_liveness_findings` (R2e) — the L5 hysteresis + L8 turn-state join with graceful
  degradation: a row the L8 prober has classified fires when `turn_state == "stale"` past
  `stale_seconds`; a row it has NEVER classified (legacy/degraded) falls back to the L5 primitive
  alone — `liveness_failures > 0` on an otherwise-`running` row.
- `evaluate_escalation_findings` (260707-HFX2-L4, R2) — every pending, unacked
  `OperatorInboxStore` row due for its NEXT ladder rung, per `escalation_ladder.rung_due` (the
  per-`message_kind` SLA at rung 0, that rung's own re-anchored dwell thereafter). Since
  260707-HFX2-L7, `_delivery_failure_still_retrying` skips delivery-failure rows whose
  `deliveryState` is `"no-hosted-session"` or `"unconfirmed"` while `attemptCount` is still below
  `PERSISTENT_FAILURE_ATTEMPTS` and `escalatedAt` is unset; those rows exhaust the redelivery
  backoff path before the generic unacked ladder is allowed to advance them.
- `evaluate_dead_upstream_findings` (260707-HFX2-L4, R4 — P-6 made mechanical) — every live
  (`status == "running"`) spawned worker/manager catalog row whose OWN recorded
  `spawned_by_session` is dead (`signal_routing.is_seat_dead`); a row with NO recorded provenance at
  all is a legacy/unrouted row, not a dead-owner case, and is skipped.

**R4 actions** (`act_on_finding` dispatches by `finding.kind`):

- `inbox-redeliverable` → `_redeliver`: calls `serving.inbox_delivery.deliver_inbox_entry` (the
  current injector entry point over `TerminalPaster`); on a failing redeliver past
  `PERSISTENT_FAILURE_ATTEMPTS` (5), calls `_escalate_inbox_entry` (`OperatorInboxStore
  .mark_escalated` — a distinct, rung-agnostic "this row is now escalatable" stamp; the ladder's own
  rung transitions go through the separate `advance_rung`, not this call). In L8 this path uses the
  sweep index and refuses to push a terminal-rung dead-seat row. In HFX2-L9 it passes
  `ctx.redeliver_rate_limit_seconds` into the hosted delivery path, so retry scheduling stays at the
  configured/shared 900-second floor.
- `inbox-ladder-terminal` → `_resolve_ladder_terminal` (260707-HFX2-L8): calls
  `OperatorInboxStore.mark_ladder_resolved`, updates the sweep index, and logs one
  `orchestration.agent-notifier.ladder-resolved` event for the terminal transition. This is distinct
  from ack/consume.
- `expectation-overdue` / `turn-report-stale` → `_auto_nudge`: derives the owner via
  `signal_routing.derive_signal_owner`, records through `OrchestrationNudgeStore.record` (the
  EXISTING per-target rate limit — `missing_artifact()` finally gets its caller here too, via the
  nudge reason mapping `_nudge_reason`), posts an owner-addressed inbox row via `_post_owner_signal`,
  and calls `_mark_expectation_missed` (the sweep is the reserved caller of
  `ExpectationRowStore.mark_missed`, idempotent every sweep the row stays overdue — per
  `expectation_rows.py:93-97`'s own docstring: "this leaf only reserves the transition — the L2
  sweep is the actual caller").
- `pane-signal` / `seat-liveness` → `_signal_emit`: derives the owner, skips `pane-signal:
  mid-turn` as a busy pane state before posting, consults `AgentNotifierSignalCooldownStore` by
  owner/leaf/kind/detail, posts an owner-addressed `escalation`-kind inbox row via the same
  `_post_owner_signal` helper only when outside cooldown, then appends the cooldown record with the
  resulting delivery state.
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
  from `evaluate_predicates`'s eight kinds).

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

Every action calls `_log_event` to append one `orchestration.agent-notifier.redeliver` /
`.escalate` / `.signal` / `.respawn` / `.dead-upstream` event (or the dedicated
`orchestration.escalation.rung` event for `_escalate_rung`, or the existing `orchestration.nudge`
kind for auto-nudge, matching that tool's own event shape) via `EventStore.append` — so the
dashboard river shows what code did on whose behalf with no separate reporting path.

**`run_agent_notifier_sweep(ctx, *, now)`** is the sweep entry point: fold the inbox once into
`_SweepState`, evaluate every predicate, act on terminal rows and the budgeted redelivery set, then
tick `ctx.heartbeat_store.tick(...)` LAST and UNCONDITIONALLY — even a zero-finding sweep proves
agent-notifier liveness (R5). Returns a `AgentNotifierSweepResult` (findings + actions + `swept_at` +
backlog counts + duration).

### Conventions

Frozen dataclasses throughout (`AgentNotifierFinding`, `AgentNotifierActionResult`,
`AgentNotifierSweepResult`, `AgentNotifierContext`) matching the project's `McpRuntimeConfig`-style
convention. Private action helpers are prefixed `_` and take `ctx`/`finding`/`now` uniformly.

### Invariants And Boundaries

- **R3 is enforced by import discipline, not a runtime guard** — this module's imports are the
  contract; keep any new predicate reading a store directly, never the projection.
- **Level-triggered, not edge-triggered:** every predicate re-evaluates the CURRENT store state
  every sweep; a missed action on one sweep is simply re-found and re-acted-on the next.
- **Observation cadence is not delivery/escalation cadence:** short sweeps may observe every second,
  but redelivery and repeated owner signals are floor-gated at 900 seconds by durable row/cooldown
  state.
- **The timed escalation ladder was removed.** Current evaluation relays mechanical store facts; expectations remain owner-visible deadlines and are not evaluated as missed by the relay.
- **Delivery-failure rows exhaust redelivery, then resolve terminal `unresolved`.** A hosted-delivery
  failure (`"no-hosted-session"` or `"unconfirmed"`) below `PERSISTENT_FAILURE_ATTEMPTS` is still in
  the inbox redelivery domain; at the attempt ceiling `_redeliver` calls `_mark_unresolved`
  (N3, delivery evidence intact) instead of handing the row to a ladder.


- **Every action is logged, whether it "succeeds" or is skipped** (e.g. "no routable owner") —
  `_log_event` calls happen inside the action helpers themselves, not conditionally at the call
  site, except where an action short-circuits before attempting delivery (`"skipped"` results with
  no source id / no pending entry do not log, since nothing was attempted).
- **Pure functions over injected stores** — every predicate/action function is independently
  testable against fixture stores with no agent-notifier-loop scaffolding required (see
  `test_agent_notifier.py`).

### Todos

No known follow-up in this file itself. Two gaps documented in this leaf's builder report (not
follow-ups against THIS module, but scope boundaries this module's callers should know): rung 3's
developer surfacing rides the existing dashboard-visible `OperatorInboxStore` row
(`recipientRole="developer"`) rather than a dedicated attention-queue tile, since the 260628
developer-notification seam does not exist in this repo; and `orphan_policy.find_orphaned_workers`
is detection/surfacing only — no leaf yet auto-reparents an orphaned worker to a respawned manager.
Tracked HFX2-L11 gap: `_signal_emit` currently calls the new signal-cooldown store once per
pane/seat-liveness finding, and that store is an unbounded append-only full-file read with no
compactor yet. The precise limitation lives in `controlplane/agent_notifier_signals.py`'s sidecar.

## Evidence

### Docs References

No relevant external documentation found after checking the repo Domain Documentation for
agent-notifier-sweep-specific behavior; this is same-repository control-plane plumbing whose design
source is the pilot-observer log (P-15) and the leaf task doc, not an external spec.

### Repo-Internal References

- `_agent_notifier_loop`/`_agent_notifier_context` in `_app_lifespan.py` construct one `AgentNotifierContext` per sweep iteration (with the resolved last-good settings since 260713-TES-L4) and call `run_agent_notifier_sweep` via `asyncio.to_thread` on the settings-driven interval. [1]
- The pane classifier `evaluate_pane_findings` calls per running harness row. [2]
- The heartbeat store `run_agent_notifier_sweep` ticks unconditionally at the end of every sweep, and the staleness helpers built on top of it. [3]
- The expectation-row store is read only for the compaction pass — the relay never evaluates expectation rows (owner-visible deadline surface, 260713-TES-L5). [4]
- The operator inbox store is read and written directly through the landing/terminal/rebind/renew transitions (the ladder transitions are deleted, 260713-TES-L5). [5]
- The liveness check the rebind/dead-target and dead-upstream machinery reads (one-hop provenance; no ladder walk remains). [6]
- The current sweep does not own the retired missing-artifact/SLA predicates. [7]
- The owner-derivation helper `_signal_emit` calls before posting an owner-addressed inbox row. [8]
- The current injector entry point `_redeliver`/`_post_owner_signal` deliver through. [9]
- The signal cooldown store `_signal_emit` consults before minting repeated pane/seat-liveness inbox rows. [10]
- HFX2-L9 redelivery and signal behavior: `_redeliver` passes the redelivery floor, `_post_owner_signal` (moved to `serving/owner_signals.py` in 260713-TES-L2) returns delivery state, and `_signal_emit` skips mid-turn, checks cooldown, and appends a cooldown record. [11]
- The terminal catalog every pane/seat-liveness predicate reads directly (R3). [12]


### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary owns or consumes this local sweep; the level-triggered-reconciliation design rationale cites an external incident (Inngest, Oct 2025) only as research justification, not a code boundary.

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## 260731-EFA-L2 Current Delta

Two named concepts replaced repeated argument groups in the sweep:

- **`EscalationSchedule`** (`sla_seconds`, `rung_seconds`) — when an unacked row is due for its next
  ladder rung. The SLA (how long a kind of message may sit unacked) and the rung dwell (how long
  each rung waits before the next) are **one timetable**: raising the SLA without the dwell just
  moves where the same storm starts, and `rung_due` needs both for every row.
- **`OwnerSignal`** (`message_kind`, `ask`, `response`, `leaf_key`, `seat_role`,
  `subject_agent_id`) — one owner-addressed signal: what is being said, and about which seat. The
  message and its subject are inseparable here, because coalescing looks up an existing row by
  `(ask, kind, leaf, role)` and renewal rewrites the subject from the same value — a message
  carrying someone else's subject silently renews the wrong row.

The deterministic-sweep posture is unchanged: zero tokens, pure code, every predicate reading the
durable stores directly rather than the projection.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L16 Current Delta

`ctx.catalog.list(include_terminated=True)` is now fetched BEFORE `reconcile_and_compact`, outside
the operator-inbox lock, and the reconcile closure consumes the pre-fetched `catalog_entries`. The
lock-held fold→resolve→compact transaction is unchanged — consume authority and the declared
260731-EFA-L5 exception stand — and the tmux snapshot is still taken fresh inside the callback,
bounded by its 5-second timeout and fail-closed.

The accepted staleness is one-directional and benign: `terminated` is monotone in the catalog, so a
subject that terminates after the pre-fetch reads as non-terminated and is KEPT this sweep — never
a false resolve; absence in the snapshot is never proof of gone; and the agent-notifier is
level-triggered, so a kept row is simply re-judged on the next sweep.

Provenance: the previous shape — a catalog read inside the lock-held reconcile — was the mirror
image of the liveness sweep's nesting (the catalog batch lock held across the synchronizer's
inbox/gate acquisitions), and the ABBA deadlocked the serving daemon twice on 2026-08-05. No
thread may now hold one store's lock while acquiring another's (`durable_store.exclusive_access`:
ONE ORDER ACROSS STORES, TOO); forcing regressions live in `mcp/tests/test_cross_store_lock_order.py`.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260821-CLIVE Registration Before Reclamation

Each sweep snapshots the inbox, asks the injected task-plane registrar to durably register eligible
leaf execution reports, and supplies the exact registered ids to `reconcile_and_compact`. This
occurs before any TTL/cap or confirmed-gone reclamation. With no registrar the set is empty, so
task-bound execution rows remain protected rather than being guessed safe to delete.
