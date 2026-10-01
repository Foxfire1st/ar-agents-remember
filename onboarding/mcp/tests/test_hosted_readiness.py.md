# mcp/tests/test_hosted_readiness.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Exact adapter-handshake hosted readiness.

## Code Commentary

### Logic

A matching structured handshake is ready without pane probing. Ready control with non-accepting submission state remains not-ready. Waiting obeys its deadline; a catalog identity change during adapter read becomes unknown-session.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Pane appearance is diagnostic only and cannot establish readiness. A readiness observation must remain tied to the same exact catalog generation.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Exact adapter handshake is ready and pane probes are diagnostic only. [1]
- Ready control without acceptance is not ready. [2]
- Not ready wait is bounded. [3]
- Exact identity change during adapter read is unknown. [4]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
