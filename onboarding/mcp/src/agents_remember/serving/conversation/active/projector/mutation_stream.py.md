# mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Owns canonical projection mutation, event cursor minting, bounded retention, and subscriber
fan-out.

## Code Commentary

### Logic

`ProjectionMutationStream` applies mapper outputs to one `ProjectionStore`, translates store
mutations into public mutations, and mints the sequence/cursor/event-id chain. It retains at most
1,000 envelopes and gives each subscriber a 256-entry queue. A full queue is removed from normal
fan-out and receives one retained `retention-overflow` gap followed by the close sentinel; the
shared stream continues for healthy consumers.

### Conventions

Only this component increments event sequence or writes subscriber queues. Reset is for a rebuild;
release additionally discards the heavy projection while preserving the retired shell's identity.

### Invariants And Boundaries

- Event sequences and cursor predecessor links are gap-free and generation-scoped.
- A slow subscriber cannot block or terminate other subscribers.
- Overflow and explicit gaps are public mutations, retained before delivery.
- Raw mapper output never bypasses the canonical store.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Canonical item/revision behavior. | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| Gap and overflow regressions. | [test_conversation_active_service.py](agents-remember/mcp/tests/test_conversation_active_service.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the mutation-stream
  sidecar and recorded its explicit retention and subscriber bounds. Verification metadata
  remains blank until commit.
