# mcp/src/agents_remember/memory_quality/style/citations/extents.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Generate citation ranges for anchors inside one file.

## Code Commentary

### Logic

Module-level surface:

- `Extent` (class, lines 39-49) — One range an anchor occupies in a file, and how it was found. A `DEFINITION` extent also carries `declaration`: the line the declaration itself begins on, which differs from `start` for a decorated Python definition because the extent is widened to cover its decorator (it is `None` for every other kind, where the two coincide).
- `WordMark` (class, lines 52-60) — One collapsed word and the byte position it retains from the source.
- `CollapsedText` (class, lines 63-68) — Whitespace-collapsed text whose word marks still identify source bytes.
- `QuoteMatch` (class, lines 71-82) — One exact quote occurrence before line-range rendering merges equal extents.
- `anchor_extents` (function, lines 85-91) — Every range in ``lines`` that satisfies ``anchor``, by the rule its kind implies.
- `symbol_extents` (function, lines 94-99) — The constructs binding ``name``, or -- failing that -- the lines that mention it.
- `definitions` (function, lines 102-116) — Every name this file binds at any depth, and the extent of the construct binding it, filled from `grammars.bindings` so each `DEFINITION` extent also records the line its declaration begins on.
- `qualified_spans` (function, lines 159-178; MIK-R24) — The distinct extents binding `name` in one file's `definitions`. `Holder.method` is the `method` defined inside a `Holder` definition, so a same-named method of another class does not make the name ambiguous. A symbol anchor names one construct only when exactly one span comes back. It is the one symbol-binding rule: the curator writer (`application/knowledge_writer/code_anchors._bound_spans`, MIK-R12), the conversion (`memory/conversion/code_objects.CodeObjects.symbol_span`, MIK-R24) and the converted-tree reference check (`memory_quality/reference_state`) all call it, so a symbol binds the same way wherever it is resolved. The conversion-format version pins its behaviour (MIK-R24 rule 6).
- `occurrence_runs` (function, lines 119-129) — Consecutive lines holding the pattern, grouped -- two mentions ten lines apart are two ranges, because one range spanning them would quote eight lines that say nothing.
- `heading_extents` (function, lines 132-135) — The section a heading opens: its own line to the line before the next heading of equal or higher level, or to the end of the document.
- `heading_extents_in` (function, lines 138-152) — :func:`heading_extents` with the file's heading levels already derived.
- `heading_levels` (function, lines 155-158) — Each unfenced heading line's index and its ``#`` depth.
- `quote_extents` (function, lines 161-170) — The lines a quoted literal occupies, matched with whitespace collapsed so a source that wraps the sentence still yields the window that holds it.
- `quote_extents_for_path` (function, lines 173-176) — Quoted extents with parsed-language call-argument widening.
- `all_quote_matches` (function, lines 179-199)
- `quote_match_extents` (function, lines 202-204) — Render exact occurrences as the unique line extents the citation format stores.
- `widened_quotes` (function, lines 207-230)
- `quote_matches_in` (function, lines 233-259) — Exact occurrences in one collapsed stream, with source-byte identity retained.
- `collapsed` (function, lines 262-284) — The file as whitespace-collapsed text with each word's line and byte position.
- `line_comment_blocks` (function, lines 287-321) — Contiguous ``//`` blocks with syntax prefixes removed and source lines retained.
- `word_mark_at` (function, lines 324-339) — The source word containing a non-whitespace collapsed-text offset.
- `source_line_starts` (function, lines 342-349) — UTF-8 byte offset of every line in the exact source tree-sitter parses.
- `FileView` (class, lines 352-412) — One file, matched against many anchors, with each whole-file derivation done once.
- `merged` (function, lines 415-423) — ``spans`` in order with overlapping and adjacent ones fused into one range.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Extent` (lines 39-49) — One range an anchor occupies in a file, and how it was found.. [1]
- Defines the class `WordMark` (lines 52-60) — One collapsed word and the byte position it retains from the source.. [2]
- Defines the class `CollapsedText` (lines 63-68) — Whitespace-collapsed text whose word marks still identify source bytes.. [3]
- Defines the class `QuoteMatch` (lines 71-82) — One exact quote occurrence before line-range rendering merges equal extents.. [4]
- Defines the function `anchor_extents` (lines 85-91) — Every range in ``lines`` that satisfies ``anchor``, by the rule its kind implies.. [5]
- Defines the function `symbol_extents` (lines 94-99) — The constructs binding ``name``, or -- failing that -- the lines that mention it.. [6]
- Defines the function `definitions` (lines 102-116) — Every name this file binds at any depth, and the extent of the construct binding it.. [7]
- The one symbol-binding rule, shared by the curator writer, the conversion and the reference check. [8]
- Defines the function `occurrence_runs` (lines 119-129) — Consecutive lines holding the pattern, grouped -- two mentions ten lines apart are two ranges, because one range spanning them would quote eight lines that say nothing.. [9]
- Defines the function `heading_extents` (lines 132-135) — The section a heading opens: its own line to the line before the next heading of equal or higher level, or to the end of the document.. [10]
- Defines the function `heading_extents_in` (lines 138-152) — :func:`heading_extents` with the file's heading levels already derived.. [11]
- Defines the function `heading_levels` (lines 155-158) — Each unfenced heading line's index and its ``#`` depth.. [12]
- Defines the function `quote_extents` (lines 161-170) — The lines a quoted literal occupies, matched with whitespace collapsed so a source that wraps the sentence still yields the window that holds it.. [13]
- Defines the function `quote_extents_for_path` (lines 173-176) — Quoted extents with parsed-language call-argument widening.. [14]
- Defines the function `all_quote_matches` (lines 179-199). [15]
- Defines the function `quote_match_extents` (lines 202-204) — Render exact occurrences as the unique line extents the citation format stores.. [16]
- Defines the function `widened_quotes` (lines 207-230). [17]
- Defines the function `quote_matches_in` (lines 233-259) — Exact occurrences in one collapsed stream, with source-byte identity retained.. [18]
- Defines the function `collapsed` (lines 262-284) — The file as whitespace-collapsed text with each word's line and byte position.. [19]
- Defines the function `line_comment_blocks` (lines 287-321) — Contiguous ``//`` blocks with syntax prefixes removed and source lines retained.. [20]
- Defines the function `word_mark_at` (lines 324-339) — The source word containing a non-whitespace collapsed-text offset.. [21]
- Defines the function `source_line_starts` (lines 342-349) — UTF-8 byte offset of every line in the exact source tree-sitter parses.. [22]
- Defines the class `FileView` (lines 352-412) — One file, matched against many anchors, with each whole-file derivation done once.. [23]
- Defines the function `merged` (lines 415-423) — ``spans`` in order with overlapping and adjacent ones fused into one range.. [24]
