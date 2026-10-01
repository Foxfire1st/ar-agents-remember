# dashboard/src/grammar/Panel.tsx

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
`fill` variant is opt-in and backward-compatible (default `false` = the original self-scroll block); the
Engine Room uses it for its internal 3-zone layout, while other callers use the ordinary panel surface or
their own layout props.

## Evidence

### Repo-Internal References

- `Panel` is the shared panel chrome primitive. [1]
- The Engine Room passes `fill` to bound its 3-zone grid. [2]
- The Panel shell uses the `bgPanel` background and `grid` border tokens in its styles. [3]
