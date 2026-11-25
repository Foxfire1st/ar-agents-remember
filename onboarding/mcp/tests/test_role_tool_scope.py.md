# mcp/tests/test_role_tool_scope.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Protects the role-scoped task-server surface: a server launched for a role advertises and dispatches only that role's allowlist from `models/tools/role_tool_scope.py`, a Codex seat is granted the same ordered list, every advertised public tool keeps a raw description at or below 500 characters, every canonical role and the unbound server stay within enforced compact `list_tools()` byte ceilings, and a bound Manager session over real stdio lists all 32 compacted tools with unchanged Pydantic validation.

## Code Commentary

The table case checks that every allowlist is a non-empty ordered subsequence of `PUBLIC_TOOLS` without duplicates, that the eight entries cover the roster, that `system-specialist` resolves to the Investigator entry and that an unknown role raises `ValueError`.

In-process servers bound through `AgentBinding` cover the binding precedence: every role and the alias advertise exactly `tools_for_role` with their read-only hints, an unbound server keeps the whole roster, an explainer-only launch keeps the roster followed by `render`, `define_category`, `remove_category` and `grade`, a valid mixed launch keeps the Worker allowlist followed by those four, and a malformed binding mixed with an explainer serves only `server_info` and answers `render` as an unknown tool. A Worker server still fails construction on an unclassified tool the Worker excludes, so the read-only classification runs before the narrowing. The grant case compares `preapproval_policy` for each role with `tools_for_role`, a roleless Codex grant with `PUBLIC_TOOLS`, and the Claude grant with `server_info`.

The budget case (`COMPACT_BYTE_BUDGETS` and `MAX_RAW_TOOL_DESCRIPTION_CHARS = 500`) measures the compact `list_tools()` UTF-8 JSON of the unbound 44-tool server and every canonical role on the same build. It asserts that every unbound tool's raw `description` length is `<= 500`, that every scope stays at or below its compact ceiling and strictly below its pre-compaction baseline (Manager `<= 45,000 B` vs `59,618 B`, Architect `<= 34,000 B` vs `43,988 B`, Orchestrator `<= 34,000 B` vs `43,819 B`, Curator `<= 25,000 B` vs `32,736 B`, Reviewer `<= 19,500 B` vs `25,655 B`, Investigator `<= 14,500 B` vs `18,457 B`, Worker `<= 11,000 B` vs `14,045 B`, Bootstrap `<= 7,500 B` vs `9,027 B`, and Unbound `<= 55,000 B` vs `72,590 B`), that every bound role stays strictly below unbound bytes, and that compacted unbound bytes stay strictly below uncompacted bytes when `_compact_server_tool_schemas` is monkeypatched to a no-op.

Three real MCP stdio sessions run the launched command. A bound Worker lists exactly its allowlist, and a `role_start` call fails before and after the list, leaving two raised-call log rows. A malformed binding initializes without instructions, lists only `server_info`, whose call fails naming `AR_PASEO_AGENT_ID`, and answers `task_doc` and `render` as unknown tools. A bound Manager lists all 32 tools matching `tools_for_role("manager")` (including `curator_coherence` and `worktree_operation_control`), every advertised `inputSchema` equals `compact_tool_schema(tool.inputSchema)` with no root `"title"`, and empty calls to `curator_coherence` and `worktree_operation_control` return `isError is True` under unchanged Pydantic validation.

## Relationships

The module is declared in the `unit-regression` lane of [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md), and [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) names it as an exact consumer of `_user_settings_guard.py` and the Node-profile `package-lock.json`. The launch suites [`test_paseo_launch.py`](test_paseo_launch.py.md), [`test_paseo_launch_roles.py`](test_paseo_launch_roles.py.md), [`test_paseo_catalog_r71.py`](test_paseo_catalog_r71.py.md) and [`test_role_handover_binding.py`](test_role_handover_binding.py.md) pin the same grant through the launch path. Complements [`test_tool_schema_compaction.py`](test_tool_schema_compaction.py.md).

## Evidence

- The table case checks order, union, alias and the unknown-role refusal. [1]
- A malformed binding mixed with an explainer serves only server_info and answers render as an unknown tool. [2]


- The budget case enforces raw tool descriptions `<= 500` characters, all nine per-role and unbound baselines and compact ceilings in `COMPACT_BYTE_BUDGETS`, `bound < unbound`, and `compacted < uncompacted`. [3]

- A real stdio Manager session lists all 32 compacted tools in canonical order and rejects empty `curator_coherence` and `worktree_operation_control` calls via unchanged Pydantic validation. [5]

- A real stdio Worker session lists its allowlist and leaves two raised-call rows for refused role_start calls. [4]
