# mcp/src/agents_remember/certification/final_certification_models.py

## Governing Overview

[memory_quality overview](overview.md)

## Purpose

Closed, frozen item contracts used by the memory-domain catalog: `FinalItemStatus`, `FinalCatalogItemIdentity` and `FinalCatalogItemResult`. The base forbids extra fields and mutation. Item identity is not execution evidence, and an item result does not establish an exhaustive final-catalog attestation or finalization eligibility.

## Code Commentary

### Logic

Module-level surface:

- `FinalItemStatus` is pass/fail/blocked/not-applicable.
- `FinalCertificationModel` is the frozen, extra-forbid base.
- `FinalCatalogItemIdentity` validates item ID and semver version and exposes their tuple key.
- `FinalCatalogItemResult` bounds finding count, digest spelling, blockers and optional reference; blocked status requires nonempty blockers, while pass and not-applicable forbid findings.

The plan, full attestation, final certification-state/result and shared canonical-order guard were removed rather than moved into another item model.

### Conventions

Digest spelling is `^[0-9a-f]{64}$`; item IDs and semver versions have their own module patterns. The retained status-shape validator raises `ValueError` for invalid blocked/pass/not-applicable combinations.

### Invariants And Boundaries

- Models are closed and frozen: no extra fields and no mutation after construction.
- Item identities do not prove execution.
- The surviving item models do not enforce whole-catalog exhaustiveness or green-only finalization eligibility.

### Todos

None.

## Evidence

### Repo-Internal References


- One closed final-catalog member with a canonical key. [2]
- One typed Gate-5 result with content-addressed subresult and status shape guard. [3]


- The item status vocabulary is pass/fail/blocked/not-applicable; the whole-certification state model was removed. [1]
