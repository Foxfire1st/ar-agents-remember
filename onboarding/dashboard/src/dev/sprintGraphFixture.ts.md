# dashboard/src/dev/sprintGraphFixture.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/sprintGraphFixture.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
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
revision/graphRevision and the atomic blocker + declared candidate — so the mounted sprint
page shows the graph and its queue together.

### Invariants And Boundaries

- Dev-only fixture; shapes mirror the generated `TaskExecutionGraphView` wire model.
- Deterministic values so the one-shot screenshot surface is stable.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The seeded sprint document. | `SPRINT_GRAPH_TASK_DOC` | dashboard/src/dev/sprintGraphFixture.ts:11-69 |
| The seeded sprint queue. | `SPRINT_GRAPH_QUEUE` | dashboard/src/dev/sprintGraphFixture.ts:71-88 |
| The page that consumes the fixture. | `SprintGraphPage` | dashboard/src/dev/sprintGraphPage.tsx:16-20 |
| The wire model the fixture shapes. | `TaskExecutionGraphView` | dashboard/src/types/projection.ts:561-565 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R7): the deterministic sprint-graph

fixture (segmented + atomic scenario with reasoned edges) for the `/dev/sprint-graph`

mounted-UI screenshot surface. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R7): the deterministic sprint-graph
  fixture (segmented + atomic scenario with reasoned edges) for the `/dev/sprint-graph`
  mounted-UI screenshot surface. Verified at code commit b7f2c8e2.
