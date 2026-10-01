# mcp/src/agents_remember/application/skill_resources/__init__.py

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

## Evidence

### Docs References

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

- The extension identifier, this server's own index URI and schema, and the reserved `_meta` prefix. [1]
- The SEP entry the two mandatory methods return. [2]
- The served corpus is the package's own generated runtime skills copy, which is what makes a served revision reproducible. [3]

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640) — the URL the leaf's own `notes/source-evidence.md` pins.

### Repo-Internal References

- The package's two halves and the separation contract they exist to enforce. [4]
- The revision-checked delivery half: one addressed file, containment proven before the read. [5]
- The verbatim frontmatter reader the entries depend on. [6]
- The two planes stay separate in the compiled capsule: a declared skill becomes a reference, not instruction content. [7]
- The application entry points the MCP registration layer calls. [8]
- How the boundary is registered: three public MCP tools, the resource set, and the two mandatory protocol methods. [9]
- The governing section separates per-task capsule composition from stable reusable skill delivery and states the admission and provenance boundary between them. [10]

### Cross-Repo References

No cross-repository implementation dependency governs this package. The MCP SDK it registers
against is a pinned external dependency (`mcp==1.29.1` at this leaf), not a sibling repository.
