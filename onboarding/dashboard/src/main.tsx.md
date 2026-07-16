# dashboard/src/main.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/main.tsx`                          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:25+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Panda entry + layer order it loads. | L1-L6 | [index.css](index.css) |
| The `:root` design tokens it loads. | — | [styles/tokens.css](styles/tokens.css) |
| The scoped WebTUI skin it loads third (260715-FEUI-L1). | L12-L15 | [styles/webtui.css](styles/webtui.css) |

## Update History

- 2026-07-17T00:25+02:00 — 260715-FEUI-L1 S1: added the third global stylesheet import,
  `./styles/webtui.css` (the one WebTUI mapping file), after `index.css` so its `layer(webtui)`
  rules land in the slot the layer-order statement declares. Verification metadata pinned to the
  task base until closeout stamps the L1 code commit.
- 2026-06-15T17:00 — Created for slice 5d: now imports `index.css` (the Panda/layers entry) ahead of
  `tokens.css`, and wraps the app in `MotionConfig reducedMotion="user"` (the prefers-reduced-motion
  a11y upgrade). Verification metadata pinned until closeout stamps the 5d code commit.
