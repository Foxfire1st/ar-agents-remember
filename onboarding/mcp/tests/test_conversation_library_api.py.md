# mcp/tests/test_conversation_library_api.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Conversation-library list and idempotent open contracts over ASGI.

## Code Commentary

### Logic

The real route composition validates wire scope and returns a signed conversation key, identity digest and capabilities. Escaped scopes refuse with 403 and an unknown harness with 404. A created open result binds the proven vendor/bridge identity; exact replay reuses it without reopening, while changed input conflicts.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Native ports, opener, proof and retirement are doubled. These three retained tests do not establish the historical read/status/reconcile matrix or an installed-runtime integration.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- List route returns wire page and authorizes scope. [1]
- List route rejects scope escapes and unknown harness. [2]
- Open created replays and focuses only proven identity. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
