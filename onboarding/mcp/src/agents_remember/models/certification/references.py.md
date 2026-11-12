# mcp/src/agents_remember/models/certification/references.py

## Governing Overview

[Package overview](overview.md)

## Purpose

Owns the typed reference to exact canonical certificate-store bytes, including their original provenance.

## Code Commentary

### Logic

`CertificateObjectKind` names the nine supported object families. `CertificateObjectReference` separates the semantic digest that selects the kind/address from the SHA-256 and positive strict integer size that bind the complete stored representation. The versioned shape rejects unknown fields and is frozen through the shared base.

### Conventions

Use the existing store to produce and reopen references. A semantic digest alone does not replace the byte binding when creation evidence or provenance differs.

### Invariants And Boundaries

- The schema bounds size to 10,000,000,000 bytes; the actual store still enforces its own publication/readback limits.
- A reference carries no store location, journal owner, gate execution or lifecycle-selection authority.
- Equal semantic identity does not authorize overwriting different original stored bytes.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry has no entries. This repository-owned contract is established by the source below.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- Object family membership is closed. [1]
- The reference binds address identity separately from exact bytes and size. [2]

### Cross-Repo References

No cross-repository implementation boundary is owned here.


No separately configured cross-repository source is used for this card.

## L34 Current Implementation

The closed reference vocabulary includes preparation-intent and prepared-output. A reference binds semantic digest, exact canonical content hash and size; possession of a reference does not select a lifecycle output.

- `CertificateObjectReference` owns the corresponding behavior described above. [3]
