# mcp/src/agents_remember/certification/certificate_models.py

## Governing Overview

[Certification contract overview](overview.md)

## Purpose

Immutable contracts for content-addressed closeout gate certificates: the admission semantic
envelope/manifest, the per-gate certificate semantic envelope with rail/artifact/evidence
inventories, the Gate-5 memory/coherence inputs, and the transactional finalization authority.
Every digest is re-verified at validation against the canonical semantic content (CCR-R21@v2).

## Code Commentary

### Logic

`CertificationAdmissionSemanticEnvelope` freezes repository, candidate Git tree, profile,
certification-plan/admitted-profile/registry digests, and exactly ordered Gates 1-5 admission
identities. `CertificationAdmissionManifest` binds the admission digest to that envelope and
keeps `CreationProvenance` (createdAt/producer/evidenceRef) outside semantic identity.

`GateCertificateSemanticEnvelope` carries gate, repository, candidate tree, admission/profile/
registry/gate-plan/gate-semantic digests, the exact earlier-gate predecessor prefix, canonical
semantic inputs, consumed artifacts, result-manifest digest, terminal disposition (literal
`green`), and sorted unique rail/artifact/evidence inventories; Gate 5 additionally binds
`GateFiveSemanticInputs` (memory tree, affected-closure plan, memory checker registry,
coherence subrecords, candidate-pair authority). `GateCertificate` verifies its certificate
digest against the envelope. `FinalizationSemanticEnvelope`/`FinalizationCertificateAuthority`
bind the exact green Gates 1-5 identities plus code/memory tree pair, admission, and the task-intent
and journal authorities; `FinalizationCurrentInputs` carries the mutable edges revalidated at
finalization.

### Invariants And Boundaries

- Candidate identity must be an exact Git tree.
- Predecessors are always the exact earlier-gate prefix; inventories are unique and canonically
  ordered.
- Only Gate 5 binds repository gate-plan digest absence (Gates 1-4 bind it present) and the
  memory/coherence inputs.
- Provenance is evidence only and never participates in digest identity.
- A certificate's terminal disposition is exactly `green`; nothing else is a certificate.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

- Certificate semantic envelopes bind the candidate inputs, predecessor prefix, inventories, and deterministic digest-bearing contracts. [1]

### Repo-Internal References

- Admission semantic inputs bind the exact code, memory and certification authorities. [2]
- The admission manifest binds its semantic envelope and content digest. [3]
- A gate certificate binds its semantic envelope and digest. [4]
- Certificate semantics bind candidate inputs, predecessor prefix and evidence inventories. [5]
- Gate 5 binds the memory/coherence inputs only. [6]
- Finalization authority bundles the selected certificates and their current input authorities. [7]
- Exact mutable-edge authorities revalidated by transactional finalization. [8]
- Semantic inputs must use canonical ordering. [9]
- Evidence inventory must use canonical ordering and valid identities. [10]

### Cross-Repo References

None; this is the repository-neutral certificate contract.
