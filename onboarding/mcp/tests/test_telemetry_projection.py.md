# mcp/tests/test_telemetry_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_telemetry_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The durable-reconstruction verification suite for the CCR-R16@v3 telemetry projection (leaf
260831-CCR-L16). Nine end-to-end scenario tests build full multi-gate, multi-rail, multi-attempt
event traces through the production compile adapters and force
`certification/telemetry/projection.py` to fold them into lossless boundary/gate projections for the
journal, status, wait, and dashboard surfaces.

## Code Commentary

### Logic

The suite inlines scenario builders (`_Scenario`, `_Trace`, `_RailSpec`, `_GateRun`,
`test_telemetry_projection.py:113-550`) that compile admission, gate, rail, catalog, certificate,
diagnostic, and finalization events and then drive `project_execution_telemetry`.
`test_multi_failure_gate_one_projects_failed_and_zero_start` (`test_telemetry_projection.py:551-597`)
verifies a red Gate-1 catalog with every enforcing failure and the zero-start barrier;
`test_gate_two_red_barrier_blocks_later_gates` (`test_telemetry_projection.py:598-684`) verifies
blocked later gates; `test_gate_four_certifying_e2e_carries_repetition_and_diagnostics_stay_separate`
(`test_telemetry_projection.py:742-800`) pins the certifying Gate-4 repetition rule and the
diagnostic separation; `test_memory_only_gate_five_reuse_invalidates_then_reuses`
(`test_telemetry_projection.py:801-887`) covers invalidation-then-reuse;
`test_finalization_resume_trace_projects_boundary_and_terminal` (`test_telemetry_projection.py:939-1012`)
covers the durable finalization boundary; `test_operation_terminal_gate_result_class_binds_available_manifest`
(`test_telemetry_projection.py:1013-1044`) pins the gate-result terminal manifest binding; and
`test_two_repository_profiles_produce_the_same_generic_schema` (`test_telemetry_projection.py:1045-1120`)
verifies the projection stays repository-neutral across profiles.

### Conventions

Each scenario asserts the projected gate/rail/boundary state and the projection digest, so the
test proves the fold is lossless and content-addressable without rerunning rails.

### Invariants And Boundaries

- Projection tests run in-process over compiled events only; no rails execute and no store is
  written.
- The empty-stream guard, defensive fold branches, and unmatched-kind exits live in the focused
  companion suite `test_telemetry_projection_edges.py`.
- The module is registered as explicit `unit-regression` evidence.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose normative requirement states that public
state must be reconstructable without ephemeral-log parsing - exactly what these scenario folds
verify. Task artifact paths are not repo-relative citations, so this fact is recorded as prose
here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Red catalogs, zero-start barriers, and blocked later gates project their exact state. | `test_multi_failure_gate_one_projects_failed_and_zero_start`; `test_gate_two_red_barrier_blocks_later_gates` | mcp/tests/test_telemetry_projection.py:551-684 |
| Gate-4 certifying repetition, diagnostic separation, and Gate-5 reuse/invalidation project losslessly. | `test_gate_four_certifying_e2e_carries_repetition_and_diagnostics_stay_separate`; `test_memory_only_gate_five_reuse_invalidates_then_reuses` | mcp/tests/test_telemetry_projection.py:742-887 |
| Finalization boundaries, operation terminals, and schema neutrality are pinned. | `test_finalization_resume_trace_projects_boundary_and_terminal`; `test_two_repository_profiles_produce_the_same_generic_schema` | mcp/tests/test_telemetry_projection.py:939-1012; mcp/tests/test_telemetry_projection.py:1045-1120 |
| The suite exercises the production fold and projection models. | `project_execution_telemetry`; `TelemetryProjection` | mcp/src/agents_remember/certification/telemetry/projection.py:193-244; mcp/src/agents_remember/certification/telemetry/projection.py:147-174 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite is repository-local and exercises production certification telemetry projection in-process. | `test_operation_terminal_gate_result_class_binds_available_manifest` | mcp/tests/test_telemetry_projection.py:1013-1044 |

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 durable
  reconstruction projection suite (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
