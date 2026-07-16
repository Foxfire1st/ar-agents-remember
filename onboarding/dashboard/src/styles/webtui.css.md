# dashboard/src/styles/webtui.css

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/styles/webtui.css`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **WebTUI skin for the sessions cockpit — THE one mapping file** (260715-FEUI-L1 S1; the spike
PASSED and OQ-D resolved to **adopt** WebTUI). `@webtui/css` is pinned EXACTLY at 0.1.9 (0.x churn
ruling). This file is the only place WebTUI enters the app: it imports the used dist files into
the `webtui` cascade layer and maps WebTUI's palette variables onto the existing podracer OKLCH
tokens — ONE color system, no second palette.

## Code Commentary

### Logic

- Four `@import … layer(webtui)` lines (L12-L15): `base.css`, `utils/box.css`,
  `components/badge.css`, `components/separator.css`. Each file's own `@layer
  base/utils/components` blocks nest INSIDE our `webtui` layer, which `index.css` slots between
  `effects` and `tokens` — so Panda tokens/recipes/utilities beat WebTUI on any conflict, and the
  unlayered `!important` effects freeze always wins (WebTUI ships no `!important`
  animation/transition declarations; the spike test asserts that stays true).
- **Relative node_modules paths are deliberate** (L10-L11): Vite 8's bundled postcss-import does
  not resolve bare package specifiers inside CSS `@import`, and a JS-side import could not carry
  `layer(webtui)`.
- The `@layer webtui` block (L17-L43): `[data-view="sessions"]` maps
  `--background0/1/2/3`, `--foreground0/1/2`, `--box-border-color`, `--font-family` (+
  `--font-size`, `--line-height`) onto `var(--bg)/var(--bg-panel)/var(--grid)/var(--ink)/
  var(--muted)/var(--font-mono)` — `color-mix(in oklch, …)` only ever blends token vars; the
  session-surface spec §2.1 roles table is this mapping's semantic contract. These direct-in-layer
  rules outrank the imports' nested `webtui.base` defaults.
- The scoped `:focus-visible` restore (L39-L42): WebTUI's base resets `* { outline: none }`
  inside the scope; this rule restores a visible amber ring for anything a higher layer does not
  style — Panda's `_focusVisible` rules (utilities layer) still win, so React Aria focus styling
  is untouched (spike assertion d).

### Conventions

Scoping is BUILD-TIME: `postcss-prefix-selector` (options in `webtui-scope.config.cjs`, wired in
`postcss.config.cjs`) prefixes every imported rule under `[data-view="sessions"]` and collapses
`:root|html|body` onto the scope root. The blocks authored here are already scoped, so the
transform leaves them alone.

### Invariants And Boundaries

- **One mapping file** — additional WebTUI components are imported HERE (with `layer(webtui)`),
  never elsewhere.
- No raw color literals (`oklch(`/hex/`rgb(`) — every color references a declared token var
  (spike assertion b caught the missing `--muted`, added to `tokens.css`).
- The `webtui` layer must stay between `effects` and `tokens` in `index.css`'s FIRST `@layer`
  statement, and the three runtime deps (+ the prefixer) stay exact-pinned — both enforced by
  `test/webtuiSpike.test.ts`.
- The scope root lives on `SessionsView`'s root div; no WebTUI rule may match outside it.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The layer-order statement that slots `webtui` between effects and tokens. | L6 | [../index.css](../index.css) |
| The token vars the mapping references (incl. the L1-added `--muted`). | — | [tokens.css](tokens.css) |
| The shared scoping options (prefix, includeFiles, the :root/html/body collapse transform). | — | [webtui-scope.config.cjs](../../../webtui-scope.config.cjs) |
| The build wiring: Panda first, then the prefixer over the inlined imports. | — | [postcss.config.cjs](../../../postcss.config.cjs) |
| The four automated spike assertions + exact-pin checks that keep this contract honest. | L61-L182 | [../test/webtuiSpike.test.ts](../test/webtuiSpike.test.ts) |
| The scope-root carrier. | L358-L363 | [../panels/session-cockpit/SessionsView.tsx](../panels/session-cockpit/SessionsView.tsx) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S1 (R2, OQ-D = adopt): the one WebTUI
  mapping file — four dist imports into `layer(webtui)` via relative node_modules paths (Vite 8
  postcss-import limitation), the `[data-view="sessions"]` token mapping (color-mix over token
  vars only), and the scoped `:focus-visible` restore. The `@scope` fallback was ruled viable but
  not needed (the build-time prefixer is runtime-free, layer-composable, and statically
  testable). Verification metadata pinned to the task base until closeout stamps the L1 code
  commit.
