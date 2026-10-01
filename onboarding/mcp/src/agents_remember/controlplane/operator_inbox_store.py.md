# mcp/src/agents_remember/controlplane/operator_inbox_store.py

## Governing Overview

[overview.md](overview.md)

## Purpose

File-backed operator inbox store for short-lived polling plus hosted-session
delivery metadata.

## Code Commentary

Current persistence owns strict terminal-dominant folding, lock-held transitions, ordered validated transition batches, mailbox reads, consumption and retention. Delivery, renewal and expiry payload semantics live in operator_inbox_transitions.py; they are not additional methods on this store. `transition_many` folds once, applies duplicate ids against prior batch results, validates all updated rows and appends under one lock. `reconcile_and_compact` resolves only still-pending ids, preserves a consume/terminal winner and reports persisted folded-id removal counts. Task-bound worker/reviewer/curator turn reports are protected until their execution evidence is registered. A correlated landed acknowledgement is terminal too; model consume is not the only possible end of redelivery. cit:([`transition_many`, `_unregistered_execution_report_ids`, `reconcile_and_compact`], mcp/src/agents_remember/controlplane/operator_inbox_store.py:54-67; mcp/src/agents_remember/controlplane/operator_inbox_store.py:117-150; mcp/src/agents_remember/controlplane/operator_inbox_store.py:300-350).

### 260731-EFA-L5 The Declared Compaction-Owner Exception (historical milestone)

This is the **only one of the six control-plane stores with `compaction_owner=None`**, and it is
the leaf's declared exception rather than an oversight. Every other log was given a single
compaction owner so that no two processes read-modify-write it. This one cannot be, because both
long-lived processes must physically **remove** rows, not merely append them:

- The MCP process deletes the inbox rows tied to a cancelled gate (`mcp/tools/gates.py` calling
  `delete_by_gate`) at the moment it cancels the gate.
- The dashboard's supervisor sweep must resolve and compact under one continuously held lock
  (`reconcile_and_compact`) so that a consume which won the lock stays terminal.

Neither can be moved to the other process without moving the decision it implements. So this is the
one log where locking is the whole mechanism rather than the backstop behind an owner — which is
what it already was before this leaf, and why its pre-existing `flock` was the right call kept
rather than a habit inherited.

That shows in the numbers, which are quoted on the authority of the source that carries them rather
than asserted here as independently checkable. The `durable_store.py` module docstring records this
store — the one that already took a lock — losing **0.00 percent** at the base commit while the five
unlocked stores lost records. Of the six base-commit figures in that docstring, only two are
corroborated elsewhere in the tree (31.45 percent on attention dismissals, 11.50 percent on gate);
this store's 0.00 percent and the 9.20 percent floor of the other five appear at that one site and
nowhere else. The claim that survives without any of them is the structural one: this is the only
store that held a lock at the base commit, and it is the only one that lost nothing.

### 260731-EFA-L5 What Changed Here (historical milestone)

The store's hand-rolled I/O was replaced by the shared contract, with no change to its concurrency
semantics:

- `_exclusive_access` no longer opens its own lockfile and calls `fcntl` directly; it wraps
  `durable_store.exclusive_access(self.log_path(), OPERATOR_INBOX_OWNERSHIP)`. The `import fcntl`
  and the `operator-inbox.lock` path construction are gone from this module. **The lockfile
  basename changed** as a consequence: `lock_path_for` derives it from the log, so it is now
  `operator-inbox.jsonl.lock` rather than `operator-inbox.lock`.
- `append` additionally calls `OPERATOR_INBOX_OWNERSHIP.check_declared_writer()` before taking the
  lock. Since both processes are declared writers, this raises for neither; it exists so that a
  *third* writer appearing inside either daemon fails loudly.
- `_append_unlocked` delegates to `append_line`, which now fsyncs before the handle closes.
- `_replace_unlocked` delegates to `rewrite_lines`: **it no longer unlinks** when the kept set comes
  out empty, and it no longer builds `<log>.tmp`. The old unlink let an appender holding an
  `"a"`-mode handle write into an inode with no remaining links, and the old shared temp name let
  two rewriters collide.
- `_read_unlocked` keeps its **strict** read. An inbox row that cannot be parsed is an ack nobody
  can account for, and `consume` decides on this fold. Every rewrite in this store therefore reads
  strictly, so a compaction can never erase a row it could not parse.

The lock's filesystem is now verified rather than assumed: `exclusive_access` proves once per
lockfile that `flock` on that path actually excludes, and refuses an NFS, SMB or WSL DrvFs
coordination root with `UnsafeLockFilesystemError` instead of silently degrading to a no-op.

`OperatorInboxEntry` inherits `DurableRecord` through `OperatorInboxCompatibleRecord`, so it picks
up the validated `schemaVersion` (unknown major rejected, unknown minor accepted) while keeping its
own `extra="allow"` forward-compatibility allowlist.

### 260712-TRH-L5 Same-Lock Confirmed-Gone Reconciliation (historical milestone)

`reconcile_and_compact` owns one authoritative inbox transaction: it reads and folds the
append-only log once, invokes the bounded resolver while the POSIX lock is held, appends
`ladder-resolved` snapshots for still-pending ids, and compacts before returning the folded
current used by redelivery selection. A concurrent consume that wins the lock remains
authoritative, while stale pending snapshots cannot outrank the terminal-dominant fold.
The returned `removed` count is the persisted folded-id delta, excluding transient terminal
snapshots that were appended only inside the transaction. The resolver callback must not call
back into this store. Since 260731-EFA-L16 the catalog evidence is fetched BEFORE the lock is
taken (the supervisor pre-fetches `catalog.list(include_terminated=True)` and the callback
consumes that snapshot): holding this lock across another store's read was one half of the
2026-08-05 ABBA deadlock. The exclusive lock is now intentionally held only across the remaining
tmux evidence, with a worst-case 5-second tmux timeout.

### 260707-HFX2-L20 Consume And Delivery Race (historical milestone)

`current()` now projects the append-only log through the shared terminal-dominant fold. Public
consume retains its consumed snapshot instead of immediately deleting the id, so an in-flight
delivery that finishes from an older pending snapshot cannot make the row pending or redeliverable
again. Explicit dashboard dismissal still uses physical `delete`, and normal compaction owns audit
expiry.

### Mutation Parameter Objects (260731-EFA-L2)

Three frozen objects define this store's mutating calls, plus one shared helper:

- **`AdapterReceipt(delivery_state=None, request_id=None, vendor_correlation_id=None,
  accepted_at=None, detail=None)`** — what the vendor adapter reported about one delivery attempt.
  One receipt per attempt; the fields are never sourced independently.
- **`DeliveryAttempt(delivery_state, delivered_to_session=None, detail=None,
  adapter=AdapterReceipt())`** — one attempt to put a pending row in front of its addressee.
  a delivered transport state alone is not terminal; correlated acknowledgement can land the row, and all non-pending terminals end the schedule.
- **`InboxRenewal(response=None, subject=InboxSubject(), readdress_to=None)`** — what a re-firing
  condition refreshes on the row it already has. **Passing `readdress_to` IS the readdress** —
  the former `readdress: bool` flag beside three loose `owner_*` values is gone, so there is no
  longer a way to pass an owner without readdressing or to readdress to nothing.
- **`_readdress_fields(owner)`** — the module-private mapping from an `InboxOwner` to the six
  fields a readdress rewrites (`recipientRole`/`agentId`/`lifecycleId` and
  `ownerRole`/`ownerAgentId`/`ownerLifecycleId`). `advance_rung` and `renew` share it, so the
  delivery address and the routed owner can no longer drift apart between the two paths.

`InboxOwner` and `InboxSubject` are imported from `operator_inbox_records.py`.

### 260707-HFX2-L17 Pair-Preserving Renewal (historical milestone)

`renew` can refresh `seatRole` with `leafKey` and subject identity (all three now on
`InboxRenewal.subject`) when one coalesced supervisor condition re-fires. Pair identity therefore
survives readdressing to a replacement manager and prevents same-text findings for different roles
from becoming one row.

### 260707-HFX2-L14 Transition And Readdress Mutations (historical milestone)

`advance_rung` atomically stamps `ts`, `rung`, `escalatedAt`, and `rungTransitionAt`, so every
successful transition resets both the ordinary dwell and redundant minimum-floor anchors. `renew`
can refresh `leafKey`/`subjectAgentId` and, when a `readdress_to` owner is supplied, rewrite both
direct and owner addresses to the currently resolved manager while keeping the same durable row id.
Normal renewal does not touch either rung anchor.

### Logic

The older method signatures and transition descriptions below are historical API context; the current persistence/transition split and terminal acknowledgement semantics are stated at the start of Code Commentary. They do not authorize restoring removed leaf-address fields or escalation behavior.

`OperatorInboxStore(observer_root)` writes one workspace log:
`workspace/operator-inbox.jsonl`. `append(record)` creates the parent directory
and appends a strict JSON snapshot. `read()` validates each JSONL row back into
`OperatorInboxEntry`, and `current()` folds by entry id with terminal snapshots dominating stale pending ones.

`list_pending(lifecycle_id, agent_id, recipient_role)` requires at least one
mailbox key, then returns pending entries matching every supplied key. That means
a lifecycle poll, an agent poll, a role poll, or a combined poll all use the same
log without duplicating entries. `record_delivery(entry_id, attempt, *, now, current=None,
redelivery_floor_seconds=None)` appends a delivery-state
snapshot for a queued message. `consume(entry_id, ...)` appends one consumed snapshot and
returns `(entry, True)` the first time; repeated consumes return the existing
consumed entry with `False`.

Task 23/24 added physical cleanup. `delete(entry_id)` removes all snapshots for
one inbox entry, `delete_by_gate(gate_id)` removes entries associated with a
cleared/dismissed gate, and `compact(now=...)` prunes consumed or 24h-expired
entries through `interaction_retention.inbox_keep_ids`. The public consume tool keeps the terminal
snapshot until normal compaction so concurrent stale delivery writes cannot erase the acknowledgement.

260707-HFX2-L1 (R1/R3 ack semantics + redelivery): `record_delivery(...)` now
bumps `attemptCount`, stamps `lastAttemptAt`, and schedules a durable
`nextAttemptAt` (via `inbox_backoff.next_attempt_at`) on EVERY attempt,
including a transport-delivered attempt; current correlated boundary acceptance can land the row and terminate redelivery independently of consume.
`list_redeliverable(now=..., rate_limit_seconds=...)` selects pending rows past
their backoff window and clear of the per-target rate limit
(`inbox_backoff.redeliverable`) -- the pure selection L2's sweep drives
redelivery from; this store itself never redelivers on its own (no in-memory
timer). `mark_escalated(entry_id, now=...)` stamps the reserved `escalatedAt`
field the ladder (HFX2-L4) will set -- this store only reserves the transition.
HFX2-L10 extends that path with the 900-second production floor: `record_delivery` accepts
`redelivery_floor_seconds` and passes it into `next_attempt_at`, while `list_redeliverable` still
defaults through `inbox_backoff.DEFAULT_RATE_LIMIT_SECONDS` when the caller supplies no override.
Below-floor values are refused in `inbox_backoff`, not silently shortened here.

260707-HFX2-L4 (R1/R2, the ladder's own transition): `advance_rung(entry_id, *, rung, now,
readdress_to=None, current=None)` stamps
the ladder's next rung AND re-anchors `escalatedAt` to `now` in the SAME snapshot, so the next
rung's SLA/dwell check is measured from this transition, not the row's original creation. Distinct
from `mark_escalated` (HFX2-L2's reserved, rung-agnostic "this row is now escalatable" stamp) —
`escalation_ladder`/`serving/supervisor.py`'s `_escalate_rung` is the only caller of `advance_rung`.

260707-HFX2-L8 adds sweep-scale operation support and the ladder terminal state. `record_delivery`,
`list_redeliverable`, `mark_escalated`, and `advance_rung` accept an optional folded `current`
snapshot so the supervisor can reuse one in-sweep index instead of refolding
`operator-inbox.jsonl` once per finding. `mark_ladder_resolved(entry_id, now, reason, current=...)`
appends a `state="ladder-resolved"` snapshot, clears `nextAttemptAt`, and reports whether this call
performed the terminal transition. `compact(now=...)` prunes those ladder-resolved ids through the
shared retention policy, bounding the log after a fleet of retired seats has terminated.

### Conventions

The store follows the gate store's append/read/fold pattern, but uses a shared
workspace inbox log because external chats and orchestration agents may address
by lifecycle, agent, role, or combinations of those keys.

### Invariants And Boundaries

- Current state is a fold while entries are pending; consumed/dismissed/expired
  entries are throwaway interaction data and can be physically removed.
- A `ladder-resolved` row is terminal but not acked; it is excluded from redelivery and eligible for
  compaction.
- Delivery scheduling may inherit the store default or take a caller floor, but the effective floor is
  validated in `inbox_backoff` and cannot be below 900 seconds.
- Polling without `lifecycle_id`, `agent_id`, or `recipient_role` is invalid
  because it has no mailbox boundary.
- This store owns persistence only; MCP payload shapes and attribution routing
  live in `mcp/tools/operator_inbox.py`.
- **No single compaction owner, by declaration.** `OPERATOR_INBOX_OWNERSHIP.compaction_owner` is
  `None` because both processes must physically remove rows. Give this log an owner and either the
  MCP loses its gate-cancel row deletion or the dashboard loses its same-lock resolve-and-compact
  transaction.
- **The lock is the whole mechanism here, not a backstop.** Every append and every rewrite goes
  through `_exclusive_access`. Remove it and there is no ownership rule underneath to catch the
  race — this is the one store where that is literally true.
- **`_read_unlocked` is strict, and every rewrite reads through it.** A row that cannot be parsed
  is an ack nobody can account for. Make this reader tolerant and a torn line becomes an inbox
  entry that compaction quietly deletes.
- **`_replace_unlocked` never unlinks.** An empty kept set is an empty file.

### Todos

None.

## Evidence

### Docs References

The observable-lifecycle design describes passive/active pull as the durable
return-channel family; this store supplies the durable mailbox for external
agents that cannot receive dashboard session injection.

- Pull-based return channels sit above durable gate truth and resume on the next poll/poke when push is unavailable. [1]

### Repo-Internal References

- The inbox log is `workspace/operator-inbox.jsonl`, and append/read/current preserve JSONL history. [2]
- Pending filters match supplied lifecycle and/or agent keys. [3]
- Consume is idempotent and appends a consumed snapshot only once. [4]
- Redeliverable selection is a pure filter over pending rows: it defaults the per-target rate limit to "rate_limit_seconds if rate_limit_seconds is not None else DEFAULT_RATE_LIMIT_SECONDS" and delegates the due/limit decision. [5]
- `redelivery_floor_seconds` and `next_attempt_at` are NOT in this module — the delivery-snapshot half of the old claim moved to the shared backoff module, which is also where `redeliverable` itself lives. [6]
- The strict `_read_unlocked`, the never-unlinking `_replace_unlocked`, and `_exclusive_access` now delegating to the shared contract instead of opening the module's own lockfile. [7]
- `OPERATOR_INBOX_OWNERSHIP` carries `compaction_owner=None` and states why no single owner is possible for this log. [8]

### Cross-Repo References

No meaningful cross-repo references found.

None.

#### 260713-PHA-L5 Inbox-Rooted Adapter Evidence (historical milestone)

The store records accepted, queued, rejected, unsupported, ambiguous, and terminal-completion
adapter evidence against an existing durable row. None of these transitions call `consume`.

## 260821-CLIVE Task-Execution Registration Boundary

The store identifies unregistered worker, reviewer, and curator turn reports bound to canonical
task refs. Compaction and reconcile-and-compact accept the exact registered-id set and retain every
unregistered execution report until task truth owns first-evidence proof. A missing registrar does
not authorize deletion; it fails closed. This is one retention seam, not a second task reader or a
compatibility path.
