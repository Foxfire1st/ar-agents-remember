# mcp/src/agents_remember/certification/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Defines the deliberately small public facade for repository-neutral five-gate certification contracts. Consumers enter through canonicalization, validation, plan admission/compilation, terminal result construction/publication, and - since CCR-R05@v3 - the exact-candidate lifecycle admission, prior-red corrective, certificate-recovery, and durable finalization boundaries, without depending on package-private helpers. CCR-R13@v2 widened the facade with the optional non-certifying diagnostic lane surface, CCR-R16@v3 widened it with the durable boundary/gate/rail telemetry surface, and CCR-R17 (260831-CCR-L17) widened it with the measured-replay and reduction surface (freeze/population identity, comparability, span analysis, measured-run reduction, the seventeen acceptance scenarios, and the pair comparison report).

## Code Commentary

### Logic

The module re-exports the supported certification, lifecycle, diagnostic, telemetry, and replay surfaces and fixes the complete public set in `__all__` (`__init__.py:157-283`). Import blocks in the verified file: canonical and certificate owners (lines 3-17), the R13 diagnostic lane (lines 18-37), the R05 lifecycle admission boundary (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, lines 38-41) and recovery/finalization boundary (`authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`, lines 42-47), planning and readiness surfaces (lines 48-71), the CCR-R17 replay block (lines 72-104, re-exporting `REPLAY_ACCEPTANCE_SCENARIOS`, freeze/population records and compilers, comparability, span analysis, measured-run reduction, scenario evaluators, and the comparison report), repository-profile owners (lines 105-111), results owners (lines 112-115), and the CCR-R16 telemetry surface (lines 116-154). Models remain available from their owning module so this facade does not become a second contract catalog.

### Conventions

The facade exposes composition operations and typed contracts, not repository rail declarations, an executor, or store implementations.

### Invariants And Boundaries

- Public entry points stay repository-neutral and preserve the five-gate contract, the R05 admission/finalization boundaries (admission and finalization are lifecycle boundaries, not certification gates), the R13 structural non-certifying diagnostic separation, and the R16 durable telemetry vocabulary.
- The R17 replay surface carries raw measurements only: numeric reduction thresholds are deliberately absent from the facade and its records.
- This module does not select a repository profile, execute a rail, admit runtime authority, or invent fallback behavior.
- Package-private normalization, budget, and digest helpers are not promoted through the facade.

### Todos

Execution and concrete repository-profile wiring are owned by later consumers, not this facade.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts below are the authoritative documentary sources used to close the informational gap for this change's scope (the CCR-R17 measured-replay protocol, alongside the R05 admission/recovery, R13 diagnostic-lane, and R16 telemetry packets).

The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define the measured-replay clause scope that this facade exposes; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade imports the R13 diagnostic lane surface from the diagnostics package. | `diagnostics` | mcp/src/agents_remember/certification/__init__.py:18-37 |
| The facade imports the R05 lifecycle admission boundary from its owning module. | `lifecycle_admission` | mcp/src/agents_remember/certification/__init__.py:38-41 |
| The facade imports the R05 recovery and finalization boundary from its owning module. | `lifecycle_recovery` | mcp/src/agents_remember/certification/__init__.py:42-47 |
| The facade imports the CCR-R17 measured-replay surface from the replay subpackage. | `replay` | mcp/src/agents_remember/certification/__init__.py:72-104 |
| The facade imports the R16 durable telemetry surface from the telemetry subpackage. | `telemetry` | mcp/src/agents_remember/certification/__init__.py:116-154 |
| `__all__` fixes the complete public surface, including the L17 replay exports. | `__all__` | mcp/src/agents_remember/certification/__init__.py:157-283 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository-specific declarations enter through profiles outside this facade. | - | - |

## Update History

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: re-anchored the facade rows to the verified current source (imports at lines 3-154 with the R17 replay block at 72-104 and `__all__` at 157-283) and recorded the CCR-R17 measured-replay facade exports (freeze/population identity, comparability, span analysis, measured-run reduction, seventeen scenarios, and the pair comparison report). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): re-anchored the two lifecycle import rows to the owning-module identifiers (`lifecycle_admission`, `lifecycle_recovery`) so each anchor resolves once in the facade, and widened the `__all__` row to its current extent. Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the two lifecycle import rows to identifier anchors present inside their cited ranges, and rewrote the Docs References task-artifact rows as prose (absolute ar-coordination paths are not repo-relative citations and carried no range). Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 - 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): facade widened to export the exact-candidate lifecycle admission and recovery/finalization contracts (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, `authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`); body updated, verification metadata rebased from `0506b57a` to the L05 owning commit.

- 2026-09-01T03:11+02:00 - Created for the public certification-contract facade. Verification remains closeout-owned until the source candidate is committed.
