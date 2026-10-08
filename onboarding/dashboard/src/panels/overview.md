# dashboard/src/panels/ — Cockpit Panels Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/`                          |

## The Intent Reviewer (`review/`)

`review/` is the child route of the intent reviewer. The cockpit mounts its entry component, `ReviewSurface`, full-bleed when a change-set target carries a review. The target names the repository, the master and the leaf, optionally a subject (a family or an invariant), and optionally the recorded history view of a closed leaf. The files of this child route have their cards under `review/`; there is no `review/` overview, and this section is their route text. The unexplained-changes lane, the per-hunk intent markers, the word-level intent diff and the focused expression cards have their own sections below.

### One owner each

| Module | What it owns |
| --- | --- |
| [`ReviewSurface.tsx`](review/ReviewSurface.tsx.md) | The composition: which payload the workspace is mounted over, what every subject selection does, the refresh and retry handlers, the page controls, and the root (the reviewer's keyboard zone and its own vertical scrollport). |
| [`ReviewNavigation.tsx`](review/ReviewNavigation.tsx.md) | The reviewer's own read of the subject catalogue, the selected subject, the bounded hold of the first read, and the catalogue rail in which the family tree stands. |
| [`ReviewReadCycle.ts`](review/ReviewReadCycle.ts.md) | The read: one read per question, the newest read wins, a refresh replaces and does not patch, and an answer is bound to the question it answers. It also keeps `frame`, the task context's last admitted payload. |
| [`familyWalkMerge.ts`](review/familyWalkMerge.ts.md) | What an admitted roster continuation looks like once it is merged into the family context on screen. |
| [`ReviewReadCache.ts`](review/ReviewReadCache.ts.md) | What was already read for the comparison on screen: whole-subject reviews (24) and file contents (32), least recently used first out, emptied by an answer of another comparison generation. |
| [`ReviewOutcome.tsx`](review/ReviewOutcome.tsx.md) | The outcomes that are not a payload: loading, known-empty, and the one refusal and failure block. Only a network failure offers a retry. |
| [`ReviewRefresh.tsx`](review/ReviewRefresh.tsx.md) | The reader's refresh control and the notice that answers it. |
| [`ReviewWorkspace.tsx`](review/ReviewWorkspace.tsx.md), [`ReviewScopeHeader.tsx`](review/ReviewScopeHeader.tsx.md) | The layout (scope header, rail, reading area) and the transient inspection state held above the reads. |
| [`walkedTree.ts`](review/walkedTree.ts.md) | The walked tree: the families the family tree shows across selections. |
| [`FamilyTree.tsx`](review/FamilyTree.tsx.md) | The family tree: each family with its joint guarantee and the full statements of its members, unchanged siblings included. |
| [`changeTriage.ts`](review/changeTriage.ts.md), [`ChangeBadges.tsx`](review/ChangeBadges.tsx.md), [`changeTraversal.ts`](review/changeTraversal.ts.md), [`triageOrderPreference.ts`](review/triageOrderPreference.ts.md) | Change kinds in the tree: order, counts and labels; badges, breakdown and the triage bar; the `j`/`k` traversal; the order preference. |
| [`FamilyReviewCenter.tsx`](review/FamilyReviewCenter.tsx.md), [`SubjectReview.tsx`](review/SubjectReview.tsx.md) | The central reading path: the family guarantee, the carried member context, the selected intent, the linked expressions and the evidence, with statements and evidence of the server-selected subject. |
| [`SourceExplorer.tsx`](review/SourceExplorer.tsx.md), [`SourceContent.tsx`](review/SourceContent.tsx.md) | The complete list of changed files, independent of the selection, and what one listed file opens into: its content at the two bound code trees. |
| [`ReviewRecordPanes.tsx`](review/ReviewRecordPanes.tsx.md), [`KnowledgeStatements.tsx`](review/KnowledgeStatements.tsx.md) | The record panes behind the "Technical details" disclosure: the knowledge, source, evidence and submission records of one admitted payload, and the statement area that draws each side by its declared state. |

### The reviewer stays mounted across subject selection

A read is shown only under the question it answers, and a selection changes only the reading area.

- `ReviewSurface` mounts the workspace over the answer for the subject on screen. While that subject is pending, failed or refused it mounts the workspace over the frame, with a reading status keyed to the requested question and labelled with the requested subject; a failure or refusal carries the owner's problem block. Record panes render only for an answer. Only the first read, which has no frame, is stated at the surface level.
- `ReviewWorkspace` keeps one reading-area column and swaps only its content.
- A subject already read for the comparison on screen is shown again from the read cache without a request, and a refresh always asks again.
- After the bounded wait for the catalogue, a reader gesture makes the subject on screen the reader's own, so a catalogue that answers late only fills the navigation; a reader who has not acted is moved to the first family without a remount.
- Rapid selections settle on the latest; the answer of a superseded subject selection is neither shown nor kept.

### The family tree: change kinds, triage order and `j`/`k`

On a tree comparison every family and every member occurrence shows what kind of recorded change brings it into review: `intent`, `implementation`, `membership`, `unknown` or `unchanged`, with secondary marks. Every fact is the server's, delivered with the roster as `change_kinds`; this route orders, counts and traverses by the facts and decides none.

- The tree lists families and member rows in triage order (by weight: intent, implementation, membership, unknown, unchanged) or in authored order. The choice is a browser-local preference (`review.tree-order.v1`), with triage order as the default. Neither order hides an unchanged sibling.
- `j` and `k` are the keymap owner's `review.nextChange` and `review.previousChange` chords. They are bound on the reviewer's zone (the surface root), so they act only while focus is inside the reviewer and are inert in text fields. A step focuses the next stop and clicks it, so a key step, the visible previous and next controls and a click on the row are one selection.
- The stops are the tree's rendered nodes whose primary kind is not `unchanged`, in displayed order. Past the last returned member of a family with unreturned members, `j` stops at that family's continuation control and loads nothing.
- At either end the selection stays and a polite message says so. The message belongs to the rows the tree showed when it was said: it is no longer shown once the tree has shown other rows, and it does not come back when the same rows are shown again.
- A dataset review carries no change facts: its tree has no badge, breakdown or triage bar, is listed in authored order, and binds no `j`/`k`.

### The walked tree

The server composes a family context per selected subject: one family for a family subject, every containing family for an invariant subject. The family tree shows the walked tree: the family contexts of the answers read so far, folded into one list.

- **A selection of a row the tree shows adds rows and removes none.** This holds for `j`/`k`, for the visible previous-change and next-change controls, for a pointer on a family row or a member row, for a member opened from the reading area's member list, and for the continuation control of a kept family.
- **A kept family** is a family the tree shows that is not in the selected subject's own context. It is drawn whole, tagged "kept · last read for …" with the subject it was last read for (visibly and as the family row's accessible description), and counted apart in the tree's scope line. "Family context details" and the reading area describe the selected subject's own answer only.
- **Every other selection starts the tree afresh** at the moment it is made: a row of the subject catalogue or of the list of all invariants (also one that names a subject the tree shows or the subject already selected), "All source changes", the offer to open the task context after a refusal, a followed intent marker and the return from it, and the subject the reviewer opens with. A refresh of the review and an answer of another comparison start it afresh as well. Rows of two comparisons are never shown together, and a polite status beside the tree says when kept rows were dropped for that reason.
- **These neither remove a row nor start the tree afresh:** the search filter (which hides and restores kept families like the others), the order control, a roster continuation of a family of the selected subject, a lane destination, a refresh of the subject catalogue, the page controls, opening a file, a failed or refused read, and the retry of a failed selection.
- **Back to one family.** While the tree holds a kept family, the catalogue lists a row for every family the tree shows, without badges; choosing one starts the tree afresh with that family alone.
- **One displayed order.** The walk lists its families by family identifier, and the tree orders them by weight and then by that order (in authored order, by identifier alone), so the order in which answers arrive plays no part.
- **Kept families with unreturned members.** Using the continuation control of such a family selects that family, keeps the tree, and continues its roster from the furthest cursor the tree holds.
- **No added state and no added read.** The walk is derived from answers already read, inside the mounted reviewer. A selection issues one review read for a subject not yet read and none for one the read cache holds; nothing is read for a kept family.

### Focus, refresh and retry

- A selection leaves a focus request that records the number of the tree intent current when it was made. Only a render made after the selection answers the request, so an effect of an earlier render that runs late cannot spend it. Focus then lands on the selected tree node, unless the reader has moved focus elsewhere in the meantime.
- On the stacked layout (60rem and narrower) an in-tree selection reveals the start of its reading area: the answer when it arrives, and the failed or refused status once the read ends unavailable. A status reveal moves no focus and leaves the selection's focus request for a retry. Every other selection and every wider layout keeps its previous scroll behavior.
- A refresh starts the walked tree afresh and leaves a request that only brings the selected row into view, once an answer that arrived after the refresh is shown. The request is dropped when the refresh's own read fails or is refused.
- The retry of a failed refresh is the refresh again and asks for the same scroll. The retry of any other failed read only reads again.

### Pages, history view and record panes

- The page controls offer the walkable collections and "whole review". A next page is offered only for a cursor the payload published, and a refused page is shown with its refusal and a first page of the requested collection.
- The history view is part of the question: a closed leaf's entry asks for the leaf's recorded comparison, the header states "Historical task comparison", and the root publishes `data-review-history`.
- The record panes are pure display of one payload's record fields. They are handed a payload only when it answers the subject on screen; while another subject is pending or unavailable the disclosure stays mounted and says that the records are being read.

### Tests and fixtures

All mounted cases mount the real `ReviewSurface` and stub only `fetch`.

- Between a selection and its answer: [`review/ReviewSurface.navigation.test.tsx`](review/ReviewSurface.navigation.test.tsx.md) (the mounted shell, the pending and problem states, reuse, the latest selection, a late catalogue, and the order in which a focus request is answered). The family composition: [`review/ReviewWorkspace.family.test.tsx`](review/ReviewWorkspace.family.test.tsx.md). The cache's own rules: [`review/ReviewReadCache.test.ts`](review/ReviewReadCache.test.ts.md).
- Change kinds and traversal: [`review/changeTriage.test.ts`](review/changeTriage.test.ts.md), [`review/FamilyTree.triage.test.tsx`](review/FamilyTree.triage.test.tsx.md), [`review/FamilyTree.triageReal.test.tsx`](review/FamilyTree.triageReal.test.tsx.md), [`review/ReviewSurface.triage.test.tsx`](review/ReviewSurface.triage.test.tsx.md), [`review/ReviewSurface.triageMarkers.test.tsx`](review/ReviewSurface.triageMarkers.test.tsx.md) and [`review/changeTraversal.test.tsx`](review/changeTraversal.test.tsx.md) (the traversal status on the hook alone).
- The walked tree: [`review/walkedTree.test.ts`](review/walkedTree.test.ts.md) (7 unit cases over served bodies), [`review/ReviewSurface.walk.test.tsx`](review/ReviewSurface.walk.test.tsx.md) (10 cases: by key, by click, the tag and counts, the catalogue rows, the filter, and the end message), [`review/ReviewSurface.walkFresh.test.tsx`](review/ReviewSurface.walkFresh.test.tsx.md) (21 cases: which selections keep and which start afresh, the stacked reveal of an in-tree read, and the scroll after a refresh and after its retry), [`review/ReviewSurface.walkStore.test.tsx`](review/ReviewSurface.walkStore.test.tsx.md) (3 cases on the store-authored comparison, including a deliberate failed read), [`review/ReviewSurface.walkPartial.test.tsx`](review/ReviewSurface.walkPartial.test.tsx.md) (2 cases on a real partial answer), [`review/ReviewSurface.walkUnavailable.test.tsx`](review/ReviewSurface.walkUnavailable.test.tsx.md) (10 cases: the failed and refused status reveal on the stacked layout, by click and by key, and the moved-focus guard) and their shared kit [`review/walk.test-utils.tsx`](review/walk.test-utils.tsx.md). [`review/markerNavigation.test.ts`](review/markerNavigation.test.ts.md) pins that a marker's follow and return pass no selection options.
- Fixtures are captured answers, each set with a receipt, and every body has its own card:
  - [`review/triage.capture-provenance.json`](review/triage.capture-provenance.json.md), [`review/triageReal.capture-provenance.json`](review/triageReal.capture-provenance.json.md) and [`review/triageMarker.capture-provenance.json`](review/triageMarker.capture-provenance.json.md) for the change-kind tests;
  - [`review/walkReal.capture-provenance.json`](review/walkReal.capture-provenance.json.md): 16 real served bodies of the scratch leaf 260928-MIK-L33. They are the catalogue ([entries](review/walkReal.entries.captured.json.md)), the task context ([task](review/walkReal.task.captured.json.md)), the two family reviews ([FAM-R6R095RW](review/walkReal.FAM-R6R095RW.captured.json.md), [FAM-2HBJREC2](review/walkReal.FAM-2HBJREC2.captured.json.md)), the seven changed members ([INV-2E8MG43K](review/walkReal.INV-2E8MG43K.captured.json.md), [INV-ZS9ZS878](review/walkReal.INV-ZS9ZS878.captured.json.md), [INV-555EHWM8](review/walkReal.INV-555EHWM8.captured.json.md), [INV-BR5MTSTY](review/walkReal.INV-BR5MTSTY.captured.json.md), [INV-H8EM1VJR](review/walkReal.INV-H8EM1VJR.captured.json.md), [INV-VPX81HXV](review/walkReal.INV-VPX81HXV.captured.json.md), [INV-2TQGXFAX](review/walkReal.INV-2TQGXFAX.captured.json.md)), the tree routes ([lane](review/walkReal.lane.captured.json.md), [file](review/walkReal.file.captured.json.md), [source](review/walkReal.source.captured.json.md)) and the partial pair ([INV-2TQGXFAX-page2](review/walkReal.INV-2TQGXFAX-page2.captured.json.md), [FAM-R6R095RW-continued](review/walkReal.FAM-R6R095RW-continued.captured.json.md));
  - [`review/walkStore.capture-provenance.json`](review/walkStore.capture-provenance.json.md): 7 served bodies of the store-authored world of `mcp/tests/test_review_change_kinds.py`. They are [entries](review/walkStore.entries.captured.json.md), [shared](review/walkStore.shared.captured.json.md), [sharedPage](review/walkStore.sharedPage.captured.json.md), [FAM-F00001](review/walkStore.FAM-F00001.captured.json.md), [FAM-F00002](review/walkStore.FAM-F00002.captured.json.md), [FAM-F00001Continued](review/walkStore.FAM-F00001Continued.captured.json.md) and [INV-PPPPPP](review/walkStore.INV-PPPPPP.captured.json.md);
  - [`review/walkUnavailable.capture-provenance.json`](review/walkUnavailable.capture-provenance.json.md): the one genuine refused body [`walkUnavailable.refused.captured.json`](review/walkUnavailable.refused.captured.json.md) that the status-reveal cases replay.

- The cockpit mounts the reviewer for a change-set target that carries a review, with its optional subject and history view. [130]
- The surface's hook composes navigation, read cycle, cache, selection, refresh and retry, and the reading status. [131]
- The workspace is mounted over the answer or the frame, and the records only over an answer. [132]
- The read cycle: the read state bound to its question, and the task-context frame. [133]
- The bounded cache of one mounted surface and its generation test. [134]
- The one failure and refusal block, with the retry control of a network failure. [135]
- The record panes behind the "Technical details" disclosure. [136]
- The reading-area column is one node whose content alone is swapped. [137]
- The weights of the change kinds and the two orders, which only reorder. [138]
- The order preference and its storage key. [139]
- The stops in displayed order, the stop at a partial family's control, and the end messages. [140]
- A step focuses and clicks the stop, and the chords are bound on the reviewer's zone only when the tree has change facts. [141]
- The end message is given out only beside the rows it was said for and is dropped in the commit that shows other rows. [142]
- The tree draws the walked families, hands the traversal the rows it shows, and mounts the triage bar only with change facts. [143]
- One step of the walk: an in-tree selection keeps, any other selection and another comparison replace. [144]
- The workspace advances the walk, marks the tree and the reading area apart, and selects rows of the walked tree. [145]
- Every selection numbers the tree intent, keeping only with `keepTree`. [146]
- A refresh starts the tree afresh and asks only for a scroll; the retry of a failed refresh is the refresh again. [147]
- The catalogue lists a row for every family the tree shows while one is kept. [148]
- The kept tag and the scope line that counts kept families apart. [149]
- The focus request is answered only by a render made after it; a pending or unavailable read is handled without spending it. [150]
- The page controls: a next page only for a published cursor, and the refusal of a requested page. [151]
- The mounted case of the key walk on real data. [152]
- The mounted cases of the reviewer between a selection and its answer. [153]

## 260928-MIK-L34 Per-Hunk Intent Markers In Every Diff Of A Tree Comparison

**Route meaning extended (MIK-R34, adopting ICR-R34@v1).** On a tree comparison, every diff of a changed text file in
the review workspace marks each hunk with the invariants whose recorded ranges meet its changed lines; following a
marker opens that invariant at its tree position, and `Back to <file>` returns to the hunk with focus on the marker.
Every mark comes from MIK-R32's one per-file classification (no second classifier, no client intersection), and a
dataset review renders exactly as before. The new modules under `review/`, governed here like L31's, L32's and L35's
(no `panels/review/` overview):
- [`review/hunkMarkers.ts`](review/hunkMarkers.ts.md): the pure model. One file-level mark for a confirmed-unregistered
  or wholly unreadable file, otherwise one mark per owner hunk; realizations under "Intents" and proofs under "Tests",
  never counted together; each family occurrence with its target and membership state (and, for an unknown one, the
  reason, restated from L32's rule: review N1); the labels (`2 intents`, `INV-… · test`, the compact `2`, `1+1t`,
  `?`, `!` below 40rem); placement on the owner's side lines (`markAnchor`).
- [`review/IntentMarkers.tsx`](review/IntentMarkers.tsx.md): the marks and their lists in a pane (`usePaneMarking`),
  the landed source-content view (`useSourceMarking`, only on the drawn blobs the classification names), card excerpts
  (`useExcerptMarking`, only the drawn sides compared: review R1 F1), `MarkReadNote` (unlisted, loading, unavailable,
  other content: never silence, review R1 F5) and `MarkerReturn`.
- [`review/intentMarkerScope.ts`](review/intentMarkerScope.ts.md): the workspace's scope (the comparison, one cached
  classification read per listed changed path per surface, the followed marker and the return) and `markerInventory`
  (a partial or unmeasured inventory is partial: review R2).
- [`review/markerNavigation.ts`](review/markerNavigation.ts.md): the workspace's moves (select the target through the
  rail's own selection; restore subject, lane, opened path, layout and full file; clear the tree's focus request).
- [`review/MarkerTargetState.tsx`](review/MarkerTargetState.tsx.md): the `Attribution unknown` state of a followed
  marker's unknown membership, on the member row, in the rail (focusable, named and described: review R1 F3) and in the
  centre, never `No recorded family`, with the review's own context kept beside it.
- [`file-viewer/markGutter.tsx`](file-viewer/markGutter.tsx.md), governed by the file-viewer overview: the CodeMirror
  marks gutter, collapsed runs expanded for a mark, the reveal and its bounded, passive hold.
- Tests (59 cases): [`review/hunkMarkers.test.ts`](review/hunkMarkers.test.ts.md) (12),
  [`review/IntentMarkers.test.tsx`](review/IntentMarkers.test.tsx.md) (21),
  [`review/ReviewSurface.markers.test.tsx`](review/ReviewSurface.markers.test.tsx.md) (3, the real surface over real
  bodies), [`review/intentMarkerScope.test.ts`](review/intentMarkerScope.test.ts.md) (2),
  [`review/markerNavigation.test.ts`](review/markerNavigation.test.ts.md) (4),
  [`review/MarkerTargetState.test.tsx`](review/MarkerTargetState.test.tsx.md) (2) and
  [`file-viewer/markGutter.test.tsx`](file-viewer/markGutter.test.tsx.md) (15).
- Fixtures, each set with its receipt: [`review/hunkMarkers.capture-provenance.json`](review/hunkMarkers.capture-provenance.json.md)
  (MIK-L32's lane fixture world in six scenarios, [`hunkMarkers.classifier.captured.json`](review/hunkMarkers.classifier.captured.json.md)),
  [`review/markerReturn.capture-provenance.json`](review/markerReturn.capture-provenance.json.md) (the scratch leaf's
  comparison 2: [task](review/markerReturn.task.captured.json.md), [lane](review/markerReturn.lane.captured.json.md),
  [file](review/markerReturn.file.captured.json.md), [source](review/markerReturn.source.captured.json.md),
  [invariant](review/markerReturn.invariant.captured.json.md)) and
  [`review/markerUnknown.capture-provenance.json`](review/markerUnknown.capture-provenance.json.md) (comparison 3 after
  `break-family`: [task](review/markerUnknown.task.captured.json.md), [lane](review/markerUnknown.lane.captured.json.md),
  [file](review/markerUnknown.file.captured.json.md), [source](review/markerUnknown.source.captured.json.md),
  [memberUnknown](review/markerUnknown.memberUnknown.captured.json.md), [noFamily](review/markerUnknown.noFamily.captured.json.md);
  and comparison 2's [card entries](review/markerReturn.cards.captured.json.md)). All thirteen sha256 values match.

**Hooks in the landed renderers.** [`changeset/DiffPane.tsx`](changeset/DiffPane.tsx.md) and
[`file-viewer/FilePane.tsx`](file-viewer/FilePane.tsx.md) take an optional `marks` (an unmarked pane is the landed one).
[`review/SourceContent.tsx`](review/SourceContent.tsx.md) threads an optional `markers` prop to its panes.
[`review/LaneFileFocus.tsx`](review/LaneFileFocus.tsx.md) marks every owner hunk a window draws, draws the file-level
mark once above the windows, hands the lane's own classification to the full file and reopens it on a return.
[`review/ExpressionCards.tsx`](review/ExpressionCards.tsx.md) marks its excerpts, names each full-file pane and reopens
the exact card on a return. [`review/ReviewWorkspace.tsx`](review/ReviewWorkspace.tsx.md) is a thin wrapper providing
the scope around the landed body (`WorkspaceBody`), with `setOpenPath`, the `Back to <file>` control (sticky below
60rem), the rail's target state and its focus preference. [`review/FamilyTree.tsx`](review/FamilyTree.tsx.md) renders
the member-row note (an import and one element) and [`review/FamilyReviewCenter.tsx`](review/FamilyReviewCenter.tsx.md)
the centre's family line through `MemberFamilyLabel` (one expression; `memberContextLabel` moved out). The data adapter
gains `readFileClassification` (the data overview's MIK-L34 section).

**Rulings.** 2026-09-30T13:07:38: the L32 review F5 carry (every hunk visible in a window is marked). 15:11:20: start;
markers come from L32's per-file response; the "shows every one" wording made accurate. 16:19:34: Q1 the visible Back
control only, no browser history; Q2 on a linked hunk the unread side's changed lines use the file's per-side
availability, L32's response unchanged; Q3 a per-member `Attribution unknown` state distinct from `No recorded family`,
built at the selection target with the `FamilyTree.tsx` edit kept minimal; Q4 card excerpts are marked and a collapsed
run never hides a mark. 17:39:21 (review R1, changes-required): F1 excerpts compare only the sides they draw; F2 compact
marks below 40rem; F3 the focused `Attribution unknown` region; F4 the three escaped mutations pinned and the full set
rerun; F5 the partial-inventory note; notes N1 (the reason's owner named in a comment), N2 (off-screen marks outside
CodeMirror's drawn area are not in the tab order) and N3 (a followed target's state stays until Back) accepted; landing
order L34 before L33, and at L33's sync both member-row elements are kept, the change-kind fact first, both reasons in
`aria-describedby` (built by MIK-L33's merge round). 18:23:50 (review R2): Back refocuses and re-scrolls after CodeMirror's measure on every layout,
including side by side at 390 px; three test gaps pinned. 19:27:57 (review R3): the hold also ends on wheel (passive);
the hold's end conditions and cleanup pinned by frame-by-frame tests. A short R4 confirmation runs beside this curation.
**Resolved:** the L32 F5 carry. Its Todos on `review/laneFocus.ts` and `review/LaneFileFocus.tsx` (and on the `mcp` and
`application` overviews and `review_unexplained_lane.py`) are resolved: every hunk a window draws is marked, and the
more-hunks note no longer says "the full file shows every one".

**Candidate invariants (not ingested):**
1. Every intent marker comes from L32's per-file classification response; the client never intersects ranges itself
   (realized by `hunkMarkers.ts` and the scope's one read per changed file; proved by `hunkMarkers.test.ts` over six
   real scenarios, the surface case's one read with `comparison=2`, and the mutation sets; recorded on
   `hunkMarkers.ts.md`).
2. Every hunk drawn in any diff surface carries its mark: lane windows, full files, card excerpts, including hunks inside
   collapsed runs (realized by `usePaneMarking`, `useSourceMarking`, `useExcerptMarking`, `LaneFileFocus.useWindowMarking`
   and `markGutter.expandMarkedRuns`; proved by `IntentMarkers.test.tsx`, `markGutter.test.tsx` and the surface case's
   card excerpts; recorded on `IntentMarkers.tsx.md`).
3. Unknown membership is always distinguishable from confirmed no-family (realized by the target's state and reason,
   `occurrenceLabel` and `MarkerTargetState.tsx`; proved by the surface case on real comparison 3 and
   `MarkerTargetState.test.tsx`; recorded on `MarkerTargetState.tsx.md`).
4. Back returns focus to the originating marker with its hunk in view, and never takes focus or scroll away from the
   reader (realized by the scope's return, `markerNavigation.restore`, the pane-local reopen and `markGutter`'s reveal,
   bounded passive hold and redraw carry; proved by the surface return case, `IntentMarkers.test.tsx`'s return cases,
   `markGutter.test.tsx`'s hold and redraw cases, and the R2 and R3 browser matrices at 390 and 1600 px; recorded on
   `MarkerTargetState.tsx.md`).

- Marks only from the owner's response, placed on its side lines. [5]
- Every owner hunk a pane draws is placed; the list and the reveal of a return. [6]
- A lane window marks each neighbour its context shows (the L32 F5 carry). [7]
- The scope provided around the landed workspace body. [8]
- The unknown-membership state in the rail. [9]

## 260928-MIK-L32 The Unexplained-Changes Lane: Two Destinations After The Families, And One Classification Everywhere

**Route meaning extended (MIK-R32, adopting ICR-R33@v1).** On a tree comparison (the payload's `review:trees:<n>`),
changed source that no recorded entry explains is a review destination of its own, and the entry counts it. The new
modules under `review/`, governed here like L31's and L35's (no `panels/review/` overview):
- [`review/laneFocus.ts`](review/laneFocus.ts.md): the pure presentation rules. The destination titles and group
  notes, the two groups in the server's order, "5 files · 3 hunks · 2 non-text" (file and hunk totals separately),
  the hunks a destination opens a file on, each hunk's window cut on the server's side line numbers (rule 8, three
  lines of context, `beyond` for a bounded prefix), and the labels the explorer and the technical details take from
  the lane (`explorerAttribution`, `laneAttributionFacts`, `laneCountText`).
- [`review/UnexplainedLane.tsx`](review/UnexplainedLane.tsx.md): `LaneDestinations` (the rail nodes after the
  families; pending `…`, `unavailable`, `not measured`, never a zero) and `UnexplainedLaneCenter` (the bucket's files,
  then the attributed files carrying the class, each group with a one-line note and each row's reason behind "Why").
- [`review/LaneFileFocus.tsx`](review/LaneFileFocus.tsx.md): an opened file's facts, one diff window per focused hunk
  from the landed source-content read of the exact blobs, the full file one control away, and the gate's own items for
  the file through L31's `UnexplainedGroups` ("reading" until the slower leaf-wide read answers, never "none").
- [`detail-panel/intentReviewEntry.tsx`](detail-panel/intentReviewEntry.tsx.md) renders the entry's count as its own
  element after `+N −N`: `· K unexplained`, `· K unexplained · U unknown`, `· attribution partial` (with the unmeasured
  scope in a disclosure), `· attribution unknown`, and nothing for 0/0, pending or a dataset comparison (rule 9).
- Tests: [`review/laneFocus.test.ts`](review/laneFocus.test.ts.md) (3),
  [`review/ReviewSurface.lane.test.tsx`](review/ReviewSurface.lane.test.tsx.md) (7, the real surface over the real
  bodies), [`detail-panel/intentReviewEntry.attribution.test.tsx`](detail-panel/intentReviewEntry.attribution.test.tsx.md)
  (8), and the seven captured bodies with their receipt
  ([`review/laneReview.capture-provenance.json`](review/laneReview.capture-provenance.json.md); the summary, task,
  leaf-wide trees, lane, file and source bodies of the MIK-L32 scratch leaf's comparison 2).

**Hooks in the landed renderers.** [`review/ReviewSurface.tsx`](review/ReviewSurface.tsx.md) makes the **one** lane
read (`ReviewPanes`, review R1 F1) and hands it to [`review/ReviewWorkspace.tsx`](review/ReviewWorkspace.tsx.md) (the
rail destinations, the centre swap, no family node current while a destination is chosen, the gate items only from
the same comparison's leaf-wide read, and the explorer's labels from the lane: ruling Q1) and to
[`review/ReviewRecordPanes.tsx`](review/ReviewRecordPanes.tsx.md) (the source pane's attribution counts and lists
from the lane: review F1). [`review/SourceContent.tsx`](review/SourceContent.tsx.md) exports its keyed, cached read for
the focused diff. [`review/ReviewSurface.gitTrees.test.tsx`](review/ReviewSurface.gitTrees.test.tsx.md) answers the
lane read without a lane (its captures predate it) and asserts unavailable, never zero, and the dataset review's
landed labels and details word for word. A dataset review makes no lane read and renders none of this.

**Rulings.** 2026-09-30T12:19:20: Q1 the explorer takes the lane's buckets on a tree comparison; Q3 a gate-held
non-text change is listed under `Unexplained changes` only for an attributed file; Q4 an unexplained hunk in a file of
unknown attribution stays in `Unknown attribution` (rule 10); Q5 the membership states as mapped, L34 may refine (it kept them); Q6
the entry's count shows even when the intent counts are refused. 13:07:38 (review R1): F1 the technical details
follow the lane; F5 carried to L34 (a focused window's context can show a neighbouring hunk without its own mark;
resolved by L34: see its section above);
F6 accepted (the L35 word-diff stub needs no change). Review R2: pass. **Resolved:** L35's carried rerun: L32 landed
second, and `ReviewSurface.wordDiff.test.tsx` was rerun on the L35-synced tree and passes (the Todo on that card is
resolved). L31's "disposition controls plug into `UnexplainedGroups`" Todo is resolved as display only: MIK-R32's
Exclusions forbid assessment, approval or waiver. The two code comments that still assigned disposition to the lane
were corrected in this leaf (comment text only, in `worklistGroups.ts` and `LeafKnowledgeChanges.tsx`): history rows
(MIK-R10), which the closeout gate enforces, answer the unexplained items, and the panel and the lane only list
them.

**Candidate invariants (not ingested):** on tree comparisons the explorer and the technical details take their
attribution from the lane, so no two surfaces disagree; a lane or count that is pending, unread or unmeasured never
reads as zero or as a guessed bucket; the entry's count is a separate fact from `+N −N`, read in the same request.

- The explorer's and the details' labels from the lane. [10]
- The rail nodes and the centre. [11]
- One opened file: focused windows, full file and the gate's items. [12]
- The one lane read handed to the workspace and the details. [13]
- The entry's count as its own element. [14]

## 260928-MIK-L35 The Word-Level Intent Diff In The Central Reading Path

**Route meaning extended (MIK-R35, adopting ICR-R35@v1).** On a tree comparison (the payload's `review:trees:<n>`),
a changed statement, applicability, condition, exclusion or family guarantee now reads as **one prose passage with
its removed and added words marked in place**, inside L31's decluttered structure, which it keeps. The new modules
under `review/`, governed here like L31's (no `panels/review/` overview):
- [`review/wordDiff.ts`](review/wordDiff.ts.md): the pure half. Whitespace-preserving word tokens, the token LCS with
  replaced phrases as one removed and one added run, the byte decision (identical, whitespace-only with all
  whitespace removed per review R1 F3, or words), `REWRITE_RATIO = 0.5` (ruling Q2: over the longer side, exactly
  0.5 is not a rewrite), the `DIFF_CELL_LIMIT` coarse bound, exact reassembly (rule 8), and rule 1a's list
  alignment (LCS by exact text, moved items out before gap pairing, gaps paired only on equal counts, never
  positional; ruling Q5).
- [`review/IntentWordDiff.tsx`](review/IntentWordDiff.tsx.md): the rendering and the **tree-comparison scope**
  (`TreeComparisonScope` / `useTreeComparison`), inline or side by side, the rewrite fallback with its reason and an
  unsaved per-passage "Show inline", whitespace-only with both exact texts disclosed, `<del>` / `<ins>` marks with
  visually hidden "removed:" / "added:" text (rule 7), the R06 one-sided lines distinct from an unreadable side
  (rule 5), the statement area and the changed guarantee; the layout control only where a word-diffed passage is
  drawn (review R1 F5, R2-1).
- [`review/intentDiffPreference.ts`](review/intentDiffPreference.ts.md): the browser-local layout preference
  (`review.intent-diff.layout.v1`), inline by default and when storage is unavailable.
- Tests: [`review/wordDiff.test.ts`](review/wordDiff.test.ts.md) (12),
  [`review/IntentWordDiff.test.tsx`](review/IntentWordDiff.test.tsx.md) (30, accessible-text assertions) and
  [`review/ReviewSurface.wordDiff.test.tsx`](review/ReviewSurface.wordDiff.test.tsx.md) (3, the real surface over the
  real git-trees bodies, a tree review against a dataset review).

**Hooks in the landed renderers.** [`review/SubjectReview.tsx`](review/SubjectReview.tsx.md) decides text-first on a
tree comparison (`textFirstComparison` in [`review/statementWording.ts`](review/statementWording.ts.md)) and reads
each side's text only from that side's own member row, or from the pane and the field rows filtered to the selected
revisions (review R1 F1; ruling Q4 applies the filter on dataset reviews too).
[`review/FamilyReviewCenter.tsx`](review/FamilyReviewCenter.tsx.md) wraps its body in the scope, word-diffs a changed
guarantee first, and names `same_revision_text_changed` in its details;
[`review/FamilyTree.tsx`](review/FamilyTree.tsx.md) takes a `tree` prop from
[`review/ReviewWorkspace.tsx`](review/ReviewWorkspace.tsx.md) so the rail's joint guarantee and member tags compare
text bytes (review R1 F2).

**Rulings.** 2026-09-30T11:53:13: Q1 the same-revision label ("revision r2 → r2 · the same revision on both sides;
its text differs": MIK-R21 increments `revision` only when meaning changes, so the bytes decide), Q2
`REWRITE_RATIO = 0.5`, Q3 **no word diff for dataset reviews** (the scope is the one switch), Q4 the field-row
filter on both paths, Q5 rule 1a as written, Q6 the centre roster (`FamilyMemberContext`) out of scope. 12:16:39
(review R1): F1 per-side rows, F2 every tree-comparison label compares text bytes, F3 whitespace-only detection, F4
added tests, F5 control placement. 12:43:15 (review R2): pass-with-notes; R2-1 fixed, R2-2 (a whitespace deletion
that joins two words is labelled whitespace-only) and R2-3 (one extra bounded diff for control placement) accepted as
notes. **Carried:** whichever of L35 and L32 lands second reruns `ReviewSurface.wordDiff.test.tsx` against L32's lane
fetch (a Todo on that card; resolved by MIK-L32, see its section above).

**Candidate invariants (not ingested):** on tree comparisons no review surface calls a changed text unchanged (the
byte comparison decides, even at the same revision); a changed intent field reads as one passage with removed and
added words marked in place, and both texts are reconstructed byte for byte; each side's text comes only from that
side's own row, or from its pane or filtered field rows; dataset reviews get no word diff.

- The decision, the ratio and rule 1a. [15]
- The tree-comparison scope, the statement area and the changed guarantee. [16]
- Each side's text from its own row, the filtered field rows, and the text-first decision. [17]
- The rail's labels compare bytes on a tree comparison; with MIK-L33's change facts the badges state a text change and the labels do not repeat it. [18]
- On real bodies: a tree review word-diffed, a dataset review as landed, and one guarantee revision never called unchanged. [19]

## 260928-MIK-L29 The Knowledge Reader Panel

**New panel folder (MIK-R29): `knowledge-reader/`,** governed by this overview. Following the `review/` precedent it
has no route overview of its own. It is the dashboard's **Knowledge** area: a read-only reader of one repository's
knowledge at any memory tree, browsed like a file explorer, needing no task. Since MIK-R79 (below) it is the
**Knowledge product view**: a full-width, retained layer on the File Viewer shell, so leaving the tab and coming back
shows the same document at the same place.

- [`knowledge-reader/KnowledgeReader.tsx`](knowledge-reader/KnowledgeReader.tsx.md): the panel composition: the
  single-line toolbar, the resizable tree/document/aside group, the address's own read, the citation pane and the
  outline. The address is the URL hash, so every document link is a navigation and a view can be shared;
  citations and fragments stay local; with no address it
  lands on the first repository's root summary (F2).
- [`knowledge-reader/ReaderToolbar.tsx`](knowledge-reader/ReaderToolbar.tsx.md): the repository and memory-tree
  selectors, the record lookup, the selection banner and pin, and the named side-read failures; `useRead` keeps one
  promise per selection so the lookup and the Records branch share an acquisition.
- [`knowledge-reader/KnowledgeTree.tsx`](knowledge-reader/KnowledgeTree.tsx.md): the explorer on the shared
  `ExplorerTree`: path rows, the entry counts, the "Show every path" filter, the two count rows and the Records
  branch (families, decisions and other records; invariants stay out).
- [`knowledge-reader/PathViews.tsx`](knowledge-reader/PathViews.tsx.md): the path view (prose, invariants with
  states, families here or routed, linked records, references last), a directory's bounded summary and paged
  subtree, the without-proof list and the census view. The cited code view is
  [`knowledge-reader/ReaderCode.tsx`](knowledge-reader/ReaderCode.tsx.md).
- [`knowledge-reader/TruthView.tsx`](knowledge-reader/TruthView.tsx.md): every field in its fixed order, the
  invariant and family parts, a decision in full with the **derived** status (F9), links both ways (unreadable links
  named, F11/F17), and the timeline with each source's state.
- [`knowledge-reader/readerParts.tsx`](knowledge-reader/readerParts.tsx.md), [`ReaderOutline.tsx`](knowledge-reader/ReaderOutline.tsx.md),
  [`ReaderCode.tsx`](knowledge-reader/ReaderCode.tsx.md) and [`readerNavigation.ts`](knowledge-reader/readerNavigation.ts.md):
  the shared links/badges/entry rows and the prose whose `[n]` markers are linked in text nodes only (F4); the "On
  this page" outline; the cited code in the File Viewer's pane; and the top/Back place of the reader.
- [`knowledge-reader/KnowledgeReader.test.tsx`](knowledge-reader/KnowledgeReader.test.tsx.md) (28 cases) over
  [`knowledge-reader/knowledgeReader.captured.json`](knowledge-reader/knowledgeReader.captured.json.md), the real
  served bodies; MIK-R79 added the order/top/Back, citation-pane, phone and shared-acquisition cases.

The existing panels are unchanged (the packet's preservation boundary). The data adapter is
`data/knowledgeReader.ts`; the shared primitives are `grammar/Markdown.tsx`, `grammar/ExplorerTree.tsx` and
`file-viewer/FilePane.tsx`.

## 260928-MIK-L79 The Knowledge Page Is Full Width And Reads From The Top

**Route meaning changed (MIK-R79).** The Knowledge panel is no longer a transient, railed view: it is one of the four
product destinations (Chats, Operations, Knowledge, File Viewer) and a full-width retained layer on the File Viewer
shell. The tree and the document scroll on their own; a document reads from its title through its text, its record
sections and its references last, with no empty section drawn; a followed link opens at the top and Back returns to
the place left; a citation opens the cited code beside the text on a wide screen and as its own page at 70rem and
below; and the phone layout shows the document with "Browse" opening the tree as a full screen of rows.

- [`knowledge-reader/KnowledgeReader.tsx`](knowledge-reader/KnowledgeReader.tsx.md) is the composition and the one
  records acquisition shared by the toolbar and the Records branch; [`KnowledgeTree.tsx`](knowledge-reader/KnowledgeTree.tsx.md)
  is the shared-tree adapter with the optional `hasKnowledge`/`hasOverview`/`coverage` fields consumed from
  `data/knowledgeReader.ts`.
- New modules: [`ReaderToolbar.tsx`](knowledge-reader/ReaderToolbar.tsx.md), [`ReaderOutline.tsx`](knowledge-reader/ReaderOutline.tsx.md),
  [`ReaderCode.tsx`](knowledge-reader/ReaderCode.tsx.md) and [`readerNavigation.ts`](knowledge-reader/readerNavigation.ts.md).
- Shared grammar: [`grammar/ExplorerTree.tsx`](../grammar/ExplorerTree.tsx.md) (the one tree for the File Viewer and
  Knowledge) and [`grammar/referenceMarkers.ts`](../grammar/referenceMarkers.ts.md) (opt-in `[n]` markers and heading
  ids for the shared [`grammar/Markdown.tsx`](../grammar/Markdown.tsx.md)); the File Viewer's `FileTree.tsx` now
  adapts the shared tree and `file-viewer/useFilesTree.ts` is deleted.
- Backend: [`application/knowledge_reader/tree_coverage.py`](../../../../mcp/src/agents_remember/application/knowledge_reader/tree_coverage.py.md)
  answers the tree from one code pass and one memory enumeration; `paths.py`'s `tree_listing` delegates to it and
  `files.py` no longer lists directories.

Since `260928-MIK-L37` the truth view shows a history row with its `effect` and its `because` targets (a record ID
as a navigation link, a requirement named), and a link whose source is a history row as the record the row is about
(MIK-R29 rules 4 and 5).

- A history row's line: its effect, and its because targets as links. [120]
- An incoming link from a history row names the record the row is about. [121]

## 260928-MIK-L31 Focused Expression Cards In The Central Reading Path

**Route meaning extended (MIK-R31).** For a tree comparison, the review centre no longer shows whole files in an
accordion: [`review/ExpressionCards.tsx`](review/ExpressionCards.tsx.md) shows every code and test location of the
selected family's members as one focused card per (path, range) — role or facet, the side path and resolved range
on each side, the authored rationale directly above an excerpt from the exact side blobs, a changed range as its real
diff, an unchanged range once and labelled, a not-current MIK-R03 mark, and **Full file** / **All changed files** on
every card. [`review/focusedCards.ts`](review/focusedCards.ts.md) owns the grouping, MIK-R01 order, counts, voices and
the bounded-roster scope ("These cards cover the loaded n of m members", review F2; R2-5; R3-N1 accepted);
[`review/statementWording.ts`](review/statementWording.ts.md) owns the 13:40 "wording unchanged" rule that
[`review/SubjectReview.tsx`](review/SubjectReview.tsx.md) and the guarantee block apply;
[`review/worklistGroups.ts`](review/worklistGroups.ts.md) groups the worklist (L11 marks, `planned_untouched`, L10
unexplained groups, PS-1 rows) that [`review/LeafKnowledgeChanges.tsx`](review/LeafKnowledgeChanges.tsx.md) renders
(MIK-R25 rules 2-3, carried from L25 Q2). [`review/FamilyReviewCenter.tsx`](review/FamilyReviewCenter.tsx.md) mounts
the cards (`CenterExpressions`), takes planning marks only from a leaf-wide read of the same comparison
(`pinnedWorklist`), and places the knowledge panel, or the notice that stands in its place while the leaf-wide
read is computed or unavailable, after the evidence;
[`review/ReviewWorkspace.tsx`](review/ReviewWorkspace.tsx.md) makes that leaf-wide read once per comparison, only for
a tree comparison. A dataset review makes no tree read and renders the landed
[`review/ReviewExpressions.tsx`](review/ReviewExpressions.tsx.md) (whose `ExpressionControls` the cards reuse).
`changeset/DiffPane.tsx` and `file-viewer/FilePane.tsx` gained optional `firstLine`/`fit` for excerpts. None of
the new modules has a `panels/review/` overview, following that route's precedent. **Since MIK-L35 (above)**, a tree
comparison's changed intent wording is word-diffed and its labels compare text bytes; the 13:40 rule and the dataset
path are unchanged.

**Fixtures (MIK-R31 rule 6).** The git-trees bodies were re-captured from L31's scratch leaf, with the new cards
body [`review/gitTrees.cards.captured.json`](review/gitTrees.cards.captured.json.md) (11 entries, every range
resolved); the six family fixtures L44 left at their old captures were re-captured from the current route (the
L44-R1-F5 remainder; the receipt's `mik_l31_recapture`), five dashboard expectations moved to current-route truth,
and the one branch no real body reaches is covered by a labelled SYNTHETIC body (ruling 2026-09-30T05:36:19 Q3).
A comment-only follow-up refreshed the headers of `ReviewWorkspace.family.test.tsx` and
`ReviewReadCycle.family.test.tsx` to name the re-capture, and `familyExpressions.test.ts`'s measured-shape comment
to name the re-captured `walkFinal` revision.

**Candidate invariants (not ingested):** focused cards group by (path, range) with the rationale above the excerpt,
and a missing rationale is a gap; a bounded roster never reads as the whole family; card planning marks come only
from a leaf-wide read of the same comparison; dataset reviews make no tree read.

- The card component. [24]
- Grouping by (path, range) and the bounded-roster scope. [25]
- Cards for a tree comparison, marks only from the same comparison. [26]
- The conforming example on real data. [27]

## 260928-MIK-L25 The Landed Review Workspace Over A Converted Leaf's Git Trees

MIK-R25 rule 6: the family-centered review workspace and its navigation keep their behaviour; only their data
source changed, from datasets to the derived indexes of the memory trees. No panel component changed.
[`review/ReviewSurface.gitTrees.test.tsx`](review/ReviewSurface.gitTrees.test.tsx.md) (new) proves it on real
data: the real `ReviewSurface`, with only `fetch` stubbed, renders the served family review of the worker's
converted scratch leaf (`review:trees:2`), its source inventory with the one changed file, the family's whole
7-member roster, and the touched member's own review. Its three bodies
([`gitTrees.family`](review/gitTrees.family.captured.json.md),
[`gitTrees.invariant`](review/gitTrees.invariant.captured.json.md),
[`gitTrees.entries`](review/gitTrees.entries.captured.json.md)) and the adapter's body are receipted in
[`review/gitTrees.capture-provenance.json`](review/gitTrees.capture-provenance.json.md). They were recaptured under
the directory-name refs (ruling 2026-09-30T02:32:42 (a)); the reviewer's R6 check explained every delta. The panel
that renders the tree view itself was carried to L31/L32 (ruling 2026-09-29T22:22:37 Q2) and is rendered since L31
(above), which also re-captured these bodies from its own scratch leaf (`review:trees:1`).

- The one case: the landed workspace over a converted leaf's trees. [28]
- The receipt of the captured bodies (five since L31). [29]

## 260921-ICR-L44 Two Family Bodies Re-Captured Under A Receipt, Five Still At Their Earlier Capture

The review cases' captured route bodies are no longer one provenance generation. `familyReview.complete`
and `familyReview.identical` (and `subjectReview.family` / `subjectReview.invariant`) were re-captured
over HTTP from the real review route so their member sources carry `locator`, `resolved_ranges` and
`locator_state`; each re-capture is recorded in a receipt beside the fixtures —
`review/familyReview.capture-provenance.json` (new) and `review/subjectReview.capture-provenance.json`.
`familyReview.truncated`, `.continued`, `.oneSided`, `.walkFinal` and `.emptyRoster` still hold their
capture at `63b47629`, and `familyPaging` its capture at `a5bec6c3`: the current route resolves roster
members from content and claim items too, so it cannot reproduce the first states, and several cases
assert those older states. The receipt's worker-stated `not_recaptured` section and the case headers said
so. **Superseded by MIK-L31:** all six were re-captured from the current route, the receipt's `not_recaptured`
section was replaced by `mik_l31_recapture`, and the cases were moved to the current route's states (see the L31
section above); a comment-only follow-up refreshed the case headers to match.

- The receipt's MIK-L31 re-capture, which replaced the not-re-captured section. [30]
- The case header stating which bodies were re-captured (both captures since MIK-L31's follow-up). [31]

## The Leaf's Knowledge Panel And Its Notice

On a tree comparison the review centre shows the panel "Knowledge changes in this leaf"
([`review/LeafKnowledgeChanges.tsx`](review/LeafKnowledgeChanges.tsx.md)): the Git diff of the two memory trees, the
currentness of each side, and the worklist with the history rows about its items. The workspace makes the leaf-wide
tree read once per comparison ([`review/ReviewWorkspace.tsx`](review/ReviewWorkspace.tsx.md), `useReviewTrees`) and
hands it to [`review/FamilyReviewCenter.tsx`](review/FamilyReviewCenter.tsx.md), whose `knowledgePanel` decides what
stands in the panel's place:

- no leaf-wide read, which is the case of a dataset review: nothing;
- a read that answered with trees: the panel `LeafKnowledgeChanges`;
- a read that is loading: `LeafKnowledgeNotice` with the status line "Computing the knowledge changes of this leaf.
  The first read of a large leaf takes several seconds; the review stays usable.";
- a read that is unavailable: the notice with the failure's detail and its next action;
- a read that answered `not-converted`: nothing.

The place of the panel is therefore not empty while a tree read is expected; an absent panel would read as "this leaf
changed no knowledge". The family, member and unselected centres receive the panel from this one function, the
unselected centre opened. The cards' planning marks come only from a leaf-wide read that answered for the comparison
the payload was composed over (`pinnedWorklist`).

- The panel, the notice, or nothing. [122]
- Planning marks only from a leaf-wide read of the same comparison. [123]
- The body passes the knowledge panel to the family, member and unselected centres. [124]
- The panel: status line, degraded sides, diff, currentness, worklist. [125]
- The notice for a loading and for an unavailable read; nothing for any other phase. [126]
- The workspace makes the leaf-wide read only for a tree comparison, pinned to the payload's number. [127]
- The notice says that it is computing, as a status region. [128]
- The notice names the failure and its action. [129]
- The notice draws nothing for a dataset review. [154]

## 260921-ICR-L32 The Change-Set Control Renders The Refusal It Receives

`detail-panel/changeSetBar.tsx`'s `ChangeSetButton` for `mode: "committed"` used to clear its counters on a
rejected read and show nothing else, so a **refused** read and a **pending** one were the same pixels. Since
`260921-ICR-L32` the control renders the refusal's own code and reason (`data-review-code`, the owner's
detail text) beside a `data-review-state` marker, keeps the pending state distinct, and still opens the
change set it names when clicked — the case that pins it drives the click and asserts the rendered reason,
not merely the absence of counters. The transport half of the same change is recorded on the
`dashboard/src/data` route.

## 260921-ICR-L33 A Landed Master's Leaves, And What A Closed Row Still Says

Three of this route's panels changed, and they change one story: **a master whose work has all landed is
readable, bounded, and attributable.**

> **WITHDRAWN by `a9a1a41b`, recorded by the `260921-ICR-L34` curation — the two paragraphs below about
> `LifecycleList.tsx` and `useCollapsedTaskGroups.ts` describe code that is in no tree.** Commit
> **`a9a1a41b`** (*"Revert L33's operations-list change; clear the pre-existing ruff-format red"*) is a
> **direct emergency commit with no curator pass behind it**: it deleted
> `panels/lifecycle-list/landedLeaves.ts` (its sidecar was deleted by this curation and is not listed
> below any more), removed 250 lines from `LifecycleList.tsx` (1189 now), deleted 366 lines from
> `hierarchy.test.tsx` (355 now), and restored `useCollapsedTaskGroups.ts` to its 28-line pre-L33 shape
> with one collapse set and `toggleCollapsed(key)`. `leafRecordsLandedWork`, `childFactsByParent`,
> `enclosureForDoc`, `markAutoCollapsed`, `rowIsCollapsed`, `landedLeafDocs`, `openedKeys`,
> `setCollapsed` and `CollapseState` **exist nowhere in the code tree**. The *third* panel
> (`panels/changeset/`) is not affected by the revert and its paragraphs stand.

**`lifecycle-list/LifecycleList.tsx`** *(withdrawn — see the banner above)* admits a landed leaf — a non-master task document whose status is
`Completed` — as a row under its OPEN master, instead of only ever admitting a leaf whose worktree
physically exists. The supporting rules moved into a new sibling module,
`lifecycle-list/landedLeaves.ts`: `leafRecordsLandedWork`, `childFactsByParent`/`rowChildFacts`,
`enclosureForDoc` (the one join, moved so admission and the row builders cannot disagree),
`markAutoCollapsed`, `rowIsCollapsed` and `landedLeafDocs`. The bounds are two, and both are measured:
a row whose only children are its own landed leaves is closed by default and prints `N landed`
(`Tasks · 57 → 167` on the live projection, with 110 landed rows carried at first paint and 19 masters
held closed); and a row that carries OTHER rows is never closed by that rule, because one orchestration
row owns a 161-row subtree. The list's header count still counts task ENTRIES rather than projected
documents, and now says so in its own tooltip.

**`panels/useCollapsedTaskGroups.ts`** gained the second half of the reader's collapse state —
`operations.tasks.opened.v1`, the keys opened past a row's default, beside the unchanged
`operations.tasks.collapsed.v1` — and its public signature changed from `toggleCollapsed(key)` to
`setCollapsed(key, collapsed)`, because only the caller knows the row's default.

**`panels/changeset/ChangeSetViewer.tsx`** is governed by the `changeset/` child route, so its own record
lives there; what belongs here is the panel-level fact: both of the dashboard's master-net readers pass
`includeLeaves: true`, superseding the `includeLeaves: false` optimisation commit `a1521685` introduced.

- The header count itself. **Withdrawn in part:** the tooltip this row cited stated *what* the count counts, and the L33 revert removed it with the landed-leaf change — the h2 is again a bare `Tasks · {count}`. [39]
- The bar's request for the net's per-leaf attribution. [40]

## 260921-ICR-L25 The Change-Set Bar Names An Unrecorded Range

**`detail-panel/changeSetBar.tsx` — an unrecorded change-set range is named, not printed as a zero
(register B6).** A `committed` read of a live leaf has no landed commit to read yet. The route used to
answer that state with a `404`, which the browser logs as a console error on the page whose accepted
criterion is **zero** — and the bar probes that view as soon as a leaf document is opened. The route
now answers it in the body (`state: "unrecorded"` plus its own sentence naming the missing endpoint
and the two views that produce it), and the bar renders it as the control's **own** state
(`data-review-state="unrecorded"`, distinct from `known-empty`) while **withholding the `+0 −0`
total**: a zero of nothing is not a measurement. The three genuinely distinct refusals are untouched —
an unknown leaf is still a `404`, a bad or absent `mode` a `400`, an enclosure `scope` its own `404`.

## Hot Path Summary

Task detail prose, `TaskNotes.tsx`, and the shared notes reader use `TaskArtifactReaderTarget` for notes or registered requirement packets. `detail-panel/taskReader.tsx` mounts the requirement-link context; `notes-reader/NotesReaderViewer.tsx` owns the kind-aware content transport and takeover.

## Governing Overview

[dashboard/src overview](../overview.md)

## Current Structural Panel Contract

Panels receive real task-document hierarchy and current occupant facts from the data route. The
document chat and the session cockpit select structural document+role seats; task assignment posts that identity,
and replacement changes only the occupant. No panel derives hierarchy from spawn ancestry or treats
a lifecycle/session id as the task address.

## 260713-TES-L5F2 Change

The shared `SessionComposer` regression suite now proves that composer
answer mode does not require a lifecycle or gate. Both follow the same session-owned protocol as
the canonical cockpit: read the hosted session's bridge epoch, POST the answer to that exact
session's `interaction-response` route, lock duplicate sends, and never route an adapter answer
through reliable `/submit`.

## 260731-EFA-L8 Split Layout

### 260713-TES-L1 Reviewed — Heartbeat Wording In Session Cockpit

Route body reviewed for the supervisor → agent-notifier rename: the session-cockpit heartbeat UI
(`BusPane`, `SeatInspector`, `SessionRail`, `sessionRailParts`, sessions-view) now uses
`AgentNotifierHeartbeat` / `agentNotifierHeartbeat` and "Agent notifier heartbeat" labels. No
panel-shape or layout change; per-file detail lives in the session-cockpit overview and the file
sidecars.

The frontend-rail size remediation (R4/R5) re-shaped this route: `DetailPanel.tsx`
→ `detail-panel/` (canonical entry + `state.ts`, `model.ts`, `lifecycleBody.tsx`,
`taskReader.tsx`, `taskDocPanels.tsx`, `changeSetBar.tsx`, `styles.ts`, seven
behavior-split test files + `test-utils.tsx`); `LifecycleList.tsx` →
`lifecycle-list/` (four behavior-split test files + `test-utils.tsx`);
`SessionsView.tsx` → `session-cockpit/sessions-view/` (controller/body/palette/
styles + six test files); `ConversationTimeline.tsx` →
`session-cockpit/conversation/conversation-timeline/` (12 machinery modules +
seven test files); `engineRoomStyles.ts` → engine-room style domains + `styles.ts`
barrel; `EnclosureCanvas.tsx` → eight engine-room sibling modules. Shared panels
also gained parts/styles modules (`sessionComposer*`, `terminalSession.ts`,
`interactionParts*`, `launchFlowParts*`, `sessionRailParts*`, `stageLayers.tsx`,
`conversationSurfaceParts*`, `chatsStageStyles.ts`). The naming rule
(kebab-case folder, one canonical entry, short responsibility-based siblings) is
now a repository guideline. Behavior is preserved.

## Whole-task opening answer reuse

The mounted reviewer keeps the existing bounded opening wait and subject-first navigation. If a late catalogue supersedes a successful whole-task read, the answer may be kept unshown under the compatible existing comparison generation; it never writes the current panes or advances an incompatible generation. Superseded selected subjects, refreshes/pages and failure/refusal answers stay excluded. Selected intent, family continuation, complete explorer and mounted inspection state retain their owners.

## Purpose

### 260731-EFA-L23 Route Delta

L23 makes Hangar expose optional durable lifecycle-operation kind, status, phase, and
`currentCommand` as one compact enclosure badge without inventing an operation when none is
projected. The live command stays single-line and width-responsive through CSS ellipsis, with its
complete value retained in `title`; it is not truncated once by character count.

TES-L6 changes the command-seat panel boundary from one global spine to sprint-qualified groups.
`FlowTab` consumes bound fixtures, while the session cockpit delegates group derivation to the data
model and renders legacy unbound seats only as migration state.

This route contains reusable cockpit panels plus focused child routes. Its strategic UI owners are:

- [session-cockpit](session-cockpit/overview.md) — the sole full-page Chats destination.
- [engine-room](engine-room/overview.md) — the Engine Room process visualization.
- lifecycle-list/LifecycleList.tsx + detail-panel/DetailPanel.tsx — Operations task navigation and reader.
- cockpit/document-chat/DocumentChat.tsx — the Operations right rail's native chat for the selected document and the shared bound launcher; it lives under `cockpit/` and reads canonical launch records plus native host state, not the session registry (the older RailChat.tsx was removed by MIK-R95 rule 8).
- Terminal.tsx, SessionComposer.tsx, and HighlightComposer.tsx — shared interactive surfaces
  consumed by the canonical cockpit.

Detailed session state, submission, withdrawal, cleanup, and authority behavior belongs in the
[data overview](../data/overview.md). This parent intentionally keeps only composition boundaries.

## FEUI-L9R Recovery Composition

The shared `Terminal` panel preserves its mounted xterm and scrollback while performing at most one
explicit socket reattach for each changed serving boot. The canonical Chats chooser owns a fixed,
bounded viewport dialog with explicit loading/empty/timeout/error states and operator Retry; it does
not render a pre-session adapter process or create a second catalog store. On an empty narrow
cockpit, responsive layout keeps the sole chat-creation entrance available.

## FEUI-MX-FIX-2 Open Failure Composition

Shared callers do not infer session creation from a completed request. `HighlightComposer.tsx`
shows a failed create before readiness or submit and sends no selected context. Its former direct leaf-chat target was removed with the old rail panel (MIK-R95 rule 8); the document chat's shared frame shows the same typed unavailable notice with Retry and never pretends a session is live. The composer consumes the legacy accepted-session-row result from the data route and writes no private row, focuses no requested id, and never retries through paste; the native document chat reads role launches, launch records and native host state instead and consumes no accepted-session row.

## Route Model

### Canonical Chats

FEUI-L8 retires the legacy Chats.tsx and SessionList.tsx path. CockpitShell now exposes one
Chats destination backed by the persistent session-cockpit layer; the shell now opens on this
Chats destination (260928-MIK-L79).
The right inspector is closed by default and toggleable. The replacement duty and deletion map lives
in the [session-cockpit overview](session-cockpit/overview.md).

- SessionRail + data/railModel replace SessionList + data/sessionGroups.
- ChatContextBar carries launch, task/leaf context, local lifecycle routing, and authoritative leaf
  attach/move duties.
- SessionsView owns smart focus, live action routing, persistent PTY composition, key/palette zones,
  and the optional inspector.
- LandedCleanupNotice and EndedSessionState retain unavailable cleanup and ended-row truth without
  pretending an empty PTY is a live conversation.

### Shared Interactive Panels

- Terminal.tsx is the xterm/socket wrapper. Since 260718-CHATS-L4 a controlled session's runner
  line-log appears only inside the read-only terminal-diagnostics drawer (the structured
  `ConversationSurface` is the controlled-session default); legacy raw sessions still host a vendor
  TUI. Terminal.tsx is not the structured conversation renderer — that lives in the
  [session-cockpit](session-cockpit/overview.md) `conversation/` grammar.
- SessionComposer.tsx is the shared CodeMirror reliable-submit surface. It consumes effective
  keymap/profile state and uses authoritative withdrawal for pop-back.
- HighlightComposer.tsx sends a selected context package only after acceptance; selection and target
  choice cannot move active route/focus on rejection or ambiguity. The removed direct leaf-chat path's
  pre-projection task-document fallback (`EMPTY_TASK_DOCUMENTS`) went with that branch in MIK-R95; the
  surviving composer keeps its snapshot-driven state and does not force React into an external-store
  update loop while analytics is still absent.
- cockpit/document-chat/DocumentChat.tsx mounts the selected task's native Paseo frame from canonical launch records and native host state, with the shared bound role launcher; it is not a session-registry consumer and not a competing destination.

### Operations And Other Routes

Operations, Detail, Engine Room, notes reader, file viewer, changeset, and lifecycle-design retain
their existing responsibilities. Focused child overviews and one-to-one file cards are authoritative;
the Chats refactor does not move those routes.

## Invariants And Boundaries

- Exactly one full-page Chats destination; no legacy Chats layer and no Sessions navigation item.
- Chats is initial (260928-MIK-L79); Operations is a product destination selected from the bar. The
Chats inspector is supplementary, default closed, and toggleable.
- Shared panels consume canonical data stores and authority clients; they do not create private
  session catalogs, conversation indexes, or submission ledgers. The 260718-CHATS-L4 structured
  surface holds only a reconstructable projection — no durable browser conversation index.
- Create-dependent panel actions proceed only after the shared opener returns an accepted server
  row; visible failure precedes readiness, focus, and delivery.
- The structured conversation surface (260718-CHATS-L4) is the controlled-session default and
  consumes adapter-normalized history/index/resume from the landed L1/L2/L3 contracts; the PTY
  line-log is now the read-only diagnostics drawer + legacy-raw body, not the message renderer.
- Reliable submit, withdrawal, interaction answers, bus replies, and control actions remain separate
  channels and never fall back to shared paste.
- No Domain Documentation source is configured; direct same-repository source, tests, reviewed task
  evidence, and recovered project history govern this route.

## Child Route Onboarding Map

| Child route | Governing overview |
| --- | --- |
| `session-cockpit/` | [Canonical Chats](session-cockpit/overview.md) |
| `engine-room/` | [Engine Room](engine-room/overview.md) |
| `file-viewer/` | [File Viewer](file-viewer/overview.md) |
| `changeset/` | [Change-Set Viewer](changeset/overview.md) |
| `notes-reader/` | [Notes Reader](notes-reader/overview.md) |

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Review child route — the family tree and the central reading path | [FamilyTree.tsx](review/FamilyTree.tsx.md) · [FamilyReviewCenter.tsx](review/FamilyReviewCenter.tsx.md) |
| Review child route — the workspace and the source explorer | [ReviewWorkspace.tsx](review/ReviewWorkspace.tsx.md) · [SourceExplorer.tsx](review/SourceExplorer.tsx.md) |
| Review child route — the leaf's knowledge panel and its notice | [LeafKnowledgeChanges.tsx](review/LeafKnowledgeChanges.tsx.md) · [LeafKnowledgeNotice.test.tsx](review/LeafKnowledgeNotice.test.tsx.md) |
| Review child route — the mounted family composition cases | [ReviewWorkspace.family.test.tsx](review/ReviewWorkspace.family.test.tsx.md) |
| Review child route — the walked tree and the traversal between changes | [walkedTree.ts](review/walkedTree.ts.md) · [changeTraversal.ts](review/changeTraversal.ts.md) |
| Review child route — the captured family bodies those cases are driven with | [familyReview.complete.captured.json](review/familyReview.complete.captured.json.md) · [familyReview.continued.captured.json](review/familyReview.continued.captured.json.md) · [familyReview.emptyRoster.captured.json](review/familyReview.emptyRoster.captured.json.md) · [familyReview.identical.captured.json](review/familyReview.identical.captured.json.md) · [familyReview.oneSided.captured.json](review/familyReview.oneSided.captured.json.md) · [familyReview.truncated.captured.json](review/familyReview.truncated.captured.json.md) · [familyReview.walkFinal.captured.json](review/familyReview.walkFinal.captured.json.md) · [familyReview.capture-provenance.json](review/familyReview.capture-provenance.json.md) |

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured. This compact
parent was refreshed from its repository-local child overviews, source/tests, and reviewed L8 record.

No relevant domain documentation was found for panels.

### Cross-Repo References

No cross-repository implementation source governs the panels route; all production imports resolve
inside agents-remember.

No applicable cross-repository source was found.

### Repo-Internal References

- The `Cockpit` view map contains the declared view map. [41]
- The Chats cockpit keeps its `SessionsView` mounted and toggles its display rather than unmounting it. [42]
- The persistent Chats layer renders `SessionsView` with active, selected lifecycle/leaf, task-document, and context props. [43]
- Dashboard state authority is held by `DashboardState`, `dashboardStore`, and `applySnapshot`. [44]
- The production application route is owned by `App`. [45]
- The production route returns `Cockpit`, which wires the live streams and renders `CockpitShell`, opening it on the Knowledge view for a `#knowledge?…` reader URL (MIK-R29). [46]
- `CockpitShell` defaults `initialView="chats"`; `VIEWS` is the four-entry product bar. [47]
- The terminal panel owns the shared terminal surface. [48]
- The shared composer surface is implemented by `SessionComposer`. [49]
- Selection-send behavior builds context and submits it to a selected or routed target, committing only on accepted or queued delivery. [50]
- `LifecycleList` owns Operations navigation, row grouping, the selection callback, and hidden-list re-show behavior. [52]
- `DetailPanel` resolves the selected task/lifecycle/series reader target and renders the task document content. [53]
- The lifecycle state vocabulary is the live/terminal partition consumed by the lifecycle panel; the `State`/`Phase` literals moved to `models/lifecycle.py` by 260731-EFA-L9 while the live/terminal sets stay in observer. [54]
- The shared fixture builders seed lifecycle and projection nodes from served fixtures, with required lifecycle fields copied from the served lifecycle. Ranges re-derived: the `lifecycle` occurrences this row names are at `:90-90`, `:243-243` and `:257-257`. [55]
- The typed fixture factories provide lifecycle and projection nodes. Ranges re-derived: the `lifecycle` occurrences this row names are at `:90-90`, `:243-243` and `:257-257`. [56]
- The hand-kept snapshot payload provides the generated timestamp. [57]
- `Dot` renders its state glyph inside `aria-hidden="true"`. [58]
### L23 Engine Room Admission Evidence

Panel-level operations now expose the control plane's source-lineage state as a
diagnostic fact. Rendering stays read-only and uses the projected summary for
operator context; recovery remains a backend worktree operation.

## Current L5I Route State

The panels route now treats keep-alive shells as an explicit performance boundary: persistent
top-level panels memoize unchanged shell rerenders, while their own store subscriptions remain live.
Interactive controls also favor evidence-bounded wording, including reopened gate failures and
viewport-measured leaf-picker placement.

## 260727-CHATS-IM-L2 No Route-Model Impact

The Engine Room effects overlay and session-cockpit child-history behavior are internal to their
existing child routes. Panel inventory, cross-panel ownership, and the shared panel primitive are
unchanged.

## 260731-EFA-L4 Typed Vocabulary Route Impact

The panel inventory is unchanged. What changed is the vocabulary the panels consume, and four rules
now hold across the route rather than inside one file.

- **The state mark is named by the panel, never by `Dot`.** `grammar/Dot` renders `aria-hidden="true"`,
  so the accessible name for a severity or a lifecycle state is the wrapper's duty. `AttentionQueue.tsx`
  wraps it in a `severityMark` span carrying `role="img"` + `aria-label="Severity: <severity>"`;
  `LifecycleList.tsx`'s `data-testid="task-state"` span carries the same kind of label with NO role and
  is correct only because it sits inside React Aria's `role="option"`, whose name-from-content absorbs
  it. Drop the role from the AttentionQueue wrapper and the severity leaves the accessibility tree
  entirely — `aria-label` on a bare `<span>` names a `generic`, which ARIA prohibits (axe-core
  `aria-prohibited-attr`, `serious`) and no screen reader announces. Any new panel that renders a `Dot`
  inherits this: supply a role that can hold a name, or sit inside one.
- **Two vocabularies reach one dot, and only one of them is the document's.** Both Operations row
  builders compute `lifecycle?.state ?? statusVariant(doc.status)` (`LifecycleList.tsx` `docRow` L595,
  `seriesRow` L644; `lifecycleRow` L717 passes `lifecycle.state` straight through), so a bound lifecycle
  hands `Dot` the RAW server state string and `statusVariant` only ever sees `TaskDocNode.status` /
  `SeriesNode.status` — whose entire vocabulary is `models/task_document.py::DocStatus`
  (planning · inProgress · Completed), assigned verbatim by `snapshots.py` at both build sites. That is
  why L4 could delete its `blocked` / `paused` / `abandoned` arms with no behaviour change: they sat on
  the right of the `??` and no served payload could enter them. Adding an `awaiting-developer` arm here
  would repeat the same defect — the live state already arrives on the left.
- **`awaiting-developer` is a rendered Operations state.** The lifecycle vocabulary is six states
  composed from named halves server-side (`observer/lifecycle_state.py`: `LiveState` + `TerminalState`,
  with `State = Literal[LiveState, TerminalState]` and `check_state_partition` refusing at import any
  state filed on neither side); `awaiting-developer` is LIVE, not terminal. `LifecycleList.test.tsx`
  pins the handover rather than the paint: an `awaiting-developer` row's mark must equal a bare
  `<Dot variant="awaiting-developer">` and must NOT equal what an unrecognised variant renders, and a
  `paused` row's mark must differ from an `abandoned` row's in the same list.
- **Rollup buckets are derived, not restated.** `Metrics extends LifecycleStateCounts` in the mirror and
  the bucket field names come from `ACTIVE_STATES` through `StateCountField<>`, so a seventh state adds
  a REQUIRED field and every object claiming to be a `Metrics` stops compiling until it counts it. The
  panels suites stopped hand-listing buckets: `LifecycleList.test.tsx` and `DetailPanel.test.tsx` build
  metrics with `metricsFor(lifecycles)`, the client twin of `reducer.py::_metrics`.

`DetailPanel`'s sub-task index now renders two different server rows. `SubTaskIndex` takes
`SubTaskRow`, the union of `TaskSubTaskRefNode` and `SeriesSubTaskNode` — two `extra="forbid"` server
models that share the common task-row fields but have distinct optional navigation/time fields. Only `TaskSubTaskRefNode` declares
`linkedLifecycleId`, so the cross-series `→` jump is reachable only from a master task document; the
branch is guarded by
`"linkedLifecycleId" in ref` and is structurally unreachable for a series rendered through
`seriesAsMasterDoc`. Only `SeriesSubTaskNode` declares `createdAt`, so creation ordering moved OFF the
index — where it could never have sorted a master's rows — and onto `seriesAsMasterDoc`, the one path
whose rows carry the field; `snapshots.py::_series_subtask_nodes` has normally already applied it, and
both sides skip the sort unless every row carries a `createdAt`.

**What the fixture conversion does and does not pin.** `EventRiver.test.tsx` and
`SessionComposer.test.tsx` no longer author wire nodes: every projection node comes from
`dashboard/src/test/fixtures/wire.ts`, whose bases are assembled from `dashboard/src/fixtures/snapshot.json`
and annotated with the mirror type, so a fixture that compiles is a shape the MIRROR can produce. Be
exact about the reach — `wire.ts` and `snapshot.json` are hand-maintained fixture/sample artifacts,
while `types/projection.ts` is generated and stale-checked from the Pydantic projection schema.
`tsc -b` binds `test/fixtures/wire.ts` to that generated mirror (annotated bases,
`Overrides<O, Node>` at every call site, `test/wireFixtureGuard.test.ts` refusing one-token opt-outs),
and `test/contract.test.ts` measures how completely `snapshot.json` exercises it in three type-level
directions plus runtime vocabulary assertions. The producer-to-TypeScript contract is held by the
generator and its stale check; the manual boundary is sample coverage.

## 260731-EFA-L7 — Conversation Split Absorbed

The panels route absorbed the L7 live-thinking change on top of the L8 split: the session-cockpit conversation family carries the coalesced live-thinking indicator and its pins; the over-limit dashboard files were split by L8 and the armed file-size rail now covers this route's TS/TSX.

## 260815-DAG-L14 Detail-Panel Route

`detail-panel/` threads `docPathForRef` so typed `masterRef` sprint rows open their commanded
master document (the sprint → master leg of the drill-down); the reader renders `MasterRefIndexRow`
for projected targets and falls back for unprojected ones.


## 260815-DAG-L12 Route Impact

New child route [sprint-graph](sprint-graph/overview.md): the optional sprint execution graph wave-grid view (≤3 boxes per row, ellipsized leaf lines, atomic lumps, textual predecessor labels, narrow single-column fallback). `detail-panel/taskReader.tsx` mounts graph content when present and mounts the sprint-scoped `CloseoutQueue` independently, so graph-less atomic-sequential sprints still expose scheduling state (L12-R5); `detail-panel/model.ts` `MasterDocView` carries optional `executionGraphView` (L12-R4).

## 260821-CLIVE Projection And Discard Panels

`CloseoutQueue` renders the producer's disposable service/source/problem/member projection. Typed
`invalid-empty` source problems include their repair action; the browser does not reconstruct
readiness or mutate queue state. Graph presence is not a prerequisite for this scoped projection.

The detail reader has a separate `Discarded before start` audit section with reason, timestamp, and
proof fingerprint. `LifecycleList` appends `N discarded` beside ordinary done/total progress. Both
surfaces preserve the same boundary: audited removal stays visible but never counts as completion.


## 260815-DAG Master Full-Gate Repair Route Impact

`session-cockpit` test suites (BusPane, ChatsStageBody, ConversationSurface, stageSurface) now flush the virtualizer scroll-observer debounce in an async `afterEach` before jsdom teardown.

## 260831-CCR-L23 Task-Artifact Reader Routing

L23 routed task-local requirement packets through the existing reader chrome: `DetailPanel.tsx`,
`taskReader.tsx`, `TaskNotes.tsx`, and the takeover now carry the shared discriminated
`TaskArtifactReaderTarget` (kind notes/requirements); the task reader mounts the
`TaskRequirementLinks` provider so task prose and References can open registered
`requirements/...` packets in the internal reader. The notes-reader child route owns the
viewer change; file-level detail lives in the panel sidecars.

## CCR-R18@v1 Hangar Fixture Versions

260831-CCR-L18 updated the Hangar render-test fixture so its hand-built `lifecycleOperation` sample carries the new `schemaVersion` and `stateMatrixVersion` literals required by the generated mirror. File-level detail lives in that sidecar.

## 260915-KS-L45 The Task-View Entry Into The Review Panel Is Reachable

*(Historical. The gate and subject read below were superseded by `260921-ICR-L2`/`L12` — the entry is
offered for every leaf — and the subject read left the entry entirely in `260921-ICR-L47`; see the
section "The Task Entry Into The Intent Review" at the end of this overview.)*

The review panel existed before this leaf; what did not exist was a **navigation** into it on a live
leaf task. `detail-panel/changeSetBar.tsx` is where that is decided, and the decision is now made from
the server rather than from a prop:

- The bar renders an **Intent review** `ChangeSetButton` beside the working and committed change-set
  buttons — never in their place — and the gate is `live && subject`: the leaf's enclosure must be
  live (one extracted `leafIsLive` predicate, shared with the working action so the two entries cannot
  disagree about what "live" means) **and** a reviewed subject must have come back from the server.
- The subject catalogue comes from a new read. `useReviewCatalogue(live, repo, master, leaf)` calls
  `intentReviewEntries(repo, master, leaf)` — the `data/review.ts` client for
  `GET /api/review/intent/entries` — and keeps `result.entries?.[0]`. The `selectorKind`/`selectorId`
  **props are gone**, because no production caller ever supplied them: `taskReader.tsx` and the master
  header pass `kind`/`repo`/`master`/`leaf`/`onOpen` only, so the old `live && selectorId` gate could
  never hold on a real navigation and the panel was unreachable by design rather than by policy.
- The gate is not weakened by the swap. A refusal, an empty entry list, a rejected promise and a
  non-live leaf all leave the subject `undefined`, so **no subject means no button** — the same
  behaviour as before, now reached through a source that can actually produce a subject. The hook
  fetches nothing at all for a leaf that is not live, because there is no candidate to resolve.
- The button's target carries the subject's **recorded** identity
  (`review: { selectorKind: subject.selector_kind, selectorId: subject.selector_id }`), so the browser
  still never chooses the candidate: the id is a recorded identity inside the candidate the server
  resolved from canonical task context, and the client's `ReviewEntry` has no path field on purpose.

The entry is also still the only reviewer affordance in the bar, and it still reports no counters —
its counter effect reads the leaf or master change-set request only. It is display-only in the same
sense the panel is: the bar offers a navigation, and the surface it opens generates no semantic
judgment and publishes no assessment.

- **The gate: a live leaf and a server-returned subject, with the subject's own recorded kind and id carried into the target.** [59]
- **The hook that asks the server for the leaf's reviewable subjects and keeps the first.** [60]
- **The one liveness predicate both gated entries read.** [61]
- The client the hook calls, whose `ReviewEntry` has no path field on purpose. [62]

## 260921-ICR-L13 The Change-Set Entry Threads The Published Generation

This route's change-set entry is now generation-bound for master nets. `ChangeSetButton`
stores the master read's published `generation` as pins and opens the viewer with
`{ ...target, generation }`, so the series view — and each file expansion inside it — reads
the listed generation rather than re-resolving the live tip. No panel was added and no
takeover dispatch changed; the reviewer entry, its liveness gate and its read are untouched
by this leaf.

- **The entry threading the published generation into the viewer target.** [63]
- **The generation state the button carries from a successful master read.** [64]

## 260921-ICR-L36 The Family Column's Third Part: The Deduplicated Changed Expression Excerpts

**Route meaning changed on the review child route: a whole-family selection now presents the family's own
changed expression excerpts, deduplicated, between its member context and the shared source explorer.** The
accepted design's whole-family line asks for three things — the full guarantee, all members including the
unchanged sibling, and deduplicated changed expression excerpts — and the centre composed only the first
two, so a reader who selected a whole family saw no expressions at all. Three sources changed and no Python
did: the payload already carried every fact, so the whole change is client-side.
`review/FamilyReviewCenter.tsx` gains the collection and the helpers it needed;
`review/ReviewWorkspace.family.test.tsx` gains the mounted case over the real captured body; and
`review/familyExpressions.test.ts` is a **new unit lane** that holds the arithmetic with no DOM, because the
captures do not carry every shape the arithmetic must get right.

**The four decisions in the collection, stated here because each one is a fact a reader would otherwise have
to re-derive from the source.**

- **"Changed" is the read's own realization resolution, and it is not the comparison's measured change set.**
  A claim is a row when the read did **not** find the recorded bytes at the recorded address
  (`recorded_blob_mismatch`, `path_absent`, `unsupported_locator`, `entry_not_blob`); `exact_recorded_blob`
  is the resolved state and is not a change; `recorded_object_unavailable` and `not_requested` are **not
  measured** and are counted apart rather than called changes. On the family this surface serves, the two
  notions disagree in the direction that matters — both stale addresses resolve as `recorded_blob_mismatch`
  while neither is a changed path of the comparison's own change set — so the verdict sentence and every row
  say which of the two is being read.
- **The dedup key is the address together with the *recorded* source identity. The observed identity is
  deliberately NOT in it, and that is the F1 repair.** The accepted prototype's key is the excerpt's address
  (`path + ':' + start`), but the claims this surface receives carry no line range of their own — the range
  lives inside the read's own `detail` sentence — so the identity used is the path together with the
  **recorded** bytes, which is the only thing that keeps two different recorded blobs at one path apart
  (the verifier's over-collapse probe found none). The observed identity is what the read **found** at the
  address in one side's tree, so a divergent address has **one observed value per side**; folding it into
  the key split that address into two keys — one per side — so the pass that pairs the sides could never
  find the other one and the row printed a single side. It is now carried **per side** in
  `readingsBySide`, beside that side's resolutions, where a read result belongs.
- **The collection is built from the family's carried membership rows, not from the centre's first-wins
  `distinct` list.** A resolution is a fact about the address **in one side's tree**, so a collection built
  from one row per revision would hide a change: the captured `familyReview.walkFinal` body records a member
  revision (`a08a87b4…` since the MIK-L31 re-capture; `d24e5187…` in the earlier capture) with `src/batch.py`
  under one recorded blob, resolved `exact_recorded_blob` on the before snapshot and `recorded_blob_mismatch` on
  the after one, and a `distinct`-built collection would
  have presented that address as resolved. **The second pass that joins the two sides is `recordSideReadings`
  (renamed from `recordSideResolutions` by the F1 repair), and it now carries a read result per side rather
  than a resolution per side:** each excerpt's `readingsBySide` holds that side's **resolutions** *and* the
  **observed identities** its read found, both read results and neither an identity. The verdict sentence's
  own clause was replaced outright, and **the F-V1-3 reword then replaced it again; the page now reads**
  *"every row below prints what each side's read made of its address — the resolution that side's claim
  carried — so an address both sides carried prints both readings whenever they differ, and an address only
  one side carried prints that side's alone."* **The superseded wording must not be quoted** (F-V1-3, low): it
  read *"…each side whose read resolved its address's recorded bytes…"*, and *"resolved"* **collides with the
  product's own name for `exact_recorded_blob`** — true under the reading the code implements, false under the
  literal one on every live row, where the changed sides are `recorded_blob_mismatch`. The reword names the
  reading explicitly, and the fix verifier asserted the row-by-row behaviour on the rendered page.
  The dedup arithmetic is unchanged
  by the repair and was re-measured: 8 membership rows, 8 changed row instances, 2 distinct keys with group
  sizes `[4,4]`, `8 − 2 = 6`.
- **One row per distinct excerpt, naming every membership row that recorded it, with the revision identity
  beside the label.** A display label alone is not a key: `ICR30-I-1` is recorded as **two** member
  revisions of its family, so a label-only row would name two different rows identically. On the live case
  the served family records 4 changed expression rows over 2 distinct addresses (8 rows counting both
  sides), and the mounted product renders **2** rows — `renderedDistinct: 2` against `renderedRowSum: 8`.

**The composition, and what it did not disturb.** The family column now runs guarantee → complete recorded
member context → the excerpt collection → the shared source explorer, which is the accepted design's
"lead with its own guarantee comparison and complete member context, then relevant expressions"; the
member-context card was **extracted** from `FamilyCenter` unchanged (`FamilyMemberContext`) so the column
reads as the three things it composes. **A3's member order is untouched** — the member selection's
`data-testid` blocks in document order are the same list before and after — and the three lines this leaf
re-measured on the new build (A5's unchanged-member expressions, A3's order, B4's full-file disclosure)
are present and unchanged. Two sentences the member-level attribution used to spell inline are now **one
owner each** (`unlistedPathNote`, `listedOrPlainPath`) because the collection needs the same two facts about
the same path, and two copies could drift into disagreeing about one path.

**The honest bound on the divergent rendering, and it travels with the claim.** The divergent case is
evidenced against the **captured `familyReview.walkFinal` body through a labelled fixture** — measured on the
fix round's build as `before exact_recorded_blob · after recorded_blob_mismatch`, with `data-sides =
"before,after"`. The divergence is exercised against the captured `familyReview.walkFinal` body through a **labelled
fixture**, and that label is the whole of its evidence. Live data was searched: **the search reached 3
families served by 1 leaf** (`260921-ICR-L34`, which returns `entries` with 3 families), and the other
**35 leaves refused `candidate_dataset_absent`** — each records no comparison generation, so no knowledge
operand exists for a subject to be listed from — and therefore **carry nothing to search. Absent is not
measured:** those 35 were not searched and found clean; they were unreachable, and a family that cannot
be listed cannot be shown to be divergence-free. **`260921-ICR-L36` is one of those 35**, so this leaf's
own live data carries no divergent family either. Read from `f1/raw/live-truth.json` and reproduced
independently by the verifier in `f1v/raw/vf1-live-scan.json` (`leavesAttempted: 36`, `leavesResolved:
1`, `leavesRefused: 35`, `refusalCodes: ["candidate_dataset_absent"]`, `familiesServed: 3`,
`familiesWithDivergence: 0`, `totalDivergent: 0`). The
live family renders the same 2 excerpts as before, and nothing on this route may be read as a claim that live
data exercises the divergent path.

- **The family column's three parts and the collection mounted as the third, after the member context and before the shared explorer.** [109]
- Family excerpt arithmetic groups recorded addresses and distinguishes changed, resolved and unmeasured realization readings. [110]
- Per-side resolution and observed identities attach to the same recorded-address key. [111]
- **The two hoisted owners the member attribution and the family collection share, so the two readers cannot drift.** [112]
- **The mounted case: the rendered count is the body's distinct excerpt set, every row's collapse count is the body's own group size, and EVERY rendered row's `data-sides` is checked against the sides the body resolves that excerpt on — the page's own both-sides sentence verified row by row against the body, not read from the page.** [113]
- **The new unit lane for the same arithmetic, its own statement of which inputs are constructed, and the pair of cases that state the whole key contract between them (recorded keeps two blobs at one path apart; observed may not, because two sides of one address legitimately see different bytes).** [114]

## Bounded family context across review pages

The existing ReviewReadCycle retains exact member content and source claims only within an admitted same-comparison, same-subject family-side-revision continuation. Rejected continuations state failure beside the retained coherent display; refresh and subject/history changes remain replacement reads. FamilyTree, FamilyReviewCenter and ReviewExpressions distinguish loaded context from raw item counts and partial/unavailable source scope. Source inventory, primary statement and evidence remain their existing owners' facts. The captured-page regression fixture and mounted read-cycle cases document this boundary. This holds for an answer. The family tree of the rail is the walked tree (see "The Intent Reviewer" above): it keeps families and member rows read for earlier subjects of the same comparison beside the answer, tagged as kept, and writes them into no answer.

## The Task Entry Into The Intent Review (`detail-panel/`)

- The Intent review is one control, `⇄ Intent review +N −N` (`(recorded)` for a closed leaf), rendered
  by the new [`detail-panel/intentReviewEntry.tsx`](detail-panel/intentReviewEntry.tsx.md). Its
  numbers are the comparison's **changed-intent counts** from `GET /api/review/intent/summary`
  ([`data/reviewIntentSummary.ts`](../data/reviewIntentSummary.ts.md)): `+` counts invariant and
  joint-guarantee revisions only the after side holds, `−` those only the before side holds, a revised
  statement once on each side. They are never the change set's line totals, which the entry used to
  show because it reused `ChangeSetButton` (and made a second identical committed request).
- The entry reads **no subject catalogue**, offers no picker, has no refresh control, prints no
  paragraph and subscribes to no global analytics document. It always opens the task-context review.
- `unavailable` and `partial` are explicit brief states (`no knowledge yet`, `offline`, `unreadable`,
  `partial`), never `+0 −0`. The owner's code, reason, offending input and next action sit in a closed
  `<details>` disclosure beside the control ([`detail-panel/entryState.tsx`](detail-panel/entryState.tsx.md));
  the change-set controls use the same brief-word-plus-disclosure pattern (ICR-R16).
- The summary re-reads when this leaf's own lifecycle facts move and when the entry's re-validation
  generation moves — on re-showing the task detail, on leaving the reviewer and on the reviewer's own
  refresh (Architect ruling 2026-09-28T16:27:28+02:00; no event system). Unrelated workspace
  publications cause no read. A live push while the same panel stays open is not delivered.

- The compact control, its brief states and its disclosure (since MIK-L32 with the lane's count beside `+N −N`). [115]
- The entry mounted in place of a change-set button. [116]
- The leaf-scoped facts and re-validation generation. [117]
