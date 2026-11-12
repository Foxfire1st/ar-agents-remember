# mcp/src/agents_remember/memory_quality/style/citations/model.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Shared citation value and anchor/source grammar for conversion and converted card authoring. Document traversal, occurrence matching and prose-delimiter scanning are no longer owned here.

## Code Commentary

### Logic

Module-level surface:

- `Anchor` (class, lines 42-47) — One thing a claim asserts the cited lines contain, and how it is matched.





- `Citation` (class, lines 50-57) — One ``path:start-end``, as written and as numbers.
- `Claim` (class, lines 60-68) — One citation as parsed, wherever it was written.
- `masked` (function, lines 71-76) — ``text`` with every code span blanked, so a scan outside them cannot see in.
- `code_span_texts` (function, lines 79-87) — The contents of each code span, delimiters stripped whatever their run length.
- `anchors_in` (function, lines 90-108) — ``(anchors, count of backticked spans that are not anchors)``.
- `unescape_quote` (function, lines 111-113) — Unescape only quote-grammar escapes; leave paths and ``\n``-like text literal.
- `split_segments` (function, lines 116-132) — The segments of a source list, splitting only on separators OUTSIDE a code span.
- `unwrapped` (function, lines 135-146) — ``piece`` with an enclosing code span removed, if it is entirely one.
- `repo_relative` (function, lines 149-150)
- `citations_in` (function, lines 153-170) — ``(citations, segments that are not a repo-relative ``path:start-end``)``.



### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Anchor` (lines 42-47) — One thing a claim asserts the cited lines contain, and how it is matched. [1]






- Defines the class `Citation` (lines 50-57) — One ``path:start-end``, as written and as numbers. [7]

- Defines the class `Claim` (lines 60-68) — One citation as parsed, wherever it was written. [8]

- Defines the function `masked` (lines 71-76) — ``text`` with every code span blanked, so a scan outside them cannot see in. [9]

- Defines the function `code_span_texts` (lines 79-87) — The contents of each code span, delimiters stripped whatever their run length. [10]

- Defines the function `anchors_in` (lines 90-108) — ``(anchors, count of backticked spans that are not anchors)``. [11]

- Defines the function `unescape_quote` (lines 111-113) — Unescape only quote-grammar escapes; leave paths and ``\n``-like text literal. [12]

- Defines the function `split_segments` (lines 116-132) — The segments of a source list, splitting only on separators OUTSIDE a code span. [13]

- Defines the function `unwrapped` (lines 135-146) — ``piece`` with an enclosing code span removed, if it is entirely one. [14]

- Defines the function `repo_relative` (lines 149-150). [15]

- Defines the function `citations_in` (lines 153-170) — ``(citations, segments that are not a repo-relative ``path:start-end``)``. [16]
