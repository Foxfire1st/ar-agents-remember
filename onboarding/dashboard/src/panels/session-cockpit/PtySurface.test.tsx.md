# dashboard/src/panels/session-cockpit/PtySurface.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/PtySurface.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | L110-L252 | [PtySurface.tsx](PtySurface.tsx) |
| The L6 archetype fixtures every case hydrates. | L179-L204 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The harvest store the bell case drives. | L51-L75 | [../../data/ptyHarvest.ts](../../data/ptyHarvest.ts) |
| The mocked-away real terminal (its own suite covers xterm wiring). | — | [../Terminal.tsx](../Terminal.tsx) |

## Update History

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R1/R2/R3/R7/R9: the mocked-Terminal
  surface suite — archetype labeling + hooks presence per archetype, renderer pass-through,
  keep-alive hidden layers, read-only landed panes, accessible pane names, the persisted live
  screen-reader toggle, the empty reserved badge slot, the chord filter, and
  bell-acknowledge-on-focus. Verification metadata pinned to the leaf base until closeout stamps
  the L6 code commit.
