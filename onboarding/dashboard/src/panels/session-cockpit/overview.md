# dashboard/src/panels/session-cockpit/ — Canonical Chats Cockpit Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/session-cockpit/`          |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-21T05:30+02:00                           |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34`       |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[panels overview](../overview.md)

## Purpose

This route is the one full-page **Chats** destination. FEUI-L8 retires the former `Chats.tsx` /
`SessionList.tsx` product path and promotes the already-built session cockpit under the Chats label;
the internal `SessionsView` filename and `[data-view="sessions"]` marker remain stable implementation
identities. `CockpitShell` defaults to Operations, keeps this route mounted, and exposes no second
Sessions destination.

The route composes a role/spawn rail, persistent stage, default-closed toggleable inspector,
CodeMirror reliable composer, command/key reference palette, status line, interaction and lifecycle
notices, and — since 260718-CHATS-L4 — the **structured conversation surface** that is now the
controlled-session stage default. It projects the shared data plane documented by the
[data overview](../../data/overview.md); it does not own a second session catalog or delivery ledger.

Since 260718-CHATS-L4 the controlled-session stage body is `ChatsStageBody.tsx`, which defaults to
the structured `ConversationSurface` (the reconstructable
[data/conversation](../../data/conversation/overview.md) projection rendered by the harness-neutral
grammar in [conversation/](conversation/overview.md)) and hosts the previous-conversation
[conversation-library/](conversation-library/overview.md) browser in-stage. The runner-line-log
`PtySurface` is no longer the controlled-session body: it survives only as the default-off,
read-only **terminal-diagnostics drawer** and as the primary body of a legacy-raw (`unsupported`)
session. Any earlier claim that this route mounts an unconditional PTY body for controlled sessions
is superseded.

## FEUI-L9R Chooser And Continuity Contract

`LaunchFlow` and `useHarnessCatalogRead` form one dialog-local catalog owner. Each open performs one
abortable read; timeout, network/HTTP/protocol error, valid empty, and ready stay distinct; Retry is
explicit; and a changed or first-observed serving boot causes one superseding reread. SSE loss does
not trigger discovery. The fixed viewport dialog remains usable on short/narrow screens, while an
empty narrow cockpit keeps the sole `＋ Chat` entrance visible and accessible.

Existing PTY panes keep their mounted xterm and scrollback across a serving restart. The shared
Terminal component asks the current connection for one boot-owned reattach; stale socket callbacks
cannot demote the replacement, and a transport close never fabricates durable terminal exit.

## FEUI-MX-FIX-2 Accepted-Row Focus Contract

`ChatContextBar.tsx` owns the raw-chat create gesture and renders typed open failures in place. It
passes only a validated accepted session id upward. `SessionsView.tsx` no longer contains a parallel
raw opener: its callback focuses the accepted row produced by the shared session store. The chooser
path reaches the same `terminalOpen.ts` authority through `LaunchFlow`, so raw and harness creates
share one parser and one zero-ghost invariant.

## 260718-CHATS-L4 Structured Conversation Roof

`ChatsStageBody.tsx` is the thin controlled-session stage body: it selects between the default
structured `ConversationSurface`, the in-stage `ConversationLibrarySurface` history browser, and the
legacy-raw PTY, and it owns the default-off `TerminalDiagnosticsDrawer`. It copies no panel's state —
the composer, InteractionBar, QueuePreview, HeaderStrip, and StatusLine remain their own authorities,
rendered by `SessionsView` around this body, and QueuePreview stays inside `SessionComposer` between
interaction and composer. It resolves the bridge epoch by REUSING `readSubmissionAuthority` (no second
submission authority) with one bounded auto-retry before the fail-loud projection-failed banner.

The renderer is a harness-neutral grammar (`conversation/`): a virtualized `role="feed"` timeline with
server-ordinal articles, full-inline thinking, stable-ID tools/diffs/interactions/results, required
image labels rendered without an `<img>` fetch, ambient evidence-bound telemetry (absent-not-zero),
and unknown-vendor events preserved as labeled evidence — no vendor-clone skins. The exact-turn
**interrupt** is wired into `WorkingLine` (its §4.1 home) through `useConversationControls`, gated on
real turn+capability evidence and registered as the `conversation.stop` chord/palette command.
History open focuses a new rail row only on exact `opened` catalog proof; every other outcome leaves
the current draft/focus/scroll intact.

## Route Model

### One Product Roof

- `SessionsView.tsx` is the composition seam for the canonical Chats route. The inspector starts
  closed, is explicitly toggleable, and remembers deliberate opt-in separately from temporary
  narrow-width collapse. Operations remains the initial shell destination.
- `ChatContextBar.tsx` carries the useful duties moved from the retired Chats page: launch hosted
  Chat/raw Terminal, show task/leaf context, explicitly local lifecycle routing for old rows, and
  server-first leaf attach/move with cross-tab invalidation.
- `ChatContextBar.tsx` reports create failures locally and emits only accepted session ids;
  `SessionsView.tsx` focuses that accepted row and never reconstructs success from request fields.
- `SessionRail.tsx` replaces the legacy `SessionList`/`sessionGroups` forest. It renders the
  `railModel` role/spawn hierarchy, master/leaf groupings, completed folders, attention rollups,
  bounded fleet optimization, termination confirmation, and landed cleanup.
- `RailChat.tsx` remains contextual task-side chat, not a competing destination.

### Stage And PTY Continuity

- Controlled seats default to the structured `ConversationSurface`, NOT a PTY body (260718-CHATS-L4).
  `PtySurface.tsx` still owns keep-alive panes, but for a controlled seat it now appears only inside
  the default-off read-only `TerminalDiagnosticsDrawer` (its new `readOnly` prop disables input);
  legacy-raw (`unsupported`) seats keep the interactive `PtySurface` as their primary body, honestly
  labeled `legacy terminal · structured conversation unavailable`. A visited inspectable terminal
  still stays mounted across focus switches, preserving the exact xterm node, socket, and scrollback.
- Landed panes remain read-only inspectable. Exited/retired rows render `EndedSessionState.tsx` and
  create no terminal/socket.
- The structured surface — not the line-log — is now the requested one-roof conversation UI. It
  consumes the landed L1/L2/L3 adapter-normalized page/library/control contracts (history index and
  exact-open resume included); the read-only PTY drawer is a diagnostic, not the message renderer.

### Reliable Composition And Interaction

- `SessionComposer.tsx` uses the shared reliable-submit client; exact drafts/request ids survive
  ambiguous outcomes. Alt+Up performs authoritative withdrawal/pop-back, never a local queue delete.
- `InteractionBar.tsx` routes pending adapter questions through their gate channel, distinct from
  ordinary chat submission. Operator text, agent-bus replies, control commands, and interaction
  answers remain separate authority paths.
- `CommandPalette.tsx` and `useKeyboardZones.ts` consume the effective map from
  [data/keymap](../../data/keymap/overview.md). The palette traps focus while open and restores the
  correct invoker; F6 is the immutable region escape, including under Vim composer mode.
- `CockpitLiveRegions.tsx` keeps polite/assertive roots mounted. Same-hydration urgent seat changes
  are batched, and repeated identical announcements replace a keyed node so assistive technology sees
  a real mutation.

### Lifecycle, Evidence, And Scale

- `LandedCleanupNotice.tsx` sits outside the collapsible rail so unavailable authority results retain
  exact targets and retry; partial outcomes retain skipped reasons.
- `EvidencePane`, `CapabilitiesPane`, and `BusPane` stay mounted behind the inspector tabs; the
  inspector is optional presentation, not required to keep their per-entry state honest.
- Rail browser optimization begins only beyond 50 actually rendered rows; inspector lists virtualize
  beyond 100 while retaining accessible list cardinality. The L8 dev scenario set exercises the real
  stores and routes for fleet, failure, launch, submit, interaction, ended, PTY-drop, and stale-catalog
  states.

## Preserved Legacy Duty Map

| Retired source | Preserved/replacement owner |
| --- | --- |
| `panels/Chats.tsx` | `Cockpit.tsx` owns one persistent Chats layer and shell catalog reconciliation; `SessionsView.tsx` owns the full route; `ChatContextBar.tsx` owns launch/routing/leaf duties. |
| `panels/Chats.test.tsx` | `Cockpit.test.tsx`, `SessionsView.test.tsx`, `ChatContextBar.test.tsx`, and `catalogPoll.test.ts` pin route uniqueness, duty transfer, focus, attach, and reconciliation. |
| `panels/SessionList.tsx` | `SessionRail.tsx` consumes `railModel.ts` and renders hierarchy, grouping, attention, completion, lifecycle controls, and fleet thresholds. |
| `panels/SessionList.test.tsx` | `SessionRail.test.tsx` and `railModel.test.ts` pin the replacement tree/role/grouping contract. |
| `data/sessionGroups.ts` | `railModel.ts` derives role/spawn/master/leaf membership; `SessionRail.tsx` renders it. |
| `data/sessionGroups.test.ts` | `railModel.test.ts` and `SessionRail.test.tsx` cover the relocated behavior. |

This is a true source retirement, not a loss of product duties. Historical sidecar knowledge was
folded into this map, the data overview, and the current replacement file cards before obsolete
one-to-one sidecars were deleted.

## One-Roof Conversation Contract (realized in 260718-CHATS-L4)

The one shared visual message roof across Claude, Codex, and Pi is now landed. The two distinct
capabilities are both served: the **active conversation transcript** by the reconstructable
[data/conversation](../../data/conversation/overview.md) projection + the `conversation/` grammar, and
the **previous-conversation library/index** by [data/conversation-library](../../data/conversation-library/overview.md)
+ the `conversation-library/` browser. Both consume adapter-normalized history/index/resume from the
landed L1/L2/L3 server contracts and hold only a projection/cache — no durable browser conversation
database (R1). Visible harness identity and capability reasons are surfaced honestly; harness-specific
behavior stays in the adapters.

UA-1 is no longer absent: controlled sessions render the structured surface by default. The PTY
survives only as the read-only terminal-diagnostics drawer and the legacy-raw body. Two forward
constraints remain: interrupt capability gating is attempt-and-reflect on the L3 routes' evidence
until a control-capabilities GET or an L1-view refresh lands (a clean proactive gate), and the
measured virtualization/scale baseline plus the E1/E2 environmental faults are L5 hardening
(see the L5-Facing Register in the `conversation/` overviews).

## 260718-CHATS-L5P Cockpit chrome conventions (visual polish, PASS-WITH-NOTES)

A dashboard-only polish pass (zero backend edits) closing the developer's visual-findings file + the FB7
terminal-identity directive against the COMPOSED app. Durable cross-file conventions the next
session-cockpit leaf MUST carry (spec home for the TUI grammar: the leaf visual-audit `## FB7`, derived
from Toad `main.tcss` + the Claude Code / Codex TUIs — a reference derivation, not first principles):

- **Terminal well + gutter grammar (FB7).** The structured stage is a TUI, not a web panel: the
  `ConversationTimeline` viewport + `SessionComposer` editor frame use the `well` token (`#070b0f`, the
  xterm pty inset — `styles/tokens.css`/`panda.config.ts`; pty-pane parity is the acceptance test), the
  item chrome is `●`/`✻`/`·` gutter glyphs + lowercase phase words + left-rule washes (NOT boxed
  uppercase chips), and item rhythm is line-grid blank lines (no per-article hairline). See the
  `conversation/` overview + item cards.
- **Responsive rail-row grammar (RV-2).** `SessionRail` rows are a `flex-wrap:wrap` LABEL-group +
  ACTION-group layout: the action group (End / armed confirm·cancel) wraps WHOLE to a second line and
  stays single-line + reachable at every rail width (1440/1100/900/min-rail, e2e-pinned); the title
  absorbs (`min-width:0` end-to-end) and elides first, the chip elides next and is DROPPED while armed.
  Destructive End carries demoted (muted) weight until hover/focus/selection.
- **Collapse-or-explain chrome (R3/R4/A1/A2).** StatusLine/HeaderStrip/top-bar: an absent value
  disappears with its label (never an em-dash chain), the healthy steady state collapses to one calm
  token (`poll ✓`, `inbox clear`), a reassurance zero never wears an alarm glyph. The StatusLine UA-5
  `ctx —/cost —` slot was REMOVED.
- **Humanized durations + short ids.** `data/conversation/format.humanizeDuration` is the SINGLE duration
  authority (supervisor age, rail-footer heartbeat/cutoff, uptime — no raw `9512.1m`/`570724.69163s`);
  the new `format.shortId` renders long ULIDs/UUIDs as `…SUFFIX` with the full value in a tooltip (rail
  task badges, focus-handoff banner).
- **The @webtui/css `word-break: break-all` cascade trap (RV-1, LOAD-BEARING).** `@webtui/css`'s base
  (postcss-rewritten onto `[data-view="sessions"]`) sets `word-break: break-all`, which defeats EVERY
  component-level `overflow-wrap` patch in render. The remedy is one unlayered `word-break: normal` root
  override in `index.css`; raw-id spans keep explicit `break-all`. The test is computed-value
  verification, not source inference. Any future mid-word-break fix in this route depends on that
  override — see `index.css` card.

## Invariants And Boundaries

- Exactly one full-page Chats destination; no second Sessions tab or legacy Chats layer.
- Exactly one browser open authority; rejected raw or harness creates produce no registry row,
  focus change, readiness transition, or dependent delivery.
- Operations is the default destination; the Chats inspector is closed by default and always
  toggleable/reopenable. Responsive collapse cannot erase deliberate operator intent.
- Cockpit focus and the live action route are separate: a landed row may remain focused while a live
  row owns launch/gate/composer actions and reload preference.
- Controlled seats default to the structured surface; the PTY is NOT the controlled-session body. The
  keep-alive PTY owner still exists (read-only diagnostics drawer + legacy-raw body) and a one-render
  focus gap must not dispose unrelated visited terminals.
- The structured surface holds only a reconstructable projection: no IndexedDB/localStorage/SQLite
  conversation index and no optimistic durable item authority; the only persisted UI bit is the
  hide-thinking boolean. Diagnostics and hidden stages are `inert`+`aria-hidden` and mount no PTY
  when closed.
- Ended rows do not receive live controls, composer, interaction bar, or a socket. Landed rows remain
  read-only until authoritative cleanup.
- Reliable submit/withdrawal, interaction answer, agent bus, and control commands never fall back to
  shared paste or silently cross authority channels.
- The inspector must not become required for core Chats operation; it is supplementary evidence and
  debugging/coordination detail.

## Hot Path Summary

1. A create gesture crosses the shared opener; only an accepted server row reaches the registry and
   the context bar's focus callback.
2. Shell reconciliation hydrates catalog rows and the persistent Chats layer.
3. `SessionsView` resolves deliberate/smart focus and live action ownership, then derives one rail
   model/attention rollup for rail and palette.
4. `SessionRail` selects a row; the stage keeps visited inspectable PTYs alive and shows ended-state
   overview when no terminal exists.
5. Composer, interaction, attach, set, terminate, cleanup, and bus actions cross their own authority
   routes and project results back into shared stores.
6. Palette/keymap, status, inspector, and live regions expose the same evidence without inventing a
   second operational truth.

## Child Route Onboarding Map

| Child route | Governing overview | Responsibility |
| --- | --- | --- |
| `session-cockpit/conversation/` | [structured conversation renderer](conversation/overview.md) | The harness-neutral grammar: feed timeline, item/block components, telemetry, interrupt hook, reconnect. |
| `session-cockpit/conversation-library/` | [in-stage history browser](conversation-library/overview.md) | The previous-conversation library surface, list, read-only preview, and the sole exact-open resume action. |

The other `session-cockpit/` sources (including `ChatsStageBody.tsx`) have one-to-one file cards and
this overview is their governing pillar.

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Full-route composition | [SessionsView.tsx](SessionsView.tsx.md) |
| Structured stage body composition | [ChatsStageBody.tsx](ChatsStageBody.tsx.md) |
| Structured renderer grammar | [conversation/ overview](conversation/overview.md) |
| In-stage history browser | [conversation-library/ overview](conversation-library/overview.md) |
| Rail and product-duty bar | [SessionRail.tsx](SessionRail.tsx.md) · [ChatContextBar.tsx](ChatContextBar.tsx.md) |
| PTY (diagnostics/legacy-raw) and ended presentation | [PtySurface.tsx](PtySurface.tsx.md) · [EndedSessionState.tsx](EndedSessionState.tsx.md) |
| Cleanup/lifecycle copy | [LandedCleanupNotice.tsx](LandedCleanupNotice.tsx.md) · [lifecycleCopy.ts](lifecycleCopy.ts.md) |
| Palette and keyboard binding | [CommandPalette.tsx](CommandPalette.tsx.md) · [useKeyboardZones.ts](useKeyboardZones.ts.md) |
| Launch chooser and request ownership | [LaunchFlow.tsx](LaunchFlow.tsx.md) · [useHarnessCatalogRead.ts](useHarnessCatalogRead.ts.md) |

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured. Product and
interaction claims were verified from same-repository source/tests, the final reviewer PASS, the L8
task evidence, and the recovered same-repository history pack.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found for the canonical Chats route. | Source discovery checked | — |

## Cross-Repo References

The route composes repository-local data and server clients. Toad/T3 were historical design
references, not imported governing implementations, so no cross-repository source is cited here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository implementation source governs FEUI-L8. | Import and recovered-history review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Full-route composition and shell ownership. | [SessionsView.tsx](SessionsView.tsx) · [../../cockpit/Cockpit.tsx](../../cockpit/Cockpit.tsx) |
| Legacy duty bar. | [ChatContextBar.tsx](ChatContextBar.tsx) |
| Role/spawn rail and data derivation. | [SessionRail.tsx](SessionRail.tsx) · [../../data/railModel.ts](../../data/railModel.ts) |
| PTY/ended continuity. | [PtySurface.tsx](PtySurface.tsx) · [EndedSessionState.tsx](EndedSessionState.tsx) |
| Cleanup authority notice. | [LandedCleanupNotice.tsx](LandedCleanupNotice.tsx) |
| Effective keyboard contract. | [../../data/keymap/overview.md](../../data/keymap/overview.md) |
| Dev end-to-end scenario authority. | [../../dev/cockpitScenarios.ts](../../dev/cockpitScenarios.ts) |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator (cockpit chrome visual polish, PASS-WITH-NOTES):
  added the "Cockpit chrome conventions" section recording the durable cross-file design truths this
  dashboard-only leaf established — the FB7 terminal well + gutter grammar, the RV-2 responsive rail-row
  grammar, collapse-or-explain chrome (StatusLine/HeaderStrip/top-bar, UA-5 slot removed), the
  humanize-duration single authority + `shortId`, and the load-bearing `@webtui/css` `word-break:
  break-all` cascade trap + unlayered root-override remedy (RV-1). No route composition, authority, or
  invariant changed; zero backend edits. Spec home for the TUI grammar is the leaf visual-audit `## FB7`.
  Verification stays pinned to the leaf base (`352d5cd`) because the polish candidate is uncommitted;
  closeout owns candidate stamping.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator (structured Chats renderer, reviewer FINAL PASS,
  26/26 findings closed): recorded the composition change from the unconditional controlled-session
  PtySurface body to `ChatsStageBody` (structured `ConversationSurface` is the controlled-session
  default; PTY demoted to the default-off read-only terminal-diagnostics drawer + legacy-raw body),
  the two new child routes `conversation/` (harness-neutral grammar + interrupt hook) and
  `conversation-library/` (in-stage history browser + sole exact-open resume), the realized one-roof
  conversation contract (both active transcript and previous-conversation library served from the
  landed L1/L2/L3 adapter-normalized contracts as a reconstructable projection — no durable browser
  index), the `WorkingLine` interrupt prop / `conversation.stop` chord, and the corrected
  PTY-not-unconditional invariant. Superseded the FEUI-L8 "controlled sessions still expose the runner
  line-log because UA-1 is absent" claim. Verification metadata remains pinned to the FEUI-MX-FIX-2
  base because the reviewed L4 candidate is uncommitted; closeout owns candidate stamping.

- 2026-07-18T15:22+02:00 — FEUI-MX-FIX-2: recorded ChatContextBar as the raw-create gesture owner,
  SessionsView as accepted-row-only focus, shared raw/harness parsing through LaunchFlow, and the
  zero-row/zero-focus failure contract. Verification metadata remains pinned pending closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: added the one-owner chooser recovery state machine, narrow
  accessibility exception, fixed viewport boundary, and xterm-preserving boot reattach contract.
  Verification metadata remains pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — 260715-FEUI-L8 final curator pass: promoted this route to the sole
  product-facing Chats destination, recorded Operations/default-closed-inspector decisions, folded
  in legacy Chats/SessionList/sessionGroups duties before sidecar retirement, documented persistent
  PTY/ended/cleanup/keymap/scenario hardening, and preserved the future one-roof conversation plus
  absent-UA-1 boundary. Metadata remains pinned to the leaf base until closeout.
- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 (Round 3 reviewer PASS): replaced the interim inspector
  with stable-mounted Evidence/Capabilities/Bus panes, added the contractual StatusLine, preserved
  per-entry reply state through filter/virtual/off-tab unmount pressure, restricted reverse replies
  to sender identity, surfaced post-removal stop residuals, and documented the 100/101 accessible
  virtualization boundary. Verification metadata remains pinned to the leaf base until closeout.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: replaced the composer/queue stub with the live
  shared CodeMirror surface, exact submit/reconcile lifecycle, QueuePreview, zone-sensitive Alt+Up,
  authoritative withdrawal, response-loss convergence, revision-CAS recovery, and no-PTY-fallback
  invariants.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4: filled exact-session model/effort controls and their
  evidence/toast/live-region surfaces after final reviewer PASS; metadata remained pinned.
- 2026-07-17T06:20+02:00 — 260715-FEUI-L3: added capability-driven launch and failed-launch
  correction surfaces after final reviewer PASS; metadata remained pinned.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6: filled PTY, interaction, lifecycle, residual, and
  working-line surfaces after final reviewer PASS; chose the DOM renderer by measurement.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2: added the data layer, rail, stage, attention, smart focus,
  and palette composition after final reviewer PASS; metadata remained pinned.
- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 as the Sessions-named cockpit shell with
  resizable panels, keyboard/palette foundation, floor hint, and rail calibration.
