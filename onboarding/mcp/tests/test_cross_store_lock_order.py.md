# mcp/tests/test_cross_store_lock_order.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Cross-store sweep concurrency and event-loop responsiveness.

## Code Commentary

### Logic

Two actual sweep paths share a catalog and inbox under a controlled rendezvous and must both finish without failures or lost observation. Separate async cases verify control entry resolution and terminal-image catalog/write work run on worker threads.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The motivating ABBA incident involved catalog-to-inbox versus inbox-to-catalog nesting. Daemon-thread watchdogs bound the failure; no fake immediate-success lock substitutes for the shared-store race.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Liveness sweep and agent notifier sweep do not abba deadlock. [1]
- Control resolve entry runs off the event loop. [2]
- Terminal image response offloads catalog read and write. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
