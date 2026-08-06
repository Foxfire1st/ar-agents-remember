# mcp/src/agents_remember/controlplane/operator_inbox_store.py

| Field                  | Value                                                             |
| ---------------------- | ----------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/src/agents_remember/controlplane/operator_inbox_store.py`    |
| doc_type               | `file-level-onboarding`                                           |
| lastUpdated            | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash |                                                                   `a3e43cb0877c18b9d2b0e6ada4eb5719a01f251f`|
| lastVerifiedCommitDate |                                                                   2026-08-06T05:49:07+02:00|
| governingOverview      | `overview.md`                                                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

File-backed operator inbox store for short-lived polling plus hosted-session
delivery metadata.

## Code Commentary

### 260731-EFA-L5 The Declared Compaction-Owner Exception

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

### 260731-EFA-L5 What Changed Here

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

### 260712-TRH-L5 Same-Lock Confirmed-Gone Reconciliation

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

### 260707-HFX2-L20 Consume And Delivery Race

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
  `delivered` is not terminal (pasted != perceived); only a consume ends the schedule.
- **`InboxRenewal(response=None, subject=InboxSubject(), readdress_to=None)`** — what a re-firing
  condition refreshes on the row it already has. **Passing `readdress_to` IS the readdress** —
  the former `readdress: bool` flag beside three loose `owner_*` values is gone, so there is no
  longer a way to pass an owner without readdressing or to readdress to nothing.
- **`_readdress_fields(owner)`** — the module-private mapping from an `InboxOwner` to the six
  fields a readdress rewrites (`recipientRole`/`agentId`/`lifecycleId` and
  `ownerRole`/`ownerAgentId`/`ownerLifecycleId`). `advance_rung` and `renew` share it, so the
  delivery address and the routed owner can no longer drift apart between the two paths.

`InboxOwner` and `InboxSubject` are imported from `operator_inbox_records.py`.

### 260707-HFX2-L17 Pair-Preserving Renewal

`renew` can refresh `seatRole` with `leafKey` and subject identity (all three now on
`InboxRenewal.subject`) when one coalesced supervisor condition re-fires. Pair identity therefore
survives readdressing to a replacement manager and prevents same-text findings for different roles
from becoming one row.

### 260707-HFX2-L14 Transition And Readdress Mutations

`advance_rung` atomically stamps `ts`, `rung`, `escalatedAt`, and `rungTransitionAt`, so every
successful transition resets both the ordinary dwell and redundant minimum-floor anchors. `renew`
can refresh `leafKey`/`subjectAgentId` and, when a `readdress_to` owner is supplied, rewrite both
direct and owner addresses to the currently resolved manager while keeping the same durable row id.
Normal renewal does not touch either rung anchor.

### Logic

`OperatorInboxStore(observer_root)` writes one workspace log:
`workspace/operator-inbox.jsonl`. `append(record)` creates the parent directory
and appends a strict JSON snapshot. `read()` validates each JSONL row back into
`OperatorInboxEntry`, and `current()` folds by entry id, last snapshot wins.

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
including a confirmed `delivered` paste -- consume is the only call that stops
the schedule, because `delivered` is never terminal (pasted != perceived).
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

## Docs References

The observable-lifecycle design describes passive/active pull as the durable
return-channel family; this store supplies the durable mailbox for external
agents that cannot receive dashboard session injection.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pull-based return channels sit above durable gate truth and resume on the next poll/poke when push is unavailable. | `# Observable Lifecycle, Events, and Gates — the Agents Remember 3.0 Design` | docs/design/observable-lifecycle.md:1-402 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The inbox log is `workspace/operator-inbox.jsonl`, and append/read/current preserve JSONL history. | "def log_path" | mcp/src/agents_remember/controlplane/operator_inbox_store.py:63-63 |
| Pending filters match supplied lifecycle and/or agent keys. | "def list_pending" | mcp/src/agents_remember/controlplane/operator_inbox_store.py:82-82 |
| Consume is idempotent and appends a consumed snapshot only once. | "def consume" | mcp/src/agents_remember/controlplane/operator_inbox_store.py:127-127 |
| Redeliverable selection is a pure filter over pending rows: it defaults the per-target rate limit to `DEFAULT_RATE_LIMIT_SECONDS` and delegates the due/limit decision. | `DEFAULT_RATE_LIMIT_SECONDS` | mcp/src/agents_remember/controlplane/operator_inbox_store.py:105-125 |
| `redelivery_floor_seconds` and `next_attempt_at` are NOT in this module — the delivery-snapshot half of the old claim moved to the shared backoff module, which is also where `redeliverable` itself lives. | `require_redelivery_floor_seconds`; `next_attempt_at`; `redeliverable` | mcp/src/agents_remember/controlplane/inbox_backoff.py:42-52; mcp/src/agents_remember/controlplane/inbox_backoff.py:55-72; mcp/src/agents_remember/controlplane/inbox_backoff.py:111-124 |
| The strict `_read_unlocked`, the never-unlinking `_replace_unlocked`, and `_exclusive_access` now delegating to the shared contract instead of opening the module's own lockfile. | `_read_unlocked`; `_replace_unlocked`; `_exclusive_access`; `fcntl` | mcp/src/agents_remember/controlplane/operator_inbox_store.py:230-238; mcp/src/agents_remember/controlplane/operator_inbox_store.py:240-245; mcp/src/agents_remember/controlplane/operator_inbox_store.py:247-251; mcp/src/agents_remember/providers/provider_setup.py:22-22 |
| `OPERATOR_INBOX_OWNERSHIP` carries `compaction_owner=None` and states why no single owner is possible for this log. | `OPERATOR_INBOX_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:182-198 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

### 260713-PHA-L5 Inbox-Rooted Adapter Evidence

The store records accepted, queued, rejected, unsupported, ambiguous, and terminal-completion
adapter evidence against an existing durable row. None of these transitions call `consume`.

## Update History

- 2026-08-05T19:26+02:00 — 260731-EFA-L16 curator: corrected the TRH-L5 lock-held-evidence
  statement — the catalog read left the lock (pre-fetched by the supervisor before
  `reconcile_and_compact`); only the bounded tmux snapshot remains lock-held. Consume authority and
  the same-lock resolve/compact rationale are unchanged. Verification metadata stays pinned until
  closeout stamps the L16 commit.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact anchors, deduplicated the backoff row, and converted the history pending/consume citations;
  exact non-fixing check returns zero findings.
- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T20:15+02:00 — 260731-EFA-L5 curator (correction pass). **One stale citation and the
  leaf's least-corroborated number.** The `OPERATOR_INBOX_OWNERSHIP` row cited `durable_store.py`
  **L297-L313**; the constant is at **L368** — the file grew 598 → 699 lines mid-pass, so every
  range written earlier is off. Replaced with a symbol-name citation and no range. Re-read the five
  citations into this module's own source and left them: the log-path/append/read row L109-L126
  (`log_path` L109, `append` L113, `read` L119, `current` L124), pending filters cit:(["def list_pending"], mcp/src/agents_remember/controlplane/operator_inbox_store.py:82-82), `consume`
  cit:(["def consume"], mcp/src/agents_remember/controlplane/operator_inbox_store.py:127-127), the delivery-snapshot pair L151-L204; L234-L254, and the
  `_read_unlocked` / `_replace_unlocked` / `_exclusive_access` row L468-L492 (L471, L481, L489). The
  **0.00 percent** claim is now attributed rather than asserted as a measurement a reader can check:
  it appears only in the `durable_store.py` docstring, as does the 9.20 percent that the old
  "9.20 to 31.45 percent" range leaned on. Only 31.45 percent and 11.50 percent are carried at
  several independent sites. The structural claim that needs no figure is stated instead and is the
  one that actually carries the card: this was the only store holding a lock at the base commit and
  the only one that lost nothing. This card's read-policy statements were already correct — strict
  `_read_unlocked`, and every rewrite in this store reading through it — and were left unchanged.
- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Recorded this store as the
  leaf's **declared compaction-owner exception**: `OPERATOR_INBOX_OWNERSHIP.compaction_owner` is
  `None` because both processes must physically remove rows — the MCP deletes a cancelled gate's
  rows via `delete_by_gate`, the dashboard resolves and compacts under one held lock in
  `reconcile_and_compact` — and neither move travels without the decision it implements. It is
  therefore the one log where locking rather than ownership is the whole mechanism, and it was the
  only one of six to measure 0.00 percent loss at the base commit. Recorded the I/O migration:
  `_exclusive_access` now wraps `durable_store.exclusive_access` (the local `import fcntl` and the
  `operator-inbox.lock` path are gone, and the lockfile basename is consequently now
  `operator-inbox.jsonl.lock`), `append` adds `check_declared_writer`, `_append_unlocked` fsyncs
  through `append_line`, and `_replace_unlocked` delegates to `rewrite_lines` so it no longer
  unlinks an emptied log or shares a `<log>.tmp` name. Recorded that `_read_unlocked` stays strict
  and that every rewrite in this store therefore reads strictly. Repaired all four pre-existing
  line citations, which this leaf's edits had pushed down the file. Verification metadata pinned
  until closeout stamps the L5 commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 line citations that the parameter-object
  refactor pushed down the file. Log/append/read/current is now L92-L108 (`log_path` through
  `current`), consume is L350-L372, and the delivery-floor claim splits into L133-L186
  (`record_delivery` threading `redelivery_floor_seconds` into `next_attempt_at`) plus L216-L236
  (`list_redeliverable` defaulting to `DEFAULT_RATE_LIMIT_SECONDS`). All four spans read back.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `AdapterReceipt`, `DeliveryAttempt` and `InboxRenewal` parameter objects plus
  the shared `_readdress_fields(owner)` helper, and re-signed three mutators:
  `record_delivery(entry_id, attempt, *, now, ...)` (eight delivery/adapter keywords collapsed
  into `attempt`), `advance_rung(entry_id, *, rung, now, readdress_to=None, current=None)` and
  `renew(entry_id, renewal, *, now, current=None)`. The `readdress: bool` + three `owner_*`
  keywords were replaced on both by an optional `InboxOwner` — supplying it *is* the readdress,
  which removes the pass-an-owner-without-readdressing and readdress-to-nothing states. The two
  readdress paths now write the same six fields through one helper. Written snapshots are
  unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: refreshed correlated delivery and explicit-consumption separation.

- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: documented one-fold resolve-plus-compact
  ordering, consume authority, persisted folded-id removal semantics, and the no-store-reentry
  callback contract under the shared inbox lock. Verification metadata remains pinned until
  closeout stamps the candidate commit.

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20: made current-state folding terminal-dominant and kept
  consumed snapshots append-only until compaction, closing the live resurrection/redelivery race.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: made coalesced inbox renewal preserve the current
  leaf-role subject pair through owner readdressing.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: made rung advancement stamp both dwell anchors
  and allowed coalesced supervisor rows to preserve chain fields and readdress the current manager.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: threaded the effective 900-second redelivery floor
  through `record_delivery(..., redelivery_floor_seconds=...)` and preserved the shared default for
  `list_redeliverable`. Verification metadata pinned until closeout stamps the 260707-HFX2-L9
  commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8: added optional snapshot-aware mutation/selection paths,
  `mark_ladder_resolved`, and compaction of ladder-resolved terminal ids so supervisor sweeps avoid
  per-finding log folds and dead-seat storms leave bounded inbox logs. Verification metadata pinned
  until closeout stamps the HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (R1/R2, escalation ladder): added `advance_rung` — stamps
  the ladder's next rung and re-anchors `escalatedAt` in the same snapshot, distinct from HFX2-L2's
  rung-agnostic `mark_escalated`. `serving/supervisor.py::_escalate_rung` is the sole caller.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T14:00+02:00 — 260707-HFX2-L1: R1 ack semantics (attempt/backoff
  fields on `record_delivery`, delivered is never terminal) + R3 redelivery
  (`list_redeliverable`, `mark_escalated`), reusing the `inbox_backoff` module's
  pure math. Verification metadata pinned until closeout stamps the
  260707-HFX2-L1 commit.
- 2026-07-04T12:31+02:00 - L3: added recipient-role pending filters and
  `record_delivery(...)` snapshots so hosted push outcomes stay attached to the
  durable inbox row. Verification metadata pinned until closeout stamps the L3
  commit.
- 2026-06-25T13:10+02:00 — Task 23/24: added delete, delete-by-gate, and compaction so consumed/dismissed/expired operator-inbox entries do not accumulate forever.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: append-only workspace inbox store with lifecycle/agent pending filters and idempotent consume. Verification metadata pinned until closeout stamps the task-10 code commit.
