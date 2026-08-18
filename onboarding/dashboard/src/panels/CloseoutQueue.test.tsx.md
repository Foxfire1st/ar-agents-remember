# dashboard/src/panels/CloseoutQueue.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/CloseoutQueue.test.tsx`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-18T00:00+02:00                           |
| lastVerifiedCommitHash | `2597ff98306ba7c7963005092ac597c4972e63ce`       |
| lastVerifiedCommitDate | 2026-08-18T15:45:32+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[overview.md](overview.md)

## Purpose

Component proof for the read-only `CloseoutQueue` panel (L8-R8): it seeds the dashboard store with a
projected `CloseoutQueueNode` and asserts candidate state/grade/reasons render, the active blocker
renders with its rationale, and the panel stays empty when no queue is projected.

## Code Commentary

### Logic

A local `queue(overrides)` builder produces a minimal `CloseoutQueueNode`; the three tests seed
`dashboardStore.setState({ closeoutQueues: ... })` and assert the rendered rows, blocker, and the
empty case.

### Invariants And Boundaries

- The store is seeded via `setState` and reset in `afterEach` so tests do not leak state.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate state/grade/reasons render. | "renders candidates with state, grade, and reasons" | dashboard/src/panels/CloseoutQueue.test.tsx:41-49 |
| Blocker renders with rationale. | "renders the active atomic blocker" | dashboard/src/panels/CloseoutQueue.test.tsx:51-64 |
| Empty projection renders nothing. | "renders nothing when no queue is projected" | dashboard/src/panels/CloseoutQueue.test.tsx:66-71 |

## Update History

- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the closeout-queue panel component proof.
  Verification metadata pinned until closeout stamps the L8 commit.
