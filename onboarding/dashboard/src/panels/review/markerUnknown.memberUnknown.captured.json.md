# dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent` review of INV-Z66EMHMH on comparison 3 of the MIK-L34 scratch leaf** (102,922 bytes; test
evidence for `ReviewSurface.markers.test.tsx` and, since MIK-L33's merge round, `ReviewSurface.triageMarkers.test.tsx` and `MarkerTargetState.test.tsx`: the review a family-named unknown
target opens).

## Code Commentary

### Logic

- The review still composes FAM-4V4GSQCS's context (`recorded`, one family), so a family-named unknown target lands on
  that family's member row, which carries the `Attribution unknown` state; a family-less target of the same invariant
  shows the state above the tree (review R1 F3).
- The limitations name `review:trees:3` and `knowledge-index:after:partial`.
- **`change_kinds` (MIK-L33):** guarantee `unknown` and `members_total` absent, because the after side's
  FAM-4V4GSQCS record does not parse; every one of the five members has membership `unknown` with that record as its
  `membership_reasons`; INV-Z66EMHMH, INV-EJW15DXA and INV-ZJS1XY4R read `implementation` `+unknown` (the unknown mark
  is the membership), INV-QR24S1VH and INV-DA7D417G `unknown`. So on a tree comparison the followed member row states
  its unknown membership once, as the tagged membership line with the comparison's reason (MIK-L33 merge round).

- **Re-captured in MIK-L33's merge round** over the merged tree (MIK-L34 landed; the review route now carries `change_kinds`). Against MIK-L34's capture it differs only by scratch paths, the converted memory commit, timestamps and comparison digests, and it now carries FAM-4V4GSQCS's `change_kinds` (the reviewer's structural diff, review R3 point 5).

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

- The composed family context. [1]
- The comparison token and the partial after index. [2]
- The receipt row for this body. [3]
- The family's change facts with every membership unknown (MIK-L33). [4]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
