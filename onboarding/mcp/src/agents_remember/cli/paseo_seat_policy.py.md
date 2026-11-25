# mcp/src/agents_remember/cli/paseo_seat_policy.py

## Governing Overview

[MCP](../../../overview.md)

## Purpose

Builds the startup tool policy for the seat's own bound Agents Remember task server.

## Code Commentary

The helper selects the exact provider. Codex gets the ordered roster from `role_tool_roster`: a fresh ordinary seat names its role and receives exactly that role's allowlist, the list its task server advertises, and a call without a role, such as an explainer seat's, keeps the full public roster. Claude gets `server_info`. If the caller supplies the four explainer tool names, the helper appends those names on the same server. Other providers receive no policy.

## Relationships

[`paseo_launch.py`](paseo_launch.py.md) calls the helper with the launch's role for ordinary role creation when the provider accepts MCP definitions. [`paseo_explainer_host.py`](paseo_explainer_host.py.md) calls it without a role for bound explainer creation. The ordinary receipt uses `preapproval_detail` to describe the grant carried in the stored create call. Codex retains that startup grant across resume and reload. A replacement seat picks up tools introduced by later builds.

## Evidence

- The provider and the seat's role select the startup roster, which binds each granted tool to the supplied server. [1]

- Ordinary and explainer creates use the same policy. The explainer supplies its additional tools. [2]

- The receipt describes the lifetime of the grant. The Codex guide explains when the seat needs replacing. [3]
