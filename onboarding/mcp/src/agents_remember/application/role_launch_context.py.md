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
