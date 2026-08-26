# mcp/src/agents_remember/testing/consumer_inventory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/consumer_inventory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed owner-string relocations for quality and lifecycle consumers; the closed accepting-consumer inventory and evidence reachability rules are unchanged.
- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
