# mcp/src/agents_remember/models/certification/references.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/certification/references.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The configured Domain Documentation registry has no entries. This repository-owned contract is established by the source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Object family membership is closed. | `CertificateObjectKind` | mcp/src/agents_remember/models/certification/references.py:11-21 |
| The reference binds address identity separately from exact bytes and size. | `CertificateObjectReference` | mcp/src/agents_remember/models/certification/references.py:24-39 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |

## L34 Current Implementation

The closed reference vocabulary includes preparation-intent and prepared-output. A reference binds semantic digest, exact canonical content hash and size; possession of a reference does not select a lifecycle output.

| Finding | Anchor | Source |
| --- | --- | --- |
| `CertificateObjectReference` owns the corresponding behavior described above. | `CertificateObjectReference` | `mcp/src/agents_remember/models/certification/references.py:26-41` |

## Update History

### 2026-09-06T17:13:06+00:00 — L34 implementation memory

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

- 2026-09-06T15:03:08+00:00 — Added explicit not-applicable Docs/Cross-Repo reference rows required by the file-card template; source claims, verification stamps and all earlier history are unchanged.


- 2026-09-06T14:48:58+00:00 — Created from source at `c69d5171187fa1957025e393270db9f5a864ab14` for the shared wire/generation ownership split. Verification records source review, not gate execution or acceptance.
