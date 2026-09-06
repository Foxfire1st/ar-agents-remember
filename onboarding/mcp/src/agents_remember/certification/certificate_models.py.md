# mcp/src/agents_remember/certification/certificate_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/certificate_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | 6f10c24d72db6171c0d434b307e6806996e2f11d |
| lastVerifiedCommitDate | 2026-09-02T18:10:52+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R21 packet requires the certificate envelope, direct predecessors, inventories, and deterministic semantic digest. | "Required Certificate Envelope"; "Deterministic digest over the canonical semantic envelope" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R21-v2-content-addressed-phase-certificates.md:24-37 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Admission semantic inputs bind the exact code, memory and certification authorities. | "class CertificationAdmissionSemanticEnvelope" | mcp/src/agents_remember/certification/certificate_models.py:58-74 |
| The admission manifest binds its semantic envelope and content digest. | "class CertificationAdmissionManifest" | mcp/src/agents_remember/certification/certificate_models.py:85-97 |
| A gate certificate binds its semantic envelope and digest. | "class GateCertificate" | mcp/src/agents_remember/certification/certificate_models.py:219-236 |
| Certificate semantics bind candidate inputs, predecessor prefix and evidence inventories. | "class GateCertificateSemanticEnvelope" | mcp/src/agents_remember/certification/certificate_models.py:182-216 |
| Gate 5 binds the memory/coherence inputs only. | `GateFiveSemanticInputs` | mcp/src/agents_remember/certification/certificate_models.py:150-172 |
| Finalization authority bundles the selected certificates and their current input authorities. | "class FinalizationCertificateAuthority" | mcp/src/agents_remember/certification/certificate_models.py:267-279 |
| Exact mutable-edge authorities revalidated by transactional finalization. | "class FinalizationCurrentInputs" | mcp/src/agents_remember/certification/certificate_models.py:259-264 |
| Semantic inputs must use canonical ordering. | "def _require_canonical_inputs" | mcp/src/agents_remember/certification/certificate_models.py:282-285 |
| Evidence inventory must use canonical ordering and valid identities. | "def _require_canonical_inventory" | mcp/src/agents_remember/certification/certificate_models.py:288-310 |

## Cross-Repo References

None; this is the repository-neutral certificate contract.

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `GateFiveSemanticInputs` repointed to mcp/src/agents_remember/certification/certificate_models.py:150-172. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): created the card for the new
  certificate contract models (admission, gate certificate, Gate-5 inputs, finalization
  authority) with their digest-verified envelopes. Verification is pinned to the owning commit.
