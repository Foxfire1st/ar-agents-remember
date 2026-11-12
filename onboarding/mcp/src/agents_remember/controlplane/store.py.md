# mcp/src/agents_remember/controlplane/store.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`store.py` is the gate store: it resolves a gate snapshot's log path, appends
active snapshots as JSONL, folds current state, and can physically remove or
compact short-lived interaction gates when the retention policy says they are no
longer needed. Since 260731-EFA-L5 it also owns the one **compare-and-swap** in the
gate plane — `claim_approval`, the only way to spend a human approval.

## Code Commentary

### 260731-EFA-L5 Two Writing Processes, And The Authority They Carry

The old MCP/dashboard gate writers are historical. Today the landing chain’s `claim_approval` writes applied snapshots; shared exclusion, not session ownership, protects whole read/modify/write.

Measured 0 lost across 10 runs of all three scenarios once the contract was in place.

**This card previously drew the wrong conclusion from that, and the module docstring now names the
error explicitly.** It said: "The `applied` marker is what stops one human approval being consumed
twice, so losing it re-opens the replay window silently" — which reads as though not losing it
closed the window. It did not. **Durability of a record is not atomicity of a decision.** Three
things had to be true and only the first was:

1. **The marker must survive a concurrent rewrite.** That is the lock above — the store fix, and
   the only one of the three this file's I/O change addressed.
2. **The marker must not be reclaimed as garbage.** It was: `applied` sat in
   `interaction_retention.PRUNE_IMMEDIATE_GATE_STATES`, so the reclaim pass dropped it at any age.
   One later decision on the same lifecycle — an answered `agent-question` is enough — and the fold
   went back to permitted-gateless. Closed by `interaction_retention.CONSUMED_APPROVAL_GATE_KINDS`.
3. **The check and the write must be one step.** They were roughly a hundred lines and every commit
   of a closeout apart, with no lock across the pair, so two closeouts interleaved and both were
   permitted — reproduced with two real processes. Closed by `GateStore.claim_approval`.

Two of the three would have existed even if this store had never lost a byte. Read them together: a
record this store keeps perfectly is still worthless if something else deletes it on a schedule, or
if the decision it backs was already made against a stale copy.

The store now routes all file I/O through `controlplane/durable_store.py` under `GATE_OWNERSHIP`.
Appends and rewrites exclude each other through the log's own sibling lockfile, always and in every
process — **that** is what makes the loss zero. Reclamation is *named* as the MCP process's, but
that naming is advisory: it is silent in any process that declared no role, and the durability does
not rest on it.

### 260731-EFA-L5 R2 `claim_approval` Is Now The Only Way To Spend An Approval

`claim_approval(lifecycle_id, *, kind, now, policy=DEFAULT_GATE_POLICY, operation_key=None) -> GateGuard` atomically binds approval to a mutation, and
everything this card used to say about how an approval is consumed is superseded by it. The fold
(`current`), the policy verdict (`enforcement.evaluate_gate`) and the `applied` append all happen
inside **one held `exclusive_access`**, so `approved -> applied` is atomic against every other
writer of this log: exactly one caller can see the gate approved and be the one that marks it
consumed. A later caller reads the `applied` snapshot. A different or absent operation key refuses; the same non-null key matching `appliedOperation` may recover the already-bound operation without appending another applied snapshot. An absent gate log is evaluated as an empty gate set before opening the lock, so an ordinary gateless claim creates no lock-only lifecycle directory. This changes neither existing-log claim serialization nor the boundary between durable approval consumption and subsequent Git work.

**The unsafe primitive was deleted, not deprecated.** `worktrees/modules/closeout.py`'s
`_mark_closeout_gate_applied` — a bare `current()` read followed by an unlocked `append(apply_gate(...))`,
run at the very end of a closeout — is gone from the tree. There is no transition period and no
second path: the only thing in this module that writes an `applied` snapshot for an enforcement
path is `claim_approval`.

Why a lock around a *decision* and not only around a write: `read` takes no lock and `append` locks
only its own byte-write, so the check-then-act pair that used to straddle a whole closeout
interleaved freely. Measured with two real processes and a 0.4s body, both closeouts were permitted,
two `applied` snapshots landed on disk, and one approval was spent twice. Neither end was losing a
record; both ends were reading a fold that stopped being true before it was used.

Two behaviours are deliberately preserved rather than tightened. The **gateless verdict**
(`permitted` with `gate_id is None`) claims nothing and writes nothing — a lifecycle with no gate of
this kind is still governed by the chat/commit approval channel, so the additive fallback survives.
A **refusal likewise writes nothing**: an approval is only ever consumed on the path that was
permitted to consume it. `now` is the caller's stamp, so the append stays a pure function of what
was read.

The `append` inside the held lock is **re-entrant on purpose**: `exclusive_access` recognises the
same thread re-taking the same lock rather than deadlocking, so the write keeps its
`check_declared_writer` check instead of being open-coded to dodge the nesting.

### 260731-EFA-L5 Reads Are Deliberately Not Uniform

`read` is **strict** and raises on a torn or unknown-major line. It backs `current`, `find` and
`all_current` — the retained landing enforcement fold consults before a mutation. Skipping a malformed record there could
drop an `applied` marker and let the fold conclude the approval was never consumed.

`read_for_projection` is **tolerant** and skips the bad line. It backs the retained `projected_current` helper, not an approval decision. A tolerant read never writes back what it read, so
a skipped line is skipped for one tick and no longer.

**Every rewrite of this log reads strictly**: both `delete` and `compact` take their record list
from `read`, not from `read_for_projection`. That is the property that makes two policies safe
rather than merely different — a compaction can never be the thing that erases a gate record it
could not parse.

`schemaVersion` needs no version branch in either reader: `GateRecord` now inherits `DurableRecord`
and validates the version on the way in, so an unknown major raises `ValidationError` — the strict
reader surfaces it, the tolerant reader skips it.

### 260731-EFA-L5 Compaction Moved To The Owner

`projected_current(lifecycle_id, now=...)` remains a tolerant in-memory keep-filter, never a rewrite or current projection/TTL job. No clock means no helper age filter.

`compact` remains a locked strict-read/filter/rewrite primitive. No product decision or periodic age-reclamation loop is restored by retaining it; explicit `removed-stores` owns deletion of stored gate logs.

Applied consumed approvals have no TTL; explicit cleanup never mistakes approval history for terminal lock-only residue.

`_replace` no longer unlinks an emptied log, no longer builds `<log>.tmp`, and no longer calls
`os.replace` itself; it delegates to `durable_store.rewrite_lines`, which refuses unless the calling
thread holds the log's lock.

### 260707-HFX2-L12 CS-6 Update

`GateStore.compact_current()` combined the gate keep-filter and current-fold in one read, with
physical rewrite gated by the caller. Projection could then read each gate log once per tick while
still seeing expired/consumed rows filtered out. **Superseded by 260731-EFA-L5**: the method is
gone. `projected_current` keeps the single read and the in-memory keep-filter; the `rewrite`
parameter and the physical prune it drove were removed, because that prune ran in the process that
owns nothing here.

`GateStore(observer_root)` holds the observer root. `log_path(lifecycle_id)`
routes to `lifecycles/<id>/gates.jsonl` or `workspace/gates.jsonl` for unscoped retained records; the old per-session event file no longer exists. `append(record)` creates parent
dirs on first write and appends `record.model_dump_json(by_alias=True,
exclude_none=True)`. `read(lifecycle_id)` validates the log back into
`GateRecord`s. `current(lifecycle_id)` folds the log by gate id, last snapshot
wins.

Task 23/24 added real deletion/compaction. `delete(gate_id, lifecycle_id)`
rewrites the log without that gate id, `compact(lifecycle_id, now=...)` removes
expired/open-too-long or already-consumed interaction gates according to
`interaction_retention.gate_keep_ids`, and `lifecycle_ids()` enumerates gate logs
for retained gate-log folds, not a current projection-time TTL cleanup job. Rewrites were atomic tmp-write + `os.replace`, and empty logs
were unlinked — **both superseded by 260731-EFA-L5**. Rewrites now go through
`durable_store.rewrite_lines`, which holds the caller to the log's lock, uses a pid-scoped hidden
temp name, fsyncs the temp and the parent directory, and **never unlinks**: an empty kept set is
written as an empty file, so a concurrent appender holding an `"a"`-mode handle can no longer write
into an inode with no remaining links.

## Invariants And Boundaries

- **Append while active; compact when consumed — except for the kinds a mutating tool consumes.**
  Gate history is preserved while a gate is active or waiting for a consuming tool, and
  retained helper compaction is not automatic age reclamation or session UI cleanup. The earlier
  "and applied handoffs" half of this invariant is **retracted**: since 260731-EFA-L5 an `applied`
  snapshot whose kind is in `interaction_retention.CONSUMED_APPROVAL_GATE_KINDS` is retained with
  **no TTL at all**, because it is the whole and only proof that a human approval was spent.
  `compact` still drops every other kind's `applied` row immediately.
- **`claim_approval` is the only way to spend an approval, and there is no other path left.**
  The fold, the policy verdict and the `applied` append are one held lock. A gateless verdict and a
  refusal both write nothing. `_mark_closeout_gate_applied` was deleted rather than deprecated, so
  no caller can reach the old check-then-act shape by accident.
- **An approval binds one mutation operation, not one success.** The claim precedes the first irreversible act. Failure leaves the approval applied; a different mutation needs a fresh gate, while recovery under the same non-null operation key is admitted without spending it again. The earlier unconditional fresh-gate requirement is superseded by operation-bound recovery.
- **Exclusion, not a session-owner assumption:** every append and whole-read/rewrite takes the shared durable lock. Historical MCP/dashboard gate writers are not the current roster. Approval consumption is not atomic execution of later Git work.
- **`read` is strict, `read_for_projection` is tolerant, and every rewrite reads strictly.**
  `delete` and `compact` both take their record list from `read`, so a compaction can never erase a
  gate record it could not parse. Point either rewrite at the tolerant reader and a torn line
  becomes a silently deleted gate snapshot.
- **The lock is held across the read and the rewrite, not around the rewrite alone.** `delete` and
  `compact` open `exclusive_access` before reading and close it after `_replace`.
  `rewrite_lines` raises `DurableStoreError` if a caller has not done this.
- Co-located with the event substrate under `observer_root`; no new storage root.

## Evidence

### Repo-Internal References

- The gate envelope serialized and validated here. [1]

- Mirrors the observer event store (same append / read / JSONL shape). [2]


- The `ar-durable-store/1.0` contract this store routes every append and rewrite through: `exclusive_access`, `append_line`, `rewrite_lines`, `read_log_text`, and `GATE_OWNERSHIP`, which names the MCP process the compaction owner and the MCP, dashboard and lifecycle-operation roles as declared writers.  Anchor: `exclusive_access`, `append_line`, `rewrite_lines`, `read_log_text`, `GATE_OWNERSHIP` [3]

- `CONSUMED_APPROVAL_GATE_KINDS` and `_keep_gate`'s authority branch: what stops `compact` from reclaiming the `applied` snapshot this store's atomicity exists to protect. [5]


- `evaluate_gate` is the pure verdict taken under the lock. An already-applied gate refuses a different/absent operation key but admits the same non-null `appliedOperation` recovery without another spend. [6]



- `_claim_closeout_gate` consumes approval under the gate-store lock; its closeout call site precedes journaled mutation intent and Git. Approval consumption does not itself prove mutation or retain a generation. [7]


As of cycle 5 GateStore.find(gate_id) resolves one gate id across the workspace log and every lifecycle log — the seam-decide path: the deciding seat holds only the packet-carried gate id; lifecycle ids stay server-side. Cycle 6 adds `all_current()`, the cross-lifecycle enforcement fold: it merges every gate log (workspace + all lifecycles) last-wins per gate id, so identity-addressed consumers (the integrate-side master-handover guard, which matches by the gate's `enclosure`) can see a seam gate raised on a different lifecycle than the one the consuming contract anchors.

## Open Decision: The Handover Gate Is Guarded But Never Consumed

`worktrees/modules/integrate.py` **never consumes the `master-handover-approval` gate at all.**
`integrate_result` folds `all_current()`, evaluates `handover_gate_guard`, refuses when the verdict
is not permitted, and integrates — with no `apply_gate` and no `claim_approval` anywhere in the
module. This is **not** a record this leaf dropped and not a regression: the consume was never
written, on any commit. It is left open deliberately, for two reasons a reader needs before
"fixing" it:

- **It needs a different key from `claim_approval`'s.** That gate is matched *cross-lifecycle* by
  `enclosure` against the contract's `task_name`/`parent_task_name`, and it lives on a different log
  than the integrating lifecycle's — so a claim keyed on `(lifecycle_id, kind)`, which is what
  `claim_approval` takes, cannot address it.
- **Closeout's `integration_reopen` path means a legitimate re-integration exists.** Consuming the
  gate on the first integration would make a re-integration of newly transported content start
  demanding a fresh handover approval, which nobody has decided is correct.

The retention half is already ready: `master-handover-approval` is in
`interaction_retention.SEAM_CONSUMED_GATE_KINDS` and therefore in `CONSUMED_APPROVAL_GATE_KINDS`, so
an `applied` snapshot of that kind would already be retained with no TTL the moment something writes
one. Until then the handover gate is a *guard* (a permitted/refused read) and not a *spend*, and
nothing prevents the same approved handover gate from permitting two integrations.

## Current Durable-Store Lock Composition

Every gate append and read-filter-rewrite still uses the durable-store boundary. That boundary
first validates the checkout coordination target, then acquires the shared kernel file lock;
lock-capability failures retain the durable-store error family. Advisory compaction ownership
does not replace exclusion or the checkout guard.


- Durable exclusion guards the checkout target before invoking shared kernel locking and preserves typed unsafe-filesystem refusal. [9]
