# dashboard/src/dev/sprintGraphPage.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/sprintGraphPage.tsx`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

A deterministic mounted-UI surface for the sprint execution graph (260815-DAG-L12 R7
evidence): the real sprint page (the Operations DetailPanel) opened against seeded
sprint-graph data, so a reviewer can screenshot the mounted wave-grid view and its closeout
queue at one URL (`/dev/sprint-graph`).

## Code Commentary

### Logic

`SprintGraphPage` builds a `SPRINT_GRAPH_PROJECTION` from the dev wire fixture
(`projection({ analytics: ... taskDocuments: [SPRINT_GRAPH_TASK_DOC], closeoutQueues:
[SPRINT_GRAPH_QUEUE] })`), applies it to the dashboard store on mount, and renders
`<DetailPanel selectedId="taskdoc:/tasks/agents-remember/sprint-graph/task.json" />` — the
real sprint page showing the wave-grid view and the scoped queue.

### Invariants And Boundaries

- Dev-only route; the store snapshot is applied on mount and never persisted.
- One-shot reviewer surface — the L12-R7 screenshot leg for a browser-capable seat.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The dev sprint-graph page. | `SprintGraphPage` | dashboard/src/dev/sprintGraphPage.tsx:16-20 |
| The fixture data it seeds. | `SPRINT_GRAPH_TASK_DOC`; `SPRINT_GRAPH_QUEUE` | dashboard/src/dev/sprintGraphFixture.ts:11-69; dashboard/src/dev/sprintGraphFixture.ts:71-88 |
| The real page surface rendered. | `DetailPanel` | dashboard/src/panels/detail-panel/DetailPanel.tsx:75-75 |
| The dev route dispatch. | `DevApp` | dashboard/src/dev/DevApp.tsx:13-47 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R7): the `/dev/sprint-graph` dev

route that mounts the real sprint page against the seeded graph fixture — the one-shot

screenshot surface for mounted-UI route review. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R7): the `/dev/sprint-graph` dev
  route that mounts the real sprint page against the seeded graph fixture — the one-shot
  screenshot surface for mounted-UI route review. Verified at code commit b7f2c8e2.
