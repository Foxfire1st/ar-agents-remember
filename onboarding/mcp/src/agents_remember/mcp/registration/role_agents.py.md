# mcp/src/agents_remember/mcp/registration/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Registers role_start, the Manager-owned role_start_set, and role_message with their explicit caller-visible contracts.

## Code Commentary

role_start constructs RoleStartCall, role_start_set constructs RoleStartSetCall with validated per-seat overrides, and role_message constructs RoleMessageCall, running blocking application work in a thread so waiting does not block server transport. Descriptions name caller binding, permitted child scope, same-request retry, receipt-bound addressing, role-message final reply behavior and bounded wait. No developer gate is transported through an invented tool. `role_start` accepts `feature_values` for speed features beside agent/model/effort; its description states that a start call cannot state a mode or a permission-bearing feature, which belong in user settings or the host profile.

Set overrides admit only agent, model, effort and feature values, never a caller mode or permission-policy setting. Leaf replacement carries the holder ID and explicit interruption permission. Message input carries an optional waiting-message withdrawal ID; the mounted description says held rather than accepted when the product queues unavailable-recipient work, and preserves the developer-only permission prompt boundary.

## Evidence


## Investigator scope and request identity

The mounted description names the shared Investigator slot refusal for new turns. The adapter delegates admission to the same role-message owner and preserves named refusal/detail/remedy values; tool description is not a runtime permission grant.


- The current source implements this file’s stated Investigator boundary. [2]


## Refreshed current evidence

- Frozen implementation of register_role_agent_tools supporting the stated file behavior. [1]
