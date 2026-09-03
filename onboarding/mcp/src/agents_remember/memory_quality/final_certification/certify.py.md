# mcp/src/agents_remember/memory_quality/final_certification/certify.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/final_certification/certify.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:48+02:00 |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality overview](../overview.md)

## Purpose

Executable surface of the final full memory-coherence certification (CCR-R08 Gate 5).
`certify_final_full_memory_coherence` runs the complete Gate-5 protocol against one exact
candidate pair: prove the green Gate 1-4 prefix, bind the exact memory tree after governed
writes, run the complete final catalog with content-addressed subresults, require the current
canonical coherence record and exact candidate pair, assemble the R21 Gate-5 semantic inputs,
and publish one typed green/red/blocked certification. Certification never mutates code or
memory; every refusal is typed and blocks finalization.

## Code Commentary

### Logic

Module-level surface:

- `FinalCertificationEvidence` (class, lines 42-56) - every exact authority the final
  certification may read: admission, Gate 1-4 certificates, input changes, code/memory trees,
  pair identity, affected closure, validated coherence (or None), executed checks,
  missing-onboarding and stale-route-index counts, and the full-only rerun flag. Nothing is
  inferred.
- `certify_final_full_memory_coherence` (lines 59-134) - the protocol: green-prefix proof
  first (stale or invalid prefix refuses before any catalog work), current coherence required
  (`gate-five-coherence-blocked` otherwise), coherence subrecords derived, exact plan
  compiled, attestation built from the executed catalog (affected-closure status derives from
  the full-only rerun flag via `_affected_closure_status`), Gate-5 inputs assembled only on
  an OK attestation, and a final result that is green (finalization-eligible), red (a fail), or
  blocked (a blocked item with a reason).

### Conventions

Refusal statuses are typed and carry a legal `next_action`; the certification result binds
the exact memory tree and plan digest through the closed models.

### Invariants And Boundaries

- Certification never mutates code or memory.
- A green result requires a fully passing catalog, assembled Gate-5 inputs, a current coherence
  record, and the exact reused green Gate 1-4 prefix; anything less is red or blocked and never
  finalization-eligible.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact authority bundle the certification may read. | `FinalCertificationEvidence` | mcp/src/agents_remember/memory_quality/final_certification/certify.py:42-56 |
| Runs the complete Gate-5 protocol and publishes green/red/blocked. | `certify_final_full_memory_coherence` | mcp/src/agents_remember/memory_quality/final_certification/certify.py:59-134 |
| The affected-closure item stays blocked until the full-only rerun is consumed. | `_affected_closure_status` | mcp/src/agents_remember/memory_quality/final_certification/certify.py:137-141 |
| The typed refusal helper. | `_refuse` | mcp/src/agents_remember/memory_quality/final_certification/certify.py:144-145 |

## Update History

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 executable final full memory-coherence certification
  module delivered in code commit 16d1a4d6; anchors and ranges derived from the current
  worktree source and pinned to that commit.
