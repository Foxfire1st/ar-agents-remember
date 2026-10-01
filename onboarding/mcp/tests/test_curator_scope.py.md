# test_curator_scope.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Curator scope admission, storage and retry behavior.

## Code Commentary

### Logic

The tests drive real ingest, check semantic applicability/conditions/exclusions on readback, preserve the exact retry identity, and refuse changed scope under an allocated key or missing/malformed scope before invariant writes.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

Tests are scoped executable evidence. They do not certify the mounted product journey, whole-repository quality or semantic acceptance.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

No configured domain source could be checked.

### Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

- `test_authored_scope_survives_ingest_and_scope_change_is_not_an_exact_retry` owns the behavior described above. [1]

### Cross-Repo References

No independent cross-repository interface is introduced by this source.

No additional cross-repository evidence is required.
