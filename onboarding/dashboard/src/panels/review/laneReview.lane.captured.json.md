# dashboard/src/panels/review/laneReview.lane.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=2&lane=files` body of the MIK-L32 scratch leaf: the lane's two
destinations** (6,595 bytes; test evidence for `laneFocus.test.ts` and `ReviewSurface.lane.test.tsx`).

## Code Commentary

### Logic

- `measured`: 7 changed = 3 attributed + 3 unexplained + 1 of unknown attribution, and `paths` with every path's
  bucket (ruling Q1).
- `Unexplained changes` (5 files · 3 hunks · 2 non-text): `CONTRIBUTING.md`, `docs/scratch-lane.bin` (binary, gate
  `unexplained`) and the new module, then the attributed retention module (1 unexplained of 2 hunks) and
  `review_family_rosters.py` (mode-only, gate `unexplained`).
- `Unknown attribution` (1 file · 1 hunk): `review_source_admission.py`, whose four entries are all
  `recorded_blob_mismatch` on both sides.
- Re-captured after review R1 F4: only the admission row's reason and its two `unknown_reasons` changed wording (the
  count-then-list form).

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

- The totals and every path's bucket. [1]
- The `Unexplained changes` destination and its totals. [2]
- The `Unknown attribution` destination, with the entries recorded at an older blob. [3]
- The receipt row for this body. [4]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
