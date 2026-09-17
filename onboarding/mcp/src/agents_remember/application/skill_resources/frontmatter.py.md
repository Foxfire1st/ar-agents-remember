# mcp/src/agents_remember/application/skill_resources/frontmatter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/skill_resources/frontmatter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Purpose

Reads a `SKILL.md` YAML frontmatter block into **the JSON object SEP-2640 requires**: the specification's
§Enumeration via `skills/list` says an entry's `frontmatter` must be *"a verbatim copy of the skill's
`SKILL.md` YAML frontmatter, rendered as JSON … every field the author wrote, not a curated subset"*,
with `license`, `metadata` and fields added by future revisions of the Agent Skills specification
passing through unchanged.

That requirement is why this module is a real YAML-subset reader rather than a two-field scraper: a
reader that understood only `name:` and `description:` would silently drop the rest, which is exactly
the curated subset the specification forbids. It implements block mappings, block sequences, nested
indentation, flow sequences and mappings, quoted and plain scalars, comments, and block scalars.

It is deliberately a reader, **not a general YAML engine**: it refuses the constructs it does not
implement — anchors, aliases, tags, explicit keys and merge keys — rather than guessing, because a
silently mistranslated frontmatter is the same defect as a curated subset.

Reading is otherwise **total over its input**: a file with no frontmatter, an unclosed block, or no
usable `name` is reported as an unreadable skill by the caller instead of being served under a guessed
identity.

## Code Commentary

### Logic

- `parse_skill_frontmatter(text)` extracts the leading `---`-fenced block (`_frontmatter_block`,
  refusing a file that does not open with the fence or whose block never closes), reads it through
  `_MappingReader` into a nested dict, and returns `SkillFrontmatter(name, description, fields)`.
- It refuses an empty `name` and an empty `description`. The description refusal is not cosmetic: the
  description is the one field a host surfaces **before** it loads a body, so a skill that cannot
  describe itself cannot be discovered without loading it — the exact property the discovery registry
  exists to preserve.
- `_MappingReader` reads one block mapping plus the nested values its entries open; `_indent_of` and
  `_content` handle indentation and trailing comments (comments are stripped only from plain scalars,
  so a `#` inside a quoted value survives). `_scalar`, `_flow_mapping`, `_split_flow` and `_unquote`
  cover the scalar and flow forms.
- `_reject_unsupported` refuses the unimplemented YAML constructs by their value prefixes
  (`_UNSUPPORTED_PREFIXES` = anchors `&`, aliases `*`, tags `!`, merge keys `<<:`), naming the key and
  construct in the error.
- `SkillFrontmatter.get(key)` reads any field the caller needs; the catalog uses it for `allowed-tools`.

### Conventions

The parse is intentionally permissive about extra keys and strict about the two required ones. Errors
are one typed exception (`SkillFrontmatterError(ValueError)`) with a message naming the offending skill,
because the catalog wraps it into an `UnreadableSkill` reason that an operator reads.

### Invariants And Boundaries

- **The returned map is verbatim, not curated.** `fields` carries every key the author wrote, because
  that map is what `skills/list` publishes. Anything this reader drops is a specification violation,
  not a simplification.
- **Unimplemented constructs are refused, never guessed.** Anchors, aliases, tags, explicit keys and
  merge keys raise; a wrong-but-plausible expansion would be published as the skill's frontmatter.
- **The skill name is never inferred from the directory name here.** SEP-2640 makes the *declared* name
  the identity; the catalog separately enforces that the declared name equals the final path segment,
  so both halves of the rule are checked in the layer that owns them.
- **No YAML dependency.** A general engine would change the repository's dependency surface; the
  bounded subset plus explicit refusal is sufficient for this corpus and keeps the failure mode loud.
- A non-conforming skill is reported, never served — the caller turns the exception into an unreadable
  entry, and the whole catalog refuses delivery while one exists.

### Todos

None recorded.

## Docs References

Two specifications meet here: the Agent Skills specification requires a skill's root file to open with
YAML frontmatter carrying at least `name` and `description`, and SEP-2640 requires that block to be
republished verbatim as an entry's `frontmatter`.

| Finding | Anchor | Source |
| --- | --- | --- |
| An entry's `frontmatter` is a **verbatim copy** of the skill's `SKILL.md` frontmatter rendered as JSON — "every field the author wrote, not a curated subset". | `SkillFrontmatter`; `_MappingReader` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:40-46; mcp/src/agents_remember/application/skill_resources/frontmatter.py:97-100 |
| A host MUST NOT honor a skill's declared `allowed-tools`; the value is an observation. | `ALLOWED_TOOLS_KEY` | mcp/src/agents_remember/models/skill_resources.py:45-46 |
| The entry shape the verbatim map feeds. | `entry_document` | mcp/src/agents_remember/models/skill_resources.py:115-130 |

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The parse refuses a missing or unclosed block and then requires usable `name` and `description`. | `parse_skill_frontmatter`; `_frontmatter_block` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:52-81 |
| An empty description is refused because it is the field discovery surfaces before a body is loaded. | `parse_skill_frontmatter` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:52-71 |
| The nested mapping reader that makes the returned map verbatim rather than a scalar subset. | `_MappingReader`; `_indent_of`; `_content` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:84-100 |
| Unimplemented YAML constructs are refused by value prefix rather than guessed. | `_reject_unsupported`; `_UNSUPPORTED_PREFIXES` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:32-33; mcp/src/agents_remember/application/skill_resources/frontmatter.py:174-185 |
| The scalar and flow forms the reader does implement. | `_scalar`; `_flow_mapping`; `_split_flow`; `_unquote` | mcp/src/agents_remember/application/skill_resources/frontmatter.py:187-249 |
| The consumer that turns a frontmatter refusal into a recorded unreadable skill and carries the verbatim map onto the entry. | `_read_skill` | mcp/src/agents_remember/application/skill_resources/catalog.py:181-213 |
| The frontmatter-derived tool names that reach the registry as declared, never granted. | `SkillResourceEntry.declared_allowed_tools` | mcp/src/agents_remember/models/skill_resources.py:96-96 |
| The case that executes the verbatim-frontmatter requirement end to end. | `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter` | mcp/tests/test_capsule_serving.py:1044-1075 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter` repointed to mcp/tests/test_capsule_serving.py:1044-1075. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: refreshed this card against the
  settled candidate. **The subject changed shape**: this module is no longer a bounded two-field scalar
  reader but a YAML-**subset** reader whose product must be the *verbatim* frontmatter SEP-2640 requires
  an entry to publish ("every field the author wrote, not a curated subset"). Recorded the implemented
  forms (block mappings, block sequences, nested indentation, flow sequences/mappings, quoted and plain
  scalars, comments, block scalars), the deliberate refusal of anchors, aliases, tags, explicit keys and
  merge keys by value prefix, why the refusal is a feature rather than a limitation (a guessed expansion
  would be published as the skill's frontmatter), and that the returned map is now `fields` carrying
  every key. Re-anchored every range against the current 251-line source and recorded that the module
  is substantially larger than the card's first version described. Verification metadata remains
  closeout-owned; no acceptance claim is made.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the skill root-file frontmatter
  reader. Recorded the bounded scalar subset (no YAML dependency), the total-read contract that reports
  rather than guesses, and why an empty description is a refusal rather than a cosmetic check. Its
  "scalar subset" description is superseded above.

