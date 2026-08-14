# mcp/tests/test_citation_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Tests for path citations in package comments and docstrings.

## Code Commentary

### Logic

Module-level surface:

- `_cited` (function, lines 26-30) — The in-grammar citations the rule finds in a docstring, as their raw text.
- `_commented` (function, lines 33-37) — The same, for a ``#`` comment.
- `CitationResolutionTests` (class, lines 40-68) — The armed check. It runs in the ordinary suite, so it runs wherever the suite does.
- `CitationGrammarTests` (class, lines 71-166) — The grammar has to reach a broken citation, or the check is a no-op.
- `CitationFalsePositiveTests` (class, lines 169-280) — Measured known-good constructs. None of these may EVER be reported.
- `OffenderReportTests` (class, lines 283-301) — L6-R15: the message names every offender and the fix, or the check is unusable.

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
| Defines the function `_cited` (lines 26-30) — The in-grammar citations the rule finds in a docstring, as their raw text.. | `_cited` | mcp/tests/test_citation_resolution.py:26-30 |
| Defines the function `_commented` (lines 33-37) — The same, for a ``#`` comment.. | `_commented` | mcp/tests/test_citation_resolution.py:33-37 |
| Defines the class `CitationResolutionTests` (lines 40-68) — The armed check. It runs in the ordinary suite, so it runs wherever the suite does.. | `CitationResolutionTests` | mcp/tests/test_citation_resolution.py:40-68 |
| Defines the class `CitationGrammarTests` (lines 71-166) — The grammar has to reach a broken citation, or the check is a no-op.. | `CitationGrammarTests` | mcp/tests/test_citation_resolution.py:71-166 |
| Defines the class `CitationFalsePositiveTests` (lines 169-280) — Measured known-good constructs. None of these may EVER be reported.. | `CitationFalsePositiveTests` | mcp/tests/test_citation_resolution.py:169-280 |
| Defines the class `OffenderReportTests` (lines 283-301) — L6-R15: the message names every offender and the fix, or the check is unusable.. | `OffenderReportTests` | mcp/tests/test_citation_resolution.py:283-301 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
