# dashboard/src/panels/CloseoutQueue.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/CloseoutQueue.test.tsx`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T15:04+02:00                           |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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
| Candidate state, grade, and reasons render. | "renders candidates with state, grade, and reasons" | dashboard/src/panels/CloseoutQueue.test.tsx:50-56 |
| Typed non-admitting repair evidence renders. | "renders typed non-admitting repair evidence" | dashboard/src/panels/CloseoutQueue.test.tsx:58-79 |
| Empty projection renders nothing. | "renders nothing when no queue is projected" | dashboard/src/panels/CloseoutQueue.test.tsx:81-85 |

## 260821-CLIVE Projection Proof Boundary

These tests deliberately prove presentation of producer-owned facts. They do not certify readiness
or reproduce scheduler logic in the browser. Store reset isolation remains mandatory between cases.

## Update History

- 2026-08-24T15:04+02:00 — Replaced obsolete mutable blocker/candidate assertions with
  disposable member and typed source-problem/repair evidence coverage.

- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the closeout-queue panel component proof.
  Verification metadata pinned until closeout stamps the L8 commit.