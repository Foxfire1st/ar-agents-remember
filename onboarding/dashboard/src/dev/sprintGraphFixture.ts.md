# dashboard/src/dev/sprintGraphFixture.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/sprintGraphFixture.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T15:04+02:00                           |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5`       |
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The seeded sprint data for the `/dev/sprint-graph` mounted-UI evidence surface
(260815-DAG-L12 R7): a segmented organizational master with an early and a late segment
around an atomic lump master, edges with recorded reasons, and per-node frontier states.
The zero-edge and segmented-master scenarios are covered by the component tests; this
fixture drives the screenshot-able sprint page.

## Code Commentary

### Logic

`SPRINT_GRAPH_TASK_DOC` is a `taskDoc(...)` master with `executionGraphView` nodes: Master
A's `seg1` (wave 1, `in-flight`, two leaves), the atomic lump F (wave 2, `waiting`,
predecessor = Master A with reason "the shared framework must land first"), and Master A's
`seg2` (wave 3, `ready`, predecessor = atomic F with reason "the atomic block gates the
late segment"). `SPRINT_GRAPH_QUEUE` is a `CloseoutQueueNode` for the same sprint with a
`valid-built` service condition, exact source classification/fingerprint, no source problems,
and one generation-keyed projection member carrying classification, priority, order, and reasons.
It seeds a disposable scheduling view; it does not model a mutable blocker or candidate lifecycle.

### Invariants And Boundaries

- Dev-only fixture; shapes mirror the generated `TaskExecutionGraphView` wire model.
- Deterministic values so the one-shot screenshot surface is stable.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The seeded sprint document. | `SPRINT_GRAPH_TASK_DOC` | dashboard/src/dev/sprintGraphFixture.ts:11-69 |
| The seeded sprint queue. | `SPRINT_GRAPH_QUEUE` | dashboard/src/dev/sprintGraphFixture.ts:71-88 |
| The page that consumes the fixture. | `SprintGraphPage` | dashboard/src/dev/sprintGraphPage.tsx:16-20 |
| The wire model the fixture shapes. | `TaskExecutionGraphView` | dashboard/src/types/projection.ts:656-658 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## 260821-CLIVE Disposable Projection Fixture

The queue fixture was migrated from the retired `graphRevision`/`activeBlocker`/`candidates`
shape to the exact-current projection shape. Its deterministic graph remains independent source
data: the graph explains topology, while the queue member explains current scheduling. Neither is
durable claim, certification, commit, or recovery authority.

## Update History

- 2026-08-24T15:04+02:00 — Rebased the mounted sprint fixture onto the disposable closeout
  projection contract (`serviceCondition`, source identity/problems, and generation-keyed members).

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R7): the deterministic sprint-graph

fixture (segmented + atomic scenario with reasoned edges) for the `/dev/sprint-graph`

mounted-UI screenshot surface. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R7): the deterministic sprint-graph
  fixture (segmented + atomic scenario with reasoned edges) for the `/dev/sprint-graph`
  mounted-UI screenshot surface. Verified at code commit b7f2c8e2.
