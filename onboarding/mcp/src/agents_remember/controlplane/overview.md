# mcp/src/agents_remember/controlplane

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| sourceRoute            | `mcp/src/agents_remember/controlplane`         |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

`controlplane/` owns control-plane records: the gate control plane (task 6), the
operator/agent inbox (task 10/L3), orchestration artifact/nudge helpers (L3), the
task-23/24 interaction-retention policy, task-28 lifecycle-scoped attention
acknowledgements, and — since 260707-HFX2-L1 — the durable expectation-row
substrate (R2), inbox redelivery backoff math (R3), and hierarchical signal
routing derivation (R4) the L2 agent-notifier sweep drives from. **260707-HFX2-L4** adds the P-15
tier-3 escalation ladder ON TOP of that L1 substrate: `escalation_ladder.py` (the pure rung walker —
`rung_due`/`next_step`/`seat_is_suspect`) and `orphan_policy.py` (a detection-only hook for a dead
manager's live workers). **260707-HFX2-L13 round 2** makes leaf-signal address-time routing
manager-first (live direct manager, then exact leaf/master scope, else role-only manager), while a
separate historical provenance walk remains reserved for later ladder skip-level traversal. Later
rungs require the configured dwell plus a hard five-minute floor anchored by both `escalatedAt` and
 `rungTransitionAt`; rows also preserve `leafKey`/`subjectAgentId` for chain-aware agent-notifier checks.
The L2 agent-notifier sweep (`serving/agent_notifier.py`, governed by the
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

Start at `durable_store.py` for guarded JSONL writes, record validation and advisory ownership; `records.py`/`store.py` own gates and `operator_inbox_records.py`/`operator_inbox_store.py` own inbox rows. Lock admission authorizes the checkout target before entering `kernel.file_lock`; atomic replacement uses `kernel.atomic_write`. A host registry uses its own policy over the shared kernel lock, so coordinator isolation remains intact. Signal routing and expectation rows feed the serving-owned notifier; retention never changes authority-read strictness.

## Durable Store And Routing Operating Context

L23 extends the validated store seam for batched operator-inbox transitions used by notifier
expiry. Batch preparation resolves canonical task/owner addresses first and fails closed when a
row is missing, mismatched, or structurally unaddressable; it never guesses a replacement runtime
identity. The same durable-store containment and model-validation rules apply to these rewrites.

**260731-EFA-L21 — target containment precedes filesystem effects.** The shared durable-store lock,
append, and rewrite primitives ask the kernel checkout policy to authorize the target before
creating a parent directory, lock file, temporary file, or durable row. In undeclared linked
worktree mode permits the deterministic `provider-runtime/dev-ar-coordination` subtree for coordinator rows and enclosure `reports/` for operational artifacts; trusted MCP/dashboard/lifecycle-operation and explicit test execution follow their declared policy.

TES-L6 keeps owner routing sprint-local. `signal_routing.py` resolves architect custody and rebind
chains inside the row's exact repository+sprint identity, while `seats.py` names command roles
without constraining the notifier's structurally discovered subordinate roles.

**260731-EFA-L5 — the durable-store contract. Read this before changing how any store in this route
touches disk.** The six JSONL stores here (`store.py`, `expectation_rows.py`,
`operator_inbox_store.py`, `attention_dismissals.py`, `orchestration_nudges.py`,
`agent_notifier_signals.py`) were written independently against the same shape, and their safety
properties ended up distributed almost at random: one of six took a lock, three of six used a
pid-scoped temp name, none fsynced. **No base-commit measurement artifact is committed anywhere in
this tree**, so every base-commit rate below is checkable only as "the source says so": the harness
can be re-pointed at a `git archive` of `e52edaf5` (`mcp/tests/_store_durability.py`), but no run
output is stored and no test asserts a rate. Two figures are carried at several independent sites
and are quoted here on that authority: attention-dismissals lost **31.45 percent** of appended
records (`durable_store.py`, `agent_notifier_signals.py`, `test_durable_store_contract.py`,
`test_observer_projection.py`) and gate **11.50 percent** (`durable_store.py`, `store.py`,
`test_interaction_retention.py`). The historical `durable_store.py` module docstring reported the rest at that one
site — and those retained historical claims are not present in the shortened current contract docstring:
supervisor-signals 10.50 percent, expectation-rows 10.20 percent, orchestration-nudges 9.20 percent,
operator-inbox 0.00 percent (the one that already held a lock), 127 of 2000
`AttentionDismissalStore.dismiss` calls raising, and ten runs per store. That historical docstring was also the
only recorded authority for records disappearing whole rather than torn — the property that would explain why
no reader-side validation could have caught this while the caller was told the write succeeded.

**Against the current tree the checkable claim is narrower than "all six stores, all scenarios",**
and it lives in `mcp/tests/test_controlplane_store_durability.py::MultiProcessDurabilityTests`.
`lost == 0` is asserted in all three scenarios, but over six stores in `forced_lost_update` and
`stress` and over **five** in `forced_unlink`: attention-dismissals is excluded there by
construction, because it has no `append` at all (its `dismiss` is a whole-file read-modify-write),
which is exactly why it measured worst. `torn_lines == 0`, `append_error_count == 0` and
`reclaim_error_count == 0` are asserted in the **`stress` scenario only**, over all six stores. The
one base-commit figure a reader can check is not a rate: `HarnessSensitivityTests` asserts, against a
`git archive` of `e52edaf5`, that each of the five unlocked stores loses its single record in
`forced_lost_update` while operator-inbox loses none.

All six implement the declared `ar-durable-store/1.0` contract in `durable_store.py`. Guarded log access and single/batched append remain there; mechanical exclusion has one owner in `kernel.file_lock` and temporary-file publication has one owner in `kernel.atomic_write`. The earlier count of raw file operations describes the original consolidation, not the current owner map.

**The lock is the mechanism; ownership is advisory.** Every append and every rewrite of every one
of the six logs takes that log's lock, in every process, whether or not that process declared
anything. There is no flag that turns it off and no store exempt from it; the `serialized` opt-out
an earlier draft carried was deleted. Ownership is expressed two ways, neither of them a durability
guarantee: `StoreOwnership.check_declared_writer` raises but only inside a process that called
`declare_process_role` (MCP, dashboard and the detached lifecycle-operation writer), and
`is_compaction_owner` is a question that never raises. Where ownership does real work it does it
structurally, by moving code rather than by checking at runtime. `require_lock_held` is the one
check that raises unconditionally, from inside `rewrite_lines`, so no store can rewrite a log it
has not locked however the call was reached — it can afford to, because it asks about the calling
thread's own lock rather than about a process-wide declaration.

**Single-writer is a deployment fact, not a structural one.** An earlier draft left the two
single-writer stores (attention-dismissals, supervisor-signals) unlocked on the strength of being
single-writer, and the sources put 31.45 percent loss on attention-dismissals doing exactly
that. `AttentionDismissalStore.dismiss` is a whole-file read-modify-write reached from the
dashboard HTTP dismiss route through the serving route, so two concurrent dismisses lose each other
with no compactor involved and no second writer required. The store that looked safest was the
worst.

**Compaction owners.** Gate is the MCP process's, moved off the dashboard's 30-second projection
tick onto `mcp/tools/gates.py`. Expectation rows, attention dismissals, orchestration nudges and
agent-notifier signals are the dashboard's. Operator inbox has **none** — the leaf's declared
exception, because both processes must physically remove rows (MCP deletes a cancelled gate's rows,
the dashboard resolves and compacts under one held lock) and neither move travels without the
decision it implements.

**`rewrite_lines` never unlinks.** An empty kept set is an empty file. Previously a `_replace` that
found the kept set empty called `unlink`, so a concurrent appender holding an `"a"`-mode handle
wrote into an unlinked inode.

**Two read policies, deliberately, and not an inconsistency.** Enforcement fails loudly on a torn
line — silently skipping a malformed record could drop an `applied` marker and re-open the replay
window a human approval exists to close — while projection degrades rather than crashing. Three
stores read strictly because their rows change a decision (gate, expectation rows, operator inbox);
three read tolerantly because their rows only render or rate-limit (attention dismissals,
orchestration nudges, agent-notifier signals). Gate and expectation rows additionally carry a
projection-only tolerant reader beside the strict one — `read` plus `read_for_projection` — used by
`observer/snapshots.py` and by nothing that decides. **Every rewrite of an authority-bearing log
reads strictly**, which is what makes two policies safe rather than merely different: each of the
three strict stores drives its rewrites from its strict read, so a compaction can never erase a
record it could not parse. The three tolerant stores drive their rewrites from their tolerant read
and therefore do drop an unparseable row on compaction, which is safe only because none of them
carries authority.

**`schemaVersion` needs no version branch in any reader.** `DurableRecord` validates it on the way
in, so an unknown major raises `ValidationError` and strict readers surface it while tolerant
readers skip it. Verified on all six record types: minor `1.99` accepted, major `2.0` rejected.
`worktrees/worktree_contract.py` imports the same constant and predicate, so the tree has one
version policy.

**A per-log process-wide `RLock`** (`kernel.file_lock.thread_mutex_for`) is taken before the flock, always in that
order. Stated carefully: `flock` **does** already serialise threads within one process on POSIX,
because the lock lives on the open file description and `exclusive_access` opens a fresh one per
non-reentrant acquisition. The mutex is therefore **not** fixing a reproducible loss. What it
closes is that the thread-level exclusion rested on where the handle came from rather than on
anything declared — cache one lockfile handle across threads, the obvious "stop opening two files
per append" optimisation, and every thread would share one description and `flock` would silently
stop excluding them. That regression was simulated and does lose records without the mutex.

**The enforcement caught a real bug before it shipped.** `serving/app.py` calls
`gate_decide_payload` directly, so an MCP-side reclaim ran inside the dashboard and raised
`CompactionOwnerError` past `suppress(OSError, ValueError)` — every dashboard gate decision would
have crashed. Fixed with an `is_compaction_owner()` guard in `_reclaim_gate_log`.

**One accepted behavioural consequence.** Gate reclamation now follows owner activity rather than a
wall clock: a gate raised and expired by the dashboard is reclaimed on the next MCP decision on that
lifecycle, rather than within 30 seconds. Space-only, never correctness — the projection is
keep-filtered in memory every tick regardless of what is still on disk.

260713-PHA-L6 keeps operator inbox rolling compatibility deliberately narrow: legacy readers may
preserve optional `adapterDeliveryState` and `adapterDeliveryDetail`, while unrelated extensions
remain forbidden. These delivery-evidence fields do not alter explicit consume or provider
degradation state semantics.

260712-TRH-L5 adds a secondary confirmed-gone retention predicate without changing fallback
 retention: only pending agent-notifier nudge/escalation rows with a subject id qualify, catalog
`terminated` is direct proof, and a compacted tombstone needs one successful exact-name tmux
snapshot. `OperatorInboxStore.reconcile_and_compact` resolves and compacts under one lock and
reuses the folded current before redelivery; consumed/durable/protected rows and indeterminate
evidence remain visible.

260707-HFX2-L20 makes inbox state monotonic across concurrent consume and hosted delivery. The
append-only log retains the terminal consume snapshot; a shared fold used by live reads and
compaction ignores physically later pending snapshots once an id is consumed or ladder-resolved.
Explicit dismissal remains physical deletion, and time-based compaction remains audit cleanup.

260707-HFX2-L17 carries `seatRole` beside `leafKey` through expectation rows, operator inbox rows,
 renewal, agent-notifier cooldown records, and routing. Current manager/architect/worker discovery and
chain credit use binding identity; only the escalation ladder's historical parent hop reads
 `spawnRole`. Same-text agent-notifier conditions on one leaf coalesce only within the same role, so
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
non-enforcement wait pickup, dismiss, clear, and the 24-hour TTL physically delete throwaway
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

**260707-HFX2-L1** makes the operator inbox the signal substrate the L2 agent-notifier sweep drives:
R1 extends `OperatorInboxEntry` with ack/backoff fields (`attemptCount`/`lastAttemptAt`/
`nextAttemptAt`/`escalatedAt`) so delivered is not acknowledgement. HFX3 supersedes L1's
immortal-pending retention: pending rows expire after 48 hours, the folded inbox is capped at 500
current ids, and the durable artifact—not the row—is the record. R2 adds `expectation_rows.py`
(`ExpectationRowStore`/`write_expectation_row`): every dispatch surface (spawn, gate open, signal
post) atomically writes a durable what-must-happen-by-when row (kinds `briefed-by` /
`verdict-by` / `ack-by`; `turn-report-by` is retained only as a legacy record Literal since
260713-TES-L2 — no new rows are written and the settings surface no longer lists it),
configurable per-kind SLA via
`orchestration.expectations` in `kernel/agentic_settings.py`. R3 adds `inbox_backoff.py`: pure
backoff-ladder math + a per-target rate-limit gate mirroring `OrchestrationNudgeStore`'s pattern,
consumed by `OperatorInboxStore.list_redeliverable`/`record_delivery`. R4 adds
`signal_routing.py::derive_signal_owner`: the routed owner address (worker -> its manager, manager
-> its orchestrator, decision-item -> architect) derived from task-document containment and role,
stamped with structural owner plus private occupant correlation at post time.
Neither this leaf's redelivery driver nor its ladder escalation exist here — L2 (a sibling leaf)
drives the actual sweep; this route only builds the durable substrate + surfacing it reads.

**260713-TES-L2 — the state-signal substrate and landed terminality.** `InboxMessageKind` gains
`state-signal` (N12), and `operator_inbox_records.state_signal_landed` makes correlated adapter
acceptance at a turn boundary terminal ON THE RELAY PATH while the row state stays `pending`
(the formal `landed` state rides the L4 schema migration); `acceptance=queued` is not a landing.
`record_delivery` clears `nextAttemptAt` for landed rows, `inbox_backoff.is_due` excludes them,
and `inbox_reclamation._eligible` excludes them — no redelivery, ladder, or reclamation may
re-touch a landed relay row. The worker→manager artifact/SLA interpretation
(`turn-report-by`/`turn-report-stale`) is retired (N8/R6): `briefed-by` rows remain dashboard
provenance but no longer drive notifier findings.

**Current master-scoped ownership.** Real task-document containment supplies leaf→master→sprint
scope. `derive_signal_owner` resolves one role-appropriate parent seat and then its singular current
catalog occupant; spawn ancestry is audit provenance only. Compound-idle and non-reaction flows use
the same task-owned scope and fail closed when the qualified owner is absent or ambiguous.

**260713-TES-L4 — the N13/N16 inbox-schema migration, scoped custody, and terminal
truth.** `OperatorInboxState` gains the formal terminal vocabulary `landed`/`superseded`/
`unresolved`/`expired` (legacy `consumed`/`ladder-resolved` retained for parse compatibility);
the success terminal is `landed` — correlated adapter acceptance at a turn boundary — and
`state_signal_landed` folds to `state == "landed"`. `operator_inbox_records` adds
`terminalAt`/`terminalReason`/`supersededBy`; `consume_operator_inbox_entry` is an
attribution-only marker that never changes state. `operator_inbox_transitions` owns the
terminal/rebind transitions (`mark_landed`/`mark_superseded`/`mark_unresolved`/`mark_expired`,
`rebind_entry`, `ExpiryOptions`), all built on `OperatorInboxStore.transition` — a lock-held
read+append against the LATEST fold so a stale sweep snapshot can never overwrite a concurrent
terminal write (F1). `list_for_mailbox(..., include_terminal=True)` gives N11 terminal
inspectability. `interaction_retention` re-means the 48h window as terminal-marker retention
and the pending TTL as a sweep-owned resolution boundary; the 500-row cap drops
terminal-oldest-first with counted/surfaced drops (D4). `signal_routing.derive_architect_owner`
is repository+sprint-scoped (R13, exact-leaf preference, role-only mailbox fallback — never
global first-match) and `derive_row_owner` is the N14 sweep-time derivation (dispatch-brief
exact-pinned, worker→manager / manager→orchestrator re-resolution, scoped-orchestrator
replacement). The escalation ladder is dormant as policy (N3) — the sweep no longer drives it —
with `next_step` passing the row's `leafKey` through for scoped architect custody; L5 deletes
the machinery.
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
`serving/agent_notifier.py`, this route's sole caller.
**260707-HFX2-L8** closes the dead-seat storm gap on that substrate: `OperatorInboxEntry` gains the
durable terminal `state="ladder-resolved"` plus `ladderResolvedAt`/`ladderResolvedReason`; `inbox_backoff.py`
excludes ladder-resolved rows via an explicit predicate; `OperatorInboxStore` mutations accept an
optional in-sweep `current()` snapshot and add idempotent `mark_ladder_resolved`; and
`interaction_retention.py`/`compact()` prune ladder-resolved terminal rows. Mid-climb rows and
live-seat rows remain pending/redeliverable only within the HFX3 48-hour TTL and 500-row health cap.
**260707-HFX2-L9** adds the redelivery-cadence floor and agent-notifier signal cooldown substrate:
`inbox_backoff.py` now owns the 900-second `MIN_REDELIVERY_INTERVAL_SECONDS` and refuses sub-floor
values, `OperatorInboxStore.record_delivery` threads that floor into stored `nextAttemptAt`
scheduling, and new `agent_notifier_signals.py` stores pane/seat-liveness signal cooldown records keyed
by owner/leaf/finding kind/detail. Known deferral: `agent_notifier_signals.py` is currently an unbounded
append-only log with no compactor and performs full-file reads through `in_cooldown`; HFX2-L11 tracks
 that CS-6-class scaling gap before the agent-notifier is re-enabled.

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
| `store.py`    | `GateStore`: lifecycle/workspace gate logs beside the event log; `current()` folds by gate id (last-wins), while `delete`/`compact` physically remove throwaway interaction rows under the log's lock. The strict `read` backs enforcement; the tolerant `read_for_projection` backs `projected_current`, which replaced `compact_current` and rewrites nothing. |
| `operator_inbox_records.py` | `OperatorInboxEntry` v2 plus structural address/owner/subject value objects, private delivery correlations, formal terminal vocabulary, and attribution-only consume. |
| `operator_inbox_store.py` | (260713-TES-L4) `OperatorInboxStore`: workspace inbox log, pending/terminal mailbox filters (`list_for_mailbox`, N11), delivery-state snapshots, the lock-held latest-fold `transition` primitive, attribution-only idempotent consume, public delete/dismiss paths, and retention compaction. |
| `orchestration_artifacts.py` | Strict turn-report, master-handover, and escalation packet helpers for the L2/L3 orchestration frame, with HFX-L6 architect/curator role literals in the artifact vocabulary. |
| `orchestration_nudges.py` | `OrchestrationNudgeRecord` + `OrchestrationNudgeStore`: append-only, rate-limited manager nudge attempts plus message/artifact helpers. |
| `gate_policy.py` | `GatePolicy` / `GatePolicyRule`, built-in policy names, human-pinned/delegable kind validation, and delegated-decision attribution/evidence checks. |
| `enforcement.py` | `evaluate_gate` (pure kind-generic gate policy resolver) + `GateGuard`; `evaluate_closeout_gate` / `CloseoutGuard` remain the closeout wrapper `worktree_closeout_apply` reads. |
| `attention_dismissals.py` | `AttentionDismissalRecord` + `AttentionDismissalStore`: compact current acknowledgement rows for attention queue dismissals, with physical prune by live lifecycle id and a targetless actionable-drift exception. |
| `interaction_retention.py` | (260713-TES-L4, N13/§9) Shared 5-minute pickup/wait, 24-hour consumed-row audit TTL, 48h terminal-marker retention, sweep-owned pending-TTL resolution boundary, and 500-current-row hard health cap (terminal-oldest-first, counted drops); ladder-resolved rows drop immediately. |
| `expectation_rows.py` | Durable what-must-happen-by-when rows with task-document/role subjects and private occupant correlation; dispatch/gate seams write them atomically, never as in-memory timers. |
| `inbox_backoff.py` | (260707-HFX2-L1, R3; HFX2-L9) Pure redelivery backoff-ladder math + the shared 900-second redelivery floor/fail-loud validation, mirroring the `OrchestrationNudgeStore` pattern while refusing sub-floor retry cadences. |
| `agent_notifier_signals.py` | Persisted cooldown records keyed by structural owner plus private current-occupant correlation, finding kind, and detail. |
| `signal_routing.py` | One-hop owner routing from task containment and role; decision items resolve the sprint architect, ordinary rows rebind to current occupants, and ambiguity fails closed. Spawn ancestry is excluded from resolution. |
| `escalation_ladder.py` | (260707-HFX2-L4 + L13/HFX3 correction; DORMANT since 260713-TES-L4, N3) `rung_due`/`next_step`/`seat_is_suspect`: the pure tier-3 ladder walker, configured dwell plus redundant five-minute later-rung floor, scoped architect terminal custody via leaf-key pass-through (R13), and dead/stalled-seat respawn-candidate detection. The sweep no longer drives it; L5 deletes the module. |
| `orphan_policy.py` | (260707-HFX2-L4, R3) `find_orphaned_workers`: a pure catalog read for a dead/respawned manager's still-running worker seats -- detection/surfacing only, no re-parent action. |
| `durable_store.py` | `ar-durable-store/1.0`: record/schema validation, the six store ownership declarations, process-role view, target-guarded access, durable appends and held-lock atomic rewrite. Kernel owners provide shared file exclusion and atomic temp publication. |
| `__init__.py` | Package export surface (gate records/store/enforcement + operator inbox records/store), plus the durable-store contract surface: constants, error types, `DurableRecord`, `StoreOwnership` and the process-role pair. The locking and rewrite primitives and the per-store ownership constants are deliberately not re-exported. |

The structural `gate_*` MCP tools live in `mcp/tools/gates.py`; internal exact correlations are
isolated from the public document-and-role responses in `models/structural/gates.py`. Ordinary
agent messaging enters through the structural application and durable operator-inbox substrate;
operator-facing inbox administration remains a separate internal surface.

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
  dismiss, clear, lifecycle prune, and TTL cleanup physically delete them; inbox consume instead keeps
  a terminal audit snapshot until TTL cleanup. Durable task docs, contracts,
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
- **Every append and every rewrite of every one of the six JSONL logs holds that log's lock**
  (260731-EFA-L5). No store is exempt, no process is exempt, and there is no flag that turns it
  off. Skip it anywhere and the lost-update window returns silently, with the caller told the
  record was written.
- **The lock is held across the read AND the rewrite, never around the rewrite alone.** A record
  list chosen by a read outside the lock is already stale, and rewriting from it is the same lost
  update under a different name. Each store splits its reclaim into a public method that takes
  `exclusive_access` and a `_locked` / `_unlocked` half that does the work;
  `require_lock_held` raises from inside `rewrite_lines` for anything that gets it wrong.
- **Ownership is advisory and is never what durability rests on.** `check_declared_writer` is
  silent in every CLI invocation, script and test; `is_compaction_owner` never raises at all. Do
  not read either as a guarantee, and do not remove a lock because an owner is named.
- **Rewrites never unlink.** An empty kept set is written as an empty file, so a concurrent
  appender cannot write into an inode with no remaining links.
- **Store writes compose through `durable_store.py`.** Keep checkout authorization before lock side effects, use the shared `kernel.file_lock` mechanics, and publish replacements through `kernel.atomic_write`; duplicating those owners would split the protection contract.
- **The read-policy split is a decision, not an inconsistency**, and every rewrite of an
  authority-bearing log reads strictly. Pointing a strict store's rewrite at a tolerant reader
  turns a torn line into a silently deleted record.
- **No reader branches on `schemaVersion`.** `DurableRecord` rejects an unknown major at parse
  time; that single rule is what gives both read policies their behaviour.

## Evidence

### Repo-Internal References

- Gates mirror the observer event substrate (envelope + append-only JSONL store). [1]
- Gate policy validation and delegated decision checks. [2]
- The `gate_*` payload builders that drive this substrate. [3]
- Gate response models, including the structural public boundary and internal exact correlations. [4]
- The inbox record/store pair provides the external-chat pull return channel. [5]
- The attention acknowledgement store keeps current lifecycle-scoped queue dismissals only. [6]
- The provider degradation detector posting `degradation-alert` inbox rows addressed to `system-specialist`'s ladder peers (260707-HFX-L7); governed by the `mcp/` package overview. [7]
- Guarded durable-store composition preserves coordinator containment and held-lock rewrite. [8]
- Shared kernel exclusion is independent of caller authorization. [9]
- Durable-store role declaration follows application entry paths: `prepare_mcp_process` declares the MCP role, while dashboard `_dev_app` declares in the reload worker and `run` declares on the foreground/daemon command path. [10]
- Gate compaction is guarded by control-plane ownership because trusted dashboard paths call `gate_decide_payload` directly. [11]
- The projection tick reads folded gates and pending expectation rows without rewriting them. [12]
- The serving relay composes fact predicates and dispatches fact actions over this route's stores. [13]

## 260712-TRH-L4 Route Impact

Controlplane expectations now start at the durable exact-session dispatch-brief entry, using its timestamp and id; pending rows remain pinned and never enter generic readdressing or respawn escalation.


### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## 260718-CHATS-L5I Current Route Impact

Gate records now have an explicit reopen transition for an adapter decision that failed to deliver. The transition makes the gate answerable again and carries failure evidence, so an operator's decision is never silently consumed or left represented as an approval.

Route indexes are intentionally not regenerated during this partitioned curator pass; the manager will run the single aggregate refresh after all curator ownership is complete. Existing verification metadata remains pre-commit.

## 260731-EFA-L2 Record Builder Parameter Objects

Every record builder in this route is now signed on frozen parameter objects rather than long
keyword lists, and the groupings are the route's own vocabulary:

- gates — `GateAnchor` (what a gate is raised against), `GateRequest` (what the decider is handed),
  `GateVerdict` (the verb + who + through which channel + in which role). The verdict is one object
  because the closeout policy never reads its parts apart.
- inbox — `InboxAddress` / `InboxOwner` / `InboxRouting` (where a row goes and who owns it),
  `InboxSubject` / `InboxMessage` (what it says and about what), `InboxPoster` (who put it there),
  plus `DeliveryAttempt` / `AdapterReceipt` / `InboxRenewal` on the store. Passing
  `InboxRenewal.readdress_to` *is* the readdress — the old `readdress: bool` beside loose `owner_*`
  values is gone.
- expectations — `ExpectationSubject` / `Expectation`.
- agent-notifier signals — `AgentNotifierSignalTarget` / `AgentNotifierSignalKey`; the cooldown key is
  compared whole, so `last_sent` and `in_cooldown` cannot diverge on which fields identify a signal.

No record schema, wire field or refusal changed.

## 260731-EFA-L16 Route Impact — one order across stores

`exclusive_access`'s docstring now declares the cross-store order beside the intra-store one: no
thread may hold one store's lock (mutex, RLock, or flock) while acquiring another store's lock;
evidence a transaction needs from a second store is gathered before entry, or the side effect
runs after exit — never nested. The two nestings this forbids (the liveness sweep's catalog
batch across the synchronizer's inbox/gate locks; the agent-notifier's inbox transaction across a
catalog read) deadlocked ABBA in production on 2026-08-05. The operator-inbox store's lock-held
fold → resolve → compact transaction is untouched — L5's declared exception stands; what moved
is the evidence gathering around it (the agent-notifier's catalog read now precedes the lock), and
the liveness sweep's synchronizer side effect now follows its batch commit.

### 260713-TES-L5 Route Impact — Judgment Demolition

The control plane is reduced to the fact-relay surface: `escalation_ladder.py` and
`orphan_policy.py` are deleted, the ladder transitions (`mark_escalated`/`advance_rung`/
`mark_ladder_resolved`/`RungAdvance`) are gone, `derive_skip_level_owner` is gone, and
`expectation_rows.py` is an owner-visible deadline surface the relay never evaluates.
`operator_inbox_records` keeps the legacy rung fields and `ladder-resolved` state as
parse-compat; the confirmed-gone reclamation fold still writes `ladder-resolved`
(reviewer F4).

## 260815-DAG-L3 Sprint Candidate Artifact

The control plane now includes a bounded canonical `artifacts/closeout-candidates.json` per sprint
and one adjacent pending transaction. `CloseoutQueueStore` uses the common durable-store lock,
explicitly admits MCP and lifecycle-operation writers, retains at most 128 request receipts, and
recovers an exact one-revision publication after a crash. The same store lock serializes task-fact
publication, candidate lane ownership, atomic blockers, and sprint completion/reopen; the WAL is
publication scratch and the JSON artifact remains the survival record.

## 260815-DAG-L4 L4 Serialization Boundary

Control-plane storage adds a repository-wide integration-authority lock and composes it after sprint queue authority. Task-fact publication, candidate declaration, series terminal publication, and Git mutation therefore share a fail-closed queue-to-repository order instead of racing check-then-act branch guards. That lock module (`controlplane/integration_authority_lock.py`) was deleted with the whole lock plane by the de-entanglement cut (commit `1a0919c1`); there is no queue-to-repository lock order any more.

## 260815-DAG-L15 Route Impact

`integration_authority_lock` gained the keyword-only `create` flag: the three dry-run paths (graph authoring + sprint attach/detach) lock with `create=False` so a preview never writes the lock file (playthrough F2); apply paths keep `create=True` and re-lock before any mutation.

## 260815-DAG Master Full-Gate Repair Route Impact

`closeout_queue_store.py` / `closeout_queue_records.py` import paths updated to the moved `worktrees/queue/*` / `models/queue/*` locations.

## 260821-CLIVE Final Task-Publication And Projection Boundary

Task and door truth was published under `task_publication_lock.py`, a short repository-scoped CAS
mutex. **That lock was deleted with the whole lock plane by the de-entanglement cut** (commit
`1a0919c1`, "delete the lock plane"), together with `controlplane/integration_authority_lock.py` and
`worktrees/integration/lifecycle/lifecycle_operation_lease.py`. The developer ruling is that these are
throwaway task documents rather than bank records; the accepted cost is that two concurrent writers
of the same task document may lose one write. No lock is taken to prove a claim. The canonical
mutation is still never blocked by the state of a closeout projection. The transaction shape is
unchanged:

```text
task or door change
  -> publish canonical bytes
  -> invalidate each affected projection to durable invalid-empty
  -> build a complete candidate off-side from current task + waiting-door truth
  -> publish valid-built only if the source identity is still exact-current
```

`closeout_queue_records.py` and `closeout_queue_store.py` therefore own only disposable projection
builds and invalid-empty/valid-built persistence. They do not own claims, commits, certification,
integration, blockers, receipts, lifecycle state, or task freezes. A failed refresh is an explicit
bounded effect and cannot undo the accepted canonical mutation.

Task-execution retention follows the same ownership rule. `operator_inbox_store.py` and
`interaction_retention.py` protect task-bound worker/reviewer/curator reports until exact first
evidence is registered in task truth. Missing registration fails closed for deletion; no heuristic
reader or compatibility path may erase the only proof that execution started.

## 260824-PDLS Final Queue-Store Reconciliation

The closeout queue store persists only disposable valid-built or invalid-empty projection state.
It does not retain lifecycle, claim, commit, certification, or stale-row transition evidence; an
absent prior file is normalized by publishing invalid-empty state rather than reporting a separate
`not-created` authority condition.

## 260821-ARSPAWN-L2 Canonical Occupancy

`seats.current_seat_occupant` is the single pure selector for a canonical document-and-role seat.
It checks incumbent and staged-heir cardinality independently, so duplicate heirs still fail
closed even while one valid incumbent is present. One incumbent wins until it leaves; only then
does the one staged heir become current. Routing, delivery, catalog, and observer consumers use
this selector instead of re-deriving generation choice.

`signal_routing.py` translates malformed or ambiguous occupancy into
`StructuralRoutingError`. Notifier evaluation contains that error per finding so one corrupt
address cannot abort unrelated rows.
