# dashboard/src/panels/review/ReviewSurface.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Compose the normal Intent Reviewer from one subject catalogue, one comparison read cycle and a family-centered workspace. The surface is read-only and produces no semantic judgment. Since `260921-ICR-L48` (`ICR-R24@v3`) it also decides **which payload the workspace is mounted over**: the answer for the subject on screen, or — while that subject is pending, failed or refused — the task context's last admitted `frame`, so a selection never unmounts the workspace, its navigation or its open disclosures.

## Code Commentary

### Logic

The subject-selection callback carries the chosen family context into the new subject read. Selecting a member requests its invariant through the existing read cycle; it does not render a family payload as that member own assessment.

useSurface gets recorded subjects through useReviewNavigation and passes the chosen identity to useReviewReadCycle. Changing subjects (`selectSubject`) records the element that had focus (`focusSelection = { from }`), clears the prior page request and local family selection while the workspace display preferences persist. The retained payload is shown only when its full target key matches the question on screen. ReviewPanes mounts one workspace; records, pagination, submission contract and complete technical panes remain inspectable in the technical-details disclosure, whose renderers moved to `ReviewRecordPanes.tsx` (`ReviewTechnicalDetails`) in L48. Typed outcomes stay with ReviewOutcome, refresh identity with ReviewRefresh, source bytes with SourceContent, and family/intent/source composition with ReviewWorkspace.

**The mounted shell (L48).** `useSurface` owns one `ReviewReadCache` per mounted surface (`useState(() => new ReviewReadCache())`), passes it to the read cycle and provides it to source content through `ReviewReadCacheContext`. It computes `reading` with `readingStatusOf` only when a `frame` exists and no payload answers the question on screen: the status is keyed to the read cycle's target key, names the requested subject (`kind:id`, labelled from the catalogue entry when there is one) and, for a failed or refused read, carries the owner's `ReviewProblemBlock` labelled with that subject (retry for a transport failure, the source-changes offer for an intent-only refusal). `ReviewPanes` renders the workspace over `shown ?? (reading ? frame : null)`, passes `reading` only when nothing answers, and hands `ReviewTechnicalDetails` the answer alone (or an `unanswered` label), so records are never shown under another subject; the page controls render only for an answer. The root publishes `data-review-pending` or `data-review-unavailable` with the requested subject, and `ReviewOutcomeRegion` receives `readingInWorkspace` so the read is stated once. `useReaderEngagement` on the root reports reader gestures to `navigation.engage` (the late-catalogue rule, see `ReviewNavigation.tsx`).

**One lane read for the tree comparison on screen (MIK-L32; review R1 F1, ruling 2026-09-30T13:07:38).**
`ReviewPanes` calls `useReviewLane(repo, master, leaf, treeComparisonNumber(payload.limitations))` once and hands
the result as `laneRead` to both `ReviewWorkspace` (the lane's rail destinations, its center and the source
explorer's labels) and `ReviewTechnicalDetails` (the source pane's attribution counts and lists), so every surface of
a tree comparison shows the one classification and there is exactly one `lane=files` request per comparison. A
dataset review names no tree comparison, so the hook asks nothing and both receive `null`.

**The reviewer's keyboard zone (MIK-L33, MIK-R33 rule 7).** The surface root carries `data-kbzone="review"`, the
keymap owner's `review` zone (`data/keymap/zones.ts`). The family tree binds its `j`/`k` change traversal
(`changeTraversal.useChangeTraversal`) on this element, so the chords act only while focus is inside the reviewer and
the owner's routing keeps them inert in inputs, textareas, contenteditable regions and the terminal zone. This is the
file's only MIK-L33 change.

Since `260921-ICR-L47`, `useSurface` passes `hold: navigation.settling` to `useReviewReadCycle`, so the
reviewer's first read waits (at most `SUBJECT_HOLD_MS`) for the catalogue to choose a subject, and calls
`useObservedComparison(navigation.observeComparison, shown)` so the navigation re-reads its catalogue only
when the displayed snapshot pair changes. The file grew by 3 lines to 931, over the 900-line soft rail
(L47-R1-F5, routed to L48, which reworks this file). **L48 closed it:** the record panes moved to
`ReviewRecordPanes.tsx`, leaving this file at 585 lines.

- The held first read and the snapshot observation. [1]

### Conventions

The component imports its types from `../../data/review` (the public entry that re-exports the
transport surface), the page helpers it mounts (`REVIEW_WALKABLE_COLLECTIONS`, `carriedPage`,
`continuationOf`, `intentOnlyRefusal`, `pageBounds`) from that same public entry, `ReviewPagedCollection`
as a type from it, its read cycle (`ReviewPageRequest`, `targetKeyOf`, `useReviewReadCycle`) from
`./ReviewReadCycle`, the refresh control and its one derivation from `./ReviewRefresh`, the read phases
plus the region from `./ReviewOutcome`, and the workspace together with its state hook from
`./ReviewWorkspace` — which is what makes one module the owner of the outcome states. It declares no
client of its own, **no longer imports `DiffPane`** — the diff engine is reached through
`KnowledgeStatements`, which is what keeps one rule in one place — and **no longer imports
`SourceContent`**, because an openable row is mounted by `SourceExplorer.tsx` now. Inline `style`
objects are used throughout,
matching the cockpit panels' idiom, and
every list item carries a stable `key` derived from the record's own identifiers (`assessment_id`,
`record_kind:record_id`, `signal_id`, `item_id:field`, `claim_id:path`, `claim_id`). Data attributes
carry the machine-readable facts — `data-pane`, `data-binding`, `data-change-state`,
`data-submission-state`, `data-testid` — so the surface's behaviour is inspectable without reading its
text. Sub-components are plain functions taking the payload or the pane they render; **none of them
holds state**, and the only reader state this file owns is `instead`, `selection`, the
`useWorkspaceState()` value and (L48) the surface's read cache, all held by `useSurface` for
`ReviewSurface`. The per-record keys and `data-*` attributes listed above now live with the record
renderers in `ReviewRecordPanes.tsx`. `data-side-state` **no longer
appears in this file**: it moved with the statement area into
`KnowledgeStatements.tsx`, where the same attribute still spells a side's declared state.

### Invariants And Boundaries

No browser path selects a dataset. Failed reads may retain only the last coherent answer to the same question and never invent an empty review. The frame keeps only the shell: nothing of the frame's subject is rendered as the requested subject's reading, records or comparison identity (`ICR-R26` isolation, L48). A selection never unmounts the workspace once a frame exists; only the first read, which has no frame, is stated at the surface level. One-sided statements, subject applicability, evidence currentness and authored assessments retain their existing owners. Source review remains reachable when only intent is unavailable.

### Todos

None recorded. The assessment-publication control is deliberately not shipped by this increment, and
the Source pane's expansion is a read: no control on this surface writes, and the byte-form rows stay
identification-only until this vocabulary can carry a path as bytes.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The current ownership and boundaries above are grounded in these source declarations.

- `useSurface` owns the behavior described above, including the cache, `selectSubject` and the `reading` status. [2]
- The unanswered subject's status, keyed and labelled with the requested subject. [3]
- `ReviewPanes` owns the behavior described above: the workspace over the answer or the frame, the records only for an answer, and the one lane read handed to both (MIK-L32). [4]
- One lane read per comparison through the real surface; none for a dataset review. [5]
- `ReviewSurface` owns the behavior described above, including the cache provider, the pending/unavailable root attributes and the engagement observer. [6]
- `PageControls` owns the behavior described above. [7]
- The root is the keymap owner's reviewer zone (MIK-L33). [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The component renders one repository
namespace's records and carries no identity that ranges beyond it.

No meaningful cross-repo references found.

## 260921-ICR-L25 Round 3 — The Reviewer's Own Narrow-Width Shape

**This surface gained its own scrollport and the layout constraints that let its panes fit a narrow
column.** The work is one round of the accepted design's B7 line, and it was driven by the round-2
verifier's findings F1 and F2 — so the shape of the change is best read as *two answers to two measured
facts*, not as a restyle.

**F2's answer: a vertical affordance of this panel's own.** The cockpit's `MAIN` is `overflow: hidden` by
a deliberate, documented shell decision (`cockpit/Cockpit.tsx`: *"the viewport does not scroll, its panel
scrolls on its own"*), shared with every other view. This panel had supplied no scrollport, so at 320 px
it rendered 7 620 px of content into a 706 px box that clipped it: `userScrollableCount` was **0**, the
window was exactly viewport-height, three wheel trials moved nothing, and a long guarantee was reachable
only by the browser's programmatic focus scroll. The root now carries
`style={{ height: "100%", minHeight: 0, minWidth: 0, overflowY: "auto" }}` — `height: 100%` plus
`minHeight: 0` *fills* the shell's row instead of growing past it, and `overflowY: auto` is the
scrollport a reader can move. **The shell was not changed and its decision is not overridden here.**

**F1's answer: the panes may shrink and wrap.** F1's measurement is what named the real cause — 51 of the
64 overflowing elements at 320 px were descendants of `[data-testid="review-surface"]` (the reviewer's own
root, `:906`), not of the inner `review-workspace`, and the pane sections were **565 px wide inside a
294 px column** with no pannable ancestor. The cause is a grid-item minimum, not a width: each pane is a
**grid item** of the disclosure, so its automatic minimum size is content-based unless it is told
otherwise, and the identities this surface prints are single unbreakable tokens — a 64-character
comparison reference measured **539 px**, a repository path **565 px** — while the inherited `break-word`
does **not** lower min-content. Three declarations answer it together, and none of them works alone:

- `pane` carries `minWidth: 0` and `overflowWrap: "anywhere"` (`:89-97`);
- the disclosure's own grid track is `minmax(0, 1fr)`, not the implicit `auto` (`:774-782`), because the
  track must be allowed to shrink below its items' min-content for the panes' `min-width: 0` to bite;
- the header row wraps (`flexWrap: "wrap"`) and the subject span takes its own `minWidth: 0` +
  `overflowWrap: "anywhere"` (`:828-848`), because at 320 px that row was the last thing past the edge —
  one unbreakable line of identities beside two controls, pushing the refresh control 4 px out.

**The regression pin, and what it does not claim.** `ReviewSurface.narrow.test.tsx` is the new
acceptance module for this change and it asserts **these declarations**, on `review-surface` rather than
on the inner root, precisely because neither round's defect was a wrong computation a rendered-text case
could catch. It is honest about its own limit: jsdom has no layout engine, so a `getBoundingClientRect()`
case there would read zeros and pass vacuously, and the module labels itself a **pin** while pointing at
the served-bundle probe for the measurement. Its card is
[ReviewSurface.narrow.test.tsx](ReviewSurface.narrow.test.tsx.md).

**Re-measured after the fix, and stated as the round-3 measurement reports it:** descendants of
`review-surface` past the viewport edge went **51 → 0** and the total **64 → 13**, with all 13 in neither
review root — they are cockpit chrome. `review-surface` is now the scrollport (`userScrollableCount`
0 → 1; a wheel over the review moves it 0 → 800 px), and `MAIN` no longer clips (its `scrollHeight`
7620 → 706, equal to its `clientHeight`). **The number was not improved by changing the root** — the
inner root's count was already 0 in both rounds, which is exactly why F1 was a classification defect.

- **The pane helper's two load-bearing declarations (moved unchanged to `ReviewRecordPanes.tsx` by L48).** [9]
- **The disclosure track that lets the panes shrink: `minmax(0, 1fr)`, not the implicit `auto`.** [10]
- The header wraps the task/subject controls while keeping their context and refresh action available. [11]
- The reviewer root owns its vertical scrollport while the shell retains its own layout responsibility. [12]
- The fixture builder and the mount this pin relies on, cited from their own declarations. [13]
- The shell decision this file does **not** change, and which stays routed to the cockpit owner: the comment that states it sits on the declaration itself. [14]

## 260921-ICR-L10 The Page Control That Reaches The Rest, And The Refusal It Renders

`260921-ICR-L10` (`ICR-R10@v1`) makes the remainder reachable. The surface used to render a
remainder with no control that reached the rest of the collection — the packet's own non-conforming
example — and it now renders the bounds, the scope and one action that advances the walk with the cursor
**the server published**, plus a first page action when a cursor was refused.

The control is `PageControls` with `PagePicker`, `PageActions` and `PageBoundsLine`, and the refusal is
`PageRefusalBlock`: the code, the owner's two identities, and a live first page of the collection that
was asked for. The page is part of the read's target key, so a page change is its own read rather than a
re-render over the wrong payload. No next action is offered for a body that published no cursor,
whatever remainder it reported — a button that fetches nothing is the defect this control exists to
prevent. Keyboard and focus traversal of the control remain `ICR-R24@v1`'s.

**ICR-R31@v1 narrows what the picker offers, not what the wire carries.** `PagePicker` maps
`REVIEW_WALKABLE_COLLECTIONS`, so it offers only the collections whose first page exists — `knowledge`
and `records`. The client's `ReviewPagedCollection` still carries all three members, and
`family_members` is deliberately not offered with no cursor because it is the set of per-family roster
walks a response composed: naming it would fetch the server's own `comparison_page_unreadable` refusal
for a question the reader did not mean to ask. A response whose page *is* `family_members` still renders
through the same bounds and continuation controls as any other.

## 260921-ICR-L26 The Three Mounted Labels

`260921-ICR-L26` (`ICR-R26@v1`) mounts the server's attribution facts on both review panes through three
small renderers and no new state: `applicabilityNote` prints one record's treatment with the true subject
its binding names (and prints **nothing** when the payload carries no label), `contextList` renders the
labelled context rows with the relationship that reached each one and the record's kind, and
`applicabilityCounts` renders the six-way partition beside the collections it filtered.
**879 → 946 lines.**

**A label is displayed, never computed.** The three renderers read the fields the server sent — the note
prints the server's own `detail` beside its `state` and subject, the context list prints the server's
`relationship` and `references`, and the counts block formats the server's numbers — and none of them
derives a treatment, a relationship or a total. A payload published before this vocabulary mounts exactly
as it did before, with no empty block standing in for an absent one.

**One record, one treatment, two panes.** `applicabilityNote` is called on the knowledge pane's
assessment/effect/signal rows and on the evidence pane's evidence link and observation rows, so the same
record cannot read one way in one pane and another way in the other; `contextList` and
`applicabilityCounts` are mounted on both panes for the same reason. The sibling's finding is **not**
rendered from a context row at all — the row carries the record's kind, and that is the whole point of
the value.

## 260921-ICR-L12 The Record Is Part Of The Question, And The Header States It

`260921-ICR-L12` (`ICR-R12@v1`) makes the record a first-class part of this surface's question and
says out loud which record the panes below are read from:

- **`history` joins `ReviewTarget` and the target key.** The key is now
  `repo/master/leaf/<history ?? "live">/<question>/<position>`, so switching records reloads rather
  than reinterpreting a response read for another record — the same rule the page cursor already
  followed. `intentReview` receives it as its last argument.
- **`ReviewHeader` is the surface's header, extracted as one component because the record statement is
  a claim about everything under it.** It renders the mounted provenance line
  (`data-testid="review-history"`) only for the recorded read: "recorded comparison — this leaf's
  durable generation, re-read from its own record: the panes below are the comparison it bound, not
  whatever the repository holds now." The root publishes `data-review-history` (`live` or the record)
  so a reader or a case can see the record without opening a pane.
- **`ReviewPanes` mounts the three panes and the two controls above them for one payload.**
- **Both extractions clear the lint rail without widening it.** `ReviewSurface` had grown past its
  `max-lines-per-function` rail while gaining the record statement; the two components were extracted
  with no ignore added and no limit changed, and every prop is threaded rather than re-derived.

The refusal path is untouched: a recorded read that earns a refusal still reaches the reader with its
code, detail and action, which is what makes a leaf that recorded nothing a stated state rather than a
missing entry.

## 260921-ICR-L17 The Read Cycle And The Refresh Control Leave The Surface

`260921-ICR-L17` (`ICR-R17@v1`) makes this surface a renderer of a read cycle it no longer owns, and
takes **462 lines of read logic and rendering out of it**. Two new modules arrive beside it in the same
child route:

- [`ReviewReadCycle.ts`](ReviewReadCycle.ts.md) owns the question's identity (`targetKeyOf`), the one
  read started for it (`startRead` through `askReview`) and the state a reader's refresh needs
  (`useReviewReadCycle`, returning the read, the retained comparison, the carried binding identity and
  the `refresh` callback). `ReviewPageRequest` is declared there now and imported back, because the page
  position participates in the target key the hook computes.
- [`ReviewRefresh.tsx`](ReviewRefresh.tsx.md) owns the reader's explicit refresh control, the notice
  that answers it, and the one derivation of a claim (`generationOf`). The header receives both as a
  `refresh` node and mounts them beside the subject line, because the control belongs to the question the
  header names and the notice describes the comparison the panes below are showing.

**What is deleted here rather than moved.** The inline `load` callback, the `useEffect` that called it,
the `targetKeyOf` function, the private `ReviewPageRequest` interface and the `useState`/`useCallback`
read state are all gone: `useReviewReadCycle` supplies `read`, `retained`, `carried` and `refresh`, and
what stays in this component is the `instead` state, the `selection` state, the coherence check on the
retained generation and the wiring of the three regions.

**What a later reader must not undo.** The retained generation is still used only when it was read for
the question on screen now (`retained.key === targetKey`): the check is belt-and-braces beside the
reset inside the hook, because a payload under a header it was not read for is exactly the mismatch this
surface must not be able to produce. `retryFor` now takes the hook's `refresh` rather than a reload
promise, so a retry is the same one read path as the refresh control and can never become a second way
of composing a review.


## 260921-ICR-L23 The Unmeasured Line The Submission Block Mounts

`SubmissionBlock` gains a third mounted line, keyed on `staleness.state === "not-measured"`
(`:557-565`) and carrying `data-testid="review-staleness-unmeasured"`. It renders the boundary's
own sentence and nothing else: no previous input is named, because nothing was observed to move,
and the block's existing `stale` line (`:554`) and disabled-submission state are untouched.
That is the whole point of the state — a switched checkout or an unreadable generation must not
be able to read as an ordinary current review on the one line this block mounts, and it must not
be able to borrow the `stale` rendering that would assert a movement nobody measured.
