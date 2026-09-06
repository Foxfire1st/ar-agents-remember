# Shared Certification Wire Models

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/certification/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T14:48:58+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Parent overview](../overview.md)

## What This Area Is

The common value layer for certification and lifecycle owners. It centralizes wire validation while leaving registry compilation, certificate storage, semantic admission and journal mutation with their domain owners.

## Hot Path Summary

Start with `base.py` for frozen models and rail identity, `corrective.py` for exact prior-red repair shapes, and `references.py` for semantic-address versus exact-byte binding. The initializer performs no registration.

## Local Invariants And Traps

- Shared wire constraints do not prove observed currentness or grant execution authority.
- Corrective declarations require comparison with actual before/after inputs and prior failed/blocked results.
- Stored references retain original provenance through a separate byte digest; they are not a latest-object lookup.

## File-Level Onboarding Map

| Source File | Onboarding | Role |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | Documentation-only namespace |
| `base.py` | [base.py.md](base.py.md) | Frozen model, gate and rail primitives |
| `corrective.py` | [corrective.py.md](corrective.py.md) | Canonical direct/root repair dispositions |
| `references.py` | [references.py.md](references.py.md) | Exact stored object references |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared identity and base carry only closed wire constraints. | `FrozenContractModel`; `RailIdentity` | mcp/src/agents_remember/models/certification/base.py:30-33; mcp/src/agents_remember/models/certification/base.py:36-42 |
| Corrective shape requires actual digest movement and canonical entries. | `CorrectiveInputChange`; `RedCatalogDisposition` | mcp/src/agents_remember/models/certification/corrective.py:22-38; mcp/src/agents_remember/models/certification/corrective.py:41-70 |
| Exact original bytes are bound separately from semantic address. | `CertificateObjectReference` | mcp/src/agents_remember/models/certification/references.py:24-39 |

## Docs And Cross-Repo References

The configured Domain Documentation registry has no entries. These source-owned models and transitions introduce no cross-repository protocol.

## Update History

- 2026-09-06T14:48:58+00:00 — Created this nearest route from source at `c69d5171187fa1957025e393270db9f5a864ab14`. Preserved domain/store authority outside the wire/transition package; source review is not gate or acceptance evidence.
