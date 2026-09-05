# mcp/tests/test_rail_bindings.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_rail_bindings.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `8f670ceecd75323600c873d40c47c4a1cc946ab3` |
| lastVerifiedCommitDate | 2026-09-05T06:48:24+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests payload construction from observed evidence/artifact bytes, consumption by the certificate compiler, and non-mutation of the shared Dagger container handle.

## Code Commentary

### Logic

Pure builders bind evidence ids to the capture's digest/size/reference, including valid empty captures. Artifact builders bind observed files and return missing required ids without fabricating values. A synthetic producer fixture writes a file for every declared artifact, then passes those observations through Gates 1–4 and validates the resulting certificate chain.

The map-coverage test currently requires the missing set to equal three documented gaps: dashboard-e2e-result, provider-integration-result and teardown-proof. It therefore records the absence of those production bindings rather than proving map completeness. The full-chain fixture supplies files for those gaps itself and cannot establish that the real executor produces them.

Focused assertions bind the Python suite result to pytest-phases.json and dashboard coverage to Vitest's coverage-final.json. The immutable container double proves evidence attachment does not reassign or execute on the shared handle used by later rails.

### Conventions

Dynamic imports load the repository-owned .dagger helpers without turning them into normal Python package imports. Synthetic observed files remain fixtures, never accepted run artifacts.

### Invariants And Boundaries

- Bind only observed bytes; a missing required artifact stays missing.
- Empty output is valid evidence with the digest of empty bytes.
- Attaching evidence must not mutate the shared execution container.
- A test that asserts the current gap list is not proof that the gap is acceptable.

### Todos

The three documented Gate-4 producer gaps require implementation and revised completeness tests before full certification can succeed.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Observed capture/file binding and explicit gaps | `test_evidence_bindings_bind_real_capture_for_every_declared_id`; `test_artifact_bindings_bind_observed_files_and_journal_gaps_never_fake` | mcp/tests/test_rail_bindings.py:107-161 |
| Synthetic certificate chain and missing-artifact refusal | `test_emitted_bindings_feed_the_green_mint_chain`; `test_unbound_required_artifact_refuses_the_manifest_not_a_fake_digest` | mcp/tests/test_rail_bindings.py:164-271 |
| Documented producer gaps and concrete mapped file contracts | `_DOCUMENTED_ARTIFACT_GAPS`; `test_artifact_map_covers_every_declared_required_on_pass_artifact`; `test_mapped_suite_result_binds_the_pytest_phases_file`; `test_dashboard_coverage_map_targets_the_vitest_coverage_json` | mcp/tests/test_rail_bindings.py:274-338 |
| Immutable container double and no shared-handle mutation | `_FakeContainer`; `test_emission_never_mutates_the_shared_execution_container` | mcp/tests/test_rail_bindings.py:341-409 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Created the emission test account and made explicit that its synthetic chain fixture coexists with three real producer gaps.
