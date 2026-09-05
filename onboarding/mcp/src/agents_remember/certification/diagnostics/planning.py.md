# mcp/src/agents_remember/certification/diagnostics/planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/diagnostics/planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T07:08:26+00:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Compiles the exact diagnostic-altitude plan for the CCR-R13 optional non-certifying diagnostic E2E lane (leaf 260831-CCR-L13, code commit 4ba18bb2). A diagnostic is one optional replication of the exact canonical scenario catalog the certifying profile would run, compiled at diagnostic altitude: CCR-R13 forbids a second scenario implementation, so the compiled diagnostic rails for the scenario gate must equal the certifying plan's gate rails in identity, posture, and applicability, exactly as the R09 readiness compiler re-checks them.

## Code Commentary

### Logic

- `compile_diagnostic_plan` (lines 30-96) is the single admission/compilation entry: it validates the registry (lines 46-48), refuses an unknown profile (`diagnostic-profile-unknown`, via `_selected_profile` lines 123-139) or a non-diagnostic-altitude profile (`diagnostic-profile-kind-mismatch`, lines 50-60), refuses a scenario gate the profile does not plan over the complete earlier-gate prefix (`diagnostic-scenario-gate-unplanned`, lines 61-74), and requires a certifying plan that itself plans the scenario gate (`diagnostic-certifying-plan-missing`, lines 75-87). It then compiles the diagnostic-altitude plan through the shared plan compiler (lines 88-92) and proves the scenario rail catalog is identical to the certifying gate plan (`_require_canonical_scenario_catalog`, lines 142-162; `diagnostic-scenario-rail-mismatch`), so diagnostics can only replicate the exact canonical scenario rails.
- `diagnostic_scenario_gate` (lines 99-114) selects the exact scenario gate plan, refusing zero or multiple matches (`diagnostic-gate-absent`).
- `scenario_gate_digest` (lines 117-120) returns the immutable digest of the planned scenario gate catalog (`gatePlan.planDigest`).
- Rail-contract comparison helpers (lines 165-190) sort the catalog deterministically by orderKey/identity/version/definitionDigest and compare each rail's identity key, posture, and applicability status, so drift in any of those semantics is a typed refusal.
- `_raise_contract_error` (lines 193-200) raises `CertificationContractError` carrying serialized `RegistryValidationFinding` payloads.

### Conventions

All refusals raise typed `CertificationContractError` with finding code/path/detail. The diagnostic plan is compiled from the canonical registry through the shared `compile_certification_plan`; there is no second scenario implementation.

### Invariants And Boundaries

- The selected profile must be diagnostic altitude and must plan the exact complete earlier-gate prefix through the scenario gate.
- A diagnostic requires the exact certifying plan for the candidate, and the scenario gate must exist in it.
- The diagnostic gate catalog must match the certifying gate catalog in rail identity, posture, and applicability - nothing else is a valid diagnostic replication.
- This module projects plans only; it never executes rails or admits runtime authority.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. The CCR-R13@v2 packet clauses (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) and the leaf doc 13_non-certifying-diagnostic-e2e.md carry the one-canonical-scenario rule; task artifact paths are not repo-relative citations, so they are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The diagnostic catalog may only replicate the exact canonical scenario rails at diagnostic altitude. | `_require_canonical_scenario_catalog` | mcp/src/agents_remember/certification/diagnostics/planning.py:142-162 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared certification plan compiler builds the altitude plan. | `compile_certification_plan` | mcp/src/agents_remember/certification/planning.py:1-160 |
| Registry validation gates admission before any plan is compiled. | `validate_registry` | mcp/src/agents_remember/certification/validation.py:1-120 |
| The run controller consumes the compiled plan to build its run spec and plan record. | `build_diagnostic_run_spec` | mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:575-617 |
| The diagnostics package imports these three planning helpers. | "from agents_remember.certification.diagnostics.planning import (" | mcp/src/agents_remember/certification/diagnostics/__init__.py:26-30 |
| The diagnostics package lists these planning helpers in its public exports. | `__all__` | mcp/src/agents_remember/certification/diagnostics/__init__.py:43-67 |
| The outer certification facade re-exports these planning helpers. | "from agents_remember.certification.diagnostics import (" | mcp/src/agents_remember/certification/__init__.py:18-37 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The altitude rules stay repository-neutral and rely only on registry/profile/certifying-plan inputs. | `compile_diagnostic_plan` | mcp/src/agents_remember/certification/diagnostics/planning.py:30-96 |

## Update History

- 2026-09-05T07:08:26+00:00 — L31 final residual curation against frozen code `ea35964985f30080488270e71ac81657ac40682b`: Split the two-facade claim into exact import and export constructs in one source file per row; public planning-helper ownership unchanged. This scoped repair does not promote the card's verification stamp or certify a gate.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new CCR-R13@v2 diagnostic-altitude plan projection delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
