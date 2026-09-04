# mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

The CCR-R14 run controller that consumes the exact trusted R12 host authority (leaf 260831-CCR-L14, code commit 54ff803a). The final real-codex lane is the certifying Gate-4 proof: after the exact candidate's R12 Gates 1-3 are green, it runs exactly two fresh independent certifying repetitions of the canonical scenario rails with retry disabled, fresh client/process state per repetition, exact accepted scenario version, bounded evidence, and an explicit result for each. This module composes the durable final-codex manifest store and projection (agents_remember.certification.final_codex) with the R12 trusted launcher so every Dagger-backed certifying repetition freezes one existing connection-only runner/store snapshot and registers itself as a live owner through the exact same authority closeout and integration consume.

## Code Commentary

### Logic

- `FinalCodexHardFailure` (lines 90-110) is a typed infrastructure/parser failure carrying a `FinalCodexFailureRecord` plus bounded teardown evidence; it produces a hard-failure repetition result and never a pass.
- `FinalCodexScenarioEvidence` (lines 113-119) is one complete fresh scenario repetition: full checkpoint catalog plus teardown facts.
- `FinalCodexScenarioRunner` (lines 122-134) is the injection protocol: `run_once` executes the canonical rails exactly once against the admitted environment/snapshot with fresh state.
- `FinalCodexRunSpec` (lines 137-153) freezes the compiled plan identity one two-repetition run certifies.
- `FinalCodexEngineOptions` (lines 156-163) injects environ, inspector, clock, and nonce source; defaults are production.
- `FinalCodexAttempt` (lines 166-176) is one live run bound to its frozen authority snapshot.
- `FinalCodexExecutionEngine` (lines 179-600) is the run control:
  - `admit` (lines 199-235) requires the exact candidate's certifying Gate-1..3 manifests to be green against the frozen plan (`require_gates_one_to_three_green`), derives two fresh repetition identities, reserves the attempt, and freezes the R12 authority (`_admit_authority`, lines 295-354: fresh admission via `admit_dagger_authority` or continuation reuse via `reuse_authority_for_continuation`); on store refusal it releases the owner. Refusals before any scenario step include live authority-transition barriers, missing/malformed/provisioning-capable hosts, ambient/profile conflicts, an in-flight run, and the retry-disabled same-plan terminal run.
  - `run` (lines 237-258) executes each fresh repetition exactly once (`_run_repetition`, lines 373-390) and releases the owner only after both slots publish; a `FinalCodexHardFailure` terminalizes the interrupted slot as a typed hard failure.
  - `abort` (lines 260-291) publishes aborted results for every unpublished slot with teardown evidence, releases the exact owner, and never fabricates a pass.
  - `_publish_catalog` (lines 392-447) builds rail results, compiles the certifying Gate-4 result manifest, derives the scenario failure from the red enforcing rail, and publishes the repetition.
  - Draft/record construction (lines 496-600) binds candidate/plan identity, fresh repetition identity, environment binding, and the frozen runtime-authority binding copy from the snapshot - never selecting or provisioning.
- `FinalCodexRunOptions` (lines 603-609) freezes environment/scenario/plan versions.
- `build_final_codex_run_spec` (lines 612-640) compiles the plan record and resolves the exact Gate-4 plan into the run spec.
- `FinalCodexAdmissionRefused` (lines 643-648) wraps an R12 `DaggerRuntimeAuthorityError` as a typed `CertificationContractError`.

### Conventions

All execution crosses the R12 trusted launcher; no engine selection, private provisioning, profile override, or runner retirement happens here. Every terminalization releases only the run's own runtime owner and never deletes the reusable layer store or retires a runner owned by another operation.

### Invariants And Boundaries

- The final lane runs only after the exact candidate's R12 Gates 1-3 are green at certifying altitude against the exact frozen plan.
- Exactly two fresh independent certifying repetitions with distinct client/process identities and retryCount zero; one passing repetition can never compensate the other.
- Pass/fail outcomes embed the complete certifying Gate-4 result manifest; aborted and hard-failure outcomes carry teardown evidence and never a pass.
- Retry is disabled for the exact same plan identity; a code/config/runtime repair changes the plan identity and admits a genuinely fresh attempt.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R14@v3 requires every Dagger-backed certifying repetition to consume and bind the exact R12 host runner/store authority; the R12 authority contract is implemented by dagger_authority.py (CCR-R12). Task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| Certifying repetitions bind the frozen R12 host authority and never select, copy, replace, or privately provision infrastructure. | `_admit_authority`; `admit_dagger_authority` | mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py:295-354; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:933-989 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The R12 host authority layer owns admission, snapshot freeze, owner registry, and exact release. | `dagger_authority` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:1-60; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:588-833 |
| Gate-1..3 green manifests come from the shared certifying result-manifest contracts. | `compile_gate_result_manifest`; `GateResultManifest` | mcp/src/agents_remember/certification/results.py:1-120; mcp/src/agents_remember/certification/models.py:60-119 |
| The durable final-codex store owns reservation, running, publish, and the CAS chain. | `FinalCodexManifestStore` | mcp/src/agents_remember/certification/final_codex/store.py:62-274 |
| The lane projection gates certificate readiness for the run. | `project_final_codex_lane` | mcp/src/agents_remember/certification/final_codex/projection.py:88-113 |
| The outer certification facade re-exports the run controller vocabulary for the certification boundary. | `final_codex_executor` | mcp/src/agents_remember/certification/__init__.py:38-67; mcp/src/agents_remember/certification/__init__.py:154-277 |

## Cross-Repo References

No cross-repository implementation boundary is owned here; the R12 authority is host-level and repository-external but consumed only through the R12 module boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R12 host declaration/registry lives outside every repository and worktree and is never re-selected here. | `admit_dagger_authority`; `release_dagger_authority` | mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py:346-354; mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py:237-258 |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new CCR-R14 final real-codex run controller delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
