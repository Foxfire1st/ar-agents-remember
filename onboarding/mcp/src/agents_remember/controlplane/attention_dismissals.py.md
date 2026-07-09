# mcp/src/agents_remember/controlplane/attention_dismissals.py

| Field                  | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/attention_dismissals.py`      |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-09T19:31+02:00 |
| lastVerifiedCommitHash | `dbe750e4cd7fb777b8f39e7ba6279d1080502d8e`                         |
| lastVerifiedCommitDate | 2026-07-09T19:42:39+02:00|
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
  rows whose lifecycle id is outside the live projected lifecycle set, keeps targetless
  `actionable-drift` current records, and deletes the file when empty.

The reducer consumes these records as lifecycle-scoped acknowledgements; gate-open
attention rows are consumed by cancelling/deleting the gate itself, so they normally do
not need a row in this store.

## Invariants And Boundaries

- Disposable interaction state only; durable task history lives in task docs, contracts,
  commits, ledgers, and observer events.
- Lifecycle scope is load-bearing. Rows without a `lifecycleId` are pruned instead of
  becoming global item-id suppressions, except for `kind == "actionable-drift"`, whose
  source is a repo/branch drift snapshot with its own `checkedAt` signal timestamp.
- The store mirrors the gate/inbox physical-delete pattern: rewrite the current set with
  `os.replace`, and unlink the file when no rows remain.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Projection tick that prunes rows after folding live lifecycle state. | [observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| Reducer suppression check that requires the acknowledgement lifecycle to match the item lifecycle. | [observer/reducer.py](agents-remember/mcp/src/agents_remember/observer/reducer.py) |
| Serving route that records lifecycle acknowledgements or cancels gate-open items. | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| Targetless actionable-drift rows are the only non-lifecycle acknowledgements retained by prune. | L77-L111 | [attention_dismissals.py](agents-remember/mcp/src/agents_remember/controlplane/attention_dismissals.py) |

## Update History

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: `prune_lifecycles` now retains targetless
  actionable-drift current acknowledgements while still pruning lifecycle rows whose lifecycle left the
  live projection. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:05+02:00 — Created for task 28 S5.2: compact lifecycle-scoped attention acknowledgements replace append-only suppression history; prune folds legacy duplicate rows and physically removes terminal/non-live lifecycle rows. Verification metadata pinned until closeout stamps the task-28 code commit.
