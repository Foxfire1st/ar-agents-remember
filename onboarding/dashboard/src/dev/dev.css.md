# dashboard/src/dev/dev.css

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/dev.css`                      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-19T23:58+02:00                          |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Imported by the DEV harness router. | — | [DevApp.tsx](DevApp.tsx) |

## Update History

- 2026-06-22T16:00 — slice 5o: pinned the player transport's size — `.player` switched from `min-width: 32rem`
  to a FIXED `width: 40rem` (`box-sizing: border-box`, `max-width: 92vw`) and `.player__caption` became a
  single-line ellipsis (`white-space: nowrap`/`overflow: hidden`/`text-overflow: ellipsis`/`width: 100%`), so a
  long beat caption no longer widens the centred player or jolts the controls row between beats/scenarios.
  Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-19T23:58+02:00 — slice 5i: swapped the `.bench__nav` button wall for the compact
  `.bench__picker`/`.bench__select` scenario selector and added the bottom-docked `.player*` transport
  styles (caption, controls + `.is-on`, scrub, count). Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-18T21:27 — Dev-bench review-ergonomics: added `.bench__picker` (+ its `select`) for the compact state picker that replaced the `bench__nav` link strip; left the `.bench__nav` rules in place (task 5 still uses them; slice 5i supersedes). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-15T17:00 — Created for slice 5d: the dev-gallery styles extracted from the retired monolith
  into this co-located sheet. Verification metadata pinned until closeout stamps the 5d code commit.
