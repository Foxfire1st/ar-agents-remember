# mcp/src/agents_remember/certification/final_codex/certificate.py

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

## Evidence

### Docs References

The approved CCR-R14@v3 requirement packet and the leaf doc 14_final-real-codex-certification govern this module; task-artifact paths are not repo-relative citations, so clauses are recorded as prose here.

- The certificate binds the exact green Gate-1..3 predecessor identities as direct predecessors. [1]

### Repo-Internal References

- The run manifest supplies the two-fresh aggregate and both repetition results the certificate binds. [2]
- Predecessor identities use the R21 gate-certificate identity model. [3]
- The frozen plan record supplies candidate, profile, scenario, and plan identities. [4]
- The runtime-authority binding is the copied R12 snapshot digest plus inspected runner/store identities. [5]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

- The lane is repository-neutral and consumes the frozen R12 host snapshot through the trusted launcher only. [6]
