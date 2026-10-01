# mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py

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

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Canonical item/revision behavior. [1]


### Cross-Repo References

No meaningful cross-repository references found.
