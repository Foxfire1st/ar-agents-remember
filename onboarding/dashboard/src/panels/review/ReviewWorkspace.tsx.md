# dashboard/src/panels/review/ReviewWorkspace.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Own the family-centered review layout and its transient inspection state: one scope header, one combined rail and the unified intent/source/evidence center. Since MIK-L34 it is also the scope of the diffs' **per-hunk intent markers** for a tree comparison: which comparison they describe, each changed file's classification, and the one followed marker `Back to <file>` returns to. Since `260921-ICR-L48` (`ICR-R24@v3`) the workspace also **stays mounted across subject selection**: while the selected subject has no answer, only its reading area changes, to a status bound to the requested subject.

## Code Commentary

### Logic

Member navigation calls the existing subject reader using the member invariant identity while retaining its family/roster context. The narrow jump focuses the center without the browser default scroll, then scrolls to its start so the selected heading and guarantee remain visible. Layout, full-file disclosure and open path are unchanged by the jump.

useWorkspaceState holds selected family/member, search, diff layout, full-file disclosure, expanded path and focus references above paged reads. Changed regions are the initial display. WorkspaceRail combines recorded catalogue navigation, the loaded guarantee/member subtree and the complete source inventory. sourceAttribution picks the explorer's labels by the kind of review: on a tree comparison (a `laneRead` is present, since MIK-L32) every changed path takes its label from the lane's classification through `laneFocus.explorerAttribution` (`attributed` → Mapped, `unexplained` → Unmapped, `attribution_unknown` → Attribution unknown; Attribution pending while the lane is read, and Attribution unknown when it could not be read; ruling 2026-09-30T12:19:20 Q1), so the explorer and the lane never disagree; a dataset review uses only the backend mapped and unmapped partitions, and everything else is unknown. The scope header (and its `recordLabelOf`, which distinguishes reconstructed recorded endpoints from frozen historical and live comparisons) moved to `ReviewScopeHeader.tsx` in L48; the workspace mounts it with a `status` derived from `reading`. The center reuses FamilyReviewCenter and ReviewExpressions; desktop rail scrolling is independent.

**The unanswered subject (L48).** `ReviewWorkspace` takes an optional `reading: ReadingStatus | null`. The surface sets it only when the subject on screen has no answer and the task context has a `frame`; `payload` is then that frame, used for the shell only. `ReadingStatus` carries the read cycle's key for the requested question, the requested subject (`kind:id`), its label and, for a failed or refused read, the owner's problem block (`problem`; `null` while pending). `WorkspaceCenter` is the reading-area column — one DOM node (`review-center-column`) for the life of the workspace — and swaps only its content: `ReadingStatusCenter` renders `review-reading-pending` (`aria-busy`, `role="status"`, "Reading <label>…") or `review-reading-problem` ("<label> could not be read" plus the owner block, with `data-problem-key`/`data-problem-subject`), else the answered subject's `FamilyReviewCenter` and roster note. While unanswered, the tree marks only the reader's explicit choice (`state.chosen`) — deriving one from the frame would mark the previous subject's family as the requested subject's context.

**The leaf's tree view, read once per comparison (MIK-L31).** `WorkspaceCenter` receives the task context
(`repo`, `master`, `leaf`, `history`) and, only for a tree comparison, reads the leaf-wide `/api/review/trees` view
through `useReviewTrees`: the comparison number is `treeComparisonNumber(payload.limitations)` (the payload's own
`review:trees:<n>` token), passed as `{ comparison }` so the read is pinned to the comparison the review on screen
was composed over (review F11), and the hook's `enabled` flag is false when the payload declares no such token. A
dataset review therefore makes no tree read at all. The result goes to `FamilyReviewCenter` as `leafTrees`, which
renders the knowledge panel and takes the cards' planning marks from it only when its comparison number matches.

**The unexplained-changes lane (MIK-L32, MIK-R32 rule 10).** `ReviewWorkspace` takes the surface's one lane read as
`laneRead` (`null` for a dataset review; its props moved into the `ReviewWorkspaceProps` interface to keep the function
under the 80-line lint rule). `WorkspaceState` gains `lane` (the `LaneSelection` on screen: a destination and the file
it opened) and `setLane`; choosing a family clears the lane, and choosing a destination reveals the centre the same
way a family selection does. `WorkspaceRail` mounts `RailLaneDestinations` (the `Unexplained changes` and `Unknown
attribution` nodes, `LaneDestinations`) after the families in the same tree panel, and while a lane destination is on
screen no family node is marked current (`treeChosen`). `WorkspaceCenter` swaps the reading area for
`UnexplainedLaneCenter` while a destination is chosen and a lane read exists, handing it the task with the comparison
number, the payload's inventory, the layout and `gateRead(leafTrees, comparison)`: the gate's items for an opened file
come only from the leaf-wide read of the same comparison (`reading` until it answers, `none` with why otherwise).

**The rail's family navigator is told when it reads a tree comparison (MIK-L35; review R1 F2).** `FamilyRailContext`
mounts `FamilyTree` with `tree={treeComparisonNumber(payload.limitations) !== undefined}`, so on a tree comparison
the navigator's joint-guarantee and member labels compare text bytes and never call one revision "unchanged" when
its two texts differ; a dataset review passes `false` and keeps the landed labels. This is the only change here; the
review centre sets its own scope from the payload.

**Focus after a selection (L48-R1-F2).** `focusSelection` holds `{ from }`, the element that had focus when the reader selected. `useSelectionFocus` runs on the next payload, clears the request, and moves focus to the selected tree node (or the center) only if focus is still on `from` or has fallen to `body`; focus the reader moved while the subject was pending is kept. Since MIK-L34 the node is `selectionNode`'s: a followed marker's unknown-membership state (`[data-target-state-focus]`) when the rail shows one, else the tree's current node (review R1 F3).

**The per-hunk intent markers' scope (MIK-L34, MIK-R34).** `ReviewWorkspace` is now a thin wrapper around the landed body, renamed `WorkspaceBody` and otherwise unchanged. The wrapper builds the scope with `useIntentMarkerScope` from the task context, the payload's tree comparison (`treeComparisonNumber(payload.limitations)`), the change inventory (`markerInventory`: the listed paths, and whether the inventory is partial or not measured) and the workspace's own moves (`markerNavigation.workspaceMarkerMoves(state, navigation)`), and provides it through `IntentMarkerScope.Provider`. A dataset review names no comparison, so the scope is `null` and no diff below draws a mark or reads a classification. `WorkspaceState` gains `setOpenPath`, the raw setter a follow (which closes the file the marker sat in) and a return (which reopens it) use without the focus move `openFromCenter` makes. `WorkspaceBody` renders `MarkerReturn` (`← Back to <file>`) in the grid's full row while a followed marker has not been returned to; below 60rem it is sticky (`markerReturn`), so it stays in view at the target on a phone. `WorkspaceRail` passes the answered subject (none while another subject is read) to `FamilyRailContext`, which asks `useInvariantTargetState(subject, context)`: for the invariant a marker opened on an unknown membership that has no row in this tree, the rail shows `InvariantTargetState` ("Attribution unknown", the reason, and that this is not a confirmed absence) in place of the review's own statement when no tree is composed, or above the composed tree (ruling 2026-09-30T16:19:34 Q3, review R1 F3).

**One sticky offset for the triage bar and the way back (MIK-L33 with MIK-L34; ruling 2026-09-30T17:47:43's merge
plan).** On the stacked layout (at or below 60rem) both leaves have a sticky control: MIK-L34's `Back to <file>` and
MIK-L33's triage bar in the family tree (`ChangeBadges.TriageControls`). `useMarkerReturnState` reads the scope's
`origin` and sets `data-marker-return="open"` on the workspace root while a way back is shown; the `workspace` class
then sets `--review-sticky-top: 2.75rem`, and the triage bar sticks at `top: var(--review-sticky-top, 0)`. The way
back keeps `top: 0.5rem` with `z-index: 2` and is now a fixed 2rem box (one line, an ellipsis for a long file name),
so the offset is exact (0.5 + 2 + 0.25 gap) and neither covers the other. Side by side nothing changes: the rail
scrolls on its own and the way back is not sticky. Measured in the browser at 390 px with both stuck (Back 19–51 px,
the bar 55–151 px, computed `top` 44px) and by the reviewer's 20-step scroll sweep; the one transitional step where
the tree's end scrolls the bar up under Back keeps Back on top and clickable (review R3-2, accepted). The workspace
root is inside `ReviewSurface`'s `data-kbzone="review"`, so `j`/`k` also act from a returned marker outside the tree
(the merge round); L34's hold ends on the key first.

### Conventions

Styles come from `../../../styled-system/css` as module-level constants (`workspace`, which since MIK-L33 also
holds the stacked layout's `--review-sticky-top`, `markerReturn`, `fullWidth`, `shell`,
`title`, `muted`, `mono`, `jump`), matching the cockpit panels' idiom. Imports are split by kind: React
hooks from `react`; the payload types (`ReviewPayload`, `ReviewFamilyContext`, `ReviewFamilySideName`,
`ReviewSelectorKind`) as type-only imports from `../../data/review`; `carriedPage` as the module's one
value import from that entry; `treeComparisonNumber` and `useReviewTrees` from `../../data/reviewTrees`
(MIK-L31); `ReviewPageRequest` as a type-only import from `./ReviewReadCycle`;
`FamilyReviewCenter`, `FamilyTree`/`FamilySelection`, `ReviewScopeHeader` and the type-only `DiffLayout` from their own modules.
Every sub-component is a plain function taking the values it renders; props are threaded rather than
re-derived, so two mount points of the same control cannot drift. Test ids are the contract
(`review-workspace`, the `review-scope-*` ids now rendered by `ReviewScopeHeader.tsx`, `review-reading-pending`,
`review-reading-problem`, `review-roster-walk`, `review-family-tree`,
`review-family-context`, `review-family-limitation`, `review-jump-to-selection`, `review-center-column`,
`review-display-state`, `review-center-display-controls`, `review-center-diff-layout`,
`review-center-full-file`), and the workspace root publishes `data-diff-layout` and `data-full-file` so a
case can read the live preferences off the element. No fetch appears in this file; its one `useEffect` is
`useSelectionFocus`, and its one read is the leaf-wide tree view through the adapter's `useReviewTrees` hook
(MIK-L31), made only for a tree comparison. The lane read is the surface's (`ReviewSurface.ReviewPanes`, MIK-L32
review F1) and arrives as `laneRead`; the lane's components come from `./UnexplainedLane`, `GateRead` from
`./LaneFileFocus` and `explorerAttribution` from `./laneFocus`. The intent markers' pieces come from their own modules
(`MarkerReturn` from `./IntentMarkers`, the scope from `./intentMarkerScope`, the target state from
`./MarkerTargetState`, the moves from `./markerNavigation`), so this file holds only the provider wrapper, one control
line and the rail hook. The file is 747 lines (MIK-L33 added `useContext`, the sticky offset and `useMarkerReturnState`).

### Invariants And Boundaries

Semantic selection never filters the full changed-file population. On a tree comparison the explorer's labels are the lane's buckets and never the landed accounting's (MIK-L32 ruling Q1; part of the candidate invariant recorded on `review_unexplained_lane.py.md`), and a lane that is pending or unread is never labelled with a guessed bucket. Confirmed no-family, unselected, absent and unreadable context remain different states, and an unknown membership opened from an intent marker is its own `Attribution unknown` state, never the `No recorded family` statement (MIK-L34). Display preferences do not change knowledge or comparison identity.

**R26 isolation under a retained shell (L48).** While `reading` is set, nothing of the frame's subject is rendered as the requested subject's reading: the center shows only the requested subject's status, the scope header replaces its subject-bound lines, and the tree marks only the explicit choice. The rail's tree and source explorer keep the frame's attribution labels while the subject is pending or unavailable (A2 observation A2-O3): those are comparison-level labels of the task's source changes, not the new subject's intent. A selection never unmounts the workspace, its navigation, tree or open disclosures; only a read with no frame at all (the reviewer's first) has no workspace to keep.

### Todos

None recorded. The workspace adds no control that writes and no second reader of the review payload; its one
request of its own, since MIK-L31, is the leaf-wide tree view of a tree comparison (none for a dataset review); the
per-file classifications the intent markers read are asked by the scope it provides (`intentMarkerScope.ts`), once
per changed file per surface. The
one page control stays the surface's, the tree keeps its own keyboard traversal, and the centre keeps its
own statements. Any further layout work belongs to the owners named above rather than to this file.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no entries).
The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The current ownership and boundaries above are grounded in these source declarations.

- `useWorkspaceState` owns the behavior described above, including the lane selection a family choice clears (MIK-L32) and the raw `setOpenPath` an intent marker's follow and return use (MIK-L34). [1]
- `ReviewWorkspace` is a thin wrapper that provides the intent markers' scope (MIK-L34) around `WorkspaceBody`, the landed body, which owns the behavior described above; its props include the surface's lane read (MIK-L32). [2]
- **The unanswered subject's status and its two renderings in the reading area.** [3]
- **The reading-area column: one DOM node, only its content swapped; for a tree comparison it reads the leaf-wide tree view pinned to the payload's comparison (MIK-L31).** [4]
- **Selection focus lands only if the reader has not moved it; it prefers a followed marker's unknown-membership state to the tree's current node (MIK-L34, review R1 F3).** [5]
- The rail's family navigator, told whether the payload is a tree comparison (MIK-L35); for a followed marker's unknown membership with no row in the tree, the `Attribution unknown` state in place of the review's statement or above the composed tree (MIK-L34). [6]
- `WorkspaceRail` owns the behavior described above, with the lane's destinations after the families and no family node current while a destination is on screen (MIK-L32), and hands the answered subject to the family navigator for a followed marker's target state (MIK-L34). [7]
- The subject the rail receives: none while another subject is read. [8]
- `Back to <file>` in the grid's full row, sticky below 60rem so it stays in view at the target (MIK-L34). [9]
- The workspace's moves for a marker: select the target through the rail's own selection; restore subject, lane, opened path, layout and full file. [10]
- The lane's rail nodes, for a tree comparison only (MIK-L32). [11]
- The lane's centre and the gate's items only from the same comparison's leaf-wide read (MIK-L32). [12]
- `recordLabelOf` (moved to the scope header's module by L48) owns the behavior described above. [13]
- The explorer's labels: a tree comparison's from the lane (ruling Q1), a dataset review's from the landed partitions. [14]
- The stacked layout's one sticky offset while a way back is open, and the way back's fixed box (MIK-L33). [15]
- The workspace carries the state of the way back (MIK-L33). [16]
- The triage bar sticks below it. [17]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The workspace renders one repository namespace's
records, and carries no identity that ranges beyond it; the repository id it displays is the one the
payload's own candidate published.

No meaningful cross-repo references found.
