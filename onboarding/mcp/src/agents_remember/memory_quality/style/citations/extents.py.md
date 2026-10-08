# mcp/src/agents_remember/memory_quality/style/citations/extents.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Finds citation extents and quote candidates without silently choosing an ambiguous source match.

## Code Commentary

`FileView` holds source text and extracted definitions; symbol and qualified spans locate declarations, while headings and line-comment blocks provide text extents. `quote_extents_for_path`, `all_quote_matches`, `widened_quotes` and `quote_matches_in` are the current quote APIs; the removed quote_extents/quote_match_extents names are not callable. Normalized/collapsed text retains offset information so a match can map back to source lines. Multiple candidates remain candidates for the citation resolver, not automatic semantic equivalence.

## Evidence

### Repo-Internal References

- `FileView` owns the current boundary described above. [25]
- `qualified_spans` owns the current boundary described above. [26]
- `all_quote_matches` owns the current boundary described above. [27]
- `quote_matches_in` owns the current boundary described above. [28]
