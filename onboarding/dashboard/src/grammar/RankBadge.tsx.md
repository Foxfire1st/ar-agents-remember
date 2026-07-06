# dashboard/src/grammar/RankBadge.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/RankBadge.tsx`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T23:56:00+02:00                           |
| lastVerifiedCommitHash | `278a7bf789ceca4378b0de44ba9fae4ec2f1d4b2`       |
| lastVerifiedCommitDate | 2026-07-06T13:30:12+02:00|
| governingOverview      | `overview.md`                                    |

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
chevrons) — with only the rendered `width`/`height` changing per size: `row` is 16px wide (task
rows), `sm` ~13px (the Chats group headers / rail-scale use), via the `DIMENSIONS` table. A Panda
`cva` keys the tier colour (`color: gold` / `color: purple` tokens, L14 palette additions) plus a
soft `drop-shadow` glow mixed from the same token; chevron paths stroke `currentColor` (the cva
base sets `fill:none`, `strokeWidth:1.9`, round caps/joins on `& path`), while the pip carries an
inline `style={{ fill: "currentColor", stroke: "none" }}` because an inline style is what outranks
the stylesheet's `fill:none` path rule.

### Invariants And Boundaries

Presentational and `aria-hidden` (the surrounding row/header text carries the meaning);
`data-rank-tier` / `data-rank-size` are the test + styling hooks. The glyph anatomy is the
contract with the approved L14 sketch (`l14-sketches.html`, V4): pip + three chevrons vs two
chevrons — do not restyle per call-site; consumers pick only `tier` and `size`. Both the tasks
list (`LifecycleList`, size `row`) and the Chats command tree (`SessionList` group headers, size
`sm`) must render rank through this one component.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The gold/purple tier tokens (+dim/ghost) this badge colours by. | theme.tokens.colors | [panda.config.ts](agents-remember/dashboard/panda.config.ts) |
| Task rows render the badge at `row` size beside the state dot, keyed by `OperationRow.tier`. | render body + `commandFacts` | [LifecycleList.tsx](../panels/LifecycleList.tsx) |
| Chats group headers render the badge at `sm` size from `SessionGroup.tier`. | group header button | [SessionList.tsx](../panels/SessionList.tsx) |
| Glyph-anatomy and sizing tests. | all cases | [RankBadge.test.tsx](RankBadge.test.tsx) |

## Update History

- 2026-07-06T23:56:00+02:00 — 260703-L14 (visual hierarchy + chat grouping): created — the V4 chevron
  rank insignia (gold 3-chevron + pip orchestration tier, purple 2-chevron management tier; `row`
  16px / `sm` ~13px; Panda cva colour + glow over the new gold/purple tokens), shared by the tasks
  list and the Chats command tree. Verification metadata pinned until closeout stamps the L14 commit.
