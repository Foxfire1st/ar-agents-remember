# dashboard/src/index.css

## Governing Overview

[dashboard/src overview](overview.md)

## Purpose

The Panda **entry** + the global non-component layers (the layered blueprint). Declares the cascade
layer order and holds `reset` / `base` / `effects` — the layers Panda does not own.

## Code Commentary

### Logic

`@layer reset, base, effects, webtui, tokens, recipes, utilities;` sets the order (260715-FEUI-L1
S1 added the `webtui` slot); Panda's PostCSS plugin injects the generated
`tokens`/`recipes`/`utilities` layers, and `styles/webtui.css`'s `layer(webtui)` imports fill
`webtui` — slotted between `effects` and `tokens` so Panda tokens/recipes/utilities always beat
WebTUI on a conflict, while the unlayered freeze below stays above it all. `@layer reset` (box-sizing + html/body
reset), `@layer base` (body typography + the `h2`/`.muted`/`.raw-list` utilities moved here from the
monolith), `@layer effects` (the global `.crt-overlay` — scanlines + the re-centred vignette +
flicker). Four app-wide keyframes now live here: `flicker` (the CRT overlay), the shared `pulse` (the ≤3/s alarm
flash used by blocked/alarm dots, signal-lost, `caution--alarm`, and the cockpit rail / topology), and —
260715-FEUI-L2 — **`pulseSlow`** (the cockpit STATE pulse, developer ruling 2026-07-16): a SLOW
ease-in-out opacity dip to 0.45 at 50%, driven at 2.4 s by `data/stateGrammar.ts`'s
`PULSE_ANIMATION` and rendered only by `panels/session-cockpit/StateDot.tsx` — NEVER
steps()/on-off blinking; frozen by the unlayered effects-off rule below and steady under
`_motionReduce` at the consumer. The fourth, paseoAgentSpin, supplies the native sidebar
Busy/Starting glyph's full rotation; PaseoNavigation selects a 2.4-second cycle and reduced-motion
suppression, and the existing effects-off rule freezes it. **Slice
05k deleted the nine Engine Room canvas `@keyframes`** — `chargeSweep`, `conduitDraw`, `pktRun`, `attnBreath`,
`stopFlash`, `closeoutSweep`, `warpSurgeUp`, `warpSurgeDown`, and `landingIn` — because the canvas motion now
lives in GSAP (`useEngineTimeline`) + Motion (`EnclosureCanvas`), never CSS (`05f` §8). A header comment
records that removal and (2026-06-21) was extended to also drop the `powerup` keyframe: the
indexing→nominal engine "powerup" is now a **Motion opacity pulse** owned by the charge rect, and the
cyan→mint step is an instant `engineCharge`-class fill flip (not an animation), so there is no `powerup`
CSS keyframe left and the canvas carries **no animation carve-out** at all. The `html[data-effects="off"] *` determinism rule (unlayered + `!important` so it
always wins) freezes every animation + transition; the two companion display-freeze rules survive because
their targets have no settled end-state — `[data-testid="conduit-packet"]` (the travelling packet) and
`[data-testid="warp-surge"]` (the warp-core bands) are hidden under the freeze.

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
The RV-1 `word-break` override is deliberately UNLAYERED (like the effects freeze) so it beats webtui's
layered base without needing `!important`.

### Invariants And Boundaries

Effects stay global + isolated (note 09), never per-component. The body/utility rules reference the
`:root` vars from `styles/tokens.css`. Component styling is Panda, not here — the RV-1 `word-break`
override is the deliberate exception (an app-wide reset that MUST live above the webtui layer at the root;
a component-level fix cannot neutralize an inherited `break-all`).
The `webtui` slot must stay in the FIRST `@layer` statement, between `effects` and `tokens`, and
the `data-effects=off` freeze must stay UNLAYERED and top-level — both are asserted by
`test/webtuiSpike.test.ts` (for `!important` declarations, layered beats unlayered, so the freeze
stays sovereign only while WebTUI ships no `!important` animation/transition — also asserted). Canvas animation is GSAP/Motion,
not CSS keyframes (`05f` §8): `flicker` + `pulse` + (260715-FEUI-L2) `pulseSlow` +
`paseoAgentSpin` are the global keyframes — `pulse` is still live (the rail / cockpit / topology + the engine-room `cva`s drive
`animation: pulse …`), and `pulseSlow` is the RULED cockpit state pulse whose only sanctioned
driver is the grammar/StateDot pair (2.4 s ease-in-out, never steps()). The native busy glyph
uses paseoAgentSpin as presentation only; the glyph's activity is derived by its native-row consumer. *(Correcting the prior 5i note: `chargeSweep` was never an orphan — through 5i it backed
`engineReindexCharge`, the amber reindex pulse, so only `conduitDraw` was truly orphaned after the conduit
draw-on moved to GSAP. 05k makes the point moot by deleting all nine canvas keyframes and re-driving the
reindex pulse from GSAP `data-fx='reindex'`.)*

### 2026-07-24 Curator Delta

The CRT effects overlay no longer uses full-screen `mix-blend-mode:multiply`. Its unchanged translucent
scanline and vignette treatment can remain a static compositor layer rather than forcing a whole-screen
re-raster for scroll, video, or animation invalidations.

## Evidence

### Repo-Internal References

The current source extents below record the reviewed UI contract. Inline test names/facets are source-bound evidence; the installed writer cannot create typed proves from those call titles, and these citations do not claim such a proof or a rerun.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `paseoAgentSpin` | `dashboard/src/index.css:103-107` |
| Current source owner or exact assertion described above. | `html[data-effects="off"]` | `dashboard/src/index.css:144-149` |

- The `:root` vars referenced by the base layer. [1]
- The Panda PostCSS plugin that fills the layers. [2]
- The one WebTUI mapping file whose `layer(webtui)` imports fill the new slot. [3]
- Asserts the exact layer-order statement and the unlayered freeze. [4]
- The scoped WebTUI base whose `word-break: break-all` the RV-1 root override neutralizes. [5]
- Consumers whose overflow-wrap fixes only hold under the RV-1 override (Inspector values, prose, rail footer). [6]
