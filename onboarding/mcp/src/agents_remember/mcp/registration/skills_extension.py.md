# mcp/src/agents_remember/mcp/registration/skills_extension.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/registration/skills_extension.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `overview.md` |

## Governing Overview

[registration route overview](overview.md)

## Purpose

Implements the **two mandatory SEP-2640 protocol methods** — `skills/list` and `skills/get` — against
the pinned SDK, which has no skills affordance of its own. This module is the leaf's answer to the
requirement's own escape hatch: *"the smallest published implementation or **bounded explicit method
support**"*.

This is the surface that makes the `io.modelcontextprotocol/skills` capability honest. The
specification's §Capability Declaration states that *"declaring the extension itself commits the server
to `skills/list` and `skills/get`"* — so a server that advertises the capability without these methods
is advertising something it cannot answer. `capsule_serving.py` declares the capability and this module
supplies the methods, and they are installed from the same function so they cannot drift apart.

**Why the SDK needs patching at all.** The pinned `mcp==1.29.1` has zero case-insensitive `skill`
matches: `ServerCapabilities` carries no `extensions` field and an unmodelled method is refused with
`-32602` in `mcp/shared/session.py`. The extension is therefore neither declarable nor answerable
through the SDK's published vocabulary, and there is no newer SDK in this repository's pin range that
provides it.

## Code Commentary

### Logic

`install_extension_methods(server)` is the single entry point and makes exactly **three additive
changes**, each the narrowest that lets the two methods reach a handler:

1. `_install_request_union` rebinds the session's request-validation union to
   `ClientRequestType | SkillsListRequest | SkillsGetRequest`. `BaseSession.__init__` stores that union
   on the *instance* and `ServerSession.__init__` passes the SDK's own `ClientRequest`, so the union is
   rebound as each session is constructed. Guarded by a module-level `_INSTALLED` flag so the
   `ServerSession.__init__` patch is applied once per interpreter.
2. `_install_dispatcher` widens `Server._handle_message` so it recognises this module's request wrapper
   as a **request** rather than ignoring it. Without this the request is *silently dropped* and the call
   hangs — a worse failure than an error, and the reason this hook exists separately from the handler
   registration. Guarded per server by `_DISPATCH_INSTALLED`, a `WeakKeyDictionary`.
3. The two handlers join the SDK's own `server.request_handlers` map, keyed by this module's request
   types.

The request/result wire types are declared here as pydantic models: `SkillsListParams` (optional
`cursor`), `SkillsGetParams` (`uri`), `SkillsListResult` (`resultType`, `skills`, `nextCursor`, `ttlMs`,
`cacheScope`) and `SkillsGetResult` (`resultType`, `skill`). `EXTENDED_REQUEST_TYPE` /
`EXTENDED_RESULT_TYPE` are the **supersets** the session validates and serializes through.

Handler behavior:

- `_skills_list_handler` returns every entry in one page. It accepts and ignores `request.params.cursor`
  deliberately: with one page there is no cursor to continue from, and refusing a cursor this server
  never issued would turn a conforming client's harmless retry into an error. Omitting `nextCursor` is
  the specification's own completion signal.
- `_skills_get_handler` resolves one skill by its `SKILL.md` resource URI through
  `SkillResourceCatalog.skill_for_root_uri` — an entry for **every** skill the server serves, listed or
  not — and raises `McpError(INVALID_PARAMS)` when the URI is not one this server serves, matching the
  code `resources/read` uses for an unknown resource.
- Both handlers answer from `skill_catalog_registry()`, the **same catalog the resources are registered
  from**, so the method surface and the resource surface cannot disagree about what is served.
- `_require_servable` translates a `SkillCatalogError` (an unreadable skill directory) into
  `McpError(INVALID_PARAMS)` rather than a 500, so a broken tree is a typed protocol refusal.

`resources/directory/read` is deliberately **not** implemented and `DIRECTORY_READ_CAPABILITY` is
deliberately **not** declared. The specification gates that optional method behind the capability
(*"a server that does not declare it never receives the call"*), and this server publishes concrete
resources, so the gate is the specification's own and is documented rather than silently omitted.

### Conventions

`SKILLS_LIST_METHOD` / `SKILLS_GET_METHOD` are module constants, so a test or a caller names the method
strings rather than spelling them. The two optional capability names (`DIRECTORY_READ_CAPABILITY`,
`LIST_CHANGED_CAPABILITY`) are declared as named constants with the reason they are **not** in the
declared set, so a later reader does not mistake an omission for an oversight. The module reaches
`application.skill_resources` through function-local imports in the two thin helpers
(`_catalog_for_request`, `_require_servable`) to keep the registration layer's module-import graph
unchanged.

### Invariants And Boundaries

- **The extension is additive, never a replacement.** The SDK's own request and result types stay in the
  unions unchanged; a method this module does not register is still refused by the SDK's own `-32602`.
  No SDK version is moved, no transport is replaced, and no legacy index/archive mode is substituted for
  a method.
- **Declaring the capability and answering it are one act.** `skills_extension.install_extension_methods`
  is called from `capsule_serving._register_skill_resources` immediately beside
  `declare_skills_extension`, so the two cannot be installed independently. The round-1 rejection
  (`F-L4-05`) was precisely that gap, and this coupling is the repair.
- **The dispatcher hook is required, not decorative.** Removing it does not produce an error — it
  produces a hung call, because the SDK drops an unrecognised request wrapper. It is the one place in
  this module whose deletion is silent at the call site.
- **The optional capability is the gate, not a target.** `resources/directory/read` is unimplemented by
  design and the absence is a documented scope boundary, not a gap.
- **Answering methods does not widen authority.** The handlers read the registry and return entries;
  no handler activates a skill, grants a tool permission, or treats server-supplied text as trusted.
- The served entries carry **verbatim frontmatter** and per-file digests — the shape work belongs to
  `models/skill_resources.py` (`SkillResourceEntry.entry_document`) and the reading to
  `application/skill_resources/catalog.py`; this module only wires the methods to them.

### Todos

None recorded.

## Docs References

The specification this module implements, quoted in its own docstring:

| Finding | Anchor | Source |
| --- | --- | --- |
| The extension introduces **three** protocol methods; `skills/list` and `skills/get` are implemented by every server declaring the extension, and it introduces no **other** methods, message types or schema changes. | "This extension introduces three protocol methods."; "The extension introduces no other methods, message types, or schema changes." | mcp/src/agents_remember/mcp/registration/skills_extension.py:7-10 |
| **Declaring the extension itself commits the server** to `skills/list` and `skills/get`. | "Declaring the extension itself commits the server to" | mcp/src/agents_remember/mcp/registration/skills_extension.py:10-11 |
| The optional `resources/directory/read` method is gated behind the `directoryRead` capability a server may decline, and "a server that does not declare it never receives the call". | `DIRECTORY_READ_CAPABILITY` | mcp/src/agents_remember/mcp/registration/skills_extension.py:62-64 |
| An entry's `frontmatter` is a **verbatim copy** of the skill's `SKILL.md` frontmatter rendered as JSON — "every field the author wrote, not a curated subset". | `_MappingReader` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:97-100 |

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one entry point, making three additive changes; the process-wide session patch is idempotent. | `install_extension_methods`; `_install_request_union`; `_INSTALLED` | mcp/src/agents_remember/mcp/registration/skills_extension.py:133-177 |
| The dispatcher hook, without which an extension request is silently dropped rather than refused. | `_install_dispatcher`; `_DISPATCH_INSTALLED` | mcp/src/agents_remember/mcp/registration/skills_extension.py:180-214 |
| `skills/list` answers one page and omits `nextCursor`, which is the completion signal. | `_skills_list_handler`; `SkillsListResult` | mcp/src/agents_remember/mcp/registration/skills_extension.py:95-103; mcp/src/agents_remember/mcp/registration/skills_extension.py:243-257 |
| `skills/get` answers for any served skill, listed or not, and refuses an absent URI with `-32602`. | `_skills_get_handler`; `skill_for_root_uri` | mcp/src/agents_remember/mcp/registration/skills_extension.py:260-280; mcp/src/agents_remember/models/skill_resources.py:177-187 |
| Both handlers answer from the same catalog the resources are registered from. | `_catalog_for_request`; `_require_servable` | mcp/src/agents_remember/mcp/registration/skills_extension.py:235-240; mcp/src/agents_remember/mcp/registration/skills_extension.py:283-294 |
| The declaration beside it: the capability and the methods are installed together, so the advertisement cannot outrun the implementation. | `_register_skill_resources`; `declare_skills_extension` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:143-154; mcp/src/agents_remember/mcp/registration/capsule_serving.py:157-184; mcp/src/agents_remember/mcp/registration/capsule_serving.py:155-166 |
| The entry shape the methods return: verbatim frontmatter plus per-file digest and size. | `entry_document`; `entry_documents` | mcp/src/agents_remember/models/skill_resources.py:115-130; mcp/src/agents_remember/models/skill_resources.py:192-198 |
| The reading half both handlers depend on, including the containment and revision guards. | `build_skill_catalog`; `read_served_file` | mcp/src/agents_remember/application/skill_resources/catalog.py:75-95; mcp/src/agents_remember/application/skill_resources/catalog.py:117-148 |
| The real-process exchange that exercises the declared capability and both methods against the shipped entry point. | `test_a_real_client_and_server_exchange_over_the_installed_sdk` | mcp/tests/test_capsule_serving.py:1198-1268 |
| The case that pins the install-once idempotence of the declaration. | `test_the_extension_declaration_is_installed_once_per_server` | mcp/tests/test_capsule_serving.py:1393-1407 |

## Cross-Repo References

No cross-repository implementation dependency. `mcp==1.29.1` is a pinned external dependency this
module extends additively without moving it.

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_a_real_client_and_server_exchange_over_the_installed_sdk` repointed to mcp/tests/test_capsule_serving.py:1198-1268. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_the_extension_declaration_is_installed_once_per_server` repointed to mcp/tests/test_capsule_serving.py:1393-1407. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, closing pass: created the card for the new
  `skills_extension.py` module. Recorded the three additive changes (request union, dispatcher hook,
  handler registration), why the dispatcher hook is load-bearing (a dropped request hangs rather than
  errors), that the handlers answer from the same catalog the resources come from, that the
  declaration and the methods install together so the capability cannot outrun the implementation, and
  that `resources/directory/read` is declined by design through the specification's own capability
  gate. This module is the repair for round 1's `F-L4-05`. Verification metadata remains
  closeout-owned; no acceptance claim is made.
