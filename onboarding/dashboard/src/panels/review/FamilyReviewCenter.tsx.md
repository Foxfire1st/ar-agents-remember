# dashboard/src/panels/review/FamilyReviewCenter.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/FamilyReviewCenter.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `63b476297708f779de8ed5c0bf3555b9d1de70c2` |
| lastVerifiedCommitDate | 2026-09-24T04:10:11+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The unified central reading path of the family route: one intent-to-expression route for the selected
family or member, rendered in one column in the order the packet names — the family guarantee and the
selected intent first, then the linked expressions, then the recorded execution evidence and the
authored assessment. `ICR-R24@v3` rejects a surface where the reviewer has to reconstruct the
relationship between an intended guarantee, the exact statement it is about, the source that
realizes it, the evidence someone executed and the judgment someone authored by switching tabs or
opening a detached inspector; this module renders that route in one column instead. Every block reads
records other owners store, none of them concludes anything about another, and no block can carry a
verdict.

**The independent facts stay independent.** A statement change, a membership/realization change, a
source/test change, an execution observation and an authored assessment are five separate states
owned by five separate modules. This rendering prints each of them under its own heading with the
owner's own words, so a member that changed cannot read as a claim that its family guarantee holds,
and a guarantee revision cannot read as an assessment.

**What it refuses to do.** It does not compare two operands the store did not record both of — a side
that carried no revision has no text to diff, and "unchanged" is a claim about two operands; it does
not print a member statement whose revision content was not on the page; and it does not show a
record of another subject as this member's evidence — records are joined on the recorded
`invariant_revision_id` the server publishes as the join key, and everything not joined is counted
and stated rather than displayed.

The source explorer is mounted beneath the reading path unconditionally, so the complete measured
review population stays reachable while a family or member is selected: the family navigation is an
attribution lens, not an exclusion filter.

## Code Commentary

### Logic

**`GuaranteeComparisonBlock` renders the five shapes of `guaranteeComparison(entry)` as five
different sentences, and only one of them may say the guarantee is unchanged.** `unrecorded` prints
that neither snapshot selected a family revision for this family, plus the composition's own
statement. `one_sided` prints that only that side records a family revision, that no comparison was
made, that the other snapshot records none, and — explicitly — that this is a one-sided guarantee
and not an unchanged one, and then mounts the one guarantee through `GuaranteeBlock` with its side.
`unchanged_revision` prints that both snapshots selected the same revision, so the guarantee is
unchanged because one authored revision stands behind both sides. `identical_text` prints that the
two snapshots selected different revisions whose recorded guarantee text is identical — a revision
was authored between them and the text is what did not move — and lays the two `GuaranteeBlock`s side
by side. `changed` prints the two revision ids and mounts `DiffPane` over the two
`joint_guarantee` texts in the caller's layout, with both revisions named beneath it.

**`GuaranteeBlock` prints one guarantee whole with the identities a reader needs to find it again.**
The metadata line carries the family id, the side when one was named, the revision id, the display
version, `state_at_origin` and the `acceptance_ref` when the record has one; the stored
`joint_guarantee` text is the prose paragraph. Provenance and the payload seal are technical detail
and stay out of the reading path.

**`MemberStatement` is the only place a member's stored text is rendered, and it can never render a
missing statement as an empty one.** When the member's own `state` is not `recorded` it prints
`review-center-member-not-on-page`: this page did not carry the revision content of that member
revision, so no statement for it may be shown here, followed by the member's own `detail`. Otherwise
it mounts `MemberIdentity` (the label and version it was authored under, the exact revision identity
and the lifecycle when the record has one), the stored `statement` as prose, and `MemberFacts` — the
recorded applicability, the essential conditions and the exclusions, each printed only when the store
has one, so an absent list is absent rather than an empty claim.

**`missingRowNote(entry, side)` decides what may be said about a side this comparison has no row for,
and only one of its two answers is about the snapshot.** When that side's own `state` is not
`recorded` the note says the side read no roster, names that exact state, and states that this
revision has no such operand. Otherwise the side did read a roster, and the note turns on that
roster's page: a side with no page or with a `complete` page means the snapshot really records no
member row for this revision, while a side whose page is a position in a bounded walk means only
that *this page* did not carry the row — and saying the snapshot records none would be false about
the store, so the note states the page fact and names the continuation beside it as what reaches the
rows this page did not carry.

**`oneSidedStatement(entry, comparison)` is mounted for the `one_sided` member comparison, and its
sentence is decided from each member's own state and its roster page's completeness rather than from
the comparison kind.** With no operand at all it prints that neither snapshot carried a member row
for the selected revision. Otherwise it partitions the listed sides into those whose row was listed
without its revision content and those that carried content, and finds the side that listed nothing:
when a listed row was not carried it says which side(s) listed the membership row without its
content and where the carried side's content is below; when nothing is missing it says no operand is
missing from this comparison; otherwise it delegates to `missingRowNote` for the side that listed
nothing. The note is always followed by the sentence that no before/after comparison is drawn from
one side's content, and the one member statement there is, is mounted beneath it. The round-1 bytes
printed "the after snapshot records no member row for this revision" for a row the after snapshot
*does* record and merely did not carry on that page, while the tree row for the same member read
"recorded on both snapshots"; this function is where that disagreement was removed.

**`memberStatementBlock` dispatches the four `memberComparison` kinds.** `not_on_page` mounts the one
member `MemberStatement` there is — the page-scoped fact, with no comparison claimed. `one_sided`
goes to `oneSidedStatement`. `unchanged_revision` prints that both snapshots record the same member
revision, that the statement is unchanged and that the change this review is about is elsewhere, and
mounts the member. `changed` mounts `DiffPane` over the two carried statements, mounts a
`MemberStatement` for any side whose own state was not `recorded` (so an uncarried side is stated
rather than diffed against a blank), and names both revision identities beneath.

**`RealizationClaims` prints the member's recorded realization claims and nothing else.** With no
claims it prints that no realization claim is recorded for this member revision in this payload.
Otherwise each claim is one row carrying its `claim_id` and the role its author recorded, then either
the recorded address with what this read resolved it to, or the explicit statement that this read
observed no address for it — never an empty path, which is what the server refuses to send — then the
claim's `rationale` and its `detail`.

**`AttributedPaths` is the measured source attribution of one member revision, joined on the member's
own `invariant_revision_id`.** It filters `payload.source.locations` to the records whose own
`invariant_revision_id` equals the member's, and with none of them prints that no source location
record in this payload names this member revision, naming the revision and stating that the source
owner publishes one record per selected claim. Each row carries `data-change-state` from the
location's own value and prints a `review-center-open-path` button — addressed by the published
`path` and wired to `onOpenPath` — when the path is among the comparison's measured changed paths,
and the path as plain `<code>` when it is not, together with the role (or `unclassified (no role
recorded)`), the owner's own `change_state`, the `before-only` marker when it applies, and the
`resolution`. A path that is not listed carries one of two sentences: when the inventory is partial,
that absence from its list is not a measurement that the path did not change; otherwise, that the
path is not a changed path of the comparison's measured change set. The location's `rationale` and
its `reached_via` paths follow when the record has them.

**`EvidenceBlock` joins the evidence and the authored judgment on the member's own
`invariant_revision_id`, and counts-and-names the records that name another subject instead of
displaying them.** Observations are filtered to those whose `revision_id` is this member revision and
assessments to those whose `applicability.subject_revision_ids` includes it; `unjoined` is the total
of the pane's observations and assessments minus the joined ones. The block states the comparison's
own `evidence_state` and how many of the observations name this member revision, mounts the
`observationBlock` rows (id, execution result, and the tested candidate, command identity, artifact
reference and digest, each printed as `not recorded` / `no digest` when the store has none) or the
statement that no recorded observation names this member revision, then states the comparison's own
`assessment_state` and the joined assessment count, mounts the `assessmentBlock` rows (disposition,
finding, rationale, the attribution that prints `author: unresolved reference` for an absent author,
the binding state and the role when there is one) or the sentence that an absence of a recorded
judgment is not a judgment that the member is fine, and finally, when `unjoined` is non-zero, states
how many records in this payload name another subject and are not displayed beside this member —
because a record belongs to the review of the subject its own binding names.

**`memberContextHeading(entry)` prints "Complete recorded member context" only when the entry really
is complete.** It requires both that the entry's own `state` is `recorded` and that `membersComplete`
holds, and `membersComplete` is the same predicate the tree uses: every side's page is absent or
`complete`, which is the read owner's own flag rather than "some rows happen to be here". Any other
entry gets `Recorded member context (partial)`, so a bounded or partial context says so in its own
heading instead of borrowing the complete claim.

**`memberContextCounts(entry, carriedCarried)` prints the read owner's measured total rather than this
page's share.** With no recorded side it prints that no snapshot records a family revision for this
family, plus the entry's `detail`. Otherwise it sums the recorded sides' `members_total`, spells the
per-side breakdown, states how many member rows this page carried of that measured total, and appends
the sentence naming the continuations beside the bounded rosters **only** when the entry is not
complete. The two populations are printed apart for the same reason `RosterLine` prints them apart:
`members_total` is what the read measured and the page's share is what the reader is looking at.

**`FamilyCenter` is one family's context in the central reading path, and it reuses the tree's own
components.** It computes the distinct member revisions of the page by folding
`entry.before.members` and `entry.after.members` into a `Map` keyed by `invariant_revision_id`, then
renders the family heading and the entry's own state and selection lines (`selection.state` and its
`statement`), the guarantee comparison block, and the member-context card: the heading from
`memberContextHeading`, the counts from `memberContextCounts`, the distinct-member sentence, the two
per-side `RosterLine`s (mounted with `testid="review-center-roster"`), one `review-center-open-member`
control per distinct member with its stored statement or its explicit not-carried line, the
`emptyRosterSentence` behind `review-center-family-empty` when no distinct member exists, and the
`RosterNext` continuation control with `testid="review-center-roster-next"` — the same cursor and the
same handler the tree uses.

**`IndependentFacts` prints the five independent facts, each from its own owner's value.** The
guarantee fact comes from `guaranteeComparison(entry)` (unchanged / identical text on two distinct
authored revisions / changed / recorded on one snapshot only with no comparison made / not compared);
the statement fact comes from `memberComparison` over the member's two rows found in the two sides
(unchanged / changed / one-sided / not carried on this page so nothing is compared); the membership
fact names the snapshots that recorded the row, the recorded realization-claim count and how many
other family revisions cite this same member revision; the source-attribution fact counts the
location records naming this member revision and breaks them down by the owner's own `change_state`;
and the authored-judgment fact counts the assessments bound to this member revision and states that
no member, membership or guarantee change creates one. The strip exists so a reader can see that a
member change produced no guarantee revision and no assessment rather than having to infer it from
what is absent further down.

**`MemberCenter` is the member reading path, and it keeps the family context above the member.** It
finds the member's two rows in the entry's sides, builds the set of paths this comparison's inventory
listed, and renders the member heading with the family label and the selected family revision above
the guarantee comparison block — the packet's "member selection keeps the family context", so the
guarantee the statement is about is on screen with it. The four cards that follow are the packet's
order: the independent-facts strip, "Selected intent" with `memberStatementBlock`, "Linked
expressions" with `RealizationClaims` and `AttributedPaths` (fed the inventory's listed paths, its
`partial` flag and the centre's own open-path handler), and "Execution evidence and authored
assessment" with `EvidenceBlock`. `RosterNext` is mounted at the end with the same cursor and handler
for the reader whose selected member's side content was not carried on this page — exactly the reader
who needs the continuation.

**`FamilyReviewCenter` resolves the selection and mounts the explorer beneath the reading path.** It
takes the whole `ReviewPayload` and a `FamilySelection | null`, finds the entry by `family_id` and
the member by `invariant_revision_id` in the union of the entry's two sides, and publishes
`data-selection-kind` as `none`, `member` or `family` from which of the three it resolved. An
unresolved entry mounts `UnselectedCenter`, which says what the column is for and states that the
complete source change explorer below is the whole measured review population and is **not** filtered
by this selection — the one thing a reader must know before choosing, because the family navigation
is an attribution lens rather than an exclusion filter. Otherwise it mounts `MemberCenter` or
`FamilyCenter`, and beneath either one `SourceExplorer`, fed the payload's inventory, the candidate's
repository/master/leaf identities, the caller-owned layout, full-file and open-path state and the
center's own open-path callback.

### Conventions

The module is one default-free file of small function components plus two private predicates
(`membersComplete`, `memberContextHeading`) and two private sentence builders (`missingRowNote`,
`memberContextCounts`) that are pure functions of the entry. It imports its family values from
`../../data/review` (the public entry that re-exports the mirror module), the shared roster
components and the `FamilySelection` type from `./FamilyTree`, the diff renderer from
`../changeset/DiffPane`, and `SourceExplorer` with its `DiffLayout` type from `./SourceExplorer` —
one implementation of each, never a second. Styling uses the `styled-system/css` `css` helper with
module-level constants (`shell`, `sectionLabel`, `card`, `muted`, `prose`, `rows`, `linkButton`),
matching the cockpit panels' idiom. Every list item and block carries a stable `key`
(`assessment.assessment_id`, `observation.observation_id`, `claim.claim_id`,
`${location.claim_id}:${location.path}`, the member revision) and a machine-readable `data-testid`,
with the owner's own values beside them where a case or a reader needs them (`data-revision`,
`data-family`, `data-family-state`, `data-side`, `data-binding`, `data-evidence-state`,
`data-change-state`, `data-fact`, `data-selection-kind`, `data-path`). Layout, full-file and
open-path state are owned by the caller and threaded down, so switching the diff layout while a file
is open is the caller's state change rather than this component's; the only state this file holds is
none at all.

### Invariants And Boundaries

- **One column, in the packet's order.** Guarantee and selected intent, then linked expressions, then
  execution evidence and authored assessment; the reader never has to reconstruct the route across
  tabs or a detached inspector.
- **The five independent facts stay independent.** The guarantee comparison, the member statement
  comparison, the membership/realization facts, the source attribution and the authored judgment are
  printed under their own headings from their own owners' values, and none of them is derived from
  another.
- **Only `unchanged_revision` may say the guarantee is unchanged.** `identical_text` records that a
  revision *was* authored between the two revisions, and `one_sided` records that no comparison was
  made at all.
- **A missing side is stated from that side's own state and its roster page's completeness.**
  `missingRowNote` may say the snapshot records no row only for a side whose roster was read whole
  (or which read no roster at all); a bounded walk's missing row is a page fact, never "the snapshot
  records no row".
- **No statement is rendered for a revision whose content this page did not carry.**
  `MemberStatement` prints the explicit not-carried line, and the `changed` branch mounts that line
  for whichever side lacked content instead of diffing against a blank.
- **"Complete" is a claim the page must earn.** `memberContextHeading` requires both the entry's own
  `recorded` state and every roster's own `complete` flag before it prints the complete heading.
- **The read owner's measured total is what is printed.** `memberContextCounts` sums the recorded
  sides' `members_total` and states this page's share of it as the page's share; a partial entry adds
  the continuation sentence.
- **Records are joined on the recorded join key and nothing else.** `EvidenceBlock` and
  `AttributedPaths` filter on the member's own `invariant_revision_id` (observations by
  `revision_id`, assessments by their `applicability.subject_revision_ids`), never on a label or a
  path.
- **A record of another subject is counted and named, not displayed.** `unjoined` states how many
  records belong to other subjects, because a record belongs to the review of the subject its own
  binding names.
- **An unresolved attribution is printed, never dropped.** `assessmentBlock` prints
  `author: unresolved reference` for an absent author.
- **No assessment is implied by a change.** The authored-judgment fact says how many assessments bind
  to the member revision and states that no member, membership or guarantee change creates one; an
  empty list is an absence of a recorded judgment, not a judgment that the member is fine.
- **The explorer below is not filtered by the selection.** `SourceExplorer` is mounted beneath the
  selected centre and beneath the unselected centre alike, over the payload's whole inventory, so the
  measured review population stays complete while the family navigation operates as an attribution
  lens.
- **Boundary.** This is a presentation component: it starts no request, writes nothing, resolves no
  candidate and owns no route. The one continuation control it mounts is the tree's own `RosterNext`,
  the one empty-roster sentence is the tree's own `emptyRosterSentence`, and the roster lines are the
  tree's own `RosterLine`, so the two columns cannot drift apart.

### Todos

None recorded. The centre renders what the payload and the owners' records carry; the two known
limits of the surrounding family route — the browser-class journeys and the state a served bundle
would have to exercise — belong to the read/refresh and interaction increments rather than to this
rendering.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the header's own statement of why the
column is central, of the five independent facts and of what the file refuses to do; the five
guarantee branches; the member statement, its not-on-page state and the missing-row note; the
one-sided sentence; the realization claims and the attributed paths joined on the member's own
revision identity; the evidence block with its unjoined count; the member-context heading and counts;
the five-fact strip; the two centre components; the root's three-way selection and the explorer it
mounts beneath; and the shared components and mount point it borrows. Every anchor in a row occurs
inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own statement of why ICR-R24 rejects the tab-switching reconstruction, that the five independent facts are owned by five separate modules, and that records are joined on `invariant_revision_id` with everything not joined counted rather than displayed.** | `ICR-R24@v3`; `invariant_revision_id` | dashboard/src/panels/review/FamilyReviewCenter.tsx:1-22 |
| The imports that fix the ownership: the family values from the public review entry, the shared diff renderer, the explorer and the shared roster components. | `guaranteeComparison`; `DiffPane`; `SourceExplorer` | dashboard/src/panels/review/FamilyReviewCenter.tsx:24-46 |
| One guarantee printed whole with the identities a reader needs to find it again, and the technical detail kept out of the reading path. | `GuaranteeBlock`; `state_at_origin`; `acceptance_ref` | dashboard/src/panels/review/FamilyReviewCenter.tsx:96-110 |
| **The five guarantee shapes as five sentences, with `unchanged_revision` the only one that may say the guarantee is unchanged and the diff mounted only for `changed`.** | `GuaranteeComparisonBlock`; `review-center-guarantee-unrecorded`; `review-center-guarantee-identical-text`; `review-center-guarantee-changed` | dashboard/src/panels/review/FamilyReviewCenter.tsx:112-188 |
| The member's authored identity line: label, version, exact revision identity and lifecycle. | `MemberIdentity`; `lifecycle` | dashboard/src/panels/review/FamilyReviewCenter.tsx:190-202 |
| The recorded facts beside a statement: applicability, essential conditions and exclusions, each printed only when the store has one. | `MemberFacts`; `essential_conditions`; `exclusions` | dashboard/src/panels/review/FamilyReviewCenter.tsx:204-221 |
| **`MemberStatement`: the only place a member's stored text is rendered, and the explicit not-carried state that prevents a missing statement from reading as an empty one.** | `MemberStatement`; `review-center-member-not-on-page` | dashboard/src/panels/review/FamilyReviewCenter.tsx:223-242 |
| **`missingRowNote`: the two answers about a missing side, only one of which is about the snapshot, decided from that side's own roster state and its page's completeness.** | `missingRowNote`; "bounded walk" | dashboard/src/panels/review/FamilyReviewCenter.tsx:244-261 |
| **`oneSidedStatement`: the note decided from each member's own state and the roster page's completeness rather than from the comparison kind, and the standing sentence that no comparison is drawn from one side's content.** | `oneSidedStatement`; "review-center-member-one-sided-note"; "no before/after comparison is drawn" | dashboard/src/panels/review/FamilyReviewCenter.tsx:263-298 |
| **`memberStatementBlock`: the four comparison kinds dispatched, with one-sided content stated rather than diffed against a blank.** | `memberStatementBlock`; `not_on_page`; `review-center-member-changed` | dashboard/src/panels/review/FamilyReviewCenter.tsx:300-343 |
| **`RealizationClaims`: the recorded claim identities, their roles, and the explicit no-address statement instead of an empty path.** | `RealizationClaims`; "this read observed no address for it"; "review-center-expressions" | dashboard/src/panels/review/FamilyReviewCenter.tsx:345-376 |
| **`AttributedPaths`: the source records joined on the member's own `invariant_revision_id`, the listed path becoming an open control, and the partial-inventory sentence that keeps absence from reading as a measurement.** | `AttributedPaths`; `listedPartial`; `review-center-open-path` | dashboard/src/panels/review/FamilyReviewCenter.tsx:378-442 |
| One execution observation with its result and the technical identities, each stated as not recorded when absent. | `observationBlock`; `execution_result` | dashboard/src/panels/review/FamilyReviewCenter.tsx:444-456 |
| One authored assessment: disposition, finding, rationale, attribution and binding state. | `assessmentBlock`; "unresolved reference"; `binding_state` | dashboard/src/panels/review/FamilyReviewCenter.tsx:458-472 |
| **`EvidenceBlock`: observations and assessments joined on the member's own revision identity, the two owner states printed, and the unjoined records counted and named rather than displayed.** | `EvidenceBlock`; `subject_revision_ids`; `review-center-unjoined`; `data-evidence-state` | dashboard/src/panels/review/FamilyReviewCenter.tsx:474-528 |
| **`UnselectedCenter`: the explorer below is the whole measured review population and is not filtered by the selection, because the family navigation is an attribution lens rather than an exclusion filter.** | `UnselectedCenter`; "not filtered by this selection" | dashboard/src/panels/review/FamilyReviewCenter.tsx:530-545 |
| The completeness predicate both this file and the tree use: every roster page absent or complete. | `membersComplete`; `page.complete` | dashboard/src/panels/review/FamilyReviewCenter.tsx:547-554 |
| **`memberContextHeading`: "Complete recorded member context" only when the entry's own state is `recorded` and every roster is complete.** | `memberContextHeading`; "Complete recorded member context" | dashboard/src/panels/review/FamilyReviewCenter.tsx:556-564 |
| **`memberContextCounts`: the read owner's measured `members_total` across the recorded sides, this page's share stated as a share, and the continuation sentence only for a partial entry.** | `memberContextCounts`; `members_total`; "the continuations beside the bounded rosters reach the rest" | dashboard/src/panels/review/FamilyReviewCenter.tsx:566-579 |
| **`FamilyCenter`: one family's guarantee comparison and its member context, reusing the tree's own roster line, empty-roster sentence and continuation control.** | `FamilyCenter`; `review-center-member-heading`; `review-center-roster-next` | dashboard/src/panels/review/FamilyReviewCenter.tsx:581-658 |
| **`IndependentFacts`: the five independent facts, each from its own owner's value, so a member change cannot read as a guarantee revision or an assessment.** | `IndependentFacts`; `data-fact="membership"`; `data-fact="assessment"` | dashboard/src/panels/review/FamilyReviewCenter.tsx:660-731 |
| **`MemberCenter`: the member reading path in the packet's order, with the family context retained above the member and the continuation reachable from here too.** | `MemberCenter`; "Selected intent"; "Linked expressions"; "Execution evidence and authored assessment" | dashboard/src/panels/review/FamilyReviewCenter.tsx:733-798 |
| **The root: the three-way selection resolution, `data-selection-kind`, the two centres, and `SourceExplorer` mounted beneath either one over the payload's whole inventory.** | `FamilyReviewCenter`; `data-selection-kind`; `SourceExplorer` | dashboard/src/panels/review/FamilyReviewCenter.tsx:800-875 |
| **The shared components this file mounts rather than re-declares: the tree's roster line, its continuation control and its one empty-roster sentence.** | `RosterLine`; `RosterNext`; `emptyRosterSentence` | dashboard/src/panels/review/FamilyTree.tsx:232-232; dashboard/src/panels/review/FamilyTree.tsx:324-324; dashboard/src/panels/review/FamilyTree.tsx:284-284 |
| The explorer implementation the centre mounts beneath the reading path. | "export function SourceExplorer" | dashboard/src/panels/review/SourceExplorer.tsx:234-234 |
| The workspace mount that resolves the selection and threads the layout, full-file and open-path state into the centre. | "<FamilyReviewCenter" | dashboard/src/panels/review/ReviewWorkspace.tsx:317-330 |
| The case that pins the retained family context and the five separately stated facts on member selection. | "keeps the family context when a member is selected and states the five facts separately" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:228-228 |
| The case that pins the bounded member-context heading and the owner's row count rather than this page's. | "heads a bounded member context partial and counts the owner's rows, not this page's" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:463-463 |
| The cases that pin a listed-but-uncarried row and a bounded page's missing row as page facts, never as "the snapshot records no row". | "says a listed-but-uncarried row about the page, never that the snapshot records no row"; "says a bounded page's missing row about the page, never that the snapshot records none" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:541-541; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:589-589 |
| The case that pins two distinct revisions with identical text against one unchanged revision. | "distinguishes two distinct revisions with identical text from one unchanged revision" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:499-499 |
| The case that pins a member whose content the page did not carry against a one-sided statement. | "states a member whose content the page did not carry as that, not as a one-sided statement" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:522-522 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It renders records of one repository
namespace from a payload the server composed, and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the unified central reading path. It records that the centre renders the family guarantee and the selected intent, then the linked expressions, then the execution evidence and authored assessment in one column; that `missingRowNote()` decides what may be said about a missing side from that side's own roster state and its roster page's completeness — a bounded walk's missing row is a page fact and never "the snapshot records no row"; that `oneSidedStatement()` decides its note from each member's own state rather than from the comparison kind; that `memberContextHeading()` prints "Complete recorded member context" only when the entry's own state is `recorded` and every roster page is complete; that `memberContextCounts()` prints the read owner's measured `members_total` with this page's share stated as a share; that `IndependentFacts` prints the five independent facts from their own owners' values; that `EvidenceBlock` joins records on the member's own `invariant_revision_id` and counts-and-names the unjoined records instead of displaying them; and that `FamilyReviewCenter` mounts `SourceExplorer` beneath the reading path so the measured population is never filtered by the selection. Every row of the reference table was derived against this leaf's candidate, and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
