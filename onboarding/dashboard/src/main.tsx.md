# dashboard/src/main.tsx

## Governing Overview

[dashboard/src overview](overview.md)

## Purpose

The Vite entry: mounts `<App>` into `#root` (StrictMode) and loads the global stylesheets.

## Code Commentary

### Logic

Imports `./index.css` (the Panda entry + reset/base/effects layers) then `./styles/tokens.css` (the
`:root` design-token vars), and — 260715-FEUI-L1 S1 — `./styles/webtui.css` (the scoped WebTUI skin
for the sessions cockpit) third, AFTER index.css so the layer-order statement there (`reset, base,
effects, webtui, tokens, recipes, utilities`) governs where its `layer(webtui)` rules land. Sets `document.documentElement.dataset.effects = "off"`
when `?effects=off` or `localStorage["calm-cockpit"]==="1"` (the determinism flag), before render.
Wraps `<App>` in Motion's `<MotionConfig reducedMotion="user">` so transform-heavy animation yields
to opacity-led motion when the OS `prefers-reduced-motion` is set (the slice-5d accessibility
upgrade, complementing the manual `effects=off` freeze).

### Invariants And Boundaries

Import order: `index.css` (declares the cascade-layer order) before `tokens.css`; CSS-var resolution
is order-independent regardless. The effects flag is read once at boot.

### 2026-07-24 Curator Delta

Development builds now periodically clear React's accumulating performance marks and measures. The
minute janitor is dev-only, preventing a long-running cockpit tab from retaining an unbounded timeline
while leaving production bundles and live DevTools recording behavior untouched.

## Evidence

### Repo-Internal References

- The Panda entry + layer order it loads. [1]
- The `:root` design tokens it loads. [2]
- The scoped WebTUI skin it loads third (260715-FEUI-L1). [3]
