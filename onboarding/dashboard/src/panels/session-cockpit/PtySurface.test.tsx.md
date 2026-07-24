# dashboard/src/panels/session-cockpit/PtySurface.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/PtySurface.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom PtySurface suite (260715-FEUI-L6 R1/R2/R3/R7/R9): archetype honesty, keep-alive layers,
accessible names, the screen-reader toggle, and the reserved slots — with **xterm kept OUT of
jsdom**: `vi.mock("../Terminal")` replaces the Terminal with a prop-reflecting div (the real
terminal behavior stays Terminal.tsx's own suite).

## Code Commentary

### Logic

- **The Terminal mock** (L15-L35): reflects `readOnly`/`renderer`/`screenReaderMode`/`ariaLabel`
  and the PRESENCE of `hooks`/`keyEventFilter` as data attributes — the surface's wiring is
  asserted without a single xterm/canvas import.
- **Two archetypes (R1)** (L51-L77): controlled panes labeled "runner line-log" +
  `data-has-hooks="false"`; legacy raw labeled "vendor TUI" + `data-has-hooks="true"`;
  `data-pty-archetype` per layer; the measured `PTY_RENDERER` passes through to every pane.
- **Keep-alive** (L79-L105): focus switch keeps the previous layer mounted with `display:none` +
  `aria-hidden="true"` while the new one is visible; landed panes render read-only.
- **Accessibility + reserved slots (R2/R3)** (L107-L145): every pane's `aria-label` carries
  label + harness + state; the screen-reader toggle is `aria-pressed`, names the perf cost,
  flips the pane prop live, and persists to `cockpit.sessions.screen-reader-mode`; the
  scrollback-paused badge slot exists and stays EMPTY (never faked); the reserved-chord key
  filter reaches every pane.
- **Bell acknowledgment (R7)** (L147-L153): focusing a seat clears its pending bell in
  `ptyHarvestStore`.

### Invariants And Boundaries

Fixtures are the shared `L6_CONTROLLED_WORKING`/`L6_LEGACY_RAW` rows; stores + localStorage reset
between cases. Test-only.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | L110-L252 | [PtySurface.tsx](PtySurface.tsx) |
| The L6 archetype fixtures every case hydrates. | L179-L204 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The harvest store the bell case drives. | L51-L75 | [../../data/ptyHarvest.ts](../../data/ptyHarvest.ts) |
| The mocked-away real terminal (its own suite covers xterm wiring). | — | [../Terminal.tsx](../Terminal.tsx) |

## FEUI-L8 Reviewed Candidate Delta

Pins exact terminal-node/scrollback continuity across the transient removed-focus handoff, read-only landed inspection, and exited/retired ended-state presentation with no new socket or PTY zone.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Current L5I Maintenance

The PTY surface tests now cover the removed chrome, floating accessibility control, and visibility
boundary that prevents hidden panes or ended states from participating in stage focus.

## Update History

- 2026-07-24T13:17:17Z — Curator: recorded PTY declutter and hidden-focus regression coverage;
  verification fields remain pre-commit.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R1/R2/R3/R7/R9: the mocked-Terminal
  surface suite — archetype labeling + hooks presence per archetype, renderer pass-through,
  keep-alive hidden layers, read-only landed panes, accessible pane names, the persisted live
  screen-reader toggle, the empty reserved badge slot, the chord filter, and
  bell-acknowledge-on-focus. Verification metadata pinned to the leaf base until closeout stamps
  the L6 code commit.
