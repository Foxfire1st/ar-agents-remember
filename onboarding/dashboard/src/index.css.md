# dashboard/src/index.css

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/index.css`                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-21T05:30+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                    |

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
flicker). Three app-wide keyframes now live here: `flicker` (the CRT overlay), the shared `pulse` (the ≤3/s alarm
flash used by blocked/alarm dots, signal-lost, `caution--alarm`, and the cockpit rail / topology), and —
260715-FEUI-L2 — **`pulseSlow`** (the cockpit STATE pulse, developer ruling 2026-07-16): a SLOW
ease-in-out opacity dip to 0.45 at 50%, driven at 2.4 s by `data/stateGrammar.ts`'s
`PULSE_ANIMATION` and rendered only by `panels/session-cockpit/StateDot.tsx` — NEVER
steps()/on-off blinking; frozen by the unlayered effects-off rule below and steady under
`_motionReduce` at the consumer. **Slice
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
not CSS keyframes (`05f` §8): `flicker` + `pulse` + (260715-FEUI-L2) `pulseSlow` are the global
keyframes — `pulse` is still live (the rail / cockpit / topology + the engine-room `cva`s drive
`animation: pulse …`), and `pulseSlow` is the RULED cockpit state pulse whose only sanctioned
driver is the grammar/StateDot pair (2.4 s ease-in-out, never steps()). *(Correcting the prior 5i note: `chargeSweep` was never an orphan — through 5i it backed
`engineReindexCharge`, the amber reindex pulse, so only `conduitDraw` was truly orphaned after the conduit
draw-on moved to GSAP. 05k makes the point moot by deleting all nine canvas keyframes and re-driving the
reindex pulse from GSAP `data-fx='reindex'`.)*

### 2026-07-24 Curator Delta

The CRT effects overlay no longer uses full-screen `mix-blend-mode:multiply`. Its unchanged translucent
scanline and vignette treatment can remain a static compositor layer rather than forcing a whole-screen
re-raster for scroll, video, or animation invalidations.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `:root` vars referenced by the base layer. | ":root" | dashboard/src/styles/tokens.css:5-5 |
| The Panda PostCSS plugin that fills the layers. | "@pandacss/dev/postcss" | dashboard/postcss.config.cjs:10-10 |
| The one WebTUI mapping file whose `layer(webtui)` imports fill the new slot. | "base.css" | dashboard/src/styles/webtui.css:12-12 |
| Asserts the exact layer-order statement and the unlayered freeze. | "S1 spike (d): layer order + focus-visible survival (React Aria intact)" | dashboard/src/test/webtuiSpike.test.ts:156-172 |
| The scoped WebTUI base whose `word-break: break-all` the RV-1 root override neutralizes. | "word-break: break-all" | dashboard/src/index.css:117-127 |
| Consumers whose overflow-wrap fixes only hold under the RV-1 override (Inspector values, prose, rail footer). | "export function InspectorFact"; "export const MarkdownBlock"; "export function SessionRail" | dashboard/src/panels/session-cockpit/InspectorPrimitives.tsx:98-98; dashboard/src/panels/session-cockpit/SessionRail.tsx:160-160; dashboard/src/panels/session-cockpit/conversation/MarkdownBlock.tsx:88-88 |

## Update History

- 2026-08-05T13:06:07+02:00 — 260731-EFA-L6 residual curator: repointed the WebTUI-base row from the untracked dashboard/node_modules/@webtui/css/dist/base.css:1-1 to the tracked RV-1 comment block dashboard/src/index.css:117-127, which states the @webtui/css `word-break: break-all` base rule and the root override that neutralizes it; anchor corrected to the exact tracked literal "word-break: break-all".

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 6 repository-reference citations (6/6 anchored and sourced; scoped citation check clean).

- 2026-07-24T13:17:50Z — Documented the compositor-safe CRT overlay change. Verification hash/date
  remain pinned to the pre-commit source stamp.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the RV-1 root override (LOAD-BEARING) —
  an unlayered `html, body, [data-view="sessions"] { word-break: normal; overflow-wrap: break-word }`
  that neutralizes `@webtui/css`'s inherited `word-break: break-all` app-wide. Captured the durable
  lesson: a third-party scoped reset in a lower layer silently defeats local overflow-wrap patches; the
  test is computed-value verification (the `[data-view="sessions"]` inclusion is required because postcss
  rewrites webtui's `body,html` rule onto the scope root; raw-id spans keep explicit `break-all`).
  Verification pinned to the leaf base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 (R14): added the `pulseSlow` keyframe — the cockpit
  seat-state pulse (2.4 s ease-in-out opacity, ruled 2026-07-16, never steps()) consumed by the
  grammar's single renderer `StateDot`; the header comment names the ruling and the
  effects-off/motion-reduce freeze paths. Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.
- 2026-07-17T00:25+02:00 — 260715-FEUI-L1 S1 (WebTUI adoption, OQ-D): the FIRST `@layer` statement
  gained the `webtui` slot between `effects` and `tokens` (`reset, base, effects, webtui, tokens,
  recipes, utilities`), hosting the scoped WebTUI skin from `styles/webtui.css` so Panda layers
  always win a conflict and the unlayered freeze stays sovereign; the header comment documents the
  slot. The production minifier drops the order statement but emits layer blocks in declaration
  order — semantics preserved because all layered CSS lives in the one bundle. Verification
  metadata pinned to the task base until closeout stamps the L1 code commit.
- 2026-06-21T23:35 — removed the `@keyframes powerup` rule and updated the canvas-motion doctrine header
  comment: the indexing→nominal engine "powerup" is now a Motion opacity pulse owned by the charge rect, and
  the cyan→mint step is an instant `engineCharge`-class fill flip — so no `powerup` CSS keyframe remains and
  the canvas carries no animation carve-out. Only `flicker` + `pulse` survive as global keyframes.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-21T02:27+02:00 — slice 05k: deleted the nine Engine Room canvas `@keyframes` (`chargeSweep`,
  `conduitDraw`, `pktRun`, `attnBreath`, `stopFlash`, `closeoutSweep`, `warpSurgeUp`/`warpSurgeDown`,
  `landingIn`) — the canvas motion is now GSAP (`useEngineTimeline`) + Motion (`EnclosureCanvas`), never CSS
  (`05f` §8). Kept the app-wide `flicker` + `pulse` keyframes (`pulse` is still driven by the rail / cockpit /
  topology + the engine-room `cva`s) and the `data-effects=off` freeze (incl. the `conduit-packet` /
  `warp-surge` display-freeze rules). **Corrected the 5i note**: `chargeSweep` was NOT orphaned — through 5i
  it backed `engineReindexCharge` (the reindex pulse); only `conduitDraw` was truly orphaned. Verification
  metadata pinned until closeout stamps the 05k code commit.
- 2026-06-18T13:01+02:00 — slice 5h coupler fix: added the `warpSurgeUp`/`warpSurgeDown` keyframes (the warp-core surge on the ledger coupler — two hot bands born at the link, splitting up/down; hidden under effects=off, no settled state) + the `warp-surge` freeze rule. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T11:55+02:00 — slice 5h H2: added the `closeoutSweep` keyframe (the T13 closeout-train left-to-right derived fill on closeout-pending; per-beat delay set inline, frozen by effects=off to the all-done strip). Verification metadata pinned until closeout stamps the 5h H2 code commit.
- 2026-06-17T16:15 — slice 5g G5: added the `stopFlash` keyframe (the t14c terminal integration-conflict
  STOP — a brief flash ×3 then steady, frozen by the `effects=off` rule). Verification metadata pinned
  until closeout stamps the G5 code commit.
- 2026-06-17T14:00 — slice 5g G3: added the `attnBreath` keyframe (the gentle alarm-parity breathing for the
  failure-overlay attention badge — distinct from the sharp `pulse` fault flicker). Verification metadata
  pinned until closeout stamps the G3 code commit.
- 2026-06-17T12:47 — slice 5g G2: added the Engine Room pod-stage motion keyframes — `chargeSweep`
  (center-out engine charge), `conduitDraw` (conduit draw-on), `pktRun` (travelling flow packet) — plus a
  freeze rule hiding `conduit-packet` under effects=off. Verification metadata pinned until closeout stamps
  the G2 code commit.
- 2026-06-15T17:00 — Created for slice 5d: the Panda entry + reset/base/effects layers (reset, base,
  CRT overlay, keyframes) extracted from the monolith. Verification metadata pinned until closeout
  stamps the 5d code commit.
