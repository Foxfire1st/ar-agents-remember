# dashboard/src/panels/detail-panel/intentReviewEntry.attribution.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/detail-panel/intentReviewEntry.attribution.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The task entry's unexplained-changes count (MIK-R32 rule 9), 8 cases.** The real `IntentReviewEntry` reads the
real served summary of the MIK-L32 scratch leaf (`panels/review/laneReview.summary.captured.json`); the state table
derives each other state from that body by setting an `attribution` the owner's vocabulary defines (counted, partial,
unavailable), so every row is a shape the route can answer. Only `fetch` is stubbed.

## Code Commentary

### Logic

- **Case 1, real data.** The entry reads `+0 −0` and, as its own element, `· 3 unexplained · 1 unknown`; neither
  element contains the other; exactly one request was made (`/api/review/intent/summary`), so the count is asked
  together with the intent counts and no more eagerly.
- **Cases 2-7, the state table (`it.each`):**
  - unexplained only → `· 3 unexplained`;
  - unknown with zero unexplained → `· 0 unexplained · 2 unknown` (K shown even when 0);
  - nothing unexplained or unknown → nothing;
  - a partially measured change set → `· attribution partial`, with the disclosure naming the unmeasured path;
  - an unmeasured change set → `· attribution unknown`;
  - a dataset comparison (no `attribution`) → nothing.
- **Case 8.** While the summary is pending (`data-intent-state="loading"`), no attribution element is rendered:
  never a zero.

### Conventions

- The captured summary is read with `readFileSync` from the review panel's fixture directory.

### Invariants And Boundaries

- Proves rule 9 on the entry: the count is a separate fact from `+N −N`, read in the same request, and an
  unmeasured or pending state never reads as zero. The mutations "0/0 shown" and "partial shows a count" are caught.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real summary, and the state table's derivation from it. | "'../review/laneReview.summary.captured.json'" | dashboard/src/panels/detail-panel/intentReviewEntry.attribution.test.tsx:1-23 |
| Case 1: two elements, one request. | "shows the real leaf's unexplained and unknown files beside +N −N, from the one summary read" | dashboard/src/panels/detail-panel/intentReviewEntry.attribution.test.tsx:55-66 |
| Cases 2-7: each state as its own rendering. | "renders %s as its own state" | dashboard/src/panels/detail-panel/intentReviewEntry.attribution.test.tsx:70-136 |
| Case 8: nothing while pending. | "shows nothing while the summary is pending: never a zero" | dashboard/src/panels/detail-panel/intentReviewEntry.attribution.test.tsx:138-148 |
| The entry's count and its details under test. | `attributionText`; `AttributionCount`; `AttributionDetails` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:70-110 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new entry test module (8 cases, MIK-R32 rule 9). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
