# dashboard/src/panels/session-cockpit/PtySurface.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/PtySurface.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-04T00:41+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom PtySurface suite (260715-FEUI-L6 R1/R2/R3/R7/R9): archetype honesty, keep-alive layers,
accessible names, the screen-reader toggle, and the removed pane-chrome boundary — with **xterm kept OUT of
jsdom**: `vi.mock("../Terminal")` replaces the Terminal with a prop-reflecting div (the real
terminal behavior stays Terminal.tsx's own suite).

## Code Commentary

### Logic

- **The Terminal mock** cit:(["../Terminal"], dashboard/src/panels/session-cockpit/PtySurface.test.tsx:15-37): reflects `readOnly`/`renderer`/`screenReaderMode`/`ariaLabel`
  and the PRESENCE of `hooks`/`keyEventFilter` as data attributes — the surface's wiring is
  asserted without a single xterm/canvas import.
- **Two archetypes (R1)** cit:(["const controlled = () => fromTerminalSessionInfo(L6_CONTROLLED_WORKING);", "const raw = () => fromTerminalSessionInfo(L6_LEGACY_RAW);"], dashboard/src/panels/session-cockpit/PtySurface.test.tsx:39-40): controlled panes labeled "runner line-log" +
  `data-has-hooks="false"`; legacy raw labeled "vendor TUI" + `data-has-hooks="true"`;
  `data-pty-archetype` per layer; the measured `PTY_RENDERER` passes through to every pane.
- **Keep-alive** cit:(["controlledLayer.style.display"], dashboard/src/panels/session-cockpit/PtySurface.test.tsx:104-104): focus switch keeps the previous layer mounted with `display:none` +
  `aria-hidden="true"` while the new one is visible; landed panes render read-only.
- **Accessibility + removed badge chrome (R2/R3)** cit:(["aria-label={props.ariaLabel}", "pty-scrollback-badge-slot"], dashboard/src/panels/session-cockpit/PtySurface.test.tsx:34-34; dashboard/src/panels/session-cockpit/PtySurface.test.tsx:216-216): every pane's `aria-label` carries
  label + harness + state; the screen-reader toggle is `aria-pressed`, names the perf cost,
  flips the pane prop live, and persists to `cockpit.sessions.screen-reader-mode`; the
  focused absence assertion proves the pane-chrome bar and its former
  `pty-scrollback-badge-slot` are gone, so no reserved slot or badge is faked; the
  reserved-chord key filter reaches every pane.
- **Bell acknowledgment (R7)** cit:([`ptyHarvestStore`], dashboard/src/data/ptyHarvest.ts:51-73): focusing a seat clears its pending bell in
  `ptyHarvestStore`.

### Invariants And Boundaries

Fixtures are the shared `L6_CONTROLLED_WORKING`/`L6_LEGACY_RAW` rows; stores + localStorage reset
between cases. Test-only.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test. | `PtySurface` | dashboard/src/panels/session-cockpit/PtySurface.tsx:136-336 |
| The L6 archetype fixtures every case hydrates. | `L6_CONTROLLED_WORKING`; `L6_LEGACY_RAW` | dashboard/src/test/fixtures/catalogRows.ts:198-210; dashboard/src/test/fixtures/catalogRows.ts:214-221 |
| The harvest store the bell case drives. | `ptyHarvestStore` | dashboard/src/data/ptyHarvest.ts:51-73 |
| The mocked-away real terminal (its own suite covers xterm wiring). | `Terminal` | dashboard/src/panels/Terminal.tsx:110-202 |

## FEUI-L8 Reviewed Candidate Delta

Pins exact terminal-node/scrollback continuity across the transient removed-focus handoff, read-only landed inspection, and exited/retired ended-state presentation with no new socket or PTY zone.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Current L5I Maintenance

The PTY surface tests now cover the removed chrome, floating accessibility control, and visibility
boundary that prevents hidden panes or ended states from participating in stage focus.

## Update History

- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T00:41:58+02:00 — 260731-EFA-L6 S18-SR1 worker: removed the B06 semantic-residual
  scaffold for the retired scrollback badge slot. Live prose now follows the focused absence
  assertion: pane chrome and `pty-scrollback-badge-slot` are gone, so the test promises no
  reserved slot. Preserved the existing generated citation ranges and the prior curator entry; did not
  run citation mechanics. Verification metadata remains pinned until closeout stamps the L6 code
  commit.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the focused PTY citations and marked the obsolete badge-slot statement as a semantic residual; final exact frozen-snapshot check is clean.
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
