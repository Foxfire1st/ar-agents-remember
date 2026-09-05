# mcp/tests/test_telemetry_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_telemetry_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The focused model-level verification suite for the CCR-R16@v3 durable telemetry vocabulary
(leaf 260831-CCR-L16). Its sixty-three unit-regression tests force the frozen event schema and
closed vocabularies of `certification/telemetry/models.py` fail closed: execution identity,
exhaustive-matrix ID cardinality, certificate refusal codes, terminal result classes, per-kind
payload shape guards, span overlap math, deterministic catalog manifest digests, and the exact
gate/rail identity agreement rules on `TelemetryEvent`.

## Code Commentary

### Logic

The module builds real production events through the compile adapters and asserts model
refusals. `test_closeout_execution_identity_requires_operation_kind_and_generation`
(`test_telemetry_models.py:95-122`) and `test_closeout_event_requires_operation_kind_and_generation`
(`test_telemetry_models.py:840-851`) force the closeout-generation identity contract;
`test_diagnostic_run_can_never_acquire_certificate_authority`
(`test_telemetry_models.py:123-146`) pins the diagnostic-run exclusion;
`test_gate_pass_reuse_requires_prior_identity` (`test_telemetry_models.py:198-248`) pins the R21
reuse identity rule; `test_span_model_and_overlap_not_double_counted`
(`test_telemetry_models.py:280-317`) verifies span aggregation over contained and extending
overlaps; `test_catalog_counts_and_manifest_digest_are_deterministic`
(`test_telemetry_models.py:318-363`) verifies the ordered-terminal-set digest;
`test_rail_event_requires_the_exact_rail_identity` (`test_telemetry_models.py:464-474`) and
`test_catalog_disposition_must_match_enforcing_results` (`test_telemetry_models.py:765-777`)
pin the identity/disposition agreement rules, and `test_invalidation_closure_must_contain_the_gate`
(`test_telemetry_models.py:815-819`) pins the invalidation closure shape.

### Conventions

Every refusal asserts an exact model error or vocabulary membership; nothing here touches the
store, projection, or validator layers.

### Invariants And Boundaries

- The suite is model-only: no durable journal writes and no stream validation.
- Fail-closed assertions cover identity, cardinality, digest, and payload-shape rules, never
  fallback behavior.
- The module is registered as explicit `unit-regression` evidence.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose execution-identity and exhaustive-event-matrix
sections normatively define the rules this suite forces. Task artifact paths are not repo-relative
citations, so this fact is recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout-generation identity, matrix cardinality, and diagnostic-run exclusion fail closed on the root event. | `test_closeout_execution_identity_requires_operation_kind_and_generation`; `test_diagnostic_run_can_never_acquire_certificate_authority` | mcp/tests/test_telemetry_models.py:95-146 |
| R21 reuse, span totals, catalog digest, and invalidation closure shapes are pinned. | `test_gate_pass_reuse_requires_prior_identity`; `test_span_model_and_overlap_not_double_counted`; `test_catalog_counts_and_manifest_digest_are_deterministic` | mcp/tests/test_telemetry_models.py:198-248; mcp/tests/test_telemetry_models.py:280-363 |
| Exact gate/rail identity, payload-shape, and catalog disposition agreement rules fail closed. | `test_rail_event_requires_the_exact_rail_identity`; `test_catalog_disposition_must_match_enforcing_results` | mcp/tests/test_telemetry_models.py:464-474; mcp/tests/test_telemetry_models.py:765-777 |
| The suite exercises the production event schema and matrix vocabulary. | `TelemetryEvent`; `EVENT_MATRIX` | mcp/src/agents_remember/certification/telemetry/models.py:673-851; mcp/src/agents_remember/certification/telemetry/models.py:160-185 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite is repository-local and exercises production certification telemetry models in-process. | `test_catalog_counts_and_manifest_digest_are_deterministic` | mcp/tests/test_telemetry_models.py:318-363 |

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 telemetry model
  vocabulary suite (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
