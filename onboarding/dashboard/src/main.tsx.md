# dashboard/src/main.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/main.tsx`                          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:25+02:00                           |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`       |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The Panda entry + layer order it loads. | "@layer reset" | dashboard/src/index.css:9-9 |
| The `:root` design tokens it loads. | ":root" | dashboard/src/styles/tokens.css:5-5 |
| The scoped WebTUI skin it loads third (260715-FEUI-L1). | "base.css" | dashboard/src/styles/webtui.css:12-12 |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 6 citation findings for the three stylesheet reference rows using exact CSS literals.

- 2026-07-24T13:17:50Z — Added the development performance-timeline cleanup boundary. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-17T00:25+02:00 — 260715-FEUI-L1 S1: added the third global stylesheet import,
  `./styles/webtui.css` (the one WebTUI mapping file), after `index.css` so its `layer(webtui)`
  rules land in the slot the layer-order statement declares. Verification metadata pinned to the
  task base until closeout stamps the L1 code commit.
- 2026-06-15T17:00 — Created for slice 5d: now imports `index.css` (the Panda/layers entry) ahead of
  `tokens.css`, and wraps the app in `MotionConfig reducedMotion="user"` (the prefers-reduced-motion
  a11y upgrade). Verification metadata pinned until closeout stamps the 5d code commit.
