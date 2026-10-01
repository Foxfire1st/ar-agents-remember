# mcp/tests/test_codex_adapter_thread_routing_and_registry.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Codex seat policy and thread-identity routing tests.

## Code Commentary

### Logic

Unset policies are omitted from turn/start; configured sandbox mappings become copied JSON data. An unsolicited turn/started on the seat thread makes it busy and blocks preflight. A sub-agent settings frame crosses as raw evidence without changing the seat, while identical drift on the seat thread fails the bridge.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Thread identity, not payload shape, determines settings authority. The removed partial-collab registry tests must not be described as current coverage here.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Turn start sends only the policies the seat configured. [1]
- A turn the seat did not dispatch still makes it busy. [2]
- A sub agents settings frame is evidence not the seats settings. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
