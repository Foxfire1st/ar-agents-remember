# dashboard/src/panels/session-cockpit/SessionsView.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionsView.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The sessions view end-to-end jsdom suite (260715-FEUI-L1 S2–S5, 18 cases after review round 2;
+3 integration cases from 260715-FEUI-L2; +7 from 260715-FEUI-L6 incl. the fix round; +2
launch-integration cases from 260715-FEUI-L3): scaffold structure + the keyboard/palette
foundation wired end-to-end — zones resolved from real DOM markers, tinykeys at the window, cmdk
palette pages, and the F6 focus cycle — now running against the REAL rail/stage (all 21 L1 cases
pass unchanged against the L2-filled panels; the pty-zone cases still exercise the placeholder,
which hydrating no sessions keeps on screen). The L2 cases: R9 view-entry focus lands on the
awaiting-input seat first, F17 focus handoff when the focused seat retires/lands (reason-bearing
stage note + smart refocus), and alt+↑/↓ rail-order session cycling. The L6 block covers the
stage fill: the real `PtySurface` (xterm mocked out of jsdom via `vi.mock("../Terminal")`), the
WorkingLine slot, the InteractionBar axis, stop residuals (incl. the unfocused-seat sweep), and
the grammar-gated Stop-turn palette command. The L3 cases wire the launch flow and failed-launch
banner through the real view.

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
- **L6 stage surface + lifecycle honesty (L308-L422)** — seven cases against the real store
  patch path: (1) a focused seat mounts the REAL `PtySurface` and the placeholder covers only
  the empty stage (the surface carries the `data-kbzone="pty"` contract); (2) the WorkingLine
  renders in the reserved stage slot ONLY for a working focused seat; (3) the InteractionBar
  renders on the interaction axis ABOVE the composer, never replacing it (DOM-position
  assertion); (4) a retired seat's stop residual renders as an INFORMATIONAL `role="status"`
  line — asserts the word "fail" never appears; (5) the UA-7-gated Stop-turn palette command is
  offered with the gap named in its title; (6) Stop-turn gates on the WorkingLine's OWN grammar
  state (review F3): patching a pending interaction onto a working seat unmounts the line AND
  removes the command; (7) an UNFOCUSED seat's retire residual is captured by the sweep — the
  note renders with no handoff fired and no failure wording (review F1, sev-3).
- **Launch integration (L3: R5/R6)** (L299-L346 on the L3 code state) — the palette lists
  "Launch session…" and running it opens the flow (`launch-flow` appears); focusing the FLEET
  failed scout renders the banner with its bridgeError VERBATIM (and never on a healthy seat —
  asserted first), and 'Launch corrected…' opens the flow with the failed seat's harness
  pre-selected against a live stubbed capability fetch.

### Conventions

`setClientWidth` pins `clientWidth` via `defineProperty` (jsdom has no layout). All keyDown inits
carry explicit `code` (tinykeys v4 drops synthetic events without it). `afterEach` clears
localStorage (react-resizable-panels persists under autoSaveId). Relies on the vitest-only
react-resizable-panels browser-build alias (`vitest.config.ts`) — the edge-light node build skips
layout effects and would break the imperative panel API. Since L6, `vi.mock("../Terminal")` (L15)
keeps xterm entirely out of jsdom — the mock renders an inert marker div, so `PtySurface` mounts
for real while the canvas emulator never loads.

### Invariants And Boundaries

The F1a/F1b cases are the round-2 regression net for the floor chip: they must keep driving a
layout change WITHOUT a root resize. Test-only.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | L192-L660 | [SessionsView.tsx](SessionsView.tsx) |
| The L6 block: surface/WorkingLine/InteractionBar/residual/stop-gate cases (+ the Terminal jsdom mock). | L15-L19; L308-L422 | [SessionsView.test.tsx](SessionsView.test.tsx) |
| The notice store the residual cases reset and assert against. | L47-L146 | [../../data/sessionLifecycle.ts](../../data/sessionLifecycle.ts) |
| The keys-page data the drift-proof assertions read. | L62-L150 | [../../data/keymap/reserved.ts](../../data/keymap/reserved.ts) |
| The shared jsdom stubs (incl. the cmdk `scrollIntoView` stub) this suite relies on. | — | [../../test/setup.ts](../../test/setup.ts) |
| The vitest alias to the browser development build of react-resizable-panels. | — | [vitest.config.ts](../../../vitest.config.ts) |
| The L3 launch dialog + banner the integration cases exercise. | — | [LaunchFlow.tsx](LaunchFlow.tsx), [FailedLaunchBanner.tsx](FailedLaunchBanner.tsx) |
| The envelope fixture the stubbed capability fetch serves. | — | [../../test/fixtures/capabilityEnvelopes.ts](../../test/fixtures/capabilityEnvelopes.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

View tests now cover the empty-stage/no-composer boundary, slash-opened palette query, real
CodeMirror focus, PTY plus interaction plus composer ordering, and a single gate-only answer. They
exercise the actual shared composer rather than the former textarea placeholder.

## FEUI-L8 Reviewed Candidate Delta

Pins the L8 canonical Chats contract end to end: default-closed/toggleable inspector intent across responsive changes, focus/reload/handoff separation, inherited launch/routing, cleanup failure recovery, ended-versus-landed stage behavior, effective keymaps, and persistent PTY ownership.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: updated the stage integration matrix for the real composer,
  palette, PTY ordering, and sole interaction-answer path.

- 2026-07-17T06:10+02:00 — 260715-FEUI-L3 (R5/R6): +2 appended integration cases — the palette's
  "Launch session…" opens the flow, and the focused FLEET failed scout renders the banner with
  its verbatim bridgeError plus 'Launch corrected…' opening the flow pre-selected. Verification
  metadata pinned to the leaf base until closeout stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (incl. fix round): +7 cases in the L6 block — real
  PtySurface for the focused seat vs empty-stage placeholder (zone contract carried by the real
  surface), WorkingLine only-while-working in the reserved slot, InteractionBar above the
  never-replaced composer, informational stop residual ("fail" asserted absent), the UA-7-gated
  Stop-turn command naming its gap, Stop-turn disappearing with the WorkingLine's own grammar
  state (F3), and the unfocused-seat retire-residual sweep capture (F1). xterm stays out of jsdom
  via `vi.mock("../Terminal")`; the placeholder-copy update kept every L1 zone case passing (the
  pty-zone cases hydrate no sessions). Verification metadata pinned to the leaf base until
  closeout stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2: +3 integration cases against the real rail/stage —
  "view entry focuses the awaiting-input seat first" (R9), the F17 retire/land focus handoff with
  the reason-bearing `stage-handoff-note`, and alt+↑/↓ cycling over the rail order; all 21
  pre-existing L1 shell cases pass unchanged against the filled panels. Verification metadata
  pinned to the leaf base until closeout stamps the L2 code commit.
- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S5 (extended in review round 2 with the
  F1a/F1b floor-chip layout-path cases and the two rail-calibration cases): the end-to-end shell
  suite — structure/markers, palette pages + focus return, printable suppression, `/` rule, PTY
  non-interception via preventDefault observation, F6 cycle, and keep-alive `active=false`
  gating. Verification metadata pinned to the task base until closeout stamps the L1 code commit.
