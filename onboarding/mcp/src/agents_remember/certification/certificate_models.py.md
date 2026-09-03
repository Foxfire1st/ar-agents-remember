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
| Admission envelope/manifest freezes the exact dual-authority inputs. | `CertificationAdmissionSemanticEnvelope`; `CertificationAdmissionManifest` | mcp/src/agents_remember/certification/certificate_models.py:60-76; mcp/src/agents_remember/certification/certificate_models.py:87-99 |
| The gate certificate binds semantic inputs, predecessor prefix, inventories, and digest. | `GateCertificate`; `GateCertificateSemanticEnvelope` | mcp/src/agents_remember/certification/certificate_models.py:221-238; mcp/src/agents_remember/certification/certificate_models.py:184-218 |
| Gate 5 binds the memory/coherence inputs only. | `GateFiveSemanticInputs` | mcp/src/agents_remember/certification/certificate_models.py:152-174 |
| Finalization authority revalidates current certificates plus intent/journal authorities. | `FinalizationCertificateAuthority`; `FinalizationCurrentInputs` | mcp/src/agents_remember/certification/certificate_models.py:269-281; mcp/src/agents_remember/certification/certificate_models.py:261-267 |
| Canonical ordering and inventory validators are shared. | `_require_canonical_inputs`; `_require_canonical_inventory` | mcp/src/agents_remember/certification/certificate_models.py:284-287; mcp/src/agents_remember/certification/certificate_models.py:290-312 |

## Cross-Repo References

None; this is the repository-neutral certificate contract.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): created the card for the new
  certificate contract models (admission, gate certificate, Gate-5 inputs, finalization
  authority) with their digest-verified envelopes. Verification is pinned to the owning commit.
