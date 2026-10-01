# mcp/tests/test_knowledge_requirement_reference_contract.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

**`RequirementRevision`'s reference contract with the task plane, and the derived views.** These cases
protect `KS-R19@v1`'s reason to exist — reference, never replacement — and the disposability of
everything this record group makes readable: the owner reference's exact three components, the
admitted version spelling, the reference the payload deliberately does not police, the four forbidden
operative-obligation names, the five forbidden task-authority names at both the model and schema
planes, the real owner's refusals carried verbatim, route governance, the reference-resolution
outcomes, and the four derived views' rebuildability, totality and no-winner rules.

**Why these cases need the real owner.** A second resolver is the failure this suite must be able to
catch, and a stubbed resolver cannot catch it: the cases call the **real** `_approved_packet_ref`
through `requirement_owner.consume_owner_resolution` against real packet files under a temporary task
root, so the codes asserted are the codes the task plane actually returns.

## Code Commentary

### Logic

- **18 flat module-level cases, no test classes.** Three constants (80-86, 88-93, 95) and nine private
  helpers: `_store` (98), `_owner` (104), `_payload` (110), `_request` (128), `_write_packet`
  (148-178, the live copy — called here at 446, 447 and 507), `_refusal_of` (181), `_scope_of` (192),
  `_payload_refusal` (199) and `_stored_payload_bytes` (207).
- **The absent-field campaign runs at two planes, and both are needed.** At the payload plane
  `test_a_payload_carrying_an_operative_obligation_field_is_refused` (294-310) parametrizes over
  `obligation_text`, `requirement_text`, `title` and `display_version` and requires each refused with
  `invalid_payload` and the name present in the refusal detail; at the schema plane
  `test_no_registered_generation_declares_a_column_for_the_forbidden_set` (311-333) **re-derives the
  column census over every registered generation** rather than checking a stored list, and also asserts
  that the kind is not a table. The pair is what makes the absence falsifiable instead of merely
  asserted, and it is the evidence for this leaf's recorded quotation-degree ruling: the record group
  holds no operative-text field.
- **The seal is tested from both sides.** `test_a_stored_payload_carrying_a_forbidden_field_could_not_be_decoded`
  (334-365) hand-seals a row carrying `task_status="inProgress"` and requires a `KnowledgeStorageError`
  matching `"does not validate"` — so the refusal is the frozen shape, not a digest mismatch, which is
  the fact that distinguishes "the field is not in the model" from "the row is corrupt".
- **The owner's refusals are real refusals.** `test_each_owner_refusal_is_carried_verbatim_and_leaves_the_reference_unrewritten`
  (435-499) drives four cases through the real resolver (a missing packet, two paths outside the task
  root, and a version mismatch) and asserts both the owner's own codes and that the **stored reference
  equals the caller's reference byte for byte** — that is the proof that the reference is never
  rewritten under any outcome, and it is the case that would fail if the owner's normalized path were
  adopted.
- **The reference-resolution outcomes are a three-way fact.**
  `test_a_reference_from_another_record_group_resolves_to_this_record_group` (528-568) walks
  `unresolved` → `resolved` with exactly one record → `ambiguous` with two, and requires a malformed
  mapping to report `unresolved` with `reference is None` rather than raising.
- **Disposability is measured as byte-equality.** `test_every_derived_view_rebuilds_byte_identically_from_the_stored_rows`
  (569-616) reads the same stored rows twice and compares the serialized views, so a view that
  accumulated state between calls would fail.
- **Totality over an empty row set is a case, not an assumption.**
  `test_the_derived_views_are_total_over_a_row_set_holding_no_revision` (730-755) requires
  `head_revision_ids(()) == ()`, `CHAIN_BOUND > 0`, and every documented absence on an empty record's
  scope.

### Conventions

- The no-winner rules are asserted **with** their positive controls: the disagreement case (647-700)
  requires `disagreement` to carry both states and both provenances with `"no winner"` in the detail,
  and separately requires that asserting `aligned` against disagreeing values raises with
  `"derived from the values it reports"`. A case that only checked the happy path would let a
  winner-picking implementation pass.
- Refusal assertions read `code`, `observed` and `expected` rather than message text, except where the
  message itself is the contract (the digest mismatch, the derived-currentness error).
- The forbidden-name constants are restated here rather than imported from production, for the same
  reason as in the sibling suite.

### Invariants And Boundaries

- **Reference, never replacement.** Nothing in this suite lets the substrate derive an obligation that
  the owner did not state: a packet path the owner would refuse is still *representable* in the
  payload, so the case proves the refusal can only come from the owner.
- **A view is an answer, never an authority.** Rebuildability, totality and the no-winner rules are the
  three properties that make "derived" checkable; a view that persisted anything would fail the first.
- **Boundary.** This module is evidence about the record group, not part of it. Its lane row lives in
  `mcp/tests/test-evidence-lanes.toml` (`unit-regression`).

### Todos

None recorded. The same code-side gate gap the sibling card records applies here: this module imports
`knowledge_fixture_test_support.py` and `generation_test_support.py`, both of which declare
`consumer_scope = "exact"` consumer lists in `mcp/tests/evidence-lifecycle.toml`, and neither list
names this module — so the repository's own evidence-lifecycle validator reports two findings for this
change set. Recorded as a code-side gate gap in this leaf's curator report.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The owner reference's exact three components, and the fourth addressing scheme refused without a denylist.** [1]
- The admitted version spelling, over seven inputs the task plane would also refuse. [2]
- **The reference the payload deliberately does not police: four paths the owner would refuse are still representable, so the answer cannot be the substrate's.** [3]
- The five forbidden task-authority names refused at the payload plane. [4]
- **The four forbidden operative-obligation names refused at the payload plane — the falsifiable absence behind this leaf's recorded quotation-degree ruling.** [5]
- **The same absence re-derived at the schema plane over every registered generation, and the fact that the kind is not a table.** [6]
- The hand-sealed forbidden row that cannot be decoded, which is what separates "not in the model" from "corrupt row". [7]
- The ungoverned route as a reported state, and the sealed association that cannot be repointed. [8]
- **The real owner's four refusals carried verbatim, with the stored reference byte-identical — the proof that the reference is never rewritten.** [9]
- The resolved owner recorded as resolved, with no refusal fields. [10]
- The three-way resolution outcome — unresolved, one record, two records — and the malformed mapping that refuses to invent one. [11]
- **Disposability measured as byte-equality across two builds from the same stored rows.** [12]
- The fork reported as more than one head, with no successor designated. [13]
- **The no-winner case with its positive control: both states and provenances reported, and an asserted `aligned` refused as not derived from the values.** [14]
- An unresolved owner that has nothing to compare even when a state is supplied. [15]
- **Totality over a row set holding no revision, and the bounded chain constant.** [16]
- The payload mapping helper that reads only a stored mapping and invents no reference. [17]
- **The real resolver these cases drive, rather than a stub — a stubbed resolver cannot catch the second resolver this suite exists to exclude.** [18]
- The module that consumes the owner's answer and translates it into this record group's resolution value. [19]
- The derived views these cases keep disposable. [20]
- The two shared-support artifacts this module imports, whose exact consumer lists are the code-side gate gap this leaf left open. [21]
- The lane row that gives this module its classification and keeps it collectable under a named lane. [22]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
