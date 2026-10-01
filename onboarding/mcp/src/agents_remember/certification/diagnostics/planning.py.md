# mcp/src/agents_remember/certification/diagnostics/planning.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The CCR-R13@v2 packet clauses (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) and the leaf doc 13_non-certifying-diagnostic-e2e.md carry the one-canonical-scenario rule; task artifact paths are not repo-relative citations, so they are recorded as prose here.

- The diagnostic catalog may only replicate the exact canonical scenario rails at diagnostic altitude. [1]

### Repo-Internal References

- The shared certification plan compiler builds the altitude plan. [2]
- Registry validation gates admission before any plan is compiled. [3]
- The run controller consumes the compiled plan to build its run spec and plan record. [4]
- The diagnostics package imports these three planning helpers. [5]
- The diagnostics package lists these planning helpers in its public exports. [6]
- The outer certification facade re-exports these planning helpers. [7]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

- The altitude rules stay repository-neutral and rely only on registry/profile/certifying-plan inputs. [8]
