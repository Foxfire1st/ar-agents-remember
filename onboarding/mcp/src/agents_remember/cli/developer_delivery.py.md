# mcp/src/agents_remember/cli/developer_delivery.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Adapts filed developer messages to the existing native host send/held lane.

## Code Commentary

### Logic

Uses the developer channel key, existing recipient launch state and held FIFO; holds busy/permission/start/limited cases through `held_reset_delivery.hold_at_receipt` inside `open_held_store(ref)`, resumes only eligible existing closed seats, and returns its own held ID or named refusal/end.

### Invariants And Boundaries

No agent-role binding, second role or new public tool. Held is not delivery, and a refused or vanished recipient is not silently recreated.

When holding a provider-limited developer send, `_hold` carries `limited_until` into `hold_at_receipt` (publishing any known reset to `HeldResetIndex` before the held store write and recording the held receipt) and preserves the same reset time on the returned held answer.

## Evidence

- Adapts filed developer messages to the existing native host send/held lane. [1]


- Adapts filed developer messages to the existing native host send/held lane. [2]


- Adapts filed developer messages to the existing native host send/held lane. [3]
