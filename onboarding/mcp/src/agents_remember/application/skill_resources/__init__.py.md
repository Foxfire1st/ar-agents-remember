# mcp/src/agents_remember/application/skill_resources/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/skill_resources/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:20+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Purpose

The package door for the AR MCP boundary that serves **role capsules** and **reusable skills**. It
re-exports the two deliberately separate halves — the narrow read-only capsule operation
(`capsule.py`) and the SEP-2640 skills transport's reading half (`catalog.py`) — plus the frontmatter
reader, the application entry points, the corpus provider and the wire response builders.

The separation is the point of the package, and the module docstring states it: a capsule is
per-task context composition and a skill is a stable reusable instruction module. Nothing here turns
one into the other, and no resource read grants a tool permission.

## Code Commentary

### Logic

A pure re-export surface, with one grouping decision that matters:

- `capsule.py` — `compile_task_capsule`, `CapsuleCompileRequest`, `CapsuleSourceSelectionRequest`,
  `CapsuleCompileOutcome`, `routed_admission_request`, `admitted_tool_policy`, `capsule_payload`,
  `COMPOSITION_MANIFEST`, and — added by `260915-CAPS-L15` — `CapsuleSeatAddress` and
  `routed_admission_for`, the seat-addressed form of the same routing rule for a caller with no task
  document and therefore no compile request to hand over. It reads no caller-named path.
- `catalog.py` — `build_skill_catalog`, `read_served_file`, `require_servable`, `unreadable_skills`,
  `index_resource_meta`, `SkillSourceTree`, `ServedSkillFile`, `SkillCatalogError`.
- `frontmatter.py` — `parse_skill_frontmatter`, `SkillFrontmatter`, `SkillFrontmatterError`.
- `operation.py` — `role_capsule_compile_tool`, `skill_catalog_list_tool`,
  `skill_catalog_read_tool`, `skill_catalog_registry`, and the two request records.
- `provider.py` — the shipped corpus and its publishing origin as one binding.
- `responses.py` — the three wire response builders.

`__all__` is explicit and complete; there is no `*` re-export and no computed `__all__`.

### Conventions

The package follows the `application` layer's ordinary shape: typed request dataclasses in, wire
response contracts out, no MCP or protocol types read at this layer. The two surfaces each get one
owning module rather than one module with two modes. The protocol-method half of the transport lives one
layer up, in `mcp/registration/skills_extension.py`; this package supplies the registry and the entries
those methods answer with.

### Invariants And Boundaries

- **A capsule is not a skill and a skill is not capsule content.** A declared skill produces a
  *reference* (identity + origin + uri + revision) and is never composed into the instruction stream;
  per-task facts stay in the capsule's task-context channel.
- **The caller names no path inside the admitted corpus.** The composition manifest routes the source
  set; the corpus root, its manifest and its `origin` travel together.
- **The registry is the single source both transport halves answer from.** `skill_catalog_registry()`
  feeds this server's own listing/read tools, the MCP resources, and the `skills/list` / `skills/get`
  handlers, so the surfaces cannot disagree about what is served.
- This package owns no permission decision: `admitted_tool_policy` reads the published roster and the
  compiler narrows requests against it.
- **One routing rule, two addresses.** `routed_admission_request` (enclosure + task path) and
  `routed_admission_for` (role + operation) are entry points to the *same* manifest selection; neither
  may grow a selection rule of its own, and the launch path uses the second precisely so a taskless
  seat cannot re-derive a source set.

### Todos

None recorded.

## Docs References

The served transport is the MCP skills extension (SEP-2640). Its operative facts for a reader of this
package:

1. The extension introduces **three protocol methods**, and declaring it **commits** a server to
   implementing `skills/list` and `skills/get`. Its own Rationale records "the choice of a method over
   an index resource" — so a resource index is **not** the extension's enumeration surface. Both
   mandatory methods are implemented by this leaf, in `mcp/registration/skills_extension.py`.
2. `skills/list` entries carry the SEP shape `{uri, frontmatter, resources:[{uri,digest,size}]}`, where
   `frontmatter` is the **verbatim** `SKILL.md` frontmatter. This package's `models/skill_resources.py`
   renders that shape and `catalog.py`/`frontmatter.py` supply it.
3. A `SKILL.md` MAY appear in a descendant directory, so **skills can nest**; publication stays flat,
   and a nested skill's files also belong to the enclosing skill's entry.
4. This server additionally publishes its own `skill://index.json` in the Agent Skills
   well-known-discovery shape. That is a **convenience resource of this server**, not the extension's
   enumeration result, and the wire description says so.

The package's reading contract (discovery separated from delivery, containment proven before the read,
per-file revision re-checked, unreadable recorded not dropped) is what makes the entries trustworthy.

| Finding | Anchor | Source |
| --- | --- | --- |
| The extension identifier, this server's own index URI and schema, and the reserved `_meta` prefix. | `SKILLS_EXTENSION_ID`; `SKILL_INDEX_URI`; `SKILL_INDEX_SCHEMA`; `SKILL_META_PREFIX` | mcp/src/agents_remember/models/skill_resources.py:31-43 |
| The SEP entry the two mandatory methods return. | `entry_document` | mcp/src/agents_remember/models/skill_resources.py:115-130 |
| The served corpus is the package's own generated runtime skills copy, which is what makes a served revision reproducible. | `PACKAGED_SKILLS_DIRECTORY`; `shipped_skill_tree` | mcp/src/agents_remember/application/skill_resources/provider.py:28-47 |

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640) — the URL the leaf's own `notes/source-evidence.md` pins.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package's two halves and the separation contract they exist to enforce. | `compile_task_capsule` | mcp/src/agents_remember/application/skill_resources/capsule.py:185-216 |
| The revision-checked delivery half: one addressed file, containment proven before the read. | `read_served_file` | mcp/src/agents_remember/application/skill_resources/catalog.py:117-148 |
| The verbatim frontmatter reader the entries depend on. | `parse_skill_frontmatter` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:52-71 |
| The two planes stay separate in the compiled capsule: a declared skill becomes a reference, not instruction content. | `CapsuleSkillReferencePayload`; `RoleCapsuleResponse` | mcp/src/agents_remember/models/role_capsule_resources.py:47-52; mcp/src/agents_remember/models/role_capsule_resources.py:86-115 |
| The application entry points the MCP registration layer calls. | `role_capsule_compile_tool`; `skill_catalog_list_tool`; `skill_catalog_read_tool` | mcp/src/agents_remember/application/skill_resources/operation.py:68-107 |
| How the boundary is registered: three public MCP tools, the resource set, and the two mandatory protocol methods. | `register_capsule_and_skill_tools`; `install_extension_methods` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:73-78; mcp/src/agents_remember/mcp/registration/skills_extension.py:133-153; mcp/src/agents_remember/mcp/registration/capsule_serving.py:85-90 |
| The section of the governing route overview that documents this package's two surfaces and their boundary. | `## 260915-CAPS-L4 The Capsule And Skill-Resource Application Boundary` | onboarding/mcp/src/agents_remember/application/overview.md:18-58 |

## Cross-Repo References

No cross-repository implementation dependency governs this package. The MCP SDK it registers
against is a pinned external dependency (`mcp==1.29.1` at this leaf), not a sibling repository.

## Update History

- 2026-09-17T10:20+02:00 — 260915-CAPS-L15 curator: **the re-export surface gained two names, and the
  grouping entry now records why both routing addresses exist.** `CapsuleSeatAddress` and
  `routed_admission_for` were added for the launch path: a seat with no task document has no
  `CapsuleCompileRequest` to hand over and must still use the one manifest selection, so the second
  entry point takes the two values that actually decide it. The invariant says explicitly that the two
  are entry points to one rule. Verification metadata moves to this leaf's base `15fa0e2c`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit and no
  hash or fingerprint was invented here.


- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: rewrote this card against the
  settled candidate. **Removed the rejection banner** — its subject was repaired by round 2 and round 3,
  so the banner described a candidate that no longer exists. Recorded that **both mandatory protocol
  methods are now implemented** (`mcp/registration/skills_extension.py`), that the SEP entry shape is
  `{uri, frontmatter, resources:[{uri,digest,size}]}` with **verbatim** frontmatter, that nested skills
  are published flat and their files also belong to the enclosing entry, and that this server's own
  `skill://index.json` is a convenience resource **distinct from** the extension's enumeration surface.
  Recorded that this package's registry is the single source all three transport halves answer from, and
  pointed the boundary at the new protocol-method module one layer up. All citation ranges re-derived
  against the current sources. Verification metadata remains closeout-owned; no acceptance claim is made.

- 2026-09-16T11:50+02:00 — 260915-CAPS-L4 curator, post-verdict correction (superseded): corrected this
  card's claim that the extension defines no protocol methods and recorded the rejected round-1 surface.
  That surface has since been repaired, so the banner is removed above.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the new
  `application/skill_resources` package. Recorded the two-surface separation (per-task capsule
  composition vs. stable reusable skill modules), the no-caller-named-path admission rule, and the
  package layout. Its claim that the extension adds no protocol methods was wrong and is corrected above.

