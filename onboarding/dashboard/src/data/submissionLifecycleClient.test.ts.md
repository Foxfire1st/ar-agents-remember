# dashboard/src/data/submissionLifecycleClient.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submissionLifecycleClient.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md`                                   |

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

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The system under test owns polling, withdrawal, and draft recovery. | `ensureSubmissionLifecyclePolling`; `withdrawLastQueuedSubmission`; `restoreWithdrawnRecovery` | dashboard/src/data/submissionLifecycleClient.ts:949-961; dashboard/src/data/submissionWithdrawal.ts:352-377; dashboard/src/data/submissionWithdrawal.ts:405-417 |
| The server authority suite proves the corresponding linearization boundary. | `HarnessSubmissionAuthorityTests` | mcp/tests/test_harness_submission_authority.py:230-755 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is a repository-local frontend integration suite. | — | — |

## FEUI-L8 Reviewed Candidate Delta

Pins same-id poller isolation: an old poll completion neither applies to new per-seat truth nor deletes/reschedules the successor poller after a dev authority reset.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the suite update for the validated narrow. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:30:16+02:00 — W3-B05 curator: anchored 2 Tier-2 table citations with exact source paths; fixer generated all final ranges.

- 2026-07-24T13:17:50Z — Added terminal-word and bounded-watch polling coverage. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured authoritative poll ordering,
  withdrawal race/loss convergence, epoch loss, revision-CAS restoration, recovery-slot decisions,
  and exact local dismissal. Verification metadata remains pinned to the leaf base.
