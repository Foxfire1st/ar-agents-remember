# dashboard/src/panels/review/laneReview.summary.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent/summary` body of the MIK-L32 scratch leaf: the changed-intent counts and the lane's
entry count together** (579 bytes; test evidence for `detail-panel/intentReviewEntry.attribution.test.tsx`).

## Code Commentary

### Logic

- `state: "counted"` with the intent counts (`realization_only: 1`, every other count 0, so the entry reads `+0 −0`) and
  `attribution`: `counted`, 7 changed = 3 attributed + 3 unexplained + 1 of unknown attribution, nothing unmeasured
  (the entry reads `· 3 unexplained · 1 unknown`).

### Conventions

Keep the captured bytes and their receipt (`laneReview.capture-provenance.json`) intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the scratch copies under `/tmp/mik-l32-real` (code at `b54d1b03` with the scratch leaf's edits;
memory `58d016cb` converted), not current project knowledge; its line numbers and blobs are the scratch tree's.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The lane's count on the summary. [1]
- The receipt row for this body. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
