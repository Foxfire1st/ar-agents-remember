# dashboard/src/grammar/ — Shared Primitives Library Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/grammar/`                         |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-06T23:57:30+02:00                           |
| lastVerifiedCommitHash | `278a7bf789ceca4378b0de44ba9fae4ec2f1d4b2`       |
| lastVerifiedCommitDate | 2026-07-06T13:30:12+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`grammar/` is the **shared primitives library** (note 08 "state grammar" — state carried by colour
+ silhouette, never chrome). Each primitive is a small, reusable React component styled by
co-located Panda `css()` / `cva()`; two wrap React Aria for behavior. Panels and the shell compose
these rather than re-styling raw elements (the slice-5d analogue of the device-management
`libs/` discipline, minus Material).

## Route Model

- `Panel.tsx` — the panel chrome primitive: a self-scrolling box (`overflow:auto`, no top padding)
  with a sticky header **band** (flush at the top so rows scroll under it). Takes `title` or a
  custom `head` (the lifecycle list bundles its pivot there) + a sizing `className`. An opt-in `fill`
  variant swaps the self-scroll block for a bounded flex column (`display:flex` + `overflow:hidden`) — the
  Engine Room uses it to hold a fixed height while its inner columns scroll on their own.
- `ModeBar.tsx` — the viewport switcher: a **React Aria `ToggleButtonGroup`** (single-select
  radiogroup) styled by Panda `_selected` / `_focusVisible` conditions; roving focus + arrow-key
  nav, look unchanged from the old `.modebar`.
- `Dot.tsx` — the state/severity dot: a Panda `cva` mapping lifecycle state / attention severity to
  a colour (unknown → nominal amber).
- `Affordance.tsx` — the display-only action affordance: a Panda `cva` (ready/off) over the reducer's
  precomputed enabled/reason; `aria-disabled`, never mutates (slice 06 enforces).
- `ProgressFill.tsx` — the bottom-up cyan charge fill (task-step / provider-seed progress).
- `TokenGauge.tsx` — the cumulative-token fuel gauge as a dependency-free SVG sparkline (uPlot stays
  deferred to slice 08).
- `Markdown.tsx` — a **memoized** markdown renderer (react-markdown + remark-gfm) for task-doc prose:
  Panda descendant-selector styling, GFM tables wrapped in a horizontal-scroll box, and an `inline`
  variant (unwraps the paragraph) for list items / decision cells. `React.memo` keeps the projection
  tick from re-parsing stable section strings (the source of the scroll-jank it fixed). No raw HTML.
- `RankBadge.tsx` — the rank insignia (260703-L14, the developer-picked V4 chevrons): tier
  `orchestration` = three gold chevrons under a filled command pip, tier `management` = two purple
  chevrons; inline SVG on fixed viewBoxes with a soft token-mixed glow, sizes `row` (16px, task rows)
  and `sm` (~13px, Chats group headers). The ONE insignia component both the tasks tab and the Chats
  command tree render rank through; only ever visible when an orchestration task exists (D3).
  Covered by `RankBadge.test.tsx` (glyph anatomy is the contract).

## Invariants And Boundaries

- **Reusable + presentational** — primitives take data props and render; no store reads, no mutation.
- **Panda + React Aria** — visuals via co-located Panda tokens/conditions; behavior (where present)
  via React Aria. `Panel`'s sticky-header contract replaces the old `.rail > .panel > h2` descendant
  rule — each Panel is self-contained.
- **Determinism-safe** — animations (blocked/alarm `pulse`) use the shared global keyframe and freeze
  under `?effects=off`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The Panda runtime these primitives import (`css`/`cva`/`cx`). | [panda.config.ts](agents-remember/dashboard/panda.config.ts) |
| The React Aria condition reconciliation (data-hovered/-focused). | [panda.config.ts](agents-remember/dashboard/panda.config.ts) |
| The action-availability shape `Affordance` renders. | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |

## Update History

- 2026-07-06T23:57:30+02:00 — 260703-L14 route impact (visual hierarchy + chat grouping): the library
  gained `RankBadge.tsx` (+ `RankBadge.test.tsx`) — the V4 chevron rank insignia (gold orchestration
  / purple management tiers, `row`/`sm` sizes) shared by `panels/LifecycleList` rows and
  `panels/SessionList` group headers, coloured by the new gold/purple Panda tokens. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T03:20+02:00 — No route impact: 260703-L9 reuses `Markdown.tsx` unchanged as the renderer for the task reader's opened notes (the sidecar-view treatment); no grammar primitive was added or modified.
- 2026-06-21T02:44+02:00 — slice 6g: added the `Markdown.tsx` primitive (memoized react-markdown + remark-gfm renderer for task-doc prose; GFM tables, `inline` variant). Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-17T22:45 — engine-room visual-parity: `Panel` gained an opt-in `fill` variant (a bounded flex
  column vs the default self-scroll block) so a panel that hosts its own internal layout — the Engine Room's
  3-zone grid — can hold a fixed height while its columns scroll. Backward-compatible; other primitives
  unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-15T17:00 — Created for slice 5d: the grammar primitives migrated to Panda; new `Panel`
  chrome primitive + `ModeBar` (React Aria). Verification metadata pinned until closeout stamps the
  5d code commit.
