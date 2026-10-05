# mcp/src/agents_remember/application/role_launch_context.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Resolves the canonical task hierarchy selected for one role launch.

## Code Commentary

Role classes define required sprint/master/leaf references; taskless classes reject those references. resolve_role_launch_context resolves real documents and verifies orchestration kind and parent relations. selection_binding serializes those exact references and role so receipt, handover and message addressing share one stable selection.

## Evidence

- Frozen implementation of resolve_role_launch_context supporting the stated file behavior. [1]
- Frozen implementation of selection_binding supporting the stated file behavior. [2]
