# dashboard/src/panels/detail-panel/intentReviewEntry.attribution.test.tsx

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The real summary, and the state table's derivation from it. [1]
- Case 1: two elements, one request. [2]
- Cases 2-7: each state as its own rendering. [3]
- Case 8: nothing while pending. [4]
- The entry's count and its details under test. [5]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
