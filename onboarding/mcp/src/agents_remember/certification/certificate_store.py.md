# mcp/src/agents_remember/certification/certificate_store.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

- The R21 packet requires atomic content-addressed storage and exact-reference lookup. [1]

### Repo-Internal References

- Publish/load are digest-addressed with collision and readback checks. [2]
- The store checks bounded capacity before accepting another object. [3]
- Capacity refusal exposes the store policy and reclamation boundary. [4]
- Stored object bytes use canonical serialization. [5]
- The store resolves the object digest by certificate object kind. [6]
- Only safe readable regular files are accepted. [7]

### Cross-Repo References

None; this is the repository-neutral content-addressed store.

## L34 Current Implementation

The closed store dispatch now also owns preparation-intent and prepared-output objects. Generic typed publish/load and exact reference readback preserve canonical bytes, original provenance, existing locking and capacity bounds; there is no separate preparation store.

- `CertificateStorePolicy` owns the corresponding behavior described above. [8]
- `ContentAddressedCertificateStore` owns the corresponding behavior described above. [9]
- `_object_digest` owns the corresponding behavior described above. [10]
- `_read_regular_file` owns the corresponding behavior described above. [11]
- `_capacity_error` owns the corresponding behavior described above. [12]
- `_raise` owns the corresponding behavior described above. [13]
