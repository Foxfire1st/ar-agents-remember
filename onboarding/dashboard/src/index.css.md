# dashboard/src/index.css

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/index.css`                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-21T23:35                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[dashboard/src overview](overview.md)

## Purpose

The Panda **entry** + the global non-component layers (the layered blueprint). Declares the cascade
layer order and holds `reset` / `base` / `effects` — the layers Panda does not own.

## Code Commentary

### Logic

`@layer reset, base, effects, tokens, recipes, utilities;` sets the order; Panda's PostCSS plugin
injects the generated `tokens`/`recipes`/`utilities` layers. `@layer reset` (box-sizing + html/body
reset), `@layer base` (body typography + the `h2`/`.muted`/`.raw-list` utilities moved here from the
monolith), `@layer effects` (the global `.crt-overlay` — scanlines + the re-centred vignette +
flicker). Two app-wide keyframes remain: `flicker` (the CRT overlay) and the shared `pulse` (the ≤3/s alarm
flash used by blocked/alarm dots, signal-lost, `caution--alarm`, and the cockpit rail / topology). **Slice
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

### Conventions

Cascade layers, not specificity, order the cascade; effect/determinism rules sit unlayered + `!important` so
they win regardless. Token values are read as `var(--…)` from `styles/tokens.css` during the migration.

### Invariants And Boundaries

Effects stay global + isolated (note 09), never per-component. The body/utility rules reference the
`:root` vars from `styles/tokens.css`. Component styling is Panda, not here. Canvas animation is GSAP/Motion,
not CSS keyframes (`05f` §8): only `flicker` + `pulse` remain as global keyframes, and `pulse` is still
live (the rail / cockpit / topology + the engine-room `cva`s drive `animation: pulse …`), so it is NOT
orphaned. *(Correcting the prior 5i note: `chargeSweep` was never an orphan — through 5i it backed
`engineReindexCharge`, the amber reindex pulse, so only `conduitDraw` was truly orphaned after the conduit
draw-on moved to GSAP. 05k makes the point moot by deleting all nine canvas keyframes and re-driving the
reindex pulse from GSAP `data-fx='reindex'`.)*

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `:root` vars referenced by the base layer. | — | [styles/tokens.css](styles/tokens.css) |
| The Panda PostCSS plugin that fills the layers. | — | [postcss.config.cjs](agents-remember/dashboard/postcss.config.cjs) |

## Update History

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
