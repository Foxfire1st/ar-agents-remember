# dashboard/src/dev/ScenarioPlayer.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/ScenarioPlayer.tsx`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-19T23:58+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../overview.md`                                 |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `applyFrame` snapshots + replays a frame into the real store. | `applyFrame` | dashboard/src/dev/ScenarioPlayer.tsx:12-17 |
| The `Scenario`/`ScenarioFrame` model it walks. | `ScenarioFrame`, `Scenario` | dashboard/src/dev/scenarios.ts:17-22; dashboard/src/dev/scenarios.ts:24-29 |
| The real store it drives (`applySnapshot` / `pushEvent`). | `applySnapshot`, `pushEvent` | dashboard/src/data/store.ts:43-43; dashboard/src/data/store.ts:45-45 |
| Mounted (keyed by scenario) beneath the cockpit by the bench. | `ScenarioPlayer` | dashboard/src/dev/Bench.tsx:39-43 |

## Update History

- 2026-08-03T03:59:59+02:00 — Curated 6 citation claims (3 table rows, 3 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-06-22T16:00 — 05o: the new-`scenario` effect now calls `dashboardStore.getState().reset()` FIRST
  (before applying frame 0) on each scenario mount — since the Bench keys the player by scenario name, the
  reset clears the SHARED store and bumps `gen` per switch, remounting the engine-room canvas clean and
  fixing the dropdown overlay bleed (a prior mode's failure overlay could otherwise linger as an orphaned
  opacity-0 Motion exit node). Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-19T23:58+02:00 — Created for slice 5i: the player transport — `applyFrame` (snapshot + event
  replay into the real store), the cursor/play/loop state machine (seek applies the full frame; play walks
  on a `durMs`/1600ms timer; loop wraps), and the transport UI (reset/prev/play/next/loop/scrub + count).
  Verification metadata pinned until closeout stamps the code commit.
