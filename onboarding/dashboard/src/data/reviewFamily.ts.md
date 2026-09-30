# dashboard/src/data/reviewFamily.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewFamily.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076` |
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

The client-side mirror of the server's `models/knowledge/review_family_context.py`, the module
`ICR-R31@v1` landed and `ICR-R24@v3` consumes: it declares the family half of the review payload —
which recorded families the selected subject belongs to on each snapshot, each selected family
revision's own authored joint guarantee, and that revision's recorded member revisions with the
unchanged siblings included — and nothing else. The file is a value tree plus two pure comparisons:
one type import from the surrounding contract, no request, no state, no DOM, no side effect.

It exists as its own module because the family vocabulary is self-contained and `data/review.ts`
already owns the rest of the payload; mirroring the family tree inside that file would have pushed
the one public entry past the size at which nobody reads it. `data/review.ts` re-exports every name
declared here, so a consumer of the review contract still imports one public entry.

**The mirror's two refusals are the whole file.** It may not narrow the server's vocabulary, and it
may not default a field the server omits. The five context states, the four side states and the two
member content states are distinct facts a rendering has to keep apart — a client that collapsed
`no_family_recorded` (a *measured* zero) into `unavailable` (a read that did not happen), or
`not_recorded` into an empty roster, would be manufacturing the lie the packet forbids — and a field
the server does not send stays `undefined` here rather than acquiring a default the store never
recorded.

Three exported values and two exported functions carry the rules a rendering must not re-invent.
`FAMILY_CONTEXT_JOIN_KEY` is the string `"invariant_revision_id"`: the one key that joins a member
context to the evidence and assessment owners' own collections, held as a value rather than prose
because joining on a display label or a path would be inventing the association. `FAMILY_SIDES` is
the two-snapshot order, so a rendering never spells the pair out and cannot accidentally read one
side twice. `UNRESOLVED_SELECTION_STATES` is the server's own vocabulary for a lineage this context
could not reduce to a single head — a distinct answer from "no members", because a lineage without a
head is not a roster that came back empty. `guaranteeComparison(entry)` reduces the two recorded
sides to one of five shapes and is the only place a surface may learn that a family guarantee did
not change; `memberComparison(before, after)` reduces one member revision's two sides to one of four
shapes, decided from each member's own carried `state`, and deliberately carries no sentence, because
what may be said about a missing side is a fact about that side's roster page rather than about the
comparison kind.

## Code Commentary

### Logic

ReviewRevisionSelection is shared by recorded family context and the primary invariant statement pane. Both use the owner-selected before/after pair or explicit ambiguous/unresolved state; neither browser consumer chooses a head.

**The vocabulary is a closed set of literals, and each union states what none of its members is.**
`ReviewFamilyContextState` is the five-state answer to what the context could say about the recorded
scope: `recorded`, `partial`, `no_family_recorded`, `no_subject_selected` and `unavailable`, and the
file's own comment fixes `no_family_recorded` as a measured zero. `ReviewFamilySideName` is
`before` | `after`. `ReviewFamilySideState` is one snapshot's side of one family context —
`recorded`, `not_recorded`, `not_resolved`, `unreadable` — and the file states that none of the four
is an empty roster. `ReviewFamilyEntryState` is `recorded` | `partial` | `unresolved` | `unavailable`
for a single family entry. The member's own content state is the two-member union on
`ReviewFamilyMember.state`: `recorded` means this page carried that revision's own content, and
`content_not_on_page` means the membership row is recorded and only its content fell outside the
page — and because the server refuses a member whose state and carried content disagree, that field
is the whole truth about the statement.

**`FAMILY_CONTEXT_JOIN_KEY` is one exported string, and it is the file's only identity rule.**
`export const FAMILY_CONTEXT_JOIN_KEY = "invariant_revision_id"` is not documentation: it is the
value `FamilyReviewCenter.tsx` and `FamilyTree.tsx` filter their collections with, so a record
belongs to a member revision only when its own `invariant_revision_id` equals the member's. The
sibling value `FAMILY_SIDES` types the two-snapshot array as `ReviewFamilySideName[]`, and
`UNRESOLVED_SELECTION_STATES` types the two selection states (`ambiguous`, `unresolved`) that mean a
context could not name one selected revision.

**The value tree mirrors the server's models field for field.** `ReviewFamilyGuarantee` carries the
family revision's authored text (`joint_guarantee`), its identities, `state_at_origin`, the optional
`acceptance_ref`, its `provenance` and its `payload_digest`. `ReviewFamilyMemberSource` carries one
realization claim's `claim_id`, `invariant_revision_id`, `role`, `rationale` and `detail`, with
`path`, `recorded_source_identity`, `observed_source_identity` and `resolution` optional because the
address and the resolution travel together or not at all — the server refuses one without the other.
`role` and `rationale` are **required** strings: the store holds both for every claim and the server
refuses a reference without them, so an optional type would model an unreachable state. Per side and
per claim it also carries the anchor's structured recorded `locator` (optional, travelling with the
address), the required `resolved_ranges` array and the required `locator_state`. Three new declarations
type them: `ReviewSourceLocator` (the server's three locator kinds — `file`, `line_range` with
`start_line`/`end_line`, `symbol` with `language`/`qualified_name`), `ReviewSourceLineRange` (one
one-based inclusive range in the side's exact recorded blob) and `ReviewSourceLocatorState`
(`resolved` / `whole_file` / `unresolved` / `not_observed`). Two claims at one path keep two regions,
and no region is ever read out of `detail`. There is no runtime decoder for this payload — the
transport casts the body to these types — so the mirror is the whole client-side contract; no rendering
reads the new fields yet.
`ReviewFamilyMember` carries the membership's exact identities, its optional display fields, its
`state`, its optional `statement`, `applicability`, `lifecycle` and `payload_digest`, its
`essential_conditions`, `exclusions`, the required `other_family_revision_ids`, `sources`, the
optional `movement_reference` and its `detail`. `ReviewReadCounts` carries the read owner's own
eleven counts whole, `ReviewFamilyRosterPage` carries one page's `scope`, `state`, `counts`,
`complete`, `members_total` and optional cursors, and `ReviewFamilyRevisionContext` carries one
side's `state`, optional `family_revision_id`, its `recorded_revision_ids`, optional `guarantee`, its
`members`, `members_total`, optional `page` and its `detail`. `ReviewFamilyContextEntry` binds one
`family_id` to its `selection`, its `before`/`after` contexts, the `candidates` present exactly for
the two states that chose no revision, its entry `state` and its `detail`. `ReviewFamilyContext`
closes with the entry list, the four family/membership totals and
`ReviewFamilyContextReferences`.

**The change facts of a tree comparison (MIK-L33, MIK-R33).** `ReviewFamilyContextEntry` gains the optional
`change_kinds: ReviewFamilyChanges`, mirroring `models/knowledge/review_change_kinds.py`; a dataset review carries
none. `ReviewChangeKind` (`intent`, `implementation`, `membership`, `unknown`, `unchanged`), `ReviewChangeFact`
(`established`, `not_established`, `unknown`) and `ReviewChangeMark` (the three facts, `text_differs`, `test`,
`unknown`) are the server's literals. `ReviewMemberChange` is one member occurrence keyed by the roster's `member_id`
(the same on both sides, so both revision rows of a revised member read one fact set), with the optional `invariant`
and `authored_position`, the three facts, `proof`, `text_differs`, `range_unresolved`, the server-derived `primary`
and `marks`, and three bounded line lists kept apart: `evidence`, `unknown_reasons` (why the change kind is not fully
known) and `membership_reasons` (why the membership is unknown; the merge round's split). `ReviewFamilyChanges` is
the family's own `guarantee` fact (`intent`, `unchanged`, `unknown`) with its `guarantee_detail`, the optional
`members_total` (absent when it could not be read), the returned occurrences and an optional `detail`. As everywhere
in this file, an omitted field stays `undefined`: a rendering orders, counts and traverses by these facts
(`panels/review/changeTriage.ts`) and never recomputes one. **`ReviewFamilyRosterPage.complete` is not "every member
returned":** a roster page can be incomplete with every member returned, because the read owner's page also counts
realization items, so MIK-L33 counts unreturned members as returned below `members_total` (ruling
2026-09-30T16:22:22 item 8).

**Two comments in the tree fix a population, not a rendering.** `ReviewFamilyRevisionContext`'s
`recorded_revision_ids` is every revision of that family the snapshot records — a *larger* population
than the revisions a selection reached, because a family revision that cites no member is recorded
and may never have been chosen — and `ReviewReadCounts` is carried whole because the walk's
arithmetic is checked by the owner's own validator and is never restated by a rendering.
`ReviewFamilyRosterPage.complete` is the owner's own `enumeration_complete`, with the server
refusing the two facts of a truncated roster and its cursor disagreeing. `ReviewRevisionSelection`
and `ReviewRevisionSelectionState` are `ICR-R07@v1`'s revision-selection value mirrored here rather
than in `review.ts`, because the family context is its only consumer on this surface.
`FamilyMemberRow` is the tree's own row shape: one side plus the member that side recorded.

**`guaranteeComparison(entry)` is the one place the three "did not change" shapes are kept apart.**
It reads the two `guarantee` fields and nothing else. When the before side recorded none it returns
`unrecorded` (with the entry's own `detail`) if the after side recorded none too, otherwise
`one_sided` for `after`; when only the after side is absent it returns `one_sided` for `before`;
when both are present it delegates to `twoRecordedGuarantees`. That private helper compares the two
`revision_id` values first: equal means `unchanged_revision` — one authored revision behind both
sides, and the only shape in which a surface may say the guarantee is unchanged — otherwise it
compares `joint_guarantee` text and returns `identical_text` for two distinct revisions whose
recorded text happens to be equal (a revision was authored; the text is what did not move) or
`changed` for two distinct texts. The five shapes are therefore distinct answers about the store,
and `one_sided` is an addition or a removal, never an unchanged guarantee.

**`memberComparison(before, after)` decides from carried content, and its two "nothing to compare"
answers are different facts.** A side that is `undefined` sends the pair to `oneSidedMember`; so does
a pair in which either member's own `state` is not `recorded`, because comparing a carried revision
against one whose content was not on the page would claim a comparison the store does not support.
Only when both sides carried content does it compare `invariant_revision_id`: equal yields
`unchanged_revision` carrying that one member, different yields `changed` carrying both.
`oneSidedMember` counts the sides whose state is `recorded`: with none carried it returns
`not_on_page` around the one member the page did reach (or a bare `one_sided` when there is no member
at all), and with exactly one carried it returns `one_sided` around both operands. The distinction
the file draws is explicit — `not_on_page` means no side this page reached carried the revision's
content, while `one_sided` means at most one side's content is here and the other side either listed
no row or listed the row without its content — and the value carries no sentence for either, because
only a rendering holding each member's own `state` and the roster page's own completeness may say
which of the two it is. A row missing from a *bounded* page is a row the page did not reach, which is
a different fact from a snapshot that records none.

### Conventions

Declarations are `export type` / `export interface` / `export const` / `export function`; there is no
default export and no class. Every optional server field is declared with `?` and is never given a
fallback value, so an omitted field is `undefined` in the client and a rendering must decide what to
say about it. Server `provenance` and other open maps are typed `Record<string, unknown>` rather than
narrowed into a client shape. The two comparison functions are pure and total over their declared
inputs: they read the values they are handed, return a discriminated union member, and touch no
module state, no clock and no transport. The unions are named types rather than inline literal
parameters, and each carries a comment that states what its members mean and which one is a measured
zero. `data/review.ts` re-exports the five names and the twenty-one types from this module (including the three locator types); the five change types MIK-L33 adds are not re-exported there, and `changeTriage.ts`, `ChangeBadges.tsx` and `FamilyTree.tsx` import them from this file directly, and
`FamilyTree.tsx` / `FamilyReviewCenter.tsx` import them from `../../data/review` rather than reaching
into this file directly. Inline prose comments sit above the declaration they explain, and the
header comment names both the packet revision the vocabulary mirrors and the increment that consumes
it.

### Invariants And Boundaries

- **The mirror may not narrow the server's vocabulary.** Five context states, four side states, two
  member content states and four entry states are declared exactly as the server spells them.
- **A field the server omits stays `undefined`.** No default, no coercion and no `??` fallback is
  declared in this file; the absence is data a rendering must state for itself.
- **A measured zero is never an unavailable read.** `no_family_recorded` and `unavailable` are
  separate members of one union, and the file's own comment says which is which.
- **No side state is an empty roster.** `not_recorded`, `not_resolved` and `unreadable` each state a
  different fact in the header, and the roster page beneath a `recorded` side says separately how
  much of it this page carried.
- **`FAMILY_CONTEXT_JOIN_KEY` is the only join.** The association is the recorded
  `invariant_revision_id`, never a display label, a version or a path.
- **Only `unchanged_revision` supports "unchanged".** `identical_text` records that a revision *was*
  authored, and `one_sided` records that no comparison was made at all.
- **`memberComparison` carries no sentence.** It answers with a kind and the operands it reached;
  what may be said about a missing side is decided by the caller from that side's own `state` and its
  roster page's completeness.
- **A row without its content can never reach `unchanged_revision` or `changed`.** The carried-state
  guard runs before the revision-identity comparison.
- **One member revision is one subject.** `other_family_revision_ids` is carried so a shared member
  is visible as the same canonical revision beneath every family that records it, not as a copy.
- **The file is a value tree.** It declares no request, resolves no candidate, holds no state and
  imports no module other than the review contract's own types.

### Todos

None recorded. The vocabulary is complete for the two comparisons it owns; any rendering rule about
a bounded roster belongs to `FamilyTree.tsx` and `FamilyReviewCenter.tsx`, which read these values
rather than extend them.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the header's own statement of what
the mirror may not do, the four state unions, the join key and the two exported values beside it, the
value tree that mirrors the server's models, and the two comparison functions with the shapes they
return. The server module this file mirrors and the two consumers that read these names are cited
beside it, and every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own statement of what this file mirrors, the packet revision it mirrors it for, and the rule that a field the server omits stays `undefined` rather than becoming a default.** | `review_family_context.py`; `ICR-R31@v1`; `undefined` | dashboard/src/data/reviewFamily.ts:1-14 |
| **The five context states, with `no_family_recorded` fixed as a *measured* zero.** | `ReviewFamilyContextState`; `no_family_recorded` | dashboard/src/data/reviewFamily.ts:16-23 |
| The two snapshot names, and the four side states none of which is an empty roster. | `ReviewFamilySideName`; `ReviewFamilySideState`; `not_resolved` | dashboard/src/data/reviewFamily.ts:25-25; dashboard/src/data/reviewFamily.ts:28-28 |
| The entry's own four-state union. | `ReviewFamilyEntryState`; `unavailable` | dashboard/src/data/reviewFamily.ts:30-30 |
| **The one join key, held as a value rather than prose because joining on a label or a path would be inventing the association.** | `FAMILY_CONTEXT_JOIN_KEY`; `invariant_revision_id` | dashboard/src/data/reviewFamily.ts:32-35 |
| The family revision's own authored guarantee, printed from the stored text rather than assembled from members. | `ReviewFamilyGuarantee`; `joint_guarantee`; `payload_digest` | dashboard/src/data/reviewFamily.ts:37-46 |
| One realization claim's source reference: the address and what the read resolved it to travel together or not at all; required stored role and rationale; the structured locator, this side's resolved ranges and the locator state. | `ReviewFamilyMemberSource`; `observed_source_identity`; `detail`; `locator_state` | dashboard/src/data/reviewFamily.ts:67-87 |
| **The three locator declarations: the server's locator kinds, one resolved line range, and the four locator states with what each one carries.** | `ReviewSourceLocator`; `ReviewSourceLineRange`; `ReviewSourceLocatorState` | dashboard/src/data/reviewFamily.ts:49-52; dashboard/src/data/reviewFamily.ts:55-59; dashboard/src/data/reviewFamily.ts:65-65 |
| The server rule these states mirror. | `source_locator_state` | mcp/src/agents_remember/models/knowledge/review_family_source.py:108-123 |
| **One recorded membership: the exact member revision, the two member content states, and the shared-identity list.** | `ReviewFamilyMember`; `content_not_on_page`; `other_family_revision_ids` | dashboard/src/data/reviewFamily.ts:89-111 |
| The read owner's own counts, carried whole because the walk's arithmetic is the owner's. | `ReviewReadCounts`; `primary_items_remaining`; `unresolved_anchor_total` | dashboard/src/data/reviewFamily.ts:115-127 |
| **One roster page: the owner's own `enumeration_complete` flag, its two measures and the cursor that reaches the rest.** | `ReviewFamilyRosterPage`; `enumeration_complete`; `continued_from` | dashboard/src/data/reviewFamily.ts:130-130; dashboard/src/data/reviewFamily.ts:132-140 |
| **One side's family revision context, whose `recorded_revision_ids` is a larger population than the revisions a selection reached.** | `ReviewFamilyRevisionContext`; `recorded_revision_ids`; `members_total` | dashboard/src/data/reviewFamily.ts:142-156 |
| The owner's revision-selection value, mirrored here and shared by the family context and the primary invariant statement pane; neither consumer selects a head. | "shared by family context and the primary invariant"; `ReviewRevisionSelectionState` | dashboard/src/data/reviewFamily.ts:158-158; dashboard/src/data/reviewFamily.ts:160-165 |
| **One family entry: its selection, its two sides, the `candidates` present exactly for the two states that chose no revision, and on a tree comparison its optional change facts (MIK-L33).** | "export interface ReviewFamilyContextEntry {"; "label_side?: ReviewFamilySideName;"; "candidates: ReviewFamilyGuarantee[];"; "change_kinds?: ReviewFamilyChanges;" | dashboard/src/data/reviewFamily.ts:229-242 |
| The owner's own published collections a member context is referenced through, named by identity and joined on `join_key`. | `ReviewFamilyContextReferences`; `join_key` | dashboard/src/data/reviewFamily.ts:244-253 |
| The context itself: its four totals, its references and its stated limitations. | `ReviewFamilyContext`; `unique_member_revision_total`; `limitations` | dashboard/src/data/reviewFamily.ts:255-266 |
| **`FAMILY_SIDES`: the two snapshots as a value, so a rendering cannot read one side twice.** | `FAMILY_SIDES`; "[\"before\", \"after\"]" | dashboard/src/data/reviewFamily.ts:270-270 |
| **The tree's own row shape: one member revision as one row, keyed by the revision rather than the association.** | `FamilyMemberRow`; `other_family_revision_ids` | dashboard/src/data/reviewFamily.ts:107-107; dashboard/src/data/reviewFamily.ts:276-279 |
| **`UNRESOLVED_SELECTION_STATES`: a lineage this context could not reduce to a head, which is a distinct answer from "no members".** | `UNRESOLVED_SELECTION_STATES`; `ambiguous` | dashboard/src/data/reviewFamily.ts:284-287 |
| **The five shapes of a guarantee comparison.** | `GuaranteeComparison`; `unrecorded`; `one_sided` | dashboard/src/data/reviewFamily.ts:293-298 |
| **The three "did not change" shapes kept apart on purpose: one revision, two revisions with identical text, and a one-sided record.** | `unchanged_revision`; `identical_text`; `one_sided` | dashboard/src/data/reviewFamily.ts:300-309 |
| **`guaranteeComparison`: the two recorded sides reduced to one shape, and the only place a surface may learn that a guarantee did not change.** | `guaranteeComparison`; "before === undefined" | dashboard/src/data/reviewFamily.ts:310-320 |
| The private second half: identities decide first, then the recorded text. | `twoRecordedGuarantees`; `joint_guarantee` | dashboard/src/data/reviewFamily.ts:41-41; dashboard/src/data/reviewFamily.ts:325-335 |
| **`MemberComparison`'s four shapes, and the `not_on_page` / `one_sided` distinction that the caller must decide rather than the value.** | `MemberComparison`; `not_on_page`; `missingRowNote` | dashboard/src/data/reviewFamily.ts:337-359 |
| **`memberComparison`: decided from each member's own carried `state`, never from the revision ids alone.** | `memberComparison`; "before.state !== \"recorded\"" | dashboard/src/data/reviewFamily.ts:361-372 |
| The one-sided reducer: how many sides carried content is the question, and a row missing from a bounded page is the page's fact. | `oneSidedMember`; "carried.length === 0" | dashboard/src/data/reviewFamily.ts:385-397 |
| **The public entry that re-exports this module's names, so the surface imports one contract.** | `FAMILY_CONTEXT_JOIN_KEY`; `guaranteeComparison` | dashboard/src/data/review.ts:32-41 |
| The payload key whose absence is its own fact — a body that is not a measured zero and is never shown as `no_family_recorded`. | "family_context?: ReviewFamilyContext" | dashboard/src/data/review.ts:467-467 |
| **The server module this file mirrors, and the packet revision that asked for the vocabulary.** | "ICR-R31@v1" | mcp/src/agents_remember/models/knowledge/review_family_context.py:1-3 |
| The server's own rules the mirror carries across: a guarantee is the family's authored text and the five status dimensions stay separate. | "A guarantee is the family's own authored text"; "The five status dimensions stay separate" | mcp/src/agents_remember/models/knowledge/review_family_context.py:10-24 |
| The tree uses shared side order and its own guarantee/roster helpers; central guarantee comparison stays separate from authoritative selected statements. | `guaranteesOf`; `memberRows`; `GuaranteeComparisonBlock`; `SelectedStatement` | dashboard/src/panels/review/FamilyTree.tsx:335-363; dashboard/src/panels/review/FamilyTree.tsx:152-171; dashboard/src/panels/review/FamilyReviewCenter.tsx:130-212; dashboard/src/panels/review/SubjectReview.tsx:255-334 |
| The change literals and one member occurrence's facts, primary, marks and three reason lists kept apart (MIK-L33). | `ReviewChangeKind`; `ReviewChangeFact`; `ReviewChangeMark`; `ReviewMemberChange`; `membership_reasons` | dashboard/src/data/reviewFamily.ts:180-216 |
| One family occurrence: its guarantee fact, its total when readable, its returned occurrences (MIK-L33). | `ReviewFamilyChanges`; `members_total` | dashboard/src/data/reviewFamily.ts:218-227 |

## Cross-Repo References

No cross-repository behavior is implemented in this file, and none is implied by it. The module
mirrors a server module of the *same* repository across the client/server process boundary, so the
one association it carries is an in-repository contract rather than a cross-repo dependency.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-R33:** the mirrored change types (`ReviewChangeKind`, `ReviewChangeFact`, `ReviewChangeMark`, `ReviewMemberChange` with `membership_reasons` apart from `unknown_reasons`, `ReviewFamilyChanges`) and `ReviewFamilyContextEntry.change_kinds`; the note that a roster page's `complete` is not "every member returned" (ruling 2026-09-30T16:22:22 item 8); Conventions records that the new types are imported from this file directly, not re-exported through `data/review.ts`. **Reopened claim reworded and re-anchored** on line-exact quotes: the family-entry row; this pass's generated bullet for it was removed (the others are kept). Two rows added. The other rows moved by the 49 inserted lines were re-pointed by the installed fixer (its bullets kept) or the exact base-to-staged line shift.
- 2026-09-30T20:19:37+00:00: Generated citation repair: `ReviewFamilyContextReferences`; `join_key` repointed to dashboard/src/data/reviewFamily.ts:244-253; dashboard/src/data/reviewFamily.ts:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:19:37+00:00: Generated citation repair: `ReviewFamilyContext`; `unique_member_revision_total`; `limitations` repointed to dashboard/src/data/reviewFamily.ts:255-266; dashboard/src/data/reviewFamily.ts:263-263; dashboard/src/data/reviewFamily.ts:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:19:37+00:00: Generated citation repair: `FAMILY_SIDES`; "[\"before\", \"after\"]" repointed to dashboard/src/data/reviewFamily.ts:270-270; dashboard/src/data/reviewFamily.ts:270-270. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:19:37+00:00: Generated citation repair: `memberComparison`; "before.state !== \"recorded\"" repointed to dashboard/src/data/reviewFamily.ts:361-372; dashboard/src/data/reviewFamily.ts:366-366. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:19:37+00:00: Generated citation repair: `oneSidedMember`; "carried.length === 0" repointed to dashboard/src/data/reviewFamily.ts:385-397; dashboard/src/data/reviewFamily.ts:392-392. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): No content impact: MIK-R34 inserted one import line in `FamilyTree.tsx` and one in `FamilyReviewCenter.tsx`, so the fixer normalised the one row citing them (`FamilyTree.tsx` `312-339` → `313-340`, `132-151` → `133-152`; `FamilyReviewCenter.tsx` `127-209` → `128-210`). The claim is unchanged. No stamp advanced.
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): No content impact: citation ranges into files this leaf changed (`FamilyTree.tsx`, `FamilyReviewCenter.tsx`, `SubjectReview.tsx`) were normalised by the installed fixer to where the same anchors now sit (`guaranteesOf`, `memberRows`, `GuaranteeComparisonBlock`, `SelectedStatement`). The claim still holds: the tree keeps its own guarantee and roster helpers, and the central guarantee comparison stays separate from the selected statement. Claim wording unchanged. No stamp advanced.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): No content impact: citation-only repair. This card's source is unchanged. Its rows into `panels/review/FamilyReviewCenter.tsx` and `panels/review/SubjectReview.tsx` moved with MIK-L31's edits there: the tree/centre row was re-pointed by the exact line shift (`104-169` → `114-188` for `GuaranteeComparisonBlock`, `53-114` → `217-280` for `SelectedStatement`), and the installed fixer normalised two further ranges.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): the mirror gained `ReviewSourceLocator`, `ReviewSourceLineRange` and `ReviewSourceLocatorState`, and `ReviewFamilyMemberSource` now carries optional `locator`, required `resolved_ranges`/`locator_state` and required `role`/`rationale`. Recorded that there is no runtime decoder and no rendering reads the new fields yet, corrected the re-export count (twenty-one types), and re-measured every range the insertions shifted. No verification stamp was advanced.

- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.
- 2026-09-26T21:07:45+00:00: Generated citation repair: "family_context?: ReviewFamilyContext" repointed to dashboard/src/data/review.ts:452-452. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:40:46Z — Reconciled the shared revision-selection consumer and scoped technical-pane regression account.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (memory worktree only; no code changed by this card's own pass; the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`): **citation repair only — the row naming the two consumers of the exported values was re-anchored, and no claim wording changed.** L36 added one import line at the top of `panels/review/FamilyReviewCenter.tsx`, so the `FAMILY_SIDES` / `guaranteeComparison` / `memberComparison` import moved `:38-38` → `:39-39`. This is the whole of the change: the module's contract, its two consumers and its re-export are unaltered. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): created this one-to-one card for the review contract's family mirror. It records that `reviewFamily.ts` is the client-side mirror of `models/knowledge/review_family_context.py` (`ICR-R31@v1`, consumed by `ICR-R24@v3`), that it may neither narrow the server's vocabulary nor default a field the server omits, that the five context states, four side states and two member content states stay distinct with a server-omitted field left `undefined`, that `FAMILY_CONTEXT_JOIN_KEY` is the one join and a value rather than prose, that `guaranteeComparison()` has five shapes and only `unchanged_revision` may say the guarantee is unchanged, that `memberComparison()` returns `not_on_page`/`one_sided`/`unchanged_revision`/`changed` from each member's own carried `state` and carries no sentence because the caller decides, and that `FAMILY_SIDES` and `UNRESOLVED_SELECTION_STATES` are the two remaining exported values. Every row of the reference table was derived against this leaf's candidate, and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, so the stamp names the leaf's base plus the working-tree delta, and governed closeout owns the real stamp.
