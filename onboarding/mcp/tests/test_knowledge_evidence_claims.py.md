# mcp/tests/test_knowledge_evidence_claims.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The case that asserts the payloads are frozen, extra-forbidden and never default the limitations value. [1]
- The case that asserts the two subject kinds are two tables and neither can address the other, including the absence of a polymorphic column. [2]
- The case that drives all five endpoint kinds and asserts each refusal names its kind. [3]
- The case that asserts the author is the admission and the lifecycle is stored data. [4]
- The case that asserts the claim command joins the closed union, its dispatch and its tables. [5]
- The case that asserts a refused batch moved neither the dataset nor a row. [6]
- The case that asserts the generation gate in both directions and that `PRAGMA user_version` does not move. [7]
- The case that asserts the coverage key makes one endpoint covered once unrepresentable. [8]
- The case that asserts no served field of a claim could carry a verdict. [9]
- The case that is this artifact's registered executable evidence node for the shared fixture. [10]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
