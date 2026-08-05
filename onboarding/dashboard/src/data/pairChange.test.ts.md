# dashboard/src/data/pairChange.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/pairChange.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Exhaustive pure-machine regression suite for serialized pair changes.

## Code Commentary

### Logic

Tables cover every acceptance at both steps, confirmed and disproved unknown readbacks,
wrong-step/finished guards, model-route abort versus effort-route partial termination, two-step
progress copy, designed refusal copy, and the fix-round-3 unknown-effectiveness route copy.

### Conventions

The suite uses real shared SetResult fixtures and asserts both directives and resulting state.

### Invariants And Boundaries

Pure tests complement, but do not replace, `setClient.test.ts` production-path ordering and fetch
tests.

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
| Pure machine under test. | `applyPairStepResult`; `applyPairRouteError`; `applyPairReadback` | dashboard/src/data/pairChange.ts:58-111; dashboard/src/data/pairChange.ts:119-150; dashboard/src/data/pairChange.ts:156-196 |
| Production driver tests that prove actual POST ordering and route siblings. | "serialized pair change (R5)" | dashboard/src/data/setClient.test.ts:340-536 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: retained the direct pair-change source rows and supplied the S18-B12 history marker; scoped fixer will generate final ranges.
- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R5/R9, including fix-round-3 route-copy
  assertions accepted by the final reviewer PASS. Base metadata awaits the code commit.
