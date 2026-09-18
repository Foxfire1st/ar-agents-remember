# mcp/tests/test_knowledge_requirement_revisions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_requirement_revisions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash | `a066550591eb3116ae008cc0d57f3558b0af52c5` |
| lastVerifiedCommitDate | 2026-09-18T07:03:08+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l19` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

**`RequirementRevision`'s own boundary — kind, payload, state and lineage.** These cases protect
`KS-R19@v1`'s record group at the envelope the substrate already has: the kind's admissible pair, the
two operations it declares, the state/acceptance consistency rule, the explanation's non-emptiness,
the absence of any authorship substitute, the promotion refusal, and the lineage rules — predecessor
recording, self-predecessor, cross-record predecessor, dangling predecessor and a stored cycle.

**Why this module is separate from the reference-contract suite.** This half measures the record
group's *internal* boundary, where every answer comes from the store's own tables. The sibling
`test_knowledge_requirement_reference_contract.py` measures the boundary with the task plane and the
disposability of the derived views. A fact that needs the owner's real resolver belongs there, not
here.

## Code Commentary

### Logic

- Both new modules are **flat module-level `def test_*` functions with no test classes** — 17 here and
  18 in the reference-contract sibling — and both share the same three module constants:
  `FORBIDDEN_TASK_AUTHORITY_FIELDS` (69-75: `task_status`, `seat_owner`, `lifecycle_gate`,
  `implemented`, `approved_by_substrate`), `OPERATIVE_OBLIGATION_FIELDS` (77-82: `obligation_text`,
  `requirement_text`, `title`, `display_version`) and `OWNER_PATH` (84). The two forbidden sets are
  **restated rather than imported from production**, so the case that asserts their absence cannot be
  satisfied by an import that silently stopped covering a name.
- The private helpers are the case harness: `_store` (87), `_owner` (93), `_payload` (99),
  `_request` (117), `_write_packet` (137-167), `_refusal_of` (170), `_scope_of` (181), `_chain_of`
  (188), `_payload_refusal` (196) and `_stored_payload_bytes` (204).
- The suite drives the **public** operation surface (`record_requirement_revision`,
  `read_requirement_revisions`) through a real admitted store, and asserts on stored bytes where the
  claim is about immutability: the promotion case reads the stored payload before and after the
  attempt and requires it byte-identical.
- The stored-cycle case is the one place the suite **forces store damage** to reach a rule: the
  `record_revision_no_rewrite` trigger is dropped, an edge and a re-sealed digest are written directly,
  and the descendant write must then refuse with `lineage_cycle` and name the cycle. The shared
  `lineage.find_cycle` is what produces both the cycle wordings, so this case proves the record group
  composes the package's rule rather than judging adjacency itself.

### Conventions

- `_write_packet` (137-167) is defined and **not called in this module**; the live copy of that helper
  is in the reference-contract sibling, where it is called three times. A reader looking for the packet
  writer should read the sibling.
- The suite asserts **membership**, not an exact set, where a shared vocabulary grew:
  `test_the_record_group_declares_two_operations_beside_the_shipped_vocabulary` (246-257) checks that
  both names are members of `KnowledgeOperation` rather than that the vocabulary equals two names.
- Refusal assertions read the code, the `observed` and the `expected` fields rather than message text,
  so a reworded refusal does not silently pass a case that meant to pin the reason.

### Invariants And Boundaries

- **Immutability is asserted against stored bytes, not against the API's own report.** The successor
  case and the promotion case both re-read the predecessor's stored payload and require it unchanged,
  which is what makes "a revision is never rewritten" a measured fact rather than a claim about a
  return value.
- **No case reaches the task plane.** Every owner resolution used here is constructed locally; the
  real resolver is exercised only in the reference-contract sibling.
- **Boundary.** This module does not own the payload vocabulary, the codecs, the operation surface or
  the envelope seam; it is evidence about them. Its lane row lives in
  `mcp/tests/test-evidence-lanes.toml` (`unit-regression`), which is what makes it collectable under a
  named classification rather than by accident.

### Todos

None recorded. Note for a later reader: this leaf added the two modules to the lane manifest but did
**not** add them to the two `consumer_scope = "exact"` consumer lists in
`mcp/tests/evidence-lifecycle.toml` that they now import from
(`knowledge_fixture_test_support.py`, `generation_test_support.py`), so the repository's own
evidence-lifecycle validator reports two `consumer proof differs from source-derived ownership`
findings for this change set. That is a code-side gate gap recorded in this leaf's curator report, not
something these cards can settle.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The kind admits exactly its own declared pair; a wrong schema or an unknown kind is `invalid_payload`.** | "test_the_requirement_kind_resolves_only_to_its_own_declared_pair" | mcp/tests/test_knowledge_requirement_revisions.py:186-212 |
| The two declared operations are members of the shipped vocabulary rather than a second one. | "test_the_record_group_declares_two_operations_beside_the_shipped_vocabulary" | mcp/tests/test_knowledge_requirement_revisions.py:213-224 |
| The state/acceptance consistency rule applied at construction, in both directions. | "test_an_accepted_origin_state_without_an_acceptance_reference_is_refused"; "test_a_proposed_origin_state_carrying_an_acceptance_reference_is_refused" | mcp/tests/test_knowledge_requirement_revisions.py:225-234; mcp/tests/test_knowledge_requirement_revisions.py:235-246 |
| **The promotion refusal, measured as the stored payload being byte-identical after the attempt.** | "test_a_promotion_attempt_is_refused_and_no_stored_byte_changes" | mcp/tests/test_knowledge_requirement_revisions.py:247-276 |
| **An `accepted` payload stored with the envelope lifecycle still `proposed`: an acceptance recorded, no approval produced.** | "test_recording_an_accepted_revision_stores_the_state_and_produces_no_approval" | mcp/tests/test_knowledge_requirement_revisions.py:277-314 |
| The explanation refused by value, and the four authorship substitutes refused as a second author. | "test_an_empty_or_absent_explanation_is_refused"; "test_no_payload_field_can_substitute_for_the_revisions_authorship" | mcp/tests/test_knowledge_requirement_revisions.py:315-325; mcp/tests/test_knowledge_requirement_revisions.py:326-341 |
| The stored authorship surviving a close and reopen unchanged. | "test_the_stored_revision_carries_the_authorship_it_was_authored_under" | mcp/tests/test_knowledge_requirement_revisions.py:342-367 |
| **A successor records its predecessor and leaves it byte-identical.** | "test_a_successor_records_its_predecessor_and_leaves_it_byte_identical" | mcp/tests/test_knowledge_requirement_revisions.py:368-402 |
| The three lineage refusals: a self-predecessor, a predecessor under another record, and a predecessor stored nowhere. | "test_a_self_predecessor_is_refused_as_a_cycle_and_writes_nothing"; "test_a_predecessor_belonging_to_another_record_is_refused"; "test_a_dangling_predecessor_is_refused" | mcp/tests/test_knowledge_requirement_revisions.py:403-425; mcp/tests/test_knowledge_requirement_revisions.py:426-447; mcp/tests/test_knowledge_requirement_revisions.py:448-461 |
| **The stored-cycle case: forced store damage, then a descendant refused by the shared rule that names the cycle.** | "test_a_stored_cycle_refuses_a_descendant_and_names_the_cycle" | mcp/tests/test_knowledge_requirement_revisions.py:462-515 |
| The read of a record nothing stores, refused with the table named. | "test_the_read_refuses_a_record_that_is_not_stored" | mcp/tests/test_knowledge_requirement_revisions.py:516-528 |
| The namespace refusal, and the row codec's envelope-tuple round trip with its tampered-payload case. | "test_a_request_addressed_to_another_namespace_is_refused"; "test_the_revision_row_codec_round_trips_through_the_envelope_tuple" | mcp/tests/test_knowledge_requirement_revisions.py:529-547; mcp/tests/test_knowledge_requirement_revisions.py:548-581 |
| The shared acyclic-lineage rule this suite proves the record group composes rather than re-implements. | `find_cycle` | mcp/src/agents_remember/memory/knowledge/lineage.py:133-159 |
| The immutable-revision trigger the stored-cycle case must drop to reach its rule. | `record_revision_no_rewrite` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:222-228 |
|The operation surface these cases drive, and the guards they pin.|`record_requirement_revision`; `require_acyclic_lineage`| mcp/src/agents_remember/memory/knowledge/requirements.py:89-112; mcp/src/agents_remember/memory/knowledge/requirements.py:324-364 |
|The production payload vocabulary these cases are about.|`RequirementRevisionPayload`| mcp/src/agents_remember/models/knowledge/requirement.py:172-213 |
|The two shared-support artifacts this module imports, whose exact consumer lists are the code-side gate gap this leaf left open.|`make_authorship`; `create_current_generation_store`| mcp/tests/knowledge_fixture_test_support.py:189-202; mcp/tests/generation_test_support.py:86-108 |
| The lane row that gives this module its classification and keeps it collectable under a named lane. | "unit-regression = [" | mcp/tests/test-evidence-lanes.toml:5-5 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:20+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): created this one-to-one card for the record group's internal-boundary suite. It records what the 17 cases actually pin and, more usefully, the three things a reader would otherwise have to infer: immutability is asserted **against stored bytes** re-read after the fact rather than against a return value, so "a revision is never rewritten" is measured; the two forbidden-name sets are **restated in the suite rather than imported from production**, so the absence case cannot be satisfied by an import that quietly stopped covering a name; and the stored-cycle case **forces store damage on purpose** (the `record_revision_no_rewrite` trigger is dropped and an edge re-sealed) to prove the record group composes the shared `lineage.find_cycle` instead of judging adjacency itself. It also records that `_write_packet` is defined here and never called — the live copy is in the reference-contract sibling — and the code-side gate gap this leaf left open, which is recorded in the leaf's curator report rather than settled by a card: these modules were added to the lane manifest but not to the two `consumer_scope = "exact"` consumer lists in `mcp/tests/evidence-lifecycle.toml` they now import from. Verification metadata advances to the leaf's base commit `e963a01c` because the body was read against the current source; the code commit does not exist yet and closeout owns that stamp.
