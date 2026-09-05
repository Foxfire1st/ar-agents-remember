# mcp/src/agents_remember/memory_quality/final_certification/certify.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/final_certification/certify.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T07:12:23Z |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `../overview.md` |

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

- `FinalCertificationEvidence` (class, lines 42-56) - every exact authority the final
  certification may read: admission, Gate 1-4 certificates, input changes, code/memory trees,
  pair identity, affected closure, validated coherence (or None), executed checks,
  missing-onboarding and stale-route-index counts, and the full-only rerun flag. Nothing is
  inferred.
- `certify_final_full_memory_coherence` (lines 59-134) - result assembly: green-prefix proof
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact authority bundle the certification may read. | `FinalCertificationEvidence` | mcp/src/agents_remember/memory_quality/final_certification/certify.py:42-56 |
| Folds supplied executed checks and identities into a returned green/red/blocked result. | `certify_final_full_memory_coherence` | mcp/src/agents_remember/memory_quality/final_certification/certify.py:59-134 |
| Maps the caller's full-only rerun observation to pass or blocked for the affected-closure item. | `_affected_closure_status` | mcp/src/agents_remember/memory_quality/final_certification/certify.py:137-141 |
| The typed refusal helper. | `_refuse` | mcp/src/agents_remember/memory_quality/final_certification/certify.py:144-145 |

## Update History

- 2026-09-05T07:12:23Z — CCR L31 independent-review correction: reread the complete module at
  ea359649 and distinguished actual result assembly from caller-owned check execution,
  coherence validation and certificate/finalization publication. The former wording copied
  the module docstring's broader protocol claim. Original source verification remains valid
  because the module's source blob is unchanged; this is a semantic card correction, not a
  new code acceptance or a claim that the missing production caller now exists.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 executable final full memory-coherence certification
  module delivered in code commit 16d1a4d6; anchors and ranges derived from the current
  worktree source and pinned to that commit.
