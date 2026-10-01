# mcp/tests/test_codex_adapter_thread_demux.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Async observation helpers for Codex adapter consumers.

## Code Commentary

### Logic

eventually yields for a bounded number of turns before failing; live_snapshot requires a real current adapter snapshot; agent_registry reads the registry from that snapshot. An AnyIO fixture selects asyncio. No demultiplexing or queue tests remain in this file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Comments about historical matrices are not retained protection. These helpers observe a live test adapter without starting a vendor process themselves.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Eventually. [1]
- Live snapshot. [2]
- Agent registry. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
