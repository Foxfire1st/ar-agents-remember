# mcp/src/agents_remember/mcp/registration/capsule_serving.py

## Governing Overview

[registration route overview](overview.md)

## Purpose

Registers the capsule operation and the SEP-2640 skills transport as **one** MCP boundary, because they
are one leaf's surface over one admitted corpus — while keeping their exposures separate:

- `role_capsule_compile` is the narrow read-only capsule operation. It takes an enclosure contract path,
  a task path, a role and an operation, and returns the typed capsule or the explanation of its refusal.
  The seat is derived from the task document, and the role argument is checked against it.
- the skill surface is the SEP-2640 transport, in **three** parts: the `io.modelcontextprotocol/skills`
  capability declared in the `initialize` result, the extension's two mandatory protocol methods
  (`skills/list` and `skills/get`, installed by `skills_extension.py`), and one MCP resource per served
  skill file. `skill_catalog_list` and `skill_catalog_read` are this server's own tool reads over the
  same registry for a client that is not resource-aware.

Nothing registered here activates a skill, grants a capability, or turns server-supplied text into
local-file trust.

> **The module's own docstring is stale.** Its lines 10–15 still say the surface "adds no protocol
> method" and describe enumeration as the `skill://index.json` resource. That wording is contradicted by
> the module's own line 150 (`install_extension_methods(server._mcp_server)`) and by
> `models/skill_resources.py`, which states that SEP-2640 enumerates through `skills/list`. The
> behavior documented below is the code's; the docstring sentence is a residual wording defect in this
> leaf's own production file, recorded here rather than propagated. See "Defects routed" in the closing
> curator report.

## Code Commentary

### Logic

- `register_capsule_and_skill_tools(server, config)` is the single entry point `TOOL_REGISTRARS` calls.
  It registers the capsule tool, then the two skill tools, then the resource set (which also installs
  the extension declaration and the two protocol methods).
- `_register_capsule_tool` declares `role_capsule_compile(contract_path, task_path, role,
  operation="orientation")` and forwards to `role_capsule_compile_payload`. `_narrow_operation` refuses
  an operation outside the frozen `CAPSULE_OPERATIONS` with a `ValueError` before any work.
- `_register_skill_tools` declares `skill_catalog_list()` and `skill_catalog_read(uri)`. The registered
  signatures expose only `uri`; the `origin`/`root` overrides exist on the payload builder for tests and
  are **not** on the wire, so a live client cannot point the server at another tree.
- `_register_skill_resources` builds the catalog once, gates it through `require_servable`, and then —
  in this order — calls `declare_skills_extension(server)`, calls
  `install_extension_methods(server._mcp_server)`, adds the index resource, and adds one
  `FunctionResource` per skill file. Guarded by `_REGISTERED`, a `WeakKeyDictionary` keyed on the
  server, so a second call cannot register the same resources twice.
- `declare_skills_extension(server)` wraps `server._mcp_server.create_initialization_options` so the
  `initialize` result carries `capabilities.extensions = {"io.modelcontextprotocol/skills": {}}`.
  Guarded by `_DECLARED`, also a `WeakKeyDictionary`. The installed SDK has no `extensions` field on
  `ServerCapabilities`; the model declares `extra="allow"`, so the key rides the options' one
  construction point and **no typed SDK field is narrowed or replaced**.
- `skill_file_resource` and `index_resource` build the two resource shapes. `skill_file_resource`'s
  loader calls `read_served_file`, which re-checks the revision and proves containment; a non-UTF-8 body
  raises rather than being served as mangled text.
- `declared_extensions(server)` and `read_resource_contents(server, uri)` are read helpers for a caller
  that wants the declaration or one resource without going through a client.
- `build_shipped_catalog()` exposes the shipped registry without a server.

### Conventions

Resources are declared with `FunctionResource`, carrying `uri`, `name`, `description`, `mime_type` and
the `_meta` provenance block from `models/skill_resources.py::skill_meta`. Idempotence is per server and
held in a **weak** key, so a collected server cannot hand its registration state to a later server that
happens to reuse its identity. The protocol-method installation itself lives in the sibling
`skills_extension.py`; this module only calls it, so the registration layer's shape stays
"declare the surface, then register it".

### Invariants And Boundaries

- **The capability and its methods are installed together.** `declare_skills_extension` and
  `install_extension_methods` are adjacent calls in `_register_skill_resources`, because the
  specification makes the declaration itself a commitment: *"declaring the extension itself commits the
  server to `skills/list` and `skills/get`."* A server that advertises the capability and answers
  neither is the round-1 defect (`F-L4-05`), and this adjacency is the repair. `M5` of the leaf's
  mutation probe removes the coupling and the live exchange case fails on a missing `extensions` key.
- **The `skill://index.json` resource is this server's own convenience surface, not the extension's
  enumeration result.** `index_resource`'s description says so on the wire, and
  `models/skill_resources.py::index_document` says so in code. `skills/list` is the enumeration surface.
- **The registered tool signature is the published schema** (the route's defining contract). The skill
  tools are therefore flat by construction, and the test-only `origin`/`root` parameters stay off the
  wire.
- **A weak key, not `id()`.** The per-server registration state is keyed on the server object; a key
  derived from `id(self)` would let a garbage-collected server's registration be inherited by a new
  server that reused the address.
- Nothing here decides a selection or a permission: it declares, and forwards to
  `mcp/tools/capsule_serving.py` and the application layer.
- The `mcp` route may not import from below its layer rank, and this module imports only `application`,
  `models` and the SDK.

### Todos

None recorded.

## Evidence

### Docs References

The specification this surface implements. Its two operative clauses for a reader here:

- The extension introduces **three** protocol methods; `skills/list` and `skills/get` are implemented by every server declaring the extension, and it introduces no **other** methods, message types or schema changes. [1]
- **Declaring the extension itself commits the server** to `skills/list` and `skills/get` — which is why the declaration and the methods install together here. [2]
- This server's own index resource is the Agent Skills well-known-discovery shape and is explicitly *not* the extension's enumeration result. [3]

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

### Repo-Internal References

- The one entry point the registrar tuple calls, registering both tool families and the resource set. [4]
- The flat registered signature is the published schema; the test-only corpus overrides stay off the wire. [5]
- The capability and the two protocol methods are installed by adjacent calls, so the advertisement cannot outrun the implementation. [6]
- The extension declaration extends the SDK's initialization options at their one construction point, without narrowing a typed field. [7]
- The resource shapes, whose loader re-checks the revision and proves containment before serving. [8]
- The two mandatory methods and their handlers. [9]
- The payload builders every declaration forwards to. [10]
- The three response models the payloads are validated against. [11]
- The resource `_meta` provenance block every served file carries. [12]
- The live client/server exchange that executes the declaration, both methods and the resource list. [13]
- The traversal case that reads a path outside a skill directory from the live process and must be refused. [14]
- The case that pins the install-once idempotence of the declaration. [15]

### Cross-Repo References

No cross-repository implementation dependency. The MCP SDK is a pinned external dependency
(`mcp==1.29.1` at this leaf); this leaf neither moved nor migrated it, and substituted no legacy
index/archive mode for a protocol method.
