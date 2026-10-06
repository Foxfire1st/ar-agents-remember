# dashboard/src/panels/review/ReviewSurface.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Compose the Intent Reviewer from one subject catalogue, one comparison read cycle and the family-centered workspace. The surface is read-only and produces no semantic judgment.

It decides three things:

- **which payload the workspace is mounted over**: the answer for the subject on screen or, while that subject is pending, failed or refused, the task context's last admitted answer (`frame`), so a selection never unmounts the workspace, its navigation or its open disclosures (`ICR-R24@v3`);
- **what every subject selection does**, including whether it keeps the walked family tree or starts it afresh (requirement MIK-R39);
- **what the reader's refresh does** beside re-reading.

## Code Commentary

### `useSurface`

`useSurface` wires the owners together:

- `useReviewNavigation` gives the recorded subjects and the selected subject. The selected subject's kind and identifier come from the navigation; the props only name the subject the reviewer opens with.
- It holds the reader state of this file: `instead` (the failure after which the reader chose the task context), `selection` (the page request), the `useWorkspaceState()` value and one `ReviewReadCache`, created once per mounted surface.
- `useReviewReadCycle` reads the review for the task context, the subject, the page request and the history view. `hold: navigation.settling` makes the first read wait for the catalogue's first subject, for at most the navigation's bound.
- The retained payload is shown only when its full target key (`targetKeyOf`) equals the key of the question on screen (`coherent`), and `shown` is `shownPayload(read, coherent)`.
- `useObservedComparison` reports the shown comparison to the navigation, which re-reads its catalogue only when the displayed snapshot pair changes.
- `useRefreshReview` gives the hook `refreshReview` and `retryReview` (below); the reading area's problem block and the surface's outcome region share the one `retryReview`.
- `reading` is computed with `readingStatusOf` only when a `frame` exists and no payload answers the question on screen. The status is keyed to the read cycle's target key and names the requested subject: `kind:id`, labelled from the catalogue entry when there is one, or "all source changes" for the task context. For a failed or refused read it carries the owner's `ReviewProblemBlock`, labelled with that subject, with retry for a failed read and the offer to open the task context for an intent-only refusal (`insteadFor`).

### Subject selection

`subjectSelection` builds the two selections the surface owns.

`selectSubject(subject, context, options)` is the `onSelect` the workspace and the navigation receive. In this order it:

1. leaves a focus request in the workspace state: the element that has focus now, and the number of the tree intent that is current before this selection (`after`);
2. calls `workspace.beginSelection(options?.keepTree === true)`. Only a caller that passes `keepTree` keeps the walked tree; every caller that passes no options starts it afresh. The workspace passes `keepTree` for a row of the tree and for a kept family's roster continuation. The catalogue rows, the list of all invariants, "All source changes" and an intent marker's follow and return pass none;
3. gives the subject to the navigation;
4. clears `instead`;
5. sets the page request to `options?.page`, which is absent for every selection except a kept family's roster continuation, so an ordinary selection also clears the earlier page request;
6. stores the chosen family context, or clears it.

`openTaskContext(failure)` is the offer shown after an intent-only refusal. It calls `beginSelection(false)`, so it starts the walked tree afresh, and sets `instead`.

### Refresh and retry

`useRefreshReview(workspace, read, refresh)` is called in `useSurface` and wraps the read cycle's `refresh`. It returns two handlers.

`refreshReview` is the handler of the refresh control. A refresh:

1. calls `beginSelection(false)`: the walked tree starts afresh, because a refresh shows the comparison as it reads now;
2. leaves a `scrollOnly` focus request, so that the selected row is brought into view once the refreshed answer is shown and focus stays where it is;
3. remembers the read that was on screen (`asked`), then re-reads.

`settle(read)` is the one rule for a refresh whose read has no answer. When the read on screen is failed or refused, is not the read remembered at the click, and a `scrollOnly` request is pending, it drops the request and remembers that read as the failed read of a refresh (`failed`). A refresh whose own read fails therefore leaves no request behind, and a later answer for the same subject (a page, a roster continuation) does not move the rail. A failure that was already on screen when the refresh was asked does not drop the request. An effect runs `settle` for every read.

`retryReview` is the handler of the retry control of a failed read, in the surface's own failure block and in the reading area's. It runs `settle` first, because a retry made in the turn that shows the failure comes before that turn's effects. Then:

- when the failure on screen is the remembered failed read of a refresh, the retry is the refresh again: it calls `refreshReview`, so the tree starts afresh and the scroll is asked for again;
- the retry of any other failed read (a selection's, a page's, a continuation's) only reads again. It makes no selection and leaves no focus request, so a retry after a failed in-tree selection keeps the walked tree.

`retryFor` offers the retry only for a failed read.

### `ReviewPanes`

`ReviewPanes` renders the workspace over `shown ?? (reading ? frame : null)` and passes `reading` only when nothing answers. It calls `useReviewLane` once, with the tree comparison number of the payload on screen, and hands the result to both `ReviewWorkspace` and `ReviewTechnicalDetails`, so every part of a tree comparison shows one classification. A dataset review names no tree comparison, and the hook is then called with no comparison number. `ReviewTechnicalDetails` receives the answer alone (or an `unanswered` label), so records are never shown under another subject, and the page controls are rendered only for an answer.

### The root and the header

`ReviewSurface` renders the root (`review-surface`):

- `data-kbzone="review"` makes it the keymap owner's reviewer zone; the family tree binds its `j`/`k` traversal on this element.
- `data-comparison`, `data-review-target` and `data-review-history` (`live` or the history view) identify what is shown. `data-review-pending` or `data-review-unavailable` carries the requested subject while it has no answer.
- The root is its own vertical scrollport (`height: 100%`, `minHeight: 0`, `minWidth: 0`, `overflowY: auto`).
- `useReaderEngagement` reports reader gestures on the root to `navigation.engage`.
- `ReviewReadCacheContext` provides the surface's cache to the source content rendered below.

`ReviewHeader` renders the back button, the leaf, a disclosure with the task and subject identifiers (`subjectLabel`), the refresh control, and, for the recorded history view, the line "Historical task comparison" (`review-history`). Its row wraps.

`ReviewOutcomeRegion` receives the read, `instead`, the shown payload, the last coherent payload only for a failed read, the retry, the offer of the task context, and `readingInWorkspace`, so a read the workspace states is stated once.

### The page controls

`PageControls` renders `PagePicker` (the walkable collections of `REVIEW_WALKABLE_COLLECTIONS`, and "whole review"), `PageActions` (a "next page" button only when the payload published a cursor, `continuationOf`; a "first page" button while a requested page is shown), `PageBoundsLine` (the bounds of the carried page, or the sentence that the whole review was read) and the reset line when the page carries one. When the requested page was refused (`refusedPageOf`), `PageRefusalBlock` shows the refusal's code and detail, its expected and observed values when present, its next action, and a button for the first page of the requested collection; the bounds line is then omitted.

### Conventions

- Exports: `ReviewTarget` and `ReviewSurface`.
- The record panes live in `ReviewRecordPanes.tsx`, the outcome states in `ReviewOutcome.tsx`, the refresh control in `ReviewRefresh.tsx`, the read cycle in `ReviewReadCycle.ts` and the workspace in `ReviewWorkspace.tsx`. This file composes them.
- No component of this file calls `useState`: the reader state is held by `useSurface`.
- The file is 679 lines.

### Invariants And Boundaries

- The surface names a task context, a subject, a page and a history view. It never names a dataset.
- A failed read may retain only the last coherent answer to the same question.
- The frame keeps only the shell: nothing of the frame's subject is passed on as the requested subject's reading or records.
- A selection never unmounts the workspace once a frame exists. Only the first read, which has no frame, is stated at the surface level.
- Every selection made through `selectSubject` without `keepTree`, the offer of the task context, a refresh and the retry of a failed refresh start the walked tree afresh. The retry of any other failed read does not.

## Evidence

- The surface's hook: navigation, reader state, the cache, the read cycle, the coherent payload, the refresh and retry handlers and the reading status. [32]
- A selection leaves its focus request, numbers the tree intent with or without `keepTree`, selects the subject, and sets or clears the page request; the offer of the task context starts the tree afresh. [33]
- A refresh starts the walked tree afresh and asks for a scroll once its answer is shown; the request is dropped when the refresh's own read fails or is refused; the retry of that failed read is the refresh again, and the retry of any other failed read only reads again. [34]
- The unanswered subject's status, keyed and labelled with the requested subject. [35]
- The workspace over the answer or the frame, the records only for an answer, and the one lane read handed to both. [36]
- The root: the reviewer zone, the identity and pending attributes, the scrollport, the engagement observer, the cache provider, and the refresh and retry handlers handed to the header and the outcome region. [37]
- The header: back, leaf, identifiers, refresh and the history line. [38]
- The offer of the task context exists only for an intent-only refusal with no earlier offer taken. [39]
- Retry exists only for a failed read. [40]
- The page controls: picker, actions, bounds, refusal and reset. [41]
- The picker offers the walkable collections. [42]
- A next page is offered only for a published cursor. [43]
- The refusal of a requested page, with a first page of that collection. [44]
- The workspace state the selections write: the focus request and the tree intent. [45]
- The selection options a caller may pass. [46]
- The mounted cases of which selections keep the walked tree and which start it afresh, of the stacked reveal of an in-tree read, and of the scroll after a refresh and after the retry of a failed refresh. [47]
- The mounted cases of the mounted shell, the pending and problem states and the focus order. [48]
