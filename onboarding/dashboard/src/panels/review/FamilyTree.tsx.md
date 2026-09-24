# dashboard/src/panels/review/FamilyTree.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/FamilyTree.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `63b476297708f779de8ed5c0bf3555b9d1de70c2` |
| lastVerifiedCommitDate | 2026-09-24T04:10:11+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The family column of the Intent Reviewer's family route: recorded families rendered as the semantic
parents of the review population, each with its own independently authored joint guarantee beneath
it and that family revision's complete member statements beneath that. The three levels stay
separate on purpose and nothing here is derived from anything else — a family label is a display
fact, the guarantee is the family owner's stored text printed whole and wrapped, and a member
statement is that member revision's stored text; no level concludes anything about the levels beside
it, and the unchanged siblings are included because a member that did not change is still part of
what the guarantee is about.

**A tree is a presentation of recorded relations, not a claim that the graph is single-parent.** The
same invariant revision recorded under two families appears beneath each of them — that is what the
server publishes `other_family_revision_ids` for — and it is the *same* canonical revision in both
places rather than a copy: rows are keyed by the member revision identity, and a repeated membership
is never counted as another subject.

**The five context states are not one state, and each renders its own sentence.** `recorded` and
`partial` composed a family; the `no_family_recorded` destination states a *measured* zero; the
uninitialized/unavailable channel states that no recorded scope was read, which is attribution
unknown and never silently grouped as "no family"; `no_subject_selected` says this review asked about
no subject at all. Where the server sent its own value, that value is what is printed.

**Selection is a roving-focus group, not a pointer.** A family's guarantee control opens that
family's review; a member control opens that member's review with the family context retained. The
current selection is exposed on the tree and on each node through `aria-current`, the nodes are real
buttons in one roving-focus group, and the arrow keys move within it — so the whole tree is
traversable without a mouse, while Enter and Space stay the buttons' own activation.

## Code Commentary

### Logic

**`memberRows(entry)` is the roster union and the one thing that keeps the tree from inflating.** It
walks `FAMILY_SIDES` and each side's `members`, filling a `Map` keyed by `invariant_revision_id`. A
revision seen for the first time becomes a `MemberRow` carrying that side in `sides` and the member
value that side carried; a revision already in the map has the new side pushed onto `sides`, and its
`member` value is replaced by the after side's row only when that row's own `state` is `recorded` —
so the value a reader sees is the revision the reader is looking at now, and otherwise the before
side's. A membership recorded on both sides is therefore one row carrying both sides, and the count
of rows is a count of distinct member revisions rather than of associations.

**`FamilyTree` derives everything from the union and never from the raw arrays.** It trims and
lowercases the caller-owned `query`, computes `allMembers` by reducing `memberRows(entry).length`
over every entry, filters `context.entries` through `familyMatches` (or keeps all of them when the
needle is empty), and recomputes `shownMembers` over the filtered set. `composed` is
`context.entries.length > 0`, which is what decides between the filter's own empty state and a review
that composed no family context at all.

**`familyMatches(entry, needle)` builds one lowercase haystack per family**: the family id, the
optional display label, both sides' optional `joint_guarantee` texts, every candidate's
`joint_guarantee`, and, for each row of `memberRows(entry)`, the row's `invariantRevisionId`, the
member's `invariant_revision_id`, its label and its statement. A match inside a member therefore
keeps that member's family and its siblings on screen, which is what "search retains the matching
family's context" means.

**The family node prints its guarantee in one of three shapes, decided by what the two sides
recorded.** `guaranteesOf(entry)` returns nothing when neither side has a guarantee — and
`FamilyGuarantees` then prints the sentence that no family revision was selected for this family, so
no guarantee of it may be shown, followed by the entry's own `detail`. When both sides recorded one
and the two `revision_id` values are equal it returns a single record labelled `both` with the note
that both snapshots selected this family revision; when the ids differ it returns the before record
and the after record, each labelled with its side and its own revision id; when exactly one side
recorded one it returns that record labelled with its side and the note that this side only recorded
it. A side that recorded no revision contributes nothing here, because printing its neighbour's text
as if it were shared is what this refuses.

**`SideStates` and `FamilyHistory` state the side facts beside the guarantee.** `SideStates` draws
one `review-family-side` line per side whose `state` is not `recorded`, carrying the side name, that
exact state and the side's own `detail`. `FamilyHistory` draws one `review-family-history` line per
side whose `recorded_revision_ids` is non-empty: how many revisions of this family that snapshot
records, and then either that this review selected none of them or which revision it selected. The
population the sentence counts is the family owner's own revision list, which is larger than the
revisions the selection reached.

**`RosterLine` prints the read owner's two measures as two different populations.** It returns
nothing when the side has no `page`, and otherwise prints, from `page.counts`, how many
`primary_items_returned` of `primary_items_total` items of the family revision's recorded selection
this page carried and how many are `primary_items_remaining`, and then, from the side's own
`members_total`, how many membership rows the selected family revision records and how many of them
this page carried. The two numbers are different populations — the item counts measure the family
revision's whole recorded selection, while `members_total` counts its membership rows alone — so a
page that carried every membership row can still report items remaining, and reading the item
remainder as "more members remain" would be false about the store. The line also prints the
selection's unresolved-anchor count when it has one, the page's own `scope` (or `no scope recorded`),
and `data-roster-complete` from the page's own flag.

**`completionNote(page)` says what a complete page's completeness actually means, and it depends on
which page it is.** `complete` is the read walk's flag rather than the page's: a walk the read took in
one page *is* the whole selection, so a `first_page` says "the page is the whole selection", while the
final page of a multi-page walk is only the last position in it — the pages before it carried the rows
this one did not — so it says that it completes the walk instead. Saying the first sentence for the
second page was false about the store, and it became reachable once the walk's completion guard was
corrected to let a final page exist at all.

**`emptyRosterSentence(entry)` is the one sentence about an empty roster, and it keeps three facts
apart.** It collects the sides whose `state` is `recorded`; with none of them it prints that no member
row is carried here plus the entry's own `detail` (there is no roster to describe). With recorded
sides it sums their `members_total`: a sum of zero prints the measured zero — the read measured zero
memberships for the selected family revision — and only here may that be said. Otherwise it states
the page-scoped fact, naming each recorded side's carried-of-measured pair through `carriedOf`, and
adds the continuation sentence **only** when some recorded side's page exists and is not `complete`.
When nothing is bounded the sentence stops at the page-scoped fact and does not reach for an
explanation of where the other rows went: an explanation no case exercises is a sentence this leaf
cannot prove. `MemberRoster` mounts it behind `review-family-empty-roster` exactly when the row union
is empty, and `FamilyReviewCenter` mounts the same function for the same empty state, so the two
columns cannot disagree about what an empty roster means.

**`RosterNext` publishes the cursor the page published, and it is the only family-walk control.** For
each side it returns nothing when the side has no page, when the page is `complete`, or when the page
published no `continuation`; otherwise it renders a `review-family-roster-next` button carrying
`data-family`, `data-side` and `data-continuation` and labelled with the side, the family label and
the fact that the cursor is the one this page published, and calls
`onRosterNext(family_id, side, page.continuation)`. Nothing here mints a cursor: `family_members` is
not one walk but the set of per-family walks a response composes, so naming it with no cursor earns
the server's own refusal rather than an arbitrary walk's first page — and the cursor a reader is told
to present is exactly the value the refusal's own action sentence names.

**`MemberNode` prints one row's control, its statement and its recorded membership facts from the
row's own carried value.** The button's label comes from `memberLabel` (the display label, or the
display version, or the revision id, plus the version when both display fields exist), the amber side
tag and the sentence from `memberSidesNote` name the sides the row was recorded on — "recorded on
both snapshots" for two sides, the single side otherwise — and `aria-current` is set only for the row
that is the current selection. When the member's `state` is `recorded` its stored `statement` is the
paragraph; otherwise the row renders `review-family-member-state`, which says the statement is not
carried on this page, names the exact state and prints the member's `detail` — never a blank
statement, which would read as a recorded empty one. A member with `other_family_revision_ids`
renders `review-family-member-shared` and names those revisions, so the shared-identity fact is
visible where the row is.

**`treeArrow` is the keyboard half of the roving-focus group, and it moves focus only.** The handler
sits on the buttons themselves rather than on their container, because a listener on a plain list
would give the list an interaction role it does not have and cannot honour. It maps `ArrowDown` to
`+1` and `ArrowUp` to `-1`, finds the selectable nodes with
`closest("[data-testid=review-family-list]")` and `querySelectorAll("[data-tree-node]")`, and moves
focus to the neighbour at `(index + delta + nodes.length) % nodes.length`, wrapping at both ends.
Any other key returns without preventing the default, so Enter and Space remain the buttons' own
activation and selection stays a real button click.

**`FamilyList` and the root agree on one list and one filter.** `FamilyList` renders the filtered
entries in a `review-family-list` list and is what `treeArrow` searches for its roving ancestors.
The root section carries `review-family-tree` and `data-family-state` from the context's own state,
mounts the labelled search input (`review-family-filter`, cleared on Escape through `onQuery("")`),
then the filter-scope line, the context state line (`review-family-context`, carrying
`data-context-state` and printing the server's `state` and `detail`), the composed counts
(`review-family-counts`: returned of total family contexts, remaining or none remaining, the
membership-row total and the distinct member revision total) only when something was composed, one
`review-family-limitation` line per stated limitation, and then either the list or
`review-family-none-shown` — which distinguishes a filter that matched nothing from a review that
composed no family context at all, and says in the first case that the composed contexts are
unchanged by the filter.

**`filterScope` states a display filter and never restates the comparison's totals.** With an empty
query it states how many family contexts and recorded member rows are shown and that no filter is
applied. With a query it states how many of each the filter matched and then, explicitly, that this
is a filter on this display only: the comparison's recorded totals are unchanged and clearing the
filter restores every row.

### Conventions

The module is one default-free file of small function components plus two exported pure helpers
(`memberRows`, `familyMatches`) and three exported presentational components reused elsewhere
(`RosterLine`, `RosterNext`, `emptyRosterSentence`) — the centre mounts the same three rather than
declaring a second roster line, a second continuation control or a second empty-roster sentence.
Styling uses the `styled-system/css` `css` helper with inline style objects hoisted to module
constants (`shell`, `sectionLabel`, `searchInput`, `muted`, `statements`, `node`, `current`,
`guaranteeText`, `memberText`, `sideTag`, `familyBlock`), matching the cockpit panels' idiom; the
`cx` helper composes the base node class with the amber current-selection class. Every list item and
every per-side element carries a stable `key` (`entry.family_id`, `row.invariantRevisionId`, the
member revision, the side name, `${side}:${revision_id}`). Sub-components take the entry (or the side
context) and the handlers they need, hold no state at all, and expose machine-readable facts as data
attributes — `data-testid`, `data-side`, `data-side-state`, `data-family`, `data-family-state`,
`data-guarantee-side`, `data-guarantee-revision`, `data-tree-node`, `data-revision`, `data-sides`,
`data-continuation`, `data-roster-complete` — so the tree's behaviour is inspectable without reading
its text. `FamilySelection` is exported so the workspace and the centre share one selection type, and
the tree takes its selection and its query from the caller rather than owning them.

### Invariants And Boundaries

- **Three levels, no derivation.** The family label, the family revision's stored `joint_guarantee`
  and each member's stored `statement` are printed as themselves; nothing here summarizes a member
  into a guarantee or a guarantee into a verdict.
- **Unchanged siblings are part of the tree.** A member whose statement did not change is rendered
  because the guarantee is about it.
- **A repeated membership is one row.** `memberRows` unions both sides by
  `invariant_revision_id`, so a revision recorded under two families — or on both snapshots — never
  inflates the tree, and the row's own `member` value is the after side's only when that side carried
  content.
- **The guarantee's three shapes are kept apart.** One revision for both sides, two distinct
  revisions, and one side only are three different records with three different notes; a side that
  recorded no revision never borrows its neighbour's text.
- **The owner's two populations are printed apart.** `counts.primary_items_*` measures the family
  revision's whole recorded selection and `members_total` counts its membership rows; neither is
  rendered as the other.
- **Only the owner's own numbers decide an empty-roster sentence.** `emptyRosterSentence` reads
  `members_total` and the page's own `complete`, never "a page exists", so a measured zero and a
  bounded page that carried none of N rows are two different sentences.
- **Nothing is said about a snapshot from a bounded page.** The missing-row fact belongs to
  `FamilyReviewCenter.missingRowNote`; this file's bounded-page sentence states only what this page
  carried and that the continuation reaches the rest.
- **The family walk happens in exactly one place.** `RosterNext` renders the page's own published
  cursor and no control at all without one, and no other component in this file advances a walk.
- **A member without its content says so.** `content_not_on_page` renders the explicit state line,
  never an empty statement.
- **Selection is display state with an accessible current marker.** `aria-current` marks the current
  node, the arrow keys move focus inside one roving group, and no control writes anything.
- **The filter is a display filter.** `filterScope` says so in words, `familyMatches` only decides
  what is shown, and the comparison's own recorded totals are never recomputed.
- **Boundary.** This is a presentation component: it resolves no candidate, starts no request, holds
  no durable state and owns no route. Its two caller-owned values (`selection`, `query`) and its two
  callbacks (`onSelect`, `onRosterNext`) are threaded from `ReviewWorkspace.tsx`.

### Todos

None recorded. The tree's own sentences are the ones the family route needs; a state this vocabulary
cannot yet carry would arrive as a new server fact rather than as a rendering-side default.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the header's own statements about the
three levels, the recorded-relations rule, the five context states and the selection model, the row
union, the side and history lines, the roster line with its two populations, the single empty-roster
sentence, the one family-walk control, the guarantee shapes, the member node, the filter and the
keyboard traversal, and the two callers that mount these exports. Every anchor in a row occurs inside
the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own statement of the three separate levels, of unchanged siblings belonging to the tree, of the cross-family shared revision, of the five context states, and of the selection model.** | "unchanged siblings"; `other_family_revision_ids`; `no_family_recorded`; "aria-current" | dashboard/src/panels/review/FamilyTree.tsx:1-26 |
| The one tree selection type: a family's guarantee review, or one member revision inside it. | `FamilySelection`; `memberRevisionId` | dashboard/src/panels/review/FamilyTree.tsx:42-46 |
| **The roster union: both sides keyed by `invariant_revision_id`, so a repeated membership is one row and the row's member value is the after side's only when it carried content.** | `memberRows`; `byRevision`; "member.state === \"recorded\"" | dashboard/src/panels/review/FamilyTree.tsx:150-172 |
| **Every side that is not a complete roster states its own name, its exact state and its own detail.** | `SideStates`; `data-side-state`; `review-family-side` | dashboard/src/panels/review/FamilyTree.tsx:174-197 |
| The recorded history lines: the family owner's own revision list, which is a larger population than the selection reached. | `FamilyHistory`; `recorded_revision_ids`; `review-family-history` | dashboard/src/panels/review/FamilyTree.tsx:199-221 |
| **`RosterLine`, printing the read owner's two different populations — the family revision's recorded selection items and its membership rows — and carrying the page's own completeness flag.** | `RosterLine`; `primary_items_remaining`; `members_total`; `data-roster-complete` | dashboard/src/panels/review/FamilyTree.tsx:223-259 |
| **`completionNote`: what a complete page's own flag means, which differs between a one-page walk's first page and the final page of a multi-page walk.** | `completionNote`; "the page is the whole selection" | dashboard/src/panels/review/FamilyTree.tsx:261-272 |
| One recorded side's carried-of-measured pair, stated in the owner's two numbers. | `carriedOf`; "recorded membership row(s) it measured" | dashboard/src/panels/review/FamilyTree.tsx:274-277 |
| **`emptyRosterSentence`: the one sentence both columns mount, keeping no-family-revision, the measured zero and the bounded page apart, and stopping at the page-scoped fact when nothing is bounded.** | `emptyRosterSentence`; "the read measured zero memberships"; "The continuation beside each bounded roster reaches" | dashboard/src/panels/review/FamilyTree.tsx:279-303 |
| The per-side roster line mount. | `RosterLines`; `RosterLine` | dashboard/src/panels/review/FamilyTree.tsx:305-315; dashboard/src/panels/review/FamilyTree.tsx:232-232|
| **`RosterNext`: the family collection's only walk control, rendered from the cursor the page published and absent without one.** | `RosterNext`; "data-continuation"; "continue the" | dashboard/src/panels/review/FamilyTree.tsx:317-355 |
| The label fallback: the recorded display label, or the family id. | `familyLabel`; "entry.display_label ?? entry.family_id" | dashboard/src/panels/review/FamilyTree.tsx:357-359 |
| **The three guarantee shapes: one revision labelled as both sides' record, two revisions labelled with their own sides, and one side only — with a side that recorded nothing contributing nothing.** | `guaranteesOf`; "side: \"both\"" | dashboard/src/panels/review/FamilyTree.tsx:361-391 |
| The guarantee block itself, and the sentence it prints when no family revision was selected. | `FamilyGuarantees`; "no family revision was selected for this family" | dashboard/src/panels/review/FamilyTree.tsx:393-419 |
| The recorded heads an unresolved lineage left unchoosable, each named by its own revision identity. | `FamilyCandidates`; "recorded head(s) this context declined" | dashboard/src/panels/review/FamilyTree.tsx:421-432 |
| One row's control label, decided from the row's own carried display values. | `memberLabel`; `display_version` | dashboard/src/panels/review/FamilyTree.tsx:434-444 |
| One row's membership sentence, decided from the row's own recorded sides. | `memberSidesNote`; "recorded on both snapshots" | dashboard/src/panels/review/FamilyTree.tsx:446-450 |
| **One member node: its selectable control with `aria-current`, its stored statement, the explicit not-carried state line, and the shared-family list.** | `MemberNode`; `review-family-member-state`; `review-family-member-shared` | dashboard/src/panels/review/FamilyTree.tsx:452-505 |
| **`MemberRoster`: the complete roster this page carried, or the one empty-roster sentence — which is decided from the owner's own counts and the page's completeness, never from "a page exists".** | `MemberRoster`; `review-family-empty-roster`; `emptyRosterSentence` | dashboard/src/panels/review/FamilyTree.tsx:507-546; dashboard/src/panels/review/FamilyTree.tsx:284-284|
| **One family node in its render order: the guarantee control, the label side, the guarantees, the candidates, the side states, the history, the rosters, the members and the continuation.** | `FamilyNode`; `data-family-state`; `FamilyGuarantees` | dashboard/src/panels/review/FamilyTree.tsx:548-597; dashboard/src/panels/review/FamilyTree.tsx:393-393|
| **`filterScope`: the display-filter statement that never restates the comparison's recorded totals.** | `filterScope`; "the comparison's recorded totals are unchanged" | dashboard/src/panels/review/FamilyTree.tsx:599-612 |
| The match rule: one lowercase haystack per family over its ids, its guarantee texts, its candidates and every member row. | `familyMatches`; `joint_guarantee` | dashboard/src/panels/review/FamilyTree.tsx:614-634 |
| **`treeArrow`: the roving-focus traversal over the selectable nodes, moving focus only so activation stays the button's own.** | `treeArrow`; `data-tree-node`; `review-family-list` | dashboard/src/panels/review/FamilyTree.tsx:636-653 |
| The filtered list the arrow handler searches, and the key it searches it by. | `FamilyList`; `review-family-list` | dashboard/src/panels/review/FamilyTree.tsx:655-679 |
| **The root: the labelled filter input, the filter scope, the context state, the composed counts, the limitations, and the two empty states that distinguish a filter matching nothing from a review that composed no family context.** | `FamilyTree`; `review-family-filter-scope`; `data-family-state` | dashboard/src/panels/review/FamilyTree.tsx:681-756 |
| **The centre mounts the same roster line, the same continuation control and the same empty-roster sentence rather than declaring a second of each.** | `RosterLine`; `RosterNext`; `emptyRosterSentence` | dashboard/src/panels/review/FamilyReviewCenter.tsx:41-46 |
| **Both mount points in the workspace: the family column that renders the tree and the selection column that renders the centre, with the selection, the query and the walk handler threaded from the workspace's own state.** | "<FamilyTree"; "<FamilyReviewCenter" | dashboard/src/panels/review/ReviewWorkspace.tsx:214-221; dashboard/src/panels/review/ReviewWorkspace.tsx:317-330 |
| The public entry this file imports its family values from, which re-exports the mirror module. | `FAMILY_SIDES` | dashboard/src/data/review.ts:36-41 |
| The case that pins the three levels in one rendering: the recorded families, their authored guarantees and the full member statements. | "renders the recorded families, their authored guarantees and the full member statements" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:153-153 |
| The case that pins the selection marker and the keyboard traversal of the tree. | "marks the current selection and traverses the tree by keyboard" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:372-372 |
| The case that pins one empty-roster sentence mounted in both columns rather than two that happen to agree. | "prints one empty-roster sentence in both columns, not two that happen to agree" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:617-617 |
| The case that pins the bounded page that carried none of the measured rows, and the case that pins the real measured zero beside it. | "says a bounded roster carried none of the measured rows, never that the read measured zero"; "still says the measured zero when the read really measured zero memberships" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:429-429; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:452-452 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It renders the family records of one
repository namespace from a payload the server composed, and carries no identity that ranges beyond
it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the family tree column. It records that the file renders three separate levels — the family label, the family revision's own independently authored joint guarantee, and the complete member statements with the unchanged siblings included — and derives nothing across them; that `memberRows()` unions both sides by `invariant_revision_id` so a repeated membership never inflates the tree and the row's member value is the after side's only when that side carried content; that `RosterLine` prints the read owner's two different populations (`counts.primary_items_*` for the family revision's whole recorded selection against `members_total` for its membership rows) with `completionNote` distinguishing a one-page walk's first page from a multi-page walk's final page; that `emptyRosterSentence()` is the one sentence both this column and the centre mount and keeps no-family-revision, the measured zero and the bounded page apart; that `RosterNext` renders only the cursor the page published and is the family collection's only walk control; that selection is a roving-focus group with arrow-key traversal and `aria-current`; and that `filterScope()` states a display filter without restating the comparison's totals. Every row of the reference table was derived against this leaf's candidate, and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
