# mcp/tests/test_conversation_library_cursor.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Conversation-library cursor purpose and canonical scope authority.

## Code Commentary

### Logic

List and read tokens round-trip their exact purpose, scope and continuation position. Tampered tokens and wrong-purpose reuse refuse. Canonical scope rejects traversal, symlink escape and cross-scope widening.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A signed continuation is not permission to widen its bound project scope. Retained tests exercise repository-owned token contracts rather than an external conversation provider.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- List cursor round trip and tamper rejection. [1]
- Read cursor round trip and wrong purpose rejection. [2]
- Canonical scope rejects traversal symlink and cross scope. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
