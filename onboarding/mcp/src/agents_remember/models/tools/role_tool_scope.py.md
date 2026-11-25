# mcp/src/agents_remember/models/tools/role_tool_scope.py

## Governing Overview

[Models route overview](../overview.md)

## Purpose

Holds `ROLE_TOOL_ALLOWLISTS`, the one canonical table of the MCP tools each AR role may use, and the two lookups that read it. The task server narrows a role-bound process with this table and the seat's preapproval policy grants from it (currently for Codex seats), so neither owns a second copy.

## Code Commentary

Each of the eight role entries is a tuple of tool names in the exact order of `PUBLIC_TOOLS`, and the union of the eight entries is the whole public roster. The table is a read-only `MappingProxyType`. The entry sizes are Architect 26, Orchestrator 27, Manager 32, Worker 8, Curator 17, Reviewer 11, Investigator 10 and Bootstrap 8. Bootstrap holds no `role_message`, and only Architect, Orchestrator and Manager hold `role_start`.

`tools_for_role` normalizes the role through `canonical_role`, so `system-specialist` returns the Investigator entry. It raises `ValueError` naming a role the table does not hold, instead of returning the public roster. `role_tool_roster` returns `PUBLIC_TOOLS` for `None` and otherwise the role's entry.

## Relationships

[`mcp/server.py`](../../mcp/server.py.md) narrows a role-bound task server to `tools_for_role` of its binding, and [`cli/paseo_seat_policy.py`](../../cli/paseo_seat_policy.py.md) grants a Codex seat `role_tool_roster` of its role, so the advertised surface and the grant are the same ordered tuple. The `roles.<role>.tools` arrays of `skills/l-01-agent-lifecycles/composition-manifest.json` list the same tools; no code derives them from this table and no test compares the two. The module imports only `models.role_identity` and `models.tools.public_roster`.

## Evidence

- The table holds one ordered allowlist per canonical role, each a subsequence of the public roster. [1]
- An alias resolves to its canonical role and an unknown role raises instead of receiving the public roster. [2]
- A seat without a role keeps the public roster. [3]
- The task server narrows a role-bound process to its role's entry, and the Codex seat policy grants the same roster. [4]
