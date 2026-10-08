# dashboard/src/panels/review/ReviewSurface.triageMarkers.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-L33 with MIK-L34 in the mounted reviewer, on real data (the merge round):** following an intent marker to a member
whose membership is unknown, the member's one membership statement, the shared sticky offset while the way back is
open, and `j` after a return. The bodies are MIK-L34's scenario rebuilt under `/tmp/mik-l33-merge` and re-captured over
the merged tree, comparison 3 (`markerUnknown.*`), and that comparison's expression cards (`triageMarker.cards`); the
one synthetic body is the empty subject catalogue. 2 cases.

## Code Commentary

### Logic

- **Case 1:** following notes.py:124's "FAM-4V4GSQCS r1 · membership unknown" opens INV-Z66EMHMH's row with one
  membership statement (the tagged **Attribution unknown** line with the comparison's reason; no
  `review-member-target-state`), its name the served statement plus " · before only" and its description "impl +unknown
  Attribution unknown opened from an intent marker · membership unknown: …" with "Attribution unknown" once (R3-1); the
  workspace carries `data-marker-return` and the triage bar is present; Back returns focus to the hunk.
- **Case 2:** from Z66's card, following INV-413DC8XE's "No recorded family" and pressing Back holds focus on the
  card's marker; `j` then focuses and selects the next change, and the released hold does not take focus back.

### Conventions

Vitest with Testing Library over real captured bodies; unanswered reads are held, as a slow one is.

### Invariants And Boundaries

Proves the merged statement on real data (candidate invariant on `ChangeBadges.tsx.md`) and that `j` never has focus taken from it by L34's released hold.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The suite's statement: the merge round on real data, comparison 3 and its cards. [1]
- One membership statement on the followed member, below the way back. [2]
- j after a marker return, focus never taken back by the hold. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.


### Clock And Settlement Evidence

- Before J, fake animation frames leave the returned marker focused while the return hold is active. J releases that hold and focuses the next triage row; after the selected reply/effects are flushed and another frame advances, the next row remains focused. The released return hold does not steal focus back. [4]
