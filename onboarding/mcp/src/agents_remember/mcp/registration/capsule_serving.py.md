# mcp/src/agents_remember/mcp/registration/capsule_serving.py

## Current operative account

`capsule_serving.py` builds the SEP-2640 skills `SkillsExtension` passed to `MCPServer(extensions=[...])` at server construction time (replacing the retired 1.x `register_capsule_and_skill_tools` / `declare_skills_extension` / `_register_skill_resources` hooks):

- `build_skills_extension(catalog=None)` resolves the active `SkillResourceCatalog`, runs `require_servable`, collects `ResourceBinding` instances (imported from public `mcp.server.mcpserver`) for `skill://index.json` (`index_resource`) and every served skill file (`skill_file_resource`), and returns `SkillsExtension(bindings)`. Because `SkillsExtension` declares `io.modelcontextprotocol/skills` and binds `skills/list`, `skills/get`, and all `skill://` resources in one object passed to `MCPServer(extensions=[...])`, the capability, methods, and resources are installed together per server with no process-wide SDK patching or `WeakKeyDictionary` guards.
- `declared_extensions(server)` queries `client.server_capabilities.extensions` through a public `mcp.Client(server)` session as a dict (never touching `_lowlevel_server`).
- `read_resource_contents(server, uri)` reads one registered resource synchronously via `asyncio.run(server.read_resource(uri))`, and `build_shipped_catalog()` exposes the shipped catalog without constructing a server.
- The optional `resources/directory/read` method gated behind `directoryRead` remains unimplemented and undeclared. Nothing here activates a skill, grants a capability, or turns server-supplied text into local-file trust.

## Evidence

- `build_skills_extension` constructs `SkillsExtension` carrying the capability declaration, `skills/list` and `skills/get`, and all `ResourceBinding` entries for `skill://index.json` and served skill files before `MCPServer` construction. [2]

- `capsule_serving.py` builds the SEP-2640 `SkillsExtension` rather than registering tools in `TOOL_REGISTRARS`. [4]

- `build_skills_extension` couples capability declaration, methods, and resource bindings into one per-server `SkillsExtension` object. [6]

- `declared_extensions` reads `client.server_capabilities.extensions` through a public `mcp.Client(server)` session. [7]
- `skill_file_resource` and `index_resource` build `FunctionResource` objects whose loaders re-check revision and prove containment before serving. [8]
- `SkillsExtension` binds `skills/list` and `skills/get` to `_skills_list_handler` and `_skills_get_handler` via `MethodBinding`. [9]

- The extension introduces **three** protocol methods; `skills/list` and `skills/get` are implemented by every server declaring the extension, and it introduces no **other** methods, message types or schema changes. [1]
- This server's own index resource is the Agent Skills well-known-discovery shape and is explicitly *not* the extension's enumeration result. [3]
- The three response models the payloads are validated against. [11]
- The resource `_meta` provenance block every served file carries. [12]

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[registration route overview](overview.md)

## Purpose

Historically under `mcp` 1.x, this module registered capsule/skill tools and monkeypatched `create_initialization_options` via `declare_skills_extension`, `_register_skill_resources`, and `install_extension_methods` with `WeakKeyDictionary` guards. Those hooks were retired in `261125-DEP-L3` in favor of `build_skills_extension` returning a SEP-2133 `SkillsExtension`.

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills extension specification, SEP-2640).

</details>
