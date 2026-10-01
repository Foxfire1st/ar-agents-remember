# mcp/src/agents_remember/memory/conversion/citations.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**One legacy citation row becomes one reference (MIK-R24 rules 1 and 2).** A row is anchored in the code
tree of its card's anchor commit. Its targets are its bound symbols, its uncovered ranges, and its other
sources. Any anchor text no target carries is kept in the reference's `note`, so no citation information
is lost.

## Code Commentary

### Logic

- **Symbols (`_symbol_targets`).** Each symbol-kind anchor (a backticked identifier) that the shipped
  extractor binds exactly once in one of the row's cited files, tried in citation order, becomes a `symbol`
  target in that file (`CodeObjects.symbol_span` through `extents.qualified_spans`).
- **Ranges (`_source_targets`).** Each `path:start-end` source becomes its own `line_range` target,
  unless a symbol target of the row in the same file lies inside the range or contains it (`_covered`).
  Such a range is counted as covered and adds nothing. The packet's two sentences disagreed here ("lies
  inside" against "already covers"); the worker took both, and a partial overlap keeps the range. A path
  the tree does not hold becomes an `unresolved` target with reason `path-absent`, and a range past the
  file's end `range-outside-file`.
- **Other sources.** A whole file the tree holds becomes a `file` target, a URL an `external` document,
  and anything else `unresolved` (`not-a-source`). A row with no target at all keeps its citation text
  as one `unresolved` target (`no-target`), so no row is silently dropped.
- **Anchors (`_anchor`)** record the blob they were resolved in and `content` computed through
  `models/knowledge_files/anchor_content`, the one definition the writer uses. The anchor carries `path`
  only when it differs from the card's own file, or in a route sidecar. A test file (`is_test_path`) gives
  a `test` target, and anything else a `code` target.
- **The note (`row_reference`, `reference_note`).** The `note` is the row's finding, then, as its own
  paragraph, `Anchor: <text>` holding the anchor text no symbol target carries (`unbound_anchor_text`). That
  covers a quoted literal, a heading, an unbound identifier or any other anchor text, kept byte for byte
  with its separators. Only segments that are exactly a bound symbol's name, and empty markers, are cut.

### Conventions

- `TargetTally` collects the report's counts: targets by kind (`code:symbol`, `test:line_range`, …),
  covered ranges, references keeping anchor text, and every unresolved target with its card and reason.

### Invariants And Boundaries

- **No citation information is lost (architect ruling, 2026-09-29).** A quoted-literal anchor, a heading
  anchor or an unbound identifier keeps its original anchor text in the reference's `note` (a MIK-R21
  shape), beside the `line_range` target that keeps its location. On the real conversion, 8,207 of 31,575
  anchor texts were not carried by a symbol target: 6,023 quoted literals, 530 headings, 1,392 unbound
  identifiers and 262 other code spans. All of them were kept, and the reviewer's independent matcher
  found 0 lost anchor texts and 0 lost sources.
- Targets are de-duplicated, and each is anchored once.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The row-to-reference rules.

- Test paths give `test` targets. [1]
- Symbols bound exactly once in a cited file become symbol targets. [2]
- A range a symbol target lies inside, or that contains it, is covered. [3]
- Ranges, whole files, URLs and unresolved sources. [4]
- An anchor records blob and content; path only when needed. [5]
- The reference: targets, a no-target fallback, and the note. [6]
- Anchor text no target carries is kept byte for byte in the note. [7]
- The fixture rows: several anchors, covered ranges, a quoted anchor, a removed path, a range past the end. [8]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
