# mcp/src/agents_remember/certification/telemetry/validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/telemetry/validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

Exhaustive matrix and cardinality validation for one durable CCR-R16@v3 execution stream.
Missing, duplicate, out-of-order, cross-identity, cardinality-invalid, or result-inconsistent
events make telemetry readiness red. The validator never reruns a rail and never derives a rail
pass from telemetry alone: a passing rail-terminal must carry its own bounded evidence.

## Code Commentary

### Logic

`TelemetryValidationReport` (`validation.py:56-69`) is a closed report - red findings never double as
rail passes - and `TelemetryReadiness` (`validation.py:72-87`) is the typed readiness projection:
green exactly when no findings exist. `validate_execution_telemetry` (`validation.py:90-111`) validates
one complete ordered stream and never raises: it records `missing-execution-events` on an empty
stream, then runs the identity check (`_validate_stream_identity` at `validation.py:137-180`), the
diagnostic envelope check (`_validate_diagnostic_envelope`), the zero-start barrier check
(`_validate_zero_start_barrier`), rail start/terminal matching (`_validate_rail_matching` at
`validation.py:218-233` with the per-kind checks `_check_gate_start`, `_check_rail_start`,
`_check_rail_terminal`), catalog validation (`_validate_catalogs` at `validation.py:335-364` with
`_validate_catalog_records`, `_partition_catalog_terminals`, `_validate_catalog_terminal_match`,
`_validate_extra_terminals`, `_validate_catalog_manifest_match`, `_validate_catalog_latest_stale`,
`_validate_catalog_disposition`), catalog citation validation (`_validate_catalog_citations` at
`validation.py:489-534`), blocked-gate validation (`_validate_blocked_gates`), invalidation
validation (`_validate_invalidations`), operation-terminal validation
(`_validate_operation_terminal`), finalization validation (`_validate_finalization` at
`validation.py:762-805`), and the rail-pass evidence rule (`_validate_rail_pass_evidence` at
`validation.py:806-823`). `compile_telemetry_readiness` (`validation.py:114-121`) projects the R16
failure surface from the report. Findings are sorted deterministically by code, path, and detail
(`_report` at `validation.py:124-134`) and every finding is a typed
`CertificationContractFinding` (`_finding` at `validation.py:842-853`).

### Conventions

Validation is exhaustive and never raises: invalidity is a typed finding, never an exception or a
silent repair.

### Invariants And Boundaries

- Missing, duplicate, out-of-order, cross-identity, cardinality-invalid, or result-inconsistent
  events make readiness red.
- A passing rail-terminal must carry its own bounded evidence; the validator never derives a rail
  pass from telemetry alone.
- Diagnostic-run envelopes accept only diagnostic and control events and can never promote gate,
  certificate, delivery, approval, or finalization authority.
- Readiness is green exactly when no findings exist; a red report always carries its findings.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose normative requirement and exhaustive event
matrix define the cardinality and zero-start rules this validator enforces. Task artifact paths
are not repo-relative citations, so this fact is recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One ordered stream is validated exhaustively without raising. | `validate_execution_telemetry` | mcp/src/agents_remember/certification/telemetry/validation.py:86-107 |
| Typed telemetry readiness; a failure is itself typed and never a rail pass. | "class TelemetryReadiness" | mcp/src/agents_remember/certification/telemetry/validation.py:68-79 |
| Project the R16 failure surface: readiness red on any telemetry invalidity. | "def compile_telemetry_readiness" | mcp/src/agents_remember/certification/telemetry/validation.py:110-117 |
| Stream validation checks exact event identity, envelope and sequence consistency. | "def _validate_stream_identity" | mcp/src/agents_remember/certification/telemetry/validation.py:133-174 |
| Rail event matching verifies the declared gate and rail identity. | "def _validate_rail_matching" | mcp/src/agents_remember/certification/telemetry/validation.py:214-227 |
| Rail-pass telemetry requires corresponding passing evidence. | "def _validate_rail_pass_evidence" | mcp/src/agents_remember/certification/telemetry/validation.py:802-817 |
| Catalog telemetry validates the selected population and decision events. | "def _validate_catalogs" | mcp/src/agents_remember/certification/telemetry/validation.py:331-358 |
| Catalog citations must bind their declared decision evidence. | "def _validate_catalog_citations" | mcp/src/agents_remember/certification/telemetry/validation.py:485-492 |
| Finalization telemetry validates finalization event authority. | "def _validate_finalization" | mcp/src/agents_remember/certification/telemetry/validation.py:758-799 |
| Telemetry validation returns deterministically ordered typed findings. | "def _report" | mcp/src/agents_remember/certification/telemetry/validation.py:120-130 |
| Telemetry validation constructs typed contract findings. | "def _finding" | mcp/src/agents_remember/certification/telemetry/validation.py:838-841 |
| The validated vocabulary comes from the models layer. | `TelemetryEvent`; `EVENT_MATRIX` | mcp/src/agents_remember/certification/telemetry/models.py:673-851; mcp/src/agents_remember/certification/telemetry/models.py:160-185 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `validate_execution_telemetry` repointed to mcp/src/agents_remember/certification/telemetry/validation.py:86-107. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: created for the CCR-R16@v3 exhaustive stream
  validator and telemetry readiness (leaf 260831-CCR-L16, certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`). Verification stamp advanced to the certified code
  commit.
