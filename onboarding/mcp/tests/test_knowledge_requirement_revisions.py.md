# mcp/tests/test_knowledge_requirement_revisions.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The kind admits exactly its own declared pair; a wrong schema or an unknown kind is `invalid_payload`.** [1]
- The two declared operations are members of the shipped vocabulary rather than a second one. [2]
- The state/acceptance consistency rule applied at construction, in both directions. [3]
- **The promotion refusal, measured as the stored payload being byte-identical after the attempt.** [4]
- **An `accepted` payload stored with the envelope lifecycle still `proposed`: an acceptance recorded, no approval produced.** [5]
- The explanation refused by value, and the four authorship substitutes refused as a second author. [6]
- The stored authorship surviving a close and reopen unchanged. [7]
- **A successor records its predecessor and leaves it byte-identical.** [8]
- The three lineage refusals: a self-predecessor, a predecessor under another record, and a predecessor stored nowhere. [9]
- **The stored-cycle case: forced store damage, then a descendant refused by the shared rule that names the cycle.** [10]
- The read of a record nothing stores, refused with the table named. [11]
- The namespace refusal, and the row codec's envelope-tuple round trip with its tampered-payload case. [12]
- The shared acyclic-lineage rule this suite proves the record group composes rather than re-implements. [13]
- The immutable-revision trigger the stored-cycle case must drop to reach its rule. [14]
- The operation surface these cases drive, and the guards they pin. [15]
- The production payload vocabulary these cases are about. [16]
- The two shared-support artifacts this module imports, whose exact consumer lists are the code-side gate gap this leaf left open. [17]
- The lane row that gives this module its classification and keeps it collectable under a named lane. [18]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
