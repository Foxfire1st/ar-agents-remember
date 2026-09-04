# mcp/tests/test_telemetry_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_telemetry_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The stream-validation verification suite for the CCR-R16@v3 durable telemetry validator (leaf
260831-CCR-L16). Its thirty-eight unit-regression tests build complete ordered event traces and
force `certification/telemetry/validation.py` to fail closed on missing, duplicate, out-of-order,
cross-identity, cardinality-invalid, and result-inconsistent streams, and to report green
telemetry readiness only for a valid stream.

## Code Commentary

### Logic

The suite inlines trace and rail-spec builders (`_RailSpec`, `_Trace`, `_GateRunOptions`,
`test_telemetry_validation.py:96-425`). Green parity is pinned by
`test_complete_green_gate_one_trace_is_valid` (`test_telemetry_validation.py:426-435`) and
`test_telemetry_readiness_is_green_on_valid_stream` (`test_telemetry_validation.py:799-917`); red
cardinality is forced by `test_rail_terminal_without_rail_start_is_invalid`,
`test_duplicate_rail_terminal_is_invalid`, and `test_rail_pass_without_evidence_is_invalid`
(`test_telemetry_validation.py:479-508`); catalog invalidity by
`test_catalog_missing_terminal_is_invalid` (`test_telemetry_validation.py:509-518`); blocking by
`test_gate_blocked_with_started_later_gate_is_invalid` (`test_telemetry_validation.py:640-661`); envelope
rules by `test_diagnostic_envelope_accepts_only_diagnostic_and_control_events`
(`test_telemetry_validation.py:675-712`); terminal rules by `test_operation_terminal_must_be_final`
(`test_telemetry_validation.py:726-738`); cross-identity rules by
`test_cross_generation_identity_is_invalid` (`test_telemetry_validation.py:760-768`); and the empty
stream by `test_empty_stream_is_invalid` (`test_telemetry_validation.py:777-782`), with
`test_telemetry_readiness_is_red_on_invalid_stream` (`test_telemetry_validation.py:783-798`) pinning
the typed red readiness.

### Conventions

Every red assertion expects an exact finding code through the production validator; no rail is
ever rerun and no rail pass is derived from telemetry alone.

### Invariants And Boundaries

- Green is asserted only for fully valid streams; every other shape is red with typed findings.
- The suite never touches the store or writes journals.
- The module is registered as explicit `unit-regression` evidence.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose exhaustive event matrix defines the
cardinality rules this suite forces. Task artifact paths are not repo-relative citations, so
this fact is recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Green parity and typed red readiness are pinned on complete traces. | `test_telemetry_readiness_is_green_on_valid_stream`; `test_telemetry_readiness_is_red_on_invalid_stream` | mcp/tests/test_telemetry_validation.py:783-917 |
| Rail, catalog, blocking, envelope, terminal, identity, and empty-stream rules fail closed. | `test_rail_terminal_without_rail_start_is_invalid`; `test_catalog_missing_terminal_is_invalid`; `test_diagnostic_envelope_accepts_only_diagnostic_and_control_events`; `test_empty_stream_is_invalid` | mcp/tests/test_telemetry_validation.py:479-518; mcp/tests/test_telemetry_validation.py:675-712; mcp/tests/test_telemetry_validation.py:777-782 |
| The suite exercises the production validator and readiness models. | `validate_execution_telemetry`; `compile_telemetry_readiness`; `TelemetryValidationReport` | mcp/src/agents_remember/certification/telemetry/validation.py:90-111; mcp/src/agents_remember/certification/telemetry/validation.py:114-121; mcp/src/agents_remember/certification/telemetry/validation.py:56-69 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite is repository-local and exercises production certification telemetry validation in-process. | `test_complete_green_gate_one_trace_is_valid` | mcp/tests/test_telemetry_validation.py:426-435 |

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 exhaustive stream
  validation suite (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
