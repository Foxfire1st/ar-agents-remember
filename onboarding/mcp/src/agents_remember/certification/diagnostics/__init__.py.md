# mcp/src/agents_remember/certification/diagnostics/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/diagnostics/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Package facade for the CCR-R13 optional non-certifying diagnostic E2E lane delivered by leaf 260831-CCR-L13 (code commit 4ba18bb2). The lane lets a developer or architect run at most one real-Codex replication of the canonical ARSPAWN scenario as explicitly non-certifying diagnostic evidence once the exact candidate's R12 Gates 1-3 are green. This facade re-exports the closed diagnostic vocabulary and helpers from the subpackage: the immutable result/attempt/manifest/plan record models (models.py), the diagnostic-altitude plan projection helpers (planning.py), the optional-lane readiness projection (projection.py), and the durable isolated manifest store (store.py). Run control that binds the R12 host runner/store authority intentionally lives at the higher worktree quality layer (agents_remember.worktrees.modules.quality.diagnostic_executor), which consumes these contracts through the trusted R12 launcher.

## Code Commentary

### Logic

The module re-exports the full public subpackage surface and fixes it in `__all__` (diagnostics/__init__.py:43-67). The imports and `__all__` sets are identical in membership: every diagnostic model, plan, projection, and store symbol exported here is also exported through the outer certification facade (certification/__init__.py), so consumers can reach the lane vocabulary from either boundary without importing package-private helpers.

### Conventions

Exports follow the certification-domain frozen-model style: models are repository-neutral closed contracts, and no execution, authority admission, runner selection, or provisioning behavior is exposed from this package.

### Invariants And Boundaries

- This package owns the durable diagnostic manifest, altitude plan projection, optional-lane readiness projection, and nonce/telemetry identity helpers only.
- Run control that freezes the R12 host runner/store authority is deliberately absent here and lives in worktrees.modules.quality.diagnostic_executor.
- Nothing exported by this facade can flip a diagnostic record into an accepted or certifying one: acceptanceEligible/certifying are structural false literals in the models.

### Todos

None.

## Docs References

The approved CCR-R13@v2 requirement packet (requirements/CCR-R13-v2-non-certifying-diagnostic-e2e.md, frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) and the leaf doc 13_non-certifying-diagnostic-e2e.md govern this lane; task-artifact paths are not repo-relative citations, so the packet clauses are recorded as prose here and in the leaf Update History.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package re-exports the full diagnostic contract surface for the one optional non-certifying lane. | `__all__` | mcp/src/agents_remember/certification/diagnostics/__init__.py:43-67 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closed diagnostic models (result, attempt, manifest, plan, failure, teardown, authority and environment bindings). | `DiagnosticDisposition`; `DiagnosticAttemptState`; `DiagnosticArtifact`; `DiagnosticFailureRecord`; `DiagnosticTeardownRecord`; `DiagnosticRuntimeAuthorityBinding`; `DiagnosticEnvironmentBinding`; `DiagnosticAttemptRecord`; `DiagnosticPlanRecord`; `DiagnosticRunResultDraft`; `DiagnosticRunResult`; `DiagnosticRunManifest` | mcp/src/agents_remember/certification/diagnostics/models.py:42-44; mcp/src/agents_remember/certification/diagnostics/models.py:66-205; mcp/src/agents_remember/certification/diagnostics/models.py:259-375 |
| Diagnostic-altitude plan projection from the canonical R11 scenario rails. | `compile_diagnostic_plan`; `diagnostic_scenario_gate` | mcp/src/agents_remember/certification/diagnostics/planning.py:30-96; mcp/src/agents_remember/certification/diagnostics/planning.py:99-114 |
| Optional-lane readiness projection (not-requested-optional, running, newest-terminal blocking). | `project_diagnostic_lane` | mcp/src/agents_remember/certification/diagnostics/projection.py:98-137 |
| Durable isolated candidate manifest store with CAS publication. | `DiagnosticManifestStore` | mcp/src/agents_remember/certification/diagnostics/store.py:53-288 |
| The R12-run-controlled executor consumes these contracts through the trusted authority launcher. | `DiagnosticExecutionEngine`; `admit`; `admit_dagger_authority` | mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:176-225; mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:321-329 |
| The outer certification facade re-exports the same diagnostic surface. | `diagnostics` | mcp/src/agents_remember/certification/__init__.py:18-37; mcp/src/agents_remember/certification/__init__.py:130-142 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Diagnostics are repository-neutral and bind the frozen R12 runtime authority snapshot, never a repository-selected engine. | `DiagnosticRuntimeAuthorityBinding` | mcp/src/agents_remember/certification/diagnostics/models.py:109-132 |

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `project_diagnostic_lane` repointed to mcp/src/agents_remember/certification/diagnostics/projection.py:98-137. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new CCR-R13@v2 optional non-certifying diagnostic E2E package facade delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
