# mcp/tests/test_knowledge_portable_boundaries.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

**The portable artifact's boundary population** — the properties the ordinary export/import path cannot
reach from outside. It is the second half of the leaf's evidence set: it imports the round-trip module's
helpers rather than copying them, so there is still exactly one definition of what an artifact, a refusal
or a published row count is. It is a second module because the repository's 1200-line hard limit is a real
limit and one file cannot hold both populations.

Registered in the **integration** lane (`mcp/tests/test-evidence-lanes.toml:140`) and declared as an exact
consumer of **three** shared support artifacts (`knowledge_fixture_test_support.py`,
`snapshot_lifecycle_test_support.py`, `merge_case_test_support.py`), because it also drives L4's
publication path. Unregistered, the module would make `load_lane_manifest` refuse the whole repository.

## Code Commentary

### Logic

Five properties live here, each because the ordinary path cannot fail it:

1. **The freeze's own closure, proved from a producer this leaf did not write a new node for.**
   `test_a_frozen_snapshot_of_a_wal_resident_candidate_is_published_closed` measures the property on the
   **published destination** — the file a consumer opens — rather than on the private stage. It is the node
   this leaf owns for the shared `require_closed_database` step, and it is killed by the same mutations
   (`F1a`/`F1b`) that kill L4's own node, which is kept as corroboration and **not edited**.
2. **The canonical form of the whole document, including every header type.**
   `test_the_canonical_form_of_the_whole_document_is_the_only_form_the_reader_accepts` is **the** node the
   guarantee rests on. It drives, in one case: every non-canonical spelling axis the format declares
   (`_non_canonical_axes` — whitespace, escapes, reordered envelope, reordered tables, unsorted nested keys,
   the nested-spelling mutants at depth two and inside lists), the `canonical_document` assertions, and
   `_assert_the_header_types_are_pinned` over `_header_type_respellings()` — **all seven envelope keys
   respelled with a different JSON type**, each asserted to be refused, and each asserted to **pass** the
   whole-document gate, which is what proves the refusal is the header check's rather than the gate's.
   `test_a_stage_opened_in_wal_mode_is_published_as_a_closed_database` covers the import's close/verify
   step, and `test_a_frozen_snapshot_of_a_wal_resident_candidate_is_published_closed` covers the freeze's.
3. **The staged sealed-aggregate read.**
   `test_an_artifact_whose_sealed_payload_contradicts_its_digest_is_refused` tampers **every retained row of
   both revision tables** and asserts the import refuses with the destination byte-identical,
   row-count-identical and digest-identical. This is the node that made the review's HIGH finding
   unfalsifiable-by-construction: before it, a `payload_digest` that contradicted its row crossed the
   artifact as ordinary text and was published unchecked.
4. **Destination admission before any staging work.**
   `test_destination_admission_refuses_before_any_staging_work` asserts each of the three destination
   states' **own code** and that **no private stage directory was even requested**.
5. **The typed read of an artifact that is not readable text.**
   `test_an_artifact_that_cannot_be_read_as_text_is_refused_with_a_typed_code` covers the empty file, the
   non-UTF-8 byte sequence and the text-that-is-not-JSON cases, so a raw `UnicodeDecodeError` cannot escape
   the boundary.

### Conventions

- `pytestmark = pytest.mark.integration` at module level.
- The module reaches into internals **deliberately and only where a boundary needs it**
  (`export_import._verify_staged_dataset`, `export_portable._out_of_canonical_order`, L4's
  `journal_mode`/`open_read_only_database`), which is the reason this population is separate: a boundary
  case is allowed to construct the state the public path cannot produce.
- `journal_mode_of` and the `snapshot_lifecycle_test_support` helpers are what let the WAL cases assert the
  **published destination's** mode rather than the stage's.

### Invariants And Boundaries

- **A survivor is never reported as coverage.** The two mutations that do not die are recorded with their
  reasons in the leaf's evidence: `_out_of_canonical_order` is unreachable from the public reader (the gate
  refuses the same text one step earlier), and the header namespace-binding guard at
  `export_portable.py:911` is reachable and verdict-changing but has no killing node — it is an
  **observation for L9**, not a claim of this module.
- **No `skip`, `xfail` or `deselect`.** Every property above is asserted, and the module did not grow by
  adding a case in the final fix round: round 3 extended the cases that already owned each property.
- **Classification and evidence, not acceptance.** This card does not claim a passing run.
- **Boundary.** This module owns the artefacts' *boundary* properties. The round trip, the completeness
  mutations and the preservation cases are the round-trip module's, and the two are one evidence set
  precisely because neither can carry the other's cases.

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The five properties that live here because the ordinary path cannot fail them. [1]
- The lane marker, and the three shared support artifacts this module's registry row must declare. [2]
- The helpers imported from the round-trip module, so the two modules keep one definition of an artifact and a refusal. [3]
- The journal-mode reader the WAL cases assert the **published destination** through. [4]
- **The freeze's closure proved on the published destination, from the producer this leaf shares with L4.** [5]
- **The node the whole guarantee rests on: every non-canonical spelling axis, the `canonical_document` assertions, and all seven header types pinned — the header's namespace guard (`bound`) is the one reachable guard the population does not kill (an observation for L9).** [6]
- **The staged sealed-aggregate read, tampering every retained row of both revision tables with the destination held identical.** [7]
- The import's close/verify step, proved by a stage opened in WAL mode. [8]
- **Destination admission before any staging work: three states, their own codes, and no stage directory even requested.** [9]
- The typed read of an artifact that is not readable UTF-8 text. [10]
- The unreachable defence-in-depth branch whose mutation survives for a stated reason. [11]
- The integration-lane row this module occupies. [12]
- The snapshot-lifecycle artifact whose consumer list gained this module. [13]
- The merge-cases artifact whose consumer list gained this module. [14]
- The identity-branching fixture artifact whose consumer list gained this module. [15]
- The L4 node this module corroborates rather than replaces, and its own marker caveat. [16]
- The round-trip module whose helpers this one imports, and the onboarding card that records the shared set. [17]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
