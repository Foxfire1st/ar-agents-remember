# mcp/src/agents_remember/serving/conversation/active/projector/facade.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/facade.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Provides the small public `ActiveSessionProjector` facade for one exact session and bridge epoch.

## Code Commentary

### Logic

The constructor composes the mutation stream, agent authority, native and echo ingestion,
selected-child history, interaction projection, and rebuild coordinator around one shared apply
lock. Public page, subscription, retained-event, poll, and child-refresh methods delegate to those
owners. The consumer-driven poll task maps epoch loss and ordering failures to typed gaps, tolerates
only a bounded run of control-read failures, and releases the component graph after its consumer
TTL.

### Conventions

Blocking control reads remain inside the components and execute through `asyncio.to_thread`.
The facade coordinates lifecycle; it does not duplicate component state.

### Invariants And Boundaries

- `matches` requires session id, bridge epoch, vendor conversation id, and a live facade.
- Polling begins only when the event loop and a consumer exist.
- Close cancels polling and child-history work before closing subscribers.
- Dormant release retires the facade and frees every component's retained projection state.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The active service owns facade registration and replacement. | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/service.py) |
| Coordinator and stream implement the delegated work. | [rebuild_coordinator.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py), [mutation_stream.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the facade ownership
  record after the projector decomposition. Verification metadata remains blank until commit.
