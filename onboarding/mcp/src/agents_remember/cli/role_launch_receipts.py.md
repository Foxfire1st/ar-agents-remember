# mcp/src/agents_remember/cli/role_launch_receipts.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns durable current-line launch receipts, immutable saved-call replay, report binding and public projection.

## Code Commentary

Receipt creation is exclusive and complete before native launch; unknown outcomes retain replayRequest with original UUID/prompt/options. Resolved receipts drop replayRequest. Taskless canonical storage/migration remains bounded to exact receipt identities; old schema at current address refuses, previous host receipts are not execution authority. Public execution whitelists lifecycle fields and requested/observed tier disclosure, never task acceptance.

## Evidence

- Frozen implementation of _execute_prepared_launch supporting the stated file behavior. [1]
- Frozen implementation of _create_receipt supporting the stated file behavior. [2]
- Frozen implementation of _read_receipt supporting the stated file behavior. [3]
- Frozen implementation of _public_execution supporting the stated file behavior. [4]
- The launch observer checks complete receipt, stable UUID and stored call before runtime launch. [5]
- Interrupts between receipt and call and checks retry retains one agent identity. [6]
- Changes task/capsule/prompt inputs and verifies repeat returns or replays saved receipt without new preparation. [7]
- Races publication and checks one persisted winner; competing request cannot issue another launch. [8]
- Through leaf/taskless routes checks restoration/refusal, exact advice and unchanged receipt/foreign link target. [9]
- Checks unresolved/rejected receipts returned unchanged without host read. [10]
- Checks an idle finished native turn projects completed lifecycle status and its bounded last text; the test does not itself prove absence of every semantic/Git mutation. [11]
- Pins delivered worker doctrine: one parent role_message after report, none for dashboard-started worker, and a finished turn is not AR acceptance. [12]
- Composes delivered architect/manager/orchestrator capsule text, requires current diff/evidence inspection and owner acceptance clauses, and detects removal of manager inspection; this proves instruction delivery rather than runtime no-mutation. [13]
