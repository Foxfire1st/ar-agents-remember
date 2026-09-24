# mcp/src/agents_remember/models/knowledge/review_family_context.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_family_context.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T02:20:00+02:00 |
| lastVerifiedCommitHash | `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` |
| lastVerifiedCommitDate | 2026-09-24T02:30:06+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

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

**A source reference carries its address and its observation, or neither.**
`ReviewFamilyMemberSource` (`:134-163`) is one recorded realization claim: the claim's own identity, the
author's recorded role and rationale, and the address this read observed. Its validator
(`_require_an_address_to_travel_with_its_observation`, `:155-163`) refuses the two halves apart, because
an address without an observation reads as a resolved realization while a resolution without an address
names nothing. Whether the address resolves stays with the source inventory and the relationship union;
`detail` states the absence rather than leaving an empty resolution to be read as agreement.

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
(`LABEL_MAX_LENGTH`, `PATH_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`,
`SHA256_PATTERN`). The module imports only value types it embeds — `KnowledgeReadCounts` from
`models/knowledge/read.py` and `ReviewRevisionSelection` from
`models/knowledge/revision_selection.py` (`:46-47`) — and defines no behaviour beyond its validators.
`__all__` (`:49-63`) publishes the thirteen names the composition, the roster read, the review payload
and the transport consume, in one alphabetical list. Collection fields default to `()` and optional
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
- **No schema or store authority.** This module declares value shapes over facts other owners hold; it
  reads no store, derives no grouping and publishes nothing.

### Todos

None recorded.

## Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.

## Repo-Internal References

Every claim on this card is checkable in the module's own declarations and in the owners the
composition calls. The five details a reader should carry: **the four side states are four distinct
facts and none of them is an empty roster**; **`no_family_recorded` is a measured zero of the family
population and is refused any entries**; **`recorded_revision_ids` is the family owner's own list, and a
recorded side must be one of its members**; **`complete` is the walk's flag and not the page's, so the
roster guard holds only a single-page walk to the revision-wide count and a completed continued page is
a position in a walk rather than a truncated whole**; and **no field in this module can hold a
Changed/Passed conclusion, so a member change cannot be rendered as a claim about its family's
guarantee**.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The four refusals this vocabulary encodes: an authored guarantee never assembled from members, a membership citing one exact family revision and one exact member revision, a side stating which snapshot fact it is, and five status dimensions that never collapse.** | "A guarantee is the family's own authored text, never assembled from members." | mcp/src/agents_remember/models/knowledge/review_family_context.py:1-30 |
| The published surface: the thirteen names the composition, the roster read, the payload and the transport consume. | `__all__` | mcp/src/agents_remember/models/knowledge/review_family_context.py:49-63 |
| **The five states one review's family context can be in, and why the measured zero is deliberately not spelled `empty`.** | `ReviewFamilyContextState` | mcp/src/agents_remember/models/knowledge/review_family_context.py:72-78 |
| The two snapshots a side context or a label may name, so no value can name a third. | `ReviewFamilySideName` | mcp/src/agents_remember/models/knowledge/review_family_context.py:82-82 |
| **The four distinct facts one side can state — `recorded`, `not_recorded`, `not_resolved`, `unreadable` — none of them an empty roster.** | `ReviewFamilySideState` | mcp/src/agents_remember/models/knowledge/review_family_context.py:89-89 |
| One family's own four states, including the unresolved one that chose no revision. | `ReviewFamilyEntryState` | mcp/src/agents_remember/models/knowledge/review_family_context.py:95-95 |
| **The one key that joins a member context to the evidence and assessment owners' own collections, so a rendering cannot join on a label or a path.** | `FAMILY_CONTEXT_JOIN_KEY` | mcp/src/agents_remember/models/knowledge/review_family_context.py:101-101 |
| **The owners this context points into rather than copying: the relationship union, the source inventory, evidence links, observations, assessments and applicability.** | `RELATIONSHIP_UNION_OWNER`; `SOURCE_INVENTORY_OWNER`; `EVIDENCE_LINKS_OWNER`; `OBSERVATIONS_OWNER`; `ASSESSMENTS_OWNER`; `APPLICABILITY_OWNER` | mcp/src/agents_remember/models/knowledge/review_family_context.py:106-111 |
| One family revision's authored joint guarantee with its display version, origin state, acceptance reference, provenance and payload seal. | `ReviewFamilyGuarantee` | mcp/src/agents_remember/models/knowledge/review_family_context.py:114-131 |
| One recorded realization claim as an inspectable source reference. | `ReviewFamilyMemberSource` | mcp/src/agents_remember/models/knowledge/review_family_context.py:134-163 |
| **The validator refusing an address without its observation, so a reference never reads as a resolved realization.** | `_require_an_address_to_travel_with_its_observation` | mcp/src/agents_remember/models/knowledge/review_family_context.py:155-163 |
| One recorded membership carrying its exact member revision and the other family revisions that revision is recorded in. | `ReviewFamilyMember` | mcp/src/agents_remember/models/knowledge/review_family_context.py:166-222 |
| **The validator keeping a member's stated content state and the content it carries one fact, and pinning a movement reference to the row's own recorded identity.** | `_require_the_content_state_to_match_the_content` | mcp/src/agents_remember/models/knowledge/review_family_context.py:198-222 |
| The read owner's own window of one family revision's roster: its counts, its completeness and the cursor that reaches the rest. | `ReviewFamilyRosterPage` | mcp/src/agents_remember/models/knowledge/review_family_context.py:225-277 |
| **The docstring paragraph stating that `complete` is the WALK's flag and not the page's, so a completed continued page is a position in a walk and only a single page may be read as the roster whole.** | "``complete`` describes the WALK, not the page." | mcp/src/agents_remember/models/knowledge/review_family_context.py:237-244 |
| **The validator refusing a truncated roster presented as a complete one, and a member total that is not the read owner's own count.** | `_require_the_cursor_and_the_remainder_to_agree` | mcp/src/agents_remember/models/knowledge/review_family_context.py:255-277 |
| One snapshot's context for one family: the selected revision, its guarantee, the roster page it carried and the family owner's own recorded revision list. | `ReviewFamilyRevisionContext` | mcp/src/agents_remember/models/knowledge/review_family_context.py:280-356 |
| **The family owner's own list of every revision the snapshot records — a different population from the revisions a selection reached, which is the fix-round-1 field.** | `recorded_revision_ids` | mcp/src/agents_remember/models/knowledge/review_family_context.py:303-303 |
| **The validator requiring a recorded side to name the revision it read and carry the page it read, requiring that revision to be one the family owner records, and — this delta's correction — holding only a single-page walk (`complete and state == "first_page"`) to the revision-wide member count.** | `_require_the_state_to_match_what_it_carries` | mcp/src/agents_remember/models/knowledge/review_family_context.py:310-356 |
| One family's full context: both snapshot sides, the explicit revision selection and the candidate guarantees of an unresolved lineage. | `ReviewFamilyContextEntry` | mcp/src/agents_remember/models/knowledge/review_family_context.py:359-443 |
| The validator pinning an entry's selection to the family it carries and its two sides to the two snapshots. | `_require_the_entry_to_describe_one_family` | mcp/src/agents_remember/models/knowledge/review_family_context.py:379-393 |
| **The validator refusing a chosen revision beside a selection that chose none, an ambiguity with no inspectable candidate, and a guarantee presented as a family's own on an unresolved selection.** | `_require_the_state_to_match_its_candidates_and_sides` | mcp/src/agents_remember/models/knowledge/review_family_context.py:395-443 |
| Where each independent fact beside this context is owned, and the key that joins them. | `ReviewFamilyContextReferences` | mcp/src/agents_remember/models/knowledge/review_family_context.py:446-465 |
| The comparison-bound family context of one review: its entries, its measured counts, its references and its limitations. | `ReviewFamilyContext` | mcp/src/agents_remember/models/knowledge/review_family_context.py:468-548 |
| **The validator refusing a claimed remainder with no way to reach it, counts that do not describe the entries beside them, and a unique member total inflated by counting rows.** | `_require_the_family_counts_to_describe_the_entries` | mcp/src/agents_remember/models/knowledge/review_family_context.py:493-548 |
| **The composition that builds this value, from the two snapshots, the reviewed selector and the shipped read operation.** | `review_family_context` | mcp/src/agents_remember/application/review_family_context.py:254-301 |
| The roster read that supplies each side's guarantee, its members and its page. | `read_family_roster` | mcp/src/agents_remember/application/review_family_rosters.py:209-272 |
| **The production review read that composes the context once and carries it on the payload.** | `compose_review` | mcp/src/agents_remember/application/knowledge_review.py:371-611 |
| The payload field itself, required rather than optional so an absent field can never be read as a measured zero. | `family_context` | mcp/src/agents_remember/models/knowledge/review.py:1035-1035 |
| The task-context review, which states `no_subject_selected` because it compared no knowledge operand. | `task_context_review` | mcp/src/agents_remember/application/review_task_context.py:93-191 |
| The values cases that pin the construction rules this module enforces. | `test_a_recorded_side_may_not_name_a_revision_its_family_does_not_record` | mcp/tests/test_review_family_context_values.py:95-111 |

## Cross-Repo References

No cross-repository behavior is implemented in this module. Every value it declares describes a
comparison this same repository's own review surfaces compose, over two knowledge datasets its own
resolution selected and a selector its own request named. No remote, credential, network or external
system appears in any shape here, so no cross-repo reference row is recorded — no cited range proves a
repository or external-system boundary.

## Update History

- 2026-09-24T02:20:00+02:00 — 260921-ICR-L31 curator, **reopened enclosure** (`260921-icr-l31b`, same base `fdf3e4b6cfe73040d35cbfd4d8b93fd55369e499`): **the roster page's completion semantics on this card were corrected, and every range was re-anchored past this delta's insertions.** The reopen's subject is that `complete` describes the **WALK and not the page**: `ReviewFamilyRosterPage`'s docstring paragraph (`:237-244`) now says so, and `_require_the_state_to_match_what_it_carries` (`:310-356`) holds only a **single-page** walk — `single_page_walk = self.page.complete and self.page.state == "first_page"` — to the revision-wide member count. The card previously read "a complete page carries every membership the owner counted, never fewer", which was the pre-correction rule and is **false for a completed continued page**; it now states the corrected rule and says explicitly that nothing about the truncation the guard exists for was relaxed (a complete page that continued nothing *is* the whole roster, so the same carried rows on a walk's first page are still refused). What did **not** change: no new field, `Literal` state, capability, policy or signature; `complete`'s own meaning (`enumeration_complete`, the read owner's flag) is untouched and this module only *reads* it; the `len(members) > members_total` bound is untouched. Every range was re-measured on the candidate bytes (`ReviewFamilyRosterPage` `:225-277`, `ReviewFamilyRevisionContext` `:280-356`, `ReviewFamilyContext` `:468-548`, and the prose clauses at `:323-328`, `:428-432`, `:515-522`), and one reference row was added for the corrected docstring paragraph. **Stamp accounting: no verification stamp was advanced.** The header's pair still names this leaf's base `fdf3e4b6`, because the candidate is uncommitted and the governed closeout owns the real code and memory commits; the verified basis is that base plus the working-tree delta, exactly as the first curation recorded it. *Note for the reader:* this card describes the corrected semantics only. The pre-correction comparison was a real defect — it produced an unhandled server failure on an ordinary multi-page roster — and the source's own comments record it as fixed; the sentence on the older class docstring that still read "a complete page carries all of it" was corrected on these bytes after independent verification flagged it.

- 2026-09-23T22:10:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): created this one-to-one card for the value vocabulary `ICR-R31@v1` introduced as **the comparison-bound family review context**, so the accepted reviewer can inspect a family's guarantee and its member obligations together. The stamp basis is honest rather than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf's base commit, and the verified basis is the working-tree delta on top of it — no commit contains what a stamp would otherwise claim to have verified. The card records what a consumer has to act on: the four side states are four distinct facts and none of them is an empty roster, `no_family_recorded` is a **measured zero** of the family population and the validator refuses it any entries, and `recorded_revision_ids` is the family owner's own list of every revision a snapshot records — a different population from the revisions a selection reached, which was the leaf's one real defect and is why a recorded side is now required by validator to be a member of that list (`:323-328`). No field here can hold a Changed/Passed conclusion: the five status dimensions the packet names are referenced by owner name and join key only, so a member change makes its family context available without becoming a computed claim about its family's guarantee.
