# Certification Contract Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/certification` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-01T11:33+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
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

It owns immutable registry, plan, and terminal-result semantics. It does not yet execute rails,
declare the Agents Remember repository profile, replace the current closeout wrapper, or own
lifecycle publication.

The repository layer contract declares this package at rank 3, after root errors, feature-free
kernel primitives, and served wire models, and before the stateful control plane. The placement is
an ownership rule rather than an inference from the current import graph: later control-plane,
worktree, and application consumers may depend on these generic contracts, while certification
cannot reach upward into their lifecycle or repository-specific behavior.

## Hot Path Summary

`canonicalize_registry` performs bounded deterministic admission; `validate_registry` returns all
semantic findings within that budget; `compile_certification_plan` creates exact candidate-bound
gate plans; `admit_certification_plan` refuses altered plan bytes; `build_rail_result` binds one
observation to a planned rail; and `compile_gate_result_manifest` publishes the complete typed
terminal catalog only after all result contracts pass.

## Local Invariants And Traps

- Gate meaning is fixed, while the concrete Gate 1–4 rails, adapters, commands, ownership, and
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
candidate, and later validates executor observations against that exact plan. Concrete profile
loading, orchestration, process execution, retry policy, and lifecycle projection belong to later
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

## Docs And Boundary References

No Domain Documentation source or cross-repository implementation is configured for this memory
root. The accepted behavior is repository-owned and the package remains independent of any one
repository's commands.


## 260831-CCR-L16 - Durable Gate And Rail Telemetry

CCR-R16@v3 (certified commit `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`, leaf 260831-CCR-L16) adds the
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

## Update History

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
