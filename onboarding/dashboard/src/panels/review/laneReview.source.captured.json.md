# dashboard/src/panels/review/laneReview.source.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent/source-content` body of the MIK-L32 scratch leaf: both exact blobs of
`review_comparison_retention.py` at the listed generation** (53,371 bytes; test evidence for `ReviewSurface.lane.test.tsx`,
where the focused hunk's window is cut from it).

## Code Commentary

### Logic

- `state: "content"`, admission `changed`, currentness `current`, language `python`; the before blob `87c7c5dc…`
  (24,801 bytes) and the after blob `99f7742a…` (24,961 bytes), both `present` and not truncated.

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

- Both sides' exact blobs, complete. [1]
- The receipt row for this body. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
