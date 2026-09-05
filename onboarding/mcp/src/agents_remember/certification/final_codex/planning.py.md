# mcp/src/agents_remember/certification/final_codex/planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/final_codex/planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Final real-codex plan projection and exact-predecessor barriers (leaf 260831-CCR-L14, code commit 54ff803a). CCR-R14@v3 runs exactly two fresh independent no-retry certifying repetitions only after exact green certifying Gate-1..3 certificates for the same code tree, profile, plan, config, toolchain/runtime, and selected certification profile. This module compiles the immutable `FinalCodexPlanRecord` from the R11 canonical registry and the exact certifying plan, resolves the exact Gate-4 plan the record froze, and enforces the must-not-run barriers so no scenario step starts against a red, stale, non-certifying, candidate-mismatched, or differently bound predecessor.

## Code Commentary

### Logic

- `compile_final_codex_plan_record` (lines 45-131) validates the registry, selects the profile, requires a certifying-altitude profile that plans the complete sorted Gate-1..4 prefix, refuses a candidate mismatch or non-certifying plan, admits the certifying plan as the exact canonical registry compilation (`admit_certification_plan`), reads the Gate-4 plan, and freezes the self-digested `FinalCodexPlanRecord`. Because the plan must equal the canonical registry compilation, a second or framework-hardcoded scenario catalog is structurally impossible.
- `final_codex_gate_plan` (lines 134-191) returns the certifying Gate-4 plan only when the certifying plan binds the exact frozen candidate, profile, registry, and Gate-4 plan digest; a stale or rebinding certifying plan refuses before any scenario step.
- `require_gates_one_to_three_green` (lines 194-256) requires the exact complete certifying Gate-1..3 result manifests: green disposition, certifying altitude, exact candidate binding, and the exact certification-plan digest plus each gate-plan digest the run freezes.
- Typed refusal helpers (`_raise_contract_error` and `_raise_lane`, lines 306-321) produce `CertificationContractError`s carrying `RegistryValidationFinding`/`CertificationContractFinding` payloads.

### Conventions

Every plan-time refusal is a typed `CertificationContractError`; every run-time predecessor refusal is a lane finding under the `final-codex-` code family.

### Invariants And Boundaries

- The final lane never runs at diagnostic altitude and requires a certifying profile planning the complete Gate-1..4 prefix.
- The Gate-4 rails equal the exact canonical scenario catalog of the certifying plan.
- Missing, stale, red, non-certifying, candidate-mismatched, or differently bound Gate-1..3 predecessors refuse before any scenario step starts.

### Todos

None.

## Docs References

The approved CCR-R14@v3 requirement packet and the leaf doc 14_final-real-codex-certification govern this module; task-artifact paths are not repo-relative citations, so clauses are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The plan record compiles only from the exact canonical registry compilation for a certifying profile planning the Gate-1..4 prefix. | `compile_final_codex_plan_record` | mcp/src/agents_remember/certification/final_codex/planning.py:45-131 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The R11 canonical registry validation runs before plan admission. | `validate_registry` | mcp/src/agents_remember/certification/validation.py:1-120 |
| Certifying-plan admission refuses altered plan bytes against the canonical registry. | `admit_certification_plan` | mcp/src/agents_remember/certification/planning.py:1-160 |
| The immutable plan record is defined in the final-codex models. | `FinalCodexPlanRecord` | mcp/src/agents_remember/certification/final_codex/models.py:173-199 |
| Gate-1..3 manifests come from the shared result-manifest contracts. | `GateResultManifest` | mcp/src/agents_remember/certification/models.py:457-479 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lane is repository-neutral and consumes profile/plan declarations, never repository-selected behavior. | `RegistryProfile`; `CertificationPlan` | mcp/src/agents_remember/certification/models.py:140-143; mcp/src/agents_remember/certification/models.py:326-342 |

## Update History
- 2026-09-05T06:24:16+00:00: Generated citation repair: `GateResultManifest` repointed to mcp/src/agents_remember/certification/models.py:457-479. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `RegistryProfile`; `CertificationPlan` repointed to mcp/src/agents_remember/certification/models.py:140-143; mcp/src/agents_remember/certification/models.py:326-342. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new CCR-R14 final-codex plan projection and exact-predecessor barriers delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
