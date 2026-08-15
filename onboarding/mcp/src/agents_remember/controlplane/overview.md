# mcp/src/agents_remember/controlplane

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| sourceRoute            | `mcp/src/agents_remember/controlplane`         |
| doc_type               | `route-local-overview`                         |
| lastUpdated            | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2`|
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview      | `../../../overview.md`                         |

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

L23 extends the validated store seam for batched operator-inbox transitions used by notifier
expiry. Batch preparation resolves canonical task/owner addresses first and fails closed when a
row is missing, mismatched, or structurally unaddressable; it never guesses a replacement runtime
identity. The same durable-store containment and model-validation rules apply to these rewrites.

**260731-EFA-L21 — target containment precedes filesystem effects.** The shared durable-store lock,
append, and rewrite primitives ask the kernel checkout policy to authorize the target before
creating a parent directory, lock file, temporary file, or durable row. In undeclared linked
worktree mode only the deterministic `provider-runtime/dev-ar-coordination` subtree is writable;
trusted MCP/dashboard and explicit test modes retain their declared roots.

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
`test_interaction_retention.py`). `durable_store.py`'s module docstring reports the rest at that one
site — and it is the text these cards document, so quoting it back is not corroboration:
supervisor-signals 10.50 percent, expectation-rows 10.20 percent, orchestration-nudges 9.20 percent,
operator-inbox 0.00 percent (the one that already held a lock), 127 of 2000
`AttentionDismissalStore.dismiss` calls raising, and ten runs per store. That docstring is also the
only authority for records disappearing whole rather than torn — the property that would explain why
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

All six now implement one declared contract, `ar-durable-store/1.0` in `durable_store.py`, and
every byte of control-plane file I/O routes through it — exactly one `open("a", ...)`, one
`os.replace`, one temp-path construction and one `import fcntl` remain in the whole package, all
four in that module.

**The lock is the mechanism; ownership is advisory.** Every append and every rewrite of every one
of the six logs takes that log's lock, in every process, whether or not that process declared
anything. There is no flag that turns it off and no store exempt from it; the `serialized` opt-out
an earlier draft carried was deleted. Ownership is expressed two ways, neither of them a durability
guarantee: `StoreOwnership.check_declared_writer` raises but only inside a process that called
`declare_process_role` (the MCP server and the dashboard daemon, nowhere else), and
`is_compaction_owner` is a question that never raises. Where ownership does real work it does it
structurally, by moving code rather than by checking at runtime. `require_lock_held` is the one
check that raises unconditionally, from inside `rewrite_lines`, so no store can rewrite a log it
has not locked however the call was reached — it can afford to, because it asks about the calling
thread's own lock rather than about a process-wide declaration.

**Single-writer is a deployment fact, not a structural one.** An earlier draft left the two
single-writer stores (attention-dismissals, supervisor-signals) unlocked on the strength of being
single-writer, and the sources put 31.45 percent loss on attention-dismissals doing exactly
that. `AttentionDismissalStore.dismiss` is a whole-file read-modify-write reached from the
dashboard HTTP dismiss route at `serving/app.py:1164`, so two concurrent dismisses lose each other
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

**A per-log process-wide `RLock`** (`thread_mutex_for`) is taken before the flock, always in that
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
| `durable_store.py` | (260731-EFA-L5) `ar-durable-store/1.0`: the one contract all six JSONL stores implement, and the only place in the package that appends, rewrites, builds a temp path or imports `fcntl`. Owns `DurableRecord` (the shared record base with `extra="forbid"` and a validated `schemaVersion`), `StoreOwnership` plus the six per-store ownership constants, `declare_process_role`, the `exclusive_access` / `thread_mutex_for` / `require_lock_held` locking primitives, the `_verify_lock_capability` filesystem probe, and `append_line` / `rewrite_lines`. |
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
- **All file I/O for this route lives in `durable_store.py`.** Adding a second `open("a", ...)`,
  `os.replace`, temp-path construction or `fcntl` import anywhere else in the package is the
  regression this leaf exists to prevent.
- **The read-policy split is a decision, not an inconsistency**, and every rewrite of an
  authority-bearing log reads strictly. Pointing a strict store's rewrite at a tolerant reader
  turns a torn line into a silently deleted record.
- **No reader branches on `schemaVersion`.** `DurableRecord` rejects an unknown major at parse
  time; that single rule is what gives both read policies their behaviour.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Gates mirror the observer event substrate (envelope + append-only JSONL store). | "class EventStore" | mcp/src/agents_remember/observer/store.py:103-103 |
| Gate policy validation and delegated decision checks. | "class GatePolicy:" | mcp/src/agents_remember/kernel/primitives/gate_policy.py:54-54 |
| The `gate_*` payload builders that drive this substrate. | "def gate_create_payload" | mcp/src/agents_remember/mcp/tools/gates.py:44-44 |
| Gate response models, including the structural public boundary and internal exact correlations. | "class GateCreateResponse"; "class StructuralGateResponse" | mcp/src/agents_remember/models/structural/gates.py:48-55; mcp/src/agents_remember/models/structural/gates.py:108-116 |
| The inbox record/store pair provides the external-chat pull return channel. | "class InboxAddress", "class OperatorInboxStore" | mcp/src/agents_remember/controlplane/operator_inbox_records.py:41-41; mcp/src/agents_remember/controlplane/operator_inbox_store.py:54-54 |
| The attention acknowledgement store keeps current lifecycle-scoped queue dismissals only. | "class AttentionDismissalStore" | mcp/src/agents_remember/controlplane/attention_dismissals.py:45-45 |
| The provider degradation detector posting `degradation-alert` inbox rows addressed to `system-specialist`'s ladder peers (260707-HFX-L7); governed by the `mcp/` package overview. | "class ProviderDegradationStore" | mcp/src/agents_remember/providers/degradation.py:171-171 |
| The `ar-durable-store/1.0` contract every JSONL store in this route implements, and the only module in the package that appends, rewrites, builds a temp path or imports `fcntl`. | "SCHEMA_VERSION = " | mcp/src/agents_remember/controlplane/durable_store.py:46-46 |
| Durable-store role declaration follows application entry paths: `prepare_mcp_process` declares the MCP role, while dashboard `_dev_app` declares in the reload worker and `run` declares on the foreground/daemon command path. | `prepare_mcp_process`; `_dev_app`; `run` | mcp/src/agents_remember/application/runtime/startup.py:33-36; mcp/src/agents_remember/cli/dashboard.py:52-81; mcp/src/agents_remember/cli/dashboard.py:161-196 |
| Gate compaction is guarded by control-plane ownership because trusted dashboard paths call `gate_decide_payload` directly. | "def gate_decide_payload" | mcp/src/agents_remember/mcp/tools/gates.py:92-122 |
| The projection tick reads folded gates and pending expectation rows without rewriting them. | "def read_gates(coordination_root: Path, *, now: datetime"; "def read_expectation_rows(" | mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:105-105; mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:195-195 |
| The serving relay composes fact predicates and dispatches fact actions over this route's stores. | `evaluate_predicates`; `_FINDING_ACTIONS` | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:349-403; mcp/src/agents_remember/serving/_agent_notifier_actions.py:675-702 |

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
publication, candidate lane ownership, atomic barriers, and sprint completion/reopen; the WAL is
publication scratch and the JSON artifact remains the survival record.

## Update History

- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: documented the canonical bounded queue
  artifact, writer census, WAL recovery, and shared task-fact/sprint-status lock. Verification
  remains closeout-owned.

- 2026-08-13T09:05+02:00 — No route impact: L23's current source delta changes lifecycle model
  packaging and worktree-lineage enforcement without changing any `controlplane/` source. Existing
  gate, durable-store, signal, and inbox authority remains unchanged; verification provenance
  remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: documented structurally addressed, fail-closed batched inbox transitions under the validated store boundary; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled the control-plane route with
  plane-owned occupant addressing, structural document-and-role seats, pinned inbox delivery, and
  current-owner routing; affected file cards retain the direct source evidence.

- 2026-08-10T19:57:55+02:00 — 260731-EFA-L21 route impact: recorded the durable-store target guard,
  its pre-filesystem ordering, and linked-worktree dummy-root containment. Verification metadata
  remains pinned until closeout stamps the L21 code commit.

- 2026-08-10T10:30+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-10T04:39+02:00 — 260713-TES-L6: added exact-sprint routing and command-role versus
  subordinate-role separation to the controlplane hot path. Verification metadata remains pinned
  until closeout.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 route impact: recorded the ladder/orphan/skip-level
  demolition, the owner-visible expectation surface, and the legacy parse-compat posture in
  the records. Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 route impact: recorded the N13/N16 inbox-schema
  migration (formal terminal vocabulary, landed-at-boundary, attribution-only consume), the
  lock-held latest-fold transition primitive (F1), N11 terminal inspectability, the N13/§9
  retention re-meaning, R13 scoped architect custody, N14 row-based owner derivation, and the
  dormant escalation ladder (N3). Layout rows refreshed for records/store/retention/routing/
  ladder. Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 route impact: recorded the public `master_key`
  promotion and its compound-idle consumer (`state_signals.py` master-scoped membership),
  plus `derive_signal_owner` as the one-hop owner for compound-idle and manager-residue
  signals (no global fallback). Verification metadata pinned until closeout stamps the
  260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 route impact: recorded the state-signal substrate
  (`InboxMessageKind`, `state_signal_landed`, backoff/reclamation/transition exclusions) and
  the turn-report-by retirement. Verification metadata pinned until closeout stamps the
  260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 route impact: `supervisor_signals.py` renamed to
  `agent_notifier_signals.py` with `AgentNotifierSignal*` identifiers; durable names
  (`supervisor-signals.jsonl`, `store="supervisor-signals"`, `ar-supervisor-signal/v1`) retained
  until their schema migration; the sole caller is now `serving/agent_notifier.py` and the
  settings family is `orchestration.agentNotifier` (explicit legacy alias). Verification metadata
  pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-05T22:30+02:00 — 260731-EFA-L16 route impact: recorded the cross-store lock-order doctrine in `durable_store.py` and that the inbox's lock-held transaction (L5's exception) is untouched. Verification metadata pinned until closeout stamps the code commit.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  anchors and source-backed ranges; exact non-fixing check returns zero findings.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: corrected durable-store startup ownership to
  the application wrapper plus both dashboard entry paths. New ranges are explicit `:1-1` curator
  input.

- 2026-08-01T19:10+02:00 — Measured-claim repair; no prose about the lock, ownership, the read-policy
  split or the compaction owners was touched, because it was right. The Hot Path Summary asserted six
  base-commit loss rates, "127 of 2000 raising", "zero torn lines in every run" and a post-fix "0
  lost, 0 raised, 0 torn, all six stores, all scenarios" as findings a reader could check. **No
  base-commit measurement artifact is committed anywhere in the tree**, so that is now stated once,
  plainly, and the rates are split by how well they are corroborated: 31.45 percent (four
  independent sites) and 11.50 percent (three) are asserted plainly on the sources' authority, while
  10.50 / 10.20 / 9.20 / 0.00 percent, 127 of 2000, "ten runs per store" and the whole-not-torn
  property exist only in `durable_store.py`'s module docstring — the text these cards document — and
  are attributed to it rather than restated as findings. **The post-fix claim was wrong in both
  directions and is now stated at its true strength against
  `test_controlplane_store_durability.py::MultiProcessDurabilityTests`:** `lost == 0` holds in all
  three scenarios but over *five* stores in `forced_unlink` (`APPEND_CASES`; attention-dismissals has
  no `append`, so it is excluded by construction) and six in the other two, while `torn_lines == 0`,
  `append_error_count == 0` and `reclaim_error_count == 0` are asserted in the `stress` scenario
  only. Added the one base-commit fact a reader *can* check — `HarnessSensitivityTests` asserting
  1-of-1 loss for each unlocked store and 0 for operator-inbox against a `git archive` of
  `e52edaf5`. The 18:30 entry below had the same six-rate list in its parenthetical and it was
  reduced to the attribution. No line numbers were added into `durable_store.py`, which is under
  active edit. Verification metadata untouched; closeout owns it.
- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity), route-level. Recorded the loss
  the sources report across all six JSONL stores at the base commit and the single
  `ar-durable-store/1.0` contract
  in the new `durable_store.py` that closed it. Recorded, as the route's governing distinction,
  that the unconditional per-log lock is the mechanism while ownership is advisory, with
  `require_lock_held` the one check that raises unconditionally because it asks about the calling
  thread's own lock. Recorded that single-writer is a deployment fact rather than a structural one
  and why the store that looked safest lost the most. Recorded the compaction owners including the
  operator-inbox `None` exception; that `rewrite_lines` never unlinks; the strict/tolerant read
  split with the every-authority-rewrite-reads-strictly property stated per store; the
  `schemaVersion` rule that removes version branches from readers; the process-wide `RLock`
  described as defending a simulated regression rather than fixing an existing thread race; the
  `CompactionOwnerError` bug the enforcement caught in the dashboard's direct `gate_decide_payload`
  call; and the accepted space-only consequence that gate reclamation now follows owner activity.
  Added `durable_store.py` to the Layout table and eight route invariants. The route index
  (`overview.index.json`) is deliberately not regenerated in this partitioned curator pass;
  the manager owns the single aggregate refresh. Verification metadata pinned until closeout stamps
  the L5 commit.
- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: `create_gate`, `decide_gate`,
  `create_operator_inbox_entry`, `OperatorInboxStore.record_delivery`/`advance_rung`/`renew`,
  `create_expectation_row`, `write_expectation_row`, `SupervisorSignalCooldownStore.last_sent` and
  `in_cooldown` were all re-signed onto frozen parameter objects, and `gate_policy` gained the
  extracted `_decision_attribution_failure_reason`. Record schemas and refusals are unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: recorded the exact two-field additive inbox-reader seam for
  rolling serving compatibility; unrelated extensions remain rejected.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.

- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: refreshed the control-plane route for the
  confirmed-gone inbox predicate, same-lock terminal resolution/compaction, persisted folded-id
  removal accounting, unchanged TTL/cap fallback, and the callback no-store-reentry contract.
  Verification metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20 control-plane route impact: documented the shared
  terminal-dominant inbox fold and durable consume snapshot that close the in-flight redelivery race.

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
