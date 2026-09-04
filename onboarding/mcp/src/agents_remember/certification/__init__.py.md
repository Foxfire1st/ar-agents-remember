# mcp/src/agents_remember/certification/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T12:30:00+02:00 |
| lastVerifiedCommitHash | `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb` |
| lastVerifiedCommitDate | 2026-09-04T12:20:39+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Defines the deliberately small public facade for repository-neutral five-gate certification
contracts. Consumers enter through canonicalization, validation, plan admission/compilation,
terminal result construction/publication, the exact-candidate lifecycle admission, prior-red
corrective, certificate-recovery, and durable finalization boundaries (since CCR-R05@v3), and -
since CCR-R16@v3 (leaf 260831-CCR-L16) - the durable boundary, gate, and rail telemetry surface,
without depending on package-private helpers.

## Code Commentary

### Logic

The module re-exports the supported certification, lifecycle orchestration, and telemetry
functions and fixes that public set in `__all__` (`__init__.py:104-181`). L05 widened the facade:
`lifecycle_admission` contributes `compile_lifecycle_admission` and
`validate_lifecycle_admission_currentness` (`__init__.py:18-21`), while `lifecycle_recovery`
contributes `authorize_finalization_leg`, `compile_certification_recovery_record`,
`compile_lifecycle_finalization`, and `validate_lifecycle_finalization_currentness`
(`__init__.py:22-27`). CCR-R16@v3 widened the facade a second time: the telemetry import
block (`__init__.py:63-101`) brings in the complete durable telemetry surface from
`agents_remember.certification.telemetry` - the ten telemetry models
(`DurableTelemetryStore`, `TelemetryEvent`, `TelemetryExecutionContext`,
`TelemetryJournalEntry`, `TelemetryProjection`, `TelemetryReadiness`,
`TelemetryReplay`, `TelemetrySpan`, `TelemetryStorePolicy`,
`TelemetryValidationReport`), the twenty event-compile adapters plus `span` and
`aggregate_span_totals`, and the two projections `project_execution_telemetry` and
`project_gate_history` with the readiness surface `compile_telemetry_readiness` and
`validate_execution_telemetry`; all of these names appear in `__all__`
(`__init__.py:111-125`, `__init__.py:128`, `__init__.py:134-138`, `__init__.py:143-150`,
`__init__.py:160-165`, `__init__.py:169-170`, `__init__.py:173`, `__init__.py:175`).
Models remain available from their owning module so this facade does not become a second contract
catalog.

### Conventions

The facade exposes composition operations and typed contracts, not repository rail declarations,
an executor, or store implementations.

### Invariants And Boundaries

- Public entry points stay repository-neutral and preserve the five-gate contract, the R05
  admission/finalization boundaries (admission and finalization are lifecycle boundaries, not
  certification gates), and the R16 durable telemetry vocabulary.
- This module does not select a repository profile, execute a rail, publish journal entries, or
  invent fallback behavior.
- Package-private normalization, budget, digest, and store helpers are not promoted through the
  facade.

### Todos

Execution, concrete repository-profile wiring, and telemetry store lifecycle are owned by later
consumers, not this facade.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts
used to close the informational gap for this change scope (exact-candidate admission/recovery
plus durable gate and rail telemetry) are the CCR-R05@v3 and CCR-R16@v3 requirement packets and
the corresponding leaf task docs. Task artifact paths are not repo-relative citations, so these
facts are recorded as prose here: CCR-R05@v3 defines admission and finalization as lifecycle
boundaries with zero gate starts, which the facade exposes (leaf L05 landed that surface at
commit 4e0ea4b3c493); CCR-R16@v3 normatively requires the durable boundary/gate/rail stream that
the facade now re-exports (leaf 260831-CCR-L16 landed that surface at commit 2cd360d8).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade imports the L05 lifecycle admission boundary from its owning module. | `lifecycle_admission` | mcp/src/agents_remember/certification/__init__.py:18-21 |
| The facade imports the L05 recovery and finalization boundary from its owning module. | `lifecycle_recovery` | mcp/src/agents_remember/certification/__init__.py:22-27 |
| The facade imports the complete CCR-R16@v3 durable telemetry surface from its owning package. | `agents_remember.certification.telemetry` | mcp/src/agents_remember/certification/__init__.py:63-101 |
| `__all__` fixes the complete public surface, including the L05 lifecycle functions and the L16 telemetry models, adapters, and projections. | `__all__` | mcp/src/agents_remember/certification/__init__.py:104-181 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository-specific declarations enter through profiles outside this facade. | - | - |

## Update History

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5: facade widened to export the CCR-R16@v3
  durable gate and rail telemetry surface (telemetry import block plus `__all__` entries:
  ten telemetry models, twenty compile adapters, `span`, `aggregate_span_totals`,
  `project_execution_telemetry`, `project_gate_history`, `compile_telemetry_readiness`,
  `validate_execution_telemetry`); body and reference rows updated and re-anchored to
  the widened facade (import block `__init__.py:63-101`, `__all__` extent
  `__init__.py:104-181`). Verification stamp advanced to the certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): re-anchored the two lifecycle import rows to the owning-module identifiers (`lifecycle_admission`, `lifecycle_recovery`) so each anchor resolves once in the facade, and widened the `__all__` row to its current extent. Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the two lifecycle
  import rows to identifier anchors present inside their cited ranges, and rewrote the
  Docs References task-artifact rows as prose (absolute ar-coordination paths are not
  repo-relative citations and carried no range). Verification remains pinned to the pre-commit
  source history until closeout.

- 2026-09-03T12:30+02:00 - 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): facade widened to export the exact-candidate lifecycle admission and recovery/finalization contracts (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, `authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`); body updated, verification metadata rebased from `0506b57a` to the L05 owning commit.

- 2026-09-01T03:11+02:00 - Created for the public certification-contract facade. Verification
  remains closeout-owned until the source candidate is committed.
