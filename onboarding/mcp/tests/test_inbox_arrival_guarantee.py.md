# mcp/tests/test_inbox_arrival_guarantee.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Scoped terminal-seat builder shared by inbox consumers.

## Code Commentary

### Logic

_seat creates a TerminalCatalogEntry from caller-supplied identity and task scope. This module now supplies the row fixture used by delivery tests and contains no retained arrival-guarantee test methods.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The old 25-case arrival, expiry and watcher matrix is historical. A fixture row does not prove that any command arrived or that a retry is authorized.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Seat. [1]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
