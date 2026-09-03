# mcp/src/agents_remember/certification/certificate_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/certificate_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | 6f10c24d72db6171c0d434b307e6806996e2f11d |
| lastVerifiedCommitDate | 2026-09-02T18:10:52+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R21 packet requires admission to compile and freeze direct-input identities before Gate 1. | "Required Behavior"; "Admission compiles and freezes direct-input identities before Gate 1" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R21-v2-content-addressed-phase-certificates.md:77-91 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The admission transaction freezes the dual plan authorities and derives gate identities. | `compile_certification_admission` | mcp/src/agents_remember/certification/certificate_admission.py:36-84 |
| Identity and rail alignment between R11 and R22 refuse mismatches. | `_require_admission_identity_alignment`; `_require_rail_alignment` | mcp/src/agents_remember/certification/certificate_admission.py:122-147; mcp/src/agents_remember/certification/certificate_admission.py:150-168 |
| Per-gate semantic inputs include rail definition/adapter/runtime/scope/artifact contracts. | `_compile_admission_gate`; `_generic_gate_inputs` | mcp/src/agents_remember/certification/certificate_admission.py:179-203; mcp/src/agents_remember/certification/certificate_admission.py:206-240 |
| Inputs are canonicalized and conflict-rejected. | `canonicalize_certificate_inputs` | mcp/src/agents_remember/certification/certificate_admission.py:96-112 |

## Cross-Repo References

None; this is the repository-neutral admission owner.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): created the card for the new
  admission compiler that freezes the R11/R22 dual authority, per-gate semantic inputs, and the
  admission digest before Gate 1. Verification is pinned to the owning commit.
