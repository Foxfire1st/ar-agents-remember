# dashboard/src/data/submitClient.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitClient.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

## Purpose

Provides transport-level regression proof for FEUI-L5 reliable submission, especially the boundary
between certified pre-dispatch failure and ambiguous response loss.

## Code Commentary

### Logic

The suite drives exact epoch/id/text requests through success, queued, rejection, unknown,
unsupported, deadline, first-byte loss, safe certificate, and reconciliation paths. It proves that
only the typed server certificate retries, all possible-post-write failures keep one id and perform
status/reconcile without resending, and store updates respect source provenance plus draft revision
CAS. Create-then-ready scenarios verify that UI composition can precede bridge readiness without
allowing premature delivery.

### Invariants And Boundaries

- Assertions count native-facing submit calls so a test cannot pass while silently duplicating a
  prompt.
- Safe retry reuses both id and text; a new user send gets a new id.
- Non-composer sends cannot clear or restore the composer draft.

### 2026-07-24 Curator Delta

Regression coverage now exercises the honest queued receipt, delivering draft-clear path, live-turn
submission gate, and continued lifecycle polling after non-terminal authority states.

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The system under test owns transport classification and store-driving. | `createFetchSubmitTransport` | dashboard/src/data/submitClient.ts:197-254 |
| Shared fixtures name accepted, ambiguous, queued, and withdrawal scenarios. | `RECEIPT_ACCEPTANCES` | dashboard/src/test/fixtures/submitScenarios.ts:79-85 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is a repository-local unit suite. | — | — |

## FEUI-L8 Reviewed Candidate Delta

Adds polite receipt-copy coverage and proves only the focused session announces accepted/queued/rejected/unsupported delivery truth.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 2 table citations for the submit transport and receipt acceptances; fixer-generated ranges verified.

- 2026-07-24T13:17:50Z — Added submit honesty and continued-watch coverage. Verification hash/date
  remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured certified retry, first-byte
  ambiguity, no-resend reconciliation, exact epoch/id/text correlation, readiness, and draft/source
  provenance regression coverage. Verification metadata remains pinned to the leaf base.
