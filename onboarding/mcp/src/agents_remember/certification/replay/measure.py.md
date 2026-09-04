# mcp/src/agents_remember/certification/replay/measure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/replay/measure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Owns the CCR-R17 (leaf 260831-CCR-L17) deterministic measured-run reduction: `measure_replay_run` folds one ordered R16 closeout telemetry export into the closed `RunMeasurement` record (per-gate start and zero-start evidence, last complete gate catalog and decision, rail census, certificate publication/reuse/invalidation counts, finalization evidence, and the whole-run per-category span reduction). The reducer never classifies a stream or certifies a gate; it only measures what the export records, so a measurement can never promote diagnostic or partial evidence.

## Code Commentary

### Logic

The fold is a single pass over an ordered event sequence:

- `measure_replay_run` (lines 53-86) refuses an empty export and any export whose execution kind is not closeout-generation, seeds one `GateRunMeasurement` per gate 1-5 inside `_MeasurementState` (lines 34-50), folds every event, reduces the collected spans, and returns a digest-verified `RunMeasurement`.
- `_fold_event` (lines 89-101) dispatches each event: span-bearing events accumulate into the span list, flag kinds toggle admission/finalization state, an operation-terminal event records its terminal result class, and gate-bound kinds route through `_GATE_FOLDERS` after requiring the exact gate identity.
- Flag kinds (`_FLAG_KINDS`, lines 104-112) map candidate-admitted / admission-refused / finalization-started / finalization-boundary-resumed / finalization-completed onto `_MeasurementState` booleans via `_FLAG_ATTRS` (lines 114-121) and `_apply_flag` (lines 123-124).
- Per-gate folders (lines 127-222) count starts and rail starts/terminals (`_fold_started`, `_fold_rail_started`, `_fold_rail_terminal`), capture the last complete catalog and its disposition/counts (`_fold_catalog`), record pass-published vs pass-reused decisions with publish/reuse counters (`_fold_pass`), and set fail / certificate-refused / blocked (with zero-start evidence) / invalidated decisions. The `_GATE_FOLDERS` dispatch table (lines 225-235) binds each event kind to its folder.
- `_replace` (lines 238-240) copies a gate measurement with validated updates; `_required_gate` (lines 243-250) refuses gate events that omit the exact gate identity.

### Conventions

Mutable fold state lives only in the module-private `_MeasurementState` and never escapes; each produced record revalidates its full shape through `RunMeasurement.model_validate` before returning.

### Invariants And Boundaries

- A measurement is evidence-only: it never classifies a stream or certifies a gate.
- Zero-start evidence can accompany only a gate that never started; a blocked gate never started.
- The reducer requires at least one event and refuses any non-closeout-generation export.
- The result always carries the exact ordered Gates 1-5 and a digest-verified span reduction.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define that a measurement folds the R16 closeout export only; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| A measured replay consumes closeout-generation exports only, and never a diagnostic envelope. | `measure_replay_run` | mcp/src/agents_remember/certification/replay/measure.py:53-86 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reducer consumes the R16 telemetry event vocabulary and catalog payloads. | `TelemetryEvent`; `GateCatalogCompletePayload`; `GatePassPayload` | mcp/src/agents_remember/certification/telemetry/models.py |
| The reducer produces the measured vocabulary records defined in the replay models module. | `RunMeasurement`; `GateRunMeasurement`; `ReplayLegIdentity` | mcp/src/agents_remember/certification/replay/models.py:255-286; mcp/src/agents_remember/certification/replay/models.py:196-252 |
| The span reduction is delegated to the deterministic span analyzer. | `analyze_span_categories` | mcp/src/agents_remember/certification/replay/spans.py:39-72 |
| Refusal raises the shared certification contract error. | `CertificationContractError` | mcp/src/agents_remember/errors.py:22-31 |
| The public subpackage facade re-exports the reducer. | `replay.__all__` | mcp/src/agents_remember/certification/replay/__init__.py:56-88 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Measurement stays repository-neutral and consumes only the shared telemetry vocabulary. | - | - |

## Update History

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created this card for the new CCR-R17 measured-run reducer delivered in code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
