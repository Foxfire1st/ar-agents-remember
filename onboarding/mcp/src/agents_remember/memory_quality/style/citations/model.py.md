# mcp/src/agents_remember/memory_quality/style/citations/model.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Shared citation value and anchor/source grammar for conversion and converted card authoring. Document traversal, occurrence matching and prose-delimiter scanning are no longer owned here.

## Code Commentary

### Logic

Module-level surface:

The live reader recognizes additional Lean name spellings when the row cites Lean. `Anchor` records a grammar for those extended names and `Claim` retains ordered source paths. `CitationReader.FORMAT_1` preserves historical format 1 language selection.

- `Anchor` (class) — One thing a claim asserts the cited lines contain, and how it is matched.





- `Citation` (class) — One ``path:start-end``, as written and as numbers.
- `Claim` (class) — One citation as parsed, wherever it was written.
- `masked` (function) — ``text`` with every code span blanked, so a scan outside them cannot see in.
- `code_span_texts` (function) — The contents of each code span, delimiters stripped whatever their run length.
- `anchors_in` (function) — ``(anchors, count of backticked spans that are not anchors)``.
- `unescape_quote` (function) — Unescape only quote-grammar escapes; leave paths and ``\n``-like text literal.
- `split_segments` (function) — The segments of a source list, splitting only on separators OUTSIDE a code span.
- `unwrapped` (function) — ``piece`` with an enclosing code span removed, if it is entirely one.
- `repo_relative` (function)
- `citations_in` (function) — Ranged citations and other source segments in written order.



### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- An Anchor records the asserted text and locator kind, with an optional grammar for extended Lean spellings. [1]







- A Citation retains the source path and numeric range. [7]


- A Claim retains the row's anchors, ranged citations and ordered local source paths. [8]


- Code spans are masked before scanning the surrounding text. [9]



- The code span iterator strips its delimiters and yields the contained text. [10]



- The anchor parser returns the recognized anchors and the count of unrecognized code spans. [11]



- Quoted text is unescaped using the quote grammar. [12]



- The separator scan keeps a delimiter inside protected text within its segment. [13]



- A complete enclosing code span is unwrapped for source parsing. [14]



- Local source paths must be confined repository-relative paths. [15]



- The source parser returns ranged citations and other source segments in written order. [16]
