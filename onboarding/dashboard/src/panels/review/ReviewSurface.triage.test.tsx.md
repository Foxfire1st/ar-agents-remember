# dashboard/src/panels/review/ReviewSurface.triage.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

`j` in the mounted reviewer (requirement MIK-R33), over the served bodies of the store-authored comparison (`triage.family`, `triage.memberA`, `triage.memberH` and `triage.entries`; receipt `triage.capture-provenance.json`). `ReviewSurface` is the real component and only `fetch` is stubbed. 1 case.

## Code Commentary

### The case

- The reviewer opens on the family. The center's member list follows the tree's displayed order, in triage order and, after one click on the order control, in authored order; a second click returns to triage order.
- The family's row is focused and `j` is pressed. The member review of the next change is read, as a click would read it; its row is marked `aria-current` and has focus; the workspace is the same DOM node; and the family's breakdown is still on screen.
- A second `j` selects the following change, again with the mark and focus on its row and the same workspace node.

### How the case stays stable on a loaded machine

- Async conditions use the shared Testing Library guard; the Vitest configuration owns the test and hook hang guards. The case still waits for the displayed order and selection conditions rather than elapsed time.
- After each click on the order control the case waits until the control's `data-order` shows that click's order (`authored`, then `triage`), because the control computes the next order from the one it shows.
- The first `j` is pressed again until the selection moves, because the keymap's binding is a passive effect and a press made before it has run is ignored, as in a browser.

### Logic

- A `j` move selects the next change's subject exactly as a click does (the member review read for that subject) and
  keeps the family context, the focus on the moved-to node and the mounted workspace node (ICR-R32 rule 6, ICR-L48).
- The centre's member list follows the tree's displayed order, in triage and in authored order (review R1 note;
  `FamilyReviewCenter.FamilyCenter`).

### Conventions

Vitest with Testing Library. Requests for the tree view and for source content get a typed refusal, because they are outside this check; a review request for a subject without a body throws.

### Invariants And Boundaries

Selection moves keep family context, focus and the mounted workspace.

### Todos

No additional work is asserted by this card.

## Evidence

- The suite's statement, its bounds and its stubbed reads. [3]
- The one case: the center's order in both orders with a wait after each click on the order control, the two moves, and the kept context, focus and workspace. [4]

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

| Restored finding | Primary anchor | Tip range |
| --- | --- | --- |
| The suite's statement and its stubbed reads. | `beforeEach` | dashboard/src/panels/review/ReviewSurface.triage.test.tsx:1-60 |
| The one case: the move, the kept context, focus and workspace, and the centre's order. | `moves the selection to the next change and keeps family context, focus and workspace` | dashboard/src/panels/review/ReviewSurface.triage.test.tsx:62-132 |

### Cross-Repo References

No cross-repo boundary is crossed by this file.
