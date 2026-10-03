# dashboard/src/panels/ — Cockpit Panels Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/`                          |

## 260928-MIK-L33 Change-Kind Badges, Triage Order And `j`/`k` In The Family Tree Of A Tree Comparison

**Route meaning extended (MIK-R33, adopting ICR-R32@v1 with the storage substitutions).** In the review workspace's
family tree, on a tree comparison, every family occurrence and member occurrence shows what kind of recorded change
brings it into review (`intent`, `implementation`, `membership`, `unknown` or `unchanged`, with secondary marks);
the tree lists the most review-relevant changes first without hiding unchanged siblings, and `j`/`k` (and visible
controls) move between the changes. Every fact is the server's, delivered with the roster
(`application/review_change_kinds.py`); this route orders, counts and traverses by them and never recomputes one. A
dataset review renders exactly the landed tree (no badges, breakdown or controls; landed order; `j`/`k` inert). The
new modules under `review/`, governed here like L31's, L32's, L34's and L35's (no `panels/review/` overview):
- [`review/changeTriage.ts`](review/changeTriage.ts.md): the pure rules (weights, labels and meanings; a family's
  counts, returned, total, `partial` and `scoped` state and weight; the breakdown text; family and member order; the
  union of two deliveries across a roster walk).
- [`review/ChangeBadges.tsx`](review/ChangeBadges.tsx.md): the member badge and marks, the labelled reason lines
  ("change kind unknown", "membership unknown", "guarantee unknown"), the family's guarantee badge, the breakdown, and
  the sticky triage bar with the order control, previous/next and the polite status.
- [`review/changeTraversal.ts`](review/changeTraversal.ts.md): the stops in displayed order, the partial family's
  continuation stop, the ends, and the keymap owner's `j`/`k` bound on the reviewer's zone.
- [`review/triageOrderPreference.ts`](review/triageOrderPreference.ts.md): the browser-local order preference
  (`review.tree-order.v1`; triage when storage is unavailable).
- Tests (36 cases): [`review/changeTriage.test.ts`](review/changeTriage.test.ts.md) (12),
  [`review/FamilyTree.triage.test.tsx`](review/FamilyTree.triage.test.tsx.md) (18),
  [`review/FamilyTree.triageReal.test.tsx`](review/FamilyTree.triageReal.test.tsx.md) (3, real data),
  [`review/ReviewSurface.triage.test.tsx`](review/ReviewSurface.triage.test.tsx.md) (1) and
  [`review/ReviewSurface.triageMarkers.test.tsx`](review/ReviewSurface.triageMarkers.test.tsx.md) (2, the merge with
  MIK-L34 on real data); `session-cockpit/sessions-view/shell.test.tsx`'s `?` case is extended (the session-cockpit
  overview's MIK-L33 section).
- Fixtures, each set with its receipt: [`review/triage.capture-provenance.json`](review/triage.capture-provenance.json.md)
  (the store-authored world of `mcp/tests/test_review_change_kinds.py`: [entries](review/triage.entries.captured.json.md),
  [family](review/triage.family.captured.json.md), [familyPage](review/triage.familyPage.captured.json.md),
  [familyContinued](review/triage.familyContinued.captured.json.md), [shared](review/triage.shared.captured.json.md),
  [memberA](review/triage.memberA.captured.json.md), [memberH](review/triage.memberH.captured.json.md)),
  [`review/triageReal.capture-provenance.json`](review/triageReal.capture-provenance.json.md) (the worker's real
  scratch: [family](review/triageReal.family.captured.json.md), [shared](review/triageReal.shared.captured.json.md))
  and [`review/triageMarker.capture-provenance.json`](review/triageMarker.capture-provenance.json.md) (comparison 3's
  [cards](review/triageMarker.cards.captured.json.md)). MIK-L34's `markerReturn.*` and `markerUnknown.*` bodies were
  re-captured in the merge round and now carry `change_kinds` (their cards say so). All 22 sha256 values and byte
  counts match their receipts (checked by this curation).

**Hooks in the landed renderers.** [`review/FamilyTree.tsx`](review/FamilyTree.tsx.md): the orders, the badges and
breakdown, the traversal's data attributes, the triage bar, and the member row's one statement per fact (the change
badge or MIK-L34's note; the name the subject only, the facts described). [`review/familyWalkMerge.ts`](review/familyWalkMerge.ts.md)
unions the facts of an admitted roster continuation. [`review/FamilyReviewCenter.tsx`](review/FamilyReviewCenter.tsx.md):
the family centre's member list follows the tree's order. [`review/ReviewSurface.tsx`](review/ReviewSurface.tsx.md):
the root is the keymap owner's `review` zone. [`review/ReviewWorkspace.tsx`](review/ReviewWorkspace.tsx.md): the
stacked layout's one sticky offset while a marker's way back is open. [`review/MarkerTargetState.tsx`](review/MarkerTargetState.tsx.md):
`useMemberTarget` shared with the badge, and the note's `id`. The data mirror (`data/reviewFamily.ts`) and the keymap
(`data/keymap/`) have their own MIK-L33 sections.

**Rulings** (`33_review-triage-order-and-change-kind-badges.json`). 2026-09-30T15:11:20: start; the `implementation`
fact (b) comes from L32's per-file classification, with no second hunk classifier; built beside L34. 16:22:22 (worker
items 1–11): accepted as built 1 (tree comparisons only), 2 (catalogue rail rows carry no badges), 3 (a family row's
badge is its guarantee fact; its weight includes its members), 4 (pre-curation unknowns follow MIK-R32's exact-blob
rule), 6a (retired counts as removed), 6c (the impl mark beside an intent), 7 (authored order is the record's
`members` list), 8 (unreturned means returned < total), 10 and 11; changed: 5 (one revision with changed text is
`intent`, noted "same revision; text differs", never `unchanged`), 6b (a `file` entry on a changed non-text file
establishes `implementation`), 4 and 9 (every unknown shows its reason; the end status is visible beside the selection
in a sticky bar). 17:47:43 (review R1, changes-required): F1 only the writer's mechanical carry is exempt from
re-anchoring; F2 a breakdown with no total says "(total unknown)" and weighs at least unknown; F3 tests for the eight
surviving mutations; F4 the unresolved-range unknown mark is unconditional; notes: one statement per fact, the centre
follows the tree, the total unknown only for the family's own records, reuse L32's lane helper; the landing order (L34
first) and the merge plan. 18:57:45 (review R2): "re-anchored (stale at base)", the N5/N6 cases, reasons from entries
that established nothing first. 21:41:02: the merge round accepted; a `j` move at 390 px reveals the centre through the
existing `revealCenter`, as a tap does (kept). 21:55:02 (review R3): R3-1 fixed (a member row's name is its subject,
its facts only in its description); R3-2 accepted as notes (two lines for two unknown facts with one cause; the bar
sliding under Back for one step); R3-3 routed to this curation. **Resolved:** MIK-L34's merge Todos on
`review/FamilyTree.tsx` and `review/MarkerTargetState.tsx` (the 17:39:21 merge order), as built.

**Candidate invariants (not ingested; no speculative ingestion):**
1. Change-kind facts are computed on the server, for returned members only, from recorded comparison facts; the hunk
   intersection comes only from MIK-L32's classification, and the client never recomputes it (realized by
   `with_change_kinds` and the entry validator; the client reads `primary`/`marks` and only counts and orders; proved
   by the server tests, the lane reconciliation 2 of 2, and the mutation sets; recorded on
   `application/review_change_kinds.py.md`).
2. Unreadable or partial knowledge produces `unknown` with a stated reason, never `unchanged` or a complete-looking
   total (realized on the server by `_unread`, `_record`, `_entries`, `_unresolved` and a `None` total, and here by
   `occurrenceKind`'s undescribed member and `familyTriage`'s `scoped` "(total unknown)"; proved by the server's
   failure cases, `changeTriage.test.ts` and `FamilyTree.triage.test.tsx`'s SYNTHETIC cases; recorded on
   `application/review_change_kinds.py.md`).
3. Changed intent text is never `unchanged`, even at the same revision (realized by `_intent`'s byte comparison and the
   `text_differs` note; proved by INV-PPPPPP on the server and in the tree, and INV-2E8MG43K on real data; recorded on
   `application/review_change_kinds.py.md`).
4. Triage order never hides unchanged siblings, and traversal never forces unreturned pages to load (realized by
   `orderFamilies`/`orderMemberRows` and `changeTraversal`'s continuation stop; recorded on `review/changeTriage.ts.md`).
5. Each fact is stated once per node, both visually and to assistive technology (realized by `MemberChangeBadge`, the
   replaced side-tag and guarantee labels, and `aria-labelledby`/`aria-describedby`; proved by the tree and surface
   cases, the merge and R3 mutations and the CDP reads at 390 px; recorded on `review/ChangeBadges.tsx.md`).

**Inert before MIK-R37:** only a converted leaf's tree comparison carries `change_kinds`; the worker's preservation
rerun found 29 of 29 unconverted reads identical to base once the null `change_kinds` is dropped (the served body
omits it).

- The rules over the delivered facts; nothing decides a fact. [1]
- The member badge and the tagged membership line; the sticky controls. [2]
- Stops in displayed order and the keymap binding on the reviewer's zone. [3]
- The tree's hooks: facts order the tree and drive the traversal. [4]

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
`aria-describedby` (built by MIK-L33's merge round: see its section above). 18:23:50 (review R2): Back refocuses and re-scrolls after CodeMirror's measure on every layout,
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
knowledge at any memory tree, browsed like a file explorer, needing no task, and opened by the Cockpit as a transient
mode (not full-bleed; a `#knowledge?…` URL opens the Cockpit on it).

- [`knowledge-reader/KnowledgeReader.tsx`](knowledge-reader/KnowledgeReader.tsx.md): the panel. The address is the URL
  hash (`useReaderAddress`), so reload and back keep the view; the toolbar (repository, the memory-tree selector with
  unconverted commits disabled, a record lookup, "without proof [under path]", "census"); the selection banner naming
  the tree, memory revision, code tree and its note, a partial index's problems, and "pin this view to memory …" for a
  clean `published` or leaf tree (ruling N2); refusals named (`not-converted` and the rest); failed side reads named
  beside the toolbar (F11). With no address it lands on the first repository's root summary (F2).
- [`knowledge-reader/KnowledgeTree.tsx`](knowledge-reader/KnowledgeTree.tsx.md): the lazy explorer, one read per opened
  level, entry counts, "(onboarding only)" paths, an unlisted code tree named; an answer after a tree switch is
  dropped (F13).
- [`knowledge-reader/PathViews.tsx`](knowledge-reader/PathViews.tsx.md): the path view (prose, invariants with states,
  families here or routed, linked records with a decision in full), a directory's bounded summary with "list all N
  entries" (F2), the paged subtree with one "more" in flight at a time (the R2 note), the without-proof list, the
  census view and the code view with the resolved lines marked.
- [`knowledge-reader/TruthView.tsx`](knowledge-reader/TruthView.tsx.md): every field, the invariant and family parts,
  a decision in full with the **derived** status in the header (F9), links both ways (unreadable links named, F11/F17),
  and the timeline with each source's state (a source that could not be read named, never "no history").
- [`knowledge-reader/readerParts.tsx`](knowledge-reader/readerParts.tsx.md): every link a navigation (rule 5), state
  badges, `DecisionCard` (the rule carried from L13), and the prose whose `[n]` markers are linked in text nodes only,
  never inside code spans or fences (F4).
- [`knowledge-reader/KnowledgeReader.test.tsx`](knowledge-reader/KnowledgeReader.test.tsx.md) (15 cases) over
  [`knowledge-reader/knowledgeReader.captured.json`](knowledge-reader/knowledgeReader.captured.json.md), 17 real served
  bodies from a converted scratch copy with SCRATCH-AUTHORED routes, decisions, incident, proof, history rows and census.
  A debugging `console.log` that curation found left in one case was removed by a staged, test-only follow-up.

The existing panels are unchanged (the packet's preservation boundary); the Cockpit gained one mode and one hash check.
The data adapter is `data/knowledgeReader.ts`.

- The panel. [20]
- The bounded directory summary and the paged subtree. [21]
- The truth view. [22]
- A decision in full; markers linked in text nodes only. [23]

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
(`pinnedWorklist`, review F11, R2-3), and places the knowledge panel after the evidence;
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

## Current family-centered review ownership

SubjectReview owns central statements and evidence from the exact server-selected subject. Member selection uses the ordinary invariant read while preserving family context; confirmed no-family and ambiguous revision states retain their own truthful rendering.

ReviewSurface composes the reviewer's catalogue (read once on entry since `260921-ICR-L47`) and the existing comparison read cycle. ReviewWorkspace owns one family/subject/source rail and the unified center (its scope header is `ReviewScopeHeader`, and the technical records live in `ReviewRecordPanes` since `260921-ICR-L48`); ReviewExpressions opens actual bound diffs after intent, while familyExpressions owns the existing pure grouping. FamilyTree preserves full statements and unchanged siblings. The complete source inventory remains independent of attribution; diagnostics remain inspectable through disclosure.

**The reviewer stays mounted across subject selection (`260921-ICR-L48`, `ICR-R24@v3`).** Four owners share one rule — *a read is shown only under the question it answers, and a selection changes only the reading area*:

- `ReviewReadCycle` binds every answer to its target key (the surface is handed a read only for the question on screen) and keeps `frame`, the task context's last admitted payload, which a failure or refusal does not clear.
- `ReviewSurface` mounts the workspace over the answer or, while the selected subject is pending, failed or refused, over the frame, with a `reading` status keyed to the requested question and labelled with the requested subject (a failure or refusal carries the owner's R16 block, with retry). Records (`ReviewRecordPanes`) render only for an answer, and `ReviewOutcomeRegion` stays silent when the workspace states the read (one statement per read). Only the first read, which has no frame, is stated at the surface level.
- `ReviewWorkspace` keeps one reading-area column and swaps only its content; its scope header (`ReviewScopeHeader`) replaces the subject-bound comparison, currentness and family lines while unanswered; focus after an answer lands on the selected node only if the reader has not moved it.
- `ReviewReadCache`, one bounded LRU cache per mounted surface (24 whole-subject reviews, 32 content answers), makes a return to a subject or a reopened file cost no request; it keeps only answers, is emptied by any answer from another comparison generation, and a refresh always re-asks. `SourceContent` reads through it by `sourceContentKey`. Cached returns are not a live check (by design).
- `ReviewNavigation.engage`: after the bounded first-read wait, a reader gesture freezes the subject on screen, so a late catalogue only fills the navigation; an idle reader is still landed on the first family, without a remount.

Rapid selections settle on the latest; a superseded answer is neither shown nor kept. `familyWalkMerge` holds the roster-walk merge the read cycle admits (moved unchanged). The mounted evidence is `ReviewSurface.navigation.test.tsx`; the cache's own rules are `ReviewReadCache.test.ts`.

- `ReviewWorkspace` owns the behavior described above; since MIK-L34 it is a thin wrapper that provides the intent markers' scope around the landed body, `WorkspaceBody`. [32]
- `WorkspaceRail` owns the behavior described above. [33]
- The read bound to its question, and the task-context frame. [34]
- The workspace mounted over the answer or the frame, with a subject-bound reading status. [35]
- The reading-area column and its pending/problem statements. [36]
- The bounded per-comparison cache and its generation rule. [37]
- The mounted delayed-reply cases. [38]

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

## 260921-ICR-L25 The Change-Set Bar Names An Unrecorded Range, And The Jump Sits Above The Tree

Two panels on this route changed, and each change is the same shape: **a surface stopped describing a
state it was not in.**

**`detail-panel/changeSetBar.tsx` — an unrecorded change-set range is named, not printed as a zero
(register B6).** A `committed` read of a live leaf has no landed commit to read yet. The route used to
answer that state with a `404`, which the browser logs as a console error on the page whose accepted
criterion is **zero** — and the bar probes that view as soon as a leaf document is opened. The route
now answers it in the body (`state: "unrecorded"` plus its own sentence naming the missing endpoint
and the two views that produce it), and the bar renders it as the control's **own** state
(`data-review-state="unrecorded"`, distinct from `known-empty`) while **withholding the `+0 −0`
total**: a zero of nothing is not a measurement. The three genuinely distinct refusals are untouched —
an unknown leaf is still a `404`, a bad or absent `mode` a `400`, an enclosure `scope` its own `404`.

**`review/ReviewWorkspace.tsx` and `review/FamilyReviewCenter.tsx` — the narrow-screen route moved
above the tree, and the empty column names its own plane (register B3).** The accepted design's finding
P2-3 puts the "jump to the selected review" affordance **near the top** precisely because the family
tree's height is why it exists; rendered immediately before the centre column instead, it sat at
`y=1183` in a 900 px viewport — reachable only after the scroll it exists to avoid. It is now one
`NarrowJump` mounted between the header and the tree, and the tree itself is unchanged. The centre's
empty sentence used to read "No family or member is selected", which collided with the **server's** own
"selected" on the same screen (the header's composed-context count, the tree's "this review selected
<revision>", a roster line's "the page is the whole selection"), so a reader comparing them read a
contradiction that was a collision of vocabularies; it now says a family or member has not been
**chosen in this column** yet and states that the header's composition and the tree's revision selection
are not choices made here. **The sentence was not false about its own state** — the measured
`data-selection-kind` is `none`, with no `aria-current` in the tree, until the reader chooses — so this
is a wording fix and the layout of the centre was deliberately not changed. **One caveat the round-2
verifier measured, and round 3 then removed (its F2):** at 320 px the reviewer had supplied no scrollport
of its own, so with `MAIN` at `overflow-y: hidden` its 7 620 px of content were reachable only by
programmatic focus scroll — the narrow reader's route to the review was not one they could scroll. That
is fixed on the reviewer's own side (`ReviewSurface.tsx`'s root is now the scrollport, `userScrollableCount`
0 → 1); the composition requirement and the wording fix are unchanged by it.

**Two further lines of the same accepted design were addressed on this route, and the second one is
only half fixed — stated here as the independent verifier measured it.** `review/FamilyTree.tsx`
carried the review surface's **only** raw colour literals (`oklch(0.82 0.16 75 / 0.08)` and
`… / 0.16` — `--amber`'s channels copied by hand); both are now one `AMBER_WASH(percent)` helper
stating `color-mix(in oklab, var(--amber) N%, transparent)`, because an `oklch` mix interpolates the
**hue** and that is how the accepted page's own row first came out visibly teal (register B1).
**The form of that claim which is true, and the form which is not:** the raw amber-wash literal is
gone, the wash computes as `oklab` through `var(--amber)`, and hue 215 is absent — but "zero `oklch`
users remain in the review surface" is **false as worded**, because `getComputedStyle` resolves
`var(--token)` and this dashboard's tokens are themselves defined in `oklch`
(`styles/tokens.css:8-23`), so token-resolved `oklch` values are everywhere in the surface by design.
A reader scanning computed styles for the word `oklch` will conclude the fix failed unless this is
said. `review/SourceExplorer.tsx`'s path button gained `overflow-wrap: anywhere` and
`max-width: 100%`, which is what lets the column shrink: measured at 320 px, one
`review-inventory-open` button was 556 px wide inside a 294 px column with its right 262 px neither
visible nor reachable, and it now wraps inside its container (register B7).

**B7 needed a second round, and the two readings of its residual are both worth keeping.** Round 2
claimed the residual was *"the cockpit's own status bar, outside the review surface"*; that was
**false as worded** — the count had been classified against the **inner**
`[data-testid="review-workspace"]` root (`ReviewWorkspace.tsx:515`) while the Intent Reviewer's own
root is `[data-testid="review-surface"]` (`ReviewSurface.tsx:906`, mounted by `Cockpit.tsx:585`).
Against the reviewer's own root, **51 of the 64** elements past the right edge at 320 px were **inside**
the reviewer (13 were cockpit chrome), the pane sections were **565 px wide in a 294 px column** with
`pannableCount 0`, and the vertical half was worse: **nothing in the document was user-scrollable**,
because `MAIN` is `overflow-y: hidden` carrying 7 620 px in a 706 px box. **Round 3 fixed both halves in
the reviewer's own code** (`ReviewSurface.tsx`): the panes got `min-width: 0` +
`overflow-wrap: anywhere`, the disclosure track became `minmax(0, 1fr)`, the header row wraps, and the
surface root took `height: 100%` / `minHeight: 0` / `overflowY: auto`. Re-measured: descendants of
`review-surface` past the edge **51 → 0**, total **64 → 13**, panes **565 → 294 px** in a 294 px column,
the root's own **311/294 → 294/294**, `userScrollableCount` **0 → 1**, and a wheel over the review moves
the surface **0 → 800 px**. **The number was not improved by changing the root** — the inner root's
count was 0 in both rounds, which is precisely why F1 was a classification defect. **What remains
routed, and it is the shell's rather than the reviewer's:** `MAIN`'s deliberate `overflow: hidden`
(`cockpit/Cockpit.tsx:323`, *"the viewport does not scroll — its panel scrolls on its own"*, shared by
every view) and the **13** cockpit-chrome elements, owned by R24's cockpit takeover.

## Hot Path Summary

Task detail prose, `TaskNotes.tsx`, and the shared notes reader use `TaskArtifactReaderTarget` for notes or registered requirement packets. `detail-panel/taskReader.tsx` mounts the requirement-link context; `notes-reader/NotesReaderViewer.tsx` owns the kind-aware content transport and takeover.

## Governing Overview

[dashboard/src overview](../overview.md)

## Current Structural Panel Contract

Panels receive real task-document hierarchy and current occupant facts from the data route. RailChat
and the session cockpit select structural document+role seats; task assignment posts that identity,
and replacement changes only the occupant. No panel derives hierarchy from spawn ancestry or treats
a lifecycle/session id as the task address.

## 260713-TES-L5F2 Change

The shared `SessionComposer` and contextual `RailChat` regression suites now prove that composer
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
- RailChat.tsx — contextual task-side chat, not a second full-page chat product.
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
shows a failed create before readiness or submit and sends no selected context. `RailChat.tsx`
shows the same typed failure and withholds contextual delivery. Both consume the accepted-row result
from the data route; neither writes a private row, focuses a requested id, or retries through paste.

## Route Model

### Canonical Chats

FEUI-L8 retires the legacy Chats.tsx and SessionList.tsx path. CockpitShell now exposes one
Chats destination backed by the persistent session-cockpit layer; Operations remains the default.
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
  choice cannot move active route/focus on rejection or ambiguity. Its pre-projection task-document
  fallback is a stable module-level snapshot, so the always-mounted composer cannot force React into
  an external-store update loop while analytics is still absent.
- RailChat.tsx renders contextual task-side chat under the same registry, not a competing destination.

### Operations And Other Routes

Operations, Detail, Engine Room, notes reader, file viewer, changeset, and lifecycle-design retain
their existing responsibilities. Focused child overviews and one-to-one file cards are authoritative;
the Chats refactor does not move those routes.

## Invariants And Boundaries

- Exactly one full-page Chats destination; no legacy Chats layer and no Sessions navigation item.
- Operations is initial. The Chats inspector is supplementary, default closed, and toggleable.
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
| Review child route — the mounted family composition cases | [ReviewWorkspace.family.test.tsx](review/ReviewWorkspace.family.test.tsx.md) |
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
- `CockpitShell` defaults `initialView="operations"`. [47]
- The terminal panel owns the shared terminal surface. [48]
- The shared composer surface is implemented by `SessionComposer`. [49]
- Selection-send behavior builds context and submits it to a selected or routed target, committing only on accepted or queued delivery. [50]
- Contextual task-side chat builds a leaf context package and resolves the current occupant from structural task identity. [51]
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

**What the fixture conversion does and does not pin.** `EventRiver.test.tsx`, `RailChat.test.tsx` and
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
offered for every leaf — and the subject read left the entry entirely in `260921-ICR-L47`; see the L47
section at the end of this overview.)*

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

## 260921-ICR-L3 The Source Pane's Entries Open Into The Content Of Both Bound Code Trees

**Route meaning changed, narrowly: the Source pane stopped being display-only about *what* changed and
became the way into *the bytes*.** A listed inventory entry is now openable, and opening it reads the
file at the two code trees the inventory published and renders both endpoints' actual content in place.
That is ICR-R03's rendering half, and it is the defect the route had been carrying: an inventory row
labelled as an expansion showed a path, a status and a reproducing command, and **no bytes at all**, so
a reader had to leave the surface and run the command to learn what had changed.

`panels/review/SourceContent.tsx` is the new renderer (222 lines), a third component in the child route,
and `panels/review/ReviewSurface.tsx` grew 462 → **549 lines** to reach it:

- **`inventoryEntry` renders the published path as a button** — `data-testid="review-inventory-open"`,
  `data-path` carrying the path exactly as the server published it, `aria-expanded` carrying the open
  state — **only when the inventory named both of its code trees**; the same click closes the row. An
  inventory that named no pair has nothing to open, so it renders the path as text and no control.
- **`Inventory` holds the one piece of state this route's rendering now has** — `const [open, setOpen] =
  useState<string | null>(null)`, addressed by the published path — and derives the generation pair from
  its own `before_code_tree_id`/`after_code_tree_id`, which `inventoryEntry` then mounts `SourceContent`
  with. The two ids are the listing's, so a row opened after the branch moved still shows the generation
  the reader was looking at.
- **`SourcePane` forwards the task context** (`repo`/`master`/`leaf`) into `Inventory`, which is how the
  expansion request carries the same target the root's `data-review-target` stamps.
- **`byteNamedEntry` gained the explicit non-addressability note** (`data-testid=
  "review-byte-path-not-addressable"`): the byte-form row is listed by its exact bytes and carries **no**
  expansion control, because no request this text-carrying vocabulary can spell would address it. The
  pane states that rather than implying a click would open something.

**What the new renderer decides, and what it deliberately does not.** Every branch is decided by each
side's declared `state` and never by inspecting its text: both sides `present` → the shipped `DiffPane`
in split mode over the two files' own bytes; one side textual (a regular file's text, or a symlink's
recorded target) → that side drawn as content with the other side's own reason beside it, plus an
explicit `review-source-no-diff-claimed` line, because a diff there would claim the opposite endpoint is
a known-empty document; neither side textual → the two state lines alone. The state line carries the
declared state, the measured object identity and the byte count, and adds the long detail only when the
state is not a complete untruncated text. A bounded read is stated as a prefix of the object
(`review-source-truncated`), `currentness` says whether the listed generation is still the leaf's, the
leaf-change-set bound is stated only when that is what admitted the path, and a typed refusal renders
with its code, detail, next action and offending input and **no content** — a refusal is a normal answer
from this route, not a degraded success. `DiffPane` (from the change-set route) and `FilePane` (from the
file-viewer route) are reused rather than a third viewer being grown, and the module's header records
both, so the surface now names **two** reused renderers instead of one.

**`data/review.ts` grew 320 → 414 lines** and gained the expansion's wire types
(`ReviewSourceSideState`, `ReviewSourceSide`, `ReviewSourceExpansion`, `ReviewSourceContentResult`) and
`reviewSourceContent(...)`, which reads the typed refusal body **whatever the HTTP status** and throws
`FilesApiError` only for a body that is not this route's answer — the one function in that client that
deliberately does not go through `getJson`, because on this route a typed refusal arrives with a 400/404
status. `intentReview` and `intentReviewEntries` are unchanged.

The panel inventory is otherwise unchanged: no new route, no new takeover, no change to the reviewer
dispatch or its target shape, and no other panel touched. The server half of this contract — the
source-content route and the model the expansion mirrors — is recorded by the `mcp/` route's onboarding,
not here.

- Inventory rows preserve path/status and control state; optional inline content expansion uses the listed tree pair. [65]
- Byte-named paths remain listed and explicitly cannot be addressed by this text request vocabulary. [66]
- Inventory rows receive their expansion state from the workspace and bind expansion to the inventory tree IDs. [67]
- The source pane, which since `260921-ICR-L24` points at the explorer, and the explorer mount that forwards the task context an expansion request carries (the pane moved to `ReviewRecordPanes.tsx` in L48). [68]
- The central statement applies the 13:40 wording rule through the subject renderer (MIK-L31), and a dataset review's source expressions delegate to bound source content. [69]
- Source operands are rendered from their declared states; unavailable content does not become an invented diff operand. [70]
- The expansion states bounded content and the admitted path relation alongside the actual source rendering. [71]
- **The typed refusal rendered with its code, detail, next action and offending input, and with no content.** [72]
- **The client's expansion wire types and the request that reads the typed body whatever the status.** [73]
- **The cases that measure the whole route at the real surface over a stubbed transport: the addition, the two-sided modification, the binary/symlink/submodule sides, the superseded generation, the bounded prefix, the typed refusal, the exact request, the leaf-change-set bound, the byte-form row and the inventory with no pair.** [74]

## 260921-ICR-L6 The Review Panel's Statement Area Gets Its Own Component

The **review child route gained its second component**, and the route-level fact is that the Intent
Reviewer's pane 1 no longer decides its own statement rendering inline.
`dashboard/src/panels/review/KnowledgeStatements.tsx` owns the statement area — the two recorded
operands and the state of each side — and `ReviewSurface.tsx` delegates it (476 → **462 lines**, with
the `sideState` helper and the `DiffPane` import gone from that file).

**The rule the component implements is ICR-R06's, and the defect it closes is worth stating at this
altitude because no gate caught it.** The pane used to draw the shipped `DiffPane` only when *both*
statement sides were `present`, while the side line returned `null` for the side that *was* present —
so an added or a removed statement rendered as two muted state lines and **no statement text at all**.
The four branches now decided from a side's declared `state`, never from its text:

- both `present` → the shipped two-sided diff, unchanged (and, as before, naming no side);
- one `present`, the other `absent` → a **one-sided diff** with the present operand on its own side and
  the absent side named above it, so the empty half is a stated fact rather than a blank to interpret;
- one `present`, the other `binary`/`unresolved` → the available text as content with the unavailable
  side's own reason beside it, an explicit "no diff is drawn" line, and **no diff** — a diff there
  would claim the opposite operand is a known-empty document;
- neither `present` → both sides' own state lines and no diff and no content pane.

**The route's other half of the same rule is a mechanical field row.** `ReviewSurface.tsx` gained
`fieldValue`, which prints `(absent)` for a value the server did not send and `(recorded empty)` for a
value that is present and empty, so no field row is silently blank and no reader has to decide which of
the two a gap meant — the display counterpart of the data contract
`application/review_statement_sides.py` owns. The panel inventory is otherwise unchanged: no new
route, no takeover change, and the child's file cards are the authority for the rest.

- **The child route's statement-area component: the four branches, the one-sided diff, and the available-content path that claims no addition or removal.** [75]
- **The state line rendered for every non-two-sided area, carrying each side's own token in `data-side-state`.** [76]
- The technical knowledge pane delegates statement rendering to KnowledgeStatements. [77]
- **The field-row words this leaf added: absent and recorded-empty as two different facts.** [78]
- The technical knowledge pane delegates statement rendering to KnowledgeStatements. [79]
- **The renderer case that fails against the pre-fix pane: an added invariant's full after statement read out of the rendered diff DOM beside an absent-before label.** [80]
- The cases for the removal, the unreadable opposite, and the three declared non-present states as their own tokens. [81]

## 260915-KS-L22 The Review Panel Route And Its Three-Pane Surface

The L22 section below records the panel itself — the three panes, their prohibitions and the
display-only submission boundary — and remains current. What it did not record is a way to *reach* the
panel on a live leaf; the section above supplies that, and supersedes nothing below it.

`panels/review/` is this route's new child, and its entry component is `ReviewSurface.tsx`, mounted by
the cockpit takeover when a change-set target carries the review variant. It renders the Intent
Reviewer's three panes in one scrolling column — Knowledge, Source, Evidence and assessment — in the
order the payload declares them, and it is display-only: the module has no control that writes
anything, no submission button, and no place a conclusion of its own could be assembled. The one
renderer it reuses is the change-set route's `DiffPane`, reached through the statement area
`KnowledgeStatements.tsx` owns and fed the statements the comparison published: **both operands when
both sides recorded one, and the available operand beside the named absence when one side did not**
(the `260921-ICR-L6` section above records that rule and supersedes the "only when both sides are
`present`" reading this section was written with); a side that is `absent`, `binary` or `unresolved`
renders as its own named state rather than as an empty diff, and neither the statement area nor this
file declares a second differ.

The prohibitions are rendered, not merely intended. Authored effects, preservation claims and
unresolved questions are listed under their own heading and detection signals under a second one,
because the payload keeps those two collections apart by element type; a selected path with no
registered attribution is reported outside any claim instead of being folded into one; a count the
comparison could not measure prints as not measured with its stated reason rather than as a zero;
and both lists that could show an assessment print `UNASSESSED — no assessment is recorded against
this subject.` when the collection is empty, so no pane has a favourable default to fall into.

Failure is a state on this surface too. A typed refusal is rendered with its code, its detail, the
offending input and the next action, and a transport error is its own line; neither is a degraded
success, because a refused review shows no panes at all. The submission block states the increment's
own boundary in the same voice: submission is not offered (or disabled, for a stale comparison) with
the reason and a next action naming the existing curator authority, and the three dispositions it
prints are labelled as that authority's vocabulary — none of them publication approval. Every
rendered state carries a `data-testid`, which is how the surface's cases read each pane back.

- The child route entry component. [82]
- Pane 1, and the two collections it keeps apart — **and, since `260921-ICR-L6`, the statement area it delegates.** [83]
- Pane 2, the selected locations and what the selection did not reach — **and, since `260921-ICR-L3`, the pane whose listed entries open into their own content** (since MIK-L32 it also takes the lane read, for a tree comparison's attribution). [84]
- Pane 3, evidence and assessment with both absence states stated. [85]
- The technical panes print the owner assessment state rather than deriving a favorable judgment. [86]
- The block that states the display-only submission boundary. [87]
- The refusal rendering, which left the surface for the outcome owner: one block prints every field the owner published, and both the surface and the expansion pane render it. [88]
- **The one renderer this child reuses, fed both operands when both sides recorded one and the available operand beside a named absence when one side did not — reached through the statement area `260921-ICR-L6` gave its own component.** [89]

## 260921-ICR-L2 The Review Panel Renders The Whole-Task Inventory

**Route meaning changed: the review panel can render a review that compared nothing, and its source pane
now opens with the complete change inventory.** `panels/review/ReviewSurface.tsx`: `ReviewTarget`'s two
selector fields became optional and the header prints `whole task (no subject selected)`; the Knowledge
pane prints the comparison identity when there is one and `no knowledge comparison was made` with the
server's own selection detail when there is not; and three render helpers were added — `Inventory` (all
three inventory states, never an empty list, with the count, the byte-form count, the server's own reason
and the reproducing command), `inventoryEntry` (the path exactly as published, with its status and its
renderability) and `byteNamedEntry` (a name this surface cannot carry as text, printed by its exact byte
form with the stated reason). `panels/detail-panel/changeSetBar.tsx` offers the entry for every live
leaf, and `panels/detail-panel/test-utils.tsx` answers the entry read with whatever answer a case wants
to exercise. `260921-ICR-L3` (recorded above) then changed what those three helpers do to a row: the
listing now opens into each entry's content, `Inventory` holds which row is open, and `byteNamedEntry`
states that its byte-form row cannot be opened — so the measurements below name this candidate's lines.

- **The target whose selectors are optional, and the header line that names the whole task when there is none.** [90]
- **The inventory rendering: all three states, the count, the byte-form rows and the reproducing command.** [91]
- **The source pane that opens with the inventory, and the knowledge pane's selection line that survives an absent comparison identity — a pane that since `260921-ICR-L6` also delegates its statement area and since `260921-ICR-L3` opens each listed entry into its own content.** Ranges re-derived against this candidate. [92]
- **The detail-panel entry that is offered for every live leaf, with the server's subject catalogue as a refinement.** [93]
- The fixture that answers the entry read with a subject, an empty list or a refusal. [94]
- The three cases those three answers are measured by. [95]

## 260921-ICR-L16 The Review Surface Gets Its Outcome Owner, And The Entry Shows Its Own Answer

This leaf gives the Intent Reviewer's **non-payload states** one owner and makes the refusal reach the
reader on three surfaces.

**The outcome owner is new.** `panels/review/ReviewOutcome.tsx` (251 lines) owns the read's four phases
(`loading` | `reviewed` | `refused` | `failed`), the known-empty note, and **one** `ReviewProblemBlock`
that prints every field the owner published — code, reason, the offending input it named and the
next action it published, with an explicit sentence where the server published none. It renders a retry
**only** for `network`, the one token with no owner-published recovery route, and offers the task's source
change inventory only for a refusal that answers for the intent half alone. `ReviewSurface.tsx`'s inline
`RefusalBlock` and its generic `review-error` paragraph were **removed, not duplicated** (549 → 632 lines);
the surface is now the composition: it loads, keeps the last coherent payload, and renders the panes.

**The retained generation is keyed to the question it was read for.** `targetKeyOf` is the one identity a
read answers for — the task context **and** the question asked — and both the reset in `load` and the
render-time check read it, so a payload is never shown under a header it was not read for. A **failed**
read keeps the last coherent comparison on screen, labelled, and claims no empty review for it; a
**typed refusal** replaces the panes, because it is the owner's answer about the leaf's current state.

**The entry bar carries the entry read's own answer.** `changeSetBar.tsx` (186 → 280 lines) returns a
`ReviewSubjectRead` — `loading`, the first recorded subject, a known-empty flag, or the read's own
`ReviewFailure` — and `ReviewEntryState` prints it beside the entry in the owner's own words. The entry
itself is offered for every live leaf and still opens the task-context review on `review: {}`, so a
refusal here is a stated reason rather than a missing control.

**R03's expansion pane renders transported failures through the same block.** `SourceContent.tsx`
(222 → 241) keeps its own typed-refusal block untouched and routes everything else — an unwired process,
an unadmitted query, a socket that never answered — through the shared `ReviewProblemBlock`, so the 503
that used to read `503 unavailable` now carries the adapter's own instruction; the retry re-arms the read
through an `attempt` counter.

Two measured limits are recorded as **routed, not fixed**: an **in-flight** prop/question change can still
let an earlier read settle under a newer header (pre-existing at HEAD and on the round-1 bytes —
**R17**, with R24 for the interaction side; the retained-generation guarantee holds for every *settled*
change), and the **browser-class A01/A13 journeys** over a served dashboard are not verified by this leaf
(**R25**, with R24/R17).

- **The one place the non-payload states are decided, where the known-empty statement and the retained-generation label are mutually exclusive.** [96]
- **The one failure renderer, with the retry gated on `network` and the inventory offer gated on an intent-only refusal.** [97]
- The read key names the actual question, and retention is shown only for that same question. [98]
- **The entry's own read state on a control that never disappears — since `260921-ICR-L47` a brief word from the changed-intent summary read, with the owner's explanation in a disclosure (the catalogue-based `ReviewEntryState` recorded above is gone).** [99]
- The source pane keeps shared transport failure rendering separate from the source owner typed refusal. [100]

## 260921-ICR-L10 The Page Control, And The Captured Body That Proves The Refusal Actually Reaches It

`260921-ICR-L10` (`ICR-R10@v1`) adds the reachable next page to this route's review surface. The surface
used to render a remainder with no control that reached the rest of the collection — the packet's own
non-conforming example — and it now renders the bounds, the scope and one action that advances the walk
with the cursor **the server published**, plus a first-page action when a cursor was refused.

The control is four small pieces over the page the client already carries (`PageControls`, `PagePicker`,
`PageActions`, `PageBoundsLine`) and a refusal block (`PageRefusalBlock`) that states the code, the
owner's two identities and a live first page of the collection that was asked for. The page is part of
the read's target key, so a page change is its own read rather than a re-render over the wrong payload.
No next action is offered for a body that published no cursor, whatever remainder it reported — a button
that fetches nothing is the defect this control exists to prevent.

**Two files on this route are new, and both are about proof rather than behavior.**
`ReviewSurface.paging.test.tsx` drives the real component over the real client with only `fetch` stubbed,
and `recordsPageRefusal.captured.ts` is the raw body of a real refused records page, exported verbatim
with a provenance header. The capture exists because the route omits the `page` key rather than sending
`null`: the mounted case asserts that absence before rendering the bytes, so the case cannot pass against
a body the route would never send.

Keyboard and focus traversal of the control, and the finished cockpit interaction, remain `ICR-R24@v1`'s;
the assembled acceptance remains `ICR-R25@v1`'s. This leaf records the boundary rather than claiming
either.

## 260921-ICR-L26 The Review Surface Mounts The Attribution On Both Panes

`260921-ICR-L26` (`ICR-R26@v1`) mounts the server's attribution facts on both review panes through three
renderers and no new component state: `ReviewSurface.tsx` (879 → 946 lines) gained `applicabilityNote`
(one record's treatment, the true subject its binding names, and the server's own detail — printed
**nothing** when the payload carries no label), `contextList` (the labelled context rows with the
relationship that reached each one, the record's kind and its references) and `applicabilityCounts` (the
six-way partition beside the collections it filtered). All three read the fields the server sent and
none derives a treatment, a relationship or a total.

**One record, one treatment, two panes.** `applicabilityNote` is called on the knowledge pane's
assessments, authored effects and signals **and** on the evidence pane's evidence links and
observations, and the context list and the counts block are mounted on both panes, so the same record
cannot read one way in one pane and another way in the other. A context row never renders the sibling's
finding: the row carries the record's kind, and that is the whole point of the value.

**The route gained one case module.** `ReviewSurface.applicability.test.tsx` (311 L, four mounted cases
over the real component and the real client with only `fetch` stubbed) asserts the treatment and the
true subject of a labelled context row, the absence of the sibling's finding from the document, the
six-way counts rendered as arithmetic, the historical label with the tree it examined, and that a
payload published **before** the vocabulary still renders. Browser and keyboard traversal remain
`ICR-R24@v1`'s, and the assembled A14/A15 acceptance remains `ICR-R25@v1`'s.

## 260921-ICR-L12 A Closed Leaf Keeps Its Intent Review, Bound To Its Record

`260921-ICR-L12` (`ICR-R12@v1`) changes what liveness means to the change-set bar and what the
review surface says about the record it is reading:

- **the Intent review entry is offered for every leaf.** It used to be gated on the enclosure being
  live, which is the intake defect's browser face — a cleaned leaf's worktree is gone and the review the
  packet exists to make openable could not be reached. `live` now selects **which record** the entry is
  addressed to (the live candidate, or the leaf's recorded comparison as `historical: true`, labelled
  "Intent review (recorded)") and it is not a gate. The **working** change-set stays live-gated, because
  "what is not committed yet" genuinely does not exist once the enclosure is closed, and the catalogue
  read is no longer live-gated either — it remains a refinement and never a gate, so a refusal beside
  the entry is a stated reason rather than a missing control.
- **the mounted surface states which record the panes are read from.** `history` joined the review
  target and the **target key** (`repo/master/leaf/<history ?? "live">/<question>/<position>`), so a
  response read for one record is never applied to a surface that asked for another; `ReviewHeader`
  mounts the provenance line and the root publishes `data-review-history`. The two extractions
  (`ReviewHeader`, `ReviewPanes`) cleared the surface's `max-lines-per-function` rail with no ignore
  added and no limit widened.
- **the new client case module** `ReviewSurface.history.test.tsx` pins both directions of the pair over
  the real component and the real client, stubbing only `fetch`: the recorded read asks for the record
  it was handed and says so, and the live read asks for none and claims none.

**Boundaries recorded, not closed.** `ICR-R24@v1` owns the leaf-history drill-down navigation — this
leaf provides the addressable target and adds no navigation — and `ICR-R25@v1` owns the assembled
browser acceptance; these cases are mounted components over the real client, not a real-browser run.

## 260921-ICR-L17 The Read Cycle And The Refresh Control Leave The Review Surface

`260921-ICR-L17` (`ICR-R17@v1`) adds **two components to the `panels/review/` child route** and rewrites
one read at the detail-panel entry. No route, takeover dispatch or target shape changed.

- [`panels/review/ReviewReadCycle.ts`](../panels/review/ReviewReadCycle.ts.md) owns the review surface's
  read cycle: the question's identity (`targetKeyOf`), one in-flight read per question with the newest
  read winning, the retained generation, and the reader's refresh as the single read that may carry the
  identity on screen. It exists because `ReviewSurface.tsx` is over the file-size rail and the component
  was over the per-function rail.
- [`panels/review/ReviewRefresh.tsx`](../panels/review/ReviewRefresh.tsx.md) owns the explicit refresh
  control and the one sentence that answers it. Its derivation renders **no claim** unless the read that
  carried the identity has answered, and the `superseded` sentence names both digests and says which one
  the panes below hold.
- `panels/review/ReviewSurface.tsx` is **462 lines of read logic and rendering lighter** and now wires
  the hook, the header's `refresh` node and the three regions.
- `panels/detail-panel/changeSetBar.tsx` gains the store-projection invalidation signal
  (`reviewDependencyFacts`), an always-offered refresh control (`ReviewCatalogueRefresh`) whose mark is
  derived from the facts recorded with the last answer, and the pure `catalogueAnswer` mapping.
  *(Superseded by `260921-ICR-L47`: the signal and the control are removed; see that section below.)*
- `data/review.ts` gains the ninth `intentReview` argument, the `reviewQuery` assembler and the single
  `PREVIOUS_BINDING_QUERY` spelling of the wire name.

**What a route reader should carry away.** The carried identity is `{readNumber, key, digest}` and it is
both **sent** and **described** only when the read number and the question key agree, so the identity a
notice describes is exactly the identity the request carried — a different subject, a different leaf, a
recorded read, and a later read of the same question all carry nothing.

## 260921-ICR-L24 The Family Reading Path And The Source Explorer

**Route meaning changed: the review child route gained the accepted family-centred composition, and the
surface became a composition of owners rather than the owner of everything.** Five modules are new in
`panels/review/`, and each one owns exactly what its neighbours must not:

- [`FamilyTree.tsx`](review/FamilyTree.tsx.md) — a recorded family is the semantic parent of the review
  population: the family label, then the family revision's own independently authored joint guarantee
  printed whole, then the complete member statements of the roster the page carried **including the
  unchanged siblings**. It is one roving-focus group with arrow-key traversal and `aria-current` on the
  current node, and it carries the route's **one** family-roster walk control (`RosterNext`), which
  continues the walk at the cursor the family's own roster page published.
- [`FamilyReviewCenter.tsx`](review/FamilyReviewCenter.tsx.md) — the unified central reading path: for a
  **member** selection the family guarantee and the selected intent first, then the linked expressions, then
  the recorded execution evidence and the authored assessment; for a **family** selection the guarantee,
  then the complete recorded member context, then the family's deduplicated changed expression excerpts
  (**added by 260921-ICR-L36**, below) — in one column, so a reviewer never has to reconstruct the route by
  switching tabs or opening a detached inspector. This bullet read as one route for the whole column until
  L36; the two selection shapes are two different orders and both are complete.
- [`ReviewWorkspace.tsx`](review/ReviewWorkspace.tsx.md) — which family or member is selected, the
  reader's display preferences (diff layout, full-file disclosure, the expanded path) and the
  narrow-screen route from the tree to the selected review. `useWorkspaceState()` is called once, by the
  surface **above** `ReviewPanes`, because that switch returns `null` while a page read is in flight: a
  page request can no longer reset the reader's selection or display choices.
- [`SourceExplorer.tsx`](review/SourceExplorer.tsx.md) — the complete source change explorer, moved out
  of `ReviewSurface.tsx` whole: every changed path of the comparison's bound pair, openable at the
  generation the listing named, with the inventory's three states, the byte-form rows and the reproducing
  command. The family navigation is an attribution lens over it and never an exclusion filter.
- [`ReviewWorkspace.family.test.tsx`](review/ReviewWorkspace.family.test.tsx.md) — the case module that
  drives the real surface over the real client with only `fetch` stubbed, against the seven
  `familyReview.*.captured.json` bodies the server published.

**`ReviewSurface.tsx` no longer owns the inventory.** It mounts the workspace and keeps the three
diagnostic panes — knowledge, source, evidence and assessment — inside one `<details>` disclosure, so
their content, controls, refusals and technical identities are unchanged and still in the DOM and the
keyboard's reach, reached deliberately instead of being the first thing a reviewer reads past. Its
`ReviewPanes` switch takes the workspace as a prop for the reason above, and the surface calls
`useWorkspaceState()` itself. `ReviewReadCycle.ts`'s `ReviewPageRequest.of` is typed as the server's own
`ReviewPagedCollection` rather than a narrowed copy, because a request naming `family_members` must be
representable for a truncated family roster to be continued.

- The family hierarchy shows authored guarantees and member statements with full sibling context and keyboard traversal; on a tree comparison it also badges, orders and traverses the changes without hiding a sibling (MIK-L33). [101]
- **The one family-roster walk control, continuing at the cursor the roster page published; since MIK-L33 it names its family for the traversal's partial-family message.** [102]
- **The unified central reading path, in one column and in the packet's order; since MIK-L31 the expressions slot holds the focused cards for a tree comparison.** [103]
- **The workspace's selection, preferences and narrow-screen route, and the one hook owned above the pane switch.** [104]
- **The complete source change explorer, and why it is its own module rather than part of the surface.** [105]
- **The mounted family composition cases and the captured server bodies they are driven with.** [106]
- The surface mounts the workspace and retains technical records/paging panes in a disclosure (rendered by `ReviewRecordPanes.tsx` since L48, only for an answer); state is held above the read cycle. [107]
- **The page request whose `of` is the server's own collection union.** [108]

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

The existing ReviewReadCycle retains exact member content and source claims only within an admitted same-comparison, same-subject family-side-revision continuation. Rejected continuations state failure beside the retained coherent display; refresh and subject/history changes remain replacement reads. FamilyTree, FamilyReviewCenter and ReviewExpressions distinguish loaded context from raw item counts and partial/unavailable source scope. Source inventory, primary statement and evidence remain their existing owners' facts. The captured-page regression fixture and mounted read-cycle cases document this boundary.

## 260921-ICR-L47 The Task Entry Is One Compact Intent Review Control; The Reviewer Owns Its Catalogue

`260921-ICR-L47` (`ICR-R24@v3`) changes both child routes that meet at the review entry. **It
supersedes** the entry-side catalogue design recorded above in the KS-L45, L9, L16 and L17 sections.

**`detail-panel/` — the entry.**

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

**`review/` — the reviewer.**

- The reviewer reads the catalogue **once when it opens**, keyed on the comparison
  (`repo/master/leaf/history` plus a generation that moves only when the displayed snapshot pair
  changes), not on the analytics document (`review/ReviewNavigation.tsx`, `data/useReviewCatalogue.ts`).
- Its first review read is **held** until the catalogue chooses a subject, so a prompt catalogue costs
  one subject read instead of a whole-task read and then a subject read. The hold is **bounded**
  (`SUBJECT_HOLD_MS = 750`, L47-R1-F1): a slow or stalled catalogue releases into the task-context review
  and source explorer, and the first subject is selected when the catalogue answers.
- The reviewer's own "Refresh subjects"/refresh control is kept, and its refresh also re-validates the
  entry's summary.

**Known, routed, not delivered here.** A catalogue that answers after the bound moves the reader to the
first family and drops keyboard focus (review R2 observation O-R2-1; the remount is owned by L48).
`ReviewSurface.tsx` is 931 lines, over the 900-line soft rail (L47-R1-F5, routed to L48).
**Both were delivered by `260921-ICR-L48`** (see *Current family-centered review ownership* above): a late
catalogue no longer moves an engaged reader and never remounts, and `ReviewSurface.tsx` is 585 lines.

- The compact control, its brief states and its disclosure (since MIK-L32 with the lane's count beside `+N −N`). [115]
- The entry mounted in place of a change-set button. [116]
- The leaf-scoped facts and re-validation generation. [117]
- The reviewer's comparison-keyed catalogue, bounded hold and snapshot observation. [118]
- The first read held while the navigation settles. [119]
