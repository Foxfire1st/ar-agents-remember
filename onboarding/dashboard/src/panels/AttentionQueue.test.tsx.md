# dashboard/src/panels/AttentionQueue.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/AttentionQueue.test.tsx`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T04:44+02:00 |
| lastVerifiedCommitHash | `9c3180c133fccf98586a87c4b08824edaa3755a7` |
| lastVerifiedCommitDate | 2026-08-20T01:13:12+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Vitest + `@testing-library/react` render tests for `AttentionQueue`: the original §9 blocked-start
alarm parity still reaches the cockpit, and lifecycle-bound attention entries now resolve through
`analytics.taskDocuments` so the visible row is task-centric. Task 28 S5.2 adds the lifecycle-scoped
dismiss contract; Task 29 extends it so actionable-drift repo rows are dismissible targetless one-shot
signals and dismiss/clear hides rows optimistically while the POST is in flight.

## Code Commentary

### Logic

The first test seeds the real Zustand store from the `engine-fleet` `GALLERY` projection with its
`analytics.attentionQueue` overridden to a single `blocked-start` `AttentionItem` and asserts the title
and reason text. The second test adds a `TaskDocNode` with `lifecycleId: "LC19"` plus a lifecycle gate
attention item, then asserts the row title becomes `Task 19: Gate interaction polish` while the original
gate attention text remains in detail. The dismiss tests seed lifecycle rows, actionable drift, and a
blocked-start alarm, click per-row/header controls, assert the actionable-drift row disappears
immediately, and assert only dismissible lifecycle/gate/drift rows are posted while the blocked-start
alarm has neither `Open` nor `Dismiss`/`Clear all`.
`afterEach` runs RTL `cleanup` and resets the dashboard store.

### Invariants And Boundaries

Pure render assertion — relies on the shared `test/setup.ts` jsdom stubs. It proves the parity is achieved
without any `AttentionQueue` special-casing: the panel renders items generically by `severity`, so a new
`kind` surfaces with no UI change. The item carries no `lifecycleId` (a pre-contract start has no lifecycle
yet), so no "Open" or dismissal affordance is asserted.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The panel under test (generic severity-keyed rendering). | `item`; `AttentionQueueImpl` | dashboard/src/panels/AttentionQueue.tsx:21-40; dashboard/src/panels/AttentionQueue.tsx:271-323 |
| The reducer source of the `blocked-start` item (§9). | "def _start_attention(start_progress: list[dict[str" | mcp/src/agents_remember/observer/reducer_impl/_attention.py:335-335 |
| The store `applySnapshot` path used by this fixture's projection seed. | `applySnapshot` | dashboard/src/panels/AttentionQueue.test.tsx:61-61 |
| Targetless actionable drift dismissal hides immediately and posts a nullable lifecycle target. | "dismisses actionable drift without a lifecycle target and hides it immediately" | dashboard/src/panels/AttentionQueue.test.tsx:129-145 |
| Clear all includes gate, lifecycle, and actionable-drift rows but skips worktree alarms. | "Clear all dismisses dismissible listed items" | dashboard/src/panels/AttentionQueue.test.tsx:147-193 |

## Update History

- 2026-08-20T04:44+02:00 — 260815-DAG-L14: `taskDoc` fixture defaults `seats: []`; the shifted
  `applySnapshot` citation re-pinned. Verified at code commit 9c3180c1.


- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: the local TaskDocNode fixture supplies the new
  mechanically derived `executionWaves` field; attention-queue behavior is otherwise unchanged.

- 2026-08-04T11:39+02:00 — 260731-EFA-L6 S18-B13 curator: bound each queue claim to its implementation or focused test anchor and normalized scoped citation evidence.

- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: added/recorded coverage that actionable drift dismisses
  without a lifecycle target, hides optimistically, and participates in Clear all while worktree alarms
  remain non-dismissible. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:05+02:00 — Task 28 S5.2: updated coverage so `Dismiss`/`Clear all` post only lifecycle-scoped attention rows and non-lifecycle blocked-start alarms have no dismiss controls. Verification metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: added coverage that Clear still appears and posts cancel for a stale `gate-open` item with `gateId` but no `lifecycleId`.
- 2026-06-25T13:20+02:00 — Task 23/24: added coverage for the attention queue `Clear` action deleting open gate interactions by posting `cancel` for each gate id.
- 2026-06-25T07:17+02:00 — Task 19: added coverage for task-centric attention rows resolving lifecycle-bound queue entries through `analytics.taskDocuments`. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-16T03:35 — Created for slice 5f S3: render test pinning the §9 blocked-start alarm parity (the
  reducer's `_start_attention` item surfaces in the `AttentionQueue`). Verification metadata pinned until
  closeout stamps the S3 code commit.
