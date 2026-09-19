# mcp/tests/test_knowledge_portable_boundaries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_portable_boundaries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T17:45+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l06` uncommitted source; base `7db50f8f4a67e60f9011266110ad6d0156f1a905` |
| governingOverview | `mcp/tests/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The five properties that live here because the ordinary path cannot fail them. | "Five properties live here" | mcp/tests/test_knowledge_portable_boundaries.py:1-14 |
| The lane marker, and the three shared support artifacts this module's registry row must declare. | `pytestmark`; `BranchingKnowledgeFixture`; `MergeCase`; `SnapshotCase` | mcp/tests/test_knowledge_portable_boundaries.py:73-74; mcp/tests/knowledge_fixture_test_support.py:160-186; mcp/tests/merge_case_test_support.py:81-132; mcp/tests/snapshot_lifecycle_test_support.py:130-175 |
| The helpers imported from the round-trip module, so the two modules keep one definition of an artifact and a refusal. | `test_knowledge_portable_roundtrip` | mcp/tests/test_knowledge_portable_boundaries.py:60-71 |
| The journal-mode reader the WAL cases assert the **published destination** through. | `journal_mode_of` | mcp/tests/test_knowledge_portable_boundaries.py:75-87 |
| **The freeze's closure proved on the published destination, from the producer this leaf shares with L4.** | "test_a_frozen_snapshot_of_a_wal_resident_candidate_is_published_closed" | mcp/tests/test_knowledge_portable_boundaries.py:88-131 |
| **The node the whole guarantee rests on: every non-canonical spelling axis, the `canonical_document` assertions, and all seven header types pinned — the header's namespace guard (`bound`) is the one reachable guard the population does not kill (an observation for L9).** | "test_the_canonical_form_of_the_whole_document_is_the_only_form_the_reader_accepts"; `bound`; `_assert_the_header_types_are_pinned`; `_header_type_respellings`; `_non_canonical_axes`; `_reordered_document`; `_respelled_encoding`; `_permuted_value`; `_permuted_origin_refs`; `_canonical_value`; `_nested_spelling_mutants` | mcp/tests/test_knowledge_portable_boundaries.py:140-264; mcp/src/agents_remember/memory/knowledge/export_portable.py:981-998; mcp/tests/test_knowledge_portable_boundaries.py:267-378; mcp/tests/test_knowledge_portable_boundaries.py:381-416; mcp/tests/test_knowledge_portable_boundaries.py:424-453; mcp/tests/test_knowledge_portable_boundaries.py:456-465; mcp/tests/test_knowledge_portable_boundaries.py:468-487; mcp/tests/test_knowledge_portable_boundaries.py:490-502; mcp/tests/test_knowledge_portable_boundaries.py:505-521; mcp/tests/test_knowledge_portable_boundaries.py:524-534; mcp/tests/test_knowledge_portable_boundaries.py:537-561 |
| **The staged sealed-aggregate read, tampering every retained row of both revision tables with the destination held identical.** | "test_an_artifact_whose_sealed_payload_contradicts_its_digest_is_refused" | mcp/tests/test_knowledge_portable_boundaries.py:611-611 |
| The import's close/verify step, proved by a stage opened in WAL mode. | "test_a_stage_opened_in_wal_mode_is_published_as_a_closed_database" | mcp/tests/test_knowledge_portable_boundaries.py:662-662 |
| **Destination admission before any staging work: three states, their own codes, and no stage directory even requested.** | "test_destination_admission_refuses_before_any_staging_work" | mcp/tests/test_knowledge_portable_boundaries.py:700-700 |
| The typed read of an artifact that is not readable UTF-8 text. | "test_an_artifact_that_cannot_be_read_as_text_is_refused_with_a_typed_code" | mcp/tests/test_knowledge_portable_boundaries.py:763-763 |
| The unreachable defence-in-depth branch whose mutation survives for a stated reason. | `_out_of_canonical_order` | mcp/src/agents_remember/memory/knowledge/export_portable.py:931-964 |
| The integration-lane row this module occupies. | `integration` | mcp/tests/test-evidence-lanes.toml:201-201 |
| The snapshot-lifecycle artifact whose consumer list gained this module. | "id = \"knowledge-snapshot-lifecycle-cases\"" | mcp/tests/evidence-lifecycle.toml:40-40 |
| The merge-cases artifact whose consumer list gained this module. | "id = \"common-base-merge-cases\"" | mcp/tests/evidence-lifecycle.toml:45-45 |
| The identity-branching fixture artifact whose consumer list gained this module. | "id = \"knowledge-identity-branching-fixture\"" | mcp/tests/evidence-lifecycle.toml:25-25 |
| The L4 node this module corroborates rather than replaces, and its own marker caveat. | "test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not" | mcp/tests/test_knowledge_snapshot_publication.py:81-110 |
| The round-trip module whose helpers this one imports, and the onboarding card that records the shared set. | "# mcp/tests/test_knowledge_portable_roundtrip.py" | onboarding/mcp/tests/test_knowledge_portable_roundtrip.py.md:1-1 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 1 enforced `citation_anchor_absent_from_range` row in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/test_knowledge_portable_boundaries.py:73-73` → `mcp/tests/test_knowledge_portable_boundaries.py:73-74` (row 108). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_an_artifact_whose_sealed_payload_contradicts_its_digest_is_refused" repointed to mcp/tests/test_knowledge_portable_boundaries.py:611-611. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_stage_opened_in_wal_mode_is_published_as_a_closed_database" repointed to mcp/tests/test_knowledge_portable_boundaries.py:662-662. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_destination_admission_refuses_before_any_staging_work" repointed to mcp/tests/test_knowledge_portable_boundaries.py:700-700. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_an_artifact_that_cannot_be_read_as_text_is_refused_with_a_typed_code" repointed to mcp/tests/test_knowledge_portable_boundaries.py:763-763. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:40-40. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:45-45. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:25-25. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "id = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1120-1120. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "id = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1145-1145. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: "id = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1118-1118. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: "id = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1143-1143. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: "id = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:1035-1035. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T04:55:18+00:00: Generated citation repair: "id = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1114-1114. No content impact: mechanical anchor-range projection bound to citation source snapshot 116840615150c9097436b691cc4243186059d79f882e7a6c73cd85d688950e12; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T04:55:18+00:00: Generated citation repair: "id = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1139-1139. No content impact: mechanical anchor-range projection bound to citation source snapshot 116840615150c9097436b691cc4243186059d79f882e7a6c73cd85d688950e12; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T04:55:18+00:00: Generated citation repair: "id = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:1033-1033. No content impact: mechanical anchor-range projection bound to citation source snapshot 116840615150c9097436b691cc4243186059d79f882e7a6c73cd85d688950e12; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:39:57+00:00: Generated citation repair: "test_a_stage_opened_in_wal_mode_is_published_as_a_closed_database" repointed to mcp/tests/test_knowledge_portable_boundaries.py:618-618. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:39:57+00:00: Generated citation repair: "test_destination_admission_refuses_before_any_staging_work" repointed to mcp/tests/test_knowledge_portable_boundaries.py:656-656. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): created this one-to-one card for the leaf's boundary population. It records each of the five properties and why the ordinary path cannot fail it: the freeze's closure measured on the **published destination**, the whole-document canonical-form node (every spelling axis, and **all seven header keys respelled with a different JSON type** — each refused and each passing the gate, which proves the refusal is the header check's), the **staged sealed-aggregate read** that made the review's HIGH finding unfalsifiable by tampering every retained row of both revision tables with the destination held identical, destination admission asserted before any staging work with no stage directory requested, and the typed read of a non-UTF-8 artifact. It records the two mutations that legitimately survive with their stated reasons — `_out_of_canonical_order` unreachable defence in depth, and the header namespace-binding guard at `:911` reachable with no killing node, reported for **L9** — so neither is mistaken for coverage, and it states that the final fix round extended these cases rather than adding one. Verification metadata remains empty until closeout stamps the code commit.
