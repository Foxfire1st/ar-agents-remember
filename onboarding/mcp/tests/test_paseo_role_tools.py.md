# mcp/tests/test_paseo_role_tools.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the shared fixture of both role tools and the cases that decide who may start whom: the may-start
rule, a selection whose closed execution another starter began, a request id reused on another
selection, and the registered tool surface a harness actually reaches. A registered tool refuses what
the dashboard refuses, in the same words.

## Code Commentary

### Logic

- **The may-start rule.** `MayStartRuleTests.test_each_role_may_start_exactly_the_roles_the_rule_names`
  walks the rule's table, and `test_a_task_bound_caller_starts_only_under_its_own_sprint_or_master`
  bounds a task-bound caller to its own sprint or master.
- **Another starter.** `OtherStarterTests` admits a new start on a selection whose closed execution
  another began, and refuses to take over a receipt of another starter that appears during the start.
- **A reused request id** of one leaf on another prepares nothing:
  `ReusedRequestIdTests.test_the_request_id_of_one_leaf_reused_on_another_prepares_nothing`, with
  `compile_handover()` supplying the binding that names the selection.
- **The registered surface.** `RegisteredRoleToolTests` registers the tools and calls them as a harness
  would: they are registered under their names and answer inside the envelope; `mode` is absent from the
  tool schema and rejected by the HTTP route; a chat without a role starts a parentless Architect; and
  the registered tool refuses what the dashboard refuses in the same words.
- **Reads during catalog discovery.**
  `test_fresh_catalog_wait_leaves_registered_reads_responsive` holds a registered `role_start`
  in fresh catalog discovery, receives a successful registered read while that start remains
  pending, then releases discovery and checks that the start succeeds.

### Conventions

Cases reach the tools through the MCP registration (`mcp.registration.role_agents`) rather than calling
the CLI helpers directly, and use `paseo_role_tools_test_support` for the bridge fixture.

### Invariants And Boundaries

- A request id belongs to one selection; a start never takes over another starter's request or receipt.
- The registered tool surface is narrower than the HTTP route: `mode` is not offered and is refused.

## Evidence

- May-start rules, another starter's receipt, a reused request id and the registered tool surface are asserted here. [1]


- The second start reaches the held dispatch lock before pending is asserted. [2]


- The controlled fixture patches the actual bridge, caller, recipient, held-store and retirement owners after extraction. The registry still exposes role_start, role_start_set, user_settings_init and role_message, and an unbound role_start_set call is refused. [3]

- A native binding refusal carries no redundant operation envelope. [4]

- The role answer stays concise while a real `tool_call_context` supplies the dispatch log for detailed controls. [5]


- The role, task and report registration exists before agent-create begins, under the existing dispatch lock. [6]
