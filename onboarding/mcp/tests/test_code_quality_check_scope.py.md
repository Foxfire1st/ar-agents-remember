# mcp/tests/test_code_quality_check_scope.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Explicit product/verification package ownership tests.

## Code Commentary

### Logic

A newly importable support package refuses until assigned a product or verification owner. Declaring it verification preserves lint/type inclusion while excluding it from product coverage paths. Overlapping and stale ownership declarations refuse.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Coverage paths describe measurement scope, not a percentage requirement. No fallback ownership broadening is allowed for unowned packages.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- New importable package requires explicit product or verification owner. [1]
- Package authority rejects overlap and stale declarations. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
