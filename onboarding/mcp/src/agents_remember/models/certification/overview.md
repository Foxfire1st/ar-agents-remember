# Shared Certification Wire Models

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/models/certification/` |

## Governing Overview

[Parent overview](../overview.md)

## Purpose

This directory supplies the common value layer for certification and lifecycle owners. It centralizes wire validation while leaving registry compilation, certificate storage, semantic admission and journal mutation with their domain owners. Its initializer is a documentation-only namespace and performs no registration.

## Hot Path Summary

Start with `base.py` for frozen models and rail identity, `corrective.py` for direct-repair and repaired-root declarations, and `references.py` for semantic-address versus exact-byte binding.

## How It Is Built

`FrozenContractModel` forbids extra fields and freezes model instances. The base module also defines gate IDs, nonblank and unpadded semantic text, and rail identities with constrained identifiers and semantic versions. A rail's key combines its identifier and version.

`CorrectiveInputChange` names an exact semantic input and requires distinct before and after digests. `RedCatalogDisposition` binds a declaration to a failed or blocked rail result and its corrective owner. A direct repair requires changed inputs and forbids a repaired root; a repaired-root declaration requires a root and forbids changed inputs. Changed inputs must be unique by input kind and identifier and canonically ordered.

`CertificateObjectReference` carries a closed object kind and schema version, a semantic digest selecting the object's address, and a separate SHA-256 digest and size binding its complete canonical stored representation, including original creation evidence.

| Source File | Onboarding | Role |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | Documentation-only namespace |
| `base.py` | [base.py.md](base.py.md) | Frozen model, gate and rail primitives |
| `corrective.py` | [corrective.py.md](corrective.py.md) | Canonical direct/root repair dispositions |
| `references.py` | [references.py.md](references.py.md) | Exact stored object references |

## Invariants And Boundaries

Shared wire constraints do not prove observed currentness or grant execution authority. Distinct declared digests establish a valid change shape; lifecycle admission must still compare them with actual prior and successor inputs and bind the disposition to the exact prior failed or blocked result. A repaired-root declaration also requires admission checks against the actual blocking relationship and direct repair.

Stored references retain original provenance through their separate byte digest and size. They select an exact semantic address rather than the latest object. Store location and lifecycle selection remain the caller's responsibility; a reference confers no journal or execution authority.

These source-owned models and transitions introduce no cross-repository protocol. The configured Domain Documentation registry has no entries.

## Evidence

- The shared identity and base carry only closed wire constraints. [1]
- Corrective shape requires distinct declared before/after digests and canonical entries; actual input movement is checked separately by lifecycle admission. [2]
- Exact original bytes are bound separately from semantic address. [3]
