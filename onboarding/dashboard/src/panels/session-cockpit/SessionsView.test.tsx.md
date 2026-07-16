# dashboard/src/panels/session-cockpit/SessionsView.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionsView.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The sessions view shell end-to-end jsdom suite (260715-FEUI-L1 S2–S5; 18 cases after review
round 2): scaffold structure + the keyboard/palette foundation wired end-to-end — zones resolved
from real DOM markers, tinykeys at the window, cmdk palette pages, and the F6 focus cycle.

## Code Commentary

### Logic

- **Scaffold structure (S2)** — the scope root (`data-view="sessions"` + `sessions--view`), the
  four `data-region` regions, the `data-kbzone` pty/composer markers, and the floor chip hidden
  while unmeasured (0-width = hidden, never a false alarm).
- **Floor-chip re-measure (review round 2, finding 1)** — both failure paths go through
  `PanelGroup onLayout` with NO view-root resize (under jsdom the mount-time measure sees
  clientWidth 0 and the shared-setup ResizeObserver is inert, so these fail against round-1
  code): F1a pins the stage to 500px post-mount via `defineProperty(clientWidth)`, asserts no
  chip (the old trap), drives a palette-driven inspector collapse → the chip appears; F1b re-pins
  to 900px and clears the stale chip via the reopen-inspector click.
- **Rail calibration (finding 4)** — at a pinned 2560px root, a layout event makes the rail
  panel's `flexGrow` `"12"` (280/2560 → min-clamped); with a persisted
  `react-resizable-panels:cockpit.sessions.panels` key the calibration never fires.
- **Command palette (S3)** — ctrl+k opens from chrome and Escape closes returning focus to the
  invoker (R7); `?` opens the keys page rendering the REAL tables (asserts the ctrl+alt+pagedown
  and ctrl+; rows — bindings and reference can never drift); `?` typed into the composer is
  passthrough (printable suppression); `/` at line start opens the palette; running `rail.toggle`
  surfaces the reopen affordance and closes the palette; `active={false}` (the hidden keep-alive
  layer) never reacts to keys.
- **PTY zone (S4)** — ctrl+; opens the palette from the pty zone; F6 exits to the stage header;
  unreserved keys (Esc, ctrl+k, plain, alt+↑) are never intercepted — asserted via
  **preventDefault observation** (`fireEvent` return value), not palette state alone.
- **Focus model (S4)** — the full F6 cycle across rendered regions (stage lands on the
  composer), Shift+F6 backward, and composer-Esc → stage header.

### Conventions

`setClientWidth` pins `clientWidth` via `defineProperty` (jsdom has no layout). All keyDown inits
carry explicit `code` (tinykeys v4 drops synthetic events without it). `afterEach` clears
localStorage (react-resizable-panels persists under autoSaveId). Relies on the vitest-only
react-resizable-panels browser-build alias (`vitest.config.ts`) — the edge-light node build skips
layout effects and would break the imperative panel API.

### Invariants And Boundaries

The F1a/F1b cases are the round-2 regression net for the floor chip: they must keep driving a
layout change WITHOUT a root resize. Test-only.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | L190-L506 | [SessionsView.tsx](SessionsView.tsx) |
| The keys-page data the drift-proof assertions read. | L62-L150 | [../../data/keymap/reserved.ts](../../data/keymap/reserved.ts) |
| The shared jsdom stubs (incl. the cmdk `scrollIntoView` stub) this suite relies on. | — | [../../test/setup.ts](../../test/setup.ts) |
| The vitest alias to the browser development build of react-resizable-panels. | — | [vitest.config.ts](../../../vitest.config.ts) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S5 (extended in review round 2 with the
  F1a/F1b floor-chip layout-path cases and the two rail-calibration cases): the end-to-end shell
  suite — structure/markers, palette pages + focus return, printable suppression, `/` rule, PTY
  non-interception via preventDefault observation, F6 cycle, and keep-alive `active=false`
  gating. Verification metadata pinned to the task base until closeout stamps the L1 code commit.
