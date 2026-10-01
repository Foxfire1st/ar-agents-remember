# mcp/tests/test_conversation_active_service.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Conversation projector ordering, native-history merge and gap behavior.

## Code Commentary

### Logic

A scripted bridge exercises stable IDs and ordinals, settled-turn deduplication even with disjoint native IDs, prior-session history and older paging. Epoch changes and regressed evidence tips refuse. Split results remain ordered across polls, and pending zipper frames make total_items unknown without inventing an older cursor.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Pending newer content is not older history. Native re-walks must not duplicate settled turns; retained assertions are projection behavior rather than wire-level harness execution.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Hydration orders items and mints stable ids. [1]
- Settled live turns project once when native ids disjoint. [2]
- Prior session native history survives live turns. [3]
- Native page hydration and older paging. [4]
- Gap on epoch flip. [5]
- Zipper handles split result across polls. [6]
- Page never claims completeness while frames pend. [7]
- Regressed evidence tip gaps instead of freezing. [8]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
