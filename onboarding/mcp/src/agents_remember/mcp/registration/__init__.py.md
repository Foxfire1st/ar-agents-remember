# mcp/src/agents_remember/mcp/registration/__init__.py

## Governing Overview

[registration route overview](overview.md)

## Purpose

The package door for the MCP tool surface. It declares the one registrar signature every family
module is called with and the ordered tuple `create_server` loops over.

## Code Commentary

### Logic

Two public names:

- `ToolRegistrar = Callable[[FastMCP, McpRuntimeConfig], None]` — the shape of a family module's
  `register_*_tools`.
- `TOOL_REGISTRARS: tuple[ToolRegistrar, ...]` — the **fourteen** registrars in advertise order: core,
  sessions, memory, providers, code_search, worktrees, closeout, tasks, benchmarks, lifecycle,
  gates, orchestration, capsule-and-skill-serving, knowledge.

The newest entry is `register_knowledge_tools` from `knowledge.py`, **appended** last so no existing
tool's registration order moved — registration order is part of the advertised contract, and the
advertised tuple `PUBLIC_TOOLS` therefore gained its five names at its own tail as well
(`knowledge_read`, `knowledge_change`, `knowledge_diff`, `knowledge_integrity_check`,
`knowledge_project`; 66 → 72 names). The entry immediately before it, `register_capsule_and_skill_tools`
from `capsule_serving.py`, was appended the same way in 260915-CAPS-L4.

`__all__` exports both. The module docstring states the division this package exists to enforce:
`create_server` owns process wiring (the compact-content shim, the ambient lifecycle, the `FastMCP`
instance) and nothing else; every `@server.tool()` definition lives in a family module here.

### Invariants And Boundaries

- Adding a tool means editing one family module. Adding a family means a new module plus one entry
  in this tuple — `create_server` should never grow a special case.
- **The tuple's order is the order the server advertises tools in, and a new family is appended.** A
  new registrar inserted in the middle would renumber every later tool's advertised position, so the
  two surfaces that compare order (`PUBLIC_TOOLS` and the live-inventory suite) would both report a
  violation that is really a reordering.
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

## Evidence

### Repo-Internal References

- The `create_server` consumer iterates `TOOL_REGISTRARS`. [1]
- The advertised tool-name list's one definition, re-exported unchanged by the adapter. [2]
- The registrar appended last so no existing registration order moved. [3]
- The five advertised names the appended registrar publishes, at the tail of both surfaces. [4]
- The registrar appended immediately before it, which established the same append-only precedent. [5]
- The three advertised names the capsule/skill registrar publishes, immediately before the knowledge tail. [6]
- The live registered-order comparison that makes a registrar-without-roster-name a surface violation. [7]
