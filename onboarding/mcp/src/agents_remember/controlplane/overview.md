# mcp/src/agents_remember/controlplane

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| sourceRoute            | `mcp/src/agents_remember/controlplane`         |
| doc_type               | `route-local-overview`                         |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`     |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `../../../overview.md`                         |

## Purpose

`controlplane/` owns control-plane records: the gate control plane (task 6), the
operator/agent inbox (task 10/L3), orchestration artifact/nudge helpers (L3), the
task-23/24 interaction-retention policy, task-28 lifecycle-scoped attention
acknowledgements, and — since 260707-HFX2-L1 — the durable expectation-row
substrate (R2), inbox redelivery backoff math (R3), and hierarchical signal
routing derivation (R4) the L2 supervisor sweep drives from. **260707-HFX2-L4** adds the P-15
tier-3 escalation ladder ON TOP of that L1 substrate: `escalation_ladder.py` (the pure rung walker —
`rung_due`/`next_step`/`seat_is_suspect`) and `orphan_policy.py` (a detection-only hook for a dead
manager's live workers). **260707-HFX2-L13 round 2** makes leaf-signal address-time routing
manager-first (live direct manager, then exact leaf/master scope, else role-only manager), while a
separate historical provenance walk remains reserved for later ladder skip-level traversal. Later
rungs require the configured dwell plus a hard five-minute floor anchored by both `escalatedAt` and
`rungTransitionAt`; rows also preserve `leafKey`/`subjectAgentId` for chain-aware supervisor checks.
The L2 supervisor sweep (`serving/supervisor.py`, governed by the
`serving/` overview) is the sole caller of all of this — no ladder logic lives outside this route,
and no delivery/store-write happens inside it. Gates are attributed decision points on a lifecycle — the kind vocabulary
includes the delegable `master-handover-approval` seam gate (the manager raises it with the
reviewer verdict attached; the orchestrator decides per the gate delegation policy, and
`requireReviewerVerdictAtSeams` binds delegated seam decisions to that evidence); the inbox
is the pull-based return channel for chats the dashboard does not host and the
durable substrate for agent-to-agent messages that may also be pushed into
hosted sessions; nudge rows record rate-limited manager nudges. Attention
acknowledgement rows hide one current queue occurrence. Lifecycle-bound acknowledgements disappear with their
lifecycle; Task 29 S7 keeps only targetless actionable-drift acknowledgements current
across that prune boundary because their source item is repository/branch-scoped rather
than lifecycle-scoped. These rows are throwaway interaction data, not durable task records.

## Hot Path Summary

260707-HFX2-L17 carries `seatRole` beside `leafKey` through expectation rows, operator inbox rows,
renewal, supervisor cooldown records, and routing. Current manager/architect/worker discovery and
chain credit use binding identity; only the escalation ladder's historical parent hop reads
`spawnRole`. Same-text supervisor conditions on one leaf coalesce only within the same role, so
parallel seats remain independently observable and addressable.

260707-HFX2-L15 closes the active-phase unbound-worker gap without reviving same-cwd inference.
Leaf-chain progress credits an unbound worker/reviewer/curator only when the current manager spawned
it and its catalog row explicitly names `replacementForLeaf == leafKey`; parallel-leaf activity
under the same manager remains isolated.

260707-HFX2-L13 makes leaf completion and liveness routing current-manager-first, records durable
leaf/subject provenance, separates address-time routing from historical skip-level walking, and
enforces a redundant five-minute later-rung floor. Chain progress currently credits exact-leaf seats,
the current manager, and same-worktree unbound reviewer/curator seats; unbound-worker active-phase
credit remains the accepted HFX2-L14 S7 follow-up.

A gate is publicly opened for agent workflow through `lifecycle_gate` (blocking by default; raise-and-continue exists for policy-delegated seam kinds, with `GateStore.find` giving deciders cross-lifecycle resolution by gate id), which
creates the `GateRecord`, blocks the ambient lifecycle with the ask, and
keeps the public tool call waiting until the gate is decided or a gate-specific inbox response exists.
Decisions (`gate_decide`) and listing
(`gate_list`) remain public control-plane tools; lower-level create/wait builders
are compatibility internals in `mcp/tools/gates.py`. The builders append
`GateRecord` snapshots to `GateStore`. Lifecycle-scoped gate creation expires any
previous open gate before opening the new one, so each lifecycle has one current
actionable gate. L4 adds policy-governed delegated approvals: default policy is
all-human; non-human orchestration decisions are valid only for explicitly
delegated gate kinds, never for human-pinned integration/push/cleanup gates, and
never by the owning lifecycle itself. Gate records can attach reviewer-verdict
evidence refs, and policies may require that evidence before a delegated decision
binds. Task 23/24 adds the retention boundary: cancel,
non-enforcement wait pickup, dismiss, clear, consume, and the 24-hour TTL physically delete throwaway
interaction rows. Start at `records.py` for the
entity, then `store.py` for the append-only log (co-located with the observer
event log under `observer_root`). `gate_policy.py` owns the validated
delegation schema and attribution checks. `enforcement.py`'s `evaluate_gate` is
the pure kind-generic policy resolver; `evaluate_closeout_gate` remains the
closeout wrapper `worktree_closeout_apply` obeys.

Operator/agent messages are queued with `OperatorInboxEntry` snapshots and
stored through `OperatorInboxStore`. The inbox log lives under
`observer_root/workspace/operator-inbox.jsonl`; entries carry `lifecycleId`
and/or `agentId` and/or `recipientRole`, preserve sender/recipient role metadata,
message kind, optional artifact path, originating ask, response, and hosted
delivery state while pending, and are deleted when the agent consumes them, the
developer dismisses the stale pickup warning, or TTL compaction removes them.
L3 adds `orchestration_nudges.py` for rate-limited manager nudges and
`orchestration_artifacts.py` for turn-report, master-handover, and escalation
packet helpers. Since 260703-L12 both role vocabularies carry the `strategist`
seat, and HFX-L6 extends the orchestration artifact role vocabulary with
`architect` and `curator` so turn reports, handover packets, and escalation packets can name the
split developer-facing/default seat and the curator closeout seat. `AgentRole` remains the inbox
addressing vocabulary; `OrchestrationRole` owns escalation packet roles and the ladder rung
`strategist -> orchestrator`. **260707-HFX-L7** adds the `system-specialist` investigate-first
provider-degradation seat to both vocabularies: `AgentRole` gains `system-specialist` so the
degradation detector (`providers/degradation.py`, governed by the `mcp/` package overview) can
address it on the inbox, `InboxMessageKind` gains `degradation-alert` for the detector's
role-addressed state-change alerts (posted to `orchestrator` and every active `manager`), and
`OrchestrationRole`/`_ROLE_ESCALATION` in `orchestration_artifacts.py` gain
`system-specialist -> orchestrator` so the seat's escalations/blockers route correctly.
**260707-HFX-L12** closes a master-exit BLOCK finding: `AgentRole` gains `architect` and `curator`,
and `InboxMessageKind` gains `decision-item`/`decision-ruling`, so the HFX-L6-landed decision-item
relay doctrine (orchestrator posts `decision-item` to `architect`; architect posts
`decision-ruling` back) is now representable and round-trippable through the inbox, not just
documented in `architect.md`/`orchestrator.md`/`SKILL.md`. Gate policy and inbox storage behavior
are unchanged — a pure Literal extension.

**260707-HFX2-L1** makes the operator inbox the signal substrate the L2 supervisor sweep drives:
R1 extends `OperatorInboxEntry` with ack/backoff fields (`attemptCount`/`lastAttemptAt`/
`nextAttemptAt`/`escalatedAt`) so delivered is not acknowledgement. HFX3 supersedes L1's
immortal-pending retention: pending rows expire after 48 hours, the folded inbox is capped at 500
current ids, and the durable artifact—not the row—is the record. R2 adds `expectation_rows.py`
(`ExpectationRowStore`/`write_expectation_row`): every dispatch surface (spawn, gate open, signal
post) atomically writes a durable what-must-happen-by-when row (kinds `briefed-by` /
`turn-report-by` / `verdict-by` / `ack-by`), configurable per-kind SLA via
`orchestration.expectations` in `kernel/agentic_settings.py`. R3 adds `inbox_backoff.py`: pure
backoff-ladder math + a per-target rate-limit gate mirroring `OrchestrationNudgeStore`'s pattern,
consumed by `OperatorInboxStore.list_redeliverable`/`record_delivery`. R4 adds
`signal_routing.py::derive_signal_owner`: the routed owner address (worker -> its manager, manager
-> its orchestrator, decision-item -> architect) derived from catalog spawn provenance, stamped
onto new `OperatorInboxEntry.ownerRole`/`ownerAgentId`/`ownerLifecycleId` fields at post time.
Neither this leaf's redelivery driver nor its ladder escalation exist here — L2 (a sibling leaf)
drives the actual sweep; this route only builds the durable substrate + surfacing it reads.
**260707-HFX2-L4** lands that ladder escalation: `escalation_ladder.py::rung_due`/`next_step` climb
an unacked row rung 1 (renudge) -> rung 2 (skip-level, via new `signal_routing.
derive_skip_level_owner` -- a SEPARATE two-hop walk from L1's one-hop `derive_signal_owner`, walking
PAST any dead intermediate the new `is_seat_dead` helper detects) -> rung 3 (architect custody /
architect attention, terminal); `seat_is_suspect` marks a seat past the respawn threshold as suspect only on an actually
observed dead/stalled catalog signal, never from silence alone. `orphan_policy.py::
find_orphaned_workers` is a pure, detection-only hook for a respawned/dead manager's still-running
workers -- no auto re-parent action exists yet. `OperatorInboxEntry` gains `rung: int = 0` and
`OperatorInboxStore` gains `advance_rung` (stamps the next rung AND re-anchors `escalatedAt` in one
snapshot, distinct from L2's rung-agnostic `mark_escalated`). All of this is pure/derivation-only in
this route; the actual predicate evaluation, delivery, and durable-row mutation happen in
`serving/supervisor.py`, this route's sole caller.
**260707-HFX2-L8** closes the dead-seat storm gap on that substrate: `OperatorInboxEntry` gains the
durable terminal `state="ladder-resolved"` plus `ladderResolvedAt`/`ladderResolvedReason`; `inbox_backoff.py`
excludes ladder-resolved rows via an explicit predicate; `OperatorInboxStore` mutations accept an
optional in-sweep `current()` snapshot and add idempotent `mark_ladder_resolved`; and
`interaction_retention.py`/`compact()` prune ladder-resolved terminal rows. Mid-climb rows and
live-seat rows remain pending/redeliverable only within the HFX3 48-hour TTL and 500-row health cap.
**260707-HFX2-L9** adds the redelivery-cadence floor and supervisor signal cooldown substrate:
`inbox_backoff.py` now owns the 900-second `MIN_REDELIVERY_INTERVAL_SECONDS` and refuses sub-floor
values, `OperatorInboxStore.record_delivery` threads that floor into stored `nextAttemptAt`
scheduling, and new `supervisor_signals.py` stores pane/seat-liveness signal cooldown records keyed
by owner/leaf/finding kind/detail. Known deferral: `supervisor_signals.py` is currently an unbounded
append-only log with no compactor and performs full-file reads through `in_cooldown`; HFX2-L11 tracks
that CS-6-class scaling gap before the supervisor is re-enabled.

Attention dismissals use `AttentionDismissalStore` under
`observer_root/workspace/attention-dismissals.jsonl`, but unlike gates the file is a compact current
set rather than history. Dismissing a lifecycle-bound attention row upserts one acknowledgement; each
projection tick prunes acknowledgements whose lifecycle is no longer live. Gate-open attention rows are
consumed by cancelling/deleting the gate source itself. Targetless actionable-drift dismissals are the
only repository-scoped exception: they stay as current acknowledgements until superseded by a newer drift
signal, while targetless provider-down dismissals are not accepted.

## Layout

| Module        | Owns                                                                          |
| ------------- | ----------------------------------------------------------------------------- |
| `records.py`  | `GateRecord` (`ar-gate-record/v1`) + pure `create_gate` / `decide_gate` / `expire_gate` / `coerce_gate_kind`; the `GateKind` / `GateState` / `DecidedVia` Literals, `GateEvidenceRef`, and `DECISION_STATES`. `GateKind` is the full l-01 gate spine (slice 09 added `plan-approval` / `worktree-intent` / `push-approval`); `closeout-approval` IS the commit gate — no separate `commit-approval`. |
| `store.py`    | `GateStore`: lifecycle/workspace gate logs beside the event log; `current()` folds by gate id (last-wins), while `delete`/`compact` physically remove throwaway interaction rows. |
| `operator_inbox_records.py` | `OperatorInboxEntry` (`ar-operator-inbox-entry/v1`) + pure create/consume helpers for durable operator/agent inbox snapshots, including role/message/artifact and delivery metadata. |
| `operator_inbox_store.py` | `OperatorInboxStore`: workspace inbox log, pending filters by lifecycle/agent/recipient role, delivery-state snapshots, idempotent store consume, public delete/dismiss paths, and TTL compaction. |
| `orchestration_artifacts.py` | Strict turn-report, master-handover, and escalation packet helpers for the L2/L3 orchestration frame, with HFX-L6 architect/curator role literals in the artifact vocabulary. |
| `orchestration_nudges.py` | `OrchestrationNudgeRecord` + `OrchestrationNudgeStore`: append-only, rate-limited manager nudge attempts plus message/artifact helpers. |
| `gate_policy.py` | `GatePolicy` / `GatePolicyRule`, built-in policy names, human-pinned/delegable kind validation, and delegated-decision attribution/evidence checks. |
| `enforcement.py` | `evaluate_gate` (pure kind-generic gate policy resolver) + `GateGuard`; `evaluate_closeout_gate` / `CloseoutGuard` remain the closeout wrapper `worktree_closeout_apply` reads. |
| `attention_dismissals.py` | `AttentionDismissalRecord` + `AttentionDismissalStore`: compact current acknowledgement rows for attention queue dismissals, with physical prune by live lifecycle id and a targetless actionable-drift exception. |
| `interaction_retention.py` | Shared 5-minute pickup/wait, 24-hour consumed-row audit TTL, HFX3 48-hour pending-row TTL, and 500-current-row hard health cap; ladder-resolved rows drop immediately. |
| `expectation_rows.py` | (260707-HFX2-L1, R2) `ExpectationRow`/`ExpectationRowStore`/`write_expectation_row`: durable what-must-happen-by-when rows written atomically at every dispatch surface, an L2 sweep scans, never in-memory timers. |
| `inbox_backoff.py` | (260707-HFX2-L1, R3; HFX2-L9) Pure redelivery backoff-ladder math + the shared 900-second redelivery floor/fail-loud validation, mirroring the `OrchestrationNudgeStore` pattern while refusing sub-floor retry cadences. |
| `supervisor_signals.py` | (260707-HFX2-L9) Persisted supervisor pane/seat-liveness signal cooldown records keyed by owner/leaf/finding kind/detail; known unbounded/no-compactor limitation tracked for HFX2-L11. |
| `signal_routing.py` | (260707-HFX2-L1, R4; 260707-HFX2-L4, R2/R4) `derive_signal_owner`: one-hop hierarchical routing derivation from catalog spawn provenance (worker -> manager, manager -> orchestrator, decision-item -> architect). `is_seat_dead`/`derive_skip_level_owner`: the ladder's liveness check and SEPARATE two-hop, dead-node-skipping owner's-owner walk. |
| `escalation_ladder.py` | (260707-HFX2-L4 + L13/HFX3 correction) `rung_due`/`next_step`/`seat_is_suspect`: the pure tier-3 ladder walker, configured dwell plus redundant five-minute later-rung floor, architect terminal custody, and dead/stalled-seat respawn-candidate detection. |
| `orphan_policy.py` | (260707-HFX2-L4, R3) `find_orphaned_workers`: a pure catalog read for a dead/respawned manager's still-running worker seats -- detection/surfacing only, no re-parent action. |
| `__init__.py` | Package export surface (gate records/store/enforcement + operator inbox records/store). |

The `gate_*` MCP tools live in `mcp/tools/gates.py` (config-rooted, building a
`GateStore(observer_root(config))`); their response models are `models/gates.py`.
The `operator_inbox_*` MCP tools live in `mcp/tools/operator_inbox.py`; their
response models are `models/operator_inbox.py`.

## Invariants And Boundaries

- **Records + a pure policy, not the mutation.** Creating/deciding a gate writes
  durable history (`records.py`/`store.py`); `gate_policy.py` validates which
  roles can decide which gate kinds; `enforcement.py` decides whether an
  approved gate permits the guarded operation — but the *mutation* (refusing the
  closeout, marking the gate `applied`) lives in the worktree tool
  (`worktrees/modules/closeout.py`), which imports the I/O-free policy.
- **Interaction records are disposable.** Gate/inbox rows remain modeled records while pending, and
  lifecycle-bound attention acknowledgement rows remain only while their lifecycle is live; targetless
  actionable-drift acknowledgement rows are current repo/branch records, not history. Response, cancel,
  dismiss, clear, consume, lifecycle prune, and TTL cleanup physically delete them. Durable task docs, contracts,
  commits, and ledgers carry lifecycle history.
- **Single current lifecycle gate.** A lifecycle may have only one open durable gate; creating a new
  lifecycle-scoped gate appends an `expired` snapshot for older open gates rather than deleting them.
- **Honest attribution → enforceable.** `decidedBy` (actor/session/lifecycle),
  `decidedVia` (chat/dashboard/cli/orchestration), and `decidingRole` are
  separate. MCP self-decisions stay model/cli and non-binding; delegated
  orchestration decisions name a distinct deciding lifecycle/session and must
  satisfy the configured `GatePolicy` before they are appended or consumed.
- Gates co-locate under `observer_root`, mirroring the event substrate; no new
  storage root.
- **Cross-lifecycle seam fold.** A seam gate lives on its raiser's lifecycle (the
  manager raises `master-handover-approval` with `enclosure=<master task name>`),
  while its consumer — the orchestrator's master → super integrate — anchors a
  different lifecycle. Identity-addressed consumers therefore read
  `GateStore.all_current()` (the whole-workspace last-wins fold) and match by
  `enclosure`, never by the consuming contract's lifecycle id.
- Inbox entries require `lifecycleId`, `agentId`, or `recipientRole`; an
  unaddressed response has no external mailbox or hosted-session target.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Gates mirror the observer event substrate (envelope + append-only JSONL store). | [observer/store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| Gate policy validation and delegated decision checks. | [gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |
| The `gate_*` payload builders that drive this substrate. | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| Gate response models. | [models/gates.py](agents-remember/mcp/src/agents_remember/models/gates.py) |
| The inbox record/store pair provides the external-chat pull return channel. | [operator_inbox_records.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_records.py) and [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| The attention acknowledgement store keeps current lifecycle-scoped queue dismissals only. | [attention_dismissals.py](agents-remember/mcp/src/agents_remember/controlplane/attention_dismissals.py) |
| The provider degradation detector posting `degradation-alert` inbox rows addressed to `system-specialist`'s ladder peers (260707-HFX-L7); governed by the `mcp/` package overview. | [providers/degradation.py](agents-remember/mcp/src/agents_remember/providers/degradation.py) |
| The sole caller of the ladder + orphan-detection modules: evaluates the escalation/dead-upstream/ladder-terminal predicates, performs delivery, and stamps the durable `advance_rung`/retire/ladder-resolved transitions. | `evaluate_escalation_findings`; `_escalate_rung`; `_respawn_suspect`; `_resolve_ladder_terminal` | [../serving/supervisor.py](agents-remember/mcp/src/agents_remember/serving/supervisor.py) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 control-plane route impact: made rows, renewal,
  cooldowns, current discovery, chain credit, and coalescing pair-aware while retaining the one
  historical spawn-provenance ladder walk. Verification metadata remains pinned until closeout.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 control-plane route impact: replaced same-cwd unbound
  seat credit with explicit replacement-leaf plus same-manager provenance and covered the
  parallel-leaf negative. Verification metadata remains pinned until closeout stamps the eventual
  L15 code commit.

- 2026-07-10T02:39+02:00 — HFX3 retro curation: reconciled route truth with the health-first
  48-hour pending TTL and 500-row cap, architect terminal custody, and the L13 redundant
  five-minute later-rung floor. Historical HFX2-L1 immortal-pending entries remain as superseded
  history only. Verification metadata remains pinned until closeout stamps the eventual two-parent
  code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round-2 route impact: documented current-manager-first
  leaf signals, historical-only skip-level provenance, leaf/subject row fields, redundant rung
  anchors, and the accepted unbound-worker S1 follow-up. Verification metadata remains pinned until
  closeout stamps the eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: reviewed route impact for the CS-6 store/projection/process scaling sweep and updated the route summary for changed files. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9 route impact: added the shared 900-second redelivery
  floor/fail-loud validation in `inbox_backoff.py`, threaded the floor through
  `OperatorInboxStore.record_delivery`, and added `supervisor_signals.py` as the persisted
  owner-signal cooldown store. The new store's unbounded/no-compactor scaling gap is documented as
  a tracked HFX2-L11 deferral, not treated as already bounded. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 route impact (dead-seat storm, R1-R3): operator inbox rows
  gain the terminal non-ack `ladder-resolved` state and resolution metadata; `inbox_backoff.py`
  excludes it explicitly; store mutations accept an optional in-sweep current snapshot; the store adds
  idempotent `mark_ladder_resolved`; and compaction prunes ladder-resolved terminal rows while still
  preserving pending/unacked live rows. Verification metadata pinned until closeout stamps the
  260707-HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 route impact: two new modules — `escalation_ladder.py`
  (the pure P-15 tier-3 rung walker) and `orphan_policy.py` (detection-only orphan-worker hook) —
  plus R2/R4 extensions to `signal_routing.py` (`is_seat_dead`, `derive_skip_level_owner` — a
  SEPARATE two-hop, dead-node-skipping walk, L1's one-hop `derive_signal_owner` unchanged) and R1/R2
  extensions to `operator_inbox_records.py`/`operator_inbox_store.py` (`rung` field,
  `advance_rung` transition). `serving/supervisor.py` (a sibling route) is the sole caller; no
  ladder logic, delivery, or store mutation lives outside this route's pure derivation/hook
  functions. Verification metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T14:40+02:00 — 260707-HFX2-L1 route impact: three new modules —
  `expectation_rows.py` (R2 durable deadline rows), `inbox_backoff.py` (R3 redelivery backoff +
  rate limiting), `signal_routing.py` (R4 hierarchical routing derivation) — plus R1 ack-semantics
  extensions to `OperatorInboxEntry`/`OperatorInboxStore`/`interaction_retention.py` making
  consume=ack the only terminal delivery outcome and compaction never remove a pending/unacked
  row. Gate/inbox record shapes otherwise unchanged. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L1 commit.
- 2026-07-08T04:15+02:00 — 260707-HFX-L12 route impact (small, master-exit BLOCK fix leaf):
  `AgentRole` gains `architect`/`curator` and `InboxMessageKind` gains
  `decision-item`/`decision-ruling` (`operator_inbox_records.py`) so the HFX-L6-landed
  decision-item/decision-ruling relay doctrine is representable and round-trippable through the
  inbox, closing master-exit Finding 1
  (`notes/reports/260707-HFX-master-exit-verdict.md`); pinned by
  `test_decision_item_relay_round_trip_between_orchestrator_and_architect` in
  `mcp/tests/test_operator_inbox.py`. Gate policy and inbox storage behavior are unchanged.
  Verification metadata pinned until closeout stamps the HFX-L12 commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 route impact (small): `AgentRole` gains
  `system-specialist` and `InboxMessageKind` gains `degradation-alert`
  (`operator_inbox_records.py`); `OrchestrationRole`/`_ROLE_ESCALATION` gain
  `system-specialist -> orchestrator` (`orchestration_artifacts.py`, R2 fix round closing
  reviewer F5) so the new provider-degradation investigator seat is addressable and
  ladder-routable; pinned by `test_system_specialist_escalates_to_orchestrator` in
  `test_orchestration_comms.py`. Gate policy and inbox storage behavior are unchanged.
  Verification metadata pinned until closeout stamps the HFX-L7 commit.
- 2026-07-07T23:55+02:00 — 260707-HFX-L6 route impact: orchestration artifacts can
  now name `architect` and `curator` alongside the existing orchestration roles in turn-report,
  handover, and escalation packet payloads; gate policy and inbox storage behavior are unchanged.
  Verification metadata pinned until closeout stamps the HFX-L6 commit.
- 2026-07-06T15:40+02:00 — 260703-L12 route impact (small): the `strategist` role joins `AgentRole` (`operator_inbox_records.py`) and `OrchestrationRole` + `_ROLE_ESCALATION` (`orchestration_artifacts.py`, escalating to the orchestrator) so the new spawn-first portfolio seat is addressable and ladder-routable; pinned by a new test in `test_orchestration_comms.py`. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T19:25+02:00 — 260703-L8 route impact (cycle 6, owner follow-up): the cross-lifecycle seam fold added as an invariant bullet (`all_current()` + enclosure addressing) and the Layout table de-duplicated (the older `enforcement.py`/`operator_inbox_records.py`/`operator_inbox_store.py` rows removed; the newer kind-generic + role/delivery-metadata descriptions kept). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 — 260703-L8 route impact (cycle 6, small): `GateStore.all_current()` folds every gate log (workspace + all lifecycles, last-wins per gate id) — the cross-lifecycle fold the integrate-side seam guard reads so an enclosure-addressed handover gate is visible from a different consuming lifecycle. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:24+02:00 — 260703-L8 route impact (cycle 5, small): `GateStore.find` resolves a gate id across the workspace and every lifecycle log — the packet-carried-id decide path. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:32+02:00 — 260703-L8 route impact (small): GateKind gains `master-handover-approval` (delegable master-exit seam gate; the named policy routes it to the orchestrator) and gate_policy gains SEAM_GATE_KINDS + `apply_seam_verdict_requirement` — the requireReviewerVerdictAtSeams wiring. Enforcement paths otherwise unchanged. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:32+02:00 — No route impact: orchestration_artifacts `template_path` root renamed with the unified skill folder (`l-01-agent-lifecycles`); resolution logic and the route model are unchanged (260703-L9).
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: added the
  `gate_policy.py` schema/validator, generalized enforcement to a kind-generic
  resolver, and documented delegated orchestration attribution plus reviewer
  evidence refs. Human-pinned integration/push/cleanup gates remain
  non-delegable. Verification metadata pinned until closeout stamps the L4
  commit.
- 2026-07-04T12:31+02:00 - L3 route impact: the inbox is now generalized for
  agent-to-agent addressing with role/message/artifact/delivery metadata, and
  the route adds orchestration artifact and rate-limited nudge helpers.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: attention dismissals now document the targetless
  actionable-drift exception, preserving only current repo/branch drift acknowledgements while
  lifecycle-bound rows continue to prune with live lifecycle ids. Verification metadata pinned until
  closeout stamps the task-29 code commit.
- 2026-06-28T03:05+02:00 — Task 28 S5.2: added `attention_dismissals.py` as compact lifecycle-scoped attention acknowledgement state; projection pruning removes rows for non-live lifecycles and gate-open items are consumed by gate cancellation/deletion. Verification metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-26T18:43+02:00 — Regression fix: route now records that public
  `lifecycle_gate` waits without an exposed timeout and ignores stale
  lifecycle-scoped inbox rows that are not tied to the newly opened gate.
- 2026-06-26T17:05+02:00 — Regression fix: route now records that
  `lifecycle_gate` performs the bounded gate/inbox wait itself after creating
  the gate and blocking the lifecycle; it is no longer described as wait-state
  initialization only.
- 2026-06-26T14:16+02:00 — Task 25: route overview now describes `lifecycle_gate` as the public gate-opening workflow and classifies lower-level create/wait builders as compatibility internals.
- 2026-06-25T13:20+02:00 — Task 23/24: added interaction-retention policy to the route and changed gate/inbox framing from permanent logs to disposable interaction rows with delete/TTL cleanup paths.
- 2026-06-25T07:26+02:00 — Task 19: gates now include the `expired` state/helper for replacing older
  open lifecycle gates, and the route exposes the `gate_response_wait` wait-plus-inbox helper while
  keeping decisions and messages separate. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: added `operator_inbox_records.py` and `operator_inbox_store.py` to the route, documenting the external-chat pull channel as a control-plane sibling to gates. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption, S2): `records.py`'s `GateKind` Literal gained `plan-approval`, `worktree-intent`, and `push-approval` — the full l-01 gate spine; refreshed the `records.py` Layout row (and noted `closeout-approval` IS the commit gate, no separate `commit-approval`). The route's record-vs-policy split and store/enforcement modules are unchanged. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: the route gained enforcement — `enforcement.py` (`evaluate_closeout_gate` + `CloseoutGuard`), the pure closeout-gate policy `worktree_closeout_apply` obeys. Revised the "record, not enforcement" framing: the *policy* is here (I/O-free), the *mutation* stays in the worktree tool. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the gate control-plane substrate route (`records.py` + `store.py` + facade). Verification metadata pinned until closeout stamps the 6a code commit.
