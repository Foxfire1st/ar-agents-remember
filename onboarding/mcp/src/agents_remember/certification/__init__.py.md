# mcp/src/agents_remember/certification/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Defines the deliberately small public facade for repository-neutral five-gate certification contracts. Consumers enter through canonicalization, validation, plan admission/compilation, terminal result construction/publication, and — since CCR-R05@v3 — the exact-candidate lifecycle admission, prior-red corrective, certificate-recovery, and durable finalization boundaries. CCR-R13@v2 (260831-CCR-L13) widened the facade to re-export the optional non-certifying diagnostic lane surface (records, plan projection, lane projection, and store), and the readiness/telemetry surfaces remain available through their owning modules.

## Code Commentary

### Logic

The module re-exports the supported certification and lifecycle orchestration functions and fixes that public set in `__all__` (`__init__.py:124-219`). L05 widened the facade with the lifecycle admission boundary (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, lines 38-41) and the recovery/finalization boundary (`authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`, lines 42-47). CCR-R13@v2 added the diagnostics import block (`__init__.py:18-37`) re-exporting `DiagnosticArtifact`, `DiagnosticAttemptRecord`, `DiagnosticDisposition`, `DiagnosticLaneProjection`, `DiagnosticManifestStore`, `DiagnosticPlanRecord`, `DiagnosticRunManifest`, `DiagnosticRunResult`, `DiagnosticRunResultDraft`, `DiagnosticRuntimeAuthorityBinding`, `DiagnosticStorePolicy`, `DiagnosticTeardownRecord`, `compile_diagnostic_plan`, `diagnostic_blocks_certification`, `diagnostic_never_satisfies_certification`, `diagnostic_scenario_gate`, `project_diagnostic_lane`, and `scenario_gate_digest`, with the matching `__all__` entries (`__init__.py:130-142`, `175`, `199-201`, `205`, `210`). Models remain available from their owning module so this facade does not become a second contract catalog.

### Conventions

The facade exposes composition operations, not repository rail declarations or an executor.

### Invariants And Boundaries

- Public entry points stay repository-neutral and preserve the five-gate contract and the R05 admission/finalization boundaries (admission and finalization are lifecycle boundaries, not certification gates).
- The R13 diagnostic surface is structural: results carry acceptanceEligible/certifying=false and cannot be promoted into accepted or certifying state.
- This module does not select a repository profile, execute a rail, admit runtime authority, or invent fallback behavior.
- Package-private normalization, budget, and digest helpers are not promoted through the facade.

### Todos

Execution and concrete repository-profile wiring are owned by later consumers, not this facade.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts below are the authoritative documentary sources used to close the informational gap for this change's scope (exact-candidate admission/recovery and the CCR-R13@v2 diagnostic lane).

The governing task artifacts (CCR-R05@v3 requirement packet and the 05_exact-candidate-admission-and-recovery leaf doc; CCR-R13@v2 packet frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a and the 13_non-certifying-diagnostic-e2e leaf doc) define admission/finalization as lifecycle boundaries and the diagnostic lane as one optional non-certifying replication. Task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade imports the L05 lifecycle admission boundary from its owning module. | `lifecycle_admission` | mcp/src/agents_remember/certification/__init__.py:38-41 |
| The facade imports the L05 recovery and finalization boundary from its owning module. | `lifecycle_recovery` | mcp/src/agents_remember/certification/__init__.py:42-47 |
| The facade imports the CCR-R13 diagnostic lane surface from the diagnostics package. | `diagnostics` | mcp/src/agents_remember/certification/__init__.py:18-37 |
| `__all__` fixes the complete public surface, including the L05 lifecycle functions and the R13 diagnostic exports. | `__all__` | mcp/src/agents_remember/certification/__init__.py:124-219 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository-specific declarations enter through profiles outside this facade. | — | — |

## Update History

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: re-anchored the import/facade rows to the current source (imports at lines 18-47, __all__ at 124-219) and recorded the CCR-R13@v2 diagnostics facade exports (records, plan/lane projection, and store helpers). Verification stamp is the full leaf code commit 4ba18bb23ba90e201bb37341d61c0efc64161fcf (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): re-anchored the two lifecycle import rows to the owning-module identifiers (`lifecycle_admission`, `lifecycle_recovery`) so each anchor resolves once in the facade, and widened the `__all__` row to its current extent. Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the two lifecycle import rows to identifier anchors present inside their cited ranges, and rewrote the Docs References task-artifact rows as prose (absolute ar-coordination paths are not repo-relative citations and carried no range). Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): facade widened to export the exact-candidate lifecycle admission and recovery/finalization contracts (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, `authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`); body updated, verification metadata rebased from `0506b57a` to the L05 owning commit.

- 2026-09-01T03:11+02:00 — Created for the public certification-contract facade. Verification remains closeout-owned until the source candidate is committed.
