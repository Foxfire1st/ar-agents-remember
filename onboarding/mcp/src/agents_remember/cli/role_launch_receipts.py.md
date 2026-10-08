# mcp/src/agents_remember/cli/role_launch_receipts.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns durable current-line launch receipts, immutable saved-call replay, report binding and public projection.

## Code Commentary

Receipt creation is exclusive and complete before native launch; unknown outcomes retain replayRequest with original UUID/prompt/options. Resolved receipts drop replayRequest. Taskless canonical storage/migration remains bounded to exact receipt identities; old schema at current address refuses, previous host receipts are not execution authority. Public execution whitelists lifecycle fields and requested/observed tier disclosure, never task acceptance.

## Closing mark and archive settlement (MIK-R76)

`_execute_prepared_launch` reads the leaf closing mark before replaying a saved call and re-checks it
under the receipt lock after creation, so a retired start is refused instead of publishing a running
receipt. `_write_receipt` serializes short metadata publication under the existing lock and merges
the same request's closing marker, archive debt and refusal facts when a stale ordinary writer
publishes, so a concurrent settlement is not erased. The existing request-ID reconciliation and
saved-call replay semantics are otherwise unchanged.

## Evidence


- Frozen implementation of _create_receipt supporting the stated file behavior. [2]
- Frozen implementation of _read_receipt supporting the stated file behavior. [3]


- Interrupts between receipt and call and checks retry retains one agent identity. [6]

- Races publication and checks one persisted winner; competing request cannot issue another launch. [8]

- Checks unresolved/rejected receipts returned unchanged without host read. [10]
- Checks an idle finished native turn projects completed lifecycle status and its bounded last text; the test does not itself prove absence of every semantic/Git mutation. [11]


## MIK-R95 Preparation Receipt

A successful launch receipt records the public open outcome it observed: `receipt.preparation.workspace` is `created`, `found` or `opened` when the outcome names one, and the enclosure's own `created`/`found`/`not-applicable` value is carried beside it. `_public_execution` exposes the `preparation` block to the role-start answer.

## Investigator scope and request identity

Selected-task Investigator receipts are per request rather than singleton selections. Read normalization exposes the canonical role with the one notice while keeping original stored role, labels, request/agent IDs and report paths. Same-request replay still answers from the recorded call; a new source tree is never a reason to rewrite the first assignment. Task ownership and complete-set capacity are delegated to investigator_receipts, with no second receipt writer.


- The current source implements this file’s stated Investigator boundary. [14]


## Refreshed current evidence

- Frozen implementation of _execute_prepared_launch supporting the stated file behavior. [1]
- Frozen implementation of _public_execution supporting the stated file behavior. [4]
- The launch observer checks complete receipt, stable UUID and stored call before runtime launch. [5]
- Changes task/capsule/prompt inputs and verifies repeat returns or replays saved receipt without new preparation. [7]
- Through leaf/taskless routes checks restoration/refusal, exact advice and unchanged receipt/foreign link target. [9]
- Pins delivered worker doctrine: one parent role_message after report, none for dashboard-started worker, and a finished turn is not AR acceptance. [12]
- Composes delivered architect/manager/orchestrator capsule text, requires current diff/evidence inspection and owner acceptance clauses, and detects removal of manager inspection; this proves instruction delivery rather than runtime no-mutation. [13]
