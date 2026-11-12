# mcp/src/agents_remember/certification/final_codex/planning.py

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

## Evidence

### Docs References

The approved CCR-R14@v3 requirement packet and the leaf doc 14_final-real-codex-certification govern this module; task-artifact paths are not repo-relative citations, so clauses are recorded as prose here.

- The plan record compiles only from the exact canonical registry compilation for a certifying profile planning the Gate-1..4 prefix. [1]

### Repo-Internal References

- The R11 canonical registry validation runs before plan admission. [2]
- Certifying-plan admission refuses altered plan bytes against the canonical registry. [3]
- The immutable plan record is defined in the final-codex models. [4]
- Gate-1..3 manifests come from the shared result-manifest contracts. [5]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

- A registry profile declares repository-neutral certification identity and inputs. [6]
- The certification plan binds its candidate and ordered gate plans. [7]
