# mcp/src/agents_remember/controlplane/attention_dismissals.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`attention_dismissals.py` stores current lifecycle-scoped attention acknowledgements
for the dashboard attention queue. It is not an audit log: attention rows are derived,
throwaway UI facts, so the store keeps only the acknowledgement needed to hide the
current lifecycle-bound occurrence until a newer signal arrives or the lifecycle leaves
the live set. Task 29 also keeps targetless `actionable-drift` rows as repo-level
current acknowledgements, because their occurrence is anchored by the drift snapshot
timestamp instead of by a lifecycle.

## Code Commentary

### 260731-EFA-L5 The Single-Writer Store That Lost The Most

This log measured the **worst loss of the six** at the base commit: **31.45 percent** of writes
lost — the one base-commit figure carried at several independent sites (`durable_store.py`,
`agent_notifier_signals.py`, `test_durable_store_contract.py`, `test_observer_projection.py`) rather
than at one. It also had a
single writer. Both facts are true at once, and the reason is the most important thing on this card.

`dismiss()` is not an append. It is a **whole-file read-modify-write**: read the current set, upsert
one row by `itemId`, rewrite everything. And it is reached from the dashboard's HTTP dismiss route
at `serving/app.py:1164` — a button a person presses. So two concurrent dismisses lose each other
**with no compactor involved and no second writer required**. The projection sweep's
`prune_lifecycles` is a second read-modify-write over the same file, from a different thread of the
same process, making the pair a lost-update race on its own.

The raising was the colliding temp path: `_replace` built `<log>.tmp` with nothing to distinguish
one writer from another, so two concurrent rewriters shared it, one `os.replace`d it away and the
other raised. That reached the operator as a 500 on a click.

An earlier draft of this leaf left this store **unlocked** on the strength of it being
single-writer. The proof run measured the 31.45 percent doing exactly that. This is why
`StoreOwnership` has no `serialized` field: "only one process writes this file" is a deployment
fact, not a structural one.

### 260731-EFA-L5 What Changed

Every rewrite now holds the log's lock across the read **and** the rewrite:

- `dismiss(record)` opens `exclusive_access` before folding `current()` and rewriting.
- `prune_lifecycles(live_lifecycle_ids)` opens `exclusive_access` and delegates to the new
  `_prune_locked`, which is the read-filter-rewrite half.
- `_replace` no longer unlinks an emptied file, no longer builds `<log>.tmp` and no longer calls
  `os.replace`; it delegates to `durable_store.rewrite_lines`, which refuses unless the calling
  thread holds the lock, uses a pid-scoped hidden temp name and fsyncs.

`AttentionDismissalRecord` now inherits `DurableRecord` instead of `BaseModel`, so it picks up
`extra="forbid"` (previously declared locally) plus a validated `schemaVersion`: an unknown major
raises `ValidationError` at parse time and this store's tolerant reader skips the row, with no
version branch in the reader.

`ATTENTION_DISMISSAL_OWNERSHIP` declares the dashboard both the sole writer and the compaction
owner.

**Note on the read policy.** `read()` stays tolerant — these are disposable UI facts, and one bad
row must not 500 the dismiss endpoint or freeze a tick. Because it is the store's only reader, the
rewrites above are driven by the tolerant read, so a compaction here *does* drop an unparseable row
permanently. That is safe precisely because this log carries no authority; it would stop being safe
the moment a decision depended on one of these rows.

### 260707-HFX2-L12 CS-6 Update

`AttentionDismissalStore.read()` now treats this disposable UI acknowledgement log as dashboard-tolerant: malformed or torn JSONL rows are skipped, while valid acknowledgement rows still fold by `itemId` and prune by live lifecycle id.

`AttentionDismissalRecord` is the compact `ar-attention-dismissal/v1` row keyed by
`itemId`, carrying `dismissedAt` plus optional `kind`, `lifecycleId`, and `gateId`
provenance. `AttentionDismissalStore` writes the workspace file
`<observer_root>/workspace/attention-dismissals.jsonl`, but treats it as a compact
current set:

- `dismiss(record)` upserts by `itemId`, replacing an older row for the same item.
- `current()` folds any legacy duplicate rows by `itemId` and returns the latest record.
- `prune_lifecycles(live_lifecycle_ids)` folds legacy duplicate rows, physically removes lifecycle
  rows whose lifecycle id is outside the live projected lifecycle set, and keeps targetless
  `actionable-drift` current records.

The reducer consumes these records as lifecycle-scoped acknowledgements; gate-open
attention rows are consumed by cancelling/deleting the gate itself, so they normally do
not need a row in this store.

## Invariants And Boundaries

- Disposable interaction state only; durable task history lives in task docs, contracts,
  commits, ledgers, and observer events.
- Lifecycle scope is load-bearing. Rows without a `lifecycleId` are pruned instead of
  becoming global item-id suppressions, except for `kind == "actionable-drift"`, whose
  source is a repo/branch drift snapshot with its own `checkedAt` signal timestamp.
- The store mirrors the gate/inbox physical-delete pattern, but through the shared contract:
  `durable_store.rewrite_lines` writes the current set. **The file is no longer unlinked when no
  rows remain** — an empty current set is an empty file. Restore the unlink and a concurrent
  appender holding an open handle writes into an unlinked inode, which is loss with no torn line
  and no trace at all.
- **Locked unconditionally, single writer notwithstanding.** `dismiss` and `prune_lifecycles` both
  hold `exclusive_access` across their read and their rewrite. Drop the lock on the grounds that
  one process writes this file and the 31.45 percent returns, because the race is between two
  read-modify-writes inside that one process.

## Evidence

### Repo-Internal References

- Projection tick that prunes rows after folding live lifecycle state. [1]
- Reducer suppression check that requires the acknowledgement lifecycle to match the item lifecycle. [2]
- Serving route that records lifecycle acknowledgements or cancels gate-open items. [3]
- Targetless actionable-drift rows are the only non-lifecycle acknowledgements retained by prune: `prune_lifecycles` through `_prune_locked` and the module-level `_keep_current_record`. [4]
- `dismiss` holds `exclusive_access` across the read and the rewrite; `_replace` delegates to `rewrite_lines` and never unlinks. [5]
- `ATTENTION_DISMISSAL_OWNERSHIP` records why a single-writer store is still locked and names the 31.45 percent an unlocked draft measured. [6]
- The HTTP dismiss route at L1164 that makes this whole-file read-modify-write a user-facing click. [7]
