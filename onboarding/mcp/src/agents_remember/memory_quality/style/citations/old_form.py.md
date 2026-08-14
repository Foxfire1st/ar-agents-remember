# mcp/src/agents_remember/memory_quality/style/citations/old_form.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/old_form.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Read the superseded citation format without writing it.

## Code Commentary

### Logic

Module-level surface:

- `Span` (class, lines 32-36) — One range read out of an old document, in the file it was written about.
- `link_targets` (function, lines 39-49) — Every path this Source Path cell names, in order, however it spelled them.
- `path_candidates` (function, lines 52-72) — Every repo-relative spelling of ``target`` worth trying, most specific first.
- `_mirrored` (function, lines 75-87) — ``../src/x.ts`` read against the card's own place in the mirrored tree.
- `resolved_path` (function, lines 90-107) — The one spelling of ``target`` that names a file in either tree, or ``None``.
- `old_span` (function, lines 110-117) — The first ``L`` range in a Citations cell, as numbers. A tiebreaker, never an output.
- `verified_hint` (function, lines 120-130) — ``span`` if EVERY anchor really occurs inside it in ``path``, otherwise ``None``.
- `is_marker` (function, lines 133-135) — Whether a cell is one of the four spellings this tree uses for 'nothing to cite'.
- `marker_of` (function, lines 138-144) — The no-citation marker a table already uses, so a padded row does not invent a fifth.

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
| Defines the class `Span` (lines 32-36) — One range read out of an old document, in the file it was written about.. | `Span` | mcp/src/agents_remember/memory_quality/style/citations/old_form.py:31-36 |
| Defines the function `link_targets` (lines 39-49) — Every path this Source Path cell names, in order, however it spelled them.. | `link_targets` | mcp/src/agents_remember/memory_quality/style/citations/old_form.py:39-49 |
| Defines the function `path_candidates` (lines 52-72) — Every repo-relative spelling of ``target`` worth trying, most specific first.. | `path_candidates` | mcp/src/agents_remember/memory_quality/style/citations/old_form.py:52-72 |
| Defines the function `_mirrored` (lines 75-87) — ``../src/x.ts`` read against the card's own place in the mirrored tree.. | `_mirrored` | mcp/src/agents_remember/memory_quality/style/citations/old_form.py:75-87 |
| Defines the function `resolved_path` (lines 90-107) — The one spelling of ``target`` that names a file in either tree, or ``None``.. | `resolved_path` | mcp/src/agents_remember/memory_quality/style/citations/old_form.py:90-107 |
| Defines the function `old_span` (lines 110-117) — The first ``L`` range in a Citations cell, as numbers. A tiebreaker, never an output.. | `old_span` | mcp/src/agents_remember/memory_quality/style/citations/old_form.py:110-117 |
| Defines the function `verified_hint` (lines 120-130) — ``span`` if EVERY anchor really occurs inside it in ``path``, otherwise ``None``.. | `verified_hint` | mcp/src/agents_remember/memory_quality/style/citations/old_form.py:120-130 |
| Defines the function `is_marker` (lines 133-135) — Whether a cell is one of the four spellings this tree uses for 'nothing to cite'.. | `is_marker` | mcp/src/agents_remember/memory_quality/style/citations/old_form.py:133-135 |
| Defines the function `marker_of` (lines 138-144) — The no-citation marker a table already uses, so a padded row does not invent a fifth.. | `marker_of` | mcp/src/agents_remember/memory_quality/style/citations/old_form.py:138-144 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
