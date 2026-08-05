# mcp/src/agents_remember/memory_quality/style/citations/repair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/repair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Plan exact-name tier-1 citation repairs.

## Code Commentary

### Logic

Module-level surface:

- `Repair` (class, lines 42-45) — The source list ``--fix`` would write for one claim.
- `Decline` (class, lines 49-58) — Why one claim stays for the curator, and the facts it needs to work it down.
- `Cited` (class, lines 62-66) — One of a claim's sources and the file it named, when that file still exists.
- `targets` (function, lines 69-72)
- `chosen` (function, lines 75-85) — The one extent this citation means, or ``None`` when the file offers a choice.
- `_Plan` (class, lines 89-102) — One claim's repair as it accumulates: the spans found, and the first refusal.
- `plan` (function, lines 105-118) — The tiebreaker, applied to one claim.
- `_carried` (function, lines 121-142) — The sources that survive unchanged because nothing here could regenerate them.
- `_place` (function, lines 145-168) — Where this anchor's range comes from: a cited file first, the wider tree second.
- `_place_elsewhere` (function, lines 171-184)
- `_ambiguous_in_file` (function, lines 187-196)
- `_written` (function, lines 199-211) — The generated source list: one range per anchor, merged per file, then what survives.

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
| Defines the class `Repair` (lines 42-45) — The source list ``--fix`` would write for one claim.. | `Repair` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:42-45 |
| Defines the class `Decline` (lines 49-58) — Why one claim stays for the curator, and the facts it needs to work it down.. | `Decline` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:49-58 |
| Defines the class `Cited` (lines 62-66) — One of a claim's sources and the file it named, when that file still exists.. | `Cited` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:62-66 |
| Defines the function `targets` (lines 69-72). | `targets` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:69-72 |
| Defines the function `chosen` (lines 75-85) — The one extent this citation means, or ``None`` when the file offers a choice.. | `chosen` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:75-85 |
| Defines the class `_Plan` (lines 89-102) — One claim's repair as it accumulates: the spans found, and the first refusal.. | `_Plan` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:89-102 |
| Defines the function `plan` (lines 105-118) — The tiebreaker, applied to one claim.. | `plan` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:105-118 |
| Defines the function `_carried` (lines 121-142) — The sources that survive unchanged because nothing here could regenerate them.. | `_carried` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:121-142 |
| Defines the function `_place` (lines 145-168) — Where this anchor's range comes from: a cited file first, the wider tree second.. | `_place` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:145-168 |
| Defines the function `_place_elsewhere` (lines 171-184). | `_place_elsewhere` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:171-184 |
| Defines the function `_ambiguous_in_file` (lines 187-196). | `_ambiguous_in_file` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:187-196 |
| Defines the function `_written` (lines 199-211) — The generated source list: one range per anchor, merged per file, then what survives.. | `_written` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:199-211 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
