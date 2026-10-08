# dashboard/src/panels/review/ReviewSurface.walkFresh.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Which selections keep the walked family tree and which start it afresh (requirement MIK-R39 rule 9), plus the stacked-layout reveal of an in-tree read (OR-R033, OR-R042), in the mounted reviewer on real data (`walkReal.capture-provenance.json`). `ReviewSurface` is the real component and only `fetch` is stubbed. 21 cases.

Most cases start from `keptState()`: the reader has walked from the shared member INV-2TQGXFAX to its second family FAM-2HBJREC2, so the first family FAM-R6R095RW is a kept family. Each case then makes one selection and reads what the tree shows.

## Code Commentary

### Selections that start afresh

- **A row of the list of all invariants.** Already at the click, before the answer, the kept family is gone and the tree shows only the family of the answer on screen; the answer then shows the chosen invariant's own family, with no kept tag.
- **The catalogue row of the family already selected.** The tree shows that family alone at once, no review request is made, and focus ends on the selected row.
- **"All source changes".** No family is shown, and the tree stands after the catalogue's rows as a child of the navigation section.
- **A refresh of the review.** The kept family is gone at the click; one review request follows, and the tree still shows the selected family alone.
- **An answer of another comparison.** A member row of the kept family is clicked, and its answer names another after code tree. The notice beside the tree contains "comparison changed", and the tree shows only that answer's family, with no kept tag.
- **The offer to open the task context after a refusal.** While the refusal is shown every row is still there; clicking the offer drops the kept family at once, and the task context's answer then shows no family.
- **A followed intent marker and its return.** The marker's subject is shown with its own family only; the way back restores the earlier family alone and brings no kept family back.
- **The opening subject and a late catalogue.** Opened with no subject and a catalogue that answers after the bounded wait, the reviewer first shows the task context and then the first family alone, with no kept tag.

### Selections and actions that keep

- **A refused read of a selected subject.** The tree keeps both families and the kept tag, the mark is on the requested row, and `k` works from it with one review request.
- **A failed read of a selected subject.** The tree keeps both families and the tag, with the mark on the requested row. After the retry answers, both families are still shown; the second family is now the kept one and the first is not.
- **An answer that composes no family context.** Both families stay and both are tagged as kept, the requested row is marked, and above the tree stands "For the selected subject: The selected invariant has no recorded family membership."
- **Actions that change nothing.** The order control, a refresh of the subject catalogue, opening a file of the source explorer and a lane destination leave the families and the kept tags as they were and make no review request.

### The reveal on the stacked layout

Three cases pin the OR-R033 reveal, next to the scroll cases below. `recordingScrolls` records every element asked to come into view.

- **An in-tree read reveals the reading area only when stacked.** With the viewport shimmed to answer `(max-width: 60rem)` for `stacked=true`, clicking the second family's row scrolls the reading-area column into view, focus lands on the selected row, one review is read and the workspace is the same node. A key step (`k` onto the cached shared member) follows the same rule. With `stacked=false` nothing is scrolled, and the same subject chosen from the catalogue outside the tree scrolls nothing in either layout.
- **A moved focus is kept.** With the viewport stacked, a member row is clicked and its read is held; the family filter takes focus, then the read answers. Nothing is scrolled, focus stays in the filter, the answer is the selected subject's, and both families stay.

### The scroll after a refresh and after its retry

`recordingScrolls` records every element asked to come into view, because jsdom has no `scrollIntoView`. `inTheTurnOfAFailedRefresh(view, next)` makes a refresh fail and runs `next` from a mutation observer in the first microtask in which the failure is shown with its retry control, before React has run that commit's passive effects.

- After a refresh nothing is scrolled at the click; once the refreshed answer is shown the selected row is brought into view, and focus stays on the refresh control.
- **Forced order.** A member row is selected, and a mutation observer clicks refresh in the first microtask in which the member's answer is shown, before React has run that commit's passive effects. Nothing is scrolled at the click, and the selected row is brought into view only afterwards.
- A refresh whose read fails leaves the comparison last read on screen with the failure stated. A page of the subject read afterwards brings nothing into view.
- **The retry of a failed refresh.** The refresh fails and every effect has run. The retry control is clicked: nothing is scrolled at the click, the selected row is brought into view when the answer is shown, exactly one review request is made, the retry control is gone, and the tree shows the selected family alone.
- **A second refresh asked in the turn that shows the failure.** Its request stays, and the selected row is brought into view when it is answered.
- **A retry made in the turn that shows the failed refresh.** It is the refresh again all the same: the selected row is brought into view when it is answered.

### Helpers of this file

`keptState`, `catalogue` (a catalogue row by subject), `noKept`, `memberRow` (a member row of a family by label), `refusal` (a refused review body), `serveTreeRoutes` (serves the lane, the classification of `familyWalkMerge.ts` and its source content from `walkReal.lane`, `walkReal.file` and `walkReal.source`), `recordingScrolls` and `inTheTurnOfAFailedRefresh`.

## Evidence

- The kept state every case starts from. [18]
- Afresh at a row of the list of all invariants, at the moment of the selection. [19]
- Afresh at the catalogue row of the subject already selected, with focus on the selected row. [20]
- Afresh at "All source changes". [21]
- Afresh at a refresh of the review. [22]
- Afresh at an answer of another comparison, with the notice. [23]
- A refused read keeps every row and the mark; `k` works from it. [24]
- Afresh at the offer to open the task context. [25]
- A failed read keeps every row; the retry's answer leaves the tree whole. [26]
- Afresh at a followed intent marker; its return brings no kept family back. [27]
- The opening subject and a late catalogue show their own families only. [28]
- An answer without family context keeps the families and states the subject. [29]
- The order control, a catalogue refresh, opening a file and a lane destination keep the tree and read nothing. [30]
- A refresh brings the selected row into view once its answer is shown, without moving focus. [31]
- Forced order: a refresh asked before the previous answer's effects have run waits for its own answer. [32]
- A refresh whose read fails leaves no scroll request behind. [33]
- The retry of a failed refresh is the refresh again: the row is brought into view when it is answered. [34]
- A refresh asked in the turn that shows a failed read keeps its request. [35]
- A retry made in the turn that shows the failed refresh is the refresh again. [36]
- An in-tree read reveals the reading area only in the stacked layout, by click and by key; an outside selection scrolls nothing. [39]
- A stacked in-tree answer does not reveal after the reader moved focus while it was pending. [40]

- The refresh and retry handlers these cases pin. [37]
- The selection that decides keeping or starting afresh. [38]


### Clock And Settlement Evidence

- The late-catalogue opening case advances the imported `SUBJECT_HOLD_MS` on fake time before checking task context, then releases the held catalogue in async `act` before checking the fresh first-family tree. Those assertions follow actual product-hold and response opportunities rather than a local real-time wait. [41]
