# mcp/src/agents_remember/models/knowledge/review_family_context.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Comparison-bound family values: the supplied family guarantee, exact member-revision identities,
separate side/selection states, owner roster pages and explicit counts. This model does not read
storage, assemble a guarantee from members or decide whether a guarantee holds. The current
references value names only the relationship union and source inventory. Removed reviewer evidence,
observation, assessment and applicability collections are not reconstructed by stale header prose.

## Code Commentary

The closed whole-context, side and entry states keep unreadable/unresolved/no-family/no-subject
answers distinct from a recorded roster. Member values retain source references through the
separately owned review_family_source model, their recorded role/rationale and explicit resolution
facts; no source region is guessed from a note. Shared member-revision identities and the supplied
other-family list expose sharing without inventing another revision.

A guarantee value carries the supplied text, display version, origin state, optional acceptance ref,
provenance and digest. These fields are not an authenticity measurement. In particular this class
has no origin-state/acceptance-ref pairing validator; the older card's contrary promise is historical.

`ReviewFamilyRosterPage.complete` means end of enumeration, not that the final page contains the
whole roster. The owner count's returned/total equality is the stated all-members observation.
Continuation/completion, continued-from state and membership total must agree with the supplied
counts. A complete first-page side must contain its full declared roster; a completed continued page
can carry only its own share. A recorded side must identify a revision on its supplied recorded list.

The entry checks pin family identity, before/after side names, label/side pairing, candidate and
selection states. Candidate guarantees never become the selected family's guarantee by this model.
Change facts compare member-ID sets to the actually returned member-ID sets; that local check is
not an independent uniqueness or measured-classification certificate.

Whole-context counts match entry length, roster sums and a distinct member-revision set. They do
not authenticate the underlying facts. A no-family or no-subject result carries no family entries;
partial and unavailable keep their reasons, and an empty recorded context is not substituted for a
measured no-family answer. Production composition, roster reading and task-context selection keep
their own owners and refusal boundaries.

## Invariants And Boundaries

Values stay comparison-bound; declared origin acceptance, source resolution, currentness and authored
meaning are not a current family verdict. Optional change facts are the tree-comparison carrier,
not a surviving database-review branch. Source-only checks and stored assertions below are not new
runtime, CODE or whole-MEMORY grades. Historical numeric prose extents are retained only in the
creation-era account; current evidence resolves actual constructs and the explicit roster paragraph.

<details>
<summary>Historical prior account — retained, not the current contract</summary>

# mcp/src/agents_remember/models/knowledge/review_family_context.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The value vocabulary for the comparison-bound family context (ICR-R31@v1), and the four refusals
that keep a rendering from inventing one.** `ICR-R09@v1`'s flat subject catalogue and `ICR-R08@v1`'s
relationship movement union answer other questions; neither carries *which recorded families the
selected subject belongs to on each snapshot, what each selected family revision's own authored joint
guarantee says, and which exact member revisions that revision records — unchanged siblings included*.
The module's own docstring states the four rules every value below enforces (`:1-30`):

| Rule | What it refuses |
| --- | --- |
| A guarantee is the family's own authored text | assembling a guarantee from the members it is stored beside, or deriving a summary of one |
| A membership cites one exact family revision and one exact member revision | cloning a shared member per context, or inheriting a successor's roster through a moving pointer |
| A side states which snapshot fact it is | rendering any of the four side states as an empty roster |
| The five status dimensions stay separate | any field that could hold a Changed/Passed conclusion about a member's family |

## Code Commentary

### Logic

**The state vocabularies are declared once, as `Literal` types, so a value cannot name a state the
surface does not publish.** `ReviewFamilyContextState` (`:72-78`) is the whole context:
`recorded` (every composed family is complete), `partial` (at least one part is unresolved, truncated
or unreadable), `no_family_recorded` (a **measured** zero, deliberately not spelled `empty`),
`no_subject_selected` (the task-context review, which compared no operand and therefore claims nothing)
and `unavailable` (a selection the composition could not resolve at all). `ReviewFamilySideName`
(`:82`) admits only the model's own two sides, so a rendering never maps a spelling;
`ReviewFamilySideState` (`:89`) names the four distinct facts one side can be in — `recorded`,
`not_recorded`, `not_resolved`, `unreadable` — and none of them is an empty roster;
`ReviewFamilyEntryState` (`:95`) names one family's own four states.

**The join key and the owner names are values rather than prose.** `FAMILY_CONTEXT_JOIN_KEY` (`:101`) is
`invariant_revision_id`, the one key every evidence and assessment owner already publishes for a member
record, so a rendering that joined on a display label or a path instead would be inventing the
association. `RELATIONSHIP_UNION_OWNER` through `APPLICABILITY_OWNER` (`:106-111`) name the collections
this context points into — the relationship union, the source inventory, evidence links, observations,
assessments and applicability — and each keeps its own status dimension, its own counts and its own
refusal; nothing here copies any of them or concludes anything from them.

**One family revision's guarantee travels whole.** `ReviewFamilyGuarantee` (`:114-131`) carries the
family's own stored `joint_guarantee` with its `display_version`, its `state_at_origin`, its
`acceptance_ref`, its `provenance` and its `payload_digest`. `state_at_origin` and `acceptance_ref`
travel together because an accepted origin without the authority that accepted it would be an
acceptance nobody recorded. There is no field for a derived summary and no field that could hold a
verdict about whether the guarantee still holds.

**A source reference carries its address and its observation, or neither — and it is declared next
door.** `ReviewFamilyMemberSource`, its `ReviewSourceLocatorState` and the `source_locator_state` rule
live in `models/knowledge/review_family_source.py` and are imported and re-exported here unchanged, so
every existing import from this module keeps working (a pure extraction that kept this module under the
600-line pressure line). The reference is one recorded realization claim: the claim's own identity, its
stored role and rationale (both required), the address this read observed, and — per side and per
claim — the anchor's structured recorded `locator`, the `resolved_ranges` the side's anchor resolver
placed it on in that side's exact recorded blob, and a `locator_state` (`resolved` / `whole_file` /
`unresolved` / `not_observed`). Its validators refuse an address without its observation, a locator
without its address, ranges beside any resolution other than `exact_recorded_blob`, and a state that
disagrees with the locator, ranges and resolution carried beside it. See that module's card for the rule.
Whether the address resolves still stays with the source inventory and the relationship union; `detail`
states the absence rather than leaving an empty resolution to be read as agreement, and no region is ever
read back out of it.

**A member is one canonical revision, referenced wherever it is recorded.**
`ReviewFamilyMember` (`:166-222`) carries the membership row's own `member_id` beside the exact
`invariant_revision_id` the row cites, so the same revision recorded under two families is *one*
identity referenced twice rather than one fact copied twice, and `other_family_revision_ids` makes that
sharing inspectable from either context. `movement_reference` is the recorded membership identity the
payload's own relationship union displays for this association, or absent when that union's page did not
reach the row; the movement itself — its transition, its pairing basis, its lineage — is the union's
value and is never restated here. The validator
(`_require_the_content_state_to_match_the_content`, `:198-222`) refuses three shapes: a member presented
as read while its content is missing, content beside `content_not_on_page`, and a movement reference
naming an identity other than this row's own.

**A roster page cannot be read as the whole roster when it is a position in one.**
`ReviewFamilyRosterPage` (`:225-277`) carries the read owner's own `counts` value whole, its own
`complete` flag, the measured `members_total`, and the cursor that reaches the rest.
`complete` describes the **WALK and not the page**, which this delta's docstring paragraph states
explicitly: it is `True` once the read has enumerated the whole selected scope, and for a multi-page
walk that happens on the **final** page — a page that carries only its own share of the selection while
the pages before it carried the rest. So a complete page is *the roster, whole* exactly when it is also
a single page (`state == "first_page"`), and that is the only case in which the guard below holds a page
to the revision-wide count.
`_require_the_cursor_and_the_remainder_to_agree` (`:255-277`) refuses five disagreements: a complete
enumeration carrying a continuation or an incomplete one carrying none; a continued page that names no
cursor it continued; a page reporting items ahead with no way to reach them; and a `members_total` that
is not the read owner's own `memberships_total`.

**The recorded history a selection was chosen from is published beside the selection.**
`ReviewFamilyRevisionContext` (`:280-356`) is one snapshot's context for one family.
`recorded_revision_ids` (`:303`) is the family owner's own list of **every** revision that snapshot
records — a deliberately different population from the revisions a selection reached, because a family
revision that cites no member is recorded history a reviewer may open even though no membership row
reached it (this is the fix-round-1 field: a sentence counting only the selected population printed zero
while the store recorded further revisions of the same family).
`_require_the_state_to_match_what_it_carries` (`:310-356`) keeps the state and the payload one fact: a
recorded side names its exact revision and that revision's own guarantee and carries the page it read; a
recorded side's selected revision must be **one of the revisions the family owner records** (`:323-328`,
the validator that makes an unrecorded selection unreachable); a side that read nothing carries no
members and counts none; and a roster **the read took in one page** carries every membership the owner
counted, never fewer. That last clause is this delta's correction and it is narrow on purpose: the guard
is `single_page_walk = self.page.complete and self.page.state == "first_page"`, so a completed
**continued** page is not compared against the revision-wide count — comparing a page-scoped list with a
revision-wide count refuses a page that is entirely truthful, and doing it answered an ordinary
multi-page roster's own continuation request with an unhandled failure. The truncation the guard exists
for is still refused, because a complete page that continued nothing *is* the whole roster; and the
separate `len(self.members) > self.members_total` bound is untouched.

**An entry's selection, candidates and sides are one fact.**
`ReviewFamilyContextEntry` (`:359-443`) carries `selection` in `ICR-R07@v1`'s own value and vocabulary
and `candidates` only for the two states that chose nothing, each candidate carrying **its own**
guarantee so a reader inspects the heads rather than being shown one of them as the answer.
**Since MIK-L33** the entry also carries the optional `change_kinds: ReviewFamilyChanges`, the change facts of a tree
comparison (MIK-R33; `models/knowledge/review_change_kinds.py`), `None` on a dataset review.
`_require_change_facts_for_exactly_the_returned_members` refuses facts that do not describe exactly the member
occurrences this page returned on either side: a returned member without facts would read as unbadged, and facts for
a member no page returned would describe a population the roster did not carry.
`_require_the_entry_to_describe_one_family` (`:379-393`) pins the selection to the family it carries and
requires one context per snapshot side. `_require_the_state_to_match_its_candidates_and_sides`
(`:395-443`) refuses a chosen revision presented beside a selection that chose none, an ambiguity
carrying no inspectable candidate, a complete context built on a selection that established no pair, and
— the clause the accepted reviewer depends on — a guarantee presented as a family's own on an
unresolved selection (`:428-432`). It also requires an `added` family's before side and a `removed`
family's after side to be exactly `not_recorded`.

`ReviewFamilyContextReferences` (`:446-465`) is where each independent fact beside the context is owned,
with the join key; its `detail` states that this context references them by identity and draws no
conclusion from any of them.

**The context's counts are checked against the entries beside them.**
`ReviewFamilyContext` (`:468-548`) carries the entries, the measured `families_total` /
`families_returned` / `families_remaining`, the two membership counts, the references and the
limitations. `_require_the_family_counts_to_describe_the_entries` (`:493-548`) refuses a remainder with
no way to reach it (which is what `ICR-R10@v1` forbids), a returned count that is not the number of
entries carried, a state other than `partial` claiming a remainder, a `recorded` context carrying any
incomplete family, entries beside a measured zero or a subjectless review, an empty `recorded`/`partial`
context (which must say `no_family_recorded` instead), a `membership_rows_total` that is not the sum of
the rosters carried, and a `unique_member_revision_total` inflated by counting rows where it must count
distinct member revisions.

### Conventions

Every value extends `KnowledgeModel` and takes its bounds from `models/knowledge/base.py`
(`LABEL_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`, `SHA256_PATTERN`). The module
imports only value types it embeds — `KnowledgeReadCounts` from `models/knowledge/read.py`,
`ReviewRevisionSelection` from `models/knowledge/revision_selection.py`, and the member-source reference
from `models/knowledge/review_family_source.py` — and defines no behaviour beyond its validators.
`__all__` publishes the fifteen names the composition, the roster read, the review payload and the
transport consume, in one alphabetical list, including the two re-exported source-reference names
`ReviewSourceLocatorState` and `source_locator_state`. Collection fields default to `()` and optional
scalars to `None`, so a caller constructing a value states what it read and omits what it did not.

### Invariants And Boundaries

- **No field can hold a conclusion about a member's consequence for its family's guarantee.** The five
  status dimensions the packet names — the member's statement, the recorded relationships, the
  mechanical source changes, the execution observations and the authored assessments — are referenced
  by owner name and join key only; a member change therefore makes its family context *available*
  without becoming a computed claim about the guarantee.
- **A guarantee is never assembled from members and never rewritten when one changes.** It is one
  immutable family revision's stored text with that revision's own seal.
- **The measured zero is not the empty collection.** `no_family_recorded` carries no entries by
  validator (`:515-522`), and an empty `recorded` context is refused, so a read that happened and found
  nothing is never indistinguishable from a read that never happened.
- **The recorded revision list is the family owner's, not the selection's.** `recorded_revision_ids`
  exists so a reader can see the whole recorded history the selected revision was chosen from, and a
  recorded side is required to be a member of it.
- **A page is never compared against a population it does not claim to be.** `complete` is the walk's
  flag, so the roster guard holds only a **single-page** walk (`complete and state == "first_page"`) to
  the revision-wide count; a completed **continued** page carries its own share by construction and is
  accepted, while the same carried rows on a walk's first page are still refused. Nothing about the
  truncation the guard exists for was relaxed.
- **Change facts describe exactly the returned members (MIK-L33).** The entry validator ties `change_kinds` to the
  member occurrences the page carried, so the facts never imply a member no page returned (part of the candidate
  invariant recorded on `application/review_change_kinds.py.md`).
- **No schema or store authority.** This module declares value shapes over facts other owners hold; it
  reads no store, derives no grouping and publishes nothing.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.

### Repo-Internal References

Every claim on this card is checkable in the module's own declarations and in the owners the
composition calls. The five details a reader should carry: **the four side states are four distinct
facts and none of them is an empty roster**; **`no_family_recorded` is a measured zero of the family
population and is refused any entries**; **`recorded_revision_ids` is the family owner's own list, and a
recorded side must be one of its members**; **`complete` is the walk's flag and not the page's, so the
roster guard holds only a single-page walk to the revision-wide count and a completed continued page is
a position in a walk rather than a truncated whole**; and **no field in this module can hold a
Changed/Passed conclusion, so a member change cannot be rendered as a claim about its family's
guarantee**.

- **The four refusals this vocabulary encodes: an authored guarantee never assembled from members, a membership citing one exact family revision and one exact member revision, a side stating which snapshot fact it is, and five status dimensions that never collapse.** (historical reference 1)
- The published surface: the fifteen names the composition, the roster read, the payload and the transport consume. (historical reference 2)
- **The five states one review's family context can be in, and why the measured zero is deliberately not spelled `empty`.** (historical reference 3)
- The two snapshots a side context or a label may name, so no value can name a third. (historical reference 4)
- **The four distinct facts one side can state — `recorded`, `not_recorded`, `not_resolved`, `unreadable` — none of them an empty roster.** (historical reference 5)
- One family's own four states, including the unresolved one that chose no revision. (historical reference 6)
- **The one key that joins a member context to the evidence and assessment owners' own collections, so a rendering cannot join on a label or a path.** (historical reference 7)
- **The owners this context points into rather than copying: the relationship union, the source inventory, evidence links, observations, assessments and applicability.** (historical reference 8)
- One family revision's authored joint guarantee with its display version, origin state, acceptance reference, provenance and payload seal. (historical reference 9)
- **One recorded realization claim as an inspectable source reference, with its structured locator, resolved ranges and locator state, imported from its own module and re-exported here.** (historical reference 10)
- **The validator refusing an address without its observation or its locator, so a reference never reads as a resolved realization.** (historical reference 11)
- One recorded membership carrying its exact member revision and the other family revisions that revision is recorded in. (historical reference 12)
- **The validator keeping a member's stated content state and the content it carries one fact, and pinning a movement reference to the row's own recorded identity.** (historical reference 13)
- The read owner's own window of one family revision's roster: its counts, its completeness and the cursor that reaches the rest. (historical reference 14)
- **The docstring paragraph stating that `complete` is the WALK's flag and not the page's, so a completed continued page is a position in a walk and only a single page may be read as the roster whole.** (historical reference 15)
- **The validator refusing a truncated roster presented as a complete one, and a member total that is not the read owner's own count.** (historical reference 16)
- One snapshot's context for one family: the selected revision, its guarantee, the roster page it carried and the family owner's own recorded revision list. (historical reference 17)
- **The family owner's own list of every revision the snapshot records — a different population from the revisions a selection reached, which is the fix-round-1 field.** (historical reference 18)
- **The validator requiring a recorded side to name the revision it read and carry the page it read, requiring that revision to be one the family owner records, and — this delta's correction — holding only a single-page walk (`complete and state == "first_page"`) to the revision-wide member count.** (historical reference 19)
- One family's full context: both snapshot sides, the explicit revision selection and the candidate guarantees of an unresolved lineage. (historical reference 20)
- The validator pinning an entry's selection to the family it carries and its two sides to the two snapshots. (historical reference 21)
- **The validator refusing a chosen revision beside a selection that chose none, an ambiguity with no inspectable candidate, and a guarantee presented as a family's own on an unresolved selection.** (historical reference 22)
- Where each independent fact beside this context is owned, and the key that joins them. (historical reference 23)
- The comparison-bound family context of one review: its entries, its measured counts, its references and its limitations. (historical reference 24)
- **The validator refusing a claimed remainder with no way to reach it, counts that do not describe the entries beside them, and a unique member total inflated by counting rows.** (historical reference 25)
- **The composition that builds this value, from the two snapshots, the reviewed selector and the shipped read operation.** (historical reference 26)
- The roster read that supplies each side's guarantee, its members and its page. (historical reference 27)
- **The production review read that composes the context once and carries it on the payload.** (historical reference 28)
- The payload field itself, required rather than optional so an absent field can never be read as a measured zero. (historical reference 29)
- The task-context review, which states `no_subject_selected` because it compared no knowledge operand. (historical reference 30)
- The values cases that pin the construction rules this module enforces. (historical reference 31)
- On a tree comparison the entry carries the change facts of exactly its returned members (MIK-L33). (historical reference 32)
- The facts' model. (historical reference 33)

### Cross-Repo References

No cross-repository behavior is implemented in this module. Every value it declares describes a
comparison this same repository's own review surfaces compose, over two knowledge datasets its own
resolution selected and a selector its own request named. No remote, credential, network or external
system appears in any shape here, so no cross-repo reference row is recorded — no cited range proves a
repository or external-system boundary.

</details>

## Evidence

No Domain Documentation entries are configured. Current declarations, direct producer boundaries
and the named stored value assertion were inspected; no test execution is asserted here.

- The current model carries family/member/selection state and rejects inconsistent combinations; its retained creation-era header is not evidence of a surviving assessment or observation collection. [1]
- The published surface: the fifteen names the composition, the roster read, the payload and the transport consume. [2]
- **The five states one review's family context can be in, and why the measured zero is deliberately not spelled `empty`.** [3]
- The two snapshots a side context or a label may name, so no value can name a third. [4]
- **The four distinct facts one side can state — `recorded`, `not_recorded`, `not_resolved`, `unreadable` — none of them an empty roster.** [5]
- One family's own four states, including the unresolved one that chose no revision. [6]
- Member contexts carry invariant_revision_id as their join key; this does not resurrect evidence/assessment owners removed from the current references value. [7]
- The surviving referenced collections are source.relationships and source.inventory; removed evidence, observation, assessment and applicability owner constants are not current destinations. [8]
- A supplied family guarantee carries authored text and origin/seal fields; this model does not itself authenticate them or enforce an acceptance-ref pair from the origin-state string. [9]
- **One recorded realization claim as an inspectable source reference, with its structured locator, resolved ranges and locator state, imported from its own module and re-exported here.** [10]
- **The validator refusing an address without its observation or its locator, so a reference never reads as a resolved realization.** [11]
- One recorded membership carrying its exact member revision and the other family revisions that revision is recorded in. [12]
- **The validator keeping a member's stated content state and the content it carries one fact, and pinning a movement reference to the row's own recorded identity.** [13]
- The read owner's own window of one family revision's roster: its counts, its completeness and the cursor that reaches the rest. [14]
- The roster docstring distinguishes end-of-enumeration from the population carried by one page; returned equals total is the stated all-members observation. [15]
- **The validator refusing a truncated roster presented as a complete one, and a member total that is not the read owner's own count.** [16]
- One snapshot's context for one family: the selected revision, its guarantee, the roster page it carried and the family owner's own recorded revision list. [17]
- **The family owner's own list of every revision the snapshot records — a different population from the revisions a selection reached, which is the fix-round-1 field.** [18]
- The side-context validator keeps recorded state/revision/guarantee/page together and compares the full roster size only on a complete first page, not a completed continued page. [19]
- One family's full context: both snapshot sides, the explicit revision selection and the candidate guarantees of an unresolved lineage. [20]
- The validator pinning an entry's selection to the family it carries and its two sides to the two snapshots. [21]
- **The validator refusing a chosen revision beside a selection that chose none, an ambiguity with no inspectable candidate, and a guarantee presented as a family's own on an unresolved selection.** [22]
- Where each independent fact beside this context is owned, and the key that joins them. [23]
- The comparison-bound family context of one review: its entries, its measured counts, its references and its limitations. [24]
- Context checks compare returned counts and roster sums, and compute unique member-revision total from a set; this local arithmetic is not proof that input identities were authenticated or unique. [25]
- The family-context composition owner supplies its comparison-bound result from the selected records and roster owner. [26]
- The roster read that supplies each side's guarantee, its members and its page. [27]

- The review composition carries the family-context result on its payload; this reference is static composition structure, not an executed read count. [28]

- The payload field itself, required rather than optional so an absent field can never be read as a measured zero. [29]

- The task-context review, which states `no_subject_selected` because it compared no knowledge operand. [30]

- The stored value regression rejects a recorded family selection naming a revision outside the recorded list; this is an inspected assertion, not fresh execution. [31]
- The local change-facts guard compares the returned/described member-ID sets; that comparison alone does not establish occurrence multiplicity or measured code classification. [32]
- The facts' model. [33]
