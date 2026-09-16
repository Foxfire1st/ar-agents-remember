# mcp/src/agents_remember/application/skill_resources/catalog.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/skill_resources/catalog.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `ff97072c2d816dc6bc15d55bf8578db7fdd376b8` |
| lastVerifiedCommitDate | 2026-09-16T12:47:44+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Purpose

Builds the **host's skill discovery registry** from one canonical skills tree, and serves the bytes
one `skill://` resource URI addresses. Discovery and delivery are two different jobs and this module
keeps them apart: building the catalog walks each skill directory once, reads the frontmatter the
Agent Skills specification requires, and records a revision per file; serving later re-reads exactly
the file a URI addresses. A skill's body is therefore never reachable from the metadata the catalog
hands out.

An unreadable skill directory is **recorded, not dropped**: it is listed in `unreadable` and the
delivery entry points refuse while one exists, because serving the remaining skills would let a tree
edit quietly delete a skill from the surface.

## Code Commentary

### Logic

- `build_skill_catalog(tree)` walks the tree (`_skill_paths`, bounded to `_MAX_SKILL_DEPTH = 32`), and
  for each directory carrying a `SKILL.md` reads it (`_read_skill`) into a `SkillResourceEntry`; a
  failure is captured as an `UnreadableSkill` rather than raised. Entries and unreadable rows are both
  sorted deterministically. The unreadable set rides on the returned catalog so one build produces one
  verdict and the delivery entry points read it from there instead of re-walking.
- `_skill_paths` **descends through a skill directory rather than stopping at it**, because SEP-2640
  allows a `SKILL.md` in a descendant directory and requires a nested skill to be published flat like
  any other. The stated 32-level bound exists only so a pathological tree cannot make one registration
  unbounded; it is documented rather than implied.
- `_read_skill` requires the declared frontmatter `name` to equal the final skill-path segment.
  SEP-2640 makes the declared name — not the path — the skill's identity, so a directory named
  differently from its declared name is refused rather than served under a guessed identity. It also
  requires the directory to hold a `SKILL.md` record, and carries the **verbatim** frontmatter onto the
  entry so `skills/list` can publish every field the author wrote.
- `_relative_files` walks a skill directory to any depth, skipping `__pycache__` and compiled files, and
  therefore includes a **nested skill's** files: from the enclosing skill's perspective they are
  ordinary supporting files, which the specification states explicitly. `_file_record` records each
  file's `relative_path`, `uri`, `mime_type`, `revision` and `byte_length` — the latter being the
  entry's `size`. `_mime_type` returns `text/markdown` for UTF-8 `.md` and
  `application/octet-stream` otherwise.
- `read_served_file(catalog, uri)` resolves the entry and record from the catalog
  (`entry_for_uri`), **proves containment inside the skill's own directory before reading a byte**,
  reads the bytes, and refuses when the observed digest no longer equals the recorded revision. A
  tree that moved under the catalog is a refusal, not a stale delivery.
- `require_servable(catalog, action=...)` is the delivery gate: it raises while any unreadable skill
  exists, naming every one and its cause. The two protocol-method handlers translate that refusal into
  `-32602` rather than a server error.
- `index_resource_meta` builds the `skill://index.json` `_meta` block (publishing origin and skill
  count).

### Conventions

URI shapes are built in one place each: `_skill_directory_uri` is the address every file in a skill
hangs off, and `_skill_root_file_uri` is that directory plus `SKILL.md` — explicit, because SEP-2640
makes `SKILL.md` explicit rather than implied. Digests are always rendered `sha256:<hex>` through
`_digest`.

### Invariants And Boundaries

- **Containment is proven before the read**, not after: a catalog record that could address a file
  outside its own skill directory is refused and never served. The case that executes it is
  `test_a_catalog_record_that_escapes_its_skill_directory_is_refused`, which drives the guard directly
  rather than relying on an earlier lookup refusal.
- **Bytes are re-read, not cached.** The revision check compares the recorded digest to the bytes just
  read from the same tree in the same call.
- **An unreadable skill is never a silent omission and never an empty success.** The revision check
  (`M4`), the unreadable refusal (`M6`) and the index-reader refusal
  (`test_the_index_reader_refuses_while_a_skill_cannot_be_served`) each execute one half of this.
- **A nested skill is discovered and published flat.** The walk does not stop at a skill directory, and
  a nested skill is an ordinary entry whose `uri` merely shares a path prefix with its parent's —
  nothing in the listing marks the nesting. The 32-level bound is a resource guard, not a nesting rule.
- **Verbosity is required, not optional.** The entry carries the verbatim frontmatter map; a reader
  that understood only `name:` and `description:` would silently publish the "curated subset" the
  specification forbids.
- This module owns no registration and no protocol: the `mcp` layer turns these values into resources
  and protocol methods, and the `models` layer owns the value types and the entry/index rendering.

### Todos

None recorded.

## Docs References

The Agent Skills specification requires every skill's root file to carry YAML frontmatter with at least
`name` and `description`; SEP-2640 additionally requires an entry's `frontmatter` to be a **verbatim**
rendering of that block, and makes each skill file an MCP resource addressed at its own URI under the
publishing server's origin. Enumeration is the `skills/list` **protocol method** — this module feeds it,
and no index document substitutes for it.

| Finding | Anchor | Source |
| --- | --- | --- |
| Identity is the declared frontmatter name, and skills are addressed as resources under a publishing origin. | `SKILL_ROOT_FILE`; `SKILL_META_PREFIX` | mcp/src/agents_remember/models/skill_resources.py:48-49; mcp/src/agents_remember/models/skill_resources.py:42-43 |
| The entry `skills/list` returns, and the `resources` completeness this module's walk must satisfy. | `entry_document` | mcp/src/agents_remember/models/skill_resources.py:115-130 |
| A `SKILL.md` MAY appear in a descendant directory, so skills nest and are published flat. | `_skill_paths` | mcp/src/agents_remember/application/skill_resources/catalog.py:160-178 |
| The Agent Skills index schema version **this server's own** index emits — a convenience resource, not the enumeration surface. | `SKILL_INDEX_SCHEMA` | mcp/src/agents_remember/models/skill_resources.py:39-40 |

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Discovery and delivery are kept apart: one build records a revision per file, one read re-checks it. | `build_skill_catalog` | mcp/src/agents_remember/application/skill_resources/catalog.py:75-95 |
| Containment is proven before any byte is read, and the recorded revision must still match the bytes. | `read_served_file` | mcp/src/agents_remember/application/skill_resources/catalog.py:117-148 |
| A tree edit cannot quietly delete a published skill: delivery refuses while one is unreadable. | `require_servable`; `unreadable_skills` | mcp/src/agents_remember/application/skill_resources/catalog.py:98-114 |
| The declared name must equal the final skill-path segment — the declared name, not the path, is the identity. | `_read_skill` | mcp/src/agents_remember/application/skill_resources/catalog.py:181-213 |
| The walk descends through a skill directory, so a nested skill is discovered and published flat; the 32-level bound is a resource guard. | `_skill_paths`; `_MAX_SKILL_DEPTH` | mcp/src/agents_remember/application/skill_resources/catalog.py:37-42; mcp/src/agents_remember/application/skill_resources/catalog.py:160-178 |
| A nested skill's files belong to the enclosing skill's entry too, which completeness requires. | `_relative_files` | mcp/src/agents_remember/application/skill_resources/catalog.py:216-234 |
| The value types, the entry and index renderers, and the per-read `_meta` provenance block this module produces. | `SkillResourceFile`; `SkillResourceEntry`; `SkillResourceCatalog`; `skill_meta` | mcp/src/agents_remember/models/skill_resources.py:59-73; mcp/src/agents_remember/models/skill_resources.py:76-130; mcp/src/agents_remember/models/skill_resources.py:146-250; mcp/src/agents_remember/models/skill_resources.py:253-267 |
| The frontmatter reader this module refuses a non-conforming skill through, and the verbatim map it returns. | `parse_skill_frontmatter`; `SkillFrontmatter` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:40-71 |
| The served corpus and its publishing origin, bound together. | `SkillSourceTree`; `shipped_skill_tree` | mcp/src/agents_remember/application/skill_resources/provider.py:49-53; mcp/src/agents_remember/application/skill_resources/provider.py:39-47 |
| The registration layer that turns these values into MCP resources and the two protocol methods. | `skill_file_resource`; `index_resource`; `install_extension_methods` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:194-251; mcp/src/agents_remember/mcp/registration/skills_extension.py:133-153 |
| The cases that execute the containment, revision, unreadable-refusal and nesting rules. | `test_a_catalog_record_that_escapes_its_skill_directory_is_refused`; `test_a_read_refuses_a_body_whose_bytes_changed_since_the_catalog`; `test_the_index_reader_refuses_while_a_skill_cannot_be_served`; `test_a_nested_skill_is_published_flat_like_any_other` | mcp/tests/test_capsule_serving.py:1321-1321; mcp/tests/test_capsule_serving.py:796-796; mcp/tests/test_capsule_serving.py:1348-1348; mcp/tests/test_capsule_serving.py:1489-1489 |
| The traversal case that reads a path outside a skill directory from a live process. | `test_the_server_process_never_serves_a_file_outside_a_skill_directory` | mcp/tests/test_capsule_serving.py:1268-1268 |

## Cross-Repo References

No meaningful cross-repository reference applies. The served tree is this repository's own generated
package-data copy of its canonical `skills/` tree.

## Update History

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: refreshed this card against the
  settled candidate. **Corrected the nesting contract**: `_MAX_SKILL_DEPTH` is 32 and the walk descends
  *through* a skill directory — a nested `SKILL.md` is discovered and published flat, and the depth
  bound is a resource guard rather than a "skills never nest" rule. Recorded that the entry now carries
  the **verbatim** frontmatter (so the reader's job is completeness, not a two-field subset), that a
  nested skill's files belong to the enclosing entry as well, that `byte_length` is the entry's `size`,
  and that `require_servable`'s refusal surfaces as `-32602` through the method handlers. Re-anchored
  every citation range against the current 292-line source, replaced the containment case reference with
  the one that drives the guard directly, and added the nesting, completeness and frontmatter rows.
  Verification metadata remains closeout-owned; no acceptance claim is made.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the SEP-2640 discovery
  registry and revision-checked delivery half. Recorded the named-identity rule, containment proven
  before the read, the recorded-revision re-check on every delivery, and the recorded-not-dropped
  unreadable-skill gate. Its "skills never nest" claim is corrected above.

