# mcp/src/agents_remember/application/role_launch_context.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Resolves the canonical task hierarchy selected for one role launch.

## Code Commentary

Role classes define required sprint/master/leaf references; taskless classes reject those references. resolve_role_launch_context resolves real documents and verifies orchestration kind and parent relations. selection_binding serializes those exact references and role so receipt, handover and message addressing share one stable selection.

## Evidence


- Frozen implementation of selection_binding supporting the stated file behavior. [2]

## Investigator scope and request identity

Investigator has Projects, selected-sprint and selected-sprint/master launch classes. Resolving these classes uses actual canonical topology and refuses a leaf selection before launch preparation creates anything. This extends the old taskless investigation scope; it does not infer task identity from a report path or weaken caller containment.


- The current source implements this file’s stated Investigator boundary. [3]


## Refreshed current evidence

- Frozen implementation of resolve_role_launch_context supporting the stated file behavior. [1]

## The free agent a one-call start reaches

`ROLE_LEVELS` gives `bootstrap` the `free-agent` level, so no per-level task override applies to it and its role row is its whole set of launch choices. It is taskless with `architect` and `investigator`: its execution receipt is keyed by the request id because the selection holds no document at all, not because it is a second identity of another role. `PARENTLESS_START_SELECTIONS` admits it with no sprint, master or leaf reference, so a document reference carried by a bootstrap start is a refused selection rather than an ignored one. The task-document resolution for every other role is unchanged.

- The level the free agent holds, which no per-level override reaches. [4]
- The taskless set whose receipts are keyed by their request id. [5]
- The parentless row that admits no document reference for the free agent. [6]
- The free agent is a launcher role with no document and no parent, and every document reference on its start is refused. [7]
