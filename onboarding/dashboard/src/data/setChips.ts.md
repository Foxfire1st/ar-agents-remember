# dashboard/src/data/setChips.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setChips.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Pure shared presentation model for acceptance, pair, and route chips, queued composer hints, and
unacknowledged set attention.

## Code Commentary

### Logic

`deriveSetChips` orders pair state first, then per-kind pending and latest-unacknowledged ledger
evidence, then route errors. Route-terminated pairs use `routeErrorStep` to say effectiveness is
unknown; evidence-backed unsupported pairs keep the designed abort/refusal copy. The same models
feed the header, inspector-adjacent surfaces, and background toasts.

### Conventions

Every acceptance chip carries the acceptance word in `text`; tone never carries meaning alone.
Only 503 route errors are retryable.

### Invariants And Boundaries

Pending requested values never move effective markers. Clamp copy keeps both values; pair progress
spins only while an actual step remains active.

### Todos

- Reviewer sev-4 observation 4: a superseded `unknown` ledger entry can say a readback kept the
  prior value even though no readback resolved that superseded request.
- Reviewer sev-4 observation 7: an identical-value re-request temporarily hides the persistent
  clamp chip while the new in-flight chip is shown; attention remains held.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Chip ordering, copy selection, composer hint, and attention gate. | L1-L232 | [setChips.ts](setChips.ts) |
| Full chip/pair/route/hint matrix. | L35-L232 | [setChips.test.ts](setChips.test.ts) |
| Copy source consumed by every chip. | L1-L127 | [setControlsCopy.ts](setControlsCopy.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R5/R6 through fix round 3. Final PASS
  confirmed route failures no longer borrow SetResult certainty; sev-4 observations 4 and 7 remain
  recorded. Base verification metadata is temporary until code commit.
