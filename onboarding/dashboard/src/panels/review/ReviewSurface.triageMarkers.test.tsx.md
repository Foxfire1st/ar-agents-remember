# dashboard/src/panels/review/ReviewSurface.triageMarkers.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.triageMarkers.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite's statement: the merge round on real data, comparison 3 and its cards. | "MIK-L33 x MIK-L34 (the merge round)"; "triageMarker.cards.captured.json" | dashboard/src/panels/review/ReviewSurface.triageMarkers.test.tsx:1-31 |
| One membership statement on the followed member, below the way back. | "states the followed unknown membership once on the member, below the way back" | dashboard/src/panels/review/ReviewSurface.triageMarkers.test.tsx:165-205 |
| j after a marker return, focus never taken back by the hold. | "moves with j after a marker return, never taking focus from the held return first" | dashboard/src/panels/review/ReviewSurface.triageMarkers.test.tsx:207-252 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new merge-round surface test (2 cases), recording ruling 2026-09-30T17:47:43's merge plan, the merge round (21:41:02) and R3-1 (21:55:02). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
