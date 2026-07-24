# dashboard/src/main.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/main.tsx`                          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:25+02:00                           |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Panda entry + layer order it loads. | L1-L6 | [index.css](index.css) |
| The `:root` design tokens it loads. | — | [styles/tokens.css](styles/tokens.css) |
| The scoped WebTUI skin it loads third (260715-FEUI-L1). | L12-L15 | [styles/webtui.css](styles/webtui.css) |

## Update History

- 2026-07-24T13:17:50Z — Added the development performance-timeline cleanup boundary. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-17T00:25+02:00 — 260715-FEUI-L1 S1: added the third global stylesheet import,
  `./styles/webtui.css` (the one WebTUI mapping file), after `index.css` so its `layer(webtui)`
  rules land in the slot the layer-order statement declares. Verification metadata pinned to the
  task base until closeout stamps the L1 code commit.
- 2026-06-15T17:00 — Created for slice 5d: now imports `index.css` (the Panda/layers entry) ahead of
  `tokens.css`, and wraps the app in `MotionConfig reducedMotion="user"` (the prefers-reduced-motion
  a11y upgrade). Verification metadata pinned until closeout stamps the 5d code commit.
