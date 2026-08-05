# mcp/src/agents_remember/memory_quality/style/citations/model.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/model.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Shared citation model and grammar for tables and prose.

## Code Commentary

### Logic

Module-level surface:

- `Anchor` (class, lines 44-56) — One thing a claim asserts the cited lines contain, and how it is matched.
- `documents_in` (function, lines 59-97) — Every document to walk, or just the one named -- refusing a name that matches nothing.
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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `Anchor` (lines 44-56) — One thing a claim asserts the cited lines contain, and how it is matched.. | `Anchor` | mcp/src/agents_remember/memory_quality/style/citations/model.py:44-56 |
| Defines the function `documents_in` (lines 59-97) — Every document to walk, or just the one named -- refusing a name that matches nothing.. | `documents_in` | mcp/src/agents_remember/memory_quality/style/citations/model.py:59-97 |
| Defines the function `normalised` (lines 100-102) — ``text`` with every run of whitespace collapsed, so a wrapped quote still matches.. | `normalised` | mcp/src/agents_remember/memory_quality/style/citations/model.py:100-102 |
| Defines the function `quote_normalised` (lines 105-108) — Quoted-anchor source with only a leading TypeScript line-comment mark removed.. | `quote_normalised` | mcp/src/agents_remember/memory_quality/style/citations/model.py:105-108 |
| Defines the function `whole_identifier` (lines 111-113) — ``symbol`` as a complete identifier -- ``SERVED`` never inside ``SERVED_LIFECYCLE``.. | `whole_identifier` | mcp/src/agents_remember/memory_quality/style/citations/model.py:111-113 |
| Defines the function `occurs_in` (lines 116-127) — Whether the anchor's text is inside ``body``, by the rule its kind implies.. | `occurs_in` | mcp/src/agents_remember/memory_quality/style/citations/model.py:116-127 |
| Defines the class `Citation` (lines 130-137) — One ``path:start-end``, as written and as numbers.. | `Citation` | mcp/src/agents_remember/memory_quality/style/citations/model.py:130-137 |
| Defines the class `Claim` (lines 140-148) — One citation as parsed, wherever it was written.. | `Claim` | mcp/src/agents_remember/memory_quality/style/citations/model.py:140-148 |
| Defines the function `masked` (lines 151-156) — ``text`` with every code span blanked, so a scan outside them cannot see in.. | `masked` | mcp/src/agents_remember/memory_quality/style/citations/model.py:151-156 |
| Defines the function `code_span_texts` (lines 159-167) — The contents of each code span, delimiters stripped whatever their run length.. | `code_span_texts` | mcp/src/agents_remember/memory_quality/style/citations/model.py:159-167 |
| Defines the function `anchors_in` (lines 170-188) — ``(anchors, count of backticked spans that are not anchors)``.. | `anchors_in` | mcp/src/agents_remember/memory_quality/style/citations/model.py:170-188 |
| Defines the function `unescape_quote` (lines 191-193) — Unescape only quote-grammar escapes; leave paths and ``\n``-like text literal.. | `unescape_quote` | mcp/src/agents_remember/memory_quality/style/citations/model.py:191-193 |
| Defines the function `split_segments` (lines 196-212) — The segments of a source list, splitting only on separators OUTSIDE a code span.. | `split_segments` | mcp/src/agents_remember/memory_quality/style/citations/model.py:196-212 |
| Defines the function `unwrapped` (lines 215-226) — ``piece`` with an enclosing code span removed, if it is entirely one.. | `unwrapped` | mcp/src/agents_remember/memory_quality/style/citations/model.py:215-226 |
| Defines the function `repo_relative` (lines 229-230). | `repo_relative` | mcp/src/agents_remember/memory_quality/style/citations/model.py:229-230 |
| Defines the function `citations_in` (lines 233-250) — ``(citations, segments that are not a repo-relative ``path:start-end``)``.. | `citations_in` | mcp/src/agents_remember/memory_quality/style/citations/model.py:233-250 |
| Defines the function `skip_quoted` (lines 253-264) — The index just past the quoted literal opening at ``index``, or just past the mark.. | `skip_quoted` | mcp/src/agents_remember/memory_quality/style/citations/model.py:253-264 |
| Defines the function `matching` (lines 267-291) — The index of the bracket closing the one at ``opener``, or ``None``.. | `matching` | mcp/src/agents_remember/memory_quality/style/citations/model.py:267-291 |

## Update History

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive ranges and completed the truncated `unescape_quote` description against the source docstring; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
