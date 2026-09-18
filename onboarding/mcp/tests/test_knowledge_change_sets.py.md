# mcp/tests/test_knowledge_change_sets.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_change_sets.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate |  2026-09-18T13:43:14+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l13` uncommitted staged source; base `b5a74aee6cdf671c9963f3aba4df6d44b856f697` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

`SemanticChangeSet` and the preservation claim: the composed record and its separate sibling. **29 cases**,
in the order the requirement states its clauses, all in the `unit-regression` lane.

## Code Commentary

### Logic

Every case protects one clause group: the six declared parts, the two exact snapshot identities, the
membership computed from the members' own declarations, the succession edge, preservation as a record that
is *not* an effect, the generation the record group joins, the requirement-revision reference under the
opaque-reference clause, and the derived read that reports facts and no verdict.

**The succession edge is a new record with a predecessor, never an edited row.** A successor has its own
identity and its own edge row, and the superseded change set is still readable with its own payload
afterwards. The edge is written inside the successor's own creation batch — the command union carries no
member that appends an edge to a stored change set — a self-named predecessor is refused as the shipped
`lineage_cycle` with nothing written, the appended generation's triggers refuse an update and a delete of
the edge row, and a fork is two records both naming one predecessor rather than one winner. A rewritten
lineage, an in-place revision and a mutable "current version" pointer all fail here.

**Nothing may conclude a verdict or a summary.** Two probe tuples name what would make a change set a task
authority or a decision rather than a record of authored work, and each probe is asserted refused by the
frozen payload's ordinary `extra="forbid"` rule **and** absent from the columns of every registered
generation over `knowledge_record` and `change_set_predecessor`. The payload's own field set is asserted
exactly, an open question declares exactly its three fields and is served as open with no answered field on
either the payload or the served type, and no `preserve` spelling and no preservation flag is representable
in the effect vocabulary.

Three further properties are load-bearing:

- **Both snapshot identities are stored verbatim.** The baseline *and* the candidate are read back exactly
  as the author declared them, including the schema version, and neither is re-derived from what is current
  at read time; a change set assembled from two namespaces is refused at construction, because it is not a
  comparison any reader could interpret.
- **Membership is a computed fact, and a member belongs to one change set.** A claim is listed only under
  the change set it declares and the other change set lists nothing; a change set holding preservation
  claims and no effect claims is complete and valid, and one holding no member at all is equally complete
  rather than refused or filled in.
- **An unresolved reference is a state, never a refusal and never a repair.** Requirement-revision
  references and realization-claim identities are stored verbatim and reported as unresolved references
  with the field, the holder record and the holder revision; the same references are reported from both the
  per-record plane and the scope plane, and the scope-level list is exactly the union of the per-record
  lists. A realization claim deleted after the change set was written is reported unresolved rather than
  re-pointed at a neighbouring claim, and no `requirement_revision` record is fabricated to satisfy a
  reference.

**The generation's append is asserted by name and by comparison, not against a hard-coded list.**
Generation 8's tables are generation 7's tables with exactly one table appended — `change_set_predecessor`,
whose primary key is the ordered triple `repository_id`, `successor_change_set_id`,
`predecessor_change_set_id` — and every one of generation 7's **thirty-three** names keeps its columns and
its primary key. So generation 8's **thirty-four** tables are thirty-three inherited plus one appended.
The case also asserts the suffix is that one table, that generation 8's trigger set and index set are
strict supersets of generation 7's, that `CURRENT_GENERATION is GENERATION_8`, that the appended table
carries no `content_digest` column, and that no registered generation's DDL contains `ALTER TABLE` — so a
later renumber changes two operand names and nothing else. A fresh store declares the current generation
and is served by the record group's own read.

**The closed vocabularies are asserted as exact sets, and they pin rather than union.** The three member
kinds map to exactly three frozen models of three different types, with neither payload type a subclass of
the other; the preservation subject kinds are exactly the four declared ones with an effect label refused
as a subject; the change-set payload registers under exactly one kind and one schema; requirement-revision
references stay inside the shipped `REFERENCE_MAX_LENGTH` bound and round-trip byte-identically, so
spellings a parser would fold together stay distinct stored values. A reference declared twice is refused,
because two identical references would look like two authored members.

**What the cases deliberately do NOT assert.** No case asserts that a change set is complete, endorsed,
reviewed or gated — the requirement's own position is that an authored record concludes nothing — and none
asserts a canonical spelling, a requirement identity parsed out of a reference, or a stored read.

### Conventions

Hermetic like its sibling: temporary directories, in-process APSW databases built through the candidate
namespace seam of `mcp/tests/candidate_batch_test_support.py`, and the shared knowledge fixture. The lane
row is `mcp/tests/test-evidence-lanes.toml:163`, and the module is inside the unit population registered in
`mcp/tests/evidence-lifecycle.toml`. The cases drive direct assertions rather than parametrization, with
every assertion naming the part, member or reference it is about.

### Invariants And Boundaries

- **No case was removed to make room.** The module is new; it adds 29 cases to the unit population and
  changes no shipped case.
- **The absence assertions are made at both planes.** A case that asserted only the validator half would
  leave the schema free to hold the value later, so no column of any registered generation may carry a
  probe name.
- **Every refusal in this module is a shipped code**, and a refusal is asserted with its facts
  (`lineage_cycle` naming the record on the cycle, `invalid_reference` naming the identity) and with
  `wrote_nothing()`, so a check that fell through would fail on the refusal's facts as well as on the row
  count.
- **The generation contract is asserted against the generation actually landed on rather than a literal**,
  which is why the case carries its own `RENUMBERED for the sync` note.
- **Nothing in this module writes outside a temporary root**, and the change set's own read is derived: two
  reads over unchanged rows are equal and dump to the same JSON.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring stating what these cases protect: the six declared parts, the two exact snapshot identities, the membership, the succession edge, and preservation as a record that is not an effect. | `SemanticChangeSet` | mcp/tests/test_knowledge_change_sets.py:1-19 |
| The probe names that would make a change set a task authority rather than a record of authored work. | `TASK_AUTHORITY_FIELD_NAMES` | mcp/tests/test_knowledge_change_sets.py:75-82 |
| The probe names that would make a change set a decision, or a generated narrative. | `VERDICT_AND_SUMMARY_FIELD_NAMES` | mcp/tests/test_knowledge_change_sets.py:85-94 |
| The case that asserts both snapshot identities are stored verbatim, are not re-derived at read time, and must be two sides of one namespace. | `test_a_change_set_records_both_snapshot_identities_verbatim` | mcp/tests/test_knowledge_change_sets.py:255-290 |
| The case that asserts all six declared parts are readable from one change set, the three member-declared ones as computed membership. | `test_the_six_declared_parts_are_all_readable_from_one_change_set` | mcp/tests/test_knowledge_change_sets.py:293-322 |
| The case that asserts membership is computed from the members' own declarations, so a member is listed under one change set only. | `test_membership_is_computed_from_the_members_own_declarations` | mcp/tests/test_knowledge_change_sets.py:325-342 |
| The case that asserts preservation-without-effect and the memberless change set are both complete states. | `test_a_change_set_may_hold_preservation_claims_and_no_effect_claims` | mcp/tests/test_knowledge_change_sets.py:345-369 |
| The case that asserts no preservation spelling is in the closed effect set and no preservation flag fits the effect payload. | `test_no_preservation_claim_is_representable_in_the_effect_vocabulary` | mcp/tests/test_knowledge_change_sets.py:376-406 |
| The case that asserts the three member kinds resolve to three distinct models sharing no table and no inheritance. | `test_an_effect_claim_and_a_preservation_claim_are_two_kinds_and_never_one_table` | mcp/tests/test_knowledge_change_sets.py:433-448 |
| The case that asserts the preservation subject kind set is exactly the four declared kinds, with an effect label refused. | `test_a_preservation_subject_is_a_named_reference_of_one_declared_kind` | mcp/tests/test_knowledge_change_sets.py:451-461 |
| The case that asserts a preservation subject that resolves to nothing is kept verbatim and reported unresolved. | `test_a_preservation_subject_that_resolves_to_nothing_is_reported_unresolved` | mcp/tests/test_knowledge_change_sets.py:464-487 |
| The case that asserts the unresolved state is reported for the subject that resolves to nothing and not for one that resolves. | `test_a_preservation_subject_that_resolves_is_not_reported_unresolved` | mcp/tests/test_knowledge_change_sets.py:490-519 |
| The case that asserts supersession is a new record naming its exact predecessor while the predecessor survives. | `test_a_successor_change_set_is_a_new_record_with_a_predecessor_edge` | mcp/tests/test_knowledge_change_sets.py:526-542 |
| The case that asserts the edge is written inside the successor's own creation batch and that no union member appends an edge. | `test_the_predecessor_edge_is_written_inside_the_successors_own_creation_batch` | mcp/tests/test_knowledge_change_sets.py:545-573 |
| The case that asserts a self-named predecessor is refused as the shipped lineage cycle with nothing written. | `test_a_change_set_naming_itself_as_predecessor_is_refused_as_lineage_cycle` | mcp/tests/test_knowledge_change_sets.py:576-591 |
| The case that asserts the appended generation's triggers seal the edge against an update and a delete. | `test_the_succession_edge_table_is_sealed_against_update_and_delete` | mcp/tests/test_knowledge_change_sets.py:594-622 |
| The case that asserts two successors of one predecessor are two records and neither edits the other. | `test_a_second_successor_of_one_predecessor_is_a_separate_record` | mcp/tests/test_knowledge_change_sets.py:625-642 |
| The generation-8 append: generation 7's thirty-three names keep their columns and primary keys and exactly one table is appended. | `def test_generation_eight_appends_one_table_to_the_generation_it_descends_from()`; "generation 7's thirty-three"; `"change_set_predecessor"` | mcp/tests/test_knowledge_change_sets.py:649-682; mcp/tests/test_knowledge_change_sets.py:654-654; mcp/tests/test_knowledge_change_sets.py:670-670 |
| The case that asserts a new store declares the current generation and is served by this record group's read. | `test_a_new_store_declares_the_generation_that_carries_this_leafs_table` | mcp/tests/test_knowledge_change_sets.py:685-698 |
| The case that asserts a requirement-revision reference is stored verbatim, reported unresolved with its holder, and fabricates no requirement record. | `test_a_requirement_revision_reference_is_stored_verbatim_and_reported_unresolved` | mcp/tests/test_knowledge_change_sets.py:705-738 |
| The case that asserts near-miss spellings round-trip byte-identically and stay distinct, so nothing canonicalises them. | `test_a_requirement_revision_reference_is_never_parsed_or_canonicalised` | mcp/tests/test_knowledge_change_sets.py:741-753 |
| The case that asserts the shipped reference-length bound is a property of the record. | `test_a_requirement_revision_reference_beyond_the_shipped_bound_is_refused` | mcp/tests/test_knowledge_change_sets.py:756-771 |
| The case that asserts a reference or a realization-claim identity declared twice is refused. | `test_a_reference_declared_twice_is_refused` | mcp/tests/test_knowledge_change_sets.py:774-789 |
| The case that asserts an identity no stored claim carries is refused as an invalid reference naming it, with nothing written. | `test_a_candidate_realization_claim_that_resolves_to_nothing_is_refused_as_invalid_reference` | mcp/tests/test_knowledge_change_sets.py:792-808 |
| The case that asserts a reference whose row is gone is reported unresolved rather than dropped or re-pointed. | `test_a_realization_claim_removed_after_the_change_set_is_reported_unresolved` | mcp/tests/test_knowledge_change_sets.py:811-843 |
| The case that asserts an open question declares exactly its fields and nothing records it answered. | `test_an_open_question_is_reported_open_and_nothing_records_it_answered` | mcp/tests/test_knowledge_change_sets.py:850-879 |
| The case that asserts no task status, seat ownership or approval is representable at either plane. | `test_nothing_here_stores_task_status_seat_ownership_or_approval` | mcp/tests/test_knowledge_change_sets.py:882-896 |
| The case that asserts no verdict or generated summary field is representable and the payload's field set is exactly its declared composition. | `test_a_change_set_carries_no_verdict_and_no_generated_summary` | mcp/tests/test_knowledge_change_sets.py:899-916 |
| The case that asserts the payload registers under exactly one kind and one schema. | `test_the_change_set_payload_registers_under_one_kind_and_one_schema` | mcp/tests/test_knowledge_change_sets.py:919-932 |
| The case that asserts the read projection reports every unresolved reference verbatim with its holder and that the scope list is exactly the union of the per-record lists. | `test_the_read_projection_reports_every_unresolved_reference_verbatim_with_its_holder` | mcp/tests/test_knowledge_change_sets.py:935-966 |
| The case that asserts the read is derived: two reads over unchanged rows are equal and dump to the same JSON. | `test_the_read_is_derived_and_a_rebuild_reproduces_it_byte_for_byte` | mcp/tests/test_knowledge_change_sets.py:969-983 |
| The lane row placing this module in the unit population. | "mcp/tests/test_knowledge_change_sets.py" | mcp/tests/test-evidence-lanes.toml:163-163; mcp/tests/test-evidence-lanes.toml:176-183 |
| The registration listing this module among the exact consumers of the shared candidate-batch case harness. | "candidate-batch-case-harness"; `"mcp/tests/test_knowledge_change_sets.py"` | mcp/tests/evidence-lifecycle.toml:1093-1098; mcp/tests/evidence-lifecycle.toml:1115-1115; mcp/tests/evidence-lifecycle.toml:28-35 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The cases exercise one in-process knowledge store
under a temporary root and construct no process, publication or Git object.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:20+02:00 — 260915-KS-L13 curator (uncommitted change set on `ar/260915-ks-l13`, base `b5a74aee`): created this one-to-one card for the change-set record group's 29 cases. It records the succession rule at the case level (a new record with a predecessor edge, written inside the successor's own creation batch, sealed against update and delete, and forkable), the two-plane absence assertions for task authority and verdict probes, the by-name generation argument that generation 8 appends exactly one table to generation 7's thirty-three, the exact-set vocabularies that pin rather than union, and the derived read that reports unresolved references verbatim. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
