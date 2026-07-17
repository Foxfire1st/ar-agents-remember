# dashboard/src/data/setAcceptance.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setAcceptance.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Pure reducer and promotion implementation. | L1-L250 | [setAcceptance.ts](setAcceptance.ts) |
| Clamp, queued, and unknown fixture extensions. | L219-L358 | [../test/fixtures/capabilityEnvelopes.ts](../test/fixtures/capabilityEnvelopes.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R3/R4/R9; base metadata awaits the
  actual code commit.
