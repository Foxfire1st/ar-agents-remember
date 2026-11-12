# dashboard/src/panels/review/laneReview.task.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent` body of the MIK-L32 scratch leaf: the task-context review of tree comparison 2**
(16,922 bytes; test evidence for `ReviewSurface.lane.test.tsx`).

## Code Commentary

### Logic

- The payload's limitations include `review:trees:2`, so the surface reads the lane of comparison 2.
- Its source inventory lists the seven changed paths. The landed R04 accounting in the payload lists
  `attributed_changed_paths` (the retention and rosters modules) and `unattributed_changed_paths` (five paths, including
  `review_source_admission.py` and the proof-linked test) and counts 0 unknown: the lists the lane's classification
  replaces on a tree comparison (ruling Q1 for the explorer, review R1 F1 for the technical details). The surface test
  asserts these landed lists to prove the rendered labels do not come from them.

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

- The tree comparison this review names. [1]
- The landed accounting's lists and counts. [2]
- The receipt row for this body. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
