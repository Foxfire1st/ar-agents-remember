# dashboard/src/data/submitClient.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/submitClient.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
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

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The system under test owns transport classification and store-driving. | — | [submitClient.ts](submitClient.ts) |
| Shared fixtures name accepted, ambiguous, queued, and withdrawal scenarios. | — | [../test/fixtures/submitScenarios.ts](../test/fixtures/submitScenarios.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This is a repository-local unit suite. | — | — |

## FEUI-L8 Reviewed Candidate Delta

Adds polite receipt-copy coverage and proves only the focused session announces accepted/queued/rejected/unsupported delivery truth.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured certified retry, first-byte
  ambiguity, no-resend reconciliation, exact epoch/id/text correlation, readiness, and draft/source
  provenance regression coverage. Verification metadata remains pinned to the leaf base.
