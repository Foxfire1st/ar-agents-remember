# mcp/src/agents_remember/memory_quality/style/citations/repair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/repair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:15+02:00 |
| lastVerifiedCommitHash | `709dd07671b07d85ac49eaf3b77f4609b1e5fc5f` |
| lastVerifiedCommitDate | 2026-09-04T00:53:17+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Plan exact-name tier-1 citation repairs. Generate one extent per anchor and merge only
overlapping/adjacent extents in the same file; never widen discontiguous anchors into one
enclosing range. Search cited files first, then the wider code tree only when the anchor is
absent there. Repoint only a unique exact-name match. Since CCR-R10 (260831-CCR-L10) every
`Repair` also carries the oracle-chosen `ResolvedLocation` per anchor - the extent the
repair actually followed - so the deterministic projection binds the exact resolution without a
second lookup or a second authority.

Renames, deletions, typos, and ambiguity are declined because syntax cannot distinguish them
safely. Tree-wide mode plans only failing citations. Document-scoped normalization also
regenerates passing ranges through `migration._scoped` so verified mention spans are
preserved.

## Code Commentary

### Logic

Module-level surface (decorator-inclusive ranges):

- `ResolvedLocation` (class, lines 41-53) - One anchor's chosen extent exactly as the shared oracle resolved it, carried on `Repair` for the deterministic projection (CCR-R10).
- `Repair` (class, lines 56-61) - The source list `--fix` would write for one claim, plus the resolved locations it followed.
- `Decline` (class, lines 64-74) - Why one claim stays for the curator, and the facts it needs to work it down.
- `Cited` (class, lines 77-82) - One of a claim's sources and the file it named, when that file still exists.
- `targets` (function, lines 85-88)
- `chosen` (function, lines 91-101) - The one extent this citation means, or `None` when the file offers a choice.
- `_Plan` (class, lines 104-120) - One claim's repair as it accumulates: the spans found, the first refusal, and every resolved location.
- `plan` (function, lines 123-139) - The tiebreaker, applied to one claim; returns the sources and the full `ResolvedLocation` tuple.
- `_carried` (function, lines 142-163) - The sources that survive unchanged because nothing here could regenerate them.
- `_place` (function, lines 166-189) - Where this anchor's range comes from: a cited file first, the wider tree second.
- `_place_elsewhere` (function, lines 192-205)
- `_ambiguous_in_file` (function, lines 208-217)
- `_written` (function, lines 220-232) - The generated source list: one range per anchor, merged per file, then what survives.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- Resolution is exact-name only; `ResolvedLocation` records the extent the repair actually
  followed (in-file tiebreaker or tree-wide `Sightings.unique`) so no second lookup or
  second authority can answer the projection differently (CCR-R10).

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `ResolvedLocation` (lines 41-53) - One anchor's chosen extent exactly as the shared oracle resolved it, carried on `Repair` (CCR-R10). | `ResolvedLocation` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:41-53 |
| Defines the class `Repair` (lines 56-61) - The source list `--fix` would write for one claim, plus its resolved locations. | `Repair` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:56-61 |
| Defines the class `Decline` (lines 64-74) - Why one claim stays for the curator, and the facts it needs to work it down. | `Decline` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:64-74 |
| Defines the class `Cited` (lines 77-82) - One of a claim's sources and the file it named, when that file still exists. | `Cited` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:77-82 |
| Defines the function `targets` (lines 85-88). | `targets` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:85-88 |
| Defines the function `chosen` (lines 91-101) - The one extent this citation means, or `None` when the file offers a choice. | `chosen` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:91-101 |
| Defines the class `_Plan` (lines 104-120) - One claim's repair as it accumulates: the spans found, the first refusal, and every resolved location. | `_Plan` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:104-120 |
| Defines the function `plan` (lines 123-139) - The tiebreaker, applied to one claim; returns sources plus the full resolved-location tuple. | `plan` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:123-139 |
| Defines the function `_carried` (lines 142-163) - The sources that survive unchanged because nothing here could regenerate them. | `_carried` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:142-163 |
| Defines the function `_place` (lines 166-189) - Where this anchor's range comes from: a cited file first, the wider tree second. | `_place` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:166-189 |
| Defines the function `_place_elsewhere` (lines 192-205). | `_place_elsewhere` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:192-205 |
| Defines the function `_ambiguous_in_file` (lines 208-217). | `_ambiguous_in_file` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:208-217 |
| Defines the function `_written` (lines 220-232) - The generated source list: one range per anchor, merged per file, then what survives. | `_written` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:220-232 |
| The deterministic projection consumes the resolved locations a `Repair` carries. | `plan_projection` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:167-218 |

## Update History

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: refreshed for the CCR-R10
  deterministic anchor-range projection change-set (code commit 709dd076). Body now reflects the
  new `ResolvedLocation` carrier, `Repair.locations`, the `_Plan.locations`
  accumulator, and the anchor-bearing `add` signature in `_place`/`_place_elsewhere`;
  every module-surface bullet and reference row re-anchored to the post-change source ranges;
  verification metadata pinned to 709dd076.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
