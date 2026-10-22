# mcp/src/agents_remember/cli/developer_delivery.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Adapts filed developer messages to the existing native host send/held lane.

## Code Commentary

### Logic

Uses the developer channel key, existing recipient launch state and held FIFO; holds busy/permission/start cases, resumes only eligible existing closed seats, and returns its own held ID or named refusal/end.

### Invariants And Boundaries

No agent-role binding, second role or new public tool. Held is not delivery, and a refused or vanished recipient is not silently recreated.


**L184 — INV-4DQMNE, NEW-MESSAGE-WAITS-FOR-RESET.** Both the hold's answer and the queued branch are written here, which is where the reset was lost. Both the hold's answer and the queued branch are written here, which is where the reset was lost. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

- Adapts filed developer messages to the existing native host send/held lane. [1]
- Adapts filed developer messages to the existing native host send/held lane. [2]
- Adapts filed developer messages to the existing native host send/held lane. [3]
