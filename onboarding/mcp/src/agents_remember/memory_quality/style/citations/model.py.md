# mcp/src/agents_remember/memory_quality/style/citations/model.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Shared citation model and grammar for tables and prose, including canonical document selection for both full and selected walks.

## Code Commentary

### Logic

Module-level surface:

- `Anchor` (class, lines 44-56) — One thing a claim asserts the cited lines contain, and how it is matched.
- `documents_in` (function, lines 59-104) — Every document to walk, or just the one named; both paths use `_document_for` and reject non-canonical, escaped, or non-file documents.
- `normalised` (function, lines 100-102) — ``text`` with every run of whitespace collapsed, so a wrapped quote still matches.
- `quote_normalised` (function, lines 105-108) — Quoted-anchor source with only a leading TypeScript line-comment mark removed.
- `whole_identifier` (function, lines 111-113) — ``symbol`` as a complete identifier -- ``SERVED`` never inside ``SERVED_LIFECYCLE``.
- `occurs_in` (function, lines 116-127) — Whether the anchor's text is inside ``body``, by the rule its kind implies.
- `Citation` (class, lines 130-137) — One ``path:start-end``, as written and as numbers.
- `Claim` (class, lines 140-148) — One citation as parsed, wherever it was written.
- `masked` (function, lines 151-156) — ``text`` with every code span blanked, so a scan outside them cannot see in.
- `code_span_texts` (function, lines 159-167) — The contents of each code span, delimiters stripped whatever their run length.
- `anchors_in` (function, lines 170-188) — ``(anchors, count of backticked spans that are not anchors)``.
- `unescape_quote` (function, lines 191-193) — Unescape only quote-grammar escapes; leave paths and ``\n``-like text literal.
- `split_segments` (function, lines 196-212) — The segments of a source list, splitting only on separators OUTSIDE a code span.
- `unwrapped` (function, lines 215-226) — ``piece`` with an enclosing code span removed, if it is entirely one.
- `repo_relative` (function, lines 229-230)
- `citations_in` (function, lines 233-250) — ``(citations, segments that are not a repo-relative ``path:start-end``)``.
- `skip_quoted` (function, lines 253-264) — The index just past the quoted literal opening at ``index``, or just past the mark.
- `matching` (function, lines 267-291) — The index of the bracket closing the one at ``opener``, or ``None``.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Anchor` (lines 44-56) — One thing a claim asserts the cited lines contain, and how it is matched.. [1]
- Defines `documents_in` and `_document_for` — full and selected walks share canonical relative-document and symlink/outside-root validation. [2]
- Defines the function `normalised` (lines 100-102) — ``text`` with every run of whitespace collapsed, so a wrapped quote still matches.. [3]
- Defines the function `quote_normalised` (lines 105-108) — Quoted-anchor source with only a leading TypeScript line-comment mark removed.. [4]
- Defines the function `whole_identifier` (lines 111-113) — ``symbol`` as a complete identifier -- ``SERVED`` never inside ``SERVED_LIFECYCLE``.. [5]
- Defines the function `occurs_in` (lines 116-127) — Whether the anchor's text is inside ``body``, by the rule its kind implies.. [6]
- Defines the class `Citation` (lines 130-137) — One ``path:start-end``, as written and as numbers.. [7]
- Defines the class `Claim` (lines 140-148) — One citation as parsed, wherever it was written.. [8]
- Defines the function `masked` (lines 151-156) — ``text`` with every code span blanked, so a scan outside them cannot see in.. [9]
- Defines the function `code_span_texts` (lines 159-167) — The contents of each code span, delimiters stripped whatever their run length.. [10]
- Defines the function `anchors_in` (lines 170-188) — ``(anchors, count of backticked spans that are not anchors)``.. [11]
- Defines the function `unescape_quote` (lines 191-193) — Unescape only quote-grammar escapes; leave paths and ``\n``-like text literal.. [12]
- Defines the function `split_segments` (lines 196-212) — The segments of a source list, splitting only on separators OUTSIDE a code span.. [13]
- Defines the function `unwrapped` (lines 215-226) — ``piece`` with an enclosing code span removed, if it is entirely one.. [14]
- Defines the function `repo_relative` (lines 229-230). [15]
- Defines the function `citations_in` (lines 233-250) — ``(citations, segments that are not a repo-relative ``path:start-end``)``.. [16]
- Defines the function `skip_quoted` (lines 253-264) — The index just past the quoted literal opening at ``index``, or just past the mark.. [17]
- Defines the function `matching` (lines 267-291) — The index of the bracket closing the one at ``opener``, or ``None``.. [18]
