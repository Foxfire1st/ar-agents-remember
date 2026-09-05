# mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T08:27+02:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

The CCR-R13 run controller that consumes the exact trusted R12 host authority (leaf 260831-CCR-L13, code commit 4ba18bb2). The diagnostic lane is an optional one-replication real-Codex E2E that may run only after the exact candidate's R12 Gates 1-3 are green. This module composes the durable diagnostic manifest store and plan projection (agents_remember.certification.diagnostics) with the R12 trusted launcher so every Dagger-backed diagnostic execution freezes one existing connection-only runner/store snapshot and registers itself as a live owner through the exact same authority closeout and integration consume. There is deliberately no engine selection, private provisioning, profile override, or runner retirement here.

## Code Commentary

### Logic

- `DiagnosticHardFailure` (lines 90-107) is a typed infrastructure/parser failure carrying a `DiagnosticFailureRecord` and bounded teardown evidence; it produces a hard-failure result and never a pass.
- `ScenarioReplicationEvidence` (lines 110-115) is one complete scenario replication: full checkpoint catalog plus teardown facts.
- `ScenarioReplicationRunner` (lines 118-129) is the injection protocol: `run_once` executes the canonical rails once against the admitted environment/snapshot.
- `DiagnosticRunSpec` (lines 132-149) freezes the compiled plan identity one attempt replicates (candidate, registry, certifying/diagnostic plans, gate plan, plan record, environment identity, profile, scenario gate 4, plan version).
- `DiagnosticEngineOptions` (lines 152-160) injects environ, inspector, clock, nonce source, and an optional telemetry sink. No telemetry callback is installed by default.
- `DiagnosticAttempt` (lines 163-173) is one live attempt bound to its frozen authority snapshot.
- `DiagnosticExecutionEngine` (lines 176-563) is the run control:
  - `admit` (lines 197-226) requires the exact candidate's certifying Gate 1-3 manifests to be green and complete (`_require_gates_one_to_three_green`, lines 629-662: exact (1,2,3) gate tuple, exact candidate binding, certifying altitude, green disposition), reserves the next attempt with an R16 diagnostic nonce, and freezes the R12 authority (`_admit_authority`, lines 271-329). Fresh admission goes through `admit_dagger_authority`; continuation reuses a frozen snapshot via `reuse_authority_for_continuation`. Refusals before any scenario step include a live authority-transition barrier, missing/malformed/provisioning-capable host declarations, ambient or profile conflicts, and an already-live diagnostic attempt. If the store refuses reservation/mark-running, the exact owner is released (`release_dagger_authority`).
  - `run` (lines 228-250) executes at most one replication (`_require_live_attempt`, lines 331-344 refusing a second replication or abort on a terminal attempt) and terminalizes pass/fail from the complete diagnostic-altitude manifest (`_terminalize_catalog`, lines 348-401: build_rail_result per observation, compile_gate_result_manifest at diagnostic altitude, derive the scenario failure from the red enforcing rail, build teardown and draft, publish) or terminalizes a typed hard failure (`_terminalize_hard_failure`, lines 403-420).
  - `abort` (lines 252-267) terminalizes an interrupted attempt with teardown evidence, released owner, and no pass.
  - `_publish` (lines 422-430) publishes the terminal through the store and releases the exact diagnostic owner.
  - Draft/record construction (lines 434-516) binds the attempt reservation identity, environment binding, and runtime-authority binding copies from the frozen snapshot (never selecting or provisioning), then renders the closed result payload.
  - Telemetry/nonce helpers (lines 520-563) derive the diagnostic nonce from candidate + plan + attempt number + entropy. When `on_telemetry` is supplied they compile R16 started/terminal events and call that sink; with no sink they emit nothing. Durable telemetry storage is not constructed by this module.
- `DiagnosticRunOptions` (lines 566-572) freezes scenario options (environment identity, plan version, gate).
- `build_diagnostic_run_spec` (lines 575-617) compiles the diagnostic plan and freezes the `DiagnosticPlanRecord` plus the `DiagnosticRunSpec` for one scenario gate.
- `require_gates_one_to_three_green` (lines 620-626) is the public wrapper of the gate precondition check.
- `DiagnosticAdmissionRefused` (lines 665-670) wraps an R12 `DaggerRuntimeAuthorityError` as a `CertificationContractError` carrying its findings.

### Conventions

All execution crosses the R12 trusted launcher; no engine selection, private provisioning, profile override, or runner retirement happens here. Every refusal before a scenario step is a typed `CertificationContractError` (or `DiagnosticAdmissionRefused`), and every terminalization releases only the attempt's own runtime owner.

### Invariants And Boundaries

- A diagnostic may run only after the exact candidate's R12 Gates 1-3 are green at certifying altitude.
- At most one replication per attempt; retry creates a new diagnostic result only and never promotes.
- Pass/fail outcomes embed the complete diagnostic-altitude gate result manifest; aborted and hard-failure carry teardown evidence and never a pass.
- The exact frozen R12 snapshot is bound into every attempt/result; the reusable layer store is never deleted and a runner owned by another operation is never retired.
- Emitted telemetry envelopes carry the R16 diagnostic nonce; persistence depends on the supplied sink. The diagnostic manifest store persists attempt/results independently of that optional callback.
- Scenario execution is supplied through `ScenarioReplicationRunner.run_once`; this controller does not launch a concrete Codex harness by itself.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R13@v2 (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) requires every Dagger-backed diagnostic route to consume and bind the exact R12v4 host runner/store authority; the R12 authority contract is implemented by dagger_authority.py (CCR-R12@v4). Task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| Diagnostics bind the frozen R12 host authority and never select, copy, replace, or privately provision infrastructure. | `_admit_authority`; `admit_dagger_authority` | mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:271-329; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:933-989 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The R12 authority admits a checked host snapshot, records live consumers in its locked registry, and releases only the exact owner. | `admit_dagger_authority`; `AuthorityRegistry`; `release_dagger_authority` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:933-987; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:588-600; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:1115-1130 |
| Gate 1-3 green manifests come from the shared certifying result manifest contracts. | `compile_gate_result_manifest`; `GateResultManifest` | mcp/src/agents_remember/certification/results.py:63-111; mcp/src/agents_remember/certification/models.py:457-479 |
| The durable diagnostic manifest store owns reservation, running, publish, and abandon. | `DiagnosticManifestStore` | mcp/src/agents_remember/certification/diagnostics/store.py:53-288 |
| Diagnostic event builders produce started/terminal envelopes; the engine invokes them only for an installed telemetry sink. | `compile_diagnostic_started`; `compile_diagnostic_terminal`; `_emit_started`; `_emit_terminal` | mcp/src/agents_remember/certification/telemetry/adapters.py:433-461; mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:535-563 |
| The certification facade imports diagnostic contracts and projections; run-control entry points remain in the higher worktree quality module. | "from agents_remember.certification.diagnostics import ("; "class DiagnosticExecutionEngine:" | mcp/src/agents_remember/certification/__init__.py:18-37; mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:176-193 |

## Cross-Repo References

No cross-repository implementation boundary is owned here; the R12 authority is host-level and repository-external but consumed only through the R12 module boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R12 host declaration/registry lives outside every repository and worktree and is never re-selected here. | `admit_dagger_authority`; `release_dagger_authority` | mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:321-329; mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:422-430 |

## Update History

- 2026-09-05T08:27+02:00 — L31 native curator: Corrected the nonexistent facade re-export claim to the contract/run-controller layer boundary, replaced module-name anchors with exact authority constructs, and clarified that diagnostic telemetry requires an optional sink. Reviewed against frozen code `ea35964985f30080488270e71ac81657ac40682b`; this records source verification, not gate acceptance.

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new CCR-R13@v2 diagnostic run controller delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
