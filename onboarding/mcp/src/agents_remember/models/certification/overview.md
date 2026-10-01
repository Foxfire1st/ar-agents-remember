# Shared Certification Wire Models

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/models/certification/` |

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

## Evidence

### Repo-Internal References

- The shared identity and base carry only closed wire constraints. [1]
- Corrective shape requires actual digest movement and canonical entries. [2]
- Exact original bytes are bound separately from semantic address. [3]

### Docs And Cross-Repo References

The configured Domain Documentation registry has no entries. These source-owned models and transitions introduce no cross-repository protocol.
