# mcp/src/agents_remember/mcp/registration/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Registers the two agent-initiated role tools and their explicit caller-visible contracts.

## Code Commentary

role_start constructs RoleStartCall and role_message constructs RoleMessageCall, running blocking application work in a thread so waiting does not block server transport. Descriptions name caller binding, permitted child scope, same-request retry, receipt-bound addressing, role-message final reply behavior and bounded wait. No developer gate is transported through an invented tool.

## Evidence

- Frozen implementation of register_role_agent_tools supporting the stated file behavior. [1]
