# dashboard/src/panels/session-cockpit/ — Canonical Chats Cockpit Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/session-cockpit/`          |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-08-07T23:35:00+02:00 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`       |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[panels overview](../overview.md)

## 260731-EFA-L8 Change

### 260713-TES-L1 Rename — Heartbeat UI

The session-cockpit heartbeat surface is renamed with the sweep: `BusPane` / `SeatInspector` /
`SessionRail` / `sessionRailParts` and the sessions-view body/controller now type and key the
heartbeat as `AgentNotifierHeartbeat` / `agentNotifierHeartbeat` and render "Agent notifier
heartbeat" (was "Supervisor heartbeat"). Fixtures and tests were updated to the new type and key;
the rail-bus footer remains removed and liveness stays in the top bar.

`SessionsView` moved to `sessions-view/` with controller/body/palette/styles
modules and six behavior-split test files. Shared surfaces gained parts/styles
modules (`interactionParts*`, `launchFlowParts*`, `sessionRailParts*`,
`stageLayers.tsx`, `chatsStageStyles.ts`, `conversationSurfaceParts*`). The e2e
repair fixed a genuine keep-alive defect in `ChatsStageBody` (the PTY layer stays
mounted through smart-focus handoff) and the Terminal headless-focus delegation;
the primary Playwright suite now asserts the real DOM order (rail → stage →
inspector).

## Purpose

This route is the one full-page **Chats** destination. FEUI-L8 retires the former `Chats.tsx` /
`SessionList.tsx` product path and promotes the already-built session cockpit under the Chats label;
the internal `SessionsView` filename and `[data-view="sessions"]` marker remain stable implementation
identities. `CockpitShell` defaults to Operations, keeps this route mounted, and exposes no second
Sessions destination.

The route composes a role/spawn rail, persistent stage, default-closed toggleable inspector,
CodeMirror reliable composer, command/key reference palette, source-selected working cues, interaction and lifecycle
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
the composer, InteractionBar, QueuePreview, and HeaderStrip remain their own authorities,
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

## Sub-Agent Lanes And Multiplexed Pending Interactions

The structured surface now renders harness sub-agents as first-class lanes. `ConversationSurface`
derives the roster from the per-item agent refs, hosts an `AgentsArea`, and cycles parent → agent
lanes on ArrowLeft/ArrowRight with Escape returning to the parent (editable/interactive targets own
their keys). The stored focus lives outside the projection, survives LRU eviction, and is
re-validated against the rehydrated roster rather than applied blindly; the focus switch is
announced politely and only for the operator's own action on a visible surface.

`ConversationLibraryList` renders a row's sub-agent conversations as indented child rows that
select, preview, and open through the exact same flow as a top-level row — the child's
`conversationKey` is minted server-side — and renders the page's `agentsNote` verbatim when the
server reports (partial) agent-history unavailability.

`InteractionBar` is multiplexed: one bar per pending interaction — the parent's singular slot
first, then the sub-agent entries from the additive plural catalog slot, de-duplicated by
interactionId — each badged with the adapter-bound agent label (absent on the parent, never
fabricated) and answered through the same channel routing, so a sub-agent approval is never
dropped into the legacy gate fallback. Rail rows and the palette's question triage preview name
who asks, and a seat blocked solely on a sub-agent approval still reads awaiting-input.

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
the **previous-conversation library/index** by [data/conversation-library](../../data/conversation-library/overview.md) +
the `conversation-library/` browser. Both consume adapter-normalized history/index/resume from the
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
- **Collapse-or-explain chrome.** Header/top-bar values disappear with their labels rather than
  forming em-dash chains; reassurance zeros do not wear alarm glyphs. The former StatusLine footer
  is retired entirely, so it no longer owns a reserved ctx/cost slot or reopen controls.
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for the canonical Chats route. | — | — |

## Cross-Repo References

The route composes repository-local data and server clients. Toad/T3 were historical design
references, not imported governing implementations, so no cross-repository source is cited here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository implementation source governs FEUI-L8. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Full-route composition and shell ownership. | "import { SessionsView } from \"../panels/session-cockpit/sessions-view/SessionsView\";"; "data-testid=\"sessions-stage\"" | dashboard/src/cockpit/Cockpit.tsx:47-47; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:286-286 |
| Legacy duty bar. | `ChatContextBar` | dashboard/src/panels/session-cockpit/ChatContextBar.tsx:74-117 |
| Role/spawn rail and data derivation. | `SessionRail`, `buildRailModel` | dashboard/src/data/railModel.ts:192-235; dashboard/src/panels/session-cockpit/SessionRail.tsx:149-236 |
| PTY/ended continuity. | "import { lazy, Suspense, useEffect, useMemo, useRef, useState } from \"react\";"; "import { EndedSessionState } from \"./EndedSessionState\";"; "The PtySurface: the session stage's terminal half. Wraps the"; "export function EndedSessionState({ session }: { session: OpenSession }) {" | dashboard/src/panels/session-cockpit/PtySurface.tsx:1-1; dashboard/src/panels/session-cockpit/PtySurface.tsx:19-19; dashboard/src/panels/session-cockpit/PtySurface.tsx:21-21; dashboard/src/panels/session-cockpit/EndedSessionState.tsx:35-35 |
| Cleanup authority notice. | `LandedCleanupNotice` | dashboard/src/panels/session-cockpit/LandedCleanupNotice.tsx:48-113 |
| Effective keyboard contract. | "export function useEffectiveKeymap(): EffectiveKeymap {"; "export function useKeyboardZones({" | dashboard/src/data/keymap/preferences.ts:329-331; dashboard/src/panels/session-cockpit/useKeyboardZones.ts:18-97; dashboard/src/data/keymap/preferences.ts:369-369 |
| Dev end-to-end scenario authority. | `COCKPIT_SCENARIOS` | dashboard/src/dev/cockpitScenarios.ts:113-207 |
| The shared builders every cockpit suite seeds wire nodes from (projection side and conversation side). | `SERVED`, `conversationPage` | dashboard/src/test/fixtures/conversationWire.ts:228-243; dashboard/src/test/fixtures/wire.ts:66-66 |
| The cast guard, its first-line mirror-marker discovery rule, and its own list of unmarked blind-spot modules. | `collectWireFixtureFindings` | dashboard/src/test/wireFixtureGuard.ts:484-587 |
| The launch chooser's catalog types and the server model they mirror (`HarnessInfo` ↔ `DetectedHarness`). | `HarnessInfo`, `DetectedHarness` | dashboard/src/data/harnessCatalog.ts:5-9; mcp/src/agents_remember/serving/response_contract.py:355-360 |

## Current L5I Route State

The stage now keeps controlled conversation surfaces mounted per warm projection and preserves their
scroll geometry across both focus and cockpit-view switches. It separates `visibility:hidden` pool
entries from `display:none` view geometry, remembers/recovers intentional position, and bounds
retention with the conversation LRU. The once-standing StatusLine and rail-bus footer are retired:
stage actions live by the title, working feedback sits beside the conversation/composer, and detailed
evidence remains in the inspector. Structured decision pages, queue steering, and the direct
interaction route maintain distinct authority channels.

## 260727-CHATS-IM-L2 Route Impact

Within the existing conversation child route, focus now triggers bounded native hydration only for
the effective selected agent, and exact roster identities survive incremental updates and reload.
The cockpit's rail, stage, composer, diagnostics, and layout ownership remain unchanged.

## 260731-EFA-L4 Fixture Contract For This Route

No cockpit component changed. All seven changed sources are SUITES, and the durable rule they now
carry is: **a session-cockpit test may not author its own wire node.** Projection nodes come from
`test/fixtures/wire.ts`, conversation and library nodes from `test/fixtures/conversationWire.ts`, and
the `as unknown as <WireType>` casts these seven carried are gone. A cast skips excess-property
checking, so a cast fixture can state a payload the server would reject; a builder call cannot.

Three of the removed casts were stating exactly that, and correcting them changed the shape under
assertion — not the assertions:

- `ChatsStageBody.test.tsx` seeded `capabilities: undefined as unknown as ConversationCapabilities`,
  which claims a REQUIRED field is absent; `QueuePreview.test.tsx` and `SessionsView.test.tsx` built
  or omitted the tree by hand. All three now carry the full four-group tree
  (`live`/`history`/`controls`/`telemetry`) from `conversationCapabilities()`, which is what the server
  fills.
- `SessionRail.test.tsx` seeded `{ taskDocuments, agentPickups } as unknown as Analytics` — an
  `Analytics` carrying two of its thirteen keys. `analytics()` spreads `EMPTY_ANALYTICS`, so every list
  key is present and empty, which is the shape the reducer always sends (they are list defaults
  server-side).
- Pages built through `conversationPage()` now carry `page.totalItems`, derived from the item array
  rather than omitted.

**`LaunchFlow.test.tsx` is the one file whose PROOF moved, and it moved down.** Its `HARNESSES` stub
carried `control: "starting"` on all three rows — a field `serving/response_contract.py::DetectedHarness`
does not declare, `data/harnessCatalog.ts::HarnessInfo` does not mirror, and no dashboard code reads,
on a `WireResponse` whose `model_config` is `extra="forbid"`. All three keys are gone. The consequence
must be stated plainly, because it is a guarantee this route no longer has: the suite's surviving
`not.toContain("adapter starting")` assertions have nothing planting the field, so they can no longer
fail, and any claim that this suite proves a stale legacy `control` field is not rendered is
**superseded**. The replacement is narrower and honest — `const HARNESSES: { harnesses: HarnessInfo[] }`
turns an extra field on a fresh literal into a `tsc -b` error, and a new describe asserts
`Object.keys(row).sort()` equals `["detected","id","name"]` per row for the cases an annotation cannot
see (a spread row, a key written after the fact).

**Why the chooser needs that local belt.** `wireFixtureGuard.ts` discovers wire vocabulary from a
first-line `// TypeScript mirror of` marker (plus everything under `src/types/`). `data/harnessCatalog.ts`
carries no such marker, so `HarnessInfo` is not wire vocabulary to the guard and the chooser's catalog
fixtures are covered only by the annotation and the key assertion above. The guard's own note names the
live instances of this blind spot: `harnessCatalog.ts`, `submissionLifecycleClient.ts`, `changeset.ts`,
`files.ts`, `notes.ts`. Adding a marker line to one of those brings it under the guard; until then a
cockpit fixture for those clients is guarded per-file, not by the repo-wide rule.

The honest limit of all of it: `wire.ts` and `dashboard/src/fixtures/snapshot.json` are
**hand-maintained** — no generator exists anywhere in this repository, and no in-repo mechanism keeps
the two sides in step. These suites hold two of the chain's **three** links: `tsc -b` binds
`test/fixtures/wire.ts` to `types/projection.ts` (annotated bases, `Overrides<O, Node>` at every call
site, `test/wireFixtureGuard.test.ts` refusing the one-token opt-outs), and `test/contract.test.ts`
**measures the mirror against `snapshot.json`** in three TYPE-level directions (`mirror ⊇ served`,
`served ⊇ mirror`, `fixture ⊇ mirror`) plus runtime `VOCABULARIES` assertions for the string unions
`resolveJsonModule` widens to `string` — not a one-way `⊆`. **The third link is held by nothing:
`snapshot.json` ↔ `observer/projection.py` is maintained by hand.**

## 260731-EFA-L7 — Session-Cockpit Live Thinking

The session-cockpit route gained the L7 live-thinking coalescing (one stable `thinking` row per active turn, animated indicator, completion cleanup) and its interleaved acceptance pins in the conversation-timeline family. The file-size rail covers this route's TS/TSX under `dashboard/src`.

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 route impact: route body reviewed and updated for the supervisor -> agent-notifier rename (see the route-specific body section above); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 route impact (trace delta): recorded the live-thinking coalescing and file-size coverage for session-cockpit. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: added the L8 Change section (sessions-view split, parts modules, e2e app fixes). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 10 route-reference rows and 3 prose citation groups, including the contract-test and harness-response evidence; no route behavior claims were changed.
- 2026-08-01T14:05+02:00 — 260731-EFA-L4 curator (correction pass), body only. "Fixture Contract For
  This Route" closed with *"`fixture ⊆ mirror` is what these suites enforce; `mirror ⊆ server` is
  enforced by nothing"* — the outer two nodes of a four-node chain, which reads as though nothing
  measures the mirror against the snapshot. It does: `test/contract.test.ts` measures
  `types/projection.ts` against `fixtures/snapshot.json` in three TYPE-level directions
  (`mirror ⊇ served`, `served ⊇ mirror`, `fixture ⊇ mirror`; cit:(["mirror ⊇ served — the server grows", "served ⊇ mirror — the mirror declares", "fixture ⊇ mirror — THE ORACLE ITSELF"], dashboard/src/test/contract.test.ts:32-32; dashboard/src/test/contract.test.ts:40-40; dashboard/src/test/contract.test.ts:45-45)) plus runtime `VOCABULARIES`
  assertions cit:([`VOCABULARIES`], dashboard/src/test/contract.test.ts:268-283) for the string unions `resolveJsonModule` widens to `string`. The
  paragraph now names all three links and states the unheld one as **`snapshot.json` ↔
  `observer/projection.py`, by hand** rather than as "`mirror ⊆ server`" — one letter from
  "`mirror ⊆ served`", which *is* enforced. Also brought the no-generator claim to the strength the
  evidence carries: no in-repo generator **and no in-repo mechanism keeping the two sides in step**.
  Same correction applied to the 12:35 entry's restatement below. No suite claim, table row, or
  verification field changed.

- 2026-08-01T12:35+02:00 — 260731-EFA-L4 route impact (wire contracts and typed vocabularies): added
  the "Fixture Contract For This Route" section. No cockpit component changed — all seven changed
  sources are suites — so the body records the durable rule (a cockpit test builds wire nodes through
  `test/fixtures/wire.ts` / `conversationWire.ts`, never through a cast) and, separately, the three
  seeds whose SHAPE was corrected because it was a payload the server cannot send: the `undefined` /
  hand-built `ConversationCapabilities` on a required field, the two-of-thirteen-key `Analytics` in
  `SessionRail.test.tsx`, and the now-derived `page.totalItems`. Six of the seven changed only in
  helper/seed construction with no assertion text touched; I ran all seven (163 tests, green) and read
  each diff to confirm the `expect` lines are untouched. `LaunchFlow.test.tsx` is the exception and is
  recorded as a LOSS: its three `control: "starting"` keys are gone, so the surviving
  `not.toContain("adapter starting")` assertions can no longer fail and that guarantee is marked
  superseded here — verified `DetectedHarness` declares exactly `id`/`name`/`detected`
  cit:([`DetectedHarness`], mcp/src/agents_remember/serving/response_contract.py:355-360) on a `WireResponse` with `extra="forbid"`
  cit:([`WireResponse`], mcp/src/agents_remember/serving/response_contract.py:88-100), and
  that `HarnessInfo` mirrors the same three cit:([`HarnessInfo`], dashboard/src/data/harnessCatalog.ts:5-9). Recorded the replacement
  guarantee (typed `HARNESSES` annotation + the per-row `Object.keys` assertion) and the reason the
  chooser needs a local belt at all: `wireFixtureGuard.ts` discovers vocabulary from a first-line
  `// TypeScript mirror of` marker, `harnessCatalog.ts` has none, and the guard's own note lists it
  among five unmarked blind-spot modules. Stated the fixture chain's honest reach (both `wire.ts` and
  `snapshot.json` hand-maintained, no generator in this repository; the `snapshot.json` ↔
  `observer/projection.py` crossing held by nothing). (This bullet originally read "`mirror ⊆ server`
  enforced by nothing", which dropped the middle link; corrected in the 14:05 entry.) Added three
  two-cell `Repo-Internal References` rows, matching the existing two-column
  header. Verification metadata remains pinned until closeout stamps the commit.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: the conversation surface now
  hydrates only the effective selected child and retains exact roster identity across live updates,
  reload, and child focus. The broader cockpit layout and ownership model are unchanged.
  Verification metadata remains pinned until closeout.

- 2026-07-26T18:30+02:00 — 260718-CHATS-L7 curator: added the "Sub-Agent Lanes And Multiplexed
  Pending Interactions" section — the `ConversationSurface` roster/agent-lane focus cycling with
  roster-revalidated LRU-surviving focus, the library's indented server-keyed agent child rows plus
  verbatim `agentsNote`, and the multiplexed `InteractionBar` (one bar per pending interaction,
  adapter-bound agent badge, shared answer-channel routing) with attention previews naming who
  asks. No route composition, keep-alive, or authority model changed; verification metadata
  remains pre-commit and closeout re-stamps.

- 2026-07-24T13:17:17Z — Curator: corrected the route model for mounted conversation continuity,
  scroll restoration, focused action placement, retired StatusLine/rail footer, and structured
  interaction authority. The deleted StatusLine knowledge is retained by SessionsView/SessionStage
  and this route overview; verification metadata remains pre-commit.

- 2026-07-21T11:30+02:00 — No route impact: 260718-CHATS-L5F (half-time functional fixes,
  PASS-WITH-NOTES) touched one governed file — `SessionsView.tsx` gained the R9 (audit V5)
  focused-seat live-turn merge (`useActiveConversation` → `focusedLiveTurnWorking` →
  `{ liveTurnWorking: true }` on the focused row). The route's composition, keep-alive, focus, and
  authority model are unchanged: the state-preference rule itself lives in the `data/` route's
  `stateGrammar.ts` (`seatVisualState`, terminal/fault/blocked/wait guards first) and the change is
  recorded in the [SessionsView.tsx sidecar](SessionsView.tsx.md) and the data overview's Catalog
  And Session Identity section. Verification metadata advances with closeout stamping only.
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
