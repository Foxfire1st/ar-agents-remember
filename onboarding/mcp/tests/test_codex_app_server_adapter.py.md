# mcp/tests/test_codex_app_server_adapter.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Fake Codex transport, pinned protocol fixture and async event helpers.

## Code Commentary

### Logic

FakeCodexTransport records requests and deep-copies queued results and incoming frames; BlockingTurnStartTransport exposes the before-write and response window. Builders create launch/request identities and prime startup. make_adapter accepts the production settings value, and event helpers wait for specific frames or verify already-settled notifications are inert.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

This support-only module contains no retained conformance test methods. The pinned protocol JSON is fixture data, not a production version selector or static fallback catalog.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Fakecodextransport. [1]
- Blockingturnstarttransport. [2]
- Fixture. [3]
- Fixture object. [4]
- Fixture list. [5]
- Add model. [6]
- Identity. [7]
- Launch. [8]
- Request. [9]
- Prime start. [10]
- Make adapter. [11]
- Settle. [12]
- Drain events. [13]
- Assert notification is inert. [14]
- Next event of kind. [15]
- Turn start result. [16]
- Turn completed notification. [17]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
