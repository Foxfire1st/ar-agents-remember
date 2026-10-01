# dashboard/src/dev/dev.css

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The co-located stylesheet for the DEV-only `/dev/*` gallery (Bench + Reference). Production-dead (the
dev route is dropped from the production bundle), imported by `DevApp`.

## Code Commentary

### Logic

Plain CSS (the dev gallery is auxiliary tooling, not part of the Panda cockpit): `.cockpit` /
`.cockpit__bar` (the dev shell), `.bench-overlay` (the floating top dock) / `.bench__picker` (the
gallery's floating compact `<select>` state picker; the older `.bench__nav` link-strip rules are
retained but now unused), `.reference` / `__bar` / `__frame` (the mc2 iframe mount). Uses the global
`:root` tokens (`styles/tokens.css`). **Slice 5i** replaced the old `.bench__nav` button wall (which
overlapped the cockpit header) with the compact scenario selector `.bench__picker` /
`.bench__picker-label` / `.bench__select` (+ `optgroup`/`option` toning) and added the bottom-docked
player transport `.player` (fixed, centred) / `.player__caption` / `.player__controls` (with the
`.is-on` loop-toggle state) / `.player__scrub` (amber accent range) / `.player__count`
(tabular-nums). **Slice 5o** stabilised the transport's size: `.player` is now a FIXED `width: 40rem`
(with `box-sizing: border-box`, capped at `max-width: 92vw`) rather than `min-width: 32rem`, and
`.player__caption` is constrained to a single line (`width: 100%`; `white-space: nowrap`;
`overflow: hidden`; `text-overflow: ellipsis`). A long beat caption can no longer widen the
fixed-position centred player, so the controls row beneath it no longer jumps horizontally between
beats or scenarios; over-long titles truncate with an ellipsis instead.

### Invariants And Boundaries

DEV-only; never the production cockpit (which is entirely Panda + React Aria). Kept as plain
co-located CSS deliberately — it is dev tooling, not a shipped component family.

## Evidence

### Repo-Internal References

- Imported by the DEV harness router. [1]
