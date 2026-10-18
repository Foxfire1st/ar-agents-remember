# dashboard/src/panels/review/ReviewWorkspace.tsx

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Keep one mounted review layout with scope header, compact family/invariant rail, change-set/worklist destinations and a selected-subject reading column. Display state is defined in `workspaceState.ts` and re-exported here; this module neither owns a source explorer nor fetches its own leaf-wide trees.

## Code Commentary

The surface creates display state above read changes. Its owner keeps choice/query, responsive initial diff layout (inline at at-most40rem, otherwise split), full-file/path/opener state, worklist, center ref and numbered focus/tree intent. These choices survive subject reads but not a new mounted review opening. `ReviewWorkspace` provides the comparison-bound intent-marker scope around `WorkspaceBody`.

`WorkspaceBody` receives the single surface-supplied leafTrees, binds catalogue navigation to its payload, and forwards the same read to center, rail and expression/fact consumers. `FamilyRailContext` always mounts the compact tree with that read and its expected comparison; it is not conditional on a loaded semantic family roster. Navigation summary and destinations use the same delivered facts. Worklist, pending/problem center and normal answered context are separate branches; earlier frame content never impersonates the requested subject's reading.

Walked-family selection remains an explicit identity path. The reading mark uses the answer's own context; the rail mark may use a kept family. Known loaded family selections prefetch their exact sorted invariant card set before navigation, while an unloaded outline choice does not invent that context. Kept-family cursor continuation selects the family when the current subject cannot own its cursor. Catalogue, no-family, absent, unreadable and unselected states retain distinct reading-area sentences rather than invented membership.

`useSelectionFocus` is a layout effect, with request/render ordering, catalogue-loading and pending/unavailable checks. Pending compatible kept-tree selection may be revealed locally while its request stays alive. Answered kept-tree selection at every width uses preventScroll then bounded `revealTreeRow`; ordinary other selection uses native focus. Unavailable in-tree stacked selection may reveal its status without consuming the retry's request or stealing moved focus. Refresh scrollOnly is a separate branch. The older claim that all desktop focus remains the original native focus call, or that the stacked predicate gates every reveal, is superseded.

The rail is sticky with its own scroll at wider widths, becomes static/unbounded in the stacked layout, then at-at-most40rem receives a45dvh local scroll cap. Local selected-row reveal measures the panel against review/viewport bounds and controls rather than scrolling the containing page. Marker return retains its own stacked sticky box and shared offset. These are source mechanisms/styles, not a new browser or visual execution result.

`ReviewDestinations` and lane counts are imported owners. All changes is independent of semantic selection; delivered worklist answer counts are distinct from attribution file counts. This file renders no changed-file list, makes no direct fetch and owns no second tree-read hook. The scope header and normal answer's main facts remain distinct from optional technical/provenance disclosures.

## Preserved earlier explanation

The quotation is historical rather than the current contract or active evidence; contradictory prior ownership, bounds and layout promises are superseded above.

>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> Own the family-centered review layout and its transient inspection state: one scope header, one combined rail and the unified intent, source and evidence center.
>
> - The workspace stays mounted across subject selection. While the selected subject has no answer, only its reading area changes, to a status bound to the requested subject (`ICR-R24@v3`).
> - The family tree in the rail is the tree the reader has walked (`walkedTree.ts`, requirement MIK-R39). A selection of a row the tree shows keeps every family it shows; every other selection starts the tree afresh.
> - For a tree comparison the rail offers the two destinations of the unexplained-changes lane after the families (MIK-R32), and the workspace is the scope of the diffs' per-hunk intent markers (MIK-R34).
>
> Own the review workspace layout and its transient display state: the family navigation tree in the rail with the change-set destinations after it, and the intent, worklist and evidence reading area in the center.
> - Changed files open in the change-set viewer the product already has (`ReviewChangeSetNavigation`); the reviewer keeps no file list of its own (MIK-R86). The workspace holds no source explorer and no unexplained-lane components.
> ## Code Commentary
>
> In-tree family/member selections whose family context is already loaded begin bound expression-card prefetch before selected-subject navigation; an unloaded outline family navigates without that prefetch. The mounted workspace and retained inspection state remain independent of the pending reading block; existing selection, refusal, focus and comparison-generation rules are preserved.
>
>
> ### State above the reads
>
> `useWorkspaceState` is called by the surface, above the pane switch, so a page read or a selection never resets it. It holds:
>
> - the reader's explicit family or member choice (`chosen`), the search text, the diff layout (`split` at first), the full-file disclosure (off at first, so changed regions are the initial display) and the opened path;
> - the element that opened an expression: `openFromCenter` remembers it and `closePath(null)` returns focus to it; `setOpenPath` sets the path without moving focus (an intent marker's follow and return use it);
> - the worklist-open flag (`worklist`): choosing a subject leaves the worklist view; showing the worklist reveals the reading area;
> - the reading-area column's ref (`center`);
> - `focusSelection`, a ref to the pending `FocusRequest` (below);
> - `treeIntent` and `beginSelection(keepTree)`: every selection gets the next number and says whether it keeps the walked tree.
>
> `useWorkspaceState` is called by the surface, above the pane switch, so a page read or a selection never resets it. It holds the reader's explicit family or member choice (`chosen`, cleared out of the worklist view on choose), the search text, the diff layout (`split` at first), the full-file flag, the opened path (with `openFromCenter` remembering the opener for focus return, and `setOpenPath` moving none for a marker follow and return), the lane worklist flag, the center column ref, the pending `focusSelection` request, and `treeIntent` with `beginSelection(keepTree)`.
> ### The layout
>
> `ReviewWorkspace` is a thin wrapper. It builds the intent markers' scope with `useIntentMarkerScope` from the task context, the payload's tree comparison number (`treeComparisonNumber(payload.limitations)`), the change inventory (`markerInventory`) and the workspace's own moves (`workspaceMarkerMoves(state, navigation)`), and provides it around `WorkspaceBody`. A dataset review names no tree comparison.
>
> `WorkspaceBody` renders, in one grid: `ReviewScopeHeader` (with a `status` of `pending` or `unavailable` while the subject is unanswered), the "Jump to selected review" button of the stacked layout, `MarkerReturn`, `WorkspaceRail` and `WorkspaceCenter`. The root publishes `data-diff-layout`, `data-full-file` and, while a followed marker's way back is shown, `data-marker-return="open"` (`useMarkerReturnState`).
>
> `WorkspaceRail` holds one compact family/invariant outline tree and change-set/worklist destinations.
> There is no `SourceExplorer`, `RailLaneDestinations` or local changed-file list; the held server lane
> feeds destination counts/filters without classifying files again.
>
> - `WorkspaceRail` draws the walked tree (`walkedTreeOf`: walked families, kept families with their read-for labels, the walk notice) inside `ReviewNavigation` with the lane counts (`laneCounts`) and the destinations (`ReviewDestinations`: unexplained-changes, unknown-attribution and all-changes buttons opening the change-set viewer, plus the worklist button with the leaf trees' count).
> - `WorkspaceCenter` swaps one column between the unanswered subject's `ReadingStatusCenter`, the `LeafWorklistView` (with change-set openers for memory and path items), and the answered reading: context notes, `FamilyReviewCenter`, main facts and the roster page note.
> ### The unanswered subject
>
> `ReviewWorkspace` takes an optional `reading: ReadingStatus | null`. The surface sets it only when the subject on screen has no answer; `payload` is then the last admitted answer of this task context, used for the shell only. `ReadingStatus` carries the read cycle's key for the requested question, the requested subject, its label and, for a failed or refused read, the owner's problem block (`null` while pending).
>
> `WorkspaceCenter` is one reading-area column for the workspace's lifetime. Only its content swaps:
> requested-subject status, the own worklist view, or answered-subject context notes, `FamilyReviewCenter`,
> `ReviewMainFacts` and roster continuation. Earlier payload content never masquerades as the pending subject.
>
> ### The walked tree
>
> `useWalkedSelection` connects the workspace to `walkedTree.ts`:
>
> - It calls `useWalkedTree(payload, scope, state.treeIntent)`, where `scope` is `repo/master/leaf/` plus `recorded` or `live`. The walk's families (`walked`) are what the rail's tree shows.
> - It computes two selection marks with `selectedContext`. `chosen` is the mark of the reading area and may only sit on a family of the selected subject's own answer. `treeChosen` is the mark of the rail's tree and may sit on any family the walk holds, so a row of a kept family can be the marked row. When the reader's choice names no such family, both fall back to `initialContext` over the answer's own families.
> - `choose` is `chooseSubject` over the walked families. It finds the chosen family among them, a kept family included. A family row selects `{ kind: 'family', id }`; a member row selects the member's invariant when the roster gives its `invariant_id`. Both go through `navigation.onSelect` with `{ keepTree: true }`, and the choice is stored with `state.setChosen`. A choice whose family the walk does not hold only moves the stored choice. The reading area's "open member" control calls the same `choose`.
> - `rosterNext` is the handler of a family's roster continuation control. For a family of the selected subject's own context, or without navigation, it asks for the page (`onPageSelect`). For a kept family it selects that family with `{ keepTree: true, page }`, because the server continues a cursor only for a subject whose context holds the family.
>
> `walkedTreeOf` turns the walk into what `FamilyTree` draws (`WalkedTree`): the walked entries; the kept families with the label of the subject each was last read for; the walk's notice; and `subjectState`, the sentence "For the selected subject: …" when the selected subject's own context is not composed. `readForLabel` builds the label as the subject's kind followed by the catalogue's label for it, or by `subjectTitle` of the answer that carried the family when the catalogue has no such row; it is "an earlier subject" when the answer named no subject.
>
> `WorkspaceRail` passes the catalogue outline, current subject/selection and walked entries to compact
> navigation; those identities and badges are independent of loaded semantic roster pages.
>
> `FamilyRailContext` supplies `FamilyTree` with outline/catalogue admission, loading/problem state,
> context/walk, subject selection and traversal eligibility. Unknown marker membership has its explicit
> reading-area state; it does not fabricate membership or replace the complete outline with a partial roster.
>
> ### Focus after a selection
>
> A selection leaves a `FocusRequest` in `focusSelection`: `from` (the element that had focus), `after` (the tree intent's number when the request was made), and optionally `scrollOnly` and `answered`.
>
> `useSelectionFocus(payload, state, reading)` runs an effect on every change of the payload, of the reading status and of the tree intent. The reading status tells a read still on its way (`reading` set, no problem) from one that ended unavailable (failed or refused):
>
> 1. It notes whether the payload is new to this effect.
> 2. It leaves the request alone unless the render's tree intent is later than `request.after`. An effect of a render made before the selection can run after the reader's next click; such an effect must not take the request.
> 3. A new payload seen by such a later render marks the request `answered`.
> 4. While the subject is pending, or while a `scrollOnly` request is not yet `answered`, the request stays. A read that ends unavailable calls `revealUnavailableRead` instead of waiting: it scrolls the reading area into view when the selection was in-tree, the layout is stacked and the reader has not moved focus, moves no focus, and leaves the request alive for a retry.
> 5. Otherwise it clears the request and calls `landFocus`.
>
> `landFocus` handles the two kinds of request. A `scrollOnly` request (a refresh) brings the selected node into view with `scrollIntoView({ block: 'nearest' })` and moves no focus. Any other request first tests `selectionFocusAvailable` — focus is still on `from`, has fallen to `body`, or no element is active (`null`) — and then calls `focusSelectedRead`. On the stacked layout an in-tree selection (`stackedTreeRead`: the tree intent keeps the tree, and the viewport matches `(max-width: 60rem)`) focuses the selected node with `preventScroll: true` and scrolls the reading-area column to its start; every other selection and every wider layout keeps the original `node.focus()`. The shared `revealCenter` of a lane or file destination is unchanged.
>
> Because the effect also runs when the tree intent changes, a selection that needs no new answer (the subject already selected, chosen again) lands focus when it is made.
>
> ### Held lane and the leaf's worklist read
>
> - `WorkspaceBody` reads the leaf-wide `/api/review/trees` view through `useReviewTrees`, pinned to the payload's comparison number and enabled only for a tree comparison. It passes the same `leafTrees` result to both `WorkspaceRail` and `WorkspaceCenter`; the center passes it to `FamilyReviewCenter`.
> - Lane destinations open the comparison change-set viewer with held classification filters. The own
>   worklist view receives leafTrees and comparison binding separately; no `UnexplainedLaneCenter` or
>   lane-focused file view remains.
>
> ### The stacked layout
>
> At or below 60rem the grid is one column. `markerReturn` is then sticky at `top: 0.5rem` with `z-index: 2` and a fixed height of 2rem, and while the way back is open the workspace sets `--review-sticky-top: 2.75rem`, below which the family tree's triage bar sticks. Side by side, the rail is sticky and scrolls on its own.
>
> ### Conventions
>
> - Styles are module-level constants built with `css` from `../../../styled-system/css`: `workspace`, `shell`, `muted`, `title`, `jump`, `markerReturn` and `rail`.
> - Test ids rendered here: `review-workspace`, `review-jump-to-selection`, `review-center-column`, `review-reading-pending`, `review-reading-problem`, `review-roster-walk`, and, for an uncomposed context, `review-family-tree`, `review-family-context` and `review-family-limitation`.
> - The file makes no `fetch` call, and its one `useEffect` is in `useSelectionFocus`. It calls `useReviewTrees` for the leaf-wide tree view; the lane read arrives from the surface as `laneRead`.
>
>
> ### Invariants And Boundaries
>
> - Semantic selection never filters the complete comparison change-set population; All changes remains usable independently of lane availability.
> - Lane destinations use held server classification and never substitute another comparison's inventory or facts.
> - Confirmed no-family, unselected, absent and unreadable context are different states with different sentences (`emptyFamilyDescription`), and an unknown membership opened from an intent marker is its own state.
> - While `reading` is set, nothing of the earlier payload's subject is rendered as the requested subject's reading: the center shows only the requested subject's status, and the marks are the reader's explicit choice only.
> - The reading area shows nothing of a kept family: its mark and its content come from the selected subject's own answer.
> - Display preferences change neither knowledge nor comparison identity.
>
> ## Evidence
>
>
> - The walk itself. (historical reference 40)
> - The workspace's moves for an intent marker: select the target through the navigation, and restore the reading position. (historical reference 41)
> - The scope header's record label lives in the header's module. (historical reference 42)
> - The triage bar sticks below the way back at the workspace's offset. (historical reference 43)
>
> - The workspace state: the choice, search, layout, full-file disclosure, opened path with its opener, the lane, the focus request and the numbered tree intent. (historical reference 18)
> - The focus request a selection leaves: the element that had focus, the tree intent it was made after, and the scroll-only and answered flags. (historical reference 19)
> - The wrapper provides the intent markers' scope around the body. (historical reference 20)
> - The body: scope header, jump button, way back, rail and center in one grid, with the layout and marker-return attributes on the root. (historical reference 21)
> - The unanswered subject's status and its two renderings. (historical reference 22)
>
> - The reading-area column is one node whose content alone is swapped. WorkspaceBody reads the leaf-wide tree view only for a tree comparison and supplies it to WorkspaceCenter. Anchor: `WorkspaceCenter`; `WorkspaceBody` (historical reference 23)
>
> - The walk, the two selection marks, the row selection and the roster continuation of a kept family. (historical reference 24)
> - A mark may sit only on a family that is shown to it; otherwise the answer's own first context is marked. (historical reference 25)
> - A row of the walked tree, a kept family's included, is selected through the navigation with `keepTree`. (historical reference 26)
> - What the tree draws: the walked entries, the kept families with the subject each was last read for, the notice and the selected subject's state. (historical reference 27)
> - The label of the subject a kept family was last read for. (historical reference 28)
> - The rail renders outline navigation and change-set/worklist destinations, without a source explorer or changed-file list.  Anchor: `WorkspaceRail` (historical reference 29)
> - The tree is drawn when the subject's context is composed or the walk holds a family; an unknown-membership target has its own state. (historical reference 30)
> - Only a render made after the request answers it; a pending subject and an unanswered scroll-only request keep it. (historical reference 31)
> - A scroll-only request brings the node into view; any other moves focus only if the reader has not moved it. (historical reference 32)
> - What a selection focuses: a followed marker's unknown-membership state, else the tree's current node. (historical reference 33)
> - The workspace carries the state of the way back. (historical reference 37)
> - The way back's sticky box in the stacked layout. (historical reference 38)
> - The sentences of the uncomposed context states. (historical reference 39)
> - A failed or refused in-tree selection on the stacked layout scrolls its status into view; it moves no focus and leaves the focus request for a retry. (historical reference 44)
>
> - The moved-focus test guards non-scrollOnly answered selections and unavailable reveals, so those paths neither take focus nor scroll after the reader moves on. A scrollOnly refresh remains a separate branch. (historical reference 45)
>
> - The in-tree and stacked test that gates every reveal. (historical reference 46)
> - The answered in-tree selection on the stacked layout focuses the selected row without scrolling to it and reveals the reading area; every other selection keeps its original focus call. (historical reference 47)
> - Display state owned above the pane switch (historical reference 48)
> - Rail, center and jump control composition (historical reference 50)
> - Lane counts feeding the navigation summary (historical reference 52)
> - Change-set and worklist destinations, no file list (historical reference 53)
> - Focus landing on the selection's answer (historical reference 55)

## Evidence

### Docs References

No configured domain documentation; the source owners below support this account.

### Repo-Internal References

- The workspace state: the choice, search, layout, full-file disclosure, opened path with its opener, the lane, the focus request and the numbered tree intent. [18]
- The focus request a selection leaves: the element that had focus, the tree intent it was made after, and the scroll-only and answered flags. [19]
- The wrapper provides the intent markers' scope around the body. [20]
- The body: scope header, jump button, way back, rail and center in one grid, with the layout and marker-return attributes on the root. [21]
- The unanswered subject's status and its two renderings. [22]
- The reading-area column swaps only its content. The surface owns the single comparison-bound leafTrees read; WorkspaceBody receives it and forwards that same answer to center and rail. [23]
- The walk, the two selection marks, the row selection and the roster continuation of a kept family. [24]
- A mark may sit only on a family that is shown to it; otherwise the answer's own first context is marked. [25]
- A row of the walked tree, a kept family's included, is selected through the navigation with `keepTree`. [26]
- What the tree draws: the walked entries, the kept families with the subject each was last read for, the notice and the selected subject's state. [27]
- The label of the subject a kept family was last read for. [28]
- The rail renders outline navigation and change-set/worklist destinations, without a source explorer or changed-file list.  Anchor: `WorkspaceRail` [29]
- FamilyRailContext always mounts compact FamilyTree with catalogue/outline admission, walked context, supplied leafTrees and expected comparison; unknown marker membership is stated separately in the reading area. [30]
- Only a render made after the request answers it; a pending subject and an unanswered scroll-only request keep it. [31]
- A scroll-only request brings the node into view; any other moves focus only if the reader has not moved it. [32]
- What a selection focuses: a followed marker's unknown-membership state, else the tree's current node. [33]
- The workspace carries the state of the way back. [37]
- The way back's sticky box in the stacked layout. [38]
- The sentences of the uncomposed context states. [39]
- The walk itself. [40]
- The workspace's moves for an intent marker: select the target through the navigation, and restore the reading position. [41]
- The scope header's record label lives in the header's module. [42]
- The shared triageBar style declares sticky positioning at the workspace offset, with a zero fallback. [43]
- A failed or refused in-tree selection on the stacked layout scrolls its status into view; it moves no focus and leaves the focus request for a retry. [44]
- The moved-focus availability predicate gates non-scrollOnly focus landing and unavailable reveals. A scrollOnly refresh has its own explicit branch. [45]
- The stacked/in-tree predicate gates unavailable-status reveal only, not every pending or answered kept-tree reveal. [46]
- An answered kept-tree selection at any width focuses with preventScroll and delegates bounded local-panel reveal. Other selections retain native focus behavior. [47]
- Display state owned above the pane switch [48]
- Rail, center and jump control composition [50]
- Lane counts feeding the navigation summary [52]
- Change-set and worklist destinations, no file list [53]
- The layout effect respects render/request ordering and catalogue loading, retains pending requests, reveals compatible pending kept-tree selection locally, and lands answered focus only through the appropriate branch. [55]
- WorkspaceRail and FamilyRailContext forward the same surface-supplied leafTrees and expected comparison into code summary, destinations and compact tree. Narrow rails become bounded local scrollports; no second leaf-wide fetch or semantic classification is introduced. [56]

### Cross-Repo References

No separate cross-repository implementation claim.
