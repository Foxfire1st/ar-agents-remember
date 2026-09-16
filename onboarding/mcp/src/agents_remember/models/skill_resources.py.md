# mcp/src/agents_remember/models/skill_resources.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/skill_resources.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `ff97072c2d816dc6bc15d55bf8578db7fdd376b8` |
| lastVerifiedCommitDate | 2026-09-16T12:47:44+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

The model-owned half of the SEP-2640 skills transport: the **discovery registry**, the per-file
revisions, and the **`skills/list` / `skills/get` entry shape**. Pure values plus their rendering, so
the `application` layer that owns the reading and the `mcp` layer that owns the registration both
import one definition instead of keeping two copies of the wire shape in step.

Identity is `origin` (the publishing server's identity) plus the resource URI. A resource read is data
delivery: nothing here activates a skill, grants a tool permission, or marks server-supplied text as
trusted, and there is deliberately **no field through which it could**.

The entry shape is the final specification's: `{uri, frontmatter, resources}`, where `frontmatter` is
the **verbatim** `SKILL.md` frontmatter rendered as JSON and `resources` enumerates every file of the
skill with its digest and size. A nested skill is published flat — an ordinary entry whose `uri` merely
shares a path prefix with the enclosing skill's, with nothing marking the nesting.

## Code Commentary

### Logic

- Constants: `SKILLS_EXTENSION_ID`, `SKILL_INDEX_URI` (`skill://index.json`), `SKILL_INDEX_SCHEMA`
  (the Agent Skills discovery index schema **this server's own** index emits), `SKILL_META_PREFIX`,
  `ALLOWED_TOOLS_KEY`, `SKILL_ROOT_FILE`, `RESULT_TYPE_COMPLETE` and the three MIME strings.
- `SkillResourceFile` — one addressable file inside a skill directory, with the digest of its own bytes
  as `revision` and its raw length as `byte_length`, which the entry's `size` field carries so a host
  can budget a skill before fetching anything.
- `SkillResourceEntry` — one skill in the registry. `identity` is `"<origin>#<name>"`, which is what
  keeps two servers serving a same-named skill distinct; `root` finds the `SKILL.md` record;
  `frontmatter` holds every field the author wrote.
- `entry_document()` — **the SEP-2640 entry**: `{uri, frontmatter, resources}` with
  `{uri, digest, size}` per file. This is what `skills/list` and `skills/get` return. `resources` is
  complete by construction: the catalog enumerates every file of the skill, each exactly once, and
  refuses to publish a skill whose root file is missing from that set.
- `UnreadableSkill` — one discovered directory that cannot be served, with its cause. A recorded fact
  of one build, never a silent omission.
- `SkillResourceCatalog` — every skill one server publishes plus the tree they were read from, with
  `entry(identity)`, `entry_for_uri(uri)`, **`skill_for_root_uri(uri)`** (what `skills/get` answers
  from), `names()`, `entry_documents()`, `discovery_metadata()`, `index_document()` and `index_bytes()`.
- `entry_documents()` is the **enumeration surface**: one SEP entry per skill in stable order, carrying
  no file body.
- `discovery_metadata()` is what **this server's own** tool listing hands out: name, description,
  origin, the `SKILL.md` URI, the root revision and the skill path. Bodies are not reachable from it.
- `index_document()` renders **this server's own** `skill://index.json` in the Agent Skills
  well-known-discovery shape (`$schema` plus one `{name, type: "skill-md", description, url, _meta}` row
  per skill). It is deliberately **not** the extension's enumeration result — SEP-2640 enumerates
  through `skills/list`. All three renderers sort by `(name, origin)` so a listing is deterministic.
- `skill_meta(entry, record)` is the `_meta` block a skill resource carries on read and on listing:
  origin, identity, exactly this file's revision, and `contentTrust: "server-supplied-data"`.
- `declared_allowed_tools(frontmatter)` normalizes the observed `allowed-tools` value from either a
  comma-separated string or a list.

### Conventions

Frozen slotted dataclasses, no behavior beyond lookup and rendering. Extension keys are always built
as `f"{SKILL_META_PREFIX}{key}"` rather than spelled inline, so the reserved prefix has one source.
`frontmatter` is typed `Mapping[str, Any]` and carried verbatim, because the specification forbids a
curated subset.

### Invariants And Boundaries

- **The entry carries verbatim frontmatter.** `license`, `metadata` and fields added by future
  revisions of the Agent Skills specification must pass through unchanged; the reader that produces
  this map (`application/skill_resources/frontmatter.py`) implements a YAML subset and refuses the
  constructs it does not implement rather than guessing.
- **`resources` is complete, and nested files belong to both entries.** From the enclosing skill's
  perspective a nested skill's files are ordinary supporting files, so the same file appears in both
  entries — which the specification states explicitly.
- **The `_meta` prefix is reverse-domain and reserved by the extension.** Every extension key in this
  module is composed from `SKILL_META_PREFIX`; a hand-spelled key would drift from it.
- **`contentTrust` is stated, never inferred.** The trust level is a fixed string on every served file,
  so no consumer has to infer trust from the transport.
- **`declared_allowed_tools` is an observation, never a grant.** A host MUST NOT honor a skill's tool
  declaration; this value exists for a reader that wants to refuse or gate the skill, and no code path
  turns it into a permission. `test_reading_a_skill_does_not_grant_the_tools_its_frontmatter_names`
  and mutation `M2` are the executors.
- **The catalog is host bookkeeping for discovery, deliberately not the model-visible channel.**
  Listing metadata does not read a body, and reading one body does not read the others.
- **This server's own index is not the extension's surface.** `index_document` keeps the Agent Skills
  discovery shape as a convenience resource; presenting it as the enumeration result was the round-1
  defect the review rejected, and both the code docstring and `index_resource`'s wire description now
  say so.
- This module imports nothing from `mcp`; the `models` rank forbids it, and the package's own
  `public_roster.py` records the same constraint for the same reason.

### Todos

None recorded.

## Docs References

The extension specifies the entry shape, the enumeration methods and the security posture:

| Finding | Anchor | Source |
| --- | --- | --- |
| An entry's `frontmatter` is a **verbatim copy** of the skill's `SKILL.md` frontmatter rendered as JSON — "every field the author wrote, not a curated subset". | `entry_document` | mcp/src/agents_remember/models/skill_resources.py:115-130 |
| The extension introduces **three** protocol methods; enumeration is `skills/list`, not an index resource. | `SKILL_INDEX_URI` | mcp/src/agents_remember/models/skill_resources.py:34-37 |
| The extension identifier, the index schema version and the reserved `_meta` prefix. | `SKILLS_EXTENSION_ID`; `SKILL_INDEX_SCHEMA`; `SKILL_META_PREFIX` | mcp/src/agents_remember/models/skill_resources.py:31-43 |
| A host MUST NOT honor a skill's declared tools. | `ALLOWED_TOOLS_KEY`; `declared_allowed_tools` | mcp/src/agents_remember/models/skill_resources.py:45-46; mcp/src/agents_remember/models/skill_resources.py:270-285 |

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The SEP-2640 entry the two mandatory methods return: verbatim frontmatter plus per-file digest and size. | `entry_document` | mcp/src/agents_remember/models/skill_resources.py:115-130 |
| The enumeration surface: one entry per skill in stable order, carrying no body. | `entry_documents` | mcp/src/agents_remember/models/skill_resources.py:192-198 |
| What `skills/get` answers from: the skill whose `SKILL.md` URI is given, listed or not. | `skill_for_root_uri` | mcp/src/agents_remember/models/skill_resources.py:177-187 |
| This server's own listing surfaces hand out metadata only and cannot reach a body. | `discovery_metadata` | mcp/src/agents_remember/models/skill_resources.py:200-221 |
| This server's own index keeps the Agent Skills discovery shape and is explicitly not the enumeration result. | `index_document` | mcp/src/agents_remember/models/skill_resources.py:223-250 |
| Identity is origin plus name, which keeps two servers' same-named skills distinct. | `SkillResourceEntry.identity` | mcp/src/agents_remember/models/skill_resources.py:100-104 |
| A declared tool set is normalized as an observation and applied by no code path. | `declared_allowed_tools` | mcp/src/agents_remember/models/skill_resources.py:270-285 |
| Provenance and the constant trust statement every served file carries. | `skill_meta`; `SKILL_META_PREFIX` | mcp/src/agents_remember/models/skill_resources.py:253-267; mcp/src/agents_remember/models/skill_resources.py:43-43 |
| The frontmatter reader that fills the verbatim map, refusing constructs it does not implement. | `_MappingReader` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:97-100 |
| The reading half that builds these values and re-checks the revision on delivery. | `build_skill_catalog`; `read_served_file` | mcp/src/agents_remember/application/skill_resources/catalog.py:75-95; mcp/src/agents_remember/application/skill_resources/catalog.py:117-148 |
| The two mandatory methods that return these entries. | `_skills_list_handler`; `_skills_get_handler` | mcp/src/agents_remember/mcp/registration/skills_extension.py:243-280 |
| The response contracts that project these values onto this server's own tool surface. | `SkillCatalogEntryPayload`; `SkillCatalogReadResponse` | mcp/src/agents_remember/models/role_capsule_resources.py:118-127; mcp/src/agents_remember/models/role_capsule_resources.py:153-167 |
| The same no-`mcp`-import constraint recorded for the roster leaf. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-90 |
| The cases that execute the entry completeness, verbatim-frontmatter and no-grant guarantees. | `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter`; `test_reading_a_skill_does_not_grant_the_tools_its_frontmatter_names` | mcp/tests/test_capsule_serving.py:1040-1040; mcp/tests/test_capsule_serving.py:811-811 |
| The case that pins this server's own index as the Agent Skills discovery shape. | `test_this_servers_own_index_resource_keeps_the_agent_skills_discovery_shape` | mcp/tests/test_capsule_serving.py:1008-1008 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: refreshed this card against the
  settled candidate. The registry now owns the **SEP-2640 entry shape**, not merely a JSON index:
  recorded `entry_document()` (`{uri, frontmatter, resources:[{uri,digest,size}]}`) as what `skills/list`
  and `skills/get` return, `entry_documents()` as the enumeration surface, `skill_for_root_uri()` as
  what `skills/get` resolves, the verbatim-frontmatter requirement, the flat publication of nested
  skills and the both-entries rule for nested files, and the `size`-from-`byte_length` provenance.
  Corrected the description of `skill://index.json`: it is **this server's own** convenience resource in
  the Agent Skills discovery shape and explicitly **not** the extension's enumeration result (SEP-2640
  enumerates through `skills/list`), which is the distinction the round-1 review rejected the candidate
  over. Re-anchored every citation range against the current 305-line source and added the entry-shape,
  enumeration, `skills/get`, frontmatter-reader and method-handler rows. Verification metadata remains
  closeout-owned; no acceptance claim is made.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the SEP-2640 value types.
  Recorded the origin-plus-name identity that keeps same-named skills distinct, the discovery-only
  registry contract (metadata cannot reach a body), the additive `_meta` provenance and constant trust
  statement, the observed-never-applied `allowed-tools` value, and the no-`mcp`-import boundary. Its
  description of the index document as the discovery surface is superseded above.

