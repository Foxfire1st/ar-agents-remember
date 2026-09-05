# mcp/tests/test_telemetry_projection_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_telemetry_projection_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused companion to `test_telemetry_projection.py` (leaf 260831-CCR-L16) that reaches the
defensive projection branches: the empty-stream guard, the certificate-refused and
admission-refused fold branches, the unmatched-kind and empty-history fold exits, the
gate/projection model validators, and the public `project_gate_history` helper. Keeping the ten
defensive cases in a small standalone module keeps the scenario suite focused and the file size
bounded.

## Code Commentary

### Logic

`test_projection_digest_mismatch_is_rejected` (`test_telemetry_projection_edges.py:55-73`) forces the
projection digest validator; `test_execution_projection_requires_at_least_one_event`
(`test_telemetry_projection_edges.py:74-79`) pins the empty-stream guard;
`test_certificate_refused_event_folds_refused_gate_state` (`test_telemetry_projection_edges.py:80-98`) and
`test_admission_refused_folds_refused_boundary` (`test_telemetry_projection_edges.py:99-121`) reach the
refusal fold branches; `test_gate_state_dispatch_with_unmatched_kind_exits_unchanged`
(`test_telemetry_projection_edges.py:154-171`) covers the unmatched-kind fold exit; and
`test_project_gate_history_returns_the_exact_gate` (`test_telemetry_projection_edges.py:172-186`)
exercises the public gate-history helper.

### Conventions

The module is standalone and defensive-branch-only; green-path parity stays in the main
projection suite.

### Invariants And Boundaries

- Only negative and defensive projection cases live here.
- No test-support imports; the module exercises the production projection models directly.
- The module is registered as explicit `unit-regression` evidence.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet. Task artifact paths are not repo-relative
citations, so this fact is recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The digest validator and empty-stream guard fail closed. | `test_projection_digest_mismatch_is_rejected`; `test_execution_projection_requires_at_least_one_event` | mcp/tests/test_telemetry_projection_edges.py:55-79 |
| Refusal fold branches and unmatched-kind exits behave defensively. | `test_certificate_refused_event_folds_refused_gate_state`; `test_admission_refused_folds_refused_boundary`; `test_gate_state_dispatch_with_unmatched_kind_exits_unchanged` | mcp/tests/test_telemetry_projection_edges.py:80-171 |
| The public gate-history helper returns the exact gate projection. | `test_project_gate_history_returns_the_exact_gate` | mcp/tests/test_telemetry_projection_edges.py:172-186 |
| The suite exercises the production fold and projection guards. | `project_execution_telemetry`; `project_gate_history`; `TelemetryProjection` | mcp/src/agents_remember/certification/telemetry/projection.py:193-244; mcp/src/agents_remember/certification/telemetry/projection.py:515-520; mcp/src/agents_remember/certification/telemetry/projection.py:147-174 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite is repository-local and exercises production certification telemetry projection guards in-process. | `test_execution_projection_requires_at_least_one_event` | mcp/tests/test_telemetry_projection_edges.py:74-79 |

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 projection
  defensive-edge suite (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
