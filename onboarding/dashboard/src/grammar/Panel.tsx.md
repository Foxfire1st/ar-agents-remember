# dashboard/src/grammar/Panel.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/Panel.tsx`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-17T22:45                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`Panel` is the shared panel chrome primitive (slice 5d). It replaces the old global `.panel` +
`.rail > .panel > h2` descendant rules with a self-contained component, so every panel scrolls on
its own and its header sticks without depending on a parent selector. An opt-in `fill` variant lets a
panel that hosts its own internal layout (the Engine Room's 3-zone grid) bound its slot at a fixed
height instead.

## Code Commentary

### Logic

Renders `<section className={cx(shell({ fill }), className)}>` containing a sticky header `band` and the
body `children`. `shell` (Panda `cva`) is the bg/border/radius box with `minHeight:0`; its `fill` variant
switches it between the default self-scrolling block (`display:block` + `overflow:auto`) and a **bounded
flex column** (`display:flex` + `flexDirection:column` + `overflow:hidden`). The flex-column mode lets a
panel fill its slot at a fixed height while its inner columns scroll on their own, instead of the inner
grid sizing to its tallest column's content and the whole panel scrolling. `band` is `position:sticky;
top:0` with negative inline margins that bleed over the horizontal padding for a full-width opaque bg — so
rows scroll **under** the band, never into a gap above it. `Panel` takes a `fill?: boolean` prop (default
`false`); `head` (a ReactNode) overrides the default `<h2>{title}</h2>` (the lifecycle list passes a head
that bundles its pivot).

### Conventions

Panda `css()`/`cva()` + `cx()` from `../../styled-system/css` (relative import; no path alias). The sizing of
the panel within its rail/viewport slot comes from the `className` prop, not from the panel.

### Invariants And Boundaries

Presentational only. The sticky-header contract (flush top, opaque bg, `z-index:2`) is the slice-5d
replacement for the removed `.rail > .panel > h2` rule and must keep rows scrolling under the header. The
`fill` variant is opt-in and backward-compatible (default `false` = the original self-scroll block), so
every existing panel is unchanged; only the Engine Room passes `fill`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Every panel composes this chrome. | L36-L52 | [panels/overview.md](../panels/overview.md) |
| The Engine Room passes `fill` to bound its 3-zone grid. | — | [panels/EngineRoom.tsx](../panels/EngineRoom.tsx) |
| The bg/border tokens it uses. | L1-L46 | [panda.config.ts](agents-remember/dashboard/panda.config.ts) |

## Update History

- 2026-06-17T22:45 — engine-room visual-parity pass: `shell` became a Panda `cva` with an opt-in `fill`
  variant (`display:flex` + `flexDirection:column` + `overflow:hidden` vs the default `display:block` +
  `overflow:auto`); `Panel` gained a `fill?: boolean` prop (default `false`). This binds the Engine Room to a
  fixed height so its centre canvas + right panel stop resizing per selection and the side columns scroll on
  their own. Backward-compatible; other panels are untouched. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-15T17:00 — Created for slice 5d: the shared `Panel` chrome primitive (self-scroll + sticky
  band) replacing the global panel/sticky CSS. Verification metadata pinned until closeout stamps the
  5d code commit.
