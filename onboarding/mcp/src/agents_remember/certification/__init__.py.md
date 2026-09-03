# mcp/src/agents_remember/certification/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3`|
| lastVerifiedCommitDate | 2026-09-03T00:47:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Defines the deliberately small public facade for repository-neutral five-gate certification
contracts. Consumers enter through canonicalization, validation, plan admission/compilation,
terminal result construction/publication, and — since CCR-R05@v3 — the exact-candidate lifecycle
admission, prior-red corrective, certificate-recovery, and durable finalization boundaries,
without depending on package-private helpers.

## Code Commentary

### Logic

The module re-exports the supported certification and lifecycle orchestration functions and fixes
that public set in `__all__` (`__init__.py:45-71`). L05 widened the facade:
`lifecycle_admission` contributes `compile_lifecycle_admission` and
`validate_lifecycle_admission_currentness` (`__init__.py:18-21`), while `lifecycle_recovery`
contributes `authorize_finalization_leg`, `compile_certification_recovery_record`,
`compile_lifecycle_finalization`, and `validate_lifecycle_finalization_currentness`
(`__init__.py:22-27`). Models remain available from their owning module so this facade does not
become a second contract catalog.

### Conventions

The facade exposes composition operations, not repository rail declarations or an executor.

### Invariants And Boundaries

- Public entry points stay repository-neutral and preserve the five-gate contract and the R05
  admission/finalization boundaries (admission and finalization are lifecycle boundaries, not
  certification gates).
- This module does not select a repository profile, execute a rail, or invent fallback behavior.
- Package-private normalization, budget, and digest helpers are not promoted through the facade.

### Todos

Execution and concrete repository-profile wiring are owned by later consumers, not this facade.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts
below are the authoritative documentary sources used to close the informational gap for this
change's scope (exact-candidate admission and recovery).

| Finding | Anchor | Source |
| --- | --- | --- |
| CCR-R05@v3 defines admission and finalization as lifecycle boundaries with zero gate starts; the facade exposes those boundaries. | "Admission and finalization are lifecycle boundaries, not certification gates." | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R05-v3-exact-candidate-admission-and-recovery.md |
| Leaf L05 landed this exact-candidate surface at commit 4e0ea4b3c493. | "Commit 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/05_exact-candidate-admission-and-recovery.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade imports and re-exports the L05 lifecycle admission boundary. | `from agents_remember.certification.lifecycle_admission import (...)` | mcp/src/agents_remember/certification/__init__.py:18-21 |
| The facade imports and re-exports the L05 recovery and finalization boundary. | `from agents_remember.certification.lifecycle_recovery import (...)` | mcp/src/agents_remember/certification/__init__.py:22-27 |
| `__all__` fixes the complete public surface, including the six new L05 functions. | `__all__` | mcp/src/agents_remember/certification/__init__.py:45-71 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository-specific declarations enter through profiles outside this facade. | — | — |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): facade widened to export the exact-candidate lifecycle admission and recovery/finalization contracts (`compile_lifecycle_admission`, `validate_lifecycle_admission_currentness`, `authorize_finalization_leg`, `compile_certification_recovery_record`, `compile_lifecycle_finalization`, `validate_lifecycle_finalization_currentness`); body updated, verification metadata rebased from `0506b57a` to the L05 owning commit.

- 2026-09-01T03:11+02:00 — Created for the public certification-contract facade. Verification
  remains closeout-owned until the source candidate is committed.
