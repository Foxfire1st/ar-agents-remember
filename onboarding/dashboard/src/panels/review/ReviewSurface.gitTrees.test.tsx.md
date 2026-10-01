# dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R25 rule 6 and MIK-R31 on real data: the review workspace over a converted leaf's Git trees, with the focused
expression cards (4 cases).** The five bodies (`gitTrees.family`, `gitTrees.invariant`, `gitTrees.entries`,
`gitTrees.cards` and the leaf-wide `../../data/reviewTrees.captured.json`) are the real served answers of the
reviewer routes for the MIK-L31 worker's scratch copy after conversion (a leaf that edits `_not_listed`, re-anchors
RLZ-CXH58B4W, adds a scratch-authored proof and declares two expected effects); each memory side was read through the derived index of its
tree, never a dataset copy. `ReviewSurface` is the real component and only `fetch` is stubbed: the workspace and its
navigation behave exactly as over datasets.

## Code Commentary

### Logic

- **The stub** answers `/trees` with the cards body when the request names `invariants`, with `withoutLane(leafWide)`
  when it names `lane` (MIK-L32: these captures predate the lane, so the lane read is answered with the comparison and
  no lane, which the tree's destinations show as unavailable, never as a zero), and with the leaf-wide body otherwise;
  it records every requested URL. The case-2 finder of the leaf-wide read excludes the lane read.
- **Case 1 (MIK-R25 rule 6):** the family payload declares `review:trees:1`; the family centre renders; the
  complete source inventory holds the one changed file (`review_source_admission.py`); the family renders its whole
  7-member roster from the memory trees' indexes; opening the touched member reads its own review and shows its
  statement, still under the same family, and its cards start with its own entries (RLZ-CXH58B4W, then PRF-7Q3M5K:
  the MIK-R01 seed).
- **Case 2 (the packet's conforming example on real data):** the cards read names comparison `1` and all 7 member
  identities; the leaf-wide read is pinned to comparison `1` with no `history` (review F11); no whole-file
  accordion; 11 cards, 1 changed and 10 unchanged; in `review_source_admission.py` exactly four cards in family
  order (RLZ-CXH58B4W changed at `L194–213`, RLZ-D43E5CF2, RLZ-9EC7B6PN, RLZ-NM6160PK unchanged), each with its
  role and its own rationale (4 distinct), the rationale before the excerpt in the DOM and the changed excerpt a
  diff; the proof card shows "Test proof · facet" (the boundary example); the touched member's voice carries
  MIK-R11's "touched invariant · planned"; and the leaf's knowledge panel lists a `planned_untouched` item. Since
  MIK-L32 it also asserts that the lane's destinations follow the families and read `unavailable` (twice), that the
  explorer labels the one changed file `Attribution unknown` (no bucket it did not measure; ruling
  2026-09-30T12:19:20 Q1), and that the technical details say unknown too (`data-attribution-state="unknown"`, review
  R1 F1).
- **Case 3 (preservation):** a dataset review (`familyReview.complete`, no `review:trees:<n>`) makes no `/trees`
  request, mounts no cards and no knowledge panel, and renders the landed file view. Since MIK-L32 it also asserts no
  lane destinations, explorer labels equal to the landed accounting's path by path, and the technical details'
  landed count and "changed paths with no registered attribution" list word for word
  (`data-attribution-source="landed"`, no unknown list).
- **Case 4 (review R2-3):** a leaf-wide body answering comparison 2 against a payload for comparison 1: the panel
  states "this view reads comparison 2, the review shows comparison 1" and no card voice carries a planned or
  unplanned mark (removing the `same` check in `pinnedWorklist` fails it).

### Conventions

- The 124 existing review-panel cases were rerun unchanged (worker and reviewer, rounds 1–6).

### Invariants And Boundaries

- Case 1 is MIK-R25's Expected Evidence "UI test on real data after conversion"; case 2 is MIK-R31's conforming
  example on real data; cases 3 and 4 prove the candidate invariants "dataset reviews make no tree read" and "card
  planning marks come only from a leaf-wide read of the same comparison" (recorded on `FamilyReviewCenter.tsx` and
  `data/reviewTrees.ts`).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` and its rulings
(`25_reviewer-on-git-trees.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The five real bodies, including the cards read and the leaf-wide tree view. [1]
- The stub: cards body for a named selection, a lane-less answer for the lane read (MIK-L32), leaf-wide body otherwise, every URL recorded. [2]
- Case 1: the family review from trees, then the touched member with its own entries first. [3]
- Case 2: the conforming example as focused cards, pinned reads, marks and the knowledge panel; the lane unavailable and never a zero, and the explorer and details unknown (MIK-L32). [4]
- Case 3: a dataset review makes no tree read, and keeps the landed explorer labels and details (MIK-L32). [5]
- Case 4: no planning mark from another comparison's read (R2-3). [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
