# mcp/tests/test_knowledge_evidence_observations.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

`VerificationObservation`: the recorded run, its artifact digest, its reads and its refusals. **20 cases**,
in the order the requirement states its clauses, all in the `unit-regression` lane.

## Code Commentary

### Logic

Every case protects one clause group: the typed aggregate under the same envelope, the exact tested
candidate recorded as data, the verbatim command identity, the result artifact bound by the digest of its
bytes, the closed execution-result vocabulary, the run's environment, the write-time digest decision, the
artifact-resolution states at read time, and the read projection that reports facts and no verdict.

Three properties are load-bearing enough that the module docstring names them before the cases:

- **The digest identifies an artifact, never a row and never a dataset.** The value the record carries is the
  sha256 of the artifact's bytes, and the record states whether that digest was *checked* against the bytes
  at write time. Writing a plausible hex string would be a fabricated claim, so the cases build real bytes
  under a temporary root and compare against what the write path actually did.
- **"Not run" is never reported as passed.** The execution-result set is closed, an unlisted value is refused
  rather than coerced, and `not_run` is served as `not_run`.
- **Nothing here manufactures a verdict.** A passing run and a failing run are equally facts: neither is a
  finding, a gate or a lifecycle change, and no served field or count could be read as one.

**The closed vocabulary is asserted against a near miss and a case variant.** The payload case feeds
`sufficient`, `PASSED` and a valid member, asserting refusal for the first two and identity for the third, and
asserts the exact member list. `EXECUTION_RESULT_MEMBERS` is also compared against the vocabulary's own tuple,
so the stored `CHECK` and the typed field cannot drift.

**The four artifact-resolution states are read from one record set.** The case asserts all four states are
distinguishable, and that the stored reference is byte-identical to what was written in the two failing
states — so a read path that "repaired", dropped or re-pinned the reference fails it.

**A false digest presented as checked is asserted to be refused rather than downgraded.** The refusal case
asserts the exact expected and observed facts and that the dataset's logical digest does not move.

**The generation's append is asserted by name.** `test_the_observation_generation_appends_and_inherits_by_name`
asserts `GENERATION_7.user_version == GENERATION_6.user_version + 1`, the schema-name suffix, and every
inherited table's column order equal to the generation this leaf descends from — not against a hard-coded
table list, so a later renumber changes two operand names and nothing else.

**The cases drive subtests rather than parametrization**, for the same population-budget reason the claims
module states, with every assertion naming the member or state it is about.

### Conventions

Hermetic like its sibling: temporary roots, in-process APSW databases through the production seam, and the
shared fixture module. `pytestmark = pytest.mark.evidence_unit`, and the module's lane row is
`mcp/tests/test-evidence-lanes.toml:74`.

### Invariants And Boundaries

- **A second run is a second record.** The case asserts the first observation is not edited when a second is
  written, which is the trigger's own contract at the case level.
- **The command identity is served verbatim and never resolved.** Nothing in the leaf executes a command.
- **No blob column and no second content store**, asserted by walking the declared columns rather than by
  inspection.
- **The publication reference's presence or absence is served as two states**, which is how the record
  states which retention route it relies on.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The case that asserts the payload is frozen and the execution-result set is closed, including the near miss and the case variant. [1]
- The case that asserts an artifact path that is not confined is refused as a shape error. [2]
- The case that asserts the write-time digest is measured against real bytes and recorded as checked. [3]
- The case that asserts a digest the bytes contradict is refused with exact facts and no dataset movement. [4]
- The case that asserts the four artifact-resolution states are distinguishable and the stored reference survives unchanged. [5]
- The case that walks the served fields and the rendered page for verdict words. [6]
- The case that asserts a second run is a second observation and the first is not edited. [7]
- The case that asserts a candidate seed selects by the recorded candidate and reports absence. [8]
- The case that asserts there is no blob column and no second content store. [9]
- The case that asserts the generation appends and inherits by name from the generation this leaf descends from. [10]
- The case that asserts the publication reference is stored on the record and served with it. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
