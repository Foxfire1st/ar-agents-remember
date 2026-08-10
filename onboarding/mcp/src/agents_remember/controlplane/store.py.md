# mcp/src/agents_remember/controlplane/store.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/controlplane/store.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T19:45+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`       |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

`store.py` is the gate store: it resolves a gate snapshot's log path, appends
active snapshots as JSONL, folds current state, and can physically remove or
compact short-lived interaction gates when the retention policy says they are no
longer needed. Since 260731-EFA-L5 it also owns the one **compare-and-swap** in the
gate plane — `claim_approval`, the only way to spend a human approval.

## Code Commentary

### 260731-EFA-L5 Two Writing Processes, And The Authority They Carry

This log has **two** writing processes, and the docstring that used to claim "one writer per file
in practice, because a lifecycle is owned by one live session" was false on both counts. The MCP
server mints, decides, applies and deletes gates; the dashboard raises and resolves
`agent-question` gates for adapter-owned sessions (`serving/hosted_interactions.py`) and its entire
purpose is to decide gates for lifecycles owned by other sessions. A third participant, the
compactor, ran on the dashboard's 30-second projection tick. Measured cost of believing the
docstring: **11.50 percent** of appended gate snapshots lost under ordinary two-process operation
at the base commit, and 100 percent in the deterministic forced-window scenario. Zero torn lines —
records disappeared whole, which is why no reader-side validation could ever have caught it.

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

`claim_approval(lifecycle_id, *, kind, now, policy=DEFAULT_GATE_POLICY) -> GateGuard` is new, and
everything this card used to say about how an approval is consumed is superseded by it. The fold
(`current`), the policy verdict (`enforcement.evaluate_gate`) and the `applied` append all happen
inside **one held `exclusive_access`**, so `approved -> applied` is atomic against every other
writer of this log: exactly one caller can see the gate approved and be the one that marks it
consumed. A second caller arriving while the first holds the lock reads the `applied` snapshot and
is refused with the already-applied reason.

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
`all_current` — the enforcement fold `serving/hosted_interactions.py` and
`worktrees/modules/integrate.py` consult before a mutation. Skipping a malformed record there could
drop an `applied` marker and let the fold conclude the approval was never consumed.

`read_for_projection` is **tolerant** and skips the bad line. It is new in this leaf and is used by
`projected_current` and by nothing that decides. A tolerant read never writes back what it read, so
a skipped line is skipped for one tick and no longer.

**Every rewrite of this log reads strictly**: both `delete` and `compact` take their record list
from `read`, not from `read_for_projection`. That is the property that makes two policies safe
rather than merely different — a compaction can never be the thing that erases a gate record it
could not parse.

`schemaVersion` needs no version branch in either reader: `GateRecord` now inherits `DurableRecord`
and validates the version on the way in, so an unknown major raises `ValidationError` — the strict
reader surfaces it, the tolerant reader skips it.

### 260731-EFA-L5 Compaction Moved To The Owner

`compact_current(lifecycle_id, now=, rewrite=)` is **gone**, replaced by
`projected_current(lifecycle_id, *, now)`. The single read that HFX2-L12 introduced is kept; the
rewrite that used to ride it is removed. The projection applies the same keep-filter in memory, so
what the dashboard renders is unchanged — but reclaiming the log on the projection tick was
compaction running in a process that owns nothing here, and it was the source of the measured loss.
`now=None` folds without the retention filter, which is what a caller holding no clock has always
been given.

Physical reclamation is `compact`, driven from `mcp/tools/gates.py::_reclaim_gate_log` after a gate
decision, guarded by `GATE_OWNERSHIP.is_compaction_owner()`.

**Accepted behavioural consequence:** gate reclamation now follows owner activity rather than a
wall clock. A gate raised and expired by the dashboard is reclaimed on the next MCP decision on
that lifecycle, rather than within 30 seconds. Space-only, never correctness — the projection is
keep-filtered every tick regardless of what is still on disk.

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
routes to `lifecycles/<id>/gates.jsonl` beside that lifecycle's `events.jsonl`,
or `workspace/gates.jsonl` when lifecycle-less. `append(record)` creates parent
dirs on first write and appends `record.model_dump_json(by_alias=True,
exclude_none=True)`. `read(lifecycle_id)` validates the log back into
`GateRecord`s. `current(lifecycle_id)` folds the log by gate id, last snapshot
wins.

Task 23/24 added real deletion/compaction. `delete(gate_id, lifecycle_id)`
rewrites the log without that gate id, `compact(lifecycle_id, now=...)` removes
expired/open-too-long or already-consumed interaction gates according to
`interaction_retention.gate_keep_ids`, and `lifecycle_ids()` enumerates gate logs
for projection-time TTL cleanup. Rewrites were atomic tmp-write + `os.replace`, and empty logs
were unlinked — **both superseded by 260731-EFA-L5**. Rewrites now go through
`durable_store.rewrite_lines`, which holds the caller to the log's lock, uses a pid-scoped hidden
temp name, fsyncs the temp and the parent directory, and **never unlinks**: an empty kept set is
written as an empty file, so a concurrent appender holding an `"a"`-mode handle can no longer write
into an inode with no remaining links.

## Invariants And Boundaries

- **Append while active; compact when consumed — except for the kinds a mutating tool consumes.**
  Gate history is preserved while a gate is active or waiting for a consuming tool, and
  dismiss/clear/TTL still physically remove throwaway interaction rows. The earlier
  "and applied handoffs" half of this invariant is **retracted**: since 260731-EFA-L5 an `applied`
  snapshot whose kind is in `interaction_retention.CONSUMED_APPROVAL_GATE_KINDS` is retained with
  **no TTL at all**, because it is the whole and only proof that a human approval was spent.
  `compact` still drops every other kind's `applied` row immediately.
- **`claim_approval` is the only way to spend an approval, and there is no other path left.**
  The fold, the policy verdict and the `applied` append are one held lock. A gateless verdict and a
  refusal both write nothing. `_mark_closeout_gate_applied` was deleted rather than deprecated, so
  no caller can reach the old check-then-act shape by accident.
- **An approval authorises one attempt, not one success.** `claim_approval` is called before the
  first irreversible act of the operation it guards, so a closeout that dies after the claim leaves
  the approval spent and needs a fresh gate. This is the deliberate fail-closed trade; see
  `worktrees/modules/closeout.py`'s card for why the alternative is worse.
- **Two writing processes, not one.** The earlier "one writer per lifecycle file in practice,
  the same single-writer assumption the event store makes" is retracted: it was false, and
  believing it cost 11.50 percent of appended gate snapshots. Both the MCP process and the
  dashboard append here, and every append and every rewrite takes the log's lock in both.
- **The lock is the mechanism; the compaction owner is advisory.** `GATE_OWNERSHIP` names the MCP
  process as the owner, and `mcp/tools/gates.py::_reclaim_gate_log` asks
  `is_compaction_owner()` before reclaiming. That question never raises and is answered `True` in
  any process that declared no role. Remove the lock and the loss returns; remove the ownership
  check and a dashboard-side reclaim comes back, but no record is lost to it.
- **`read` is strict, `read_for_projection` is tolerant, and every rewrite reads strictly.**
  `delete` and `compact` both take their record list from `read`, so a compaction can never erase a
  gate record it could not parse. Point either rewrite at the tolerant reader and a torn line
  becomes a silently deleted gate snapshot.
- **The lock is held across the read and the rewrite, not around the rewrite alone.** `delete` and
  `compact` open `exclusive_access` before reading and close it after `_replace`.
  `rewrite_lines` raises `DurableStoreError` if a caller has not done this.
- Co-located with the event substrate under `observer_root`; no new storage root.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The gate envelope serialized and validated here. | `GateRecord` | mcp/src/agents_remember/controlplane/records.py:45-77 |
| Mirrors the observer event store (same append / read / JSONL shape). | `EventStore` | mcp/src/agents_remember/observer/store.py:103-171 |
| The `ar-durable-store/1.0` contract this store routes every append and rewrite through: `exclusive_access`, `append_line`, `rewrite_lines`, `read_log_text`, and `GATE_OWNERSHIP`, which names the MCP process the compaction owner and the dashboard a co-writer. Cited by symbol, not by line: this file grew ~100 lines mid-leaf and every earlier range into it was invalidated. | `exclusive_access`, `append_line`, `rewrite_lines`, `read_log_text`, `GATE_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:138-150; mcp/src/agents_remember/controlplane/durable_store.py:348-403; mcp/src/agents_remember/controlplane/durable_store.py:427-431; mcp/src/agents_remember/controlplane/durable_store.py:434-445; mcp/src/agents_remember/controlplane/durable_store.py:448-455 |
| `_reclaim_gate_log` at gate_decisions.py:74-80: the reclaim pass moved here from the projection tick, guarded by `is_compaction_owner` because the dashboard calls `gate_decide_payload` directly, and its suppression narrowed from `ValueError` to `ValidationError` — the widened-except shape this leaf closed. Called from `record_gate_decision` at gate_decisions.py:116. | `_reclaim_gate_log`, `record_gate_decision` | mcp/src/agents_remember/controlplane/gate_decisions.py:74-80; mcp/src/agents_remember/controlplane/gate_decisions.py:83-128 |
| `CONSUMED_APPROVAL_GATE_KINDS` and `_keep_gate`'s authority branch: what stops `compact` from reclaiming the `applied` snapshot this store's atomicity exists to protect. | `CONSUMED_APPROVAL_GATE_KINDS`, `_keep_gate` | mcp/src/agents_remember/controlplane/interaction_retention.py:53-55; mcp/src/agents_remember/controlplane/interaction_retention.py:184-197 |
| `evaluate_gate` — the pure verdict `claim_approval` takes under the lock, including the already-applied refusal that makes a second consume fail. | `evaluate_gate` | mcp/src/agents_remember/controlplane/enforcement.py:52-94 |
| `_claim_closeout_gate` at closeout.py:513-563: the first production caller of `claim_approval`, and its call site at closeout.py:970 — one statement above the first commit, which is what makes an approval authorise one attempt rather than one success. | `_claim_closeout_gate` | mcp/src/agents_remember/worktrees/modules/closeout.py:510-560 |
| `read_gates` at snapshots.py:513-546 now folds through the tolerant `projected_current` and rewrites nothing; its docstring records that the 30-second prune cadence this tick used to run was removed. | "def read_gates(coordination_root: Path" | mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:103-103 |

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

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:09+02:00 — 260731-EFA-L6 S18-B14 curator: removed the duplicated durable_store/gate_decisions/interaction_retention source spans from 3 citation rows and corrected the stale in-claim line literals (`_reclaim_gate_log` 74-80 called at :116, `_claim_closeout_gate` 513-563 called at :970, `read_gates` 513-546). Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 16 citation findings (8 rows); scoped recheck clean.

- 2026-08-01T19:45+02:00 — 260731-EFA-L5 second curator pass. This card was written **before**
  `claim_approval` existed and everything it said about consuming an approval was superseded by
  code that landed afterwards. Corrections: (1) retracted the sentence "losing [the `applied`
  marker] re-opens the replay window silently", which conflated durability with atomicity — replaced
  with the three-conditions framing the module docstring now carries, and stated that two of the
  three defects would have existed even if this store had never lost a byte; (2) added the
  `claim_approval` section — fold, `evaluate_gate` verdict and `applied` append inside one held
  `exclusive_access`, the gateless and refused paths writing nothing, and the re-entrant `append`;
  (3) recorded that `_mark_closeout_gate_applied` was **deleted, not deprecated**, so no second path
  to an `applied` snapshot survives; (4) retracted the "applied handoffs physically remove
  interaction rows" half of the append/compact invariant — `applied` for
  `CONSUMED_APPROVAL_GATE_KINDS` is now retained with no TTL; (5) added the one-attempt-not-one-success
  invariant; (6) added the open decision that `integrate.py` guards the `master-handover-approval`
  gate but never consumes it, with the two reasons it is left open and the note that the retention
  half is already in place. Citations: converted the `durable_store.py` row from `L256-L268` to
  symbol names (that file moved to ~699 lines mid-pass and `GATE_OWNERSHIP` is at L326, not in the
  cited range); corrected `_reclaim_gate_log` from `L453-L473` to **L455-L488**, which is where the
  ownership check and the suppressed `compact` call actually are; re-verified `read_gates` at
  **L514-L537** in `observer/snapshots.py` and left it unchanged (`return gates` is on L537). Added
  four reference rows. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Retracted the false
  single-writer claim this card inherited from the module docstring: this log has two writing
  processes and lost 11.50 percent of appended snapshots at the base commit, whole rows and never
  torn. Recorded that all I/O now routes through `durable_store.py` under `GATE_OWNERSHIP`; that
  the unconditional per-log lock is the mechanism and the compaction owner is advisory; that
  `compact_current` was replaced by `projected_current` with the projection-tick rewrite removed;
  that `read` stays strict, `read_for_projection` is new and tolerant, and both `delete` and
  `compact` rewrite from the strict read; and that `_replace` now delegates to `rewrite_lines`,
  which never unlinks an emptied log. Recorded the accepted consequence that reclamation now
  follows owner activity rather than a 30-second clock. Corrected the two superseded statements in
  the older sections rather than deleting them. Verification metadata pinned until closeout stamps
  the L5 commit.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/controlplane/store.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 2 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: added `GateStore.all_current()` — the whole-workspace fold the integrate seam guard uses (AR3-1(b)). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): GateStore.find cross-lifecycle resolution added. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-06-25T13:10+02:00 — Task 23/24: added physical gate deletion, atomic log replacement, lifecycle-log enumeration, and retention compaction for throwaway gate interactions.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the append-only `GateStore`. Verification metadata pinned until closeout stamps the 6a code commit.
