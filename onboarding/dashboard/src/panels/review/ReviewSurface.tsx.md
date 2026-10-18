# dashboard/src/panels/review/ReviewSurface.tsx

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Compose one subject catalogue, keyed review cycle and retained family-centered workspace, with the existing change-set viewer as a comparison-bound takeover. The surface reads and displays supplied judgments; it does not author semantic acceptance or select a dataset.

## Code Commentary

`useSurface` owns the mounted cache and local fallback/page selections, delegates navigation and reading to their actual owners, and shows a retained payload only for the exact current question. Initial hold is caller-configured, not a measured response deadline. A last admitted same-task-context frame can keep the shell mounted while the requested subject is pending, failed or refused; `readingStatusOf` labels that subject, never the old subject as its answer. Outcome/details rendering still distinguish failed reads, typed refusal and measured answers.

`subjectSelection` records the focus request, advances tree intent with explicit keepTree, selects the subject, clears intent fallback, sets the requested page and stores the supplied family context. Manual refresh restarts the walked tree and requests scroll-only answer reveal; failed/refused refresh clears that request, and its retry re-establishes it. Other failed-read retry uses the normal cycle refresh without creating another subject selection.

`useReviewMemoryWatch` is now wired here: only a mounted active live/non-recorded scope registers on the existing stream. Notifications engage the current subject before cycle invalidation/refresh and entry revalidation; watch failure remains a failed read. This is external live input, not an additional polling loop or a semantic grade.

`ReviewPanes`, not WorkspaceBody, owns the one comparison-bound leaf-wide tree read. It shares that result with the workspace and change-page context, and the shared lane with workspace/details. Answer-only technical records/page controls do not borrow the frame's subject content. The mounted reviewer becomes hidden/inert beneath an open overlay rather than being replaced.

Opening a change page captures its exact task, comparison generation, inventory, lane and matching delivered worklist. `useHeldPageLane` may enrich lane/worklist only while `sameGeneration` accepts the pair: task and comparison match, and either both knowledge snapshot pairs are known and equal or both are unknown. A moved context while its lane is still loading becomes an explicit failure; already held old comparison facts are not reclassified as the newer comparison. Missing recorded range is a refusal, not a fallback current file list. Closing only drops overlay state and schedules opener focus return; it does not itself issue another review request.

The extracted `ReviewHeader` owns labels, supplied refresh, keyboard help and historical label. The root owns the review keyboard zone, target/current/pending attributes, cache provider and vertical scrollport with native overflow anchoring disabled. `PagePicker` offers the shared current walkable list (knowledge); family roster continuation still uses its published cursor. Page refusal, expected/observed values, bounds, reset and recovery controls retain their dedicated owners. No source explorer or local changed-file catalogue is mounted here; full file/source UI remains delegated.

## Preserved earlier explanation

The quotation is historical rather than the current contract or active evidence; contradictory prior ownership, bounds and layout promises are superseded above.

>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> Compose the Intent Reviewer from one subject catalogue, one comparison read cycle and the family-centered workspace. The surface is read-only and produces no semantic judgment.
>
> It decides three things:
>
> - **which payload the workspace is mounted over**: the answer for the subject on screen or, while that subject is pending, failed or refused, the task context's last admitted answer (`frame`), so a selection never unmounts the workspace, its navigation or its open disclosures (`ICR-R24@v3`);
> - **what every subject selection does**, including whether it keeps the walked family tree or starts it afresh (requirement MIK-R39);
> - **what the reader's refresh does** beside re-reading.
>
> The Intent Reviewer surface composes one subject catalogue, one comparison read cycle and the family-centered workspace, and stays mounted across every selection. It decides which payload the workspace shows, what each subject selection keeps or restarts, what the refresh control re-reads, and when the change-set viewer opens as a full page over the reviewer with a way back.
> ## Code Commentary
>
> ### `useSurface`
>
> `useSurface` wires the owners together:
>
> - `useReviewNavigation` gives the recorded subjects and the selected subject. The selected subject's kind and identifier come from the navigation; the props only name the subject the reviewer opens with.
> - It holds the reader state of this file: `instead` (the failure after which the reader chose the task context), `selection` (the page request), the `useWorkspaceState()` value and one `ReviewReadCache`, created once per mounted surface.
> - `useReviewReadCycle` reads the review for the task context, the subject, the page request and the history view. `hold: navigation.settling` makes the first read wait for the catalogue's first subject, for at most the navigation's bound.
> - The retained payload is shown only when its full target key (`targetKeyOf`) equals the key of the question on screen (`coherent`), and `shown` is `shownPayload(read, coherent)`.
> - `useObservedComparison` reports the shown complete comparison generation (code trees and known snapshots) to navigation. Code-only movement invalidates the catalogue too; enrichment of the same generation from unknown to known snapshots updates identity without an extra local generation bump.
> - `useRefreshReview` gives the hook `refreshReview` and `retryReview` (below); the reading area's problem block and the surface's outcome region share the one `retryReview`.
> - `reading` is computed with `readingStatusOf` only when a `frame` exists and no payload answers the question on screen. The status is keyed to the read cycle's target key and names the requested subject: `kind:id`, labelled from the catalogue entry when there is one, or "all source changes" for the task context. For a failed or refused read it carries the owner's `ReviewProblemBlock`, labelled with that subject, with retry for a failed read and the offer to open the task context for an intent-only refusal (`insteadFor`).
>
> ### Subject selection
>
> `subjectSelection` builds the two selections the surface owns.
>
> `selectSubject(subject, context, options)` is the `onSelect` the workspace and the navigation receive. In this order it:
>
> 1. leaves a focus request in the workspace state: the element that has focus now, and the number of the tree intent that is current before this selection (`after`);
> 2. calls `workspace.beginSelection(options?.keepTree === true)`. A caller passing `keepTree` keeps the walked tree; a subject selection without it starts the walk afresh. Outline rows, reading-area member selections and kept-family roster continuation use the existing in-tree selection path. The removed catalogue shortcuts and all-invariants list are not callers; All changes opens the comparison page without selecting a subject. Marker follow/return retain their existing selection owner;
> 3. gives the subject to the navigation;
> 4. clears `instead`;
> 5. sets the page request to `options?.page`, which is absent for every selection except a kept family's roster continuation, so an ordinary selection also clears the earlier page request;
> 6. stores the chosen family context, or clears it.
>
> `openTaskContext(failure)` is the offer shown after an intent-only refusal. It calls `beginSelection(false)`, so it starts the walked tree afresh, and sets `instead`.
>
> ### Refresh and retry
>
> `useRefreshReview(workspace, read, refresh)` is called in `useSurface` and wraps the read cycle's `refresh`. It returns two handlers.
>
> `refreshReview` is the handler of the refresh control. A refresh:
>
> 1. calls `beginSelection(false)`: the walked tree starts afresh, because a refresh shows the comparison as it reads now;
> 2. leaves a `scrollOnly` focus request, so that the selected row is brought into view once the refreshed answer is shown and focus stays where it is;
> 3. remembers the read that was on screen (`asked`), then re-reads.
>
> `settle(read)` is the one rule for a refresh whose read has no answer. When the read on screen is failed or refused, is not the read remembered at the click, and a `scrollOnly` request is pending, it drops the request and remembers that read as the failed read of a refresh (`failed`). A refresh whose own read fails therefore leaves no request behind, and a later answer for the same subject (a page, a roster continuation) does not move the rail. A failure that was already on screen when the refresh was asked does not drop the request. An effect runs `settle` for every read.
>
> `retryReview` is the handler of the retry control of a failed read, in the surface's own failure block and in the reading area's. It runs `settle` first, because a retry made in the turn that shows the failure comes before that turn's effects. Then:
>
> - when the failure on screen is the remembered failed read of a refresh, the retry is the refresh again: it calls `refreshReview`, so the tree starts afresh and the scroll is asked for again;
> - the retry of any other failed read (a selection's, a page's, a continuation's) only reads again. It makes no selection and leaves no focus request, so a retry after a failed in-tree selection keeps the walked tree.
>
> `retryFor` offers the retry only for a failed read.
>
> ### `ReviewPanes`
>
> `ReviewPanes` renders the workspace over `shown ?? (reading ? frame : null)` and passes `reading` only when nothing answers. It calls `useReviewLane` once for the displayed tree comparison, passes the answer to the workspace and technical details, and captures that lane and inventory when a comparison page opens. A dataset review names no tree comparison, so the hook asks nothing. The mounted reviewer becomes hidden and inert while the overlay is open; technical details receive the answer alone (or an `unanswered` label), and page controls render only for an answer.
>
> ### The root and the header
>
> `ReviewSurface` renders the root (`review-surface`):
>
> - `data-kbzone="review"` makes it the keymap owner's reviewer zone; the family tree binds its `j`/`k` traversal on this element.
> - `data-comparison`, `data-review-target` and `data-review-history` (`live` or the history view) identify what is shown. `data-review-pending` or `data-review-unavailable` carries the requested subject while it has no answer.
> - The root is its own vertical scrollport (`height: 100%`, `minHeight: 0`, `minWidth: 0`, `overflowY: auto`).
> - `useReaderEngagement` reports reader gestures on the root to `navigation.engage`.
> - `ReviewReadCacheContext` provides the surface's cache to the source content rendered below.
>
> `ReviewHeader` renders the back button, the leaf, a disclosure with the task and subject identifiers (`subjectLabel`), the refresh control, and, for the recorded history view, the line "Historical task comparison" (`review-history`). Its row wraps.
>
> `ReviewOutcomeRegion` receives the read, `instead`, the shown payload, the last coherent payload only for a failed read, the retry, the offer of the task context, and `readingInWorkspace`, so a read the workspace states is stated once.
>
> ### The page controls
>
> `PageControls` renders `PagePicker` (the walkable collections of `REVIEW_WALKABLE_COLLECTIONS`, and "whole review"), `PageActions` (a "next page" button only when the payload published a cursor, `continuationOf`; a "first page" button while a requested page is shown), `PageBoundsLine` (the bounds of the carried page, or the sentence that the whole review was read) and the reset line when the page carries one. When the requested page was refused (`refusedPageOf`), `PageRefusalBlock` shows the refusal's code and detail, its expected and observed values when present, its next action, and a button for the first page of the requested collection; the bounds line is then omitted.
>
> ### Conventions
>
> - Exports: `ReviewTarget` and `ReviewSurface`.
> - The record panes live in `ReviewRecordPanes.tsx`, the outcome states in `ReviewOutcome.tsx`, the refresh control in `ReviewRefresh.tsx`, the read cycle in `ReviewReadCycle.ts` and the workspace in `ReviewWorkspace.tsx`. This file composes them.
> - `useSurface` holds the subject/read state and cache; `useReviewChangePage`, called by `ReviewPanes`, holds the change-page state and opener reference.
> - The current file is 915 lines.
>
> ### Invariants And Boundaries
>
> - The surface names a task context, a subject, a page and a history view. It never names a dataset.
> - A failed read may retain only the last coherent answer to the same question.
> - The frame keeps only the shell: nothing of the frame's subject is passed on as the requested subject's reading or records.
> - A selection never unmounts the workspace once a frame exists. Only the first read, which has no frame, is stated at the surface level.
> - Every selection made through `selectSubject` without `keepTree`, the offer of the task context, a refresh and the retry of a failed refresh start the walked tree afresh. The retry of any other failed read does not.
>
> ### Logic
>
> The subject-selection callback carries the chosen family context into the new subject read. Selecting a member requests its invariant through the existing read cycle; it does not render a family payload as that member own assessment.
>
> useSurface gets recorded subjects through useReviewNavigation and passes the chosen identity to useReviewReadCycle. Changing subjects (`selectSubject`) records the element that had focus (`focusSelection = { from }`), clears the prior page request and local family selection while the workspace display preferences persist. The retained payload is shown only when its full target key matches the question on screen. ReviewPanes mounts one workspace; records, pagination, submission contract and complete technical panes remain inspectable in the technical-details disclosure, whose renderers moved to `ReviewRecordPanes.tsx` (`ReviewTechnicalDetails`) in L48. Typed outcomes stay with ReviewOutcome, refresh identity with ReviewRefresh, source bytes with SourceContent, and family/intent/source composition with ReviewWorkspace.
>
> **The mounted shell (L48).** `useSurface` owns one `ReviewReadCache` per mounted surface (`useState(() => new ReviewReadCache())`), passes it to the read cycle and provides it to source content through `ReviewReadCacheContext`. It computes `reading` with `readingStatusOf` only when a `frame` exists and no payload answers the question on screen: the status is keyed to the read cycle's target key, names the requested subject (`kind:id`, labelled from the catalogue entry when there is one) and, for a failed or refused read, carries the owner's `ReviewProblemBlock` labelled with that subject (retry for a transport failure, the source-changes offer for an intent-only refusal). `ReviewPanes` renders the workspace over `shown ?? (reading ? frame : null)`, passes `reading` only when nothing answers, and hands `ReviewTechnicalDetails` the answer alone (or an `unanswered` label), so records are never shown under another subject; the page controls render only for an answer. The root publishes `data-review-pending` or `data-review-unavailable` with the requested subject, and `ReviewOutcomeRegion` receives `readingInWorkspace` so the read is stated once. `useReaderEngagement` on the root reports reader gestures to `navigation.engage` (the late-catalogue rule, see `ReviewNavigation.tsx`).
>
> **One lane read for the displayed tree comparison (MIK-L32, retained by L86).**
> `ReviewPanes` calls `useReviewLane(repo, master, leaf, treeComparisonNumber(payload.limitations))` once and hands
> the answer to `ReviewWorkspace` and `ReviewTechnicalDetails`. Current sidebar destinations and main attribution
> facts use it, and the comparison page captures the same lane with its inventory instead of classifying again.
> There is no lane center or source explorer. A dataset review names no tree comparison, so the hook asks nothing.
>
> **The reviewer's keyboard zone (MIK-L33, MIK-R33 rule 7).** The surface root carries `data-kbzone="review"`, the
> keymap owner's `review` zone (`data/keymap/zones.ts`). The family tree binds its `j`/`k` change traversal
> (`changeTraversal.useChangeTraversal`) on this element, so the chords act only while focus is inside the reviewer and
> the owner's routing keeps them inert in inputs, textareas, contenteditable regions and the terminal zone. This is the
> file's only MIK-L33 change.
>
> Since `260921-ICR-L47`, `useSurface` passes `hold: navigation.settling` to `useReviewReadCycle`, so the
> first review read waits at most `SUBJECT_HOLD_MS` for the opening subject. `useObservedComparison` reports
> the displayed complete generation: code trees and known snapshots, including code-only movement. The
> L47 growth to 931 lines and L48 extraction to 585 lines are historical measurements, not this file
> size; the current file is 915 lines and retains the extracted record-pane owner.
>
> ### Conventions
>
> The component imports its types from `../../data/review` (the public entry that re-exports the
> transport surface), the page helpers it mounts (`REVIEW_WALKABLE_COLLECTIONS`, `carriedPage`,
> `continuationOf`, `intentOnlyRefusal`, `pageBounds`) from that same public entry, `ReviewPagedCollection`
> as a type from it, its read cycle (`ReviewPageRequest`, `targetKeyOf`, `useReviewReadCycle`) from
> `./ReviewReadCycle`, the refresh control and its one derivation from `./ReviewRefresh`, the read phases
> plus the region from `./ReviewOutcome`, and the workspace together with its state hook from
> `./ReviewWorkspace` — which is what makes one module the owner of the outcome states. It declares no
> client of its own and **does not import `DiffPane` or `SourceContent`**: statement diffs remain with
> `KnowledgeStatements`, and source bytes remain with the card Full file renderer (and the retained
> dataset expression renderer), not a `SourceExplorer`. The surface imports `ChangeSetViewer` for the
> comparison overlay. Panda `css` and the local inline layout declarations style the composition. The
> per-record stable keys and `data-*` facts belong to `ReviewRecordPanes.tsx`; they are not declarations
> of this surface. `useSurface` holds `instead`, `selection`, the `useWorkspaceState()` value and the
> read cache, while `useReviewChangePage` owns the overlay state and opener reference. `data-side-state` **no longer
> appears in this file**: it moved with the statement area into
> `KnowledgeStatements.tsx`, where the same attribute still spells a side's declared state.
>
> ### Invariants And Boundaries
>
> No browser path selects a dataset. Failed reads may retain only the last coherent answer to the same question and never invent an empty review. The frame keeps only the shell: nothing of the frame's subject is rendered as the requested subject's reading, records or comparison identity (`ICR-R26` isolation, L48). A selection never unmounts the workspace once a frame exists; only the first read, which has no frame, is stated at the surface level. One-sided statements, subject applicability, evidence currentness and authored assessments retain their existing owners. Source review remains reachable when only intent is unavailable.
>
> ### Todos
>
> None recorded. The assessment-publication control is deliberately not shipped by this increment, and
> the Source pane's expansion is a read: no control on this surface writes, and the byte-form rows stay
> identification-only until this vocabulary can carry a path as bytes.
>
> Paged collections render through a refusal-aware picker with bounds lines and one next or reset action. The panes mount over the coherent payload with the lane read and the comparison beside them, under one technical disclosure. The change-set overlay opens the existing viewer on the review comparison for the lane destinations and All changes, retains its lane and inventory while a held subject answers another comparison, shows the route refusal where no comparison is recorded, and returns with selection, scroll and focus and no new request.
> ## Evidence
>
> - The surface's hook: navigation, reader state, the cache, the read cycle, the coherent payload, the refresh and retry handlers and the reading status. (historical reference 32)
> - A selection leaves its focus request, numbers the tree intent with or without `keepTree`, selects the subject, and sets or clears the page request; the offer of the task context starts the tree afresh. (historical reference 33)
> - A refresh starts the walked tree afresh and asks for a scroll once its answer is shown; the request is dropped when the refresh's own read fails or is refused; the retry of that failed read is the refresh again, and the retry of any other failed read only reads again. (historical reference 34)
> - The unanswered subject's status, keyed and labelled with the requested subject. (historical reference 35)
> - The workspace over the answer or the frame, the records only for an answer, and the one lane read handed to both. (historical reference 36)
> - The root: the reviewer zone, the identity and pending attributes, the scrollport, the engagement observer, the cache provider, and the refresh and retry handlers handed to the header and the outcome region. (historical reference 37)
> - The header: back, leaf, identifiers, refresh and the history line. (historical reference 38)
> - The offer of the task context exists only for an intent-only refusal with no earlier offer taken. (historical reference 39)
> - Retry exists only for a failed read. (historical reference 40)
> - The page controls: picker, actions, bounds, refusal and reset. (historical reference 41)
> - The picker offers the walkable collections. (historical reference 42)
> - A next page is offered only for a published cursor. (historical reference 43)
> - The refusal of a requested page, with a first page of that collection. (historical reference 44)
> - The workspace state the selections write: the focus request and the tree intent. (historical reference 45)
> - The selection options a caller may pass. (historical reference 46)
> - The mounted cases of which selections keep the walked tree and which start it afresh, of the stacked reveal of an in-tree read, and of the scroll after a refresh and after the retry of a failed refresh. (historical reference 47)
> - The mounted cases of the mounted shell, the pending and problem states and the focus order. (historical reference 48)
> - Subject labels and retry/instead routing for pending or refused reads (historical reference 49)
> - Refusal rendering for pages that cannot be opened (historical reference 50)
> - Refused-page extraction for paged collections (historical reference 51)
> - Pane assembly over the coherent payload, lane and comparison (historical reference 52)
> - Held lane read while the change-set page is open (historical reference 53)
> - Open and close behavior of the change-set overlay (historical reference 54)
> - What every subject selection keeps, restarts or opens (historical reference 55)
> - Wiring of navigation, workspace, read cycle, cache and refresh (historical reference 56)
>
> ### Docs References
>
> No domain documentation source is configured for this repository (`system/sources.md` carries no
> `Domain Documentation` entries). The statements below are grounded in repository source only.
>
> No configured domain documentation could be checked.
>
> ### Repo-Internal References
>
> The current ownership and boundaries above are grounded in these source declarations.
>
> | Restored finding | Primary anchor | Tip range |
> | --- | --- | --- |
> | The held first read and the snapshot observation. | `useSurface` | dashboard/src/panels/review/ReviewSurface.tsx:520-540 |
> | `useSurface` owns the behavior described above, including the cache, `selectSubject` and the `reading` status. | `useSurface` | dashboard/src/panels/review/ReviewSurface.tsx:485-564 |
> | The unanswered subject's status, keyed and labelled with the requested subject. | `readingStatusOf` | dashboard/src/panels/review/ReviewSurface.tsx:376-396 |
> | `ReviewPanes` owns the behavior described above: the workspace over the answer or the frame, the records only for an answer, and the one lane read handed to both (MIK-L32). | `ReviewPanes` | dashboard/src/panels/review/ReviewSurface.tsx:303-371 |
> | One lane read per comparison through the real surface; none for a dataset review. | `offers the two lane destinations after the families, with their file and hunk totals` | dashboard/src/panels/review/ReviewSurface.lane.test.tsx:85-99 |
> | `ReviewSurface` owns the behavior described above, including the cache provider, the pending/unavailable root attributes and the engagement observer. | `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:613-679 |
> | `PageControls` owns the behavior described above. | `PageControls` | dashboard/src/panels/review/ReviewSurface.tsx:257-296 |
> | The root is the keymap owner's reviewer zone (MIK-L33). | `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:624-626 |
> | **The pane helper's two load-bearing declarations (moved unchanged to `ReviewRecordPanes.tsx` by L48).** | `pane` | dashboard/src/panels/review/ReviewRecordPanes.tsx:33-41 |
> | **The disclosure track that lets the panes shrink: `minmax(0, 1fr)`, not the implicit `auto`.** | `ReviewTechnicalDetails` | dashboard/src/panels/review/ReviewRecordPanes.tsx:479-487 |
> | The header wraps the task/subject controls while keeping their context and refresh action available. | `ReviewHeader` | dashboard/src/panels/review/ReviewSurface.tsx:398-452 |
> | The reviewer root owns its vertical scrollport while the shell retains its own layout responsibility. | `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:628-632 |
> | The fixture builder and the mount this pin relies on, cited from their own declarations. | `payload` | dashboard/src/panels/review/ReviewSurface.narrow.test.tsx:44-119 |
> | The shell decision this file does **not** change, and which stays routed to the cockpit owner: the comment that states it sits on the declaration itself. | `viewport` | dashboard/src/cockpit/Cockpit.tsx:320-326 |
>
> ### Cross-Repo References
>
> No cross-repository behavior is implemented in this file. The component renders one repository
> namespace's records and carries no identity that ranges beyond it.
>
> No meaningful cross-repo references found.
>
> ## 260921-ICR-L10 The Page Control That Reaches The Rest, And The Refusal It Renders
>
> `260921-ICR-L10` (`ICR-R10@v1`) makes the remainder reachable. The surface used to render a
> remainder with no control that reached the rest of the collection — the packet's own non-conforming
> example — and it now renders the bounds, the scope and one action that advances the walk with the cursor
> **the server published**, plus a first page action when a cursor was refused.
>
> The control is `PageControls` with `PagePicker`, `PageActions` and `PageBoundsLine`, and the refusal is
> `PageRefusalBlock`: the code, the owner's two identities, and a live first page of the collection that
> was asked for. The page is part of the read's target key, so a page change is its own read rather than a
> re-render over the wrong payload. No next action is offered for a body that published no cursor,
> whatever remainder it reported — a button that fetches nothing is the defect this control exists to
> prevent. Keyboard and focus traversal of the control remain `ICR-R24@v1`'s.
>
> **ICR-R31@v1 narrows what the picker offers, not what the wire carries.** `PagePicker` maps
> `REVIEW_WALKABLE_COLLECTIONS`, so it offers only the collections whose first page exists — `knowledge`
> and `records`. The client's `ReviewPagedCollection` still carries all three members, and
> `family_members` is deliberately not offered with no cursor because it is the set of per-family roster
> walks a response composed: naming it would fetch the server's own `comparison_page_unreadable` refusal
> for a question the reader did not mean to ask. A response whose page *is* `family_members` still renders
> through the same bounds and continuation controls as any other.
>
> ## 260921-ICR-L12 The Record Is Part Of The Question, And The Header States It
>
> `260921-ICR-L12` (`ICR-R12@v1`) makes the record a first-class part of this surface's question and
> says out loud which record the panes below are read from:
>
> - **`history` joins `ReviewTarget` and the target key.** The key is now
>   `repo/master/leaf/<history ?? "live">/<question>/<position>`, so switching records reloads rather
>   than reinterpreting a response read for another record — the same rule the page cursor already
>   followed. `intentReview` receives it as its last argument.
> - **`ReviewHeader` is the surface's header, extracted as one component because the record statement is
>   a claim about everything under it.** It renders the mounted provenance line
>   (`data-testid="review-history"`) only for the recorded read: "recorded comparison — this leaf's
>   durable generation, re-read from its own record: the panes below are the comparison it bound, not
>   whatever the repository holds now." The root publishes `data-review-history` (`live` or the record)
>   so a reader or a case can see the record without opening a pane.
> - **`ReviewPanes` mounts the three panes and the two controls above them for one payload.**
> - **Both extractions clear the lint rail without widening it.** `ReviewSurface` had grown past its
>   `max-lines-per-function` rail while gaining the record statement; the two components were extracted
>   with no ignore added and no limit changed, and every prop is threaded rather than re-derived.
>
> The refusal path is untouched: a recorded read that earns a refusal still reaches the reader with its
> code, detail and action, which is what makes a leaf that recorded nothing a stated state rather than a
> missing entry.
>
> ## 260921-ICR-L17 The Read Cycle And The Refresh Control Leave The Surface
>
> `260921-ICR-L17` (`ICR-R17@v1`) makes this surface a renderer of a read cycle it no longer owns, and
> takes **462 lines of read logic and rendering out of it**. Two new modules arrive beside it in the same
> child route:
>
> - [`ReviewReadCycle.ts`](ReviewReadCycle.ts.md) owns the question's identity (`targetKeyOf`), the one
>   read started for it (`startRead` through `askReview`) and the state a reader's refresh needs
>   (`useReviewReadCycle`, returning the read, the retained comparison, the carried binding identity and
>   the `refresh` callback). `ReviewPageRequest` is declared there now and imported back, because the page
>   position participates in the target key the hook computes.
> - [`ReviewRefresh.tsx`](ReviewRefresh.tsx.md) owns the reader's explicit refresh control, the notice
>   that answers it, and the one derivation of a claim (`generationOf`). The header receives both as a
>   `refresh` node and mounts them beside the subject line, because the control belongs to the question the
>   header names and the notice describes the comparison the panes below are showing.
>
> **What is deleted here rather than moved.** The inline `load` callback, the `useEffect` that called it,
> the `targetKeyOf` function, the private `ReviewPageRequest` interface and the `useState`/`useCallback`
> read state are all gone: `useReviewReadCycle` supplies `read`, `retained`, `carried` and `refresh`, and
> what stays in this component is the `instead` state, the `selection` state, the coherence check on the
> retained generation and the wiring of the three regions.
>
> **What a later reader must not undo.** The retained generation is still used only when it was read for
> the question on screen now (`retained.key === targetKey`): the check is belt-and-braces beside the
> reset inside the hook, because a payload under a header it was not read for is exactly the mismatch this
> surface must not be able to produce. `retryFor` now takes the hook's `refresh` rather than a reload
> promise, so a retry is the same one read path as the refresh control and can never become a second way
> of composing a review.

## Evidence

### Docs References

No configured domain documentation; the source owners below support this account.

### Repo-Internal References

- The surface's hook: navigation, reader state, the cache, the read cycle, the coherent payload, the refresh and retry handlers and the reading status. [32]
- A selection leaves its focus request, numbers the tree intent with or without `keepTree`, selects the subject, and sets or clears the page request; the offer of the task context starts the tree afresh. [33]
- A refresh starts the walked tree afresh and asks for a scroll once its answer is shown; the request is dropped when the refresh's own read fails or is refused; the retry of that failed read is the refresh again, and the retry of any other failed read only reads again. [34]
- The unanswered subject's status, keyed and labelled with the requested subject. [35]
- ReviewPanes mounts answer or retained task-context frame, owns the single comparison-bound leafTrees read and shared lane read, and supplies them to the workspace and held change-page context; technical details receive only the actual answer. [36]
- The root: the reviewer zone, the identity and pending attributes, the scrollport, the engagement observer, the cache provider, and the refresh and retry handlers handed to the header and the outcome region. [37]
- The separately extracted header renders back, leaf, task/subject identifiers, supplied refresh, keyboard help and the recorded-history line. [38]
- The offer of the task context exists only for an intent-only refusal with no earlier offer taken. [39]
- Retry exists only for a failed read. [40]
- The page controls: picker, actions, bounds, refusal and reset. [41]
- The picker offers the walkable collections. [42]
- A next page is offered only for a published cursor. [43]
- The refusal of a requested page, with a first page of that collection. [44]
- The workspace state the selections write: the focus request and the tree intent. [45]
- The selection options a caller may pass. [46]
- Stored walk/refresh regression source; its mounted stub assertions are not a fresh execution or browser result. [47]
- Stored navigation/shell regression source, retained as source evidence rather than execution or independent memory acceptance. [48]
- The extracted header labels the selected subject or task-context fallback; requested-subject failure/retry/instead routing remains with readingStatusOf and useSurface. [49]
- Refusal rendering for pages that cannot be opened [50]
- Refused-page extraction for paged collections [51]
- Pane assembly over the coherent payload, lane and comparison [52]
- Held comparison context accepts newly delivered lane and worklist only while `sameGeneration` accepts the pair: repository/task/comparison match and either both knowledge snapshot pairs are known and equal or both are unknown. A moved binding while the lane loads becomes an explicit comparison_context_changed failure; the old page is not silently retargeted. [53]
- Opening captures comparison generation, inventory, lane and only a matching tree worklist; absent recorded comparison becomes explicit refusal. Closing drops overlay state and schedules focus return; it does not itself trigger a new review read. [54]
- What every subject selection keeps, restarts or opens [55]
- Wiring of navigation, workspace, read cycle, cache and refresh [56]
- The mounted live, non-recorded reviewer registers memory notifications on the existing stream. A change engages the selected subject before cycle invalidation/refresh and entry revalidation; watch failure invokes the cycle failure action, and registration is disposed with the surface. [57]

### Cross-Repo References

No separate cross-repository implementation claim.
