# mcp/src/agents_remember/models/certification/corrective.py

## Governing Overview

[Package overview](overview.md)

## Purpose

Owns typed corrective dispositions carried across lifecycle admission boundaries.

## Code Commentary

### Logic

`CorrectiveInputChange` names one semantic input and requires distinct before/after digests. `RedCatalogDisposition` binds one failed or blocked rail, its exact prior result digest and corrective owner. Direct repair requires changed inputs without a repaired root; repaired-root disposition requires its root and no changed inputs. Changed inputs must be uniquely keyed and canonically sorted.

### Conventions

Input digests accept Git-width SHA-1 or SHA-256 values; the prior-result digest is SHA-256. Identifiers and rationale retain the shared unpadded semantic-text contract.

### Invariants And Boundaries

- Constructor validity does not prove that an input changed in the repository or that the named root repairs a failed rail. Admission compares dispositions with owner-produced observations and the complete prior-red catalog.
- Admission decides whether corrective evidence clears a prior failure. The wire shape separately rejects a second representation of the same input key.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry has no entries. This repository-owned contract is established by the source below.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- The disposition kinds are a closed vocabulary. [1]
- Each corrective input must move an exact semantic identity. [2]
- Direct/root shape, unique keys and canonical ordering are enforced together. [3]

### Cross-Repo References

No cross-repository implementation boundary is owned here.


No separately configured cross-repository source is used for this card.
