# mcp/test_support/agents_remember_test_support/testing/consumer_inventory.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Enumerates every acceptance edge that could otherwise consume evidence from the wrong authority.

## Code Commentary

`ACCEPTING_CONSUMER_INVENTORY` maps coverage, quality, retry, route review, lifecycle, closeout, and
integration to their owner, current evidence shape, candidate proof, reachability, and enforcement.
Tests compare it to the closed `EvidenceConsumer` vocabulary.

The coverage owner is `quality_plan._pytest_step`: command construction moved out of the stable
`check` execution facade during the file-size responsibility split. The inventory names the real
owner rather than preserving a compatibility fiction. That ownership move does not change the
Dagger-only evidence boundary or create another consumer.

## Invariants And Boundaries

- Every consumer except local feedback appears exactly once.
- `direct_route_reachable` remains false for all accepting consumers.
- New acceptance consumers must extend both the model enum and this forcing inventory.

## Evidence

### Repo-Internal References

- The complete accepting-consumer inventory is explicit. [1]
