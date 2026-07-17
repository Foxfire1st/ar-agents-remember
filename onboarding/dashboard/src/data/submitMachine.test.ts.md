# dashboard/src/data/submitMachine.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitMachine.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

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

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The system under test owns the normalized phase and partial-order rules. | — | [submitMachine.ts](submitMachine.ts) |
| Shared scenario fixtures provide named lifecycle examples used across UI tests. | — | [../test/fixtures/submitScenarios.ts](../test/fixtures/submitScenarios.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This is a repository-local unit suite. | — | — |

## Update History

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured the monotonic evidence-order,
  availability-loss, definitive-terminal, immutable-id, and wall-clock retry regression proofs.
  Verification metadata remains pinned to the leaf base until closeout.
