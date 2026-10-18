# dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

The tree-review cases consume the retained L37 comparison-5 captures and assert three members, twelve cards, revision identities, a statement-diff marker, proof identity and excerpt kind, selected-member-first grouping and worklist item-kind equality. The fixture refuses source-content reads; these assertions do not compare exact source bytes or statement operands.

## Code Commentary

The tree-review cases consume the retained L37 comparison-5 captures and assert three members, twelve cards, revision identities, a statement-diff marker, proof identity and excerpt kind, selected-member-first grouping and worklist item-kind equality. The fixture refuses source-content reads; these assertions do not compare exact source bytes or statement operands. The dataset fallback case is removed. Successful playback of this historical full-tree fixture is not current producer acceptance.

### Declared Assertions

- `it('renders a converted leaf family review from its trees and opens the touched member', async () => {`
- `it('shows the current family as focused cards with changed and unchanged expressions', async () => {`
- `it('takes no planning mark from a leaf-wide read of another comparison (review R2-3)', async () => {`

This is a declaration inventory, not a collected parametrized-case total or execution result.

### Evidence Boundary

The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.

## Prior Fixture Account — Historical Only

The following account describes the earlier fixtures and assertion scope. Its present-tense clauses and numbered labels are historical, not current guarantees, current evidence or a fresh run. The current source account above states what is still exercised and what was removed.

> # dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> **MIK-R25 rule 6 and MIK-R31 on real data: the review workspace over a converted leaf's Git trees, with the focused
> expression cards (4 cases).** The five bodies (`gitTrees.family`, `gitTrees.invariant`, `gitTrees.entries`,
> `gitTrees.cards` and the leaf-wide `../../data/reviewTrees.captured.json`) are the real served answers of the
> reviewer routes for the MIK-L31 worker's scratch copy after conversion (a leaf that edits `_not_listed`, re-anchors
> RLZ-CXH58B4W, adds a scratch-authored proof and declares two expected effects); each memory side was read through the derived index of its
> tree, never a dataset copy. `ReviewSurface` is the real component and only `fetch` is stubbed: the workspace and its
> navigation behave exactly as over datasets.
>
> ## Code Commentary
>
> ### Logic
>
> - **The stub** answers `/trees` with the cards body when the request names `invariants`, with `withoutLane(leafWide)`
>   when it names `lane` (MIK-L32: these captures predate the lane, so the lane read is answered with the comparison and
>   no lane, which the tree's destinations show as unavailable, never as a zero), and with the leaf-wide body otherwise;
>   it records every requested URL. The case-2 finder of the leaf-wide read excludes the lane read.
> - **Case 1:** the converted capture declares `review:trees:1`; the family centre renders with scope text `1 changed files` and no inline inventory entry. Its seven recorded member openers remain; selecting the touched member shows its statement, retained family, and its realization/proof cards first.
> - **Case 2:** cards and the leaf-wide read are pinned to comparison 1 with no history selector. The family has 11 cards (1 changed, 10 unchanged), four in the edited file in family order with distinct rationales, the changed range and excerpt diff, proof facet and planning voice. The subject's own worklist is separate; both attribution destinations are explicitly unavailable. Opening Worklist shows `planned_untouched` and no patch `pre`. No explorer labels or technical attribution lists are asserted.
> - **Case 3:** the dataset-shaped captured review declares no tree token, makes no trees request and mounts no cards, leaf-knowledge panel, lane destinations or inline inventory entry. The landed expression file view remains; its remaining-count block is open and uses landed attribution plus the captured unattributed count.
> - **Case 4:** a leaf-wide answer for comparison 2 beside the review for comparison 1 names the mismatched comparison in the subject-worklist view; nonempty card voices carry neither planned nor unplanned marks.
>
> ### Conventions
>
> - The 124 existing review-panel cases were rerun unchanged (worker and reviewer, rounds 1–6).
>
> ### Invariants And Boundaries
>
> - Case 1 is MIK-R25's Expected Evidence "UI test on real data after conversion"; case 2 is MIK-R31's conforming
>   example on real data; cases 3 and 4 prove the candidate invariants "dataset reviews make no tree read" and "card
>   planning marks come only from a leaf-wide read of the same comparison" (recorded on `FamilyReviewCenter.tsx` and
>   `data/reviewTrees.ts`).
>
> ### Todos
>
> No additional work is asserted by this card.
>
> The stub routes captured entries, the shared cards body for any named invariants, leaf-wide trees and a lane-less answer. The member-opening case checks its statement, family identity and first two entry IDs; the family case checks rationale/excerpt/proof voices and subject worklist. The dataset case alone checks the landed remaining-count block and no tree requests; the cross-comparison case refuses planning marks. These tests do not distinguish per-member card reply bodies or assert converted leaf-wide remaining-count labels.
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R25@v1` and its rulings
> (`25_reviewer-on-git-trees.json`) live outside the code and memory repositories, so they are named here and not
> cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.
>
> - The five real bodies, including the cards read and the leaf-wide tree view.  Anchor: "gitTrees.family.captured.json"; "gitTrees.invariant.captured.json"; "gitTrees.entries.captured.json"; "gitTrees.cards.captured.json"; "reviewTrees.captured.json" (historical reference 1)
> - The stub: cards body for a named selection, a lane-less answer for the lane read (MIK-L32), leaf-wide body otherwise, every URL recorded.  Anchor: "const withoutLane = (body: ReviewTreesResult) => ({"; "function serve(" (historical reference 2)
> - Case 1: the family review from trees, then the touched member with its own entries first.  Anchor: "renders a converted leaf family review from its trees and opens the touched member" (historical reference 3)
>
> - Case 2: focused cards, comparison-pinned reads, planning voices and subject/worklist view; both attribution destinations explicitly unavailable. No explorer-label or technical-details assertion is made. (historical reference 4)
>
>
> - Case 3: a dataset review makes no tree read, retains the landed expression file view and an open remaining-count block using landed attribution and the captured unattributed count. (historical reference 5)
>
> - Case 4: no planning mark from another comparison's read (R2-3).  Anchor: "takes no planning mark from a leaf-wide read of another comparison (review R2-3)" (historical reference 6)
> - Changed-invariants fixture for the converted leaf (historical reference 7)
>
> - Per-route captured world with one shared cards body for all named invariant selections (historical reference 8)
>
> - Touched member resolution in the rendered centre (historical reference 9)
>
> - Dataset remaining-count block; converted card cases do not assert leaf-wide remaining counts  Anchor: `remaining` (historical reference 10)

## Evidence


- The tree-review cases consume the retained L37 comparison-5 captures and assert three members, twelve cards, revision identities, a statement-diff marker, proof identity and excerpt kind, selected-member-first grouping and worklist item-kind equality. The fixture refuses source-content reads; these assertions do not compare exact source bytes or statement operands. The dataset fallback case is removed. Successful playback of this historical full-tree fixture is not current producer acceptance. [11]
