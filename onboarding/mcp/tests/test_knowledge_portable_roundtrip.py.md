# mcp/tests/test_knowledge_portable_roundtrip.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_portable_roundtrip.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T17:45+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l06` uncommitted source; base `7db50f8f4a67e60f9011266110ad6d0156f1a905` |
| governingOverview | `mcp/tests/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three properties the cases falsify, and why the cases are consolidated rather than split. | "Completeness."; "Refusal without partial acceptance."; "Preservation." | mcp/tests/test_knowledge_portable_roundtrip.py:1-23 |
| The lane marker, and the two shared support imports that make the registry rows mandatory. | `pytestmark`; `BranchingKnowledgeFixture`; `MergeCase` | mcp/tests/test_knowledge_portable_roundtrip.py:84-84; mcp/tests/knowledge_fixture_test_support.py:161-186; mcp/tests/merge_case_test_support.py:82-132 |
| The helper set the boundary module imports rather than copies. | `identity_of`; `exported`; `artifact_of`; `envelope_of`; `reencode`; `reseal`; `import_into`; `sqlite_entries`; `row_counts_of`; `table_rows`; `identifiers_of`; `labels_of`; `_staging_directories`; `_declared_digest`; `_refusal` | mcp/tests/test_knowledge_portable_roundtrip.py:103-104; mcp/tests/test_knowledge_portable_roundtrip.py:107-116; mcp/tests/test_knowledge_portable_roundtrip.py:119-120; mcp/tests/test_knowledge_portable_roundtrip.py:123-124; mcp/tests/test_knowledge_portable_roundtrip.py:127-134; mcp/tests/test_knowledge_portable_roundtrip.py:137-148; mcp/tests/test_knowledge_portable_roundtrip.py:165-168; mcp/tests/test_knowledge_portable_roundtrip.py:171-178; mcp/tests/test_knowledge_portable_roundtrip.py:181-189; mcp/tests/test_knowledge_portable_roundtrip.py:203-208; mcp/tests/test_knowledge_portable_roundtrip.py:211-223; mcp/tests/test_knowledge_portable_roundtrip.py:279-286; mcp/tests/test_knowledge_portable_roundtrip.py:226-230; mcp/tests/test_knowledge_portable_roundtrip.py:244-247; mcp/tests/test_knowledge_portable_roundtrip.py:705-709 |
| **The node that makes the artifact deterministic and self-accepting: one document of the declared shape that this reader accepts.** | "test_the_artifact_is_one_deterministic_document_of_the_declared_shape" | mcp/tests/test_knowledge_portable_roundtrip.py:317-342 |
| The completeness group, its mutation set and the filtered-response pair that keeps it honest. | "test_an_incomplete_or_inconsistent_artifact_is_refused"; "test_a_filtered_read_response_cannot_validate_as_a_complete_export"; "test_a_complete_projection_of_the_source_tables_still_validates"; `_inconsistent_artifacts` | mcp/tests/test_knowledge_portable_roundtrip.py:646-702; mcp/tests/test_knowledge_portable_roundtrip.py:712-739; mcp/tests/test_knowledge_portable_roundtrip.py:742-758; mcp/tests/test_knowledge_portable_roundtrip.py:575-643 |
| **The preservation nodes: every stored value held to the round trip, and `accepted` crossing as a value that promotes nothing.** | "test_a_populated_dataset_round_trips_to_an_equal_logical_dataset"; "test_accepted_origin_state_crosses_as_data_and_is_not_promoted"; "test_rows_and_strings_cross_the_boundary_exactly" | mcp/tests/test_knowledge_portable_roundtrip.py:401-470; mcp/tests/test_knowledge_portable_roundtrip.py:473-486; mcp/tests/test_knowledge_portable_roundtrip.py:371-395 |
| The node that exports a dataset which came through the merge — the composition the next leaves consume. | "test_a_merged_dataset_is_also_exportable_and_restorable" | mcp/tests/test_knowledge_portable_roundtrip.py:489-499 |
| The destination-behaviour nodes: replacement only for the admitted identity, and byte preservation with no surviving stage. | "test_a_destination_is_replaced_only_for_the_admitted_identity"; "test_a_refused_import_preserves_the_destination_bytes_and_leaves_no_stage"; "test_a_successful_import_leaves_no_stage_journal_or_peer_behind"; "test_a_dangling_reference_is_refused_at_commit" | mcp/tests/test_knowledge_portable_roundtrip.py:1023-1080; mcp/tests/test_knowledge_portable_roundtrip.py:1105-1123; mcp/tests/test_knowledge_portable_roundtrip.py:1083-1102; mcp/tests/test_knowledge_portable_roundtrip.py:974-1017 |
| The node that holds the export's identity admission and its no-Git-ancestry boundary. | "test_exporting_a_moved_or_absent_dataset_is_refused"; "test_an_export_carries_no_git_ancestry_and_a_repeat_import_is_a_no_change" | mcp/tests/test_knowledge_portable_roundtrip.py:1129-1156; mcp/tests/test_knowledge_portable_roundtrip.py:502-524 |
| The lane row that keeps this module in the certifying collection path. | `integration` | mcp/tests/test-evidence-lanes.toml:138-201 |
|The branch-fixture record whose consumer list this module is declared in.|"contract:knowledge-identity-branching-fixture"| mcp/tests/evidence-lifecycle.toml:1190-1190 |
|The merge-cases record whose consumer list this module is also declared in.|"contract:common-base-merge-cases"| mcp/tests/evidence-lifecycle.toml:1280-1280 |
| The boundary module that imports this module's helpers, so the two are one evidence set, and the onboarding card that records it. | "# mcp/tests/test_knowledge_portable_boundaries.py" | onboarding/mcp/tests/test_knowledge_portable_boundaries.py.md:1-1 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1190-1190. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1280-1280. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1187-1187. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1277-1277. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1183-1183. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1273-1273. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1161-1161. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1051-1051. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1159-1159. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T07:33:51+00:00: Generated citation repair: "test_a_destination_is_replaced_only_for_the_admitted_identity"; "test_a_refused_import_preserves_the_destination_bytes_and_leaves_no_stage"; "test_a_successful_import_leaves_no_stage_journal_or_peer_behind"; "test_a_dangling_reference_is_refused_at_commit" repointed to mcp/tests/test_knowledge_portable_roundtrip.py:971-971; mcp/tests/test_knowledge_portable_roundtrip.py:1053-1053; mcp/tests/test_knowledge_portable_roundtrip.py:1031-1031; mcp/tests/test_knowledge_portable_roundtrip.py:922-922. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T07:33:51+00:00: Generated citation repair: "test_exporting_a_moved_or_absent_dataset_is_refused"; "test_an_export_carries_no_git_ancestry_and_a_repeat_import_is_a_no_change" repointed to mcp/tests/test_knowledge_portable_roundtrip.py:1077-1077; mcp/tests/test_knowledge_portable_roundtrip.py:458-458. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_a_dangling_reference_is_refused_at_commit` in the row 126 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:1053-1055 to mcp/tests/test_knowledge_portable_roundtrip.py:922, the extent of the construct the claim is about (the checker named line(s) [922] as its live location); re-pointed `test_a_destination_is_replaced_only_for_the_admitted_identity` in the row 126 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:922 to mcp/tests/test_knowledge_portable_roundtrip.py:971, the extent of the construct the claim is about (the checker named line(s) [971] as its live location); re-pointed `test_a_refused_import_preserves_the_destination_bytes_and_leaves_no_stage` in the row 126 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:971 to mcp/tests/test_knowledge_portable_roundtrip.py:1053, the extent of the construct the claim is about (the checker named line(s) [1053] as its live location); added mcp/tests/test_knowledge_portable_roundtrip.py:1077 to the row 127 of this card as the citation for `test_exporting_a_moved_or_absent_dataset_is_refused`: no cited file carried the construct, and the checker named line(s) [1077] in this file as its live location
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_a_dangling_reference_is_refused_at_commit` in the row 126 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:1031-1033 to mcp/tests/test_knowledge_portable_roundtrip.py:922-924, the extent of the construct the claim is about (the checker named line(s) [922] as its live location); re-pointed `test_a_destination_is_replaced_only_for_the_admitted_identity` in the row 126 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:922-924 to mcp/tests/test_knowledge_portable_roundtrip.py:971-973, the extent of the construct the claim is about (the checker named line(s) [971] as its live location); re-pointed `test_a_refused_import_preserves_the_destination_bytes_and_leaves_no_stage` in the row 126 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:971-973 to mcp/tests/test_knowledge_portable_roundtrip.py:1053-1055, the extent of the construct the claim is about (the checker named line(s) [1053] as its live location); re-pointed `test_exporting_a_moved_or_absent_dataset_is_refused` in the row 127 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:458-460 to mcp/tests/test_knowledge_portable_roundtrip.py:1077-1078, the extent of the construct the claim is about (the checker named line(s) [1077] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_a_dangling_reference_is_refused_at_commit` in the row 126 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:1053-1055 to mcp/tests/test_knowledge_portable_roundtrip.py:922-924, the extent of the construct the claim is about (the checker named line(s) [922] as its live location); re-pointed `test_a_destination_is_replaced_only_for_the_admitted_identity` in the row 126 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:922-924 to mcp/tests/test_knowledge_portable_roundtrip.py:971-973, the extent of the construct the claim is about (the checker named line(s) [971] as its live location); re-pointed `test_a_successful_import_leaves_no_stage_journal_or_peer_behind` in the row 126 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:971-973 to mcp/tests/test_knowledge_portable_roundtrip.py:1031-1033, the extent of the construct the claim is about (the checker named line(s) [1031] as its live location); re-pointed `test_an_export_carries_no_git_ancestry_and_a_repeat_import_is_a_no_change` in the row 127 of this card from mcp/tests/test_knowledge_portable_roundtrip.py:1077-1078 to mcp/tests/test_knowledge_portable_roundtrip.py:458-460, the extent of the construct the claim is about (the checker named line(s) [458] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/tests/test_knowledge_portable_roundtrip.py:1031-1033 in the row 126 of this card; the repetition added no pooled evidence; kept one copy of the repeated citation mcp/tests/test_knowledge_portable_roundtrip.py:458-460 in the row 127 of this card; the repetition added no pooled evidence
- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): created this one-to-one card for the leaf's artifact-contract and export/import population. It records the three properties the consolidated cases exist to falsify (completeness, refusal without partial acceptance, preservation with no promotion), the filtered-response pair that keeps the completeness group honest, the two nodes that make the contract's own claims measurable (a deterministic artifact this reader accepts, and a dataset that came **through L5's merge** being exportable and restorable), and the helper set the boundary module imports rather than copies. It records both registry obligations as preconditions rather than bookkeeping — the **integration** lane row and the two exact consumer declarations — and states that lane membership is classification and evidence rather than acceptance. The module is the larger half of a deliberate 1200-line-limit split, and its population is 18 of the leaf's 24 integration cases. Verification metadata remains empty until closeout stamps the code commit.
