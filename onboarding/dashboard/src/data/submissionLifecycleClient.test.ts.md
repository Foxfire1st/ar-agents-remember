# dashboard/src/data/submissionLifecycleClient.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submissionLifecycleClient.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

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

## FEUI-L8 Reviewed Candidate Delta

Pins same-id poller isolation: an old poll completion neither applies to new per-seat truth nor deletes/reschedules the successor poller after a dev authority reset.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured authoritative poll ordering,
  withdrawal race/loss convergence, epoch loss, revision-CAS restoration, recovery-slot decisions,
  and exact local dismissal. Verification metadata remains pinned to the leaf base.
