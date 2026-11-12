# dashboard/src/panels/review/laneReview.file.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=2&file=mcp/src/agents_remember/application/review_comparison_retention.py`
body of the MIK-L32 scratch leaf: one per-file classification** (5,098 bytes; test evidence for `laneFocus.test.ts`
and `ReviewSurface.lane.test.tsx`).

## Code Commentary

### Logic

- `attributed`, 2 hunks: the edit inside `_side_binding` (before 418,1 / after 418,1) is `linked` through
  `RLZ-D2SEVSM9` on both sides (range 410-435; `INV-9BH2BNCT` revision 2 with its keys; `FAM-XZ5BR65G` revision 3,
  `member`); the appended helper (before 571,0 / after 572,6) is `unexplained` (post-curation: the entries were
  re-recorded at the candidate blob).
- Both sides list the three entries at their recorded blobs with their ranges.

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

- The per-file response. [1]
- The linked edit and its link with revision and family occurrence. [2]
- The unexplained appended helper. [3]
- The receipt row for this body. [4]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
