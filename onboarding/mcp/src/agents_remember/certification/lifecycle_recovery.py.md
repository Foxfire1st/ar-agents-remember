# mcp/src/agents_remember/certification/lifecycle_recovery.py

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns exact finalization-boundary compilation, currentness reread, unfinished-leg authorization and certificate-authority revalidation. These retained contracts bind the admitted candidate and current journal; the removed recovery-record compiler no longer journals certificate-input-change reuse here.

## Code Commentary

### Logic

`compile_lifecycle_finalization` checks ready/finalizing operation state, claimed door and current approval, then compares code/memory trees, topology/task intent, commit intent and journal authority before binding `nextLeg`. `validate_lifecycle_finalization_currentness` refuses movement; `authorize_finalization_leg` authorizes only that exact unfinished leg after the reread. `revalidate_certificate_authority` accepts retained certificate identities and rereads R21 authority without changing gate or finalization state. Typed refusals carry `gateStarts: 0`.

### Conventions

Recovery composes existing certificate and finalization authorities; it never creates a
replacement candidate or a fallback path by inference.

### Invariants And Boundaries

- Finalization consumes the supplied exact admitted chain and retained certificate identities; no newest-result or path search substitutes for them.
- Partial publication resumes only the exact unfinished durable leg with zero certification starts.
- Candidate, certificate, operation, door, approval, commit-intent and journal authority must remain current before publication.
- Partial publication resumes the exact durable leg with zero certification starts.
- The operation, door, and approval state must remain current immediately before publication.

### Todos

The durable leg execution and repository writes are later lifecycle owners; this module freezes
the boundary records only.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for recovery and finalization semantics.

CCR-R05@v3 (requirements/CCR-R05-v3-exact-candidate-admission-and-recovery.md, "Recovery
Decision") requires resuming the exact durable finalization leg with zero certification
starts, reusing every exact green predecessor, and refusing when candidate or authority
movement precedes a write.


### Repo-Internal References


### Cross-Repo References

No cross-repository implementation boundary is owned here.

- Gate certificate and invalidation contracts are imported from the R21 owners. [4]

## CCR-L42 current candidate

Finalization and certificate-authority revalidation now accept the retained `GateCertificateIdentity` sequence and pass it through the finalization authority reread. Certificate reuse remains exact and zero-start; this adds retained certificate identity to the existing boundary.

- Finalization revalidates the exact admitted candidate and journal, then binds the unfinished leg. [2]

- Currentness reread and exact-leg authorization gate every publication write. [3]
