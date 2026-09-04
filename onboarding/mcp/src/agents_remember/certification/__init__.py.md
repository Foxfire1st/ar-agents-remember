# mcp/src/agents_remember/certification/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Defines the deliberately small public facade for repository-neutral five-gate certification contracts. Consumers enter through canonicalization, validation, plan admission/compilation, terminal result construction/publication, and - since CCR-R05@v3 - the exact-candidate lifecycle admission, prior-red corrective, certificate-recovery, and durable finalization boundaries, without depending on package-private helpers. CCR-R13@v2 widened the facade with the optional non-certifying diagnostic lane surface, and CCR-R14@v3 (260831-CCR-L14) widened it further with the final real-Codex Gate-4 two-fresh-no-retry certifying lane surface (closed models, plan record, lane projection, durable CAS store, and the bound Gate-4 certificate compiler).

## Code Commentary

### Logic

The module re-exports the supported certification, lifecycle, diagnostic, and final-codex surfaces and fixes the complete public set in `__all__` (`__init__.py:154-277`). Import blocks in the verified file: canonical and certificate owners (lines 3-17), the R13 diagnostic lane (lines 18-37), the CCR-R14 final-codex lane (lines 38-67, re-exporting `CERTIFYING_GATE`, `REPETITION_COUNT`, the closed attempt/run/repetition/plan/failure/teardown/authority/environment/artifact models, `FinalCodexLaneProjection`/`FinalCodexLaneDisposition`, `FinalCodexManifestStore`/`FinalCodexStorePolicy`, `FinalCodexGateFourCertificate`/`FinalCodexCertificateEnvelope`, and `compile_final_codex_plan_record`, `compile_gate_four_certificate`, `final_codex_certificate_ready`, `final_codex_gate_plan`, `project_final_codex_lane`, `require_gates_one_to_three_green`), the R05 lifecycle admission boundary (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, lines 68-71) and recovery/finalization boundary (`authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`, lines 72-77), planning and readiness surfaces (lines 78-101), repository-profile owners (lines 102-108), results owners (lines 109-112), and the R16 durable telemetry surface (lines 113-151). Models remain available from their owning module so this facade does not become a second contract catalog.

### Conventions

The facade exposes composition operations and typed contracts, not repository rail declarations, an executor, or store implementations.

### Invariants And Boundaries

- Public entry points stay repository-neutral and preserve the five-gate contract, the R05 admission/finalization boundaries (admission and finalization are lifecycle boundaries, not certification gates), the R13 structural non-certifying diagnostic separation, and the R14 final real-codex two-fresh semantics.
- The R14 final-codex surface is structural: results carry acceptanceEligible/certifying=true and retryCount zero, and retry is disabled; one passing repetition can never compensate the other.
- This module does not select a repository profile, execute a rail, admit runtime authority, or invent fallback behavior.
- Package-private normalization, budget, and digest helpers are not promoted through the facade.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts below are the authoritative documentary sources used to close the informational gap for this change's scope (the CCR-R14@v3 final real-codex requirement packet, alongside the R05 admission/recovery, R13 diagnostic-lane, and R16 telemetry packets).

| Finding | Anchor | Source |
| --- | --- | --- |
| The CCR-R14@v3 requirement packet and the 14_final-real-codex-certification leaf doc govern the two-fresh certifying lane surface this facade exposes. | `final_codex` import block; `__all__` | mcp/src/agents_remember/certification/__init__.py:38-67; mcp/src/agents_remember/certification/__init__.py:154-277 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade imports the R13 diagnostic lane surface from the diagnostics package. | `diagnostics` | mcp/src/agents_remember/certification/__init__.py:18-37 |
| The facade imports the CCR-R14 final-codex lane surface from the final_codex package. | `final_codex` | mcp/src/agents_remember/certification/__init__.py:38-67 |
| The facade imports the R05 lifecycle admission boundary from its owning module. | `lifecycle_admission` | mcp/src/agents_remember/certification/__init__.py:68-71 |
| The facade imports the R05 recovery and finalization boundary from its owning module. | `lifecycle_recovery` | mcp/src/agents_remember/certification/__init__.py:72-77 |
| The facade imports the R16 durable telemetry surface from the telemetry subpackage. | `telemetry` | mcp/src/agents_remember/certification/__init__.py:113-151 |
| `__all__` fixes the complete public surface, including the L14 final-codex exports. | `__all__` | mcp/src/agents_remember/certification/__init__.py:154-277 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository-specific declarations enter through profiles outside this facade. | - | - |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: re-anchored the facade rows to the verified current source (imports at lines 3-151 with the CCR-R14 final-codex block at 38-67 and `__all__` at 154-277) and recorded the CCR-R14 two-fresh final-codex facade exports (closed models, plan record, lane projection, CAS store, and bound Gate-4 certificate compiler). Verification stamp is the full leaf code commit `54ff803a05209e06f732f2de1f90e2a71a069e08` (tree `aff2e268968397ab8db042a782652957a3600dda`).

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): re-anchored the two lifecycle import rows to the owning-module identifiers (`lifecycle_admission`, `lifecycle_recovery`) so each anchor resolves once in the facade, and widened the `__all__` row to its current extent. Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the two lifecycle import rows to identifier anchors present inside their cited ranges, and rewrote the Docs References task-artifact rows as prose (absolute ar-coordination paths are not repo-relative citations and carried no range). Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 - 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): facade widened to export the exact-candidate lifecycle admission and recovery/finalization contracts (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, `authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`); body updated, verification metadata rebased from `0506b57a` to the L05 owning commit.

- 2026-09-01T03:11+02:00 - Created for the public certification-contract facade. Verification remains closeout-owned until the source candidate is committed.
