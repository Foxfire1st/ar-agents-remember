# mcp/src/agents_remember/application/skill_resources/responses.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/skill_resources/responses.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Purpose

Builds the three wire responses the capsule and skill surfaces return. One place where compiled values
become the response contract, so the MCP adapter stays a registration layer and the payload shape has
a single definition. **Every field here is copied from a value an owner already produced** — nothing
in this module decides a selection, a permission or a trust level.

## Code Commentary

### Logic

- `role_capsule_response(outcome)` always sets `ok` and `explanation`; the remaining admitted facts
  (`role`, `seatAltitude`, `operationName`, `taskReference`, `taskDocumentDigest`, `repositoryId`,
  `workBranch`, `grantedTools`) are `None`/empty until a binding exists. On a refusal it also sets
  `refusalStatus` and `refusalNextAction`. `grantedTools` is the **sorted admitted policy**, which is
  why a caller can see the whole authorized surface even on a refusal that got as far as the binding.
- `_fill_manifest` (called in both shapes) fills `compositionOrder`, `instructionIdentities`,
  `conflictKinds` and `sources` from the compilation's diagnostic manifest, then — only when a result
  exists — `semanticDigest`, `instructions`, `skillReferences`, `requestedTools` and `taskContext`
  from the capsule. It returns early on `None` at either step, so a refusal keeps the manifest facts it
  does have and no fabricated capsule content.
- `skill_catalog_list_response(catalog)` renders discovery rows through `_entry_payload` and the
  recorded unreadable rows; it carries `indexUri` so a caller can find the well-known index resource.
- `skill_catalog_read_response(served, skill_revision=...)` renders one file. `skillRevision` is
  passed in rather than derived, because the entry's root revision and this file's revision are two
  different facts: on a supporting file they differ, and on `SKILL.md` they coincide. It refuses a
  non-UTF-8 body (`ValueError`), because an MCP text resource cannot carry it.
- `_entry_payload` renders a skill's `files` as **relative paths only** — the listing names files, it
  never carries their bytes.

### Conventions

Response construction is explicit keyword-by-keyword; there is no dictionary spreading and no
`model_dump` here. Refusal information travels in the same envelope as success information rather than
in a separate error type, which is what lets one response model serve both shapes.

### Invariants And Boundaries

- **`contentTrust` is a constant, not an input.** Every served skill file states
  `server-supplied-data`; no code path can set a trust level from content, and a resource read grants
  no tool permission. `M2` of the leaf's mutation probe targets the related guarantee on the grant
  side.
- **`declaredAllowedTools` is copied from the observed frontmatter and never applied.** A host MUST NOT
  honor a skill's tool declaration; the field exists so a reader that wants to refuse or gate the skill
  can see what it declared.
- **A refusal is not an empty success.** `ok` is false, a typed `refusalStatus` is present, and
  whatever was still true about the seat travels with it.
- This module reads no MCP types and formats no protocol output; it produces the strict `models`
  contracts that the transport envelope then carries.

### Todos

None recorded.

## Docs References

The trust statement this module stamps on every served file is the extension's own security posture:
skill content is server-supplied data, a host must not honor mechanisms declared in it, and a resource
read is not an activation.

| Finding | Anchor | Source |
| --- | --- | --- |
| A declared tool set is an observation, never a permission channel. | `declared_allowed_tools` | mcp/src/agents_remember/models/skill_resources.py:270-285 |
| Provenance travels with the bytes: origin, identity, this file's revision, and the trust statement. | `skill_meta` | mcp/src/agents_remember/models/skill_resources.py:253-267 |

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The response builders, and the admitted facts that are present in a refusal as well as a success. | `role_capsule_response` | mcp/src/agents_remember/application/skill_resources/responses.py:34-55 |
| A refusal keeps the manifest facts it has and never fabricates capsule content. | `_fill_manifest` | mcp/src/agents_remember/application/skill_resources/responses.py:58-119 |
| The listing names files and carries no body; `skillRevision` and this file's revision are two facts. | `_entry_payload`; `skill_catalog_read_response` | mcp/src/agents_remember/application/skill_resources/responses.py:138-164; mcp/src/agents_remember/application/skill_resources/responses.py:167-177 |
| The trust statement every served file carries, as a constant rather than an input. | `SERVER_SUPPLIED_CONTENT_TRUST` | mcp/src/agents_remember/models/role_capsule_resources.py:31-32 |
| The strict response contracts these builders produce. | `RoleCapsuleResponse`; `SkillCatalogListResponse`; `SkillCatalogReadResponse` | mcp/src/agents_remember/models/role_capsule_resources.py:86-115; mcp/src/agents_remember/models/role_capsule_resources.py:137-150; mcp/src/agents_remember/models/role_capsule_resources.py:153-167 |
| The case that executes the no-grant guarantee these builders render. | `test_reading_a_skill_does_not_grant_the_tools_its_frontmatter_names` | mcp/tests/test_capsule_serving.py:815-849 |
| The case that executes the no-body-in-a-listing guarantee these builders render. | `test_the_discovery_registry_is_not_the_model_visible_catalog` | mcp/tests/test_capsule_serving.py:886-912 |
| These builders serve this server's own tool surface; the extension's enumeration result is produced by the `skills/list` handler. | `_skills_list_handler` | mcp/src/agents_remember/mcp/registration/skills_extension.py:243-257 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_reading_a_skill_does_not_grant_the_tools_its_frontmatter_names` repointed to mcp/tests/test_capsule_serving.py:815-849. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_the_discovery_registry_is_not_the_model_visible_catalog` repointed to mcp/tests/test_capsule_serving.py:886-912. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: re-anchored every citation range
  against the current `models/skill_resources.py` and `mcp/tests/test_capsule_serving.py`, corrected the
  two case ranges that the repairs moved, and added the boundary row that matters after the repairs:
  these builders serve **this server's own tool surface**, while the extension's enumeration result is
  produced by the `skills/list` protocol handler on the registration route. The recorded contract is
  unchanged — copy-only builders, one refusal/success envelope, named-versus-carried in a listing, and
  the constant trust statement.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the response builders.
  Recorded the copy-only contract (no decision lives here), the refusal envelope that keeps the seat
  and revision facts it has, the named-versus-carried split between a listing and a read, the constant
  trust statement, and the two mutation-probe-backed guarantees (no grant, no body in a listing).
  Verification metadata remains closeout-owned; no acceptance claim is made.
