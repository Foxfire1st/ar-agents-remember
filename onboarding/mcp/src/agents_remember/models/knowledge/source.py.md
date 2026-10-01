# mcp/src/agents_remember/models/knowledge/source.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The shared source vocabulary: what a knowledge claim points at, in which exact revision of the selected
repository, and via which locator. The anchor is split into a **draft** — what the author decided — and
the **stored** record, which is the draft plus the provenance envelope that recorded it.

## Code Commentary

### Logic

`GitBlobIdentity` is the one v1 source identity (`kind: "git_blob"` plus an object id matching
`GIT_OBJECT_PATTERN`), and `SourceIdentity` is an alias of it. Three locators are declared: `FileLocator`
(`kind: "file"`), `LineRangeLocator` (`kind: "line_range"`, one-based inclusive `start_line`/`end_line`, with a
validator that refuses an `end_line` preceding `start_line`) and `SymbolLocator` (`kind: "symbol"`, nonblank
`language` and `qualified_name`). `SourceLocator` is the discriminated union of the three, keyed on `kind`.

`SourceAnchorDraft` is one attributed location as its author supplies it: a `UUID` `anchor_id`, a
repository-relative `path`, a `SourceIdentity` and a `SourceLocator`. Its
`_require_confined_relative_posix_path` validator refuses a blank path, an absolute or `~`-prefixed path, a
backslash separator, a NUL byte, and any empty, `.` or `..` segment, bounds the length, and — since 260915-KS-L7 —
**delegates the Git-pathspec half to the one shared `require_plain_git_path`**, so a spelling such as
`:(exclude)src/x.py` cannot be stored. `SourceAnchor` subclasses it and adds the `Authorship` envelope, so
provenance cannot be supplied by a caller who is only proposing a location.

**Why the pathspec refusal lands here rather than only at the tree lookup:** a stored path is later handed to
`git ls-tree`, and Git reads a leading `:` as pathspec magic — answering with an error (`:(exclude)`, `:!`) or
about a *different* location (`:(top)`, `:/`). Reporting that answer as an absent path would be a false
statement about the repository. **The glob characters `*`, `?` and `[` are admitted**, because `ls-tree`
addresses them literally; refusing them (this leaf's round-1 predicate) made a legitimate anchor un-authorable
and, through the read path, reported a file the tree really holds as `path_absent`.

`anchor_id` is a real `UUID`, not a pattern-constrained string. This is a repair of an L1 defect: the
field was declared `anchor_id: UUID = Field(pattern=UUID_PATTERN)`, and Pydantic refuses to apply a string
`pattern` constraint to its UUID schema, so **every** anchor construction raised `TypeError: Unable to
apply constraint 'pattern' … for schema of type 'uuid'`. It was latent because no L1 test constructed an
anchor. The canonical stored text is now derived from the parsed value at the storage boundary
(`records.anchor_row` writes `str(anchor.anchor_id)`), exactly as it is for an authorship operation
identity.

### Conventions

A stored locator is a well-formed record even when no resolver currently supports it: a symbol locator remains
readable after the symbol moves, and losing resolvability never erases the claim.

### Invariants And Boundaries

- The blob identity is a Git object identity, **not a copy of the bytes** — there is no second content store here.
- Path shape is checked at the vocabulary boundary; resolution against a real filesystem belongs to the filesystem
  boundary, so an absolute, drive, UNC, backslash or parent-escaping path never reaches a stored record.
- **A draft carries no provenance.** `SourceAnchorDraft` deliberately has no `provenance` field, so the
  admitted application attaches the envelope (`admitted_anchor_request`) and
  `memory/knowledge/anchors.source_anchor_from_draft` is the single construction point for a stored anchor.
**The pathspec half of the path rule is shared, not restated.** `require_plain_git_path` is the one place a
leading-`:` spelling is refused; this model and `PathSeed` both call it, so a spelling the write path refuses
cannot then be presented as a seed that is answered with an absence. The glob characters `*`, `?` and `[` are
admitted on purpose — `ls-tree` addresses them literally — so a legitimate anchor containing one is authorable.

- **An identity is a parsed value, not a formatted string.** A `pattern`-constrained string declaration on a
  `UUID` field is unconstructible rather than merely lax, so a new identifier field must choose one of the
  two shapes deliberately — the L1 defect this file repaired.
- `SourceLocator` is declared *shared* with the selective read/diff contributor (KS-R07/KS-R08): the union is
  designed so that consumer can discriminate on `kind` without a second locator vocabulary. **The read half now
  exists** — `memory/knowledge/read_anchors.py` observes a stored locator through one accessor and reports a
  symbol locator as `unsupported_locator` rather than guessing — and the diff half (KS-R08) does not exist yet.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The single v1 source identity and the alias a caller may name. [1]
- The three locators and the discriminated union over them. [2]
- The draft/stored split, the repository-relative POSIX path rule, and the repaired `UUID` identifier field. [3]
- **The Git-pathspec half of the path rule, delegated to the one shared validator so the write path and the seed path cannot disagree.** [4]
- **The node that measures a pathspec-magic spelling being refused at this boundary and never answered as an absence.** [5]
- The stored `source_anchor` table, its immutability trigger and its canonical column order. [6]
- The codec that derives the canonical identity text and decodes an anchor row through the discriminated union. [7]
- The single construction point that attaches provenance to a draft. [8]
The later requirement packets this vocabulary is declared shared with: requirement packets `KS-R07` and `KS-R08`, which live in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address them.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
