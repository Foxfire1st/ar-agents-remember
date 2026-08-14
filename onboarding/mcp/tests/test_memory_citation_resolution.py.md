# mcp/tests/test_memory_citation_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Precision and recall for citation resolution over memory documents (260731-EFA-L6).

## Code Commentary

### Logic

Module-level surface:

- `document` (function, lines 74-76)
- `numbered` (function, lines 79-80)
- `Tree` (class, lines 83-111) — A memory repository and the code repository it documents, both on disk.
- `TreeCase` (class, lines 114-126)
- `FalsePositiveFixtures` (class, lines 129-244) — Every mode the module docstring enumerates, on a construct that exists in the tree.
- `TableFormatTests` (class, lines 247-299) — The superseded shape fails, and the message names the whole migration.
- `SourceGrammarTests` (class, lines 302-367) — `path:start-end` in plain text, and what is reported instead.
- `AnchorGrammarTests` (class, lines 370-449) — The three anchor kinds, each matched by the rule its kind implies.
- `BoundsTests` (class, lines 452-504) — A range past the end of the file its own citation names.
- `AnchorPresenceTests` (class, lines 507-550) — The anchor half, and the hard facts a finding owes the curator.
- `PairingTests` (class, lines 553-578) — Half a citation. Neither half means anything alone.
- `ResolutionTests` (class, lines 581-605) — Two roots, tried in one order.
- `BiteTests` (class, lines 608-647) — L6-R16: every code this check can emit has a probe that provokes it.
- `ProseGrammarTests` (class, lines 650-756) — `cit:([anchors], path:start-end)` in running text, sharing every table rule.
- `MisplacedSerialisationTests` (class, lines 759-813) — A `cit:` in a table cell is the wrong serialisation, and silence there is the defect.
- `SupersededProseTests` (class, lines 816-860) — The spelling `cit:` replaces, and the leaf shorthand it must not swallow.
- `ProseScannerTests` (class, lines 863-885) — The block builder and the bracket walker, which nothing else exercises directly.
- `DeletedClassTests` (class, lines 888-918) — L6-R13: the two classes R27 made unrepresentable are gone, not dormant.
- `StyleSurfaceTests` (class, lines 921-978) — How the check reaches the gate, and what it says when it cannot resolve.
- `OrderingTests` (class, lines 981-1000)

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
| Defines the function `document` (lines 74-76). | `document` | mcp/tests/test_memory_citation_resolution.py:74-76 |
| Defines the function `numbered` (lines 79-80). | `numbered` | mcp/tests/test_memory_citation_resolution.py:79-80 |
| Defines the class `Tree` (lines 83-111) — A memory repository and the code repository it documents, both on disk.. | `Tree` | mcp/tests/test_memory_citation_resolution.py:83-111 |
| Defines the class `TreeCase` (lines 114-126). | `TreeCase` | mcp/tests/test_memory_citation_resolution.py:114-126 |
| Defines the class `FalsePositiveFixtures` (lines 129-244) — Every mode the module docstring enumerates, on a construct that exists in the tree.. | `FalsePositiveFixtures` | mcp/tests/test_memory_citation_resolution.py:129-244 |
| Defines the class `TableFormatTests` (lines 247-299) — The superseded shape fails, and the message names the whole migration.. | `TableFormatTests` | mcp/tests/test_memory_citation_resolution.py:247-299 |
| Defines the class `SourceGrammarTests` (lines 302-367) — `path:start-end` in plain text, and what is reported instead.. | `SourceGrammarTests` | mcp/tests/test_memory_citation_resolution.py:302-367 |
| Defines the class `AnchorGrammarTests` (lines 370-449) — The three anchor kinds, each matched by the rule its kind implies.. | `AnchorGrammarTests` | mcp/tests/test_memory_citation_resolution.py:370-449 |
| Defines the class `BoundsTests` (lines 452-504) — A range past the end of the file its own citation names.. | `BoundsTests` | mcp/tests/test_memory_citation_resolution.py:452-504 |
| Defines the class `AnchorPresenceTests` (lines 507-550) — The anchor half, and the hard facts a finding owes the curator.. | `AnchorPresenceTests` | mcp/tests/test_memory_citation_resolution.py:507-550 |
| Defines the class `PairingTests` (lines 553-578) — Half a citation. Neither half means anything alone.. | `PairingTests` | mcp/tests/test_memory_citation_resolution.py:553-578 |
| Defines the class `ResolutionTests` (lines 581-605) — Two roots, tried in one order.. | `ResolutionTests` | mcp/tests/test_memory_citation_resolution.py:581-605 |
| Defines the class `BiteTests` (lines 608-647) — L6-R16: every code this check can emit has a probe that provokes it.. | `BiteTests` | mcp/tests/test_memory_citation_resolution.py:608-647 |
| Defines the class `ProseGrammarTests` (lines 650-756) — `cit:([anchors], path:start-end)` in running text, sharing every table rule.. | `ProseGrammarTests` | mcp/tests/test_memory_citation_resolution.py:650-756 |
| Defines the class `MisplacedSerialisationTests` (lines 759-813) — A `cit:` in a table cell is the wrong serialisation, and silence there is the defect.. | `MisplacedSerialisationTests` | mcp/tests/test_memory_citation_resolution.py:759-813 |
| Defines the class `SupersededProseTests` (lines 816-860) — The spelling `cit:` replaces, and the leaf shorthand it must not swallow.. | `SupersededProseTests` | mcp/tests/test_memory_citation_resolution.py:816-860 |
| Defines the class `ProseScannerTests` (lines 863-885) — The block builder and the bracket walker, which nothing else exercises directly.. | `ProseScannerTests` | mcp/tests/test_memory_citation_resolution.py:863-885 |
| Defines the class `DeletedClassTests` (lines 888-918) — L6-R13: the two classes R27 made unrepresentable are gone, not dormant.. | `DeletedClassTests` | mcp/tests/test_memory_citation_resolution.py:888-918 |
| Defines the class `StyleSurfaceTests` (lines 921-978) — How the check reaches the gate, and what it says when it cannot resolve.. | `StyleSurfaceTests` | mcp/tests/test_memory_citation_resolution.py:921-978 |
| Defines the class `OrderingTests` (lines 981-1000). | `OrderingTests` | mcp/tests/test_memory_citation_resolution.py:981-1000 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
