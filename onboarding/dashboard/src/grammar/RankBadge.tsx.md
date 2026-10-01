# dashboard/src/grammar/RankBadge.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`RankBadge` is the **rank insignia** primitive (260703-L14, the developer-picked V4 treatment):
military chevron badges for the two command tiers of an orchestrated run. Tier `orchestration`
(the sprint's orchestration task) renders three gold chevrons under a **filled command pip**;
tier `management` (a master commanded by that task) renders two purple chevrons. Insignia are
never decoration on a leaf — the tier encodes the real orchestration > master > leaf hierarchy,
and per the D3 ruling a badge only ever appears when an orchestration task exists (flat runs
carry no insignia anywhere).

## Code Commentary

### Logic

One component, `RankBadge({ tier, size = "row" })`. The glyphs are crisp inline SVG on fixed
viewBoxes — `0 0 16 17` for orchestration (pip + 3 chevrons), `0 0 16 12` for management (2
chevrons) — with only the rendered `width`/`height` changing per size: `row` is 16px wide and is the
sole production size today; `sm` is the still-supported, test-pinned ~13px dimension with no current
production caller. Both resolve through the `DIMENSIONS` table. A Panda
`cva` keys the tier colour (`color: gold` / `color: purple` tokens, L14 palette additions) plus a
soft `drop-shadow` glow mixed from the same token; chevron paths stroke `currentColor` (the cva
base sets `fill:none`, `strokeWidth:1.9`, round caps/joins on `& path`), while the pip carries an
inline `style={{ fill: "currentColor", stroke: "none" }}` because an inline style is what outranks
the stylesheet's `fill:none` path rule.

### Invariants And Boundaries

Presentational and `aria-hidden` (the surrounding row/header text carries the meaning);
`data-rank-tier` / `data-rank-size` are the test + styling hooks. The glyph anatomy is the
contract with the approved L14 sketch (`l14-sketches.html`, V4): pip + three chevrons vs two
chevrons — do not restyle per call-site; consumers pick only `tier` and `size`. `LifecycleList` is
the sole production consumer and renders `size="row"`. Neither `SessionRail` nor any retired
`SessionList` surface imports this component; `sm` remains a supported/tested option only.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The gold/purple tier tokens (+dim/ghost) this badge colours by. [1]
- Task rows render the badge at `row` size beside the state dot, keyed by `OperationRow.tier`. [2]
- Import census confirms `LifecycleList` is the sole production consumer; the session rail does not import `RankBadge`. [3]
- Glyph-anatomy and both-size tests keep `sm` supported even though production currently uses only `row`. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
