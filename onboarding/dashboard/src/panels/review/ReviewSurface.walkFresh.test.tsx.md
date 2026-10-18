# dashboard/src/panels/review/ReviewSurface.walkFresh.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Nineteen mounted walk-refresh test declarations, including the two-value stacked-layout case, replay immutable `walkReal` review bodies with a labelled synthetic outline. They distinguish clearing kept reads from deleting outline rows, preserve same-family/viewer returns, and pin scroll/focus request timing without measuring geometry.

Most cases start from `keptState()`: the reader has walked from the shared member INV-2TQGXFAX to its second family FAM-2HBJREC2, so the first family FAM-R6R095RW is a kept family. Each case then makes one selection and reads what the tree shows.

## Code Commentary

### Outline preservation and clearing kept reads

- Choosing the already selected family keeps both outline families, the kept tag and focus with no new read.
- All changes opens and returns from the comparison viewer without resetting the walk or reading subjects, restoring trigger focus.
- Refresh clears kept reads but preserves both complete outline families at the click and after one review reply.
- An answer whose code tree changes clears kept tags and announces the comparison change while the outline rows remain.
- The source-instead offer after refusal clears kept tags but retains both outline families; following a card marker and its return likewise do not restore old kept tags or remove the outline.
- A late catalogue following the bounded task-context read selects the first family with no kept tags, while both outline families remain.

### Selections and actions that keep

- **A refused read of a selected subject.** The tree keeps both families and the kept tag, the mark is on the requested row, and `k` works from it with one review request.
- **A failed read of a selected subject.** The tree keeps both families and the tag, with the mark on the requested row. After the retry answers, both families are still shown; the second family is now the kept one and the first is not.
- **No family context:** both outline families stay, both are kept and the requested row remains selected; the centre states No recorded family.
- **Non-subject actions:** order/view toggles, Worklist and filtered comparison destinations/Back retain the shown families/tags and make no subject review read.

### Panel-local reveal in either layout

Three cases pin the OR-R033 reveal, next to the scroll cases below. `recordingScrolls` records every element asked to come into view.

- **Panel-local reveal:** the two-value viewport shim exercises both layouts. An in-tree click, cached K step and same-row reselect each request no `scrollIntoView` calls. The case also asserts selection focus after the click, request count, the same workspace and retained outline families. It measures requests rather than geometry; its source points to `ReviewWorkspace.family.test.tsx` for the separate geometry evidence.
- **A moved focus is kept.** With the viewport stacked, a member row is clicked and its read is held; the family filter takes focus, then the read answers. Nothing is scrolled, focus stays in the filter, the answer is the selected subject's, and both families stay.

### The scroll after a refresh and after its retry

`recordingScrolls` records every element asked to come into view, because jsdom has no `scrollIntoView`. `inTheTurnOfAFailedRefresh(view, next)` makes a refresh fail and runs `next` from a mutation observer in the first microtask in which the failure is shown with its retry control, before React has run that commit's passive effects.

- After a refresh nothing is scrolled at the click; once the refreshed answer is shown the selected row is brought into view, and focus stays on the refresh control.
- **Forced order.** A member row is selected, and a mutation observer clicks refresh in the first microtask in which the member's answer is shown, before React has run that commit's passive effects. Nothing is scrolled at the click, and the selected row is brought into view only afterwards.
- A refresh whose read fails leaves the comparison last read on screen with the failure stated. A page of the subject read afterwards brings nothing into view.
- **Retry of failed refresh:** nothing scrolls at the click; once the answer is shown, the selected row is requested into view, one review read is made, Retry disappears and both outline families remain.
- **A second refresh asked in the turn that shows the failure.** Its request stays, and the selected row is brought into view when it is answered.
- **A retry made in the turn that shows the failed refresh.** It is the refresh again all the same: the selected row is brought into view when it is answered.

### Helpers of this file

Helpers retain kept-state/row readers, refusal replies, scroll-call recording and forced failure-turn sequencing. `serveTreeRoutes` adds an explicitly synthetic focused-entry card over captured lane/file/source bytes; the current source has no separate catalogue-row reset helper.

Kept-state and tree-row helpers pin the before and after of each journey, with a no-kept baseline for fresh starts. Tree routes serve lane, file, source, link and card answers per comparison, and scroll recording asserts the selected row comes into view without moving focus. Refresh, retry and failure cases assert kept-read clearing, scroll forgetting on failed reads, and view restoration on answered retries.
## Evidence


- The refresh and retry handlers these cases pin. [37]
- The selection that decides keeping or starting afresh. [38]


### Clock And Settlement Evidence

- The kept state every case starts from. [18]

- Reselecting the already-selected family preserves both families and its kept tag with no new read. [19]


- All changes opens and returns without resetting the walk or reading subjects; focus returns to the trigger. [20]


- Refresh clears kept reads while preserving both complete outline families at click and answer. [21]

- Afresh at a refresh of the review. [22]
- Afresh at an answer of another comparison, with the notice. [23]
- A refused read keeps every row and the mark; `k` works from it. [24]

- The offer to open task context clears kept tags but preserves both outline families at click and answer. [25]

- A failed read keeps every row; the retry's answer leaves the tree whole. [26]
- Afresh at a followed intent marker; its return brings no kept family back. [27]

- The late catalogue selects its first family with both outline families present and no kept tags. [28]

- An answer without family context keeps the families and states the subject. [29]

- Order/view, Worklist and filtered comparison destinations/Back preserve families/tags and issue no subject review read. [30]

- A refresh brings the selected row into view once its answer is shown, without moving focus. [31]
- Forced order: a refresh asked before the previous answer's effects have run waits for its own answer. [32]
- A refresh whose read fails leaves no scroll request behind. [33]
- The retry of a failed refresh is the refresh again: the row is brought into view when it is answered. [34]
- A refresh asked in the turn that shows a failed read keeps its request. [35]
- A retry made in the turn that shows the failed refresh is the refresh again. [36]
- The late-catalogue opening case advances the imported `SUBJECT_HOLD_MS` on fake time before checking task context, then releases the held catalogue in async `act` before checking the fresh first-family tree. Those assertions follow actual product-hold and response opportunities rather than a local real-time wait.  Anchor: `SUBJECT_HOLD_MS` [41]
- Tree row resolution in the mounted rail [42]
- Per-comparison tree routes for lane, file and cards [43]
- Failed-refresh turn helper for scroll expectations [44]
- Failed-refresh turn helper for scroll expectations [45]

- One layout-parametrized declaration exercises true and false viewport matches. Click, cached K and same-row reselect each assert an empty scroll-call list; the case also preserves focus, request-count, workspace and outline checks. It does not measure geometry. [39]
- The retained pending-answer case moves focus to the family filter before releasing the answer, then asserts that focus remains there, no scrolling occurs and both families remain. [40]
