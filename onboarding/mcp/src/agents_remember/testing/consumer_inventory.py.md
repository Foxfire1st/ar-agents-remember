# mcp/src/agents_remember/testing/consumer_inventory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/consumer_inventory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Enumerates every acceptance edge that could otherwise accidentally consume direct diagnostic
evidence.

## Code Commentary

`ACCEPTING_CONSUMER_INVENTORY` maps coverage, quality, retry, route review, lifecycle, closeout, and
integration to their owner, current evidence shape, candidate proof, reachability, and enforcement.
Tests compare it to the closed `EvidenceConsumer` vocabulary.

## Invariants And Boundaries

- Every consumer except local feedback appears exactly once.
- `direct_route_reachable` remains false for all accepting consumers.
- New acceptance consumers must extend both the model enum and this forcing inventory.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The complete accepting-consumer inventory is explicit. | `ACCEPTING_CONSUMER_INVENTORY` | mcp/src/agents_remember/testing/consumer_inventory.py:22-79 |

## Update History

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
