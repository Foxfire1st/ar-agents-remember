# mcp/src/agents_remember/application/skill_resources/frontmatter.py

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

## Evidence

### Docs References

Two specifications meet here: the Agent Skills specification requires a skill's root file to open with
YAML frontmatter carrying at least `name` and `description`, and SEP-2640 requires that block to be
republished verbatim as an entry's `frontmatter`.

- An entry's `frontmatter` is a **verbatim copy** of the skill's `SKILL.md` frontmatter rendered as JSON — "every field the author wrote, not a curated subset". [1]
- A host MUST NOT honor a skill's declared `allowed-tools`; the value is an observation. [2]
- The entry shape the verbatim map feeds. [3]

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

### Repo-Internal References

- The parse refuses a missing or unclosed block and then requires usable `name` and `description`. [4]
- An empty description is refused because it is the field discovery surfaces before a body is loaded. [5]
- The nested mapping reader that makes the returned map verbatim rather than a scalar subset. [6]
- Unimplemented YAML constructs are refused by value prefix rather than guessed. [7]
- The scalar and flow forms the reader does implement. [8]
- The consumer that turns a frontmatter refusal into a recorded unreadable skill and carries the verbatim map onto the entry. [9]
- The frontmatter-derived tool names that reach the registry as declared, never granted. [10]
- The case that executes the verbatim-frontmatter requirement end to end. [11]

### Cross-Repo References

No meaningful cross-repository reference applies.
