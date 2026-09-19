# mcp/tests/test_knowledge_evidence_claims.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_evidence_claims.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate |  2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

`EvidenceClaim`: the record's shape, its links, its write path, its generation and its read. **20 cases**,
in the order the requirement states its clauses, all in the `unit-regression` lane.

## Code Commentary

### Logic

Every case protects one clause group: the typed aggregate under the shipped envelope, the two subject kinds
as structural tables, the resolved evidence anchor, the claimed coverage that is never widened, the required
explanation and limitations, the author and lifecycle as stored data, the opaque assessment references, the
code-side resolution that refuses an unresolved link, the appended commands and their dispatch, the
generation gate, and the read projection that carries the limitations field visibly.

Three properties are load-bearing enough that the module docstring names them before the cases:

- **The table IS the kind check.** A claim's subject is one of exactly two kinds and each kind has its own
  join table with its own foreign keys, so a misspelled kind, a dangling identity and a wrong-kind target are
  *not representable* rather than merely refused. The cases assert the refusal a caller sees **and** the
  structural half: there is no polymorphic column for an unchecked identity to land in.
- **An empty limitations value is a recorded fact.** The read serves `""` — the author declaring none — and
  never `None`, "unknown" or an endorsement. The case that protects this asserts the served value on a claim
  whose limitations were stored empty, and asserts that the field is not optional on either the payload or
  the served item.
- **Nothing here judges what the evidence demonstrates.** No served field is a verdict, a grade, a score or
  a status; the assessment-reference state is the *absence* of an assessment reported as absence.

**The batch path is covered from both sides.** `test_a_claim_written_in_a_batch_is_refused_when_a_link_is_absent`
asserts `before == after`, `changed == ()` and an unchanged logical digest, so a refused batch moved nothing;
`test_the_batch_path_stores_a_claim_whose_links_all_resolve` is its positive twin. The union case asserts
`set(_TARGET_CHECKS) == kinds` over the whole closed union and that every shipped command kind is still
present, so a command without a target check or a target check without a command fails here.

**The generation gate is asserted in both directions.** One case builds genuine version-1 **and** version-4
datasets from their own recorded DDL, asserts `unsupported_schema` with both numbers and asserts that
`PRAGMA user_version` does not move — a migration or an implicit table creation would fail it. Another
asserts that a fresh store declares the generation that carries these tables.

**The cases drive subtests rather than parametrization.** The population budget is a declared ceiling, so
per-endpoint-kind variants are driven inside the case that owns their property, with every assertion naming
the kind it is about. The module states the cost — no independent failure attribution between variants of one
property — and what it preserves: every clause, and a population that runs at all.

### Conventions

Cases are hermetic: temporary directories, in-process APSW databases built through the production
application seam, and the shared fixture module rather than per-module topology. `pytestmark =
pytest.mark.evidence_unit` puts every case in the evidence lane, and the module's own lane row is
`mcp/tests/test-evidence-lanes.toml:73`.

### Invariants And Boundaries

- **No case was removed to make room.** The module is new; it adds 20 cases to the unit population and
  changes no shipped case.
- **A refusal is asserted with its operation, table and endpoint kind**, not merely with a code, so a check
  that fell through would fail on the refusal's facts as well as on the row count.
- **The sealed-revision rule is asserted here too**: a claim and its revision refuse `UPDATE` and `DELETE`.
- **Nothing in this module writes outside a temporary root.** The artifact cases build their own bytes.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The case that asserts the payloads are frozen, extra-forbidden and never default the limitations value. | "def test_the_claim_payload_is_frozen_extra_forbidden_and_never_defaults_limitations(" | mcp/tests/test_knowledge_evidence_claims.py:149-190 |
| The case that asserts the two subject kinds are two tables and neither can address the other, including the absence of a polymorphic column. | "def test_the_two_subject_kinds_are_two_tables_and_neither_can_address_the_other(" | mcp/tests/test_knowledge_evidence_claims.py:232-296 |
| The case that drives all five endpoint kinds and asserts each refusal names its kind. | "def test_an_unresolved_subject_anchor_or_coverage_endpoint_is_refused_with_its_kind(" | mcp/tests/test_knowledge_evidence_claims.py:335-385 |
| The case that asserts the author is the admission and the lifecycle is stored data. | "def test_the_author_is_the_admission_and_the_lifecycle_is_stored_data(" | mcp/tests/test_knowledge_evidence_claims.py:464-505 |
| The case that asserts the claim command joins the closed union, its dispatch and its tables. | "def test_the_claim_command_joins_the_closed_union_its_dispatch_and_its_tables(" | mcp/tests/test_knowledge_evidence_claims.py:554-603 |
| The case that asserts a refused batch moved neither the dataset nor a row. | "def test_a_claim_written_in_a_batch_is_refused_when_a_link_is_absent(" | mcp/tests/test_knowledge_evidence_claims.py:604-643 |
| The case that asserts the generation gate in both directions and that `PRAGMA user_version` does not move. | "def test_a_claim_write_against_an_older_generation_is_refused_and_names_the_missing_one(" | mcp/tests/test_knowledge_evidence_claims.py:676-719 |
| The case that asserts the coverage key makes one endpoint covered once unrepresentable. | "def test_the_coverage_table_makes_one_endpoint_covered_once_unrepresentable(" | mcp/tests/test_knowledge_evidence_claims.py:868-900 |
| The case that asserts no served field of a claim could carry a verdict. | "def test_no_served_field_of_a_claim_could_carry_a_verdict(" | mcp/tests/test_knowledge_evidence_claims.py:798-837 |
| The case that is this artifact's registered executable evidence node for the shared fixture. | "def test_a_claim_reads_back_with_every_field_including_an_empty_limitations(" | mcp/tests/test_knowledge_evidence_claims.py:744-797 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:20+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the claim contract's 20 cases. It records the three named properties, the structural half of the kind check, the batch path's two sides, the generation gate asserted in both directions, and the shared-fixture registration that makes this module the evidence node's owner. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
