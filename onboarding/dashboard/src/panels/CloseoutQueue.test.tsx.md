# dashboard/src/panels/CloseoutQueue.test.tsx

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

## Evidence

### Repo-Internal References

- Candidate state, grade, and reasons render. [1]
- Typed non-admitting repair evidence renders. [2]
- Empty projection renders nothing. [3]

## 260821-CLIVE Projection Proof Boundary

These tests deliberately prove presentation of producer-owned facts. They do not certify readiness
or reproduce scheduler logic in the browser. Store reset isolation remains mandatory between cases.
