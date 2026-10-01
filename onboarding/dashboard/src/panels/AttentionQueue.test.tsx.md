# dashboard/src/panels/AttentionQueue.test.tsx

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

## Evidence

### Repo-Internal References

- The panel under test (generic severity-keyed rendering). [1]
- The reducer source of the `blocked-start` item (§9). [2]
- The store `applySnapshot` path used by this fixture's projection seed. [3]
- Targetless actionable drift dismissal hides immediately and posts a nullable lifecycle target. [4]
- Clear all includes gate, lifecycle, and actionable-drift rows but skips worktree alarms. [5]
