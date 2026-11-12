# dashboard/src/panels/review/laneReview.trees.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real leaf-wide `GET /api/review/trees?comparison=2` body of the MIK-L32 scratch leaf** (86,687 bytes; test evidence
for `ReviewSurface.lane.test.tsx`, where it is the slower read that supplies the gate's worklist).

## Code Commentary

### Logic

- `state: "trees"` for comparison 2 with the currentness per side, the knowledge diff and the computed, complete
  worklist of 21 items, among them the gate's two `unexplained_file` items (the new binary and the mode-only
  `review_family_rosters.py`) and three `unexplained_hunk` items (`CONTRIBUTING.md`, the retention helper and the new
  module).
- The focused retention file shows its gate item through `UnexplainedGroups` from this worklist.

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

- The comparison it was read from. [1]
- The worklist and its computed, complete state. [2]
- The gate's two `unexplained_file` items: the new binary and the mode-only module. [3]
- The receipt row for this body. [4]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
