# mcp/src/agents_remember/models/queue

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/models/queue` |

## Governing Overview

[models overview](../overview.md)

## Purpose

Owns the public status/rebuild request and response models for the disposable sprint scheduling projection. The projection answers which waiting candidates are schedulable from the exact canonical source; it is not the lifecycle journal.

## Hot Path Summary

`closeout_queue.py` declares the status/rebuild action vocabulary, the sprint-addressed request and the effective response. The response carries invalid-empty/valid-built service state, source classification and fingerprints, bounded source problems, waiting-generation members, first-ready identity and the next action.

## How It Is Built

The neutral member, source-problem and persisted projection-state vocabularies come from `models/closeout/projection.py`. Source census, member computation, projection publication and rebuild behavior live in `worktrees/queue/`; application/tool adapters compose the wire response rather than owning operation evidence.

The dashboard consumes its projected queue view, not an authority to mutate the lifecycle: `CloseoutQueue.tsx` reads the store's queues, optionally scopes them to a sprint and displays the service condition, source problems and member classifications. The response and dashboard projection types are distinct shapes, so the UI is not described as a direct parser of the MCP response.

## Invariants And Boundaries

- Keep the model vocabulary JSON-primary and strict; removed lifecycle fields are not compatibility inputs to these models.
- Invalid-empty projection state has no membership or accepted source identity. Valid-built state requires one exact source identity and classification and no unresolved source problems. A terminal valid-built projection is empty.
- Claims, workers, commits, certification, integration, cancellation, recovery and terminal execution evidence belong to door/journal owners. The wire member may identify its candidate tree and source-door fingerprint without acquiring authority for those operations.
- The projection is disposable and rebuildable; losing it must not lose operation evidence. Earlier lifecycle-shaped queue rows are not the current contract.

## Evidence

- Neutral projection state refuses contradictory membership, source identity or terminal state. [2]
- The dashboard renders store-projected queue classifications and problems, optionally scoped to a sprint. [3]

- Queue projection vocabulary. [1]
