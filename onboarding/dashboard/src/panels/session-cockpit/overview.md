# dashboard/src/panels/session-cockpit/ — Canonical Chats Cockpit Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/session-cockpit/`          |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-18T12:43+02:00                           |
| lastVerifiedCommitHash | `82f2de40a666ea00754f364cfe764cea9294235f`       |
| lastVerifiedCommitDate | 2026-07-18T13:07:00+02:00|
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
notices, and real PTY panes. It projects the shared data plane documented by the
[data overview](../../data/overview.md); it does not own a second session catalog or delivery ledger.

## FEUI-L9R Chooser And Continuity Contract

`LaunchFlow` and `useHarnessCatalogRead` form one dialog-local catalog owner. Each open performs one
abortable read; timeout, network/HTTP/protocol error, valid empty, and ready stay distinct; Retry is
explicit; and a changed or first-observed serving boot causes one superseding reread. SSE loss does
not trigger discovery. The fixed viewport dialog remains usable on short/narrow screens, while an
empty narrow cockpit keeps the sole `＋ Chat` entrance visible and accessible.

Existing PTY panes keep their mounted xterm and scrollback across a serving restart. The shared
Terminal component asks the current connection for one boot-owned reattach; stale socket callbacks
cannot demote the replacement, and a transport close never fabricates durable terminal exit.

## Route Model

### One Product Roof

- `SessionsView.tsx` is the composition seam for the canonical Chats route. The inspector starts
  closed, is explicitly toggleable, and remembers deliberate opt-in separately from temporary
  narrow-width collapse. Operations remains the initial shell destination.
- `ChatContextBar.tsx` carries the useful duties moved from the retired Chats page: launch hosted
  Chat/raw Terminal, show task/leaf context, explicitly local lifecycle routing for old rows, and
  server-first leaf attach/move with cross-tab invalidation.
- `SessionRail.tsx` replaces the legacy `SessionList`/`sessionGroups` forest. It renders the
  `railModel` role/spawn hierarchy, master/leaf groupings, completed folders, attention rollups,
  bounded fleet optimization, termination confirmation, and landed cleanup.
- `RailChat.tsx` remains contextual task-side chat, not a competing destination.

### Stage And PTY Continuity

- `PtySurface.tsx` owns keep-alive panes. A visited inspectable terminal stays mounted across focus
  switches and across the transient removed-focus render before smart handoff, preserving the exact
  xterm node, socket, and scrollback.
- Running controlled seats show a runner line-log; legacy raw seats may host a vendor TUI. Landed
  panes remain read-only inspectable. Exited/retired rows render `EndedSessionState.tsx` and create no
  terminal/socket.
- This line-log/PTY surface is **not** the requested structured conversation UI. FEUI-L8 establishes
  the visual/product roof and interaction mechanics but does not claim adapter-normalized message
  rendering, history index, or resume support.

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

## Future One-Roof Conversation Contract

Recovered project history requires one shared visual message roof across Claude, Codex, and Pi while
showing which harness supplies each session and preserving harness-specific behavior through adapters.
Two capabilities remain distinct: the active conversation transcript and the previous-conversation
library/index. The preferred architecture asks adapters for normalized history/index/resume rather
than duplicating vendor history in browser state; the browser may project/cache authoritative results.

UA-1 capability is absent in FEUI-L8. No current component should claim structured conversation
rendering, previous-chat navigation, or adapter history transmission until that contract is proven.
The existing PTY remains a useful fallback/diagnostic surface, not the final message renderer.

## Invariants And Boundaries

- Exactly one full-page Chats destination; no second Sessions tab or legacy Chats layer.
- Operations is the default destination; the Chats inspector is closed by default and always
  toggleable/reopenable. Responsive collapse cannot erase deliberate operator intent.
- Cockpit focus and the live action route are separate: a landed row may remain focused while a live
  row owns launch/gate/composer actions and reload preference.
- The PTY owner is unconditional inside the persistent route. A one-render focus gap must not dispose
  unrelated visited terminals.
- Ended rows do not receive live controls, composer, interaction bar, or a socket. Landed rows remain
  read-only until authoritative cleanup.
- Reliable submit/withdrawal, interaction answer, agent bus, and control commands never fall back to
  shared paste or silently cross authority channels.
- The inspector must not become required for core Chats operation; it is supplementary evidence and
  debugging/coordination detail.

## Hot Path Summary

1. Shell reconciliation hydrates catalog rows and the persistent Chats layer.
2. `SessionsView` resolves deliberate/smart focus and live action ownership, then derives one rail
   model/attention rollup for rail and palette.
3. `SessionRail` selects a row; the stage keeps visited inspectable PTYs alive and shows ended-state
   overview when no terminal exists.
4. Composer, interaction, attach, set, terminate, cleanup, and bus actions cross their own authority
   routes and project results back into shared stores.
5. Palette/keymap, status, inspector, and live regions expose the same evidence without inventing a
   second operational truth.

## Child Route Onboarding Map

No deeper child route exists below `session-cockpit/`; each source has a one-to-one file card and
this overview is their governing pillar.

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Full-route composition | [SessionsView.tsx](SessionsView.tsx.md) |
| Rail and product-duty bar | [SessionRail.tsx](SessionRail.tsx.md) · [ChatContextBar.tsx](ChatContextBar.tsx.md) |
| PTY and ended presentation | [PtySurface.tsx](PtySurface.tsx.md) · [EndedSessionState.tsx](EndedSessionState.tsx.md) |
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
