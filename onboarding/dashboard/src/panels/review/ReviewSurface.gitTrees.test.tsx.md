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
- **Case 1:** the converted capture declares `review:trees:1`; the family centre renders with scope text `1 changed files` and no inline inventory entry. Its seven recorded member openers remain; selecting the touched member shows its statement, retained family, and its realization/proof cards first.
- **Case 2:** cards and the leaf-wide read are pinned to comparison 1 with no history selector. The family has 11 cards (1 changed, 10 unchanged), four in the edited file in family order with distinct rationales, the changed range and excerpt diff, proof facet and planning voice. The subject's own worklist is separate; both attribution destinations are explicitly unavailable. Opening Worklist shows `planned_untouched` and no patch `pre`. No explorer labels or technical attribution lists are asserted.
- **Case 3:** the dataset-shaped captured review declares no tree token, makes no trees request and mounts no cards, leaf-knowledge panel, lane destinations or inline inventory entry. The landed expression file view remains; its remaining-count block is open and uses landed attribution plus the captured unattributed count.
- **Case 4:** a leaf-wide answer for comparison 2 beside the review for comparison 1 names the mismatched comparison in the subject-worklist view; nonempty card voices carry neither planned nor unplanned marks.

### Conventions

- The 124 existing review-panel cases were rerun unchanged (worker and reviewer, rounds 1–6).

### Invariants And Boundaries

- Case 1 is MIK-R25's Expected Evidence "UI test on real data after conversion"; case 2 is MIK-R31's conforming
  example on real data; cases 3 and 4 prove the candidate invariants "dataset reviews make no tree read" and "card
  planning marks come only from a leaf-wide read of the same comparison" (recorded on `FamilyReviewCenter.tsx` and
  `data/reviewTrees.ts`).

### Todos

No additional work is asserted by this card.

The world serves captured entries, cards, leaf trees and lane answers with per-route replies, distinguishing member and family card sets by the requested invariants. Cases assert the touched member's rationale, excerpt and proof voices, the unchanged remainder labels, the dataset file view without tree requests, and the cross-comparison planning-mark refusal on the R2-3 regression.
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
- Case 2: comparison-pinned focused cards, planning marks, subject worklist and unavailable destinations; Worklist renders delivered items without patches. [4]
- Case 3: dataset-shaped review makes no tree read, keeps the expression file view and open landed remaining counts. [5]
- Case 4: no planning mark from another comparison's read (R2-3). [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
- Changed-invariants fixture for the converted leaf [7]
- Per-route captured world with member and family cards [8]
- Touched member resolution in the rendered centre [9]
- Leaf-wide remaining counts beside the cards [10]
