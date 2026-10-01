# dashboard/src/panels/review/markerReturn.file.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=2&file=mcp/src/agents_remember/serving/notes.py` body of the MIK-L34 scratch
leaf: one per-file classification** (10,093 bytes; test evidence for `ReviewSurface.markers.test.tsx`,
`hunkMarkers.test.ts` and `intentMarkerScope.test.ts`).

## Code Commentary

### Logic

- `attributed`, 2 hunks, both `linked`. The L124 edit (before 124,1 / after 124,1) meets INV-Z66EMHMH (RLZ-7X2C4VRQ,
  FAM-4V4GSQCS `member`) and INV-413DC8XE (RLZ-DCXK7W7T, `confirmed_no_family`) on both sides: the marker `2 intents`.
- The L210 deletion (before 210,1 / after 209,0) meets three entries through the before side only: INV-EJW15DXA
  (FAM-4V4GSQCS `member`), INV-ZJS1XY4R (`removed_or_reassigned`) and INV-SMYSQKTJ (`confirmed_no_family`): the
  marker `3 intents`.
- Both knowledge sides' indexes are `complete`.

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

- The per-file response and its two hunks. [1]
- The two knowledge sides, both indexes complete. [2]
- The receipt row for this body. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
