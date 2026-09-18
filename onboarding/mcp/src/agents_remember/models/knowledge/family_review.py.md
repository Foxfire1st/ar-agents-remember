# mcp/src/agents_remember/models/knowledge/family_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/family_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:18+02:00 |
| lastVerifiedCommitHash |  `9f88a6de572dc15bbed1802cf08b77c1193fb24c`|
| lastVerifiedCommitDate |  2026-09-18T14:21:49+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The family-review pipeline's own vocabulary: the records `KS-R16@v1`'s pipeline produces between
`KS-R14@v1`'s detector, `KS-R15@v1`'s authored record and `KS-R17@v1`'s authored composition, and none
of the others' redefined — a detection signal stays a detection signal, an assessment stays an
assessment, an authored edge stays an authored edge. It declares the grouped fact and the match that
supports it, the five separated status owners with their own closed vocabularies, the per-record
currentness answer, the routing report with its rows, and the one recorded gate-consequence decision.
**It owns no computation over stored state and no gate.** Its only non-stdlib imports are pydantic and
the two sibling model modules whose vocabulary it repeats; its two module-level functions render a
constant rule and derive a key; and no field anywhere in it could hold one verdict, badge or boolean.

## Code Commentary

### Logic

**Four properties are enforced by the shape of these records rather than by a rule a caller
remembers.** A fact group cannot carry a conclusion: its declared field set contains no name from
`CONCLUSION_BEARING_FIELD_NAMES`, and `KS-R14@v1`'s own `conclusion_bearing_fields` review is the
measurement. The five status owners stay separate, because `SeparatedStatusReport` carries exactly one
entry per owner in the declared order and has no field for one verdict. Missing stays missing, because
the curator vocabulary reports `no-record-recorded` and has no "compatible" member and no default. And
currentness is per-input and never re-judged, because `FindingCurrentness` carries the recorded
comparison's own result, the identities that moved, and typed statements that the record stays readable
and nothing was reinterpreted for the new inputs.

**The grouping vocabulary is one declared rule with an identity, and it is deliberately mechanical.**
`FACT_GROUPING_POLICY_VERSION` is `family-fact-grouping/v1`, `fact_grouping_rule()` renders the rule as
the one sentence a record and its refusal both quote, and `fact_group_identity(subject_id,
input_signature)` returns `family-review/{subject_id}/{input_signature}` — a name for a merge rather
than a content address, since no digest, fingerprint or new identity authority is introduced. The rule
merges matches whose recorded family revisions and declared input snapshots agree, retains every
matched condition with its supporting paths and edges, and orders groups by the declared condition
order and then item identity; nothing in it reads a path, a label or a count to decide membership.

**The match and the group are the facts, and retention is a comparison rather than an assurance.**
`FactSupportingEdge` is one recorded relationship a match was reached through — `edge_kind`,
`from_record_id`, `to_record_id` and an optional `mapping_snapshot` — kept because grouping may not
drop it. `FactMatch` carries the closed `DetectionCondition` plus the sides and the three supporting
tuples (paths, edges, item ids), and its validator refuses a condition outside the policy's vocabulary.
`FamilyIntegrityFactGroup` carries `group_id`, `subject_id`, `family_revision_ids`, `input_signature`,
`grouping_policy_version`, at least one `matches` entry, and `review_record_ids` — a citation of records
that exist, whose empty tuple is the honest report of a subject nobody has reviewed and never a default
to a favourable state. `matched_conditions()`, `supporting_paths()` and `supporting_edges()` render the
group's facts in the declared condition order, a deduplicated sorted order and a stable recorded order;
`retains(contributing)` is §2.2's review, asking for every contributing match whether a kept match of
the same condition still carries its supporting paths and supporting item ids.

**Five owners, five vocabularies, and no combined verdict.** `PIPELINE_STATUS_OWNERS` names the five
owners of `Doc13:363-369` in the design's own order — structural validator, detector, curator reviewer,
verification runner, authority currentness — and `STATUS_OWNER_DECLARATIONS` gives each one its members,
the sentence stating what it establishes and the sentence stating what it does not.
`STATUS_VOCABULARIES` is derived from that table rather than restated. `PipelineStatusEntry` requires
both sentences to be nonblank and validates the status against **its own owner's** members, so one owner
cannot report another's fact; `SeparatedStatusReport` requires exactly one entry per owner in the
declared order, refusing an omitted owner as a collapse and a repeated one as "two facts wearing one
row", and `entry_for(owner)` is the keyed lookup that rule makes safe.

**Currentness records a comparison and refuses to re-judge it.** `binding_state` is `KS-R14@v1`'s own
two-member literal — `current` or `stale` — so the design's spelling stays one spelling across the
substrate; `moved_identities` names the inputs that no longer match, because "one input moved" and "the
binding is stale" are different facts. The validator derives the expected state from `moved_identities`
and refuses both directions, and refuses `reuse_permitted` on a stale binding: the recovery is a new
authored record, not a reinterpretation. `record_readable` is `Literal[True]` and
`reinterpreted_for_new_inputs` is `Literal[False]`, so a stale record cannot be recorded as unreadable
or as re-judged for the new inputs.

**The routing report decides no gate.** `FamilyReviewRoutingRow` carries one group's subject, its group
identity, a `matched_condition_count` of at least one and the records already stored, and its
`routes_to` defaults to the two declared surfaces; a third surface fails construction as a second
worklist. `FamilyReviewRouting` carries the shipped formula's three terms — `repair_count`,
`missing_count`, `stale_count` — beside `actionable_count`, the family-review row count as a **separate**
number, and `decides_closeout_readiness`, whose only admissible value names the
curator-coherence authority validator that actually decides closeout readiness. Its validator refuses a
row count that is not the rows it carries and an actionable count that is not the three-term sum, so a
fourth term has no way to arrive, and `family_rows_are_report_only()` is the property a caller asserts.

**The gate-consequence question is answered by one recorded decision that names its owner.**
`DecisionOwner` carries the role, the durable `identity_ref` a reader follows and the `ruling_basis`
sentence that makes the ownership a fact; `FamilyReviewGateDecision` carries the question, the outcome,
the owner, the rationale, a non-empty `authority_basis` with no blank entry, `effective_from`,
`revisit_when` and `creates_gate: Literal[False]` — and no field for a gate, a refusal code, a checklist
status value or a readiness input. `RECORDED_GATE_CONSEQUENCE_DECISION` is the one module-level record:
it records that an outstanding signal is report-only, that a finding routes into the existing
curator-coherence assessment collection and the report-only `knowledgeReview` section, and that a future
gate consequence needs an explicit requirement and the developer's ruling on it, naming the master's
decision log as the reference and the condition under which a later ruling supersedes it.

### Conventions

Every shape derives from `KnowledgeModel`, so `extra="forbid"` and `frozen=True` are what refuse a
payload arriving with an undeclared field — a verdict, a fifth status, a fourth count. Bounded text
reuses the base constants rather than literals: `LABEL_MAX_LENGTH` for labels, kinds and owners,
`REFERENCE_MAX_LENGTH` for identities and group keys, `PATH_MAX_LENGTH` for a durable home,
`PROSE_MAX_LENGTH` for the two required sentences and the decision's prose. Declarations that must agree
are one declaration: `STATUS_VOCABULARIES` is built from `STATUS_OWNER_DECLARATIONS`, and
`decides_closeout_readiness`'s literal and `CLOSEOUT_READINESS_DECIDER` spell the same string. The
vocabularies that belong to other leaves are imported and repeated rather than re-declared —
`DetectionCondition`, `DetectionSide` and `DETECTION_CONDITIONS` from `models/knowledge/detection.py` —
and `__all__` names the nineteen public names this module adds (seven constants, ten model classes, two
functions). Rules a reader would otherwise have to remember are written as module values that travel on
records: the grouping rule's version travels on every group.

### Invariants And Boundaries

- **A fact group cannot carry a conclusion.** `FactMatch` and `FamilyIntegrityFactGroup` declare no
  field whose name appears in `CONCLUSION_BEARING_FIELD_NAMES`; `conclusion_bearing_fields` returns the
  empty tuple for both, which is the shipped, checkable form of that property.
- **The retention review compares paths and supporting item ids.** `retains` requires, for every
  contributing match, a kept match of the same condition whose `supporting_paths` and
  `supporting_item_ids` are supersets; a dropped path, item id or contributing match answers `False`.
  `supporting_edges` is retained on the match and aggregated by `supporting_edges()`, but is not one of
  the two comparisons the predicate makes.
- **Five owners, five vocabularies, no merged verdict.** The report validates its owners against
  `PIPELINE_STATUS_OWNERS` (order included) and each entry against its own owner's members; there is no
  single-verdict, badge or boolean field to collapse them into, and a missing owner is a refusal rather
  than an omitted row.
- **Missing is reported, never defaulted.** The curator vocabulary has `no-record-recorded` and no
  "compatible" member, and an empty `review_record_ids` is the report of a subject nobody reviewed —
  the promotion `Doc13:104` forbids is not a shape these records can take.
- **Currentness follows from the comparison, in both directions.** A moved identity forces `stale`, a
  `stale` binding with nothing moved is refused, and a stale binding may not carry
  `reuse_permitted=True`; `reinterpreted_for_new_inputs` is `Literal[False]`.
- **The routing report decides no gate.** `decides_closeout_readiness` admits exactly one value, the
  actionable count is tied at construction to the shipped three terms, and the family-review row count
  is reported beside them and folded into nothing.
- **The recorded decision claims no authority it does not have.** `creates_gate` is `Literal[False]`,
  the owner is named with its ruling basis, the authority basis may not carry a blank entry, and the
  record names the route to a future ruling rather than making one.
- **The rule renderer has no caller here, and the module holds no I/O.** `fact_grouping_rule` is declared
  and exported and no module or test in the shipped candidate calls it; the file's only non-stdlib
  imports are pydantic and two sibling model modules, so grouping, status composition, currentness and
  routing live in `memory_quality/family_review.py` and this file declares the shapes they construct.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one declared grouping rule: its version value, the renderer that spells the rule as one sentence, and the identity key built from the two facts the rule merges on. | `FACT_GROUPING_POLICY_VERSION`; `fact_grouping_rule`; `fact_group_identity` | mcp/src/agents_remember/models/knowledge/family_review.py:74-78; mcp/src/agents_remember/models/knowledge/family_review.py:151-165; mcp/src/agents_remember/models/knowledge/family_review.py:168-177 |
| The two surfaces a finding may route into, declared as a value so a third surface fails construction instead of being added. | `FAMILY_REVIEW_ROUTING_SURFACES` | mcp/src/agents_remember/models/knowledge/family_review.py:80-87 |
| The one authority that decides closeout readiness, named as a value so the routing report can state what it does not decide. | `CLOSEOUT_READINESS_DECIDER` | mcp/src/agents_remember/models/knowledge/family_review.py:89-94 |
| The five status owners in the design's own order, the per-owner declaration with both its columns, and the vocabulary mapping derived from that table. | `PIPELINE_STATUS_OWNERS`; `STATUS_OWNER_DECLARATIONS`; `STATUS_VOCABULARIES` | mcp/src/agents_remember/models/knowledge/family_review.py:96-105; mcp/src/agents_remember/models/knowledge/family_review.py:107-144; mcp/src/agents_remember/models/knowledge/family_review.py:146-148 |
| One recorded relationship a match was reached through, and one matched condition with its sides and its three supporting fact tuples. | `FactSupportingEdge`; `FactMatch` | mcp/src/agents_remember/models/knowledge/family_review.py:180-186; mcp/src/agents_remember/models/knowledge/family_review.py:189-215 |
| The closed detection-condition vocabulary the match repeats rather than renames, and its declared membership order. | `DetectionCondition`; `DETECTION_CONDITIONS` | mcp/src/agents_remember/models/knowledge/detection.py:116-122; mcp/src/agents_remember/models/knowledge/detection.py:124-132 |
| The group's declared field set — recorded family revisions, the input signature, the rule's identity, the matches and the review-record citation — with its accessors and the merge review. | `FamilyIntegrityFactGroup`; `matched_conditions`; `supporting_edges`; `retains` | mcp/src/agents_remember/models/knowledge/family_review.py:218-245; mcp/src/agents_remember/models/knowledge/family_review.py:241-245; mcp/src/agents_remember/models/knowledge/family_review.py:252-260; mcp/src/agents_remember/models/knowledge/family_review.py:262-281 |
| The record citation that is a citation and not a conclusion, whose empty tuple reports a subject nobody has reviewed. | `review_record_ids` | mcp/src/agents_remember/models/knowledge/family_review.py:236-239 |
| One owner's report with both required sentences, and the validator that refuses a status outside that owner's own members. | `PipelineStatusEntry`; `_require_the_owners_own_status_member` | mcp/src/agents_remember/models/knowledge/family_review.py:284-295; mcp/src/agents_remember/models/knowledge/family_review.py:297-313 |
| The five-owner report: exactly one entry per owner in the declared order, no field for a combined verdict, and the keyed lookup that rule makes safe. | `SeparatedStatusReport`; `_require_one_entry_per_owner_in_order`; `entry_for` | mcp/src/agents_remember/models/knowledge/family_review.py:316-325; mcp/src/agents_remember/models/knowledge/family_review.py:327-339; mcp/src/agents_remember/models/knowledge/family_review.py:341-347 |
| The currentness answer's two-member state, moved identities and typed statements, plus the two-direction rule and the reuse refusal. | `FindingCurrentness`; `binding_state`; `reinterpreted_for_new_inputs`; `_require_the_state_to_follow_from_the_moved_identities` | mcp/src/agents_remember/models/knowledge/family_review.py:350-366; mcp/src/agents_remember/models/knowledge/family_review.py:368-390 |
| One routing row limited to the declared surfaces, and the report whose counts are tied to its rows and to the shipped three terms, with the report-only property beside them. | `FamilyReviewRoutingRow`; `FamilyReviewRouting`; `_require_two_counts_and_no_fourth_term`; `family_rows_are_report_only` | mcp/src/agents_remember/models/knowledge/family_review.py:393-420; mcp/src/agents_remember/models/knowledge/family_review.py:423-444; mcp/src/agents_remember/models/knowledge/family_review.py:446-467; mcp/src/agents_remember/models/knowledge/family_review.py:469-472 |
| The decision's named owner and the bounded decision shape, with the typed `False` that records it creates no gate and the refusal of an unnamed authority. | `DecisionOwner`; `FamilyReviewGateDecision`; `creates_gate`; `_require_the_authority_basis_to_name_its_sources` | mcp/src/agents_remember/models/knowledge/family_review.py:475-486; mcp/src/agents_remember/models/knowledge/family_review.py:489-509; mcp/src/agents_remember/models/knowledge/family_review.py:509-509; mcp/src/agents_remember/models/knowledge/family_review.py:511-521 |
| The one recorded decision this module exports, naming the developer as requirement authority and carrying its authority basis and revisit condition. | `RECORDED_GATE_CONSEQUENCE_DECISION` | mcp/src/agents_remember/models/knowledge/family_review.py:524-582 |
| The frozen, `extra="forbid"` base every shape derives from, with the four bounded-length constants the fields reuse. | `KnowledgeModel`; `model_config`; `LABEL_MAX_LENGTH`; `REFERENCE_MAX_LENGTH`; `PROSE_MAX_LENGTH`; `PATH_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:24-37 |
| The detector's conclusion-name list and the declared-field-set review the module names as the measurement that a fact group carries no conclusion. | `CONCLUSION_BEARING_FIELD_NAMES`; `conclusion_bearing_fields` | mcp/src/agents_remember/models/knowledge/detection.py:216-248; mcp/src/agents_remember/models/knowledge/detection.py:268-283 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A record shape is a property of one
namespace's stored knowledge, and every identity it carries is a store-local reference or a declared
vocabulary member.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T14:18+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): created this one-to-one card for the family-review pipeline's own vocabulary. It records the four properties the record shapes enforce (no conclusion field, five separated owners, missing stays missing, currentness never re-judged), the one declared grouping rule with its identity key and the retention review that measures a merge rather than assuring it, the routing report whose actionable count is tied to the shipped three terms while the family-review row count is folded into nothing, and the single recorded gate-consequence decision that names its owner instead of claiming a ruling. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
