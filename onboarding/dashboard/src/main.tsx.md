# dashboard/src/main.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/main.tsx`                          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[dashboard/src overview](overview.md)

## Purpose

The Vite entry: mounts `<App>` into `#root` (StrictMode) and loads the global stylesheets.

## Code Commentary

### Logic

Imports `./index.css` (the Panda entry + reset/base/effects layers) then `./styles/tokens.css` (the
`:root` design-token vars) — both global. Sets `document.documentElement.dataset.effects = "off"`
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

## Update History

- 2026-06-15T17:00 — Created for slice 5d: now imports `index.css` (the Panda/layers entry) ahead of
  `tokens.css`, and wraps the app in `MotionConfig reducedMotion="user"` (the prefers-reduced-motion
  a11y upgrade). Verification metadata pinned until closeout stamps the 5d code commit.
