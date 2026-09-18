# mcp/src/agents_remember/mcp/registration/capsule_serving.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/registration/capsule_serving.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `overview.md` |

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

## Docs References

The specification this surface implements. Its two operative clauses for a reader here:

| Finding | Anchor | Source |
| --- | --- | --- |
| The extension introduces **three** protocol methods; `skills/list` and `skills/get` are implemented by every server declaring the extension, and it introduces no **other** methods, message types or schema changes. | `SKILLS_EXTENSION_ID` | mcp/src/agents_remember/models/skill_resources.py:32-32 |
| **Declaring the extension itself commits the server** to `skills/list` and `skills/get` — which is why the declaration and the methods install together here. | `declare_skills_extension`; `install_extension_methods` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:150-150; mcp/src/agents_remember/mcp/registration/capsule_serving.py:157-184 |
| This server's own index resource is the Agent Skills well-known-discovery shape and is explicitly *not* the extension's enumeration result. | `SKILL_INDEX_URI`; `SKILL_INDEX_SCHEMA` | mcp/src/agents_remember/models/skill_resources.py:37-37; mcp/src/agents_remember/models/skill_resources.py:40-40 |

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one entry point the registrar tuple calls, registering both tool families and the resource set. | `register_capsule_and_skill_tools` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:85-90 |
| The flat registered signature is the published schema; the test-only corpus overrides stay off the wire. | `role_capsule_compile`; `skill_catalog_read`; `_narrow_operation` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:82-107; mcp/src/agents_remember/mcp/registration/capsule_serving.py:110-118; mcp/src/agents_remember/mcp/registration/capsule_serving.py:132-140 |
| The capability and the two protocol methods are installed by adjacent calls, so the advertisement cannot outrun the implementation. | `_register_skill_resources`; `install_extension_methods`; `_REGISTERED` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:70-70; mcp/src/agents_remember/mcp/registration/capsule_serving.py:143-154; mcp/src/agents_remember/mcp/registration/capsule_serving.py:155-166 |
| The extension declaration extends the SDK's initialization options at their one construction point, without narrowing a typed field. | `declare_skills_extension`; `_EXTENSIONS`; `_DECLARED` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:61-61; mcp/src/agents_remember/mcp/registration/capsule_serving.py:65-65; mcp/src/agents_remember/mcp/registration/capsule_serving.py:157-184; mcp/src/agents_remember/mcp/registration/capsule_serving.py:73-73 |
| The resource shapes, whose loader re-checks the revision and proves containment before serving. | `skill_file_resource`; `index_resource` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:194-225; mcp/src/agents_remember/mcp/registration/capsule_serving.py:228-251 |
| The two mandatory methods and their handlers. | `install_extension_methods`; `_skills_list_handler`; `_skills_get_handler` | mcp/src/agents_remember/mcp/registration/skills_extension.py:133-153; mcp/src/agents_remember/mcp/registration/skills_extension.py:243-257; mcp/src/agents_remember/mcp/registration/skills_extension.py:260-280 |
| The payload builders every declaration forwards to. | `role_capsule_compile_payload`; `skill_catalog_list_payload`; `skill_catalog_read_payload` | mcp/src/agents_remember/mcp/tools/capsule_serving.py:22-41; mcp/src/agents_remember/mcp/tools/capsule_serving.py:44-52; mcp/src/agents_remember/mcp/tools/capsule_serving.py:55-63 |
| The three response models the payloads are validated against. | `RoleCapsuleResponse`; `SkillCatalogListResponse`; `SkillCatalogReadResponse` | mcp/src/agents_remember/models/role_capsule_resources.py:86-166 |
| The resource `_meta` provenance block every served file carries. | `skill_meta`; `index_resource_meta` | mcp/src/agents_remember/models/skill_resources.py:253-267; mcp/src/agents_remember/application/skill_resources/catalog.py:151-157 |
| The live client/server exchange that executes the declaration, both methods and the resource list. | `test_a_real_client_and_server_exchange_over_the_installed_sdk` | mcp/tests/test_capsule_serving.py:1194-1264 |
| The traversal case that reads a path outside a skill directory from the live process and must be refused. | `test_the_server_process_never_serves_a_file_outside_a_skill_directory` | mcp/tests/test_capsule_serving.py:1267-1298 |
| The case that pins the install-once idempotence of the declaration. | `test_the_extension_declaration_is_installed_once_per_server` | mcp/tests/test_capsule_serving.py:1389-1403 |

## Cross-Repo References

No cross-repository implementation dependency. The MCP SDK is a pinned external dependency
(`mcp==1.29.1` at this leaf); this leaf neither moved nor migrated it, and substituted no legacy
index/archive mode for a protocol method.

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `register_capsule_and_skill_tools` repointed to mcp/src/agents_remember/mcp/registration/capsule_serving.py:85-90. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T12:25+02:00 — 260915-CAPS-L4 curator, **closing pass, citation work on this document
  alone** (`citation_fix --document mcp/src/agents_remember/mcp/registration/capsule_serving.py.md`
  against snapshot `d000fd91…`): one generated repair landed — the flat-signature row's three anchors
  (`role_capsule_compile`, `_narrow_operation`, `skill_catalog_read`) were split onto their own precise
  definition extents, replacing one coarse span — and ten ranges were normalised to the exact definition
  extents they claim. **Blast radius avoided (defect `D8`):** the same tool run root-wide would have
  rewritten **188 claims across many other leaves' documents**; running it per document confined every
  write to this leaf's own file (`documentsWritten`: 1, `documentsScanned`: 1).
- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: rewrote this card against the
  settled candidate. **Removed the rejection banner and the "adds no protocol method" wording** — both
  described the withdrawn round-1 surface. `_register_skill_resources` now calls
  `install_extension_methods(server._mcp_server)` beside `declare_skills_extension`, so the card
  records the extension's **two mandatory protocol methods as installed here**, the index resource as
  this server's own convenience surface rather than the extension's enumeration result, and the
  capability/method adjacency as the repair for round 1's `F-L4-05`. Recorded a residual wording defect
  in the production file itself: the module docstring at lines 10–15 still says the surface "adds no
  protocol method", contradicted by its own line 150 and by `models/skill_resources.py`. All citation
  ranges re-derived against the current 278-line source. Verification metadata remains closeout-owned;
  no acceptance claim is made.

- 2026-09-16T11:50+02:00 — 260915-CAPS-L4 curator, post-verdict correction (superseded): added a
  rejection banner and restated the surface as non-conforming, against the round-1 candidate that the
  baseline review rejected. That candidate has since been repaired, so this entry is now history about
  the rejected candidate, not about the shipped code.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the new registration module.
  Recorded the declaration and resource-registration coupling, that the registered tool signature is the
  published schema so the corpus overrides stay off the wire, and that the per-server registration state
  is weak-keyed to close the identity-reuse hazard. Its claim that the extension adds no protocol method
  was wrong and is corrected above.
