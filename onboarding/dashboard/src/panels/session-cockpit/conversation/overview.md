# dashboard/src/panels/session-cockpit/conversation/ — Structured Conversation Renderer Overview

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| sourceRoute            | `dashboard/src/panels/session-cockpit/conversation/`        |
| doc_type               | `route-local-overview`                                       |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview      | `../overview.md`                                             |

## Governing Overview

[session-cockpit overview](../overview.md) — this child owns the harness-neutral structured conversation
renderer while the session-cockpit overview owns the one-roof Chats composition. The projection it renders
is the reconstructable [data/conversation](../../../data/conversation/overview.md) store; the sibling
in-stage history browser is [conversation-library/](../conversation-library/overview.md).

## 260731-EFA-L8 Change

`ConversationTimeline.tsx` moved to `conversation-timeline/` with the machinery
split into `measurements.ts`, `timelinePremeasure.ts`, `timelineController.ts`,
`timelineControls.ts`, `timelineFeed.tsx`, `timelineScroll.ts`, `timelineFollow.ts`,
`timelineRestore.ts`, `timelineRefs.ts`, `unknownRun.tsx`, and `styles.ts`; the
former `renderer.test.tsx` split into seven behavior suites plus two shared
fixture modules. The timeline ARIA/scroll contracts (server-ordinal posinset,
honest setsize, trusted-input-cancellable restore) are unchanged.

## Purpose

`session-cockpit/conversation/` is the **one harness-neutral grammar** that renders a live structured
conversation (design §12.1, §14). It projects the reconstructable
`data/conversation` store into a single navigable `role="feed"` timeline of ruled blocks — streaming
Markdown, full-inline thinking, stable-ID plans/tools/diffs/interactions/results, required image labels,
and ambient telemetry — with visible harness identity and honest capability reasons, and **no
vendor-clone skins** (R3). It owns the exact-turn interrupt wiring (`useConversationControls`, surfaced
in `WorkingLine`) and the fail-loud reconnect surface. It renders only what the projection reconstructed;
it never writes conversation authority and never scrapes a vendor TUI.

## Route Model

- `ConversationSurface.tsx` — the page/stream shell: reconnect states, revision-keyed announcers that
  are SILENT on replay/hydration (`lastAppliedDelivery === "live"` strict, so fresh hydration/re-page
  never announces — F21), the global thinking toggle, the history-completeness note printing the
  actually-unsupported capability's reason (F13), and the ambient telemetry toolbar. It
  also owns the sub-agent FOCUS model (R7, reworked): `storedAgentFocus` → `deriveAgents` →
  `effectiveAgentFocus` (never applied blindly — a rehydrated projection without that agent honestly
  falls back to the parent), the uniform ArrowDown hijack from anywhere on the surface (feed article
  AND scroll viewport) moving DOM focus INTO the agents line as the primary path (the Claude Code
  sub-agent navigation model; the line owns Enter/menu, ArrowUp from the line returns focus to the
  timeline), ArrowLeft/ArrowRight cycling parent → agent 1 → … → agent N → parent as an additional
  path and Escape returning to the parent (editable/interactive targets
  own their keys), polite visibility-gated `viewing <label>` announcements, and
  `filterItemsForFocus` feeding the timeline (`totalItems`
  only when unfocused; a focused empty lane shows `no evidence from <label> yet`, never the welcome).
  The validated effective focus also drives selected-child history hydration after click, page
  load, or remount; stale focus sends no request. A typed local failure renders its detail and
  retry beside the agents area without changing the parent reconnect/stream state.
- `AgentsArea.tsx` — ONE compact sub-agents line above the timeline, always (R7, reworked): never one
  row per agent — the line carries the tone-colored count chip (`N agents · M running`, the status
  word never color-only, §14.2) plus, in an agent view, the `viewing <label>` note and the
  `← back to parent conversation` affordance (the surface's old focus bar is gone). The roster lives
  in a listbox menu opened from the line (click/Enter/Space/ArrowDown): one option per
  roster-evidenced agent (label, word-carrying status chip, terminal final-message preview),
  aria-activedescendant arrow navigation with wrap + scroll-into-view on every active change,
  Enter/click select (re-selecting the viewed agent just closes), Esc/backdrop/Tab dismiss, and
  honest recompute of a stale active id or an emptying roster. Projection-only with no optimistic
  rows and no polling; an empty roster is a static `0 agents` span. No transitions — a
  keyboard-driven open/focus change must not animate.
- `ConversationTimeline.tsx` — the single virtualized `role="feed"` (`aria-label="Conversation"`).
  `aria-posinset` is the server `globalOrdinal` (never the array index); `aria-setsize` is emitted only
  when the total is honestly known, else `total unknown` copy (R5). A focus-pinning range extractor pins
  BOTH the focused row and the default-tab (last) row so a tabbable article always exists even scrolled
  up (F18). Bottom-follow + a non-animated N-new button; anchor-preserving `Load older` explicit paging.
  Feed-scoped `onKeyDown` widget navigation (`[`/`]`/Home/End) with the completed exclusion list
  (`button,a,[contenteditable],.cm-editor`, input/textarea/select, active selection) and Home/End exempt
  inside labeled overflow regions (`[role="group"]`, `pre`) — the ARIA feed pattern, NOT document
  handlers (F14 accepted deviation). The exported `OPERATOR_SCROLL_KEYS` trusted-input set deliberately
  OMITS ArrowDown (the surface hijacks it into the agents line; PageDown/`]`/wheel stay scroll paths).
  It consumes `collapse.ts` to fold unknown-vendor runs.
- `ConversationItemView.tsx` — the pure kind dispatcher + stable accessible-name helper routing each
  `ConversationItem` to its component.
- Item/block components (one harness-neutral grammar): `MessageItem` (operator/assistant/user/system;
  required-alt images as a labeled reference with NO `<img>` fetch — F11; assistant clamp slicing to the
  logical line threshold so `+N lines` is exactly what is hidden — F12), `ThinkingItem` (full-inline dim,
  never clamped, obeys the hide-thinking toggle), `ToolItem` (stable-ID verb phrase + phase accent,
  in-place recompose, output clamp, diff routing), `DiffBlock` (per-file diff, full-to-threshold clamp
  with exact hidden count, labeled scroll region), `InteractionItem` (historical prompt + answer,
  NON-live — InteractionBar owns the live gate channel; a bound agent ref badges WHO is asking in a
  cyan uppercase badge), `TurnResultItem`
  (result/error/interrupt/notice/unknown-vendor as labeled evidence), `MarkdownBlock` (streaming-safe
  memoized react-markdown; code in its own labeled scroll region).
- `primitives.tsx` — `ClampButton` (a real `<button aria-expanded aria-controls>`; exact `+N` only when
  known from source lines), `SourceBadge` (only when origin changes interpretation), `CapabilityReason`
  (the exact server reason).
- `AmbientTelemetry.tsx` — the evidence-bound telemetry toolbar consuming the previously-orphaned
  `fetchConversationTelemetry` (F3): absent-not-zero chips (A2), quiet italic `stale` freshness (A4), an
  evidence tooltip; it drives `format.ts` `freshnessTone`/`joinChips`/`humanizeAge` (F19).
- `collapse.ts` — the pure grouping helper: runs of ≥3 identical-summary unknown-vendor items collapse
  to one de-emphasized expandable row; identity is never mutated; the first member's ordinal is the
  posinset (F10).
- `ConversationReconnect.tsx` — the fail-loud reconnect/gap/projection-failed banner with retry +
  show-diagnostics, rendering `${copy} — ${reason}` from the typed `ConversationRouteError` (F15); never a
  silent PTY fallback.
- `TerminalDiagnosticsDrawer.tsx` — the DEFAULT-OFF, inert-when-closed drawer (`inert` + `aria-hidden` +
  zero children/no PTY mounted when closed — R2/R7/§14.1); framed inset vendor-chrome (A7); hosts the
  controlled runner PTY READ-ONLY through `PtySurface`'s `readOnly` prop (§12.6).
- `useConversationControls.ts` — the exact-turn interrupt hook (§9.5), documented in the Renderer Rulings
  Register below.

## FB7 terminal-surface identity

The renderer's grammar was unchanged; its STYLING became a terminal well instead of a generic web panel
(spec home: the leaf visual-audit `## FB7`, derived from Toad `main.tcss` + the Claude Code / Codex TUIs).
Cross-file: `ConversationTimeline` viewport = `background: well` (the `#070b0f` token) + grid border + a
centered `100ch` content column with the page bg as gutter (FB7.1); item rhythm is line-grid blank lines,
no per-article hairline (FB7.3); item chrome is gutter grammar — `ToolItem` `●` phase dot + lowercase
phase word + left-rule output wash, `TurnResultItem` `· turn complete` flow line, `ThinkingItem` `✻
thinking`, `primitives` `ClampButton` de-boxed lowercase underline, the collapsed unknown-vendor run one
dim mono line with the honest `same summary` copy (FB7.4/R12). `MarkdownBlock` prose uses `break-word` +
inline-code `nowrap` (V10) — effective only under the app-root `word-break: normal` override (RV-1,
`index.css`). `ConversationSurface` renders the history/live capability as a short CUE (state word visible,
full reason in the hover `title` — R11), not the old always-visible reason paragraph. The composed litmus
(a settled turn over the well, indistinguishable in grammar from an adjacent vendor TUI) passed on live
content; item-level styling is not mountable in the bench (mock returns `structured surface unavailable`),
so it holds by unit tests + the reviewer's live R13 pass.

## Invariants And Boundaries

- **One grammar, no vendor skins (R3).** Every item/block renders through this shared grammar; unknown
  vendor events are preserved as labeled evidence, never dropped and never re-skinned as vendor chrome.
- **One honest `role="feed"` (R5).** Exactly one feed; `aria-posinset` is the server ordinal; `aria-setsize`
  is omitted with `total unknown` copy when the total is not honestly known; announcers are dedicated
  polite/assertive regions OUTSIDE the feed and stay silent on replay/hydration.
- **Inert closed trees.** The diagnostics drawer and any hidden stage are `inert`+`aria-hidden` and mount
  no PTY when closed; a projector failure renders the fail-loud banner, never a silent PTY fallback.
- **Honest overflow and clamps.** Clamp buttons are real `<button aria-expanded>` with an exact `+N`
  only when computed from source lines; code/diff live in labeled scroll regions; Home/End scroll those
  regions rather than navigating the feed.
- **Honest tooltips and keymap-derived aria (F24/F25).** The interrupt control never surfaces the
  known-stale L1 capability reason; its `aria-keyshortcuts` is derived from the effective keymap, so a
  rebind stays truthful to assistive technology.
- **The renderer never authors conversation authority.** It reads the projection; interrupt dispatch
  goes through the typed control client; the live interaction/queue/submit authorities are consumed, not
  duplicated (InteractionBar/QueuePreview/SessionComposer stay their own owners).
- **Selected-child history is local and retryable.** The surface triggers hydration only from the
  validated effective focus and renders only the store's child-scoped outcome; it never turns a
  child route failure into parent `projection-failed`.

## Hot Path Summary

1. `ChatsStageBody` mounts `ConversationSurface` for a controlled seat; the surface reads the
   `data/conversation` projection through `useActiveConversation`.
2. `ConversationTimeline` virtualizes `orderedItems`, stamps server-ordinal ARIA, folds unknown-vendor
   runs (`collapse.ts`), and pins tabbable rows; each item routes through `ConversationItemView` to its
   grammar component.
3. `AmbientTelemetry` renders evidence-bound metrics absent-not-zero; `ConversationReconnect` surfaces
   any typed fault fail-loud.
4. `useConversationControls` resolves the working turn id from item evidence and gates the interrupt,
   which `WorkingLine` renders and the `conversation.stop` chord/palette dispatches.
5. `ConversationSurface` hydrates the effective selected child once per runtime and renders a local
   retry state when that acquisition fails; the parent feed remains mounted and live.

## Renderer Rulings Register (durable renderer rulings a follow-on renderer change must carry)

- **Interrupt gating is attempt-and-reflect on the L3 routes' evidence, never the stale L1 page view.** No GET exposes the true control capability and the active page's
  `capabilities.controls` is the KNOWN-STALE L1 `unverified` view, so `useConversationControls` enables
  the stop on a working+resolvable turn unless the capability is a hard `unavailable`, and reflects the
  server's typed refusal reactively (a refusal disables that turn until the turn changes — F5). A clean
  proactive gate awaits a control-capabilities GET or an L1-view refresh.
- **Hosted-codex status carries no `turn.turnId` during working turns (R1).** `resolveWorkingTurnId`
  correlates the id from projector item evidence (status turn id → newest streaming/pending item
  `turnId` → null with the honest reason `turn identity unavailable on this wire`); pi supplies the AR
  operation id per ruling 3. A status fix populating `turn.turnId` on this topology invalidates the
  correlation path.
- **The known-stale L1 `unverified` reason must NEVER surface as control copy (F24 / R4).** An
  enabled stop carries no reason (WorkingLine shows an honest action tooltip); the not-working/catalog-lag
  placeholder falls back to the honest earlier `STOP_TURN_DISABLED_REASON` constant. That constant's stale
  "no cancel-turn route exists yet" wording predates the L3 control routes and should be RETIRED with the
  catalog-lag turn-state reconciliation (R4) — the catalog seat turn-state lags the projection in both directions,
  so the chord/palette can be live while the button is absent.
- **`aria-keyshortcuts` is derived from the effective keymap, never hardcoded (F25).** `ariaKeyshortcuts(
  bindingFor(effectiveKeymap, "conversation.stop"))` keeps the AT advertisement truthful across a rebind
  through the `cockpit.sessions.keymap.v1` seam.
- **Wrapping flex containers defeat height containment (R5 / F23).** A `flex-wrap:wrap` container sizes
  each line to content, so an interior `overflow:auto` never engages and in-stage affordances become
  pointer-unreachable. The reliable idiom is single-line (`nowrap`) flex + `min-height:0` columns +
  per-column interior scrollers + `@container` stacking. (This bites the sibling `conversation-library/`
  surface; recorded here because it is the renderer-wide layout lesson.)
- **Virtualization DOM-boundedness at 10k items and the E1/E2 environmental faults — DELIVERED
  (previously an open ruling).** The 10k tool-heavy DOM/interaction baseline + axe tripwire now
  lives in `renderer.test.tsx` (mounted rows bounded `< 80` AND `< total/100`; recorded 10 rows /
  ~42–55 ms; the ms is a jsdom tripwire, a real-layout supersede is a second-half item). E1
  (hosted-interactions vendor-correlation 500) is quarantined per row in `terminal_liveness.py` — the
  orphan `vendorCorrelationId` is the NORMAL steady state of cockpit-driven hosted chats — and E2 (L1
  unknown-input provenance 500) is closed by the store's input-authority pin. NEW L5 finding **F1**:
  on the hosted codex `+ Chat` topology the live and `thread/read` channels use disjoint id namespaces,
  so every settled turn was projected TWICE — a resolved live twin beside an authority-downgraded
  `unknown-input`/`native-history` twin in THIS feed; the projector's live-settled-natives filter now
  suppresses the native twin (proven once-only on the real codex wire). F3 (completion-correlation
  contract) and the substrate IPC flake register are master-exit carries.

## Child Route Onboarding Map

No deeper child route exists below `conversation/`; each source has a one-to-one file card and this
overview is their governing pillar.

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Page/stream shell + sub-agent focus model | [ConversationSurface.tsx](ConversationSurface.tsx.md) |
| Sub-agents strip + focus suites | [AgentsArea.tsx](AgentsArea.tsx.md) · [AgentsArea.test.tsx](AgentsArea.test.tsx.md) · [ConversationAgentFocus.test.tsx](ConversationAgentFocus.test.tsx.md) |
| Virtualized feed timeline | [ConversationTimeline.tsx](ConversationTimeline.tsx.md) |
| Kind dispatcher | [ConversationItemView.tsx](ConversationItemView.tsx.md) |
| Message/thinking/tool/diff items | [MessageItem.tsx](MessageItem.tsx.md) · [ThinkingItem.tsx](ThinkingItem.tsx.md) · [ToolItem.tsx](ToolItem.tsx.md) · [DiffBlock.tsx](DiffBlock.tsx.md) |
| Interaction/result items | [InteractionItem.tsx](InteractionItem.tsx.md) · [InteractionItem.test.tsx](InteractionItem.test.tsx.md) · [TurnResultItem.tsx](TurnResultItem.tsx.md) |
| Markdown + primitives | [MarkdownBlock.tsx](MarkdownBlock.tsx.md) · [primitives.tsx](primitives.tsx.md) |
| Ambient telemetry + run collapse | [AmbientTelemetry.tsx](AmbientTelemetry.tsx.md) · [collapse.ts](collapse.ts.md) · [collapse.test.ts](collapse.test.ts.md) |
| Reconnect + diagnostics drawer | [ConversationReconnect.tsx](ConversationReconnect.tsx.md) · [TerminalDiagnosticsDrawer.tsx](TerminalDiagnosticsDrawer.tsx.md) |
| Interrupt hook | [useConversationControls.ts](useConversationControls.ts.md) · [useConversationControls.test.tsx](useConversationControls.test.tsx.md) |
| Renderer + a11y suite | [renderer.test.tsx](renderer.test.tsx.md) |

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This route relies on its direct agents-remember source/tests and the reviewed
task/worker/verdict evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for the structured renderer. | — | — |

## Cross-Repo References

The renderer composes repository-local components over this package's own conversation contracts; no
cross-repository implementation source governs it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reconstructable projection this renderer reads. | `# dashboard/src/data/conversation/ — Reconstructable Active-Conversation Projection Overview` | onboarding/dashboard/src/data/conversation/overview.md:1-300 |
| The sibling in-stage history browser. | `# dashboard/src/panels/session-cockpit/conversation-library/ — In-Stage History Browser Overview` | onboarding/dashboard/src/panels/session-cockpit/conversation-library/overview.md:1-173 |
| The one-roof composition that mounts this renderer. | `# dashboard/src/panels/session-cockpit/ — Canonical Chats Cockpit Overview` | onboarding/dashboard/src/panels/session-cockpit/overview.md:1-506 |
| The interrupt chord/aria-derivation the hook consumes. | `# dashboard/src/data/keymap/ — Keyboard Zone Contract Overview` | onboarding/dashboard/src/data/keymap/overview.md:1-154 |
| The control routes whose evidence gates interrupt + the renderer-facing rulings. | `# Structured Conversation Control Route Overview` | onboarding/mcp/src/agents_remember/serving/conversation/control/overview.md:1-433 |
| The conversation-grammar fixture builders these suites seed from, and the three sanctioned brand mints. | `pageCursor`; `eventCursor`; `libraryConversationKey`; `conversationCapabilities` | dashboard/src/test/fixtures/conversationWire.ts:53-55; dashboard/src/test/fixtures/conversationWire.ts:58-60; dashboard/src/test/fixtures/conversationWire.ts:63-65; dashboard/src/test/fixtures/conversationWire.ts:103-146 |
| The registry that records those three mints as the only permitted casts, each with its reason. | `SANCTIONED_WIRE_SITES` | dashboard/src/test/wireFixtureGuard.test.ts:51-188 |

## Empty-Well Honesty And Scroll-Restoration Route State

The renderer keeps its timeline well mounted even while empty, uses process-state evidence for the
welcome state, and owns a robust scroll-memory contract for a Cockpit `display:none` view switch.
Restores wait for valid geometry, ignore collapse echoes, follow the current end only when the reader
left at bottom, and yield to trusted user input. A live SSE stream supplies a compact working cue;
the exact-turn Stop control intentionally remains beside Send in the composer.

## Selected-Child History Renderer State

A valid persisted effective focus hydrates after page load/remount without requiring a click; a
stale focus falls back to parent and performs no I/O. The focused-child error strip shows the
server/client detail and retry action. Runtime/store singleflight keeps the effect exactly once,
and retry affects only the selected child.

## 260731-EFA-L4 Fixture Contract For This Renderer

No renderer component changed. The two changed sources are suites, and both were seeding a capability
tree the server cannot produce — which matters here more than in most routes, because the Renderer
Rulings Register's interrupt gate is an argument ABOUT capability evidence.

- **`ConversationCapabilities` is a required field with a full tree.** The mirror declares four groups
  (`live` · `history` · `controls` · `telemetry`) and twenty-three capability leaves, and the server
  fills every one. `ConversationAgentFocus.test.tsx` was seeding `capabilities: {} as ConversationCapabilities`
  — an empty tree — and `useConversationControls.test.tsx` a local
  `{ controls: { interrupt } } as unknown as ConversationCapabilities` — one leaf and three absent
  groups. Both now build through `test/fixtures/conversationWire.ts` (`conversationPage()` and
  `capabilitiesWithInterrupt(state)`), so the tree under assertion is one the L1 view can actually send.
- **The interrupt gate is unmoved by that.** `useConversationControls` reads exactly
  `projection?.capabilities?.controls.interrupt` and nothing else, so filling the other twenty-two
  leaves changes no decision. What it removes is a stub that carried only the field under test — the
  shape that lets a gate look proven when it has never seen a real tree.
- **Pages built by the builder carry `page.totalItems`,** derived from the item array rather than
  omitted. That is the field the timeline's honest-`aria-setsize` rule (R5) turns on, so a renderer test
  seeding a page through `conversationPage()` is now in the "total honestly known" branch by default and
  must say so explicitly if it wants the `total unknown` copy.
- **`conversationItem()` defaults `turnId: "t1"`.** `ConversationAgentFocus.test.tsx` passes
  `turnId: undefined` on purpose to keep its items turn-less; `ConversationItem.turnId` is optional in
  the mirror and `exactOptionalPropertyTypes` is off, so the explicit `undefined` is admitted. Reuse the
  builder here knowing the default, not the previous hand-written shape.
- **The opaque tokens have exactly three mints.** `ActivePageCursor`, `ActiveEventCursor` and
  `LibraryConversationKey` are `string & { __brand }` — compile-time only, no structure to get wrong —
  so the inline `"evt-0" as ActiveEventCursor` casts collapse into `pageCursor()` / `eventCursor()` /
  `libraryConversationKey()`, each registered as a sanctioned cast site in `wireFixtureGuard.test.ts`
  with its reason. Registration is what makes them the only three rather than the first three: the
  registry counts occurrences, so a fourth cast in a listed file fails.

## 260731-EFA-L7 — Live-Thinking Coalescing

The conversation timeline now coalesces repeated empty/in-progress reasoning into ONE stable live `thinking` row per active turn identity: `collapse.ts`'s `groupDisplayRows` delegates to extracted helpers (`liveKeyFor`, `handleLiveOpen`, `handleLiveUpdate`, `handleLiveFinalize`, `unknownRunFor`) with row-object references and `rows.indexOf` finalize (no index bookkeeping); `ThinkingItem` gained the animated live indicator (shared `pulseSlow`, frozen by effects=off); `timelineController.ts` and `timelineFeed.tsx` carry the wiring in the split conversation-timeline. The interleaved R15/R17 acceptance pins live in `conversation-timeline/liveThinking.test.tsx` and `collapse.test.ts` (at most one live indicator, zero diff-update unknown rows, unknown evidence preserved).

## 260713-TES Master Gate — Hermetic Scroll-Memory Timers

The two split scroll-memory suites share timer ownership through
`conversation-timeline/scrollMemory.test-utils.tsx`: every case starts with fake timers, React
renders are unmounted while those timers are still controlled, pending TanStack Virtualizer
scroll-debounce callbacks are discarded, and only then does the suite restore real timers. The
explicit fake-timer cases in `scrollMemory1.test.tsx` and `scrollMemory2.test.tsx` perform the same
ordering in their `finally` blocks. This is a test-environment contract, not a production timeline
change: it prevents a delayed Virtualizer `onChange` from reaching React after jsdom has destroyed
`window`, which previously made an otherwise 1,551-passing suite fail nondeterministically at
process teardown.

L23 extends that same helper-owned teardown contract to `intentLock.test.tsx`. Its ten intent-lock
assertions no longer restore real timers per test; the shared fixture keeps timer ownership through
RTL cleanup and clears the Virtualizer debounce before jsdom teardown. The `msg` builder stays local
because streamed-row content is still suite-specific.

## 260815-DAG Master Full-Gate Repair Route Impact

`ConversationSurface.test.tsx` gained an async `afterEach` that flushes the timeline virtualizer's scroll debounce before jsdom teardown.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: ConversationSurface.test.tsx flushes the timeline virtualizer debounce in an async `afterEach`. Verified at code commit e5cb139f.

- 2026-08-13T07:53+02:00 — 260731-EFA-L23 super-line reconciliation: re-reviewed this card and its Repo-Internal citation targets after absorbing the super-integration memory line. Retained claims remain supported by the current tree. Verification is pinned to real code HEAD `1580f92715ff93c988f9a15439ad9bec60ef4c5d`; the new-line memory mapping remains closeout-owned.

- 2026-08-12T17:04+02:00 — 260731-EFA-L23 dashboard-gate route review: moved the intent-lock suite
  onto the existing hermetic scroll-memory geometry/timer helper, eliminating the post-jsdom
  Virtualizer debounce race without changing timeline production behavior. Focused Vitest is 10/10
  with no unhandled error; verification provenance remains closeout-owned.

- 2026-08-09T22:22+02:00 — 260713-TES master integration route impact: the shared
  conversation-timeline scroll-memory fixture now owns fake timers and tears down renders plus
  pending Virtualizer debounces before restoring real time. Both split suites preserve that order,
  eliminating the nondeterministic post-jsdom React callback while leaving production behavior
  unchanged.

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 route impact (trace delta): recorded the live-thinking coalescing change set and its acceptance pins. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: added the L8 Change section (conversation-timeline split). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:40:00+02:00 — W3-B01 curator: curated 7 Repo-Internal table citations (5 memory-overview and 2 code-source references) with exact headings, builder identifiers, and registry anchor. Verification metadata remains unchanged for closeout.
- 2026-08-01T13:05+02:00 — 260731-EFA-L4 route impact (wire contracts and typed vocabularies): added
  the "Fixture Contract For This Renderer" section. No renderer component changed; both changed sources
  are suites whose capability seeds were shapes the server cannot send — an empty
  `{} as ConversationCapabilities` in `ConversationAgentFocus.test.tsx` and a one-leaf
  `as unknown as ConversationCapabilities` in `useConversationControls.test.tsx` — now built by
  `conversationPage()` / `capabilitiesWithInterrupt()`. Checked the thing that would have made that
  consequential for the Renderer Rulings Register: `useConversationControls.ts` L107 reads exactly
  `projection?.capabilities?.controls.interrupt` and no other leaf, so the fuller tree moves no gate;
  both suites run green. Recorded three builder defaults a follow-on renderer test must know rather than
  rediscover — `conversationPage()` supplies `page.totalItems` (the field R5's honest-`aria-setsize`
  rule turns on), `conversationItem()` defaults `turnId: "t1"` (which is why the focus suite passes an
  explicit `turnId: undefined`, admitted because `ConversationItem.turnId` is optional and
  `exactOptionalPropertyTypes` is off), and the four-group / twenty-three-leaf tree the mirror declares.
  Verified the three brand mints (`ActivePageCursor`/`ActiveEventCursor`/`LibraryConversationKey`,
  `data/conversation/types.ts` L26-L27 for the first two) are registered as sanctioned cast sites in
  `test/wireFixtureGuard.test.ts` L165-L176 rather than merely tolerated. Added two two-cell
  `Repo-Internal References` rows in the existing two-column shape. Verification metadata remains pinned
  until closeout.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented effective-focus-driven
  hydration, valid persisted versus stale focus, child-local visible failure/retry, and unchanged
  parent feed/reconnect authority. Verification metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the sub-agent navigation rework in
  the Route Model — `AgentsArea` is ONE compact line always (per-agent rows and the narrow-collapse
  ResizeObserver deleted) with the roster in a new listbox menu (arrow navigation with wrap +
  scroll-into-view, Enter/click select, Esc/backdrop dismiss), the surface owns the uniform
  ArrowDown hijack INTO the line as the primary path (ArrowLeft/ArrowRight kept as an additional
  path; the surface focus bar deleted — the line carries the viewing note + back-to-parent), and
  the timeline's exported `OPERATOR_SCROLL_KEYS` drops ArrowDown from the scroll-key contract.
  Verification stays pinned (remediation uncommitted); closeout re-stamps.
- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the R7 sub-agent focus UX — the
  `AgentsArea` strip (roster-evidenced rows, word-carrying status chips, narrow/empty summary
  collapse, aria-current focus toggle), the surface-owned focus model (ArrowLeft/ArrowRight/Escape
  keys with interactive-target exclusion, effective-focus honesty against the live roster, timeline
  filtering with `totalItems` withheld while focused, the back-to-parent focus bar and the
  focused-lane empty note), and the `InteractionItem` asking-agent badge. Added `AgentsArea.tsx`,
  `AgentsArea.test.tsx`, `ConversationAgentFocus.test.tsx`, and `InteractionItem.test.tsx` to the
  file onboarding map. The L7 source is uncommitted; lastVerified* stays at the leaf base and
  closeout re-stamps verification.
- 2026-07-24T13:17:17Z — Curator: documented current empty-well honesty, scroll restoration, latest
  navigation, SSE working cue, and composer-owned stop behavior. Verification metadata remains
  pre-commit.

- 2026-07-21T12:00+02:00 — 260718-CHATS-L5P curator: added the FB7 terminal-surface identity section —
  the well (FB7.1), line-grid rhythm (FB7.3), gutter grammar across the item components (FB7.4/R12),
  V10 whole-word wrapping (dependent on the RV-1 root override), and the R11 capability CUE. Styling
  only; the harness-neutral grammar, feed ARIA, and virtualization are unchanged. Spec home is the leaf
  visual-audit `## FB7`. Verification re-pinned to this leaf's base (`352d5cd`) while the polish candidate
  is uncommitted; closeout owns candidate stamping.
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: updated the L5-Facing Register's
  virtualization/E1/E2 bullet to DELIVERED — the 10k DOM/interaction baseline + axe tripwire landed in
  `renderer.test.tsx` (its file card refreshed), E1 is quarantined and E2 authority-pinned in the
  backend, and the NEW F1 disjoint-id-namespace twin (which rendered as a duplicate `unknown-input`
  native-history row in this feed) is now suppressed in the projector, proven once-only on the real
  codex wire. No renderer component source changed this leaf beyond the added `renderer.test.tsx`
  baseline. Verification stays pinned at the leaf base (`9e6c15d`) until closeout stamps the candidate
  commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the governing pillar for the harness-neutral
  structured conversation renderer — the single honest `role="feed"` (server-ordinal posinset, honest
  setsize), the one block grammar (no vendor skins), the replay-silent announcers, the inert default-off
  diagnostics drawer, and the L5-Facing Register (attempt-and-reflect interrupt gating on L3 evidence,
  hosted-codex turn-id correlation, the never-surface-stale-L1-reason and keymap-derived aria rules, the
  wrapping-flex containment lesson, and the virtualization/E1/E2 L5 hardening). Verification is pinned to
  the leaf base (`0be0099`) because the new source route is uncommitted; closeout owns its first source
  stamp.
