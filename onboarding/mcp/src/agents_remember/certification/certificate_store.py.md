# mcp/src/agents_remember/certification/certificate_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/certificate_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | 6f10c24d72db6171c0d434b307e6806996e2f11d |
| lastVerifiedCommitDate | 2026-09-02T18:10:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification contract overview](overview.md)

## Purpose

Bounded atomic storage for exact content-addressed certification objects: admissions, result
manifests, certificates, and finalization authorities are published and loaded strictly by
digest with no latest-object lookup, no historical search, and capacity/reclamation policy
(CCR-R21@v2).

## Code Commentary

### Logic

`ContentAddressedCertificateStore` publishes objects under
`<root>/<kind>/sha256/<first-two>/<digest>.json` (`exact_path`). `_publish` writes
canonical JSON (compact separators, sorted keys, trailing newline) atomically via
`atomic_write_bytes`, refuses a content-address collision, and read-backs the exact bytes.
`_load` re-validates the model and refuses an address mismatch between stored bytes and the
requested digest. `_require_capacity` enforces operation-scoped object/byte maxima and demands
the declared `reclamationOwner` when exceeded; every object must be a readable regular file.

### Invariants And Boundaries

- Lookup is exact-digest only; there is no latest, newest-success, or historical path.
- Publication is atomic and read-back verified; a collision with different bytes refuses.
- Capacity is bounded per operation scope; reclamation is owned by the declared owner, never
  inferred or automatic.
- Stored objects are re-validated against their schema and digest on every load.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R21 packet requires atomic content-addressed storage and exact-reference lookup. | "Expected Implementation Evidence"; "Failure And Recovery" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R21-v2-content-addressed-phase-certificates.md:118-136 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Publish/load are digest-addressed with collision and readback checks. | `_publish`; `_load`; `exact_path` | mcp/src/agents_remember/certification/certificate_store.py:97-124; mcp/src/agents_remember/certification/certificate_store.py:126-153; mcp/src/agents_remember/certification/certificate_store.py:85-95 |
| Capacity is bounded and reclamation-owned. | `_require_capacity`; `_capacity_error` | mcp/src/agents_remember/certification/certificate_store.py:155-181; mcp/src/agents_remember/certification/certificate_store.py:225-234 |
| Canonical bytes and per-kind digests are the storage truth. | `_canonical_bytes`; `_object_digest` | mcp/src/agents_remember/certification/certificate_store.py:184-188; mcp/src/agents_remember/certification/certificate_store.py:191-198 |
| Only safe readable regular files are accepted. | `_read_regular_file` | mcp/src/agents_remember/certification/certificate_store.py:201-222 |

## Cross-Repo References

None; this is the repository-neutral content-addressed store.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): created the card for the new
  content-addressed certificate store (exact-digest publish/load, collision and readback refusal,
  bounded capacity with reclamation owner). Verification is pinned to the owning commit.
