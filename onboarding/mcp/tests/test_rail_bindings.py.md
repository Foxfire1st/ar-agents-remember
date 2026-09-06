# mcp/tests/test_rail_bindings.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_rail_bindings.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests payload construction from observed evidence/artifact bytes, consumption by the certificate compiler, and non-mutation of the shared Dagger container handle.

## Code Commentary

### Logic

Pure builders bind evidence ids to the capture's digest/size/reference, including valid empty captures. Artifact builders bind observed files and return missing required ids without fabricating values. A synthetic producer fixture writes a file for every declared artifact, then passes those observations through Gates 1–4 and validates the resulting certificate chain.

The map-coverage test requires exact equality between every required-on-pass artifact ID and the complete binding map, and requires every mapped output path to be in the finite profile publication inventory. Dashboard E2E results, provider integration results and teardown proof are included; there is no accepted gap list. The separate full-chain fixture still supplies its own synthetic files and does not stand in for live producer execution.

Focused assertions bind the Python suite result to `pytest-phases.json`. Dashboard coverage is read from the Vitest source `/workspace/dashboard/coverage/coverage-final.json` and exported at the stable `dashboard-coverage.json` publication path. The immutable container double proves evidence attachment does not reassign or execute on the shared handle used by later rails.

### Conventions

Dynamic imports load the repository-owned .dagger helpers without turning them into normal Python package imports. Synthetic observed files remain fixtures, never accepted run artifacts.

### Invariants And Boundaries

- Bind only observed bytes; a missing required artifact stays missing.
- Empty output is valid evidence with the digest of empty bytes.
- Attaching evidence must not mutate the shared execution container.
- Artifact map equality and publication-path membership must both hold; absent required producers are not an accepted exception.

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
| Each evidence ID binds observed capture bytes. | `test_evidence_bindings_bind_real_capture_for_every_declared_id` | mcp/tests/test_rail_bindings.py:107-126 |
| Empty output has the actual empty-byte digest. | `test_evidence_bindings_an_empty_capture_is_a_real_empty_capture` | mcp/tests/test_rail_bindings.py:129-135 |
| Missing required files remain missing. | `test_artifact_bindings_bind_observed_files_and_journal_gaps_never_fake` | mcp/tests/test_rail_bindings.py:138-161 |
| Synthetic bound files compose through the real certificate compiler. | `test_emitted_bindings_feed_the_green_mint_chain` | mcp/tests/test_rail_bindings.py:164-228 |
| An unbound required artifact refuses certificate compilation. | `test_unbound_required_artifact_refuses_the_manifest_not_a_fake_digest` | mcp/tests/test_rail_bindings.py:231-271 |
| The artifact map exactly equals the required-on-pass inventory and all paths are published. | `test_artifact_map_covers_every_declared_required_on_pass_artifact` | mcp/tests/test_rail_bindings.py:274-285 |
| Python suite result uses the actual phase-report file. | `test_mapped_suite_result_binds_the_pytest_phases_file` | mcp/tests/test_rail_bindings.py:288-307 |
| The source coverage path and stable exported path are independently asserted. | `test_dashboard_coverage_map_targets_the_vitest_coverage_json` | mcp/tests/test_rail_bindings.py:310-326 |
| The SDK double supports no-follow existence and file-size observation. | `_FakeContainer` | mcp/tests/test_rail_bindings.py:337-359 |
| Binding publication retains later-rail container identity. | `test_emission_never_mutates_the_shared_execution_container` | mcp/tests/test_rail_bindings.py:378-400 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Replaced the obsolete three-gap acceptance with exact complete artifact-map and publication-path equality, and documented the stable dashboard coverage export path.

- 2026-09-05T06:14:14+00:00 — Created the emission test account and made explicit that its synthetic chain fixture coexists with three real producer gaps.
