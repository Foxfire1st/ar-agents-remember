# dashboard/src/panels/session-cockpit/SessionsView.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionsView.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T10:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

### FEUI MX-FIX-2 Accepted Raw Integration Fixture

The legacy-duty integration case now returns a complete accepted raw-session response carrying
the selected lifecycle and server seat role. It continues to prove persistence and focus, but only
through the accepted-row path rather than an empty `ok` response.

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
- **L6 stage surface + lifecycle honesty (cit:(["L6: stage surface, WorkingLine, InteractionBar, stop residuals"], dashboard/src/panels/session-cockpit/SessionsView.test.tsx:1034-1588))** — the block contains 14 tests; the seven
  original cases are still there and assert what is described. Residual behavior records lifecycle
  notice-store state without stacking a separate DOM notice. Seven cases against the real store
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
- **Launch integration (L3: R5/R6)** (cit:(["launch flow + failed-launch banner integration"], dashboard/src/panels/session-cockpit/SessionsView.test.tsx:1590-1649)) — the palette lists
  "Launch session…" and running it opens the flow (`launch-flow` appears); focusing the FLEET
  failed scout renders the banner with its bridgeError VERBATIM (and never on a healthy seat —
  asserted first), and 'Launch corrected…' opens the flow with the failed seat's harness
  pre-selected against a live stubbed capability fetch.

### Conventions

`setClientWidth` pins `clientWidth` via `defineProperty` (jsdom has no layout). All keyDown inits
carry explicit `code` (tinykeys v4 drops synthetic events without it). `afterEach` clears
localStorage (react-resizable-panels persists under autoSaveId). Relies on the vitest-only
  react-resizable-panels browser-build alias (`vitest.config.ts`) — the edge-light node build skips
  layout effects and would break the imperative panel API. Since L6, `vi.mock("../Terminal")` keeps
  xterm entirely out of jsdom (cit:(["\"../Terminal\""], dashboard/src/panels/session-cockpit/SessionsView.test.tsx:121-145)).
  The L6 block contains the composition-level mount-ledger cases
  (cit:(["L6: stage surface, WorkingLine, InteractionBar, stop residuals"], dashboard/src/panels/session-cockpit/SessionsView.test.tsx:1034-1588)).

**Conversation-wire fixtures come from the shared builders (260731-EFA-L4).** `L5Q_IDENTITY`,
`l5qStatus`, the items and page in `seedWorkerL4Items`, and the answer case's lifecycle+gate are built
with `conversationIdentity` / `conversationStatus` / `conversationItem` / `conversationPage`
(`test/fixtures/conversationWire.ts`) and `lifecycle` / `gate` (`test/fixtures/wire.ts`) instead of
literals cast with `as unknown as …`. Two consequences a future author should expect rather than
rediscover: the seeded page's `capabilities` was literally `undefined as unknown as
ConversationCapabilities` on a REQUIRED field and is now the full 23-leaf tree with every leaf
`supported`; and `page.totalItems` is now set, so the timeline emits an `aria-setsize` it previously
omitted. Both reach only `seedWorkerL4Items`, i.e. the F-ac scroll-restore case — every other live
seed goes through `emptyProjection(L5Q_IDENTITY)`, which supplies its own capabilities and is
untouched.

### Invariants And Boundaries

The F1a/F1b cases are the round-2 regression net for the floor chip: they must keep driving a
layout change WITHOUT a root resize. Test-only.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test (`SessionsViewImpl`, exported memoized). | `SessionsViewImpl` | dashboard/src/panels/session-cockpit/SessionsView.tsx:196-1331 |
| The L6 block contains the surface, WorkingLine, InteractionBar, residual, and stop-gate cases. | "L6: stage surface, WorkingLine, InteractionBar, stop residuals" | dashboard/src/panels/session-cockpit/SessionsView.test.tsx:1034-1588 |
| The Terminal mount ledger is declared here. | "const mockTerminalMounts: string[] = [];" | dashboard/src/panels/session-cockpit/SessionsView.test.tsx:119-119 |
| The Terminal unmount ledger is declared here. | "const mockTerminalUnmounts: string[] = [];" | dashboard/src/panels/session-cockpit/SessionsView.test.tsx:120-120 |
| The Terminal jsdom mock implementation is defined here. | "\"../Terminal\"" | dashboard/src/panels/session-cockpit/SessionsView.test.tsx:121-145 |
| The notice store the residual cases reset and assert against. | `lifecycleNoticeStore` | dashboard/src/data/sessionLifecycle.ts:68-121 |
| The keys-page binding text the drift-proof assertions render. | "ctrl+alt+pagedown" | dashboard/src/panels/session-cockpit/SessionsView.test.tsx:329-329 |
| The shared jsdom stubs (incl. the cmdk `scrollIntoView` stub) this suite relies on. | "Element.prototype.scrollIntoView =" | dashboard/src/test/setup.ts:29-29 |
| The vitest alias to the browser development build of react-resizable-panels. | "react-resizable-panels.browser" | dashboard/vitest.config.ts:20-20 |
| The L3 launch dialog the integration cases exercise. | `LaunchFlow` | dashboard/src/panels/session-cockpit/LaunchFlow.tsx:177-619 |
| The failed-launch banner rendered by the integration cases. | `FailedLaunchBanner` | dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:70-182 |
| The integration cases that exercise the launch flow and failed-launch banner. | "launch flow + failed-launch banner integration" | dashboard/src/panels/session-cockpit/SessionsView.test.tsx:1590-1649 |
| The envelope fixture the stubbed capability fetch serves. | `capabilityEnvelope` | dashboard/src/test/fixtures/capabilityEnvelopes.ts:160-172 |
| The `conversationIdentity` fixture builder is defined here. | `conversationIdentity` | dashboard/src/test/fixtures/conversationWire.ts:172-185 |
| The `conversationStatus` fixture builder is defined here. | `conversationStatus` | dashboard/src/test/fixtures/conversationWire.ts:187-207 |
| The `conversationItem` fixture builder is defined here. | `conversationItem` | dashboard/src/test/fixtures/conversationWire.ts:209-226 |
| The `conversationPage` fixture builder is defined here. | `conversationPage` | dashboard/src/test/fixtures/conversationWire.ts:228-243 |
| The lifecycle builder is defined for the answer-case fixtures. | "function lifecycle<" | dashboard/src/test/fixtures/wire.ts:241-241 |
| The gate builder is defined for the answer-case fixtures. | "function gate" | dashboard/src/test/fixtures/wire.ts:248-248 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
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

## 260718-CHATS-L4 Reviewed Candidate Delta

Six cases are updated from the pre-L4 unconditional-PTY architecture to the new `ChatsStageBody`
composition (Deviation 3; reviewer-accepted — 5-of-6 faithful re-targets, the sixth's keep-alive
assertion class retired to the `data/conversation/store.test.ts` suite): the empty-stage case asserts
the pick-a-session identity; the keyboard-zone cases seed a legacy-raw session (the remaining real
`pty` zone host) and target the real PTY host; the landed-cleanup case keeps its focus-handoff subject
and drops the PTY-scrollback assertions; the L6 composition case now proves the structured default plus
the read-only diagnostics drawer (R2/R7). No test intent was silently dropped.

The reviewed candidate is uncommitted; existing verification hash/date remain pinned; closeout owns
commit stamping.

## Current L5I Maintenance

The composition suite now covers stage guttering, rail-to-input focus handoff, title-row controls,
SSE-preferred working feedback, removal of the StatusLine/end-notice chrome, and visibility passed
to the kept-alive conversation stage.

## Update History

- 2026-08-04T15:56:39+02:00 — 260731-EFA-L6 S18-B10 curator: closed same-reviewer residual D14 by splitting the Terminal mount/unmount ledger declarations from the complete jsdom mock implementation and binding the prose claim to that implementation; rechecked this card through the locked exact-document fixer/check.

- 2026-08-01T10:00+02:00 — 260731-EFA-L4 curator: recorded the conversation-wire fixture conversion and
  repaired four stale ranges. New Conventions paragraph names the two deltas the conversion actually
  produced in this file, both verified against the diff rather than assumed: the page's `capabilities`
  went from `undefined as unknown as ConversationCapabilities` — an explicit `undefined` on a REQUIRED
  field — to the full supported tree, and `page.totalItems` is now set (hence an `aria-setsize` that was
  previously absent). I traced the blast radius before attesting: those come from `conversationPage`,
  which only `seedWorkerL4Items` calls, which only the F-ac scroll-restore case uses; every other live
  seed goes through `emptyProjection(L5Q_IDENTITY)` and supplies its own capabilities, so the two
  NEGATIVE stop-command cases (L1469, L1484) still gate on the projection they always did and did not
  become tolerant. The answer case's lifecycle now carries `state: "blocked"` from `BASE_LIFECYCLE`
  where it previously had none, and its gate still sets `decisions: []` explicitly, so `BASE_GATE`'s
  `["approve","revise"]` never applies. Suite re-run: 1 file, all cases pass. Citation repairs, each
  re-anchored on its proving symbol: the L6 block `L308-L422` → `L1034-L1589` (and the "seven cases"
  wording qualified — the block now holds 17 `it`s, the seven originals among them); launch integration
  `L299-L346 on the L3 code state` → `L1590-L1658`; the Terminal mock `L15` → `L121-L145`, where it also
  gained the `mockTerminalMounts`/`mockTerminalUnmounts` ledgers the card did not mention; the component
  row `L192-L660` → `L196-L660; L1336` so it opens on `SessionsViewImpl` and reaches the memo export.
  Two rows added for the builder modules.

- 2026-07-24T13:17:17Z — Curator: recorded current stage-composition and retired-StatusLine
  regressions; verification fields remain pre-commit.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: recorded the six SessionsView test updates from the
  pre-L4 unconditional-PTY architecture to the `ChatsStageBody` composition (Deviation 3), including the
  structured-default + read-only-diagnostic L6 case and the keep-alive assertion class relocating to the
  conversation store suite. Verification metadata remains pinned to the leaf base until closeout stamps
  the L4 commit.
- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: updated raw-terminal integration to a complete accepted
  server row so lifecycle inheritance and focus are proven behind the authority gate. Verification
  metadata remains pinned until closeout.

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
