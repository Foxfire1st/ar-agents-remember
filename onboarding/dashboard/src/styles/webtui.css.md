# dashboard/src/styles/webtui.css

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/styles/webtui.css`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:42+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

- Four `@import … layer(webtui)` lines cit:(["layer(webtui)"], dashboard/src/styles/webtui.css:12-15): `base.css`, `utils/box.css`,
  `components/badge.css`, `components/separator.css`. Each file's own `@layer
  base/utils/components` blocks nest INSIDE our `webtui` layer, which `index.css` slots between
  `effects` and `tokens` — so Panda tokens/recipes/utilities beat WebTUI on any conflict, and the
  unlayered `!important` effects freeze always wins (WebTUI ships no `!important`
  animation/transition declarations; the spike test asserts that stays true).
- **Relative node_modules paths are deliberate** cit:(["postcss-import"], dashboard/src/styles/webtui.css:10-10): Vite 8's bundled postcss-import does
  not resolve bare package specifiers inside CSS `@import`, and a JS-side import could not carry
  `layer(webtui)`.
- The `@layer webtui` block cit:(["[data-view=\"sessions\"]"], dashboard/src/styles/webtui.css:22-34) maps
  `--background0/1/2/3`, `--foreground0/1/2`, `--box-border-color`, `--font-family` (+
  `--font-size`, `--line-height`) onto `var(--bg)/var(--bg-panel)/var(--grid)/var(--ink)/
  var(--muted)/var(--font-mono)` — `color-mix(in oklch, …)` only ever blends token vars; the
  session-surface spec §2.1 roles table is this mapping's semantic contract. These direct-in-layer
  rules outrank the imports' nested `webtui.base` defaults.
- The scoped `:focus-visible` restore cit:([":focus-visible"], dashboard/src/styles/webtui.css:39-39): WebTUI's base resets `* { outline: none }`
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The layer-order statement that slots `webtui` between effects and tokens. | "@layer reset, base, effects, webtui, tokens, recipes, utilities;" | dashboard/src/index.css:9-9 |
| The token vars the mapping references (incl. the L1-added `--muted`). | "--muted" | dashboard/src/styles/tokens.css:13-13 |
| The shared scoping options (prefix, includeFiles, the :root/html/body collapse transform). | `webtuiPrefixOptions` | dashboard/webtui-scope.config.cjs:26-30 |
| The build wiring: Panda first, then the prefixer over the inlined imports. | "Panda first", "postcss-import", "postcss-prefix-selector': webtuiPrefixOptions" | dashboard/postcss.config.cjs:1-4; dashboard/postcss.config.cjs:8-11 |
| The four automated spike assertions + exact-pin checks that keep this contract honest. | "S1 spike (a): every WebTUI rule is confined to the cockpit root", "S1 spike (b): one color system — WebTUI vars map onto podracer tokens", "S1 spike (c): the html[data-effects=off] determinism freeze still wins", "S1 spike (d): layer order + focus-visible survival (React Aria intact)", "S1 spike: exact version pins (0.x churn ruling)" | dashboard/src/test/webtuiSpike.test.ts:61-96; dashboard/src/test/webtuiSpike.test.ts:98-129; dashboard/src/test/webtuiSpike.test.ts:131-154; dashboard/src/test/webtuiSpike.test.ts:156-172; dashboard/src/test/webtuiSpike.test.ts:174-182 |
| The scope-root carrier. | "sessions" | dashboard/src/panels/session-cockpit/SessionsView.tsx:1030-1035 |

## Update History

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 14 citations (citation_anchor_missing=5, citation_prose_not_in_cit_form=4, citation_source_malformed=5); amended max-reviewer subject binding for layer and plugin ordering; final scoped citation check clean.
- 2026-08-02T01:42+02:00 — No content impact: corrected Source Path link depth. The link(s) in this document carried one `../` too many and had never resolved from this card's directory — not code moving out from under a citation, the path as written. Enumerating every depth in both trees leaves exactly one that resolves and it is exactly one level shallower, so there was nothing to judge (`memory_quality/style/citations`, `citation_link_depth_wrong`). No claim, range or target document changed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S1 (R2, OQ-D = adopt): the one WebTUI
  mapping file — four dist imports into `layer(webtui)` via relative node_modules paths (Vite 8
  postcss-import limitation), the `[data-view="sessions"]` token mapping (color-mix over token
  vars only), and the scoped `:focus-visible` restore. The `@scope` fallback was ruled viable but
  not needed (the build-time prefixer is runtime-free, layer-composable, and statically
  testable). Verification metadata pinned to the task base until closeout stamps the L1 code
  commit.
