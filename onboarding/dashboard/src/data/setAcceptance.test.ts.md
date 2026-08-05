# dashboard/src/data/setAcceptance.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setAcceptance.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Exhaustive pure tests for the SetResult reducer, attention/clamp classification, HTTP boundary,
snapshot promotion, and turn-ended re-fetch predicate.

## Code Commentary

### Logic

The suite runs every acceptance and edge row for both model and effort, distinguishes evidence
from transport, preserves exact provider-qualified comparisons, proves Codex both-queued
resolution on one snapshot, and keeps inflight/unconfirmed queued states untouched.

### Conventions

Shared fixtures carry the wire vocabulary; tables are preferred over one-off examples.

### Invariants And Boundaries

Test-only; driver single-flight and actual I/O sequencing live in `setClient.test.ts`.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pure reducer and promotion implementation. | `reduceSetResult` | dashboard/src/data/setAcceptance.ts:101-153 |
| Clamp, queued, and unknown fixture extensions. | `SET_RESULT_CLAMP`; `QUEUED_THEN_IMMEDIATE_SEQUENCE`; `UNKNOWN_THEN_READBACK` | dashboard/src/test/fixtures/capabilityEnvelopes.ts:253-259; dashboard/src/test/fixtures/capabilityEnvelopes.ts:273-288; dashboard/src/test/fixtures/capabilityEnvelopes.ts:305-319 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-03T02:34+02:00 — W3-B01 curator: curated 2 Repo-Internal table citations with exact reducer and fixture anchors. Verification metadata remains unchanged for closeout.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R3/R4/R9; base metadata awaits the
  actual code commit.
