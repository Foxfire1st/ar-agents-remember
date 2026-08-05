# mcp/src/agents_remember/serving/conversation/active/projector/facade.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/facade.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The active service owns facade registration and replacement. | `ActiveConversationService`; `_projector_for_locked` | mcp/src/agents_remember/serving/conversation/active/service.py:57-259 |
| Coordinator and stream implement the delegated work. | `RebuildCoordinator`; `ProjectionMutationStream` | mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py:49-197; mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py:63-192 |

## Cross-Repo References

No meaningful cross-repository references found.

## 260731-EFA-L2 Current Delta

**`ProjectedSession`** (`identity`, `authorization`, `entry`, `mapper`, `secret`) is the facade's
new single argument: WHICH conversation is being projected, and the authority to mint references
for it. The identity names the exact session and bridge epoch; the controlled session is the row
those reads go through; the mapper is that harness's shape reader; the authorization and signing
secret are what every emitted reference is bound to. A projector built from a mixed set would
publish one session's events under another's references, so the five arrive as one value.

Internally the facade now builds the two bundles in [wiring.py](wiring.py.md) — one
`SessionProjectionSpine` and one `BridgeReaders` — and hands the SAME pair to every ingestion
component, plus an `IngestionComponents` set to the rebuild coordinator. That is what makes "one
projection, one session, one epoch" structural instead of a convention repeated across five
parameter lists.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 4 citation findings for the active service, rebuild coordinator, and mutation stream ownership rows.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `ProjectedSession` and the spine/readers bundles the facade now builds and shares across every ingestion component.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the facade ownership
  record after the projector decomposition. Verification metadata remains blank until commit.
