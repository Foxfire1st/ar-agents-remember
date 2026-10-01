# mcp/tests/test_inbox_rebinding_mechanics.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Inbox transition idempotence, supersession and replacement delivery.

## Code Commentary

### Logic

Repeated terminal transitions append once. Ambiguous structural ownership refuses. A stale landing cannot overwrite concurrent supersession, and stale unresolved cannot overwrite landed truth. Superseding during actual in-flight delivery wins; a rebound row is sent to the current replacement in a subsequent sweep.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Folded durable state is the oracle. Task containment resolves structural ownership rather than guessed role mailboxes or stale spawn provenance.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Landed superseded unresolved expired and rebind are idempotent. [1]
- Ambiguous structural owner refuses instead of role mailbox guess. [2]
- Concurrent supersede survives a stale landing append. [3]
- Concurrent landed survives a stale unresolved. [4]
- Supersede during in flight delivery wins over landing. [5]
- Rebound row is delivered to replacement in next sweep. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
