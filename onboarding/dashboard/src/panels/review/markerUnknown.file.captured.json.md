# dashboard/src/panels/review/markerUnknown.file.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=3&file=mcp/src/agents_remember/serving/notes.py` body of the MIK-L34 scratch
leaf after `break-family`** (10,176 bytes; test evidence for `ReviewSurface.markers.test.tsx` and, since MIK-L33's merge round, `ReviewSurface.triageMarkers.test.tsx` and
`MarkerTargetState.test.tsx`).

## Code Commentary

### Logic

- The same two hunks as comparison 2, now with unknown memberships: in L124, INV-Z66EMHMH's before-side FAM-4V4GSQCS
  occurrence and its after-side occurrence (no family) are `membership_unknown`; INV-413DC8XE is `confirmed_no_family`
  before and `membership_unknown` after, so the four occurrences of ruling Q3 sit in one list. In L210 the two
  FAM-4V4GSQCS occurrences are unknown and INV-SMYSQKTJ stays confirmed.
- The after knowledge side's index is `partial`, naming the unparsable family record.

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

- The per-file response with the unknown memberships. [1]
- The partial after index and its problem. [2]
- The receipt row for this body. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
