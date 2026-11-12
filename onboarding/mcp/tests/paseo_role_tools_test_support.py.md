# mcp/tests/paseo_role_tools_test_support.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The fixture both role-tool case modules import (PNT-R06): the fake host's wiring, the role tables and the request helpers have one home.

## Code Commentary

`ROLES` names the seven roles, `REFS` and `CALL_REFS` map the three document references to binding fields and to tool-call keyword arguments, and `binding` and `selection_of` derive both from `ROLE_REFS`. `RoleToolsTestCase` extends the status fixture: it patches `bridge_call` in the role-tool, wait, held-message and retirement modules, replaces `resolve_role_launch_context` and `TaskDocumentTopology`, and installs `agent_send` and `agent_wait`. `agent_send` applies the delivery rules in order (not-found, archived, closed, a pending permission decision, and a recipient in a turn whose provider takes no steer unless the host says it does), records the received text and the message id, and marks the agent running; `agent_wait` advances a fake clock by `waitMs` and answers queued waits or a still-running turn. `start`, `message`, `started`, `received`, `message_ids`, `waited` and `refusal` are the case helpers.

## Invariants And Boundaries

The receipt of a message id is recorded but not deduplicated, matching the host: a resend under one id is a second copy. Refusals are asserted through `refusal`, which requires `ok` false, status refused, the named refusal, and a non-empty detail and next action together, so a refusal without a way forward does not pass.

## Evidence

### Repo-Internal References

- The fake host refuses by class: absent, archived, closed, permission-pending, and a running provider that takes no steer. [1]


- One fixture serves both case modules, with the role tables and request helpers defined once. [2]
