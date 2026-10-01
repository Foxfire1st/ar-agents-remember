# dashboard/src/data/submitMachine.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pins the pure FEUI-L5 submission lifecycle algebra, including adversarial observation order and real
wall-clock retry behavior, independently of React or network transport.

## Code Commentary

### Logic

The suite exercises every receipt/reconciliation outcome, the 1/2/5-second retry schedule inside the
120-second window, release without resend, and the evidence lattice under reordered poll/response
arrival. It specifically protects the architectural gap found during end-to-end review: dispatching
plus authority loss must become unknown, while later definitive delivery/withdrawal truth remains
admissible and cannot be regressed by stale observations.

### Invariants And Boundaries

- Tests use explicit observations and clocks; they do not infer authority from component render
  timing.
- Request identity is constant across every transition in a scenario.
- `not-found` and `generation-lost` never become safe-retry or draft-restore certificates.

### 2026-07-24 Curator Delta

The pure-machine tests distinguish a queued receipt from server-confirmed queued state and pin watch
start, terminal completion, phase exclusions, and bounded expiry.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository.

No configured live domain-documentation source was available.

### Repo-Internal References

- The system under test owns the normalized phase and partial-order rules. [1]
- Shared scenario fixtures provide named lifecycle examples used across UI tests. [2]

### Cross-Repo References

No meaningful cross-repo references found.

This is a repository-local unit suite.
