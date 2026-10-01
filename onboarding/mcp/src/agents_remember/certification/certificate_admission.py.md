# mcp/src/agents_remember/certification/certificate_admission.py

## Governing Overview

[Certification contract overview](overview.md)

## Purpose

Admission compilation for content-addressed gate certificates: freeze the exact dual-authority
inputs (generic R11 plan and repository R22 profile plan) before Gate 1 can start, and derive each
gate's semantic identity with its full semantic-input closure (CCR-R21@v2).

## Code Commentary

### Logic

`compile_certification_admission` requires a Git-tree candidate, admits the certification plan
against the registry and the repository profile plan against the canonical profile, then enforces
identity alignment (repository/candidate/profile/selection) and exact rail-contract equality per
gate between the generic and repository plans (IGA/IGA `_require_rail_alignment`,
`_rail_contract` digests). Each gate compiles an `AdmissionGateIdentity` with its
gate-plan/semantic digests, repository gate-plan digest (Gates 1-4), and canonical semantic inputs:
per-rail definition/adapter/runtime, selection-scope, artifact-dependency, plus the
repository-provided semantic inputs (prefixed `repository-`).

`canonicalize_certificate_inputs` deduplicates by input kind/id and rejects conflicting
digests; `gate_semantic_digest` digests gate-local plan semantics excluding the aggregate
plan/registry digests. The admission manifest is then content-addressed over its semantic
envelope.

### Invariants And Boundaries

- Admission happens before any gate starts and never after.
- Candidate identity must be an exact Git tree; profiles/registry/candidate must agree.
- R11 and R22 must contribute the same exact rail contracts and gate applicability per gate.
- Semantic inputs are canonical, unique, and digest-conflict free.
- A failure is a typed `CertificationContractError` with findings; there is no partial admission.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

- The R21 packet requires admission to compile and freeze direct-input identities before Gate 1. [1]

### Repo-Internal References

- The admission transaction freezes the dual plan authorities and derives gate identities. [2]
- Identity and rail alignment between R11 and R22 refuse mismatches. [3]
- Per-gate semantic inputs include rail definition/adapter/runtime/scope/artifact contracts. [4]
- Inputs are canonicalized and conflict-rejected. [5]

### Cross-Repo References

None; this is the repository-neutral admission owner.
