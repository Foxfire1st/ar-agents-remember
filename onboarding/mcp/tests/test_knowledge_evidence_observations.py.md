# mcp/tests/test_knowledge_evidence_observations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_evidence_observations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate |  2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/tests/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The case that asserts the payload is frozen and the execution-result set is closed, including the near miss and the case variant. | "def test_the_observation_payload_is_frozen_and_the_execution_result_set_is_closed(" | mcp/tests/test_knowledge_evidence_observations.py:134-191 |
| The case that asserts an artifact path that is not confined is refused as a shape error. | "def test_an_artifact_path_that_is_not_confined_is_refused_as_a_shape_error(" | mcp/tests/test_knowledge_evidence_observations.py:264-303 |
| The case that asserts the write-time digest is measured against real bytes and recorded as checked. | "def test_the_write_time_digest_is_checked_against_the_bytes_and_recorded_as_checked(" | mcp/tests/test_knowledge_evidence_observations.py:329-380 |
| The case that asserts a digest the bytes contradict is refused with exact facts and no dataset movement. | "def test_a_digest_that_does_not_describe_the_bytes_is_refused_with_exact_facts(" | mcp/tests/test_knowledge_evidence_observations.py:381-415 |
| The case that asserts the four artifact-resolution states are distinguishable and the stored reference survives unchanged. | "def test_the_four_artifact_resolution_states_are_distinguishable(" | mcp/tests/test_knowledge_evidence_observations.py:461-623 |
| The case that walks the served fields and the rendered page for verdict words. | "def test_the_observation_read_reports_facts_and_no_verdict(" | mcp/tests/test_knowledge_evidence_observations.py:624-697 |
| The case that asserts a second run is a second observation and the first is not edited. | "def test_a_second_run_is_a_second_observation_and_the_first_is_not_edited(" | mcp/tests/test_knowledge_evidence_observations.py:725-763 |
| The case that asserts a candidate seed selects by the recorded candidate and reports absence. | "def test_a_candidate_seed_selects_by_the_recorded_candidate_and_reports_absence(" | mcp/tests/test_knowledge_evidence_observations.py:764-800 |
| The case that asserts there is no blob column and no second content store. | "def test_there_is_no_blob_column_and_no_second_content_store(" | mcp/tests/test_knowledge_evidence_observations.py:871-905 |
| The case that asserts the generation appends and inherits by name from the generation this leaf descends from. | "def test_the_observation_generation_appends_and_inherits_by_name(" | mcp/tests/test_knowledge_evidence_observations.py:906-928 |
| The case that asserts the publication reference is stored on the record and served with it. | "def test_a_publication_reference_is_stored_on_the_record_and_served_with_it(" | mcp/tests/test_knowledge_evidence_observations.py:929-969 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:20+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the observation contract's 20 cases. It records the closed execution vocabulary with no sufficiency member, the digest measured against real bytes, the four resolution states read from one record set, the by-name inheritance assertion, and the rule that a second run is a second record. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
