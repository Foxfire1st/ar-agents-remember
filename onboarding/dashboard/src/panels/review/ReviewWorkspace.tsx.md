# dashboard/src/panels/review/ReviewWorkspace.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Own the family-centered review layout and its transient inspection state: one scope header, one combined rail and the unified intent, source and evidence center.

- The workspace stays mounted across subject selection. While the selected subject has no answer, only its reading area changes, to a status bound to the requested subject (`ICR-R24@v3`).
- The family tree in the rail is the tree the reader has walked (`walkedTree.ts`, requirement MIK-R39). A selection of a row the tree shows keeps every family it shows; every other selection starts the tree afresh.
- For a tree comparison the rail offers the two destinations of the unexplained-changes lane after the families (MIK-R32), and the workspace is the scope of the diffs' per-hunk intent markers (MIK-R34).

## Code Commentary

### State above the reads

`useWorkspaceState` is called by the surface, above the pane switch, so a page read or a selection never resets it. It holds:

- the reader's explicit family or member choice (`chosen`), the search text, the diff layout (`split` at first), the full-file disclosure (off at first, so changed regions are the initial display) and the opened path;
- the element that opened an expression: `openFromCenter` remembers it and `closePath(null)` returns focus to it; `setOpenPath` sets the path without moving focus (an intent marker's follow and return use it);
- the lane selection on screen (`lane`): choosing a family clears it, and choosing a family or a lane destination reveals the center (`revealCenter` scrolls the surface to its top);
- the reading-area column's ref (`center`);
- `focusSelection`, a ref to the pending `FocusRequest` (below);
- `treeIntent` and `beginSelection(keepTree)`: every selection gets the next number and says whether it keeps the walked tree.

### The layout

`ReviewWorkspace` is a thin wrapper. It builds the intent markers' scope with `useIntentMarkerScope` from the task context, the payload's tree comparison number (`treeComparisonNumber(payload.limitations)`), the change inventory (`markerInventory`) and the workspace's own moves (`workspaceMarkerMoves(state, navigation)`), and provides it around `WorkspaceBody`. A dataset review names no tree comparison.

`WorkspaceBody` renders, in one grid: `ReviewScopeHeader` (with a `status` of `pending` or `unavailable` while the subject is unanswered), the "Jump to selected review" button of the stacked layout, `MarkerReturn`, `WorkspaceRail` and `WorkspaceCenter`. The root publishes `data-diff-layout`, `data-full-file` and, while a followed marker's way back is shown, `data-marker-return="open"` (`useMarkerReturnState`).

`WorkspaceRail` holds the "Families & invariants" panel (the catalogue navigation with the family tree inside it, or the tree alone when there is no navigation, then `RailLaneDestinations`) and the `SourceExplorer`. `sourceAttribution` picks the explorer's labels: on a tree comparison (a `laneRead` is present) every changed path takes its label from the lane's classification through `explorerAttribution`; a dataset review uses the payload's attributed and unattributed path lists, and everything else is "Attribution unknown".

### The unanswered subject

`ReviewWorkspace` takes an optional `reading: ReadingStatus | null`. The surface sets it only when the subject on screen has no answer; `payload` is then the last admitted answer of this task context, used for the shell only. `ReadingStatus` carries the read cycle's key for the requested question, the requested subject, its label and, for a failed or refused read, the owner's problem block (`null` while pending).

`WorkspaceCenter` is the reading-area column: one DOM node (`review-center-column`) for the life of the workspace. It swaps only its content: `ReadingStatusCenter` (`review-reading-pending` or `review-reading-problem`), else the lane's center while a lane destination is chosen and a lane read exists, else the answered subject's `FamilyReviewCenter` and `RosterPageNote`. While unanswered, the tree marks only the reader's explicit choice; no mark is derived from the earlier payload.

### The walked tree

`useWalkedSelection` connects the workspace to `walkedTree.ts`:

- It calls `useWalkedTree(payload, scope, state.treeIntent)`, where `scope` is `repo/master/leaf/` plus `recorded` or `live`. The walk's families (`walked`) are what the rail's tree shows.
- It computes two selection marks with `selectedContext`. `chosen` is the mark of the reading area and may only sit on a family of the selected subject's own answer. `treeChosen` is the mark of the rail's tree and may sit on any family the walk holds, so a row of a kept family can be the marked row. When the reader's choice names no such family, both fall back to `initialContext` over the answer's own families.
- `choose` is `chooseSubject` over the walked families. It finds the chosen family among them, a kept family included. A family row selects `{ kind: 'family', id }`; a member row selects the member's invariant when the roster gives its `invariant_id`. Both go through `navigation.onSelect` with `{ keepTree: true }`, and the choice is stored with `state.setChosen`. A choice whose family the walk does not hold only moves the stored choice. The reading area's "open member" control calls the same `choose`.
- `rosterNext` is the handler of a family's roster continuation control. For a family of the selected subject's own context, or without navigation, it asks for the page (`onPageSelect`). For a kept family it selects that family with `{ keepTree: true, page }`, because the server continues a cursor only for a subject whose context holds the family.

`walkedTreeOf` turns the walk into what `FamilyTree` draws (`WalkedTree`): the walked entries; the kept families with the label of the subject each was last read for; the walk's notice; and `subjectState`, the sentence "For the selected subject: …" when the selected subject's own context is not composed. `readForLabel` builds the label as the subject's kind followed by the catalogue's label for it, or by `subjectTitle` of the answer that carried the family when the catalogue has no such row; it is "an earlier subject" when the answer named no subject.

`WorkspaceRail` passes the navigation the identifiers of every family the tree shows (`loadedFamilyIds`) and `listLoaded`, which is true while the tree holds a kept family. While a lane destination is on screen it passes the tree no selection, so no family node is marked current.

`FamilyRailContext` draws `FamilyTree` when the selected subject's context is composed (`recorded` or `partial`) or the walk holds a family; otherwise `FamilyNotComposed`. It gives the tree the selected subject's own context (`NO_FAMILY_CONTEXT` when the answer has none), the walked tree, and `tree`, which is true for a tree comparison. One case comes first: for an invariant that an intent marker opened on an unknown membership the tree has no row for (`useInvariantTargetState`), it shows `InvariantTargetState` alone when the subject's context is not composed, and above the tree when it is composed.

### Focus after a selection

A selection leaves a `FocusRequest` in `focusSelection`: `from` (the element that had focus), `after` (the tree intent's number when the request was made), and optionally `scrollOnly` and `answered`.

`useSelectionFocus(payload, state, reading)` runs an effect on every change of the payload, of the reading status and of the tree intent. The reading status tells a read still on its way (`reading` set, no problem) from one that ended unavailable (failed or refused):

1. It notes whether the payload is new to this effect.
2. It leaves the request alone unless the render's tree intent is later than `request.after`. An effect of a render made before the selection can run after the reader's next click; such an effect must not take the request.
3. A new payload seen by such a later render marks the request `answered`.
4. While the subject is pending, or while a `scrollOnly` request is not yet `answered`, the request stays. A read that ends unavailable calls `revealUnavailableRead` instead of waiting: it scrolls the reading area into view when the selection was in-tree, the layout is stacked and the reader has not moved focus, moves no focus, and leaves the request alive for a retry.
5. Otherwise it clears the request and calls `landFocus`.

`landFocus` handles the two kinds of request. A `scrollOnly` request (a refresh) brings the selected node into view with `scrollIntoView({ block: 'nearest' })` and moves no focus. Any other request first tests `selectionFocusAvailable` — focus is still on `from`, has fallen to `body`, or no element is active (`null`) — and then calls `focusSelectedRead`. On the stacked layout an in-tree selection (`stackedTreeRead`: the tree intent keeps the tree, and the viewport matches `(max-width: 60rem)`) focuses the selected node with `preventScroll: true` and scrolls the reading-area column to its start; every other selection and every wider layout keeps the original `node.focus()`. The shared `revealCenter` of a lane or file destination is unchanged.

Because the effect also runs when the tree intent changes, a selection that needs no new answer (the subject already selected, chosen again) lands focus when it is made.

### The lane and the leaf's tree view

- `WorkspaceCenter` reads the leaf-wide `/api/review/trees` view through `useReviewTrees`, pinned to the payload's comparison number, and only for a tree comparison (the hook's `enabled` flag is false otherwise). The result goes to `FamilyReviewCenter` as `leafTrees`.
- While a lane destination is chosen, `UnexplainedLaneCenter` receives the lane read, the task with the comparison number, the payload's inventory, the layout and `gateRead(leafTrees, comparison)`: the gate's items come only from a leaf-wide read that answered for the same comparison (`reading` until it answers, `none` with the reason otherwise).

### The stacked layout

At or below 60rem the grid is one column. `markerReturn` is then sticky at `top: 0.5rem` with `z-index: 2` and a fixed height of 2rem, and while the way back is open the workspace sets `--review-sticky-top: 2.75rem`, below which the family tree's triage bar sticks. Side by side, the rail is sticky and scrolls on its own.

### Conventions

- Styles are module-level constants built with `css` from `../../../styled-system/css`: `workspace`, `shell`, `muted`, `title`, `jump`, `markerReturn` and `rail`.
- Test ids rendered here: `review-workspace`, `review-jump-to-selection`, `review-center-column`, `review-reading-pending`, `review-reading-problem`, `review-roster-walk`, and, for an uncomposed context, `review-family-tree`, `review-family-context` and `review-family-limitation`.
- The file makes no `fetch` call, and its one `useEffect` is in `useSelectionFocus`. It calls `useReviewTrees` for the leaf-wide tree view; the lane read arrives from the surface as `laneRead`.
- The file is 923 lines.

### Invariants And Boundaries

- Semantic selection never filters the changed-file population: the source explorer always receives the whole inventory.
- On a tree comparison the explorer's labels are the lane's buckets; a dataset review keeps the payload's lists.
- Confirmed no-family, unselected, absent and unreadable context are different states with different sentences (`emptyFamilyDescription`), and an unknown membership opened from an intent marker is its own state.
- While `reading` is set, nothing of the earlier payload's subject is rendered as the requested subject's reading: the center shows only the requested subject's status, and the marks are the reader's explicit choice only.
- The reading area shows nothing of a kept family: its mark and its content come from the selected subject's own answer.
- Display preferences change neither knowledge nor comparison identity.

## Evidence

- The workspace state: the choice, search, layout, full-file disclosure, opened path with its opener, the lane, the focus request and the numbered tree intent. [18]
- The focus request a selection leaves: the element that had focus, the tree intent it was made after, and the scroll-only and answered flags. [19]
- The wrapper provides the intent markers' scope around the body. [20]
- The body: scope header, jump button, way back, rail and center in one grid, with the layout and marker-return attributes on the root. [21]
- The unanswered subject's status and its two renderings. [22]
- The reading-area column is one node whose content alone is swapped; it reads the leaf-wide tree view only for a tree comparison. [23]
- The walk, the two selection marks, the row selection and the roster continuation of a kept family. [24]
- A mark may sit only on a family that is shown to it; otherwise the answer's own first context is marked. [25]
- A row of the walked tree, a kept family's included, is selected through the navigation with `keepTree`. [26]
- What the tree draws: the walked entries, the kept families with the subject each was last read for, the notice and the selected subject's state. [27]
- The label of the subject a kept family was last read for. [28]
- The rail: the navigation with the tree inside it, the families the tree shows, the kept flag, the lane destinations and the source explorer. [29]
- The tree is drawn when the subject's context is composed or the walk holds a family; an unknown-membership target has its own state. [30]
- Only a render made after the request answers it; a pending subject and an unanswered scroll-only request keep it. [31]
- A scroll-only request brings the node into view; any other moves focus only if the reader has not moved it. [32]
- A failed or refused in-tree selection on the stacked layout scrolls its status into view; it moves no focus and leaves the focus request for a retry. [44]
- The one test for a reader who moved focus, shared by the answered and the unavailable paths, so neither takes focus nor scrolls after the reader moved on. [45]
- The in-tree and stacked test that gates every reveal. [46]
- The answered in-tree selection on the stacked layout focuses the selected row without scrolling to it and reveals the reading area; every other selection keeps its original focus call. [47]
- What a selection focuses: a followed marker's unknown-membership state, else the tree's current node. [33]
- The explorer's labels: a tree comparison's from the lane, a dataset review's from the payload's lists. [34]
- The gate's items for the lane come only from the same comparison's leaf-wide read. [35]
- The lane's rail nodes, for a tree comparison only. [36]
- The workspace carries the state of the way back. [37]
- The way back's sticky box in the stacked layout. [38]
- The sentences of the uncomposed context states. [39]
- The walk itself. [40]
- The workspace's moves for an intent marker: select the target through the navigation, and restore the reading position. [41]
- The scope header's record label lives in the header's module. [42]
- The triage bar sticks below the way back at the workspace's offset. [43]
