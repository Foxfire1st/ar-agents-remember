# dashboard/src/test/webtuiSpike.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/webtuiSpike.test.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:42+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `../overview.md`                                 |

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
  `postcss-prefix-selector` carry no range sigils. cit:(["pins @webtui/css, cmdk, and tinykeys exactly (no range sigils)"], dashboard/src/test/webtuiSpike.test.ts:175-181)

### Invariants And Boundaries

- The test MUST keep loading the shared `webtui-scope.config.cjs` — asserting against a copied
  options object would let the build and the test drift apart.
- Node-side suite (fs + postcss, no jsdom rendering); it reads `package.json`, `index.css`,
  `tokens.css`, and the mapping file as text.
- Together with the built-bundle greps recorded in the leaf's review, this suite is the durable
  guard for the S1 adoption contract; weakening any of (a)-(d) needs a design-level ruling, not a
  test edit.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The mapping file whose imports/mapping/focus-restore the assertions parse. | "--background0" | dashboard/src/styles/webtui.css:23-23 |
| The shared scoping options loaded via createRequire. | `module` | dashboard/webtui-scope.config.cjs:32-32 |
| The build config that passes the same options object to the real build. | "./webtui-scope.config.cjs" | dashboard/postcss.config.cjs:6-6 |
| The layer-order statement and unlayered freeze rule asserted. | "animation: none !important" | dashboard/src/index.css:141-141 |
| The declared token vars assertion (b) resolves against. | "--muted" | dashboard/src/styles/tokens.css:13-13 |

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 14 citation claims; scoped result 0 findings.

- 2026-08-02T01:42+02:00 — No content impact: corrected Source Path link depth. The link(s) in this document carried one `../` too many and had never resolved from this card's directory — not code moving out from under a citation, the path as written. Enumerating every depth in both trees leaves exactly one that resolves and it is exactly one level shallower, so there was nothing to judge (`memory_quality/style/citations`, `citation_link_depth_wrong`). No claim, range or target document changed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S1 (R2): the four automated spike
  assertions (scope confinement incl. the :root/html/body collapse; one-color-system token
  mapping; freeze sovereignty via the no-!important-animation walk over the whole dist + the
  unlayered-freeze brace check; exact layer order + focus-visible restore) and the exact-pin
  checks. This suite caught the missing `--muted` token during the spike. Verification metadata
  pinned to the task base until closeout stamps the L1 code commit.
