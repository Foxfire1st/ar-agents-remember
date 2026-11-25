# mcp/tests/test_role_tool_scope.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Protects the role-scoped task-server surface: a server launched for a role advertises and dispatches only that role's allowlist from `models/tools/role_tool_scope.py`, and a Codex seat is granted the same ordered list.

## Code Commentary

The table case checks that every allowlist is a non-empty ordered subsequence of `PUBLIC_TOOLS` without duplicates, that the eight entries cover the roster, that `system-specialist` resolves to the Investigator entry and that an unknown role raises `ValueError`.

In-process servers bound through `AgentBinding` cover the binding precedence: every role and the alias advertise exactly `tools_for_role` with their read-only hints, an unbound server keeps the whole roster, an explainer-only launch keeps the roster followed by `render`, `define_category`, `remove_category` and `grade`, a valid mixed launch keeps the Worker allowlist followed by those four, and a malformed binding mixed with an explainer serves only `server_info` and answers `render` as an unknown tool. A Worker server still fails construction on an unclassified tool the Worker excludes, so the read-only classification runs before the narrowing. The grant case compares `preapproval_policy` for each role with `tools_for_role`, a roleless Codex grant with `PUBLIC_TOOLS`, and the Claude grant with `server_info`.

The Architect case measures the compact `list_tools()` JSON of an unbound server and of a bound Architect on the same build and asserts the exact byte counts, 72,769 and 44,167, besides the 45,000-byte bound. Any change to a tool schema or description therefore fails the case until its expected bytes are renewed.

Two real MCP stdio sessions run the launched command. A bound Worker lists exactly its allowlist, and a `role_start` call fails before and after the list, leaving two raised-call log rows. A malformed binding initializes without instructions, lists only `server_info`, whose call fails naming `AR_PASEO_AGENT_ID`, and answers `task_doc` and `render` as unknown tools.

## Relationships

The module is declared in the `unit-regression` lane of [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md), and [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) names it as an exact consumer of `_user_settings_guard.py` and the Node-profile `package-lock.json`. The launch suites [`test_paseo_launch.py`](test_paseo_launch.py.md), [`test_paseo_launch_roles.py`](test_paseo_launch_roles.py.md), [`test_paseo_catalog_r71.py`](test_paseo_catalog_r71.py.md) and [`test_role_handover_binding.py`](test_role_handover_binding.py.md) pin the same grant through the launch path.

## Evidence

- The table case checks order, union, alias and the unknown-role refusal. [1]
- A malformed binding mixed with an explainer serves only server_info and answers render as an unknown tool. [2]
- The Architect case asserts the exact unbound and bound byte counts and the 45,000-byte bound. [3]
- A real stdio Worker session lists its allowlist and leaves two raised-call rows for refused role_start calls. [4]
