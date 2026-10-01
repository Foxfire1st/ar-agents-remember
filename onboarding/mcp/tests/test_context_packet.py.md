# test_context_packet.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Allowed-repository context packet and freshness reporting tests.

## Code Commentary

### Logic

The packet exposes versioned nested repo/memory/worktree/provider facts, publishes provider diagnostics without raw state, and leaves drift unchecked unless requested. Unknown repository IDs refuse before filesystem resolution. A real remote-branch fixture reports code lag and exact ledger mapping.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Unavailable providers do not become fabricated healthy state. The retained tests do not prove every optional packet field or inline-memory variant.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Builds packet from allowed repo. [1]
- Rejects unknown repo before filesystem resolution. [2]
- Freshness reports behind code branch and ledger mapping. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
