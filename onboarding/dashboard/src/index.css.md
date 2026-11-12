# dashboard/src/index.css

## Governing Overview

[dashboard/src overview](overview.md)

## Purpose

The Panda **entry** + the global non-component layers (the layered blueprint). Declares the cascade
layer order and holds `reset` / `base` / `effects` — the layers Panda does not own.

## Code Commentary

### Logic

`@layer reset, base, effects, tokens, recipes, utilities;` is the exact current order. Panda injects tokens/recipes/utilities; this entry owns reset, base and the empty effects slot. There is no webtui slot or styles/webtui.css import owner. The global keyframes are `pulse` (shared alarm) and `pulseSlow` (2.4-second slow state pulse); canvas motion belongs to GSAP/Motion, not restored CSS keyframes. Removed scanline/vignette/flicker and canvas rotation/powerup rules remain removed. The current root overflow policy is `html, body { overflow-wrap: break-word }`; raw-id spans choose their own character breaking.

The unlayered `html[data-effects="off"]` rules, including pseudo-elements, freeze animations/transitions with !important. The travelling conduit packet and warp surge have no settled end-state and are hidden under the freeze. No animation carve-out is introduced.

**Historical RV-1 account — the scoped WebTUI owner and corrective selector described next are not current cascade requirements.** The original computed-value findings and the general causal lesson remain qualified to that historical UI epoch.

**RV-1 — the `@webtui/css` `word-break: break-all` cascade trap (260718-CHATS-L5P, LOAD-BEARING).**
`@webtui/css`'s base layer sets `body, html { word-break: break-all }` (it lands in the `webtui` layer,
and postcss-prefix-selector ALSO rewrites that `body,html` rule onto the `[data-view="sessions"]` cockpit
scope root at build time). `word-break: break-all` permits a break between ANY two characters regardless
of `overflow-wrap` — so **every component-level `overflow-wrap` patch was INERT in render** (the Inspector
headers/values, the rail footer, the keyboard-overlay footer, and prose all still broke mid-word:
`CAPABILI/TIES`, `thi/s`, `termi/nal`, `Be bri/ef`). The remedy is ONE unlayered root override in
`index.css` — `html, body, [data-view="sessions"] { word-break: normal; overflow-wrap: break-word }` —
which wins over webtui's LAYERED rule (unlayered beats layered for non-`!important` declarations) and
whose `normal` descendants inherit. `[data-view="sessions"]` MUST be in the selector because the sessions
scope carries its OWN postcss-rewritten `break-all` that an `html/body` override alone does not reach.
Raw-id / hash spans that WANT character breaking keep their own explicit `word-break: break-all` (a direct
rule on the span overrides this inherited default — e.g. `engine-room/DiagnosticsPanel.tsx`,
`engineRoomStyles.ts nodeBranch`). **The durable lesson: a third-party scoped reset in a lower layer can
silently defeat local overflow-wrap patches app-wide; the test is COMPUTED-VALUE verification (assert
`word-break: normal` on the scope root + descendants, and `break-all` on the retained raw-id span), not
inference from the source rule.** The reviewer's final closure DOM-measured zero `break-all` elements in
the whole rendered document with the retained raw-id spans still computing `break-all`.

### Conventions

Cascade layers, not specificity, order the cascade; effect/determinism rules sit unlayered + `!important` so
they win regardless. Token values are read as `var(--…)` from `styles/tokens.css` during the migration.
The earlier RV-1 unlayered override was a remedy for the now-removed scoped WebTUI reset, not a current dependency. Computed-value verification remains the general lesson; the present overflow rule is the source-owned root policy above.

### Invariants And Boundaries

Effects stay global and isolated, never per-component. Base/utility rules still read styles/tokens.css variables; component styling belongs to Panda. The current layer inventory must not grow a removed webtui slot. The effects-off freeze stays unlayered/top-level and covers pseudo-elements. Canvas animation remains GSAP/Motion; pulse/pulseSlow remain the only source-declared global keyframes, with no restoration of paseoAgentSpin, powerup or the removed canvas keyframes. Historical WebTUI-specific test/consumer requirements do not become current source owners.

### 2026-07-24 Curator Delta

The former CRT overlay avoided full-screen `mix-blend-mode:multiply` because that treatment forced
whole-screen re-raster on scroll, video and animation invalidations. That causal performance lesson
is historical: the overlay element, scanline/vignette rule and flicker keyframe are now removed.
It is not a current instruction to mount or retain a static compositor overlay.

## Evidence

### Repo-Internal References

The current source extents below record the reviewed UI contract. Inline test names/facets are source-bound evidence; the installed writer cannot create typed proves from those call titles, and these citations do not claim such a proof or a rerun.

- Exact current six-layer order, root overflow and global pulse/freeze rules; removed WebTUI is not a current owner. [6]

- The `:root` vars referenced by the base layer. [1]
- The Panda PostCSS plugin that fills the layers. [2]
