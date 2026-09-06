# mcp/tests/test_rail_bindings.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_rail_bindings.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:56:02+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests payload construction from observed evidence/artifact bytes, consumption by the certificate compiler, declaration-owned environment census publication, and isolation of the shared Dagger container handle.

## Code Commentary

### Logic

Pure builders bind evidence ids to the capture's digest/size/reference, including valid empty captures. Artifact builders bind observed files and return missing required ids without fabricating values. A synthetic producer fixture writes a file for every declared artifact, then passes those observations through Gates 1–4 and validates the resulting certificate chain. Its lane uses explicit synthetic source-selection input; the chain is compiler evidence, not a Git observation or live rail execution.

The map-coverage test combines the fixed command-producer map with environment artifact IDs and paths from the profile. Those two inventories must be disjoint; their union must exactly equal the required-on-pass artifact IDs, and every mapped path must appear in the finite publication inventory. Each environment artifact must also belong to its declared producer rail. Dashboard E2E results, provider integration results and teardown proof remain covered; there is no accepted gap list. The separate full-chain fixture still supplies its own synthetic files and does not stand in for live producer execution.

Focused assertions bind the Python suite result to `pytest-phases.json`. Dashboard coverage is read from the Vitest source `/workspace/dashboard/coverage/coverage-final.json` and exported at the stable `dashboard-coverage.json` publication path. The immutable container double proves evidence attachment preserves the shared handle used by later rails.

The environment-producer case runs the production census builder over real tiny dependency files
through the SDK fixture, then attaches the observed output through the actual emission owner. Both
the profile's original locator and a relocated artifact ID/path must bind the retained bytes with
their exact hash and size. The parent container remains identical and has no census output file;
only the detached retained output contains that file. This checks the producer and binding
composition without claiming a live Dagger installation or complete certification run.

### Conventions

Dynamic imports load the repository-owned .dagger helpers. Synthetic rail files and source-selection inputs remain explicit fixtures. Environment census bytes are produced by the actual census owner over temporary files, with SDK execution still doubled.

### Invariants And Boundaries

- Bind only observed bytes; a missing required artifact stays missing.
- Empty output is valid evidence with the digest of empty bytes.
- Attaching evidence must not mutate the shared execution container.
- Fixed and environment-declared artifact maps must remain disjoint; their union and publication-path membership are checked exactly.
- Census bindings follow the declared producer and locator, with no output leakage into the parent container.
- Absent required producers are not an accepted exception.

### Todos

Keep full-chain fixture claims separate from producer-backed publication coverage in `test_rail_evidence_publication.py` and the live Dagger run.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| Each evidence ID binds observed capture bytes. | `test_evidence_bindings_bind_real_capture_for_every_declared_id` | mcp/tests/test_rail_bindings.py:112-131 |
| Empty output has the actual empty-byte digest. | `test_evidence_bindings_an_empty_capture_is_a_real_empty_capture` | mcp/tests/test_rail_bindings.py:134-140 |
| Missing required files remain missing. | `test_artifact_bindings_bind_observed_files_and_journal_gaps_never_fake` | mcp/tests/test_rail_bindings.py:143-166 |
| Synthetic bound files compose through the real certificate compiler. | `test_emitted_bindings_feed_the_green_mint_chain` | mcp/tests/test_rail_bindings.py:169-233 |
| An unbound required artifact refuses certificate compilation. | `test_unbound_required_artifact_refuses_the_manifest_not_a_fake_digest` | mcp/tests/test_rail_bindings.py:236-276 |
| Fixed and declared environment mappings are disjoint; their union exactly covers required artifacts and published paths. | `test_artifact_map_covers_every_declared_required_on_pass_artifact` | mcp/tests/test_rail_bindings.py:279-301 |
| Python suite result uses the actual phase-report file. | `test_mapped_suite_result_binds_the_pytest_phases_file` | mcp/tests/test_rail_bindings.py:304-323 |
| The source coverage path and stable exported path are independently asserted. | `test_dashboard_coverage_map_targets_the_vitest_coverage_json` | mcp/tests/test_rail_bindings.py:326-342 |
| The SDK double supplies fixed existence/size observations and detached inspection handles. | `_FakeContainer` | mcp/tests/test_rail_bindings.py:353-375 |
| Binding publication retains later-rail container identity. | `test_emission_never_mutates_the_shared_execution_container` | mcp/tests/test_rail_bindings.py:394-417 |
| The compiler lane receives explicit synthetic candidate/source-selection input. | `_lane` | mcp/tests/test_rail_bindings.py:84-109 |
| Actual census bytes bind both original and relocated declarations without appearing on the parent container. | `test_environment_producer_binds_actual_census_at_its_declared_locator` | mcp/tests/test_rail_bindings.py:421-462 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T14:56:02+00:00 — Bound the reviewed card body and active citations to actual source commit c69d5171187fa1957025e393270db9f5a864ab14 after checking source-byte equality. Preserved prior history; this verifies memory claims and does not assert additional test execution.

- 2026-09-06T14:02:59+00:00 — L33 candidate curation: Documented disjoint fixed/environment artifact ownership, exact declared census locators and retained-byte bindings, and parent-container isolation; preserved synthetic compiler-chain limits and repaired source anchors. Reviewed uncommitted source; the prior verification commit/date remain unchanged. This records source behavior, not gate or acceptance evidence.


- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Replaced the obsolete three-gap acceptance with exact complete artifact-map and publication-path equality, and documented the stable dashboard coverage export path.

- 2026-09-05T06:14:14+00:00 — Created the emission test account and made explicit that its synthetic chain fixture coexists with three real producer gaps.
