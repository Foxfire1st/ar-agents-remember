# dashboard/src/panels/review/markerReturn.source.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent/source-content` body for `serving/notes.py` of the MIK-L34 scratch leaf at trees
`59daf505` → `db68db54`** (28,595 bytes; test evidence for `ReviewSurface.markers.test.tsx`). Its bytes are identical
to `markerUnknown.source.captured.json` (the same content at the same trees).

## Code Commentary

### Logic

- `content`, status `modified`, `current`: the before blob `e3e6f8d4` (12,923 bytes) and the after blob `9019bea5`
  (12,848 bytes), both `present` with their whole texts, the exact objects the classification names, so
  `describesDrawn` holds and the marks are placed.

- **Re-captured in MIK-L33's merge round** over the merged tree (MIK-L34 landed; the review route now carries `change_kinds`). Against MIK-L34's capture it differs only by scratch paths, the converted memory commit, timestamps and comparison digests (the reviewer's structural diff, review R3 point 5).

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the scratch copies under `/tmp/mik-l33-merge`: MIK-L34's scenario, rebuilt by MIK-L33's merge round with MIK-L34's own scripts (code `59daf505` with the scratch leaf's edits and the same curated blobs `9019bea5` and `b6d07091`; memory `76f5e91e1` converted and committed as scratch `main` `31ab7016`), not current project knowledge; its line numbers, blobs and keys are the scratch tree's.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The expansion: both sides present with the object ids the classification names. [1]
- The receipt row for this body. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
