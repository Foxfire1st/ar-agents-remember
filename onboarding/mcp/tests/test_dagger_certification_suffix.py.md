# mcp/tests/test_dagger_certification_suffix.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dagger_certification_suffix.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:46:49+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Protects Dagger-side interpretation of a frozen code-certification suffix and its retained predecessor reports. Tests combine actual stored publications and real retained-byte verification with an SDK graph double; they do not claim ordinary rails executed in a live engine.

## Code Commentary

### Logic

`_manifest` preserves the supplied run's actual frozen repository plan, comparison base and source-selection population, then includes explicit execution and retained-report inputs. `_RetainedContainer` runs the production retained-report verification shell against physical temporary files; other container operations use the shared SDK double. Assertions inspect the container actually returned to `export_profile_reports`, preserving detached census-output semantics.

The first-gate matrix covers Gates 1 through 4. Reused rows retain original certificate/result digests and publication bindings, have no fresh rails and do not enter attempted/completed steps. Later suffixes reconstruct the declared environment; Gates 3 and 4 also receive original coverage bytes. A failing suffix retains reused predecessors, publishes the complete red gate and leaves later gates not run.

Transport cases physically delete, corrupt or symlink retained files and require refusal before suffix quality rails. Other cases reject absent or undeclared transport, detached execution/base/plan/digest/prefix inputs, contradictory zero-start/results and invalid original environment census. Omitting a census entry reaches reconstruction failure with exit code 66 and an attempted-but-not-completed environment step.

Capacity checks derive retained-member bounds and producer gates from frozen declarations. Manifest tests recompute digests before exercising candidate drift and unsafe environment paths. Duplicate publication paths refuse even when an earlier duplicate belongs only to a future gate and could otherwise disappear during retained-prefix filtering.

### Conventions

Physical fault injection targets temporary report files; semantic faults rewrite explicit untrusted manifest inputs. Environment installation and ordinary rail results remain injected SDK behavior.

### Invariants And Boundaries

- Reuse transports original evidence without emitting predecessor gates as fresh execution.
- Retained-byte verification precedes suffix rails that consume those bytes.
- The actual returned/exported container owns detached census output.
- Frozen declarations govern transport size and uniqueness before gate filtering.
- This suite verifies the Dagger composition contract, not live engine execution or complete lifecycle acceptance.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for these repository-owned test contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source governs this file. | N/A | N/A |

## Repo-Internal References

These source anchors establish the actual owner calls, fixture inputs and execution limits described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The retained container runs the production verification shell on real temporary files. | `_RetainedContainer` | mcp/tests/test_dagger_certification_suffix.py:38-59 |
| The manifest retains the frozen plan and source-selection inputs. | `_manifest` | mcp/tests/test_dagger_certification_suffix.py:62-78 |
| Every suffix preserves original predecessor results and inspects actual exported output. | `test_frozen_suffix_starts_only_selected_gates_and_preserves_original_results` | mcp/tests/test_dagger_certification_suffix.py:89-148 |
| Missing, changed or unsafe transport refuses before suffix quality rails. | `test_dagger_rechecks_actual_transported_bytes_before_any_suffix_rail` | mcp/tests/test_dagger_certification_suffix.py:152-189 |
| Contradictory execution inputs refuse before engine use. | `test_detached_or_contradictory_execution_inputs_refuse_before_engine_use` | mcp/tests/test_dagger_certification_suffix.py:195-229 |
| A red suffix retains complete gate results and zero-start successors. | `test_failed_suffix_publishes_complete_red_gate_and_zero_start_successors` | mcp/tests/test_dagger_certification_suffix.py:232-271 |
| Transport presence must match reuse and executor declaration. | `test_transport_presence_and_declaration_are_exact` | mcp/tests/test_dagger_certification_suffix.py:274-301 |
| Reconstruction validates the original census and records comparison failure. | `test_environment_reconstruction_refuses_missing_or_changed_original_before_suffix` | mcp/tests/test_dagger_certification_suffix.py:305-341 |
| Frozen producer declarations determine member bounds. | `test_retained_member_bound_comes_from_frozen_producer_publications` | mcp/tests/test_dagger_certification_suffix.py:345-360 |
| Recomputed digests do not authorize a different gate candidate. | `test_manifest_refuses_gate_candidate_drift_even_with_recomputed_digests` | mcp/tests/test_dagger_certification_suffix.py:379-390 |
| Environment identifiers and paths remain confined before runtime use. | `test_manifest_confines_environment_paths_before_runtime_use` | mcp/tests/test_dagger_certification_suffix.py:403-419 |
| Duplicate paths refuse before retained-gate filtering can hide them. | `test_resume_manifest_refuses_duplicate_paths_before_retained_gate_filter` | mcp/tests/test_dagger_certification_suffix.py:423-443 |

## Cross-Repo References

The modeled or temporary repositories belong to this isolated test composition. This file establishes no external repository or host lifecycle authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History

- 2026-09-06T14:46:49+00:00 — Created after reviewing actual source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented suffix preservation, physical transport checks, exported-container ownership and manifest refusals. This source verification makes no gate or acceptance claim.
