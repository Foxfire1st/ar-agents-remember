# curator_scope.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Validate the curator-authored semantic scope carried into an invariant revision.

## Code Commentary

### Logic

read_curator_scope accepts exactly applicability, conditions and exclusions. Applicability must be nonblank text within the revision prose limit; both clause fields must be lists of nonblank strings. Empty lists explicitly record that the curator examined the boundary and found no clauses. CuratorScope carries normalized text into the existing invariant model fields.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

Missing or malformed scope is unfinished curation, not a workflow sentence or default applicability. This helper changes no database schema and migrates no historical record.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

No configured domain source could be checked.

### Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

- `CuratorScope` owns the behavior described above. [1]
- `read_curator_scope` owns the behavior described above. [2]

### Cross-Repo References

No independent cross-repository interface is introduced by this source.

No additional cross-repository evidence is required.
