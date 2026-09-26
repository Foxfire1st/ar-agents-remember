# dashboard/src/panels/review/FamilyReviewCenter.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/FamilyReviewCenter.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T03:00:00+02:00 |
| lastVerifiedCommitHash | `1fa2588a048e14f6aff236b896caa32d3a7f26c7` |
| lastVerifiedCommitDate | 2026-09-26T04:04:54+02:00|
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

**The two selection shapes are two different routes through the same column, and both of them are
complete (260921-ICR-L36).** A **member** selection runs guarantee → selected intent → linked expressions
→ execution evidence and authored assessment. A **family** selection runs guarantee → the complete
recorded member context → **the family's changed expression excerpts, deduplicated** → the shared source
explorer. The family column used to compose only the first two of its three parts, so a reader who
selected a whole family saw no expressions at all; the accepted design's whole-family line asks for three
things ("Whole-family selection presents the full guarantee, all members including the unchanged sibling,
and deduplicated changed expression excerpts") and the family column now presents all three, in that
order, before the explorer every selection shares.

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
`resolution`. A path that is not listed carries one of two sentences, and since 260921-ICR-L36 those two
sentences come from **one owner**, `unlistedPathNote(listedPartial)` (`:379-386`): when the inventory is
partial, that absence from its list is not a measurement that the path did not change; otherwise, that the
path is not a changed path of the comparison's measured change set. `AttributedPaths` used to spell both
sentences inline; the family-level excerpt collection needs the same two facts about the same path, and two
copies could drift into disagreeing about one path, so the sentences were hoisted and both readers call the
one function. `listedOrPlainPath(path, onOpenPath, listed)` (`:954-969`) is the second hoist from the same
change: the address is a `review-center-open-path`/`review-center-family-expression-open` control when the
explorer lists it and plain `<code>` when it does not, one shape for both readers. The location's
`rationale` and its `reached_via` paths follow when the record has them.

**A4's collection: the family's changed expression excerpts, deduplicated, and the decisions in it
(`:571-1043`; 260921-ICR-L36, F1 fix round included).** The family column's third part.
`carriedMembership(entry)` (`:654-663`) flattens the entry's two sides into `FamilyMembershipRow[]` — the
side and the member revision it records — and `familyExpressionExcerpts(membership)` (`:845-862`) is the
whole arithmetic: a three-way partition of every claim, a collapse by excerpt identity, and the counts the
verdict renders.

- **What "changed" is, and what it deliberately is not.** `claimClass` (`:719-727`) partitions the read's
  own `resolution` exactly the way `AttributedPaths`' owner already partitions it: `exact_recorded_blob` is
  **resolved** (`RESOLVED_ADDRESSES`, `:634`); `recorded_blob_mismatch`, `path_absent`,
  `unsupported_locator` and `entry_not_blob` are the collection's **rows**; and
  `recorded_object_unavailable` and `not_requested` (`UNMEASURED_ADDRESSES`, `:635-638`) are **not
  measured** — counted apart and never called a change, because "never asked" and "different bytes" are
  different facts. A claim carrying no address at all is a non-measurement too, since the server refuses an
  address without a resolution. The module's own header states the consequence the reader must not miss:
  this is the **realization resolution**, not the comparison's own measured change set, which the explorer
  below reports separately, and on the served family the two disagree in the direction that matters.
- **The dedup key is the address together with the *recorded* source identity — the observed identity is
  deliberately NOT in it, and that is the F1 repair** (`excerptKey`, `:712-717`: `` `${path}\u0000${recorded}` ``).
  The prototype's key is the excerpt's address (`path + ':' + start`); the claims this surface receives
  carry no line range of their own (the range lives inside the read's own `detail` sentence), so the
  identity used is the path together with the **recorded** bytes. Two claims at one path whose recorded
  bytes differ are two excerpts and stay two rows — **that is the only thing keeping over-collapse out, and
  the verifier's over-collapse probe found none.** The observed identity is what the read *found* at the
  address in one side's tree, so a divergent address has **one observed value per side**; folding it into
  the key split that one address into two keys — one per side — and the pass that pairs the sides could
  never find the other one, which is exactly why the shipped row printed a single side. The module's header
  records that measurement under its own heading ("WHY THE OBSERVED IDENTITY IS NOT PART OF THE KEY,
  MEASURED").
- **The collection is built from the carried membership rows and not from the centre's first-wins `distinct`
  list, and that is measured rather than stylistic.** The centre's `distinct` list keeps the first member
  row per revision (before wins), which is safe for printing a statement and **unsafe for a resolution**,
  because a resolution is a fact about the address **in one side's tree**. The captured
  `familyReview.walkFinal` body records member revision `d24e5187…` with `src/batch.py` under recorded blob
  `353df144…`, which the before snapshot resolves as `exact_recorded_blob` and the after snapshot as
  `recorded_blob_mismatch`; a collection built from `distinct` would have presented that address as resolved
  and hidden the change this review exists to show.
- **`recordSideReadings` (`:804-827`) is the second pass, and it now carries a read result per side rather
  than a resolution per side.** It walks every claim of every carried row, finds the excerpt by the same
  `excerptKey`, and gathers into that excerpt's `readingsBySide` **both** the resolutions that side's read
  gave the address **and** the observed identities it found there (`FamilyExcerptSideReading`, `:671-680`).
  Both fields are read results and neither is identity, which is why they live per side and not in the key.
  `orderExcerpts` (`:829-843`) sorts the sides in the family's own order and sorts each side's observed
  identities, so the rendering is deterministic.
- **One row per excerpt, naming every membership row that recorded it.** `absorbClaim` (`:739-773`) folds a
  changed claim into its excerpt and records an occurrence keyed by side **and** revision, so two claims of
  one membership row are one occurrence while the same revision on both sides is two. The revision identity
  is printed beside the label (`occurrenceName`, `:975-982`) because a display label alone is not enough and
  the served family proves it: `ICR30-I-1` is recorded as **two** member revisions of its family, so
  "ICR30-I-1 (before)" twice would name two different rows identically.

**`familyExpressionVerdict` is the sentence the collection leads with, built from the arithmetic so the
reader never adds rows up** (`:864-909`). It states the collapse (`N changed expression row(s) across the
family's M carried membership row(s) (before x + after y; R distinct member revision(s)) collapse to K
distinct excerpt(s)`, with the removed count named as rows that named an address and recorded bytes another
row already named), the membership split (how many carried rows recorded a change and how many recorded
none, with the sentence that the roster above keeps all of them), the **notion** it counted — the
realization resolution, with the stale and unresolved state names — and the unmeasured count, which says
`no claim was left unmeasured.` at zero rather than staying silent. **The F1 repair replaced the notion
sentence's clause outright, and the F-V1-3 reword then replaced it again. The page's current sentence is the
one a reader may quote:** *"every row below prints what each side's read made of its address — the resolution
that side's claim carried — so an address both sides carried prints both readings whenever they differ, and
an address only one side carried prints that side's alone."* **The superseded wording must not be quoted**
(F-V1-3, low): it read *"every row below names the resolution of each side whose read resolved its address's
recorded bytes…"*, and the phrase *"resolved its address's recorded bytes"* **collided with the product's own
name for `exact_recorded_blob`** — true under the reading the code implements, **false under the literal
reading on every live row**, where the changed sides are `recorded_blob_mismatch` and have not "resolved"
their recorded bytes. The reword removes the collision by naming the reading explicitly ("the resolution that
side's claim carried"), and the fix verifier asserted the row-by-row behaviour on the rendered page. With no
rows at all it says the collection is empty because every addressed claim carried here resolved to its
recorded bytes, and it points at the roster above and at what selecting an unchanged member shows.

**`FamilyExpressionRow` (`:911-973`) and `FamilyExpressionExcerpts` (`:1001-1043`) render that arithmetic,
and row two is `FamilyExpressionRow`** — the address as a control or as plain code, the role(s), **each
side's resolutions** (`readingsBySide`), the carried membership rows that recorded it with the revision
identity beside each label, the recorded identity, **the observed identity per side** (printed as
`not observed` when that side's read found no address at all), the read's own `detail` sentences, the
collapsed-row count, and where the address stands in the comparison's own change set (a listed path says it
is a changed path of that set; an unlisted one gets `unlistedPathNote`). The card's machine-checkable half is
on the row: `data-path`, `data-dedup-key`, `data-collapsed-rows`, `data-membership-rows`,
`data-member-revisions` and `data-sides`, so the collapse is checkable from the DOM record without trusting
the sentence. The card carries a measured-empty sentence behind `review-center-family-expressions-none` for
the family whose carried rows recorded nothing, which says the emptiness is measured rather than missing.

**The honest bound on the divergent rendering, which a reader must carry with it.** The divergent case is
evidenced against the **captured `familyReview.walkFinal` body through a labelled fixture** — measured on the
fix round's build as `before exact_recorded_blob · after recorded_blob_mismatch`, with `data-sides =
"before,after"` — and the label is not decoration: **it is the only place the divergence is exercised.**
Live data was searched, and **the search reached 3 families served by 1 leaf** (`260921-ICR-L34`, which
returns `entries` with 3 families). The other **35 leaves refused `candidate_dataset_absent`** — each records
no comparison generation, so no knowledge operand exists for a subject to be listed from — and therefore
**carry nothing to search. Absent is not measured:** those 35 were not searched and found clean; they were
unreachable, and a family that cannot be listed cannot be shown to be divergence-free. **`260921-ICR-L36` is
one of those 35**, so this leaf's own live data carries no divergent family either. Read from the fix round's
`f1/raw/live-truth.json` and reproduced independently by the verifier in `f1v/raw/vf1-live-scan.json`
(`leavesAttempted: 36`, `leavesResolved: 1`, `leavesRefused: 35`, `refusalCodes:
["candidate_dataset_absent"]`, `familiesServed: 3`, `familiesExamined: 3`, `familiesWithDivergence: 0`,
`totalDivergent: 0`). The live family renders the same 2 excerpts as before, and no part of this card may be
read as a claim that live data exercises the divergent path.

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

**`FamilyMemberContext` (`:1048-1111`) is the family's complete recorded member context, and it reuses the
tree's own components.** It was extracted from `FamilyCenter` unchanged by 260921-ICR-L36 so the family
column reads as the three things it composes — guarantee, member context, expressions — rather than as one
function that happens to contain two of them. It renders the heading from `memberContextHeading`, the counts
from `memberContextCounts(entry, distinct.length)`, the distinct-member sentence, the two per-side
`RosterLine`s (mounted with `testid="review-center-roster"`), one `review-center-open-member` control per
distinct member with its stored statement or its explicit not-carried line, the `emptyRosterSentence` behind
`review-center-family-empty` when no distinct member exists, and the `RosterNext` continuation control with
`testid="review-center-roster-next"` — the same cursor and the same handler the tree uses. **The extraction
is a move and not a rewrite, and it is measured:** the mounted cases that read the heading, the counts, the
roster lines and the continuation out of the family selection are unchanged by it.

**`FamilyCenter` (`:1113-1163`) is one family's context in the central reading path, and it composes exactly
three things.** It computes the distinct member revisions of the page by folding `entry.before.members` and
`entry.after.members` into a `Map` keyed by `invariant_revision_id` — a first-wins list that is right for
printing statements and wrong for resolutions, which is why the excerpt collection below does **not** read it
— then renders the family heading with the entry's own state and selection lines (`selection.state` and its
`statement`), `GuaranteeComparisonBlock`, `FamilyMemberContext` over that distinct list, and then
`FamilyExpressionExcerpts` over `carriedMembership(entry)`. The composition order is the accepted design's
`README.md:23` ("lead with its own guarantee comparison and complete member context, then relevant
expressions"), and it is asserted by the mounted case that reads the collection's place between the member
context and the explorer every selection shares. A3's **member** order is untouched by it.

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

The module is one default-free file of small function components plus private predicates
(`membersComplete`, `memberContextHeading`), private sentence builders (`missingRowNote`,
`memberContextCounts`, `familyExpressionVerdict`) and private pure helpers (`unlistedPathNote`,
`carriedMembership`, `excerptKey`, `claimClass`, `absorbClaim`, `tallyChangedExcerpts`,
`recordSideResolutions`, `orderExcerpts`, `occurrenceName`, `listedOrPlainPath`) that are pure functions of
their arguments. Its **exported surface is deliberately three names wide and one of them is the arithmetic
alone** — `familyExpressionExcerpts`, `FamilyMembershipRow`, and the `FamilyExcerptOccurrence` /
`FamilyExpressionExcerpt` / `FamilyExpressionCollection` result types — because the unit lane
(`familyExpressions.test.ts`) holds the arithmetic without a DOM while the mounted lane holds the rendering
over captured bodies. `carriedMembership`, `excerptKey` and `claimClass` stay private helpers even though a
test could reach them, so the arithmetic has one entry point. It imports its family values from
`../../data/review` (the public entry that re-exports the mirror module), the shared roster
components and the `FamilySelection` type from `./FamilyTree`, the diff renderer from
`../changeset/DiffPane`, and `SourceExplorer` with its `DiffLayout` type from `./SourceExplorer` —
one implementation of each, never a second. Styling uses the `styled-system/css` `css` helper with
module-level constants (`shell`, `sectionLabel`, `card`, `muted`, `prose`, `rows`, `linkButton`),
matching the cockpit panels' idiom. Every list item and block carries a stable `key`
(`assessment.assessment_id`, `observation.observation_id`, `claim.claim_id`,
`${location.claim_id}:${location.path}`, the member revision, and the excerpt's own dedup `key`) and a
machine-readable `data-testid`, with the owner's own values beside them where a case or a reader needs them
(`data-revision`, `data-family`, `data-family-state`, `data-side`, `data-binding`, `data-evidence-state`,
`data-change-state`, `data-fact`, `data-selection-kind`, `data-path`, and on each excerpt row the
arithmetic itself: `data-dedup-key`, `data-collapsed-rows`, `data-membership-rows`, `data-member-revisions`,
`data-sides`). Layout, full-file and open-path state are owned by the caller and threaded down, so switching
the diff layout while a file is open is the caller's state change rather than this component's; the only
state this file holds is none at all.

### Invariants And Boundaries

- **One column, in the packet's order — and the family column's order has three parts, not two.**
  Guarantee and selected intent, then linked expressions, then execution evidence and authored assessment
  for a **member** selection; guarantee, then the complete recorded member context, then the deduplicated
  changed expression excerpts, then the shared explorer for a **family** selection. The reader never has to
  reconstruct the route across tabs or a detached inspector, and a family selection no longer stops after
  the roster (260921-ICR-L36).
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
- **The empty column speaks for itself and not for the screen.** `UnselectedCenter`'s first sentence
  names the plane — a family or member has not been **chosen in this column** yet — and its second
  states that the composition above is unaffected by that: the header reports which family contexts
  the review composed and the tree reports the family revision and roster page the server selected,
  and neither is a choice made here (260921-ICR-L25, register B3). The word "selected" belongs to the
  server's vocabulary on this screen, so the column must not borrow it for its own state; the
  measured discriminator is this component's own `data-selection-kind`, which is `none` before any
  choice and `family`/`member` after one.
- **The excerpt collection counts the realization resolution, and it says which notion it counted.**
  `exact_recorded_blob` is the resolved state, the four unresolved states are its rows, and
  `recorded_object_unavailable` / `not_requested` are counted apart and never called a change. It is
  **not** the comparison's own measured change set, the two disagree on the served family, and the verdict
  sentence plus every row states which of the two is being read.
- **The dedup key is the address together with the recorded and observed source identities, never the path
  alone.** Two recorded blobs at one path stay two excerpts; two rows that named one address and one blob
  pair collapse into one excerpt that names every membership row that recorded it.
- **A resolution is a per-side fact, so the collection reads the carried membership rows and carries each
  side's reading separately.** The centre's first-wins `distinct` list is right for statements and wrong for
  resolutions: the captured `walkFinal` body resolves one address on `before` and mismatches it on `after`,
  and a `distinct`-built collection would have shown it as resolved. `recordSideReadings` carries each side's
  resolutions **and** observed identities in `readingsBySide`, and the row prints them per side.
- **The observed identity is a read result, never part of the excerpt's identity, and that is what makes the
  pairing possible.** `excerptKey` is `path \0 recorded`; a divergent address has one observed value per
  side, so keying by it would split the address into two excerpts that can never be paired (F1). The recorded
  identity stays in the key because it is the only thing that keeps two different recorded blobs at one path
  apart — removing it would be over-collapse.
- **The divergent path is fixture-backed and is labelled so.** Live data was searched: **3 families served by
  1 leaf** (`260921-ICR-L34`), **0 divergent addresses**, while the other **35 leaves refused
  `candidate_dataset_absent`** and so carried nothing to search. **Absent is not measured** — 35 leaves were
  unreachable, not found clean, and **this leaf (`260921-ICR-L36`) is one of them.** The divergent rendering
  is therefore evidenced only against the captured `familyReview.walkFinal` body through a labelled fixture,
  and neither this card nor the page may imply that live data exercises it.
- **One excerpt row names every membership row that recorded it, with the revision identity beside the
  label.** A display label alone is not a key and the served family proves it: `ICR30-I-1` is recorded as two
  member revisions, so a label-only row would name two different rows identically.
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
the five-fact strip; the two centre components; A4's collection with its partition, its dedup key, its
two passes and its verdict (**260921-ICR-L36**); the root's three-way selection and the explorer it
mounts beneath; and the shared components and mount point it borrows. Every anchor in a row occurs
inside the range that row cites. The three rows reaching into `ReviewWorkspace.family.test.tsx` and
`familyExpressions.test.ts` are the cases this leaf added for the collection.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own statement of why ICR-R24 rejects the tab-switching reconstruction, that the five independent facts are owned by five separate modules, and that records are joined on `invariant_revision_id` with everything not joined counted rather than displayed.** | `ICR-R24@v3`; `invariant_revision_id` | dashboard/src/panels/review/FamilyReviewCenter.tsx:1-22 |
| The imports that fix the ownership: the family values from the public review entry, the shared diff renderer, the explorer and the shared roster components. | `guaranteeComparison`; `DiffPane`; `SourceExplorer` | dashboard/src/panels/review/FamilyReviewCenter.tsx:24-47 |
| One guarantee printed whole with the identities a reader needs to find it again, and the technical detail kept out of the reading path. | `GuaranteeBlock`; `state_at_origin`; `acceptance_ref` | dashboard/src/panels/review/FamilyReviewCenter.tsx:97-111 |
| **The five guarantee shapes as five sentences, with `unchanged_revision` the only one that may say the guarantee is unchanged and the diff mounted only for `changed`.** | `GuaranteeComparisonBlock`; `review-center-guarantee-unrecorded`; `review-center-guarantee-identical-text`; `review-center-guarantee-changed` | dashboard/src/panels/review/FamilyReviewCenter.tsx:113-189 |
| The member's authored identity line: label, version, exact revision identity and lifecycle. | `MemberIdentity`; `lifecycle` | dashboard/src/panels/review/FamilyReviewCenter.tsx:191-203 |
| The recorded facts beside a statement: applicability, essential conditions and exclusions, each printed only when the store has one. | `MemberFacts`; `essential_conditions`; `exclusions` | dashboard/src/panels/review/FamilyReviewCenter.tsx:205-222 |
| **`MemberStatement`: the only place a member's stored text is rendered, and the explicit not-carried state that prevents a missing statement from reading as an empty one.** | `MemberStatement`; `review-center-member-not-on-page` | dashboard/src/panels/review/FamilyReviewCenter.tsx:224-243 |
| **`missingRowNote`: the two answers about a missing side, only one of which is about the snapshot, decided from that side's own roster state and its page's completeness.** | `missingRowNote`; "bounded walk" | dashboard/src/panels/review/FamilyReviewCenter.tsx:245-262 |
| **`oneSidedStatement`: the note decided from each member's own state and the roster page's completeness rather than from the comparison kind, and the standing sentence that no comparison is drawn from one side's content.** | `oneSidedStatement`; "review-center-member-one-sided-note"; "no before/after comparison is drawn" | dashboard/src/panels/review/FamilyReviewCenter.tsx:264-299 |
| **`memberStatementBlock`: the four comparison kinds dispatched, with one-sided content stated rather than diffed against a blank.** | `memberStatementBlock`; `not_on_page`; `review-center-member-changed` | dashboard/src/panels/review/FamilyReviewCenter.tsx:301-344 |
| **`RealizationClaims`: the recorded claim identities, their roles, and the explicit no-address statement instead of an empty path.** | `RealizationClaims`; "this read observed no address for it"; "review-center-expressions" | dashboard/src/panels/review/FamilyReviewCenter.tsx:346-377 |
| **`AttributedPaths`: the source records joined on the member's own `invariant_revision_id`, the listed path becoming an open control, and the partial-inventory sentence that keeps absence from reading as a measurement — now read from the two shared owners (`unlistedPathNote`, `listedOrPlainPath`) that the family-level collection also calls, so the two readers cannot drift into disagreeing about one path (260921-ICR-L36).** | `AttributedPaths`; `listedPartial`; `review-center-open-path` | dashboard/src/panels/review/FamilyReviewCenter.tsx:388-448 |
| One execution observation with its result and the technical identities, each stated as not recorded when absent. | `observationBlock`; `execution_result` | dashboard/src/panels/review/FamilyReviewCenter.tsx:450-462 |
| One authored assessment: disposition, finding, rationale, attribution and binding state. | `assessmentBlock`; "unresolved reference"; `binding_state` | dashboard/src/panels/review/FamilyReviewCenter.tsx:464-478 |
| **`EvidenceBlock`: observations and assessments joined on the member's own revision identity, the two owner states printed, and the unjoined records counted and named rather than displayed.** | `EvidenceBlock`; `subject_revision_ids`; `review-center-unjoined`; `data-evidence-state` | dashboard/src/panels/review/FamilyReviewCenter.tsx:480-534 |
| **`UnselectedCenter`: the empty column names the plane its own sentence is about — "No family or member has been chosen **in this column** yet" — and states that the explorer below is the whole measured review population and is not filtered by any choice made here, because the family navigation is an attribution lens rather than an exclusion filter. (260921-ICR-L25, register B3: the earlier sentence read "No family or member is selected", which collided with the server's own "selected" — the scope header's composed-context count and the tree's "this review selected \<revision\>" — so a reader comparing the two read a contradiction that was a collision of vocabularies. The component is accurate about its own state, measured: `data-selection-kind` is `none` here and no tree row carries `aria-current` until the reader chooses.)** | `UnselectedCenter`; "has been chosen in this column yet"; "not filtered by any choice made here" | dashboard/src/panels/review/FamilyReviewCenter.tsx:536-569 |
| The completeness predicate both this file and the tree use: every roster page absent or complete. | `membersComplete`; `page.complete` | dashboard/src/panels/review/FamilyReviewCenter.tsx:1044-1051 |
| **`memberContextHeading`: "Complete recorded member context" only when the entry's own state is `recorded` and every roster is complete.** | `memberContextHeading`; "Complete recorded member context" | dashboard/src/panels/review/FamilyReviewCenter.tsx:1053-1061 |
| **`memberContextCounts`: the read owner's measured `members_total` across the recorded sides, this page's share stated as a share, and the continuation sentence only for a partial entry.** | `memberContextCounts`; `members_total`; "the continuations beside the bounded rosters reach the rest" | dashboard/src/panels/review/FamilyReviewCenter.tsx:1063-1076 |
| **`FamilyMemberContext`: the family's complete recorded member context, extracted from `FamilyCenter` unchanged so the family column reads as the three things it composes, still reusing the tree's own roster line, empty-roster sentence and continuation control (260921-ICR-L36).** | `FamilyMemberContext`; `review-center-member-heading`; `review-center-roster-next` | dashboard/src/panels/review/FamilyReviewCenter.tsx:1078-1141 |
| **`FamilyCenter`: one family's guarantee comparison, its complete recorded member context and its changed expression excerpts, in the accepted design's order, over the first-wins distinct list for the roster and over the carried membership rows for the collection.** | `FamilyCenter`; `FamilyMemberContext`; `FamilyExpressionExcerpts`; `carriedMembership` | dashboard/src/panels/review/FamilyReviewCenter.tsx:654-663; dashboard/src/panels/review/FamilyReviewCenter.tsx:1001-1043; dashboard/src/panels/review/FamilyReviewCenter.tsx:1078-1141; dashboard/src/panels/review/FamilyReviewCenter.tsx:1143-1193 |
| **`IndependentFacts`: the five independent facts, each from its own owner's value, so a member change cannot read as a guarantee revision or an assessment.** | `IndependentFacts`; `data-fact="membership"`; `data-fact="assessment"` | dashboard/src/panels/review/FamilyReviewCenter.tsx:1195-1266 |
| **`MemberCenter`: the member reading path in the packet's order, with the family context retained above the member and the continuation reachable from here too.** | `MemberCenter`; "Selected intent"; "Linked expressions"; "Execution evidence and authored assessment" | dashboard/src/panels/review/FamilyReviewCenter.tsx:1268-1334 |
| **The root: the three-way selection resolution, `data-selection-kind`, the two centres, and `SourceExplorer` mounted beneath either one over the payload's whole inventory.** | `FamilyReviewCenter`; `data-selection-kind`; `SourceExplorer` | dashboard/src/panels/review/FamilyReviewCenter.tsx:1336-1419 |
| **A4's module-level statement of why the collection exists, what a changed expression is and is not, and what the dedup key is: the accepted design's three-part whole-family line, the realization resolution against the comparison's own measured change set, and the address-together-with-the-RECORDED-identity key with its own heading stating why the observed identity is deliberately absent (260921-ICR-L36, F1 fix round).** | "A4: THE FAMILY'S CHANGED EXPRESSION EXCERPTS, DEDUPLICATED"; "Whole-family selection presents the full guarantee"; "recorded_blob_mismatch" | dashboard/src/panels/review/FamilyReviewCenter.tsx:571-632 |
| **The two states the collection does not call changes: the resolved state, and the two observations nobody made, counted apart.** | `RESOLVED_ADDRESSES`; `UNMEASURED_ADDRESSES`; `recorded_object_unavailable`; `not_requested` | dashboard/src/panels/review/FamilyReviewCenter.tsx:634-638 |
| **The hoisted sentence pair the member attribution and the family collection both read, so two copies cannot drift into disagreeing about one path.** | "function unlistedPathNote"; "this path is not among the paths this inventory listed" | dashboard/src/panels/review/FamilyReviewCenter.tsx:379-386 |
| **A carried membership row is a side and the member revision it records, and the collection is built from those rows rather than from the centre's first-wins `distinct` list — because a resolution is a fact about one side's tree.** | `export interface FamilyMembershipRow`; "function carriedMembership"; "side: ReviewFamilySideName" | dashboard/src/panels/review/FamilyReviewCenter.tsx:640-663 |
| **The excerpt's shape: the dedup key it exposes, the address, the recorded identity, each side's own reading in `readingsBySide` (its resolutions and the observed identities it found), the roles and read sentences that were merged, and the membership rows that recorded it.** | `export interface FamilyExpressionExcerpt`; `readingsBySide`; `FamilyExcerptSideReading`; `FamilyExcerptOccurrence`; `FamilyExpressionCollection`; `membershipRowsWithChanged` | dashboard/src/panels/review/FamilyReviewCenter.tsx:665-710 |
| **The dedup key: the address together with the RECORDED source identity, and the observed identity deliberately absent from it — keeping `recorded` is what stops over-collapse, and dropping `observed` is what lets a divergent address's two sides share one excerpt (260921-ICR-L36, F1).** | "function excerptKey"; `recorded_source_identity` | dashboard/src/panels/review/FamilyReviewCenter.tsx:712-717 |
| **The three-way class of one claim, including the address-less claim the server refuses an address for, which is a non-measurement and not a change.** | "function claimClass"; "unmeasured" | dashboard/src/panels/review/FamilyReviewCenter.tsx:719-737 |
| **One changed claim folded into its excerpt: the merged row keeps every role, every read sentence and every membership row that named it, with the occurrence keyed by side and revision so two claims of one row are one occurrence.** | "function absorbClaim"; `occurrenceKey` | dashboard/src/panels/review/FamilyReviewCenter.tsx:739-773 |
| **Pass one and pass two of the arithmetic, and the deterministic order every collection is served in: the changed claims collapsed by identity, then each side's resolutions AND observed identities recorded per side (`readingsBySide`) so a row can say its two operands disagree, then sides, each side's observed identities, roles, occurrences and excerpts ordered from their own values.** | "function tallyChangedExcerpts"; "function recordSideReadings"; "function orderExcerpts" | dashboard/src/panels/review/FamilyReviewCenter.tsx:775-843 |
| **The collection's one exported entry point and the counts it carries: excerpt rows, changed rows, carried membership rows, both sides' row counts, the rows with and without a change, distinct revisions, and the resolved and unmeasured claims.** | `familyExpressionExcerpts`; `distinctRevisions`; `membershipRowsWithoutChanged` | dashboard/src/panels/review/FamilyReviewCenter.tsx:845-862 |
| **The verdict sentence, built from the arithmetic so the reader never adds rows up: the collapse with the removed count named, the membership split, the notion it counted with the F1 repair's REWORDED per-side clause (quoted in the Logic section above), and the unmeasured count — which says `no claim was left unmeasured.` at zero rather than staying silent.** | "function familyExpressionVerdict"; "no claim was left unmeasured"; "changed expression row(s) across the family's" | dashboard/src/panels/review/FamilyReviewCenter.tsx:864-909 |
| **One excerpt row and the two helpers it shares with the member attribution: the address as a control or as plain code, the roles, each side's resolutions, every membership row that recorded it with the revision identity beside its label, the recorded identity, the observed identity printed PER SIDE (with `not observed` where a side's read found no address), and where the address stands in the comparison's own change set.** | "function FamilyExpressionRow"; `data-dedup-key`; `data-collapsed-rows`; "not observed"; "function occurrenceName"; "function listedOrPlainPath" | dashboard/src/panels/review/FamilyReviewCenter.tsx:911-999 |
| **The family column's third card: its heading (a REWORDING of the accepted prototype's kicker, not the prototype's own words — the prototype's section is headed `"Changed expressions in this family"` and the shipped heading is `"Changed expression excerpts in this family"`; the independent verifier measured the difference), the verdict, one row per distinct excerpt, and the measured-empty sentence that says the emptiness was measured rather than missing.** | "function FamilyExpressionExcerpts"; "Changed expression excerpts in this family"; `review-center-family-expressions-none` | dashboard/src/panels/review/FamilyReviewCenter.tsx:1001-1043 |
| **The mounted case for A4's collection over the real captured family body, fix round included: the rendered count is the distinct set and not the row count, every row's collapse count is the body's own group size, the verdict names the notion and the collapse, and EVERY rendered row's `data-sides` is checked against the sides the body resolves it on — the page's own both-sides sentence verified row by row against the body rather than read from the page.** | "renders the family's changed expression excerpts, deduplicated, over the captured family"; `review-center-family-expressions`; `review-center-family-expression-resolution`; `dataset.sides` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:735-803 |
| **The arithmetic that case's expectation is read from, computed from the captured body alone rather than imported from the component, so the assertion is checked against the body and not against the implementation it tests. It computes the fixed excerpt key (`path \0 recorded`), the per-side resolution sets the divergent predicate compares, and the side list every rendered row is checked against.** | "function familyExpressionArithmetic"; `divergent`; `groups`; "the captured body records no changed expression in any family" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:805-903 |
| **The unit lane that holds the same arithmetic without a DOM, states which of its inputs are constructed, and carries the pair of cases that state the whole key contract (recorded keeps two blobs at one path apart; observed may not, because two sides of one address legitimately see different bytes).** | "WHY THIS FILE ASSEMBLES ITS OWN PAYLOAD"; `familyExpressionExcerpts`; "collapses two member revisions that record one address"; "partitions the read's own resolutions"; "treats two different observed blobs at one address as one excerpt" | dashboard/src/panels/review/familyExpressions.test.ts:1-298 |
| **The shared components this file mounts rather than re-declares: the tree's roster line, its continuation control and its one empty-roster sentence.** | `RosterLine`; `RosterNext`; `emptyRosterSentence` | dashboard/src/panels/review/FamilyTree.tsx:246-280; dashboard/src/panels/review/FamilyTree.tsx:338-369; dashboard/src/panels/review/FamilyTree.tsx:298-317 |
| The explorer implementation the centre mounts beneath the reading path. | "export function SourceExplorer" | dashboard/src/panels/review/SourceExplorer.tsx:246-246 |
| The workspace mount that resolves the selection and threads the layout, full-file and open-path state into the centre. | "<FamilyReviewCenter" | dashboard/src/panels/review/ReviewWorkspace.tsx:332-344 |
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
- 2026-09-26T04:00:00+02:00 — 260921-ICR-L36 curator, **the F-V1-3 reword has LANDED, and this document now carries the sentence the page actually prints.** The clause this pass quoted at 03:00 and 03:50 has been replaced in the source: the verdict's notion sentence now reads *"every row below prints what each side's read made of its address — the resolution that side's claim carried — so an address both sides carried prints both readings whenever they differ, and an address only one side carried prints that side's alone."* **The superseded wording — *"…names the resolution of each side whose read resolved its address's recorded bytes…"* — must not be quoted**: *"resolved"* collides with the product's own name for `exact_recorded_blob`, which made the clause true under the reading the code implements and false under the literal one on every live row. The reword removes the collision by naming the reading explicitly, and the fix verifier asserted the row-by-row behaviour on the rendered page. **The body was updated; the two history entries above that quote the superseded sentence are left standing as the record of what this pass wrote before the reword.** **Citation accounting:** the row into `FamilyReviewCenter.tsx` for the second pass now also cites `:682-697`, the interface that declares `readingsBySide` (the checker resolves that anchor to its declaration at `:689`, which the row's previous single range `:804-827` did not contain), and the verdict row's anchor was replaced with two strings that occur inside `:864-909` (`"no claim was left unmeasured"` and `"changed expression row(s) across the family's"`) because the old anchor's sentence no longer exists in that form anywhere in the tree. No verification stamp was advanced; no commit was made.
- 2026-09-26T03:50:00+02:00 — 260921-ICR-L36 curator, **final wording pass (the last correction), and two round-1 sentences this seat repeats are corrected or bounded here.** (1) **The replacement clause is not to be quoted as self-evidently true** (F-V1-3, low; a reword is in flight). The page's notion sentence reads *"every row below prints what each side's read made of its address — the resolution
that side's claim carried — so an address both sides carried prints both readings whenever they differ, and
an address only one side carried prints that side's alone."* The phrase *"resolved its address's recorded bytes"* **collides with the product's own name for `exact_recorded_blob`**: the clause holds under the reading the code implements — a side's read result is printed for the side that produced it, which the fix verifier asserted **row by row on the rendered page** — and fails under the literal reading, where every changed side is `recorded_blob_mismatch` and has not "resolved" its recorded bytes. The body now quotes it **with the reading named**, and says so. (2) **"No claim in the leaf rests on a fixture" is falsified, and this card does not say it** (F-V1-4, low — the one round-1 sentence the corrected pass did not cover). The **divergent-rendering** claim rests on the captured `familyReview.walkFinal` body through a **labelled fixture**, because live data carries no divergent family: the search reached **3 families served by 1 leaf**, with **35 leaves refusing `candidate_dataset_absent`** and therefore **absent, not measured**, `260921-ICR-L36` among them. Every `CONSTRUCTED` label in the unit lane is about that module's own inputs and is **not** a claim about the leaf's evidence. (3) **Routed, not absorbed:** **F-V1-6** and **F-V1-7** are the verifier's remaining low findings and belong to the worker/verifier seats; the subject-catalogue route's deliberate `candidate_dataset_absent`, the shell-level scroll decision with its 13 chrome elements, and **D63**, **D64**, **D68**, **D70** remain routed exactly as before. (4) **One report-side caveat that is NOT a card fact and is deliberately not propagated as settled:** the report's `dashboard/src` digest `08de88e7…` does not reproduce under a stated method (the verifier measured `fb387272…`), and three B4 content heights differ between the two seats by 20–70 px. No card here quotes a digest or a height, and none should: those numbers were measured by one seat and may differ by seat. No verification stamp was advanced; no commit was made.
- 2026-09-26T03:35:00+02:00 — 260921-ICR-L36 curator, **the authoritative statement of the divergent bound; it supersedes every earlier phrasing of it in this document, and the entry below is corrected in place for its refusal reason only (same seat, same uncommitted pass, minutes old, and a wrong reason code must not stand).** The orchestrator passed this seat a summary of the zero-divergence measurement whose scope was too wide — "scanned every family of all 36 leaves" — and the artifact does not support that scope. Measured from `temp/icr/f1/raw/live-truth.json` and reproduced independently by the verifier in `temp/icr/f1v/raw/vf1-live-scan.json`: **36 leaves attempted; 1 resolved (`260921-ICR-L34`, state `entries`, 3 families); 35 refused with code `candidate_dataset_absent`** (each records no comparison generation, so no knowledge operand exists for a subject to be listed from); **3 families served; 0 divergent addresses**. The rule this document now carries is the point of the correction: **absent is not measured.** The 35 were not searched and found clean — they were unreachable, and a family that cannot be listed cannot be shown to be divergence-free. **`260921-ICR-L36` is itself one of those 35**, so this leaf's own live data carries no divergent family either. The bounded conclusion that stands: the divergence is exercised against the captured `familyReview.walkFinal` body through a **labelled fixture** — now verified: the divergent address renders `before exact_recorded_blob · after recorded_blob_mismatch` with `data-sides = "before,after"`, and reverting `excerptKey` fails the shipped suite at `ReviewWorkspace.family.test.tsx:777` — and live data reached 3 families of 1 leaf with none divergent. **Also settled by that verification:** the false sentence is gone from the shipped bundle, the rendered page and the report, and the replacement sentence the cards quote was checked for truth about every row the page renders and none was found untrue. No verification stamp was advanced; no commit was made.
- 2026-09-26T03:20:00+02:00 — 260921-ICR-L36 curator, **same-pass correction of the entry below, which is left standing as the record of what this pass first wrote.** The entry below says the divergence scan "scanned every family of all 36 leaves and measured zero divergent addresses". **That is an over-claim about the population, and the artifact does not support it.** Read from the fix round's own `temp/icr/f1/raw/live-truth.json` and reproduced independently by the verifier in `temp/icr/f1v/raw/vf1-live-scan.json`, the measurement is: **36 leaves attempted, 35 refused `candidate_dataset_absent`** (each records no comparison generation, so no knowledge operand exists for a subject to be listed from — **absent is not measured**), **1 resolved** (`260921-ICR-L34`, which returns `entries` with **3 families**), and of those 3 families examined **0 carry a divergent address** (`familiesExamined: 3`, `familiesWithDivergence: 0`, `totalDivergent: 0`). **The zero is measured over 3 families, not over all 36 leaves** — 35 of them never answered — and the body of this document now says so, naming the examined population and citing both artifacts. The measured conclusion is unchanged and the bound it exists for is unchanged: no live family in the population the scan could reach records a divergence, so the divergent rendering is evidenced against the captured `familyReview.walkFinal` body through a fixture-backed API and is labelled as such. Only the population was overstated; no stamp was advanced; no commit was made.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **post-fix pass: the F1 repair round landed and this card's account of the collection is re-read against the fixed bytes, with every range re-derived at the new tip.** The card no longer records a defect, because there is none: it records the repair and the measurement behind it. **The dedup key is now `path \0 recorded`** (`excerptKey`, `:712-717`) — the observed identity is out of the excerpt identity, and the module's header carries a heading of its own for it, "WHY THE OBSERVED IDENTITY IS NOT PART OF THE KEY, MEASURED", which states the captured measurement (the `familyReview.walkFinal` body records `src/batch.py` under recorded blob `353df144…`; the before read observed that same blob and resolved `exact_recorded_blob`, the after read observed `da6bf861…` and resolved `recorded_blob_mismatch`) and the consequence of the old key (one address split into two keys, one per side, so the pairing pass could never find the other one and the row printed a single side). **The second pass is renamed and widened: `recordSideResolutions` → `recordSideReadings`** (`:804-827`), and an excerpt now carries `readingsBySide` — a new `FamilyExcerptSideReading` (`:671-680`) holding each side's **resolutions** *and* the **observed identities** that side's read found, both read results and neither an identity. `orderExcerpts` (`:829-843`) sorts each side's observed identities too, so the rendering is deterministic. **The row prints the observed identity per side** (`FamilyExpressionRow`, `:911-973`) with `not observed` where a side's read found no address, and the verdict's notion sentence was replaced outright with the clause a reader may now quote: *"every row below prints what each side's read made of its address — the resolution
that side's claim carried — so an address both sides carried prints both readings whenever they differ, and
an address only one side carried prints that side's alone."* **The dedup arithmetic is unchanged by the repair and was re-measured:** 8 membership rows, 8 changed row instances, 2 distinct keys with group sizes `[4,4]`, `8 − 2 = 6`, and the over-collapse probe still finds none — two different recorded blobs at one path stay two excerpts, which is exactly what keeping `recorded` in the key buys. The mutation bites: reverting the key to include `observed` produces `Tests 3 failed | 25 passed (28)` at the case with `expected [ 'after' ] to deeply equal [ 'after', 'before' ]`. **The honest bound this card now carries and did not before:** the divergent path is evidenced against the **captured `familyReview.walkFinal` body through a fixture-backed API**, labelled as such, because **the divergence exists nowhere in live data** — the fix round scanned every family of all 36 leaves and measured zero divergent addresses — so the live family renders the same 2 excerpts as before. **This supersedes this pass's earlier F1 defect paragraph and the two history entries above it record what was written before the fix; nothing is rewritten to say something else.** **Citation accounting:** every row re-derived at the new tip — `membersComplete` `:1014-1021` → `:1044-1051`, `memberContextHeading` `:1023-1031` → `:1053-1061`, `memberContextCounts` `:1033-1046` → `:1063-1076`, `FamilyMemberContext` `:1048-1111` → `:1078-1141`, `FamilyCenter` `:1113-1163` → `:1143-1193`, `IndependentFacts` `:1165-1236` → `:1195-1266`, `MemberCenter` `:1238-1304` → `:1268-1334`, the root `:1306-1389` → `:1336-1419`, `carriedMembership` `:643-652` → `:654-663`, `listedOrPlainPath` `:954-969` → `:984-999`, the A4 header `:571-621` → `:571-632`, `RESOLVED_ADDRESSES`/`UNMEASURED_ADDRESSES` `:623-627` → `:634-638`, `FamilyMembershipRow`+`carriedMembership` `:629-652` → `:640-663`, the excerpt interfaces `:654-691` → `:665-710`, `excerptKey` `:693-695` → `:712-717`, `claimClass`+`ExcerptTally` `:697-715` → `:719-737`, `absorbClaim` `:717-752` → `:739-773`, the three passes `:754-817` → `:775-843`, `familyExpressionExcerpts` `:819-836` → `:845-862`, the verdict `:838-881` → `:864-909`, `FamilyExpressionRow`..`listedOrPlainPath` `:883-969` → `:911-999`, `FamilyExpressionExcerpts` `:971-1013` → `:1001-1043`. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (leaf `260921-ICR-L36`, memory worktree only; code worktree uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`, memory base `52c025e6f2c38d3207274d55e00a8889c0459bad`; worker report `temp/icr/report-l36.md`): **body update — the card's account of the family column is corrected, because the column stopped composing two things and started composing three.** The old card said, in two places, that the family selection renders the guarantee comparison and the member-context card; that enumeration was exhaustive and it left the family column with **no expression collection at all**, which is exactly what the accepted design's whole-family line forbids ("Whole-family selection presents the full guarantee, all members including the unchanged sibling, and deduplicated changed expression excerpts"). Both places were corrected rather than annotated: the Purpose now names the two selection shapes as two different routes through the one column, and the `FamilyCenter` paragraph now names its three parts. `FamilyMemberContext` — the member-context card **extracted** from `FamilyCenter` unchanged — has its own paragraph, the two hoisted owners (`unlistedPathNote`, `listedOrPlainPath`) are recorded as one implementation each with the reason they were hoisted, and A4's collection has four logic paragraphs covering the four decisions a reader must not have to re-derive: **what "changed" is** (the realization resolution over the read's own seven-value vocabulary, partitioned three ways, and explicitly *not* the comparison's own measured change set), **what the dedup key is** (the address together with the recorded and observed source identities, never the path alone), **why the collection reads the carried membership rows and not the centre's first-wins `distinct` list** (a resolution is a fact about one side's tree, and the captured `familyReview.walkFinal` body resolves one address on `before` and mismatches it on `after`, which a `distinct`-built collection would have presented as resolved), and **why one row names every membership row with the revision identity beside the label** (`ICR30-I-1` is recorded as two member revisions of its family). Four invariant bullets were added for the same four properties, and the first bullet was rewritten: "One column, in the packet's order" was true of the **member** selection only, so it now states both orders and says the family column no longer stops after the roster. **Citation accounting:** every row this file's own insertion displaced was re-derived from each construct's declaration at this tip — `GuaranteeBlock` `:96-110` → `:97-111`, `GuaranteeComparisonBlock` `:112-188` → `:113-189`, `MemberIdentity` `:190-202` → `:191-203`, `MemberFacts` `:204-221` → `:205-222`, `MemberStatement` `:223-242` → `:224-243`, `missingRowNote` `:244-261` → `:245-262`, `oneSidedStatement` `:263-298` → `:264-299`, `memberStatementBlock` `:300-343` → `:301-344`, `RealizationClaims` `:345-376` → `:346-377`, `AttributedPaths` `:378-442` → `:388-448`, `observationBlock` `:444-456` → `:450-462`, `assessmentBlock` `:458-472` → `:464-478`, `EvidenceBlock` `:474-528` → `:480-534`, `UnselectedCenter` `:530-567` → `:536-569`, `membersComplete` `:568-576` → `:1014-1021`, `memberContextHeading` `:577-587` → `:1023-1031`, `memberContextCounts` `:588-602` → `:1033-1046`, `FamilyCenter` `:603-681` → `:1113-1163`, `IndependentFacts` `:682-749` → `:1165-1236`, `MemberCenter` `:751-816` → `:1238-1304`, the root `:818-893` → `:1306-1389`, and the import block `:24-46` → `:24-47`. **Citation debt carried in by the sweep, and paid here rather than left:** the L25 entry's own `UnselectedCenter` range had run four lines past the construct into the next comment block; it is now the construct's true extent. **Sweep result:** every home this change falsifies was searched for and the ones found are corrected in this pass — this card, `ReviewWorkspace.family.test.tsx.md` (whose case count is now the file's own), and the `panels` route overview, with every other card that reaches into this file re-anchored in the same pass (`panels/overview.md`, `ReviewWorkspace.tsx.md`, `ReviewWorkspace.family.test.tsx.md`, `FamilyTree.tsx.md`, `data/reviewFamily.ts.md`, and the three `familyReview.*.captured.json.md` cards). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — the empty column's sentence now names the plane, and this card's account of it was corrected rather than left describing the old wording.** `UnselectedCenter` used to read "No family or member is selected", which collided with the server's own use of "selected" on the same screen (the scope header's composed-context count and the tree's "this review selected \<revision\>"), so a reader comparing the two read a contradiction that was a collision of vocabularies; the sentence now reads "No family or member has been chosen **in this column** yet" and states that the header's composition and the tree's revision selection are not choices made here (register B3). **What the correction deliberately did not claim:** the old sentence was **not** false about this component's own state — the measured `data-selection-kind` is `none` with no tree row carrying `aria-current` until the reader chooses, so the layout was left alone and only the wording changed. The invariant bullet and the `UnselectedCenter` row were corrected in place with the new anchor text. **Citation accounting:** every row whose range this file's own insertion displaced was re-derived from each construct's declaration at this tip — `UnselectedCenter` now `:530-567`, `membersComplete` `:568-576`, `memberContextHeading` `:577-587`, `memberContextCounts` `:588-602`, `FamilyCenter` `:603-681`, `IndependentFacts` `:682-749`, `MemberCenter` `:751-816`, `FamilyReviewCenter` `:818-893` — and the three cross-file rows were re-derived too (`RosterLine`/`RosterNext`/`emptyRosterSentence` in `FamilyTree.tsx`, `SourceExplorer` `:246`, the workspace mount `:332-344`). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the unified central reading path. It records that the centre renders the family guarantee and the selected intent, then the linked expressions, then the execution evidence and authored assessment in one column; that `missingRowNote()` decides what may be said about a missing side from that side's own roster state and its roster page's completeness — a bounded walk's missing row is a page fact and never "the snapshot records no row"; that `oneSidedStatement()` decides its note from each member's own state rather than from the comparison kind; that `memberContextHeading()` prints "Complete recorded member context" only when the entry's own state is `recorded` and every roster page is complete; that `memberContextCounts()` prints the read owner's measured `members_total` with this page's share stated as a share; that `IndependentFacts` prints the five independent facts from their own owners' values; that `EvidenceBlock` joins records on the member's own `invariant_revision_id` and counts-and-names the unjoined records instead of displaying them; and that `FamilyReviewCenter` mounts `SourceExplorer` beneath the reading path so the measured population is never filtered by the selection. Every row of the reference table was derived against this leaf's candidate, and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
