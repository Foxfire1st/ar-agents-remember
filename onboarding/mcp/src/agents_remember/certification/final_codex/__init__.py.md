# mcp/src/agents_remember/certification/final_codex/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/final_codex/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Package facade for the CCR-R14 final real-Codex Gate-4 certification lane delivered by leaf 260831-CCR-L14 (code commit 54ff803a). The lane runs exactly two fresh independent no-retry certifying repetitions of the exact candidate's canonical scenario rails once the exact candidate's R12 Gates 1-3 are green, and only a complete two-fresh-pass run can publish one bound Gate-4 certificate. This facade re-exports the closed final-codex vocabulary and helpers from the subpackage: the immutable two-fresh repetition models (models.py), the plan-record compiler and exact-predecessor barriers (planning.py), the lane-readiness projection (projection.py), the durable CAS run store (store.py), and the bound Gate-4 certificate compiler (certificate.py). Run control that binds the exact R12 host runner/store authority intentionally lives at the higher worktree quality layer (agents_remember.worktrees.modules.quality.final_codex_executor), which consumes these contracts through the trusted R12 launcher.

## Code Commentary

### Logic

The module re-exports the full public subpackage surface and fixes it in `__all__` (final_codex/__init__.py:52-81). The imports and `__all__` sets are identical in membership: the certificate compiler (final_codex/__init__.py:13-17), the closed models (final_codex/__init__.py:18-35), the planning helpers (final_codex/__init__.py:36-40), the projection helpers (final_codex/__init__.py:41-46), and the durable store (final_codex/__init__.py:47-50). Every symbol exported here is also exported through the outer certification facade (certification/__init__.py:38-67), so consumers can reach the lane vocabulary from either boundary without importing package-private helpers.

### Conventions

Exports follow the certification-domain frozen-model style: models are repository-neutral closed contracts, and no execution, authority admission, runner selection, or provisioning behavior is exposed from this package.

### Invariants And Boundaries

- This package owns the closed two-fresh repetition models, the plan record, the lane readiness projection, the CAS run store, and the bound Gate-4 certificate compiler only.
- Run control that freezes the R12 host runner/store authority is deliberately absent here and lives in worktrees.modules.quality.final_codex_executor.
- Nothing exported by this facade can weaken the two-fresh rule: a repetition slot is a first fresh run or does not exist, retryCount is a fixed zero literal, and diagnostic evidence has no shape that can enter this lane.

### Todos

None.

## Docs References

The approved CCR-R14@v3 requirement packet and the leaf doc 14_final-real-codex-certification govern this lane; task-artifact paths are not repo-relative citations, so the packet clauses are recorded as prose here and in the leaf Update History.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package re-exports the full final-codex contract surface for the two-fresh no-retry certifying lane. | `__all__` | mcp/src/agents_remember/certification/final_codex/__init__.py:52-81 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closed two-fresh repetition models (attempt, run manifest, repetition results/drafts, failure, teardown, plan record, authority and environment bindings, fresh repetition identity). | `final_codex.models` | mcp/src/agents_remember/certification/final_codex/models.py:66-471 |
| Plan-record compilation and the exact Gate-1..3 must-not-run barriers. | `compile_final_codex_plan_record`; `final_codex_gate_plan`; `require_gates_one_to_three_green` | mcp/src/agents_remember/certification/final_codex/planning.py:45-131; mcp/src/agents_remember/certification/final_codex/planning.py:134-191; mcp/src/agents_remember/certification/final_codex/planning.py:194-256 |
| Lane-readiness projection (not-started, running, two-fresh-pass, red, stale). | `project_final_codex_lane`; `final_codex_certificate_ready` | mcp/src/agents_remember/certification/final_codex/projection.py:88-113; mcp/src/agents_remember/certification/final_codex/projection.py:116-125 |
| Durable isolated candidate run store with atomic CAS publication and retry-disabled reservation. | `FinalCodexManifestStore` | mcp/src/agents_remember/certification/final_codex/store.py:62-274 |
| Bound Gate-4 certificate compilation binding the exact ordered Gate-1..3 predecessor identities and both fresh results. | `compile_gate_four_certificate` | mcp/src/agents_remember/certification/final_codex/certificate.py:117-204 |
| The R14-run-controlled executor consumes these contracts through the trusted authority launcher. | `final_codex_executor` | mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py:179-600 |
| The outer certification facade re-exports the same final-codex surface. | `final_codex` | mcp/src/agents_remember/certification/__init__.py:38-67; mcp/src/agents_remember/certification/__init__.py:154-277 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lane is repository-neutral and binds the frozen R12 host runner/store snapshot through the trusted launcher, never a repository-selected engine. | `FinalCodexRuntimeAuthorityBinding` | mcp/src/agents_remember/certification/final_codex/models.py:116-139 |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new CCR-R14 final real-Codex Gate-4 certification package facade delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
