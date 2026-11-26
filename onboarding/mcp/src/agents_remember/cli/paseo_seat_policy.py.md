# mcp/src/agents_remember/cli/paseo_seat_policy.py

## Governing Overview

[MCP](../../../overview.md)

## Purpose

Builds the startup tool policy for the seat's own bound Agents Remember task server and classifies whether a provider starts that task tool server eagerly at agent creation.

## Code Commentary

The helper selects the exact provider. Codex gets the ordered roster from `role_tool_roster`: a fresh ordinary seat names its role and receives exactly that role's allowlist, the list its task server advertises, and a call without a role, such as an explainer seat's, keeps the full public roster. Claude gets `server_info`. If the caller supplies the four explainer tool names, the helper appends those names on the same server. Other providers receive no policy.

`provider_starts_tool_server_at_create(provider: str) -> bool` classifies eager launch-time binding confirmation fail-closed: after stripping and lowercasing `provider`, it returns `bool(normalized) and normalized not in {"claude", "antigravity"}`, treating lazy Claude (first-turn server start) and native Antigravity (D890) as non-eager and every other non-empty provider as eager (`BUG-R51@v1`).

## Relationships

[`paseo_launch.py`](paseo_launch.py.md) calls `preapproval_policy` with the launch's role for ordinary role creation when the provider accepts MCP definitions. [`paseo_explainer_host.py`](paseo_explainer_host.py.md) calls it without a role for bound explainer creation. [`role_launch_confirmation.py`](role_launch_confirmation.py.md) and [`paseo_launch_test_support.py`](../../../tests/paseo_launch_test_support.py.md) call `provider_starts_tool_server_at_create` to gate Step 2 launch-time binding confirmation and synthetic fake bindings. The ordinary receipt uses `preapproval_detail` to describe the grant carried in the stored create call. Codex retains that startup grant across resume and reload. A replacement seat picks up tools introduced by later builds.

## Evidence

- The provider and the seat's role select the startup roster, which binds each granted tool to the supplied server. [1]

- Ordinary and explainer creates use the same policy. The explainer supplies its additional tools. [2]

- The receipt describes the lifetime of the grant. The Codex guide explains when the seat needs replacing. [3]

- `provider_starts_tool_server_at_create` returns `True` for every non-empty provider except lazy `claude` and native `antigravity` (D890), gating eager binding confirmation fail-closed (`BUG-R51@v1`). [4]
