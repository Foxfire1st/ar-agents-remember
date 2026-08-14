# mcp/src/agents_remember/controlplane/attention_dismissals.py

| Field                  | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/attention_dismissals.py`      |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-08-01T20:15+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                         |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                      |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Projection tick that prunes rows after folding live lifecycle state. | `prune_lifecycles` | mcp/src/agents_remember/serving/projections/projection_store.py:236-272 |
| Reducer suppression check that requires the acknowledgement lifecycle to match the item lifecycle. | "def _is_dismissed(" | mcp/src/agents_remember/observer/reducer_impl/_attention.py:79-79 |
| Serving route that records lifecycle acknowledgements or cancels gate-open items. | "def _dismissal_response(" | mcp/src/agents_remember/serving/_app_routes.py:267-267 |
| Targetless actionable-drift rows are the only non-lifecycle acknowledgements retained by prune: `prune_lifecycles` through `_prune_locked` and the module-level `_keep_current_record`. | `_keep_current_record` | mcp/src/agents_remember/controlplane/attention_dismissals.py:138-141 |
| `dismiss` holds `exclusive_access` across the read and the rewrite; `_replace` delegates to `rewrite_lines` and never unlinks. | `exclusive_access` | mcp/src/agents_remember/controlplane/attention_dismissals.py:58-77; mcp/src/agents_remember/controlplane/attention_dismissals.py:125-135 |
| `ATTENTION_DISMISSAL_OWNERSHIP` records why a single-writer store is still locked and names the 31.45 percent an unlocked draft measured. | `ATTENTION_DISMISSAL_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:164-180 |
| The HTTP dismiss route at L1164 that makes this whole-file read-modify-write a user-facing click. | "def _dismissal_response(" | mcp/src/agents_remember/serving/_app_routes.py:267-267 |

## Update History
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 12 citation findings and two
  unsupported claims. Re-anchored the six reference rows (projection prune, reducer check, dismiss
  route ×2, self prune/write paths). Cut the "127 of 2000" `FileNotFoundError` attribution — no file
  in the frozen source states it — and the superseded "deletes the file when empty" clause, which
  contradicts `_replace`/`rewrite_lines` and this card's own no-unlink invariant. Scoped recheck clean.
- 2026-08-01T20:15+02:00 — 260731-EFA-L5 curator (correction pass). **Three stale citations, all of
  the shape the L4 audit found — a range that starts correctly and stops short of a symbol the claim
  names.** (1) The prune row cited `prune_lifecycles` through `_prune_locked` and
  `_keep_current_record` at **L92-L122**; `_keep_current_record` is a module-level function at
  **L138**, outside the range entirely. (2) The write row cited `dismiss` at **L58-L67** for a claim
  about holding `exclusive_access` across the read and the rewrite — the `def` is at L58 but the
  `exclusive_access` line is at **L74**, past the end of the range — and `_replace` at **L109-L116**,
  which is now at **L125**. (3) `ATTENTION_DISMISSAL_OWNERSHIP` was cited at **L282-L295**; it is at
  **L350**, because `durable_store.py` grew 598 → 699 lines mid-pass. All three rows are now
  symbol-name citations with no range: a number that was wrong within the hour is worse than no
  number. The row structure is unchanged — this is a two-column `Finding | Source Path` table and it
  still is. The **127 of 2000** raising count is now attributed to `durable_store.py`, the only file
  that states it; the **31.45 percent** beside it is left asserted, because four independent files
  carry it (`durable_store.py`, `supervisor_signals.py`, `test_durable_store_contract.py`,
  `test_observer_projection.py`). This card's read-policy note was already correct — it says the
  rewrites here are driven by the tolerant read and that a compaction therefore drops an unparseable
  row — and was left unchanged.
- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Recorded why the store with a
  single writer measured the worst loss of the six — 31.45 percent, plus 127 of 2000 `dismiss`
  calls raising: `dismiss` is a whole-file read-modify-write reached from the dashboard HTTP route
  at `serving/app.py:1164`, so two concurrent dismisses lose each other with no compactor and no
  second writer, and the shared `<log>.tmp` name made concurrent rewriters raise. Recorded that
  `dismiss` and `prune_lifecycles` now hold `exclusive_access` across read and rewrite (the new
  `_prune_locked` half), that `_replace` delegates to `rewrite_lines` and no longer unlinks an
  emptied file, and that `AttentionDismissalRecord` now inherits `DurableRecord` for
  `extra="forbid"` plus a validated `schemaVersion`. Corrected the superseded unlink invariant.
  Repaired the citation the L2 format pass had left pointing at moved code and repaired the row
  itself, which carried three cells in a two-column table. Verification metadata pinned until
  closeout stamps the L5 commit.
- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/src/agents_remember/controlplane/attention_dismissals.py` and moved the lines this card
  cites, so the Citations column no longer pointed at the code its rows name. Corrected the ranges
  (L77-L111 → L77-L110). The behaviour described is unchanged — the file's AST is identical to the
  base revision — this is a citation repair only. Verification metadata pinned until closeout
  stamps the L2 commit.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: `prune_lifecycles` now retains targetless
  actionable-drift current acknowledgements while still pruning lifecycle rows whose lifecycle left the
  live projection. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:05+02:00 — Created for task 28 S5.2: compact lifecycle-scoped attention acknowledgements replace append-only suppression history; prune folds legacy duplicate rows and physically removes terminal/non-live lifecycle rows. Verification metadata pinned until closeout stamps the task-28 code commit.
