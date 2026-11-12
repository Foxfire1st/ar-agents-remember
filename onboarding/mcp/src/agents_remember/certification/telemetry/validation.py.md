# mcp/src/agents_remember/certification/telemetry/validation.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root; the governing documentary
artifact is the CCR-R16@v3 requirement packet, whose normative requirement and exhaustive event
matrix define the cardinality and zero-start rules this validator enforces. Task artifact paths
are not repo-relative citations, so this fact is recorded as prose here.

### Repo-Internal References

- One ordered stream is validated exhaustively without raising. [1]
- Typed telemetry readiness; a failure is itself typed and never a rail pass. [2]
- Project the R16 failure surface: readiness red on any telemetry invalidity. [3]
- Stream validation checks exact event identity, envelope and sequence consistency. [4]
- Rail event matching verifies the declared gate and rail identity. [5]
- Rail-pass telemetry requires corresponding passing evidence. [6]
- Catalog telemetry validates the selected population and decision events. [7]
- Catalog citations must bind their declared decision evidence. [8]
- Finalization telemetry validates finalization event authority. [9]
- Telemetry validation returns deterministically ordered typed findings. [10]
- Telemetry validation constructs typed contract findings. [11]
- The validated vocabulary comes from the models layer. [12]

### Cross-Repo References

No cross-repository implementation boundary is owned here.
