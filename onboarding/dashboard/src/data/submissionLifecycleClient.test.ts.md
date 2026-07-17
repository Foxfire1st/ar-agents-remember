# dashboard/src/data/submissionLifecycleClient.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submissionLifecycleClient.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

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

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The system under test owns polling, withdrawal, and draft recovery. | — | [submissionLifecycleClient.ts](submissionLifecycleClient.ts) |
| The server authority suite proves the corresponding linearization boundary. | — | [../../../mcp/tests/test_harness_submission_authority.py](../../../mcp/tests/test_harness_submission_authority.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This is a repository-local frontend integration suite. | — | — |

## Update History

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured authoritative poll ordering,
  withdrawal race/loss convergence, epoch loss, revision-CAS restoration, recovery-slot decisions,
  and exact local dismissal. Verification metadata remains pinned to the leaf base.
