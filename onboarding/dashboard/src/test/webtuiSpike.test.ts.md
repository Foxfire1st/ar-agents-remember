# dashboard/src/test/webtuiSpike.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **WebTUI×Panda spike's automated assertions** (260715-FEUI-L1 S1, R2/OQ-D; 11 cases) — the
falsifiable adopt-or-fallback criteria, kept as a standing regression suite. They run against the
EXACT build configuration: `webtui-scope.config.cjs` is loaded via `createRequire` — the same
object `postcss.config.cjs` passes to the build, never a copy — and the real
`node_modules/@webtui/css/dist` files are processed through the real plugin. If any assertion
fails, the spike is falsified → the Panda-recipe terminal-skin fallback (the leaf's recorded
alternative).

## Code Commentary

### Logic

The four spike assertions plus the pin check:

- **(a) scope**: every selector in every imported WebTUI file (parsed from the mapping file's
  actual `@import` lines — `importedWebtuiFiles()` ties assertions to reality) is scope-prefixed
  after running through the exact prefixer options; keyframe steps are exempt; the library's
  global anchors (`:root|html|body`) are collapsed onto the scope root itself and no global anchor
  survives. cit:(["prefixes every selector in every imported WebTUI file under the scope"], dashboard/src/test/webtuiSpike.test.ts:68-81) cit:(["collapses the library's global selectors (:root/html/body) onto the scope root itself"], dashboard/src/test/webtuiSpike.test.ts:83-95)
- **(b) tokens**: the mapping block maps every WebTUI palette/base variable, references only token
  vars DECLARED in `styles/tokens.css`, and contains no raw `oklch(`/hex/`rgb(` literal — no second
  color system. cit:(["maps every WebTUI palette/base variable in the one mapping file"], dashboard/src/test/webtuiSpike.test.ts:101-115) cit:(["references only existing token vars — no raw color literals (no second color system)"], dashboard/src/test/webtuiSpike.test.ts:117-128)
- **(c) freeze**: walks ALL of `@webtui/css/dist` (not just imported files) asserting zero
  `!important` animation/transition declarations — the cascade reason: for `!important`, LAYERED
  declarations beat unlayered ones (CSS Cascade 5 reverses layer order for important), so the
  unlayered freeze stays sovereign only while this holds — and the freeze rule itself is intact
  and top-level in `index.css` (a brace-balance check proves it sits outside every layer block).
  cit:(["WebTUI ships no !important animation/transition declaration (layered !important would beat the unlayered freeze)"], dashboard/src/test/webtuiSpike.test.ts:132-142) cit:(["the freeze rule itself is intact and UNLAYERED in index.css"], dashboard/src/test/webtuiSpike.test.ts:144-153)
- **(d) layer order + focus**: `index.css`'s FIRST `@layer` statement is exactly `reset, base,
  effects, webtui, tokens, recipes, utilities`; WebTUI's `outline: none` reset really exists AND
  the mapping file's scoped `:focus-visible` amber restore is present. cit:(["slots webtui between effects and tokens in the FIRST @layer statement"], dashboard/src/test/webtuiSpike.test.ts:157-162) cit:(["WebTUI's outline reset exists but the mapping file restores :focus-visible inside the scope"], dashboard/src/test/webtuiSpike.test.ts:164-171)
- **Exact pins**: `@webtui/css` is literally `0.1.9`; `cmdk`/`tinykeys` and the dev
  `postcss-prefix-selector` carry no range sigils. cit:(["pins @webtui/css"], dashboard/src/test/webtuiSpike.test.ts:175-181)

### Invariants And Boundaries

- The test MUST keep loading the shared `webtui-scope.config.cjs` — asserting against a copied
  options object would let the build and the test drift apart.
- Node-side suite (fs + postcss, no jsdom rendering); it reads `package.json`, `index.css`,
  `tokens.css`, and the mapping file as text.
- Together with the built-bundle greps recorded in the leaf's review, this suite is the durable
  guard for the S1 adoption contract; weakening any of (a)-(d) needs a design-level ruling, not a
  test edit.

## Evidence

### Repo-Internal References

- The mapping file whose imports/mapping/focus-restore the assertions parse. [1]
- The shared scoping options loaded via createRequire. [2]
- The build config that passes the same options object to the real build. [3]
- The layer-order statement and unlayered freeze rule asserted. [4]
- The declared token vars assertion (b) resolves against. [5]
