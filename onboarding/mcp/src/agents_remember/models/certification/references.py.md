# mcp/src/agents_remember/models/certification/references.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/certification/references.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:03:08+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
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
## Update History

- 2026-09-06T15:03:08+00:00 — Added explicit not-applicable Docs/Cross-Repo reference rows required by the file-card template; source claims, verification stamps and all earlier history are unchanged.


- 2026-09-06T14:48:58+00:00 — Created from source at `c69d5171187fa1957025e393270db9f5a864ab14` for the shared wire/generation ownership split. Verification records source review, not gate execution or acceptance.
