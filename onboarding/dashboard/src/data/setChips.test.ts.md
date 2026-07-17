# dashboard/src/data/setChips.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setChips.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pure regression suite for all shared set-chip, queued-hint, and attention derivations.

## Code Commentary

### Logic

Cases cover quiet state, honest ~35-second in-flight copy, coexisting queued/unknown pendings,
clamp, unsupported, acknowledgment suppression, pair progress/partial outcomes, route retry
classes, composer hints, and attention gates. The evidence-backed unsupported sibling remains
pinned beside the fix-round-3 route-unknown behavior.

### Conventions

Minimal `PerSessionCockpit` builders isolate presentation derivation from I/O.

### Invariants And Boundaries

Test-only; production path route failures are also asserted in `setClient.test.ts`.

### Todos

The two documented sev-4 presentation edges are not closed by this suite.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Pure presentation model under test. | L1-L232 | [setChips.ts](setChips.ts) |
| Pair copy/provenance source. | L1-L219 | [pairChange.ts](pairChange.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R5/R6/R9 through the final PASS;
  metadata awaits the uncommitted code's real commit.
