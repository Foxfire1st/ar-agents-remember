# mcp/src/agents_remember/mcp/registration/skills_extension.py

## Governing Overview

[registration route overview](overview.md)

## Purpose

Implements the **two mandatory SEP-2640 protocol methods** — `skills/list` and `skills/get` — and
bundles them with the served `skill://` resources inside an MCP 2.x SEP-2133 `Extension`
(`SkillsExtension`) passed to `MCPServer(extensions=[...])` at server construction time.

This is the surface that makes the `io.modelcontextprotocol/skills` capability honest. The
specification's §Capability Declaration states that *"declaring the extension itself commits the server
to `skills/list` and `skills/get`"* — so a server that advertises the capability without these methods
is advertising something it cannot answer. `capsule_serving.build_skills_extension` assembles the
`SkillsExtension` carrying the capability, methods, and resources together before `AgentsRememberMCP`
is constructed, eliminating any process-wide `ServerSession` monkeypatch.

## Code Commentary

### Logic

- `SkillsExtension(Extension)` declares `identifier = SKILLS_EXTENSION_ID`
  (`"io.modelcontextprotocol/skills"`), returns `{}` from `settings()`, returns the passed
  `ResourceBinding` tuple from `resources()`, and binds `skills/list` and `skills/get` via
  `MethodBinding` in `methods()`. Because `MCPServer(extensions=[...])` registers each extension
  per server instance, duplicate extension identifiers are rejected on that server and no SDK class
  is mutated process-wide.
- `preserve_handshake_extensions(extensions)` returns a `ServerMiddleware` passed to
  `MCPServer(middleware=[...])` that inspects only `ctx.method == "initialize"` responses and
  restores `capabilities.extensions` and `capabilities.experimental = {}` when absent. `mcp 2.3.0`
  validates handshake-era `initialize` results against the pre-2026 `ServerCapabilities` schema
  (`extra="ignore"`), which would otherwise strip `capabilities.extensions` and omit empty
  `experimental` before bytes reach handshake clients such as Claude Code, Codex, and Paseo.
- The request/result wire types are declared here as Pydantic models: `SkillsListParams` (optional
  `cursor`), `SkillsListRequest`, `SkillsGetParams` (`uri`), `SkillsGetRequest`,
  `SkillsListResult` (`resultType`, `skills`, `nextCursor`, `ttlMs`, `cacheScope`), and
  `SkillsGetResult` (`resultType`, `skill`).

Handler behavior:

- `_skills_list_handler(_ctx, _params)` returns every entry in one page. It accepts and ignores
  `params.cursor` deliberately: with one page there is no cursor to continue from, and refusing a
  cursor this server never issued would turn a conforming client's harmless retry into an error.
  Omitting `nextCursor` is the specification's own completion signal.
- `_skills_get_handler(_ctx, params)` resolves one skill by its `SKILL.md` resource URI through
  `SkillResourceCatalog.skill_for_root_uri` — an entry for **every** skill the server serves, listed
  or not — and raises `MCPError(code=INVALID_PARAMS, ...)` when the URI is not one this server
  serves, matching the code `resources/read` uses for an unknown resource.
- Both handlers answer from `skill_catalog_registry()`, the **same catalog the resources are
  registered from**, so the method surface and the resource surface cannot disagree about what is
  served.
- `_require_servable` translates a `SkillCatalogError` (an unreadable skill directory) into
  `MCPError(code=INVALID_PARAMS, ...)` rather than a 500, so a broken tree is a typed protocol
  refusal.

`resources/directory/read` is deliberately **not** implemented and `DIRECTORY_READ_CAPABILITY` is
deliberately **not** declared. The specification gates that optional method behind the capability
(*"a server that does not declare it never receives the call"*), and this server publishes concrete
resources, so the gate is the specification's own and is documented rather than silently omitted.

### Conventions

`SKILLS_LIST_METHOD` / `SKILLS_GET_METHOD` are module constants, so a test or a caller names the
method strings rather than spelling them. The two optional capability names
(`DIRECTORY_READ_CAPABILITY`, `LIST_CHANGED_CAPABILITY`) are declared as named constants with the
reason they are **not** in the declared set, so a later reader does not mistake an omission for an
oversight. The module reaches `application.skill_resources` through function-local imports in the two
thin helpers (`_catalog_for_request`, `_require_servable`) to keep the registration layer's
module-import graph unchanged.

### Invariants And Boundaries

- **Per-server extension registration, zero process-wide SDK patching.** `SkillsExtension` uses the
  SDK's SEP-2133 `Extension` interface (`MethodBinding` and `ResourceBinding`) at `MCPServer`
  construction time, holding no module-level patch state or `ServerSession` hooks.
- **Declaring the capability, answering its methods, and serving its resources are one unit.**
  `capsule_serving.build_skills_extension` constructs one `SkillsExtension` carrying all three, so
  the capability advertisement cannot outrun the method handlers.
- **Handshake middleware is initialize-only.** `preserve_handshake_extensions` passes every method
  other than `"initialize"` through untouched and never intercepts tool calls.
- **The optional capability is the gate, not a target.** `resources/directory/read` is unimplemented
  by design and the absence is a documented scope boundary, not a gap.
- **Answering methods does not widen authority.** The handlers read the registry and return entries;
  no handler activates a skill, grants a tool permission, or treats server-supplied text as trusted.
- The served entries carry **verbatim frontmatter** and per-file digests — the shape work belongs to
  `models/skill_resources.py` (`SkillResourceEntry.entry_document`) and the reading to
  `application/skill_resources/catalog.py`; this module only wires the methods to them.

### Todos

None recorded.

## Evidence

### Docs References

The specification this module implements, quoted in its own docstring:

- The extension introduces **three** protocol methods; `skills/list` and `skills/get` are implemented by every server declaring the extension, and it introduces no **other** methods, message types or schema changes. [1]

- **Declaring the extension itself commits the server** to `skills/list` and `skills/get`. [2]

- The optional `resources/directory/read` method is gated behind the `directoryRead` capability a server may decline, and "a server that does not declare it never receives the call". [3]
- An entry's `frontmatter` is a **verbatim copy** of the skill's `SKILL.md` frontmatter rendered as JSON — "every field the author wrote, not a curated subset". [4]

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

### Repo-Internal References

- `SkillsExtension` declares `io.modelcontextprotocol/skills` and binds `skills/list`, `skills/get`, and served `skill://` resources per server via `MethodBinding` and `ResourceBinding`. [5]
- `preserve_handshake_extensions` restores `capabilities.extensions` and `capabilities.experimental={}` on `initialize` responses without intercepting tool calls or patching SDK classes. [6]
- `build_skills_extension` assembles `SkillsExtension` with the index and every served skill file resource before `MCPServer` construction. [10]

- `skills/list` answers one page and omits `nextCursor`, which is the completion signal. [7]

- `skills/get` answers for any served skill, listed or not, and refuses an absent URI with `-32602`. [8]

- Both handlers answer from the same catalog the resources are registered from. [9]


- The entry shape the methods return: verbatim frontmatter plus per-file digest and size. [11]
- The reading half both handlers depend on, including the containment and revision guards. [12]

### Cross-Repo References

No cross-repository implementation dependency. Uses the installed `mcp` 2.x (`>=2.3.0,<3`) SEP-2133
`Extension` and `ServerMiddleware` interfaces directly.

- The real-process exchange that exercises the declared capability and both methods against the shipped entry point. [13]

- The case that pins the install-once idempotence of the declaration. [14]
