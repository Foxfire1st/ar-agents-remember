# mcp/src/agents_remember/certification/final_codex/certificate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/final_codex/certificate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Bound Gate-4 certificate compilation for the final real-Codex lane (leaf 260831-CCR-L14, code commit 54ff803a). CCR-R14@v3 publishes one immutable Gate-4 certificate only from the exact two-fresh-pass lane: the run must be complete and terminal, the aggregate green (both fresh repetitions passed, retryCount zero), the manifest bound to the exact frozen plan/candidate/profile/scenario, the direct predecessors the exact ordered Gate-1..3 certifying certificate identities, and both repetitions bound to one shared frozen R12 runtime-authority snapshot. The module is repository-neutral and consumes the R21 certificate/authority models as inputs; it does not modify those surfaces.

## Code Commentary

### Logic

- `FinalCodexCertificateEnvelope` (lines 59-100) is the semantic envelope: exact ordered Gate-1..3 `directPredecessors`, the two `resultManifestDigests`, the shared `runtimeAuthority`, and both `repetitionResults`; its validator refuses non-certifying, non-acceptance-eligible, or retried repetitions and an authority snapshot neither repetition bound.
- `FinalCodexGateFourCertificate` (lines 103-114) wraps the envelope and verifies the `certificateDigest` covers the whole semantic envelope.
- `compile_gate_four_certificate` (lines 117-204) compiles the certificate from the frozen plan record, the run manifest, and the predecessor identities: it refuses a non-(1,2,3) predecessor prefix, a candidate or plan mismatch, an incomplete or non-terminal run, a non-green aggregate (one passing repetition can never compensate), a stale or rebinding manifest, or missing result manifests, then builds the digest-verified envelope and certificate.

### Conventions

Every refusal is a typed `CertificationContractError` carrying a `CertificationContractFinding` with a stable code and path (`final-codex-...` family) via `_raise_certificate` (lines 207-212).

### Invariants And Boundaries

- A certificate can never bind a retried, aborted, hard-failure, or single-pass composition.
- Direct predecessors must be exactly the ordered Gate-1..3 identities; diagnostic-altitude predecessors never satisfy the lane.
- The certificate digest covers the entire envelope, and the envelope binds both fresh repetition results plus their result-manifest digests.

### Todos

None.

## Docs References

The approved CCR-R14@v3 requirement packet and the leaf doc 14_final-real-codex-certification govern this module; task-artifact paths are not repo-relative citations, so clauses are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The certificate binds the exact green Gate-1..3 predecessor identities as direct predecessors. | `FinalCodexCertificateEnvelope` | mcp/src/agents_remember/certification/final_codex/certificate.py:59-100 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The run manifest supplies the two-fresh aggregate and both repetition results the certificate binds. | `FinalCodexRunManifest`; `aggregate` | mcp/src/agents_remember/certification/final_codex/models.py:376-413 |
| Predecessor identities use the R21 gate-certificate identity model. | `GateCertificateIdentity` | mcp/src/agents_remember/certification/certificate_models.py:1-60 |
| The frozen plan record supplies candidate, profile, scenario, and plan identities. | `FinalCodexPlanRecord` | mcp/src/agents_remember/certification/final_codex/models.py:173-199 |
| The runtime-authority binding is the copied R12 snapshot digest plus inspected runner/store identities. | `FinalCodexRuntimeAuthorityBinding` | mcp/src/agents_remember/certification/final_codex/models.py:116-139 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lane is repository-neutral and consumes the frozen R12 host snapshot through the trusted launcher only. | `runtimeAuthority` | mcp/src/agents_remember/certification/final_codex/certificate.py:94-99 |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new CCR-R14 bound Gate-4 certificate compiler delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
