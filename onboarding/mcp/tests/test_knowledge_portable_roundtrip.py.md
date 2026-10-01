# mcp/tests/test_knowledge_portable_roundtrip.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

**The artifact contract and the export/import population for `KS-R06@v1`** — the round trip, its refusals
and what it preserves. One of the leaf's **two** test modules (`test_knowledge_portable_boundaries.py`
holds the boundary population and imports this module's helpers rather than copying them, so there is
still exactly one definition of what an artifact, a refusal or a published row count is); the split exists
because the repository's 1200-line hard limit is a real limit and one file cannot hold both populations.

The module is registered in the **integration** lane (`mcp/tests/test-evidence-lanes.toml:141`) and
declared as an exact consumer of two shared support artifacts in `mcp/tests/evidence-lifecycle.toml`:
`knowledge_fixture_test_support.py` (the branching fixture) and `merge_case_test_support.py` (the
three-commit merge case). **Both registrations are preconditions rather than bookkeeping:** an unregistered
`test_*.py` module makes `load_lane_manifest` refuse the whole repository, and the repository's dependency
ownership census derives real importers and refuses a declared consumer set that differs from the source.

## Code Commentary

### Logic

Three properties are what the cases are built to falsify, and each is the reason for a group below. The
cases are **consolidated by protected property** rather than split one per assertion, because the
population has a declared ceiling and because each function names the one failure it exists to catch while
grouping the checks that would each pass while that failure went unnoticed.

- **Completeness** — `test_an_incomplete_or_inconsistent_artifact_is_refused` mutates an artifact through
  `_inconsistent_artifacts` in many ways (a dropped collection, a truncated table, an unknown table, a
  value the declared type cannot hold, a reordered or renamed column, a repeated key) and asserts the check
  that catches each. `test_a_filtered_read_response_cannot_validate_as_a_complete_export` and
  `test_a_complete_projection_of_the_source_tables_still_validates` are the pair that keeps the first
  honest: a projection is refused **because it is not the format**, not because it is a projection, so a
  complete projection of the source tables does validate.
- **Refusal without partial acceptance** — `test_a_refused_import_preserves_the_destination_bytes_and_leaves_no_stage`
  and `test_a_destination_is_replaced_only_for_the_admitted_identity` measure the destination's file digest
  and the destination directory's contents after the fact, so "nothing was published" is a measurement
  rather than a promise. `test_a_dangling_reference_is_refused_at_commit` covers the deferred-foreign-key
  refusal.
- **Preservation** — `test_a_populated_dataset_round_trips_to_an_equal_logical_dataset` holds every stored
  ID, provenance value and relation endpoint to the round trip, and
  `test_accepted_origin_state_crosses_as_data_and_is_not_promoted` holds the `state_at_origin` **value**
  to it while asserting that nothing promotes it. `test_rows_and_strings_cross_the_boundary_exactly` covers
  Unicode, line endings and the typed JSON columns.

Two further cases make the contract's own claims measurable rather than asserted:
`test_the_artifact_is_one_deterministic_document_of_the_declared_shape` asserts the artifact this encoder
produces is the one this reader accepts (the round trip is a proof rather than a coincidence), and
`test_a_merged_dataset_is_also_exportable_and_restorable` runs the export over a dataset that came
**through L5's merge**, which is the composition the next leaves consume.

The shared helpers are the module's other half and the boundary module imports them:
`artifact_of` / `envelope_of` / `reencode` / `reseal` (build one artifact and its resealed variants),
`identity_of` / `exported` (drive the public export), `import_into` (drive the public import),
`row_counts_of` / `table_rows` / `identifiers_of` / `labels_of` (read a published dataset back), and
`sqlite_entries` / `_staging_directories` (measure the destination directory and any surviving private
stage). `_empty_dataset` builds the empty destination the fresh-install cases need.

### Conventions

- `pytestmark = pytest.mark.integration` at module level; every case therefore runs with the repository's
  real-boundary policy and is counted in the integration population.
- The cases drive the **public** operations (`application.knowledge_export`'s five entry points) except
  where a boundary cannot be reached from outside, which is the boundary module's subject rather than
  this one's.
- Assertions compare refusal **codes**, `record_id` and `table` rather than message text, which is why a
  refusal's identity is contract on this leaf.
- The fixtures come from the shared support modules rather than being rebuilt here, which is what the two
  registry rows declare.

### Invariants And Boundaries

- **A refusal case measures the destination, not only the verdict.** Every refusal case in this module
  asserts something about bytes, row counts or directory contents afterwards.
- **No `skip`, `xfail`, `deselect` or per-file ignore.** The module's population is what it appears to be;
  the one occurrence of the word "skipped" is inside a comment.
- **The cases are classification and evidence, never acceptance.** Lane membership is not execution
  evidence for the contract and this card does not claim a passing run; the observed results belong to the
  worker's and reviewer's records.
- **Boundary.** This module owns the artifact contract and the export/import population. The canonicality
  guarantee, the staged sealed-payload read, the close/verify step, destination admission before staging
  and the typed read of a non-UTF-8 artifact are the **boundary** module's cases, and the two modules
  together are one evidence set.

### Todos

None recorded for this slice. The population is the leaf's 24 cases across both modules, and the split is a
budget decision rather than a coverage one: the unit population sits exactly at its declared ceiling, so
the cases live in the integration lane, and this module's line count (1155) is the reason the boundary
population is a second file.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The three properties the cases falsify, and why the cases are consolidated rather than split. [1]
- The lane marker, and the two shared support imports that make the registry rows mandatory. [2]
- The helper set the boundary module imports rather than copies. [3]
- **The node that makes the artifact deterministic and self-accepting: one document of the declared shape that this reader accepts.** [4]
- The completeness group, its mutation set and the filtered-response pair that keeps it honest. [5]
- **The preservation nodes: every stored value held to the round trip, and `accepted` crossing as a value that promotes nothing.** [6]
- The node that exports a dataset which came through the merge — the composition the next leaves consume. [7]
- The destination-behaviour nodes: replacement only for the admitted identity, and byte preservation with no surviving stage. [8]
- The node that holds the export's identity admission and its no-Git-ancestry boundary. [9]
- The lane row that keeps this module in the certifying collection path. [10]
- The branch-fixture record whose consumer list this module is declared in. [11]
- The merge-cases record whose consumer list this module is also declared in. [12]
- The boundary module that imports this module's helpers, so the two are one evidence set, and the onboarding card that records it. [13]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
