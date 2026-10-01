# dashboard/src/dev/ScenarioPlayer.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Slice 5i — the scenario-player transport (ported from `public/_proto/podstage.html`'s player). It owns
the cursor / play timer / loop and, on every seek, applies the current FULL frame to the real store so
the real cockpit animates the diff. There is no incremental SVG mutation: a seek = apply frame `t`
(animating from wherever the cockpit is), play = walk on a timer, loop = wrap.

## Code Commentary

### Logic

`applyFrame(frame)` is the driver: `store.applySnapshot(frame.projection)`, then resets the event tail
(`events: []`) and replays the frame's own `events` (if any) so the river reflects the frame rather than
accumulating across the whole timeline. `ScenarioPlayer({ scenario })` holds three pieces of React state
— `cur` (cursor), `playing`, `loop`. Effects: (1) a new `scenario` calls `dashboardStore.getState().reset()`
FIRST, then resets to frame 0 + stops; (2) a seek effect applies `frames[cur]` whenever `frames`/`cur`
change; (3) a play effect schedules a `setTimeout` (frame `durMs` ?? `DEFAULT_FRAME_MS` = 1600) that
advances the cursor, wrapping to 0 when `loop` else stopping at the end. `seek(next)` stops playback and
clamps the cursor into range. The render
is a fixed-position transport bar: a caption line + controls (reset ⏮ / prev ◀ / play-pause ▶⏸ /
next ▶▌ / loop ⟳ with `aria-pressed`) + a range `scrub` slider + an `n/total` count. The bench mounts it
with `key={scenario.name}` so switching scenarios remounts it fresh.

Because the Bench keys the player by `scenario.name`, switching scenarios in the dropdown remounts the
component, so the new-`scenario` effect runs exactly once per scenario. As of 05o that effect calls
`dashboardStore.getState().reset()` BEFORE applying frame 0, clearing the SHARED store and bumping its
`gen`. The `gen` bump forces the engine-room canvas to remount fresh on each scenario switch, which fixes
the dropdown overlay bleed: without the reset, a failure overlay from the prior mode could linger as an
orphaned opacity-0 Motion exit node that bled through into the next scenario.

### Invariants And Boundaries

DEV-only (never in the production bundle). The player drives the REAL `dashboardStore`, not a private
copy — that is the whole point (the integrated motion is what's being verified). `data-testid` hooks
(`scenario-player`, `player-caption`, `player-reset`, `player-play`) are stable for Playwright/dev use.
Timers are cleaned up on every effect re-run (no leak across seeks). It owns transport only; the frame
content (projections/captions/durations) lives in `scenarios.ts`.

## Evidence

### Repo-Internal References

- `applyFrame` snapshots + replays a frame into the real store. [1]
- The `Scenario`/`ScenarioFrame` model it walks. [2]
- The real store it drives (`applySnapshot` / `pushEvent`). [3]
- Mounted (keyed by scenario) beneath the cockpit by the bench. [4]
