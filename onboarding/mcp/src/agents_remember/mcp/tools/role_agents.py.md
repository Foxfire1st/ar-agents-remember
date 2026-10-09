# mcp/src/agents_remember/mcp/tools/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Builds role_start/role_message payloads at the shared response-model/token boundary.

## Code Commentary

Each function forwards the typed call to the existing role tool owner and wraps its dictionary in _tool_payload under the matching public operation name. It adds no recipient resolution, launch authority, polling or compatibility state of its own.

Since 260928-MIK-L114 the two payload builders set `call_target_role` around the choke
point so the river names the started or addressed role: the role rides a context variable,
never the answer. For an id-addressed message `send_role_message` carries the role from
the resolved recipient's durable receipt instead.

## Evidence

- Frozen implementation of role_start_payload supporting the stated file behavior. [1]
- Frozen implementation of role_message_payload supporting the stated file behavior. [2]
