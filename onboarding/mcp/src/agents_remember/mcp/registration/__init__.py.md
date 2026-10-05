# mcp/src/agents_remember/mcp/registration/__init__.py

## Governing Overview

[registration route overview](overview.md)

## Purpose

The package door for the MCP tool surface. It declares the one registrar signature every family
module is called with and the ordered tuple `create_server` loops over.

Owns the one MCP registrar tuple assembling advertised tool families.

## Code Commentary

### Logic

Two public names:

- `ToolRegistrar = Callable[[FastMCP, McpRuntimeConfig], None]` — the shape of a family module's
  `register_*_tools`.
- `TOOL_REGISTRARS: tuple[ToolRegistrar, ...]` — the **fifteen** registrars in advertise order: core,
  sessions, memory, providers, code_search, worktrees, closeout, tasks, benchmarks, lifecycle,
  gates, orchestration, capsule-and-skill-serving, role-agent tools, knowledge.

`register_knowledge_tools` from `knowledge.py` remains last. The current role-agent registrar
`register_role_agent_tools` sits immediately before it, matching the advertised role names before the
knowledge tail. Historically the knowledge registrar was appended so no existing tool's registration order moved — registration order is part of the advertised contract, and the
advertised tuple `PUBLIC_TOOLS` therefore gained its five names at its own tail as well
(`knowledge_read`, `knowledge_change`, `knowledge_diff`, `knowledge_integrity_check`,
`knowledge_project`; 66 → 72 names). Before PNT, its immediate predecessor was `register_capsule_and_skill_tools` from
`capsule_serving.py`, appended in 260915-CAPS-L4; the role-agent registrar now separates them.

`__all__` exports both. The module docstring states the division this package exists to enforce:
`create_server` owns process wiring (the compact-content shim, the ambient lifecycle, the `FastMCP`
instance) and nothing else; every `@server.tool()` definition lives in a family module here.

### Invariants And Boundaries

- Adding a tool means editing one family module. Adding a family means a new module plus one entry
  in this tuple — `create_server` should never grow a special case.
- **Registrar, advertised roster and response registry preserve the same relative tool order.**
  The role-agent family is inserted immediately before knowledge on each surface. A family change must
  update all three surfaces together; a registrar whose placement disagrees with the roster is a
  live-inventory violation. Earlier append-only additions remain historical evidence.
- `PUBLIC_TOOLS` (defined at `mcp/src/agents_remember/models/tools/public_roster.py:22-97`,
  re-exported by `mcp/tools/base.py`)
  is the authority on the advertised name set; `mcp/tests/test_tools.py` compares it against a live
  server's `list_tools()` and against `server_info`'s exact list. The comparison is against a **live**
  registration, not against a payload that reports the tuple, so adding a registrar without adding its
  names to the tuple is a surface violation the suite catches.
- Importing this package imports every family module, which imports every payload builder. Keep it
  free of side effects beyond those imports. `capsule_serving.py` is the one family whose module also
  registers MCP **resources**, but the registration still happens inside its `register_*_tools`, so
  the package door's no-side-effects rule is unchanged.

### Role Runtime and Scope

register_role_agent_tools is added to TOOL_REGISTRARS in the existing registration order. Role start/message share the normal response envelope, registry and token boundary; no tool family registers itself through an alternate startup route.

## Evidence

### Repo-Internal References

- The `create_server` consumer iterates `TOOL_REGISTRARS`. [1]
- The advertised tool-name list's one definition, re-exported unchanged by the adapter. [2]
- The registrar appended last so no existing registration order moved. [3]
- The five advertised names the appended registrar publishes, at the tail of both surfaces. [4]
- The capsule registrar historically appended immediately before knowledge, before the role-agent insertion. [5]
- The three advertised names the capsule/skill registrar publishes, immediately before the knowledge tail. [6]
- The live registered-order comparison that makes a registrar-without-roster-name a surface violation. [7]

### Runtime Source References

- Frozen implementation of TOOL_REGISTRARS supporting the stated file behavior. [8]
