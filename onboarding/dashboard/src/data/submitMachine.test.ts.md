# dashboard/src/data/submitMachine.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitMachine.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The system under test owns the normalized phase and partial-order rules. | `settleSubmissionObservation` | dashboard/src/data/submitMachine.ts:155-186 |
| Shared scenario fixtures provide named lifecycle examples used across UI tests. | `submitReceipt` | dashboard/src/test/fixtures/submitScenarios.ts:87-108 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is a repository-local unit suite. | — | — |

## Update History

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 4 citation findings; scoped check passed.

- 2026-07-24T13:17:50Z — Added receipt-honesty and lifecycle-watch coverage. Verification hash/date
  remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured the monotonic evidence-order,
  availability-loss, definitive-terminal, immutable-id, and wall-clock retry regression proofs.
  Verification metadata remains pinned to the leaf base until closeout.
