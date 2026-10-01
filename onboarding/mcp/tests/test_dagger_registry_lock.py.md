# mcp/tests/test_dagger_registry_lock.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Host Dagger registry locking composed with checkout coordinator isolation.

## Code Commentary

### Logic

An undeclared linked-checkout caller admits and releases an exact host owner while live coordination writes still refuse before parent creation. Nested exception paths retain exclusion until the outer release; independent threads and processes verify the physical lock remains held and is later released.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Host registry permission does not grant coordinator permission or declare a process identity. Tests use temporary authority roots and an inspector double, not a new Dagger engine.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Host admission keeps undeclared checkout coordinator writes refused. [1]
- Registry nested exception retains then releases thread and process exclusion. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
