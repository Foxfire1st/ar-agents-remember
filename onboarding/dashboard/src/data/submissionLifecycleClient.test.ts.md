# dashboard/src/data/submissionLifecycleClient.test.ts

## Governing Overview

[data overview](overview.md)

## 260731-EFA-L8 Change

The suite was updated for the validated-narrow replacement (no bare
`as SubmissionLifecycleState` cast) and the extracted withdrawal module; the tested
contract is unchanged.

## Purpose

Pins the end-to-end browser projection of submission status and authoritative pop-back, including
poll/response races that unit tests of the pure state machine cannot exercise.

## Code Commentary

### Logic

The suite covers strict raw-free response parsing, visible/hidden/failure polling cadence, 64-id
batches, captured observation versions, and response symmetry through the central fold. Withdrawal
scenarios include queued success, dispatch races, lost HTTP responses followed by status
convergence, generation/epoch loss, unchanged-draft auto-restore, concurrent-edit recovery-slot
creation, explicit replace versus keep-current, and exact dismissal with no network call.

### Invariants And Boundaries

- A queued-looking stale poll cannot regress a later definitive result.
- Tests never restore from not-found or generation-lost evidence.
- Recovery assertions include draft revision as well as request id, preventing a successor request
  or newer edit from being dismissed accidentally.

### 2026-07-24 Curator Delta

The polling suite now proves that dispatching is non-terminal, delivered stops the poller, and a
never-terminal record reaches bounded endgame instead of producing an unbounded loop.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository.

No configured live domain-documentation source was available.

### Repo-Internal References

- The system under test owns polling, withdrawal, and draft recovery. [1]
- The server authority suite proves the corresponding linearization boundary. [2]

### Cross-Repo References

No meaningful cross-repo references found.

This is a repository-local frontend integration suite.

## FEUI-L8 Reviewed Candidate Delta

Pins same-id poller isolation: an old poll completion neither applies to new per-seat truth nor deletes/reschedules the successor poller after a dev authority reset.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
