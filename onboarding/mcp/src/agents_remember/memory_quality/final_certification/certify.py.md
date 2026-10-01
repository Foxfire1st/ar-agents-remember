# mcp/src/agents_remember/memory_quality/final_certification/certify.py

## Governing Overview

[memory_quality overview](../overview.md)

## Purpose

Assembles the final memory-coherence result from caller-supplied evidence for CCR-R08 Gate 5.
`certify_final_full_memory_coherence` validates the supplied green Gate 1-4 prefix, binds the
supplied code/memory identities and affected-closure plan, folds already executed check results
into the complete catalog attestation, and returns a typed green/red/blocked result. On green
it also returns the R21 Gate-5 semantic inputs. The caller supplies the validated coherence
record, executed checks, missing-card and stale-index counts, and full-only rerun observation.
This function performs no checker execution, memory update, certificate-store publication or
finalization write. The reviewed cumulative source has no production caller outside this
package, so this assembly API alone does not establish an end-to-end Gate-5 execution path.

## Code Commentary

### Logic

Module-level surface:

- `FinalCertificationEvidence` (class, lines 44-60) - every exact authority the final
  certification may read: admission, Gate 1-4 certificates, input changes, code/memory trees,
  pair identity, affected closure, validated coherence (or None), executed checks,
  missing-onboarding and stale-route-index counts, and the full-only rerun flag. Nothing is
  inferred.
- `certify_final_full_memory_coherence` (lines 62-137) - result assembly: green-prefix proof
  first (stale or invalid prefix refuses before any catalog work), current coherence required
  (`gate-five-coherence-blocked` when the supplied validated coherence is absent), coherence subrecords derived, exact plan
  compiled, attestation built from the executed catalog (affected-closure status derives from
  the full-only rerun flag via `_affected_closure_status`), Gate-5 inputs assembled only on
  an OK attestation, and a final result that is green (finalization-eligible), red (a fail), or
  blocked (a blocked item with a reason). The executed catalog data comes from the caller;
  this function does not invoke the underlying checks or persist the returned result.

### Conventions

Refusal statuses are typed and carry a legal `next_action`; the certification result binds
the exact memory tree and plan digest through the closed models.

### Invariants And Boundaries

- Certification never mutates code or memory.
- A green result requires a passing attestation over the supplied catalog data, assembled
  Gate-5 inputs, the supplied validated coherence record, and the exact reused green Gate 1-4
  prefix. Actual execution and currentness of the supplied memory observations belong to the
  caller; returning finalization-eligible does not itself authorize or execute a Git write.

### Todos

None.

## Evidence

### Repo-Internal References

- The exact authority bundle the certification may read. [1]
- Folds supplied executed checks and identities into a returned green/red/blocked result. [2]
- Maps the caller's full-only rerun observation to pass or blocked for the affected-closure item. [3]
- The typed refusal helper. [4]
