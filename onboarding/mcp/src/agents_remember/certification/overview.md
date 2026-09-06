# Certification Contract Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/certification` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-05T22:23+00:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## What This Area Is

The repository-neutral contract foundation for five ordered closeout gates:

1. pre-test code quality;
2. the large static test suite;
3. post-test code quality that consumes suite output;
4. clean-room integration and end-to-end tests;
5. onboarding and citation quality.

It owns immutable registry, repository-profile, plan, certificate, and terminal-result semantics.
`repository_profiles/` resolves and validates repository-owned data; the concrete Agents Remember
profile lives at `mcp/certification-profile-v1.json`. `certification_lane.py` derives the R11 registry
from that admitted R22 plan plus caller-supplied memory rails. Execution and lifecycle publication
remain owned by the worktree and application layers.

The repository layer contract declares this package at rank 3, after root errors, feature-free
kernel primitives, and served wire models, and before the stateful control plane. The placement is
an ownership rule rather than an inference from the current import graph: later control-plane,
worktree, and application consumers may depend on these generic contracts, while certification
cannot reach upward into their lifecycle or repository-specific behavior.

## Hot Path Summary

Start with `certification_lane.py` for the R22-plan plus Gate-5-rails bridge, `certificate_admission.py` for exact authority alignment, and `results.py` / `certificate_authority.py` for terminal manifests and green certificates. `repository_profiles/`, `telemetry/`, `diagnostics/`, `final_codex/`, and `replay/` preserve separate profile, observation, execution-contract, and measurement vocabularies; a library API is not proof of a production caller.

## Local Invariants And Traps

- Gate meaning is fixed, while the concrete Gate 1-4 rails, adapters, commands, ownership, and
  applicability are repository-profile data. Gate 5 remains memory-domain authority.
- Registry admission is bounded before expensive allocation and validation is exhaustive within
  that boundary. Reachability uses one prospective pre-allocation refusal followed by measured
  traversal reservations; it does not repeat a dominated exact-storage refusal. There is no
  truncation, safe-full selection, compatibility path, or fallback.
- Exact duplicate declarations may collapse, but conflicting variants remain visible.
- Plans bind the canonical registry digest, profile, exact candidate identity, all selected gates,
  complete rail catalogs, and deterministic execution waves.
- Gate 3 consumes declared Gate 2 artifacts; dependency and artifact flow cannot point backward.
- Terminal publication preserves every planned rail, typed status, ownership, evidence reference,
  artifact, and blocker. A generic wrapper exception is not equivalent evidence.
- Report-only or diagnostic data cannot elevate a failing enforcing/certifying result.
- This foundation intentionally contains no Agents Remember rail inventory or test command.
- `layers.toml` is the single package-architecture authority: `certification` is rank 3, imports
  only lower layers, and owns no baseline, exception, concrete executor, profile, lifecycle
  terminalization, or memory gate.

## Operating Model

A repository contributes explicit profiles and rail declarations to the generic registry. The
contract layer canonicalizes and validates those declarations, compiles an immutable plan for one
candidate, and later validates executor observations against that exact plan. Generic confined profile loading belongs to `repository_profiles/authority.py`; concrete profile
data, orchestration, process execution, and lifecycle projection remain with their respective
owners and must consume these contracts rather than duplicate them.

## Repository Architecture Evidence

The root architecture contract is onboarding-excluded as a one-to-one source under current path
rules, so this route overview and the governing repository overview carry its durable ownership
meaning without inventing a parallel `layers.toml` sidecar.

| Finding | Anchor | Source |
| --- | --- | --- |
| `certification` is a present rank-3 package between `models` and `controlplane`; its charter excludes concrete profiles, executors, lifecycle terminalization, and memory gates. | "order = ["; "[package.certification]" | layers.toml:32-59; layers.toml:105-114 |
| The adjacent control-plane charter remains the lowest stateful interaction service, so the lower generic contract does not absorb its record or policy ownership. | "[package.controlplane]" | layers.toml:116-126 |
| The strict checker derives direction from the declared order and refuses undeclared packages rather than using a baseline or fallback. | `load_contract`; `undeclared_dirs`; `_record_edge`; `build_report` | mcp/test_support/agents_remember_test_support/code_quality/layering.py:63-68; mcp/test_support/agents_remember_test_support/code_quality/layering.py:122-141; mcp/test_support/agents_remember_test_support/code_quality/layering.py:151-154; mcp/test_support/agents_remember_test_support/code_quality/layering.py:280-340 |

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | covered |
| `canonical.py` | [canonical.py.md](canonical.py.md) | covered |
| `digests.py` | [digests.py.md](digests.py.md) | covered |
| `limits.py` | [limits.py.md](limits.py.md) | covered |
| `models.py` | [models.py.md](models.py.md) | covered |
| `planning.py` | [planning.py.md](planning.py.md) | covered |
| `results.py` | [results.py.md](results.py.md) | covered |
| `validation.py` | [validation.py.md](validation.py.md) | covered |
| `certification_lane.py` | [certification_lane.py.md](certification_lane.py.md) | covered |
| `certificate_admission.py` | [certificate_admission.py.md](certificate_admission.py.md) | covered |
| `certificate_authority.py` | [certificate_authority.py.md](certificate_authority.py.md) | covered |
| `certificate_invalidation.py` | [certificate_invalidation.py.md](certificate_invalidation.py.md) | covered |
| `certificate_models.py` | [certificate_models.py.md](certificate_models.py.md) | covered |
| `certificate_store.py` | [certificate_store.py.md](certificate_store.py.md) | covered |
| `lifecycle_admission.py` | [lifecycle_admission.py.md](lifecycle_admission.py.md) | covered |
| `lifecycle_models.py` | [lifecycle_models.py.md](lifecycle_models.py.md) | covered |
| `lifecycle_recovery.py` | [lifecycle_recovery.py.md](lifecycle_recovery.py.md) | covered |
| `readiness.py` | [readiness.py.md](readiness.py.md) | covered |
| `readiness_models.py` | [readiness_models.py.md](readiness_models.py.md) | covered |
| `readiness_transitions.py` | [readiness_transitions.py.md](readiness_transitions.py.md) | covered |

## Docs And Boundary References

No Domain Documentation source or cross-repository implementation is configured for this memory
root. The accepted behavior is repository-owned and the package remains independent of any one
repository's commands.

## 260831-CCR-L16 - Durable Gate And Rail Telemetry

The `telemetry/` contract introduced by CCR-R16@v3 provides the
`telemetry/` subpackage to this route: one execution-coherent, content-addressed durable stream for
closeout generations and diagnostic runs. `telemetry/models.py` fixes the closed event vocabulary
(execution kinds, certificate dispositions and refusal codes, terminal result classes, the
exhaustive `EVENT_MATRIX`) and the immutable `TelemetryEvent` schema whose validators enforce the
matrix ID cardinality and the exact gate/rail identity rules; `telemetry/adapters.py` compiles one
event per owner-produced R11/R20/R21/R22 object without inventing authority;
`telemetry/store.py` CAS-publishes digest-chained journal entries into separate closeout and
diagnostic envelopes under an operation-scoped capacity policy; `telemetry/projection.py` folds the
durable events into a lossless boundary and Gate 1-5 projection with a content digest; and
`telemetry/validation.py` exhaustively validates one ordered stream without raising and without
deriving a rail pass from telemetry alone. The route facade (`__init__.py`) re-exports the full
telemetry surface.

## 260831-CCR-L13 — Optional Non-Certifying Diagnostic E2E Lane

CCR-R13@v2 (commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf`, leaf 260831-CCR-L13) adds the
`diagnostics/` subpackage to this route: the closed, immutable vocabulary and durable store for one
optional real-Codex replication of the canonical ARSPAWN scenario that may run only after the exact
candidate's R12 Gates 1-3 are green and stays explicitly non-certifying. `diagnostics/models.py`
fixes the structural separation (`acceptanceEligible`/`certifying` false literals, diagnostic-altitude
manifest carriage, typed scenario/infrastructure/parser failures, immutable gapless attempt/result
chains, and content-verified digests); `diagnostics/planning.py` projects the exact canonical scenario
rail at diagnostic altitude and refuses any second scenario implementation; `diagnostics/projection.py`
owns the optional-lane readiness projection (not-requested-optional, running, newest-terminal blocking,
plan-currentness staling, and the stable R14 non-satisfaction rule); and `diagnostics/store.py` keeps
one stable digest-chained manifest per candidate in an isolated namespace that can never overlap the
certifying quality-report manifest. The route facade (`__init__.py`) re-exports the full diagnostic
surface; actual run control that binds the trusted R12 host authority lives in
`worktrees.modules.quality.diagnostic_executor`.

## 260831-CCR-L17 - Measured Replay And Reduction Targeting

CCR-R17 (commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185`, leaf 260831-CCR-L17) adds the
`replay/` subpackage to this route: the correctness replay protocol records for measured replay of a
frozen incident baseline through the five-gate treatment. `replay/freeze.py` fixes replay freeze
identity (source, candidate, R22 profile, R11 plan, configuration, runtime/toolchain/executor/image,
machine class, instrumentation, measurement schema) and the append-only three-view incident
population (frozen original generations 1-8, post-analysis tail 9-13, dated supplements 14+ that
never enter the denominator); `replay/spans.py` reduces R16 telemetry spans to a closed
per-category union-wall reduction with reproducible arithmetic; `replay/measure.py` folds an R16
closeout event export into per-gate measured facts; `replay/models.py` fixes the closed
measured-run vocabulary (strata, span reductions, gate facts, the seventeen acceptance-scenario
expectations, evidence envelope); `replay/scenarios.py` projects the seventeen mandatory
acceptance scenarios to machine-readable green/red/not-applicable outcomes; and `replay/compare.py`
binds one digest-verified baseline-vs-treatment comparison report. Numeric reduction thresholds are
intentionally absent from the entire subpackage: the protocol approves measured replay and cost
reduction measurement, not a numeric performance claim.

## 260831-CCR-L14 - Final Real-Codex Gate-4 Certification Lane

CCR-R14@v3 (commit `54ff803a05209e06f732f2de1f90e2a71a069e08`, leaf 260831-CCR-L14) adds the
`final_codex/` subpackage to this route: the closed, immutable vocabulary and durable store for the
certifying two-fresh-no-retry Gate-4 proof of the exact candidate's canonical scenario rails.
`final_codex/models.py` fixes the structural two-fresh semantics (acceptanceEligible/certifying=true
literals, retryCount zero, disabled retry with no successor slot, one-pass-never-compensates, typed
scenario/infrastructure/parser failures, immutable attempt/run/repetition records with self-verified
digests, and no shape for CCR-R13 diagnostic evidence); `final_codex/planning.py` compiles the
immutable plan record only from the exact canonical R11 registry compilation for a certifying profile
planning the complete Gate-1..4 prefix and enforces the exact Gate-1..3 must-not-run barriers;
`final_codex/projection.py` owns the lane readiness projection (not-started, running,
two-fresh-pass, red, stale); `final_codex/store.py` keeps one stable digest-chained CAS run
manifest per candidate in an isolated namespace that can never overlap a forbidden certifying or
diagnostic quality-report root; and `final_codex/certificate.py` compiles the one bound Gate-4
certificate from the exact two-fresh run, the ordered Gate-1..3 certificate identities, and the
shared frozen runtime authority. The route facade (`__init__.py`) re-exports the full final-codex
surface; actual run control that binds the trusted R12 host authority lives in
`worktrees.modules.quality.final_codex_executor`.

## Current Production Composition

`compile_certification_lane` projects each admitted R22 `CompiledRail` back into an R11
`RailDefinition` without changing adapter, runtime, evidence, artifact, applicability, or authority
fields. It combines those Gate 1-4 rails with memory-domain Gate-5 rails, canonicalizes one registry,
compiles one exact candidate plan, and freezes the R21 admission. Unsupported repository-gate
applicability or missing/wrong-authority memory rails refuse before this admission exists.

The production caller is `worktrees/modules/quality/certification_records.py`, reached before
Gate 1 and after a green result through `quality/gate.py`. That caller currently registers memory
rails only for `agents-remember`; the generic bridge itself has no repository-specific inventory.
The record seam now requires the exact admitted candidate/profile/full plan/selection and physically reopens every nested evidence/artifact against the complete immutable report snapshot before publication. Selected certificate rows retain that snapshot and pin the actual generation; canonical store loads retain original semantic objects and provenance. Returned certification refusals propagate through the green caller. This repairs L30 evidence retention, while ordinary failed runs still raise before the record seam and therefore do not establish a complete R11 result population for every terminal outcome.

`lifecycle_admission.py` and `lifecycle_recovery.py` define R05 admission, finalization and recovery
contracts, but the inspected production tree has no caller of `compile_lifecycle_admission`,
`compile_lifecycle_finalization`, or `authorize_finalization_leg` outside that library. Similarly,
the ordinary closeout path does not call the R16 closeout event builders or instantiate
`DurableTelemetryStore`; optional diagnostic/final-Codex controllers retain their separate event
handling. R07 affected-closure and R08 final-memory certification likewise remain library-only in the
ordinary memory controller, which invokes readiness with no affected-closure plan digest.
Existing lifecycle journal recovery must not be described as integrated R05 certificate
recovery. Reconsider these gaps when the host owners actually call the APIs and verify their
required input/result identities.

| Finding | Anchor | Source |
| --- | --- | --- |
| The bridge compiles one aligned R11/R22/R21 lane and preserves admitted rail contracts. | "def compile_certification_lane("; "def _project_repository_rail(rail: CompiledRail) -> RailDefinition:"; "def _require_applicable_repository_gates(plan: RepositoryProfilePlan) -> None:" | mcp/src/agents_remember/certification/certification_lane.py:79-121; mcp/src/agents_remember/certification/certification_lane.py:187-245 |
| The production seam resolves the exact profile, binds memory rails and persists admission. | "def prepare_certification_records(" | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:165-200 |
| The gate freezes admission before execution and invokes the record adapter after a green result. | "def run_strict_code_quality_gate("; "def _freeze_certification_records(target, *, plan, candidate_tree) -> None:"; "def _record_certification_generation(target, *, plan, candidate_tree, manifest) -> None:" | mcp/src/agents_remember/worktrees/modules/quality/gate.py:243-323; mcp/src/agents_remember/worktrees/modules/quality/gate.py:464-507 |
| Typed R05 finalization and leg authorization exist as library functions; existence is not caller proof. | "def compile_certification_recovery_record("; "def compile_lifecycle_finalization("; "def validate_lifecycle_finalization_currentness("; "def authorize_finalization_leg(" | mcp/src/agents_remember/certification/lifecycle_recovery.py:53-160 |

## Update History

- 2026-09-05T22:23+00:00 — L30 route-impact review against `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Updated incoming publication-owner claims and source references. Certification-route source itself is unchanged; its genuine older verification stamp is preserved.

- 2026-09-05T07:10+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Corrected evidence retention overclaim, named R07/R08 production gap, and repaired bridge citation to the exact compiling function. Verification records current source claims, not execution or acceptance.


- 2026-09-05T06:12+00:00 — Reconciled profile, telemetry, diagnostic, final-Codex and replay knowledge; documented the live R11/R22 bridge and explicitly distinguished absent R05/closeout-telemetry callers from library capability.

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass (route impact): added the CCR-L14 section for the final real-Codex Gate-4 certification lane - the `final_codex/` subpackage (closed two-fresh models, plan-record compilation with exact-predecessor barriers, lane readiness projection, isolated CAS run store, and the bound Gate-4 certificate compiler) and the widened facade re-exports, with the higher worktree run controller consuming the trusted R12 authority. Verification stamp is the full leaf code commit `54ff803a05209e06f732f2de1f90e2a71a069e08` (tree `aff2e268968397ab8db042a782652957a3600dda`).


- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass (route impact): added the CCR-L17 section for the measured-replay and reduction subpackage - replay freeze identity and comparability, the append-only three-view incident population, the deterministic span analyzer, the measured-run reducer, the seventeen acceptance scenarios, and the digest-bound comparison report, with numeric reduction thresholds deliberately out of scope. Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).


- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass (route impact): added the CCR-L13 section for the optional non-certifying diagnostic E2E lane - the `diagnostics/` subpackage (closed models, altitude plan projection, optional-lane readiness projection, isolated durable store) and the widened facade re-exports, with the higher worktree run controller consuming the trusted R12 authority. Verification stamp is the full leaf code commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf` (tree `631145bf3e0d5899b1dcbccf8c0d4a8257821f0d`).


- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5 memory pass (route impact): added the CCR-L16
  section for the durable gate and rail telemetry subpackage - closed event vocabulary with an
  exhaustive matrix, compile adapters, digest-chained journal store, lossless projection, and
  never-raising validator. Verification metadata stays pinned until closeout stamps the leaf
  code commit.


- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 reconciled the bounded-reachability owner after
  removing a dominated second refusal: the prospective pre-allocation refusal and measured
  traversal reservations remain the complete route contract. Verification remains closeout-owned.

- 2026-09-01T05:28+02:00 — CCR-L11 Attempt 9 recorded the enforced rank-3 package declaration
  and its `models < certification < controlplane` ownership boundary. The accepted registry,
  planning, admission, and typed-result implementation account is unchanged; only its explicit
  repository architecture declaration is new. Verification remains closeout-owned.

- 2026-09-01T03:11+02:00 — Created the route-owned overview for the generic five-gate registry,
  plan-authority, bounded-validation, and typed-result foundation. Verification remains
  closeout-owned until the source candidate is committed.
