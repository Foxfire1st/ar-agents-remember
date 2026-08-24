# dashboard/src/panels/CloseoutQueue.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/CloseoutQueue.test.tsx`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T15:04+02:00                           |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`       |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[overview.md](overview.md)

## Purpose

Component proof for the read-only `CloseoutQueue` panel: it seeds the dashboard store with a
disposable `CloseoutQueueNode` and asserts projection-member classification, priority, and reasons;
typed non-admitting source problems and repair evidence; and the empty-projection null render.

## Code Commentary

### Logic

A local `queue(overrides)` builder produces a minimal exact-current projection. The tests seed
`dashboardStore.setState({ closeoutQueues: ... })` and prove a generation-keyed member row, an
`invalid-empty` projection with `source-fingerprint-mismatch` and its exact rebuild action, and the
empty case.

### Invariants And Boundaries

- The store is seeded via `setState` and reset in `afterEach` so tests do not leak state.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Projection-member classification, priority, and reasons render. | "renders projected members with classification, priority, and reasons" | dashboard/src/panels/CloseoutQueue.test.tsx |
| Invalid-empty source problem and rebuild action render. | "renders invalid projection repair evidence" | dashboard/src/panels/CloseoutQueue.test.tsx |
| Empty projection renders nothing. | "renders nothing when no queue is projected" | dashboard/src/panels/CloseoutQueue.test.tsx |

## 260821-CLIVE Projection Proof Boundary

These tests deliberately prove presentation of producer-owned facts. They do not certify readiness
or reproduce scheduler logic in the browser. Store reset isolation remains mandatory between cases.

## Update History

- 2026-08-24T15:04+02:00 — Replaced obsolete mutable blocker/candidate assertions with
  disposable member and typed source-problem/repair evidence coverage.

- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the closeout-queue panel component proof.
  Verification metadata pinned until closeout stamps the L8 commit.
