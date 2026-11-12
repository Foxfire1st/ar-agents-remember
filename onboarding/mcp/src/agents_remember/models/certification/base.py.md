# mcp/src/agents_remember/models/certification/base.py

## Governing Overview

[Package overview](overview.md)

## Purpose

Owns the closed frozen wire primitives shared by certification-domain and lifecycle models.

## Code Commentary

### Logic

`GateId` fixes the five gate identifiers. `SemanticText` rejects blank or padded text. `FrozenContractModel` forbids extra fields and freezes model assignment; `RailIdentity` constrains its identifier and semantic version and derives the `railId@version` key.

### Conventions

These are shared value constraints. Registry, plan, result, admission and journal owners import them directly instead of maintaining parallel model bases.

### Invariants And Boundaries

- A valid rail identity does not establish registry membership, applicability or execution success.
- The module validates wire shape; semantic digests and owner currentness are established by the consuming domain owners.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry has no entries. This repository-owned contract is established by the source below.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- Gate identifiers are closed to the five gates. [1]
- Semantic text rejects blank and padded values. [2]
- The shared model base rejects extra fields and freezes model assignment. [3]
- Rail identities validate identifier/version shape and derive a stable key. [4]

### Cross-Repo References

No cross-repository implementation boundary is owned here.


No separately configured cross-repository source is used for this card.
