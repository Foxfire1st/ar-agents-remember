# mcp/src/agents_remember/memory_quality/style/citations/extents.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/extents.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `../../overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `Extent` (lines 39-49) — One range an anchor occupies in a file, and how it was found.. | `Extent` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:39-49 |
| Defines the class `WordMark` (lines 52-60) — One collapsed word and the byte position it retains from the source.. | `WordMark` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:52-60 |
| Defines the class `CollapsedText` (lines 63-68) — Whitespace-collapsed text whose word marks still identify source bytes.. | `CollapsedText` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:68-73 |
| Defines the class `QuoteMatch` (lines 71-82) — One exact quote occurrence before line-range rendering merges equal extents.. | `QuoteMatch` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:71-82 |
| Defines the function `anchor_extents` (lines 85-91) — Every range in ``lines`` that satisfies ``anchor``, by the rule its kind implies.. | `anchor_extents` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:85-91 |
| Defines the function `symbol_extents` (lines 94-99) — The constructs binding ``name``, or -- failing that -- the lines that mention it.. | `symbol_extents` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:94-99 |
| Defines the function `definitions` (lines 102-116) — Every name this file binds at any depth, and the extent of the construct binding it.. | `definitions` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:102-116 |
| Defines the function `occurrence_runs` (lines 119-129) — Consecutive lines holding the pattern, grouped -- two mentions ten lines apart are two ranges, because one range spanning them would quote eight lines that say nothing.. | `occurrence_runs` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:132-142 |
| Defines the function `heading_extents` (lines 132-135) — The section a heading opens: its own line to the line before the next heading of equal or higher level, or to the end of the document.. | `heading_extents` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:145-148 |
| Defines the function `heading_extents_in` (lines 138-152) — :func:`heading_extents` with the file's heading levels already derived.. | `heading_extents_in` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:138-152 |
| Defines the function `heading_levels` (lines 155-158) — Each unfenced heading line's index and its ``#`` depth.. | `heading_levels` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:168-171 |
| Defines the function `quote_extents` (lines 161-170) — The lines a quoted literal occupies, matched with whitespace collapsed so a source that wraps the sentence still yields the window that holds it.. | `quote_extents` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:174-183 |
| Defines the function `quote_extents_for_path` (lines 173-176) — Quoted extents with parsed-language call-argument widening.. | `quote_extents_for_path` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:186-189 |
| Defines the function `all_quote_matches` (lines 179-199). | `all_quote_matches` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:179-199 |
| Defines the function `quote_match_extents` (lines 202-204) — Render exact occurrences as the unique line extents the citation format stores.. | `quote_match_extents` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:215-217 |
| Defines the function `widened_quotes` (lines 207-230). | `widened_quotes` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:207-230 |
| Defines the function `quote_matches_in` (lines 233-259) — Exact occurrences in one collapsed stream, with source-byte identity retained.. | `quote_matches_in` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:233-259 |
| Defines the function `collapsed` (lines 262-284) — The file as whitespace-collapsed text with each word's line and byte position.. | `collapsed` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:262-284 |
| Defines the function `line_comment_blocks` (lines 287-321) — Contiguous ``//`` blocks with syntax prefixes removed and source lines retained.. | `line_comment_blocks` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:287-321 |
| Defines the function `word_mark_at` (lines 324-339) — The source word containing a non-whitespace collapsed-text offset.. | `word_mark_at` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:324-339 |
| Defines the function `source_line_starts` (lines 342-349) — UTF-8 byte offset of every line in the exact source tree-sitter parses.. | `source_line_starts` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:355-362 |
| Defines the class `FileView` (lines 352-412) — One file, matched against many anchors, with each whole-file derivation done once.. | `FileView` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:352-412 |
| Defines the function `merged` (lines 415-423) — ``spans`` in order with overlapping and adjacent ones fused into one range.. | `merged` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:428-436 |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `CollapsedText` repointed to mcp/src/agents_remember/memory_quality/style/citations/extents.py:68-73. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `occurrence_runs` repointed to mcp/src/agents_remember/memory_quality/style/citations/extents.py:132-142. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `heading_extents` repointed to mcp/src/agents_remember/memory_quality/style/citations/extents.py:145-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `heading_levels` repointed to mcp/src/agents_remember/memory_quality/style/citations/extents.py:168-171. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `quote_extents` repointed to mcp/src/agents_remember/memory_quality/style/citations/extents.py:174-183. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `quote_extents_for_path` repointed to mcp/src/agents_remember/memory_quality/style/citations/extents.py:186-189. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `quote_match_extents` repointed to mcp/src/agents_remember/memory_quality/style/citations/extents.py:215-217. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `source_line_starts` repointed to mcp/src/agents_remember/memory_quality/style/citations/extents.py:355-362. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `merged` repointed to mcp/src/agents_remember/memory_quality/style/citations/extents.py:428-436. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T19:21+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the capability this change adds, which the card did not carry. `Extent` gains a defaulted `declaration` field holding the line a `DEFINITION`'s declaration itself begins on — the `def`/`class` line for a decorated Python definition, whose extent is deliberately widened to cover its decorator, and `None` for every other kind where it coincides with `start`. `definitions` now fills it from `grammars.bindings`, so one walk answers both the widened span and the declaration line. This is the value the reopen check reads (item 14): a card citing a decorated declaration at its own lines is about that construct, and the card's `definitions` description now says so. Documentation only: no source byte was touched by this pass. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are NOT advanced — these sources are uncommitted, so no commit carries their bytes; the candidate is named in the `reviewedWorkingCandidate` metadata row and the governed closeout owns the real commits.
- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive ranges and completed the truncated `occurrence_runs`, `heading_extents`, and `quote_extents` descriptions against the source docstrings; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
