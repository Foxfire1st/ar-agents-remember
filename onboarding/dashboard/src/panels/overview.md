# dashboard/src/panels/ — Cockpit Panels Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/`                          |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Current Structural Panel Contract

Panels receive real task-document hierarchy and current occupant facts from the data route. RailChat
and the session cockpit select structural document+role seats; task assignment posts that identity,
and replacement changes only the occupant. No panel derives hierarchy from spawn ancestry or treats
a lifecycle/session id as the task address.

## 260713-TES-L5F2 Change

The shared `SessionComposer` and contextual `RailChat` regression suites now prove that composer
answer mode does not require a lifecycle or gate. Both follow the same session-owned protocol as
the canonical cockpit: read the hosted session's bridge epoch, POST the answer to that exact
session's `interaction-response` route, lock duplicate sends, and never route an adapter answer
through reliable `/submit`.

## 260731-EFA-L8 Split Layout

### 260713-TES-L1 Reviewed — Heartbeat Wording In Session Cockpit

Route body reviewed for the supervisor → agent-notifier rename: the session-cockpit heartbeat UI
(`BusPane`, `SeatInspector`, `SessionRail`, `sessionRailParts`, sessions-view) now uses
`AgentNotifierHeartbeat` / `agentNotifierHeartbeat` and "Agent notifier heartbeat" labels. No
panel-shape or layout change; per-file detail lives in the session-cockpit overview and the file
sidecars.

The frontend-rail size remediation (R4/R5) re-shaped this route: `DetailPanel.tsx`
→ `detail-panel/` (canonical entry + `state.ts`, `model.ts`, `lifecycleBody.tsx`,
`taskReader.tsx`, `taskDocPanels.tsx`, `changeSetBar.tsx`, `styles.ts`, seven
behavior-split test files + `test-utils.tsx`); `LifecycleList.tsx` →
`lifecycle-list/` (four behavior-split test files + `test-utils.tsx`);
`SessionsView.tsx` → `session-cockpit/sessions-view/` (controller/body/palette/
styles + six test files); `ConversationTimeline.tsx` →
`session-cockpit/conversation/conversation-timeline/` (12 machinery modules +
seven test files); `engineRoomStyles.ts` → engine-room style domains + `styles.ts`
barrel; `EnclosureCanvas.tsx` → eight engine-room sibling modules. Shared panels
also gained parts/styles modules (`sessionComposer*`, `terminalSession.ts`,
`interactionParts*`, `launchFlowParts*`, `sessionRailParts*`, `stageLayers.tsx`,
`conversationSurfaceParts*`, `chatsStageStyles.ts`). The naming rule
(kebab-case folder, one canonical entry, short responsibility-based siblings) is
now a repository guideline. Behavior is preserved.

## Purpose

### 260731-EFA-L23 Route Delta

L23 makes Hangar expose optional durable lifecycle-operation kind, status, phase, and
`currentCommand` as one compact enclosure badge without inventing an operation when none is
projected. The live command stays single-line and width-responsive through CSS ellipsis, with its
complete value retained in `title`; it is not truncated once by character count.

TES-L6 changes the command-seat panel boundary from one global spine to sprint-qualified groups.
`FlowTab` consumes bound fixtures, while the session cockpit delegates group derivation to the data
model and renders legacy unbound seats only as migration state.

This route contains reusable cockpit panels plus focused child routes. Its strategic UI owners are:

- [session-cockpit](session-cockpit/overview.md) — the sole full-page Chats destination.
- [engine-room](engine-room/overview.md) — the Engine Room process visualization.
- LifecycleList.tsx + DetailPanel.tsx — Operations task navigation and reader.
- RailChat.tsx — contextual task-side chat, not a second full-page chat product.
- Terminal.tsx, SessionComposer.tsx, and HighlightComposer.tsx — shared interactive surfaces
  consumed by the canonical cockpit.

Detailed session state, submission, withdrawal, cleanup, and authority behavior belongs in the
[data overview](../data/overview.md). This parent intentionally keeps only composition boundaries.

## FEUI-L9R Recovery Composition

The shared `Terminal` panel preserves its mounted xterm and scrollback while performing at most one
explicit socket reattach for each changed serving boot. The canonical Chats chooser owns a fixed,
bounded viewport dialog with explicit loading/empty/timeout/error states and operator Retry; it does
not render a pre-session adapter process or create a second catalog store. On an empty narrow
cockpit, responsive layout keeps the sole chat-creation entrance available.

## FEUI-MX-FIX-2 Open Failure Composition

Shared callers do not infer session creation from a completed request. `HighlightComposer.tsx`
shows a failed create before readiness or submit and sends no selected context. `RailChat.tsx`
shows the same typed failure and withholds contextual delivery. Both consume the accepted-row result
from the data route; neither writes a private row, focuses a requested id, or retries through paste.

## Route Model

### Canonical Chats

FEUI-L8 retires the legacy Chats.tsx and SessionList.tsx path. CockpitShell now exposes one
Chats destination backed by the persistent session-cockpit layer; Operations remains the default.
The right inspector is closed by default and toggleable. The replacement duty and deletion map lives
in the [session-cockpit overview](session-cockpit/overview.md).

- SessionRail + data/railModel replace SessionList + data/sessionGroups.
- ChatContextBar carries launch, task/leaf context, local lifecycle routing, and authoritative leaf
  attach/move duties.
- SessionsView owns smart focus, live action routing, persistent PTY composition, key/palette zones,
  and the optional inspector.
- LandedCleanupNotice and EndedSessionState retain unavailable cleanup and ended-row truth without
  pretending an empty PTY is a live conversation.

### Shared Interactive Panels

- Terminal.tsx is the xterm/socket wrapper. Since 260718-CHATS-L4 a controlled session's runner
  line-log appears only inside the read-only terminal-diagnostics drawer (the structured
  `ConversationSurface` is the controlled-session default); legacy raw sessions still host a vendor
  TUI. Terminal.tsx is not the structured conversation renderer — that lives in the
  [session-cockpit](session-cockpit/overview.md) `conversation/` grammar.
- SessionComposer.tsx is the shared CodeMirror reliable-submit surface. It consumes effective
  keymap/profile state and uses authoritative withdrawal for pop-back.
- HighlightComposer.tsx sends a selected context package only after acceptance; selection and target
  choice cannot move active route/focus on rejection or ambiguity. Its pre-projection task-document
  fallback is a stable module-level snapshot, so the always-mounted composer cannot force React into
  an external-store update loop while analytics is still absent.
- RailChat.tsx renders contextual task-side chat under the same registry, not a competing destination.

### Operations And Other Routes

Operations, Detail, Engine Room, notes reader, file viewer, changeset, and lifecycle-design retain
their existing responsibilities. Focused child overviews and one-to-one file cards are authoritative;
the Chats refactor does not move those routes.

## Invariants And Boundaries

- Exactly one full-page Chats destination; no legacy Chats layer and no Sessions navigation item.
- Operations is initial. The Chats inspector is supplementary, default closed, and toggleable.
- Shared panels consume canonical data stores and authority clients; they do not create private
  session catalogs, conversation indexes, or submission ledgers. The 260718-CHATS-L4 structured
  surface holds only a reconstructable projection — no durable browser conversation index.
- Create-dependent panel actions proceed only after the shared opener returns an accepted server
  row; visible failure precedes readiness, focus, and delivery.
- The structured conversation surface (260718-CHATS-L4) is the controlled-session default and
  consumes adapter-normalized history/index/resume from the landed L1/L2/L3 contracts; the PTY
  line-log is now the read-only diagnostics drawer + legacy-raw body, not the message renderer.
- Reliable submit, withdrawal, interaction answers, bus replies, and control actions remain separate
  channels and never fall back to shared paste.
- No Domain Documentation source is configured; direct same-repository source, tests, reviewed task
  evidence, and recovered project history govern this route.

## Child Route Onboarding Map

| Child route | Governing overview |
| --- | --- |
| `session-cockpit/` | [Canonical Chats](session-cockpit/overview.md) |
| `engine-room/` | [Engine Room](engine-room/overview.md) |
| `file-viewer/` | [File Viewer](file-viewer/overview.md) |
| `changeset/` | [Change-Set Viewer](changeset/overview.md) |
| `notes-reader/` | [Notes Reader](notes-reader/overview.md) |

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured. This compact
parent was refreshed from its repository-local child overviews, source/tests, and reviewed L8 record.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for panels. | — | — |

## Cross-Repo References

No cross-repository implementation source governs the panels route; all production imports resolve
inside agents-remember.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `Cockpit` view map contains the declared view map. | `VIEWS` | dashboard/src/cockpit/Cockpit.tsx:72-80 |
| The Chats cockpit keeps its `SessionsView` mounted and toggles its display rather than unmounting it. | "The sole product-facing Chats cockpit is never unmounted"; "<SessionsView" | dashboard/src/cockpit/Cockpit.tsx:775-781 |
| The persistent Chats layer renders `SessionsView` with active, selected lifecycle/leaf, task-document, and context props. | "<SessionsView"; "active={view === \"chats\" && !takeover}"; "selectedLeafKey={viewedLeafKey}" | dashboard/src/cockpit/Cockpit.tsx:781-786 |
| Dashboard state authority is held by `DashboardState`, `dashboardStore`, and `applySnapshot`. | `DashboardState`; `dashboardStore`; `applySnapshot` | dashboard/src/data/store.ts:19-50; dashboard/src/data/store.ts:225-347 |
| The production application route is owned by `App`. | `App` | dashboard/src/App.tsx:10-19 |
| The production route returns `Cockpit`. | `Cockpit` | dashboard/src/cockpit/Cockpit.tsx:359-383 |
| `CockpitShell` defaults `initialView="operations"`. | `initialView` | dashboard/src/cockpit/Cockpit.tsx:858-858 |
| The terminal panel owns the shared terminal surface. | `Terminal` | dashboard/src/panels/Terminal.tsx:110-202 |
| The shared composer surface is implemented by `SessionComposer`. | `SessionComposer` | dashboard/src/panels/SessionComposer.tsx:57-117 |
| Selection-send behavior builds context and submits it to a selected or routed target, committing only on accepted or queued delivery. | `HighlightComposerImpl`; `submitTo`; `successful` | dashboard/src/panels/HighlightComposer.tsx:710-780; dashboard/src/panels/HighlightComposer.tsx:244-696; dashboard/src/panels/HighlightComposer.tsx:238-238 |
| Contextual task-side chat builds a leaf context package and resolves the current occupant from structural task identity. | `buildLeafContextPackage`; `RailChatImpl`; `findSessionForTask` | dashboard/src/data/sessions.ts:564-576; dashboard/src/panels/RailChat.tsx:255-289; dashboard/src/panels/RailChat.tsx:469-537 |
| `LifecycleList` owns Operations navigation, row grouping, the selection callback, and hidden-list re-show behavior. | "function LifecycleListImpl({" | dashboard/src/panels/lifecycle-list/LifecycleList.tsx:294-294; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:224-224; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:307-307; dashboard/src/grammar/ModeBar.tsx:65-65; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:350-350; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:329-329 |
| `DetailPanel` resolves the selected task/lifecycle/series reader target and renders the task document content. | "function DetailPanelImpl({"; "export function displayedReaderDoc({"; "export function TaskReader({" | dashboard/src/panels/detail-panel/DetailPanel.tsx:18-18; dashboard/src/panels/detail-panel/model.ts:102-102; dashboard/src/panels/detail-panel/taskReader.tsx:614-614 |
| The lifecycle state vocabulary is the live/terminal partition consumed by the lifecycle panel; the `State`/`Phase` literals moved to `models/lifecycle.py` by 260731-EFA-L9 while the live/terminal sets stay in observer. | "State = Literal[LiveState"; "LIVE_STATES: tuple[LiveState"; "TERMINAL_STATES: frozenset[str] = frozenset(vocabulary_names(TerminalState, label=\"TerminalState\"))"; "export const LifecycleList = memo(LifecycleListImpl);" | mcp/src/agents_remember/models/lifecycles/responses.py:19-19; mcp/src/agents_remember/observer/lifecycle_state.py:105-105; mcp/src/agents_remember/observer/lifecycle_state.py:108-108; dashboard/src/panels/lifecycle-list/LifecycleList.tsx:357-357 |
| The shared fixture builders seed lifecycle and projection nodes from served fixtures, with required lifecycle fields copied from the served lifecycle. | `SERVED_LIFECYCLE`; `BASE_LIFECYCLE`; `lifecycle`; `projection` | dashboard/src/test/fixtures/wire.ts:78-78; dashboard/src/test/fixtures/wire.ts:95-107; dashboard/src/test/fixtures/wire.ts:241-246; dashboard/src/test/fixtures/wire.ts:329-345 |
| The typed fixture factories provide lifecycle and projection nodes. | `lifecycle`; `projection` | dashboard/src/test/fixtures/wire.ts:241-246; dashboard/src/test/fixtures/wire.ts:329-345 |
| The hand-kept snapshot payload provides the generated timestamp. | "\"generatedAt\": \"2026-06-14T09:01:00+00:00\"" | dashboard/src/fixtures/snapshot.json:1748-1748 |
| `Dot` renders its state glyph inside `aria-hidden="true"`. | `Dot`; "aria-hidden=\"true\"" | dashboard/src/grammar/Dot.tsx:119-129 |
## Current L5I Route State

The panels route now treats keep-alive shells as an explicit performance boundary: persistent
top-level panels memoize unchanged shell rerenders, while their own store subscriptions remain live.
Interactive controls also favor evidence-bounded wording, including reopened gate failures and
viewport-measured leaf-picker placement.

## 260727-CHATS-IM-L2 No Route-Model Impact

The Engine Room effects overlay and session-cockpit child-history behavior are internal to their
existing child routes. Panel inventory, cross-panel ownership, and the shared panel primitive are
unchanged.

## 260731-EFA-L4 Typed Vocabulary Route Impact

The panel inventory is unchanged. What changed is the vocabulary the panels consume, and four rules
now hold across the route rather than inside one file.

- **The state mark is named by the panel, never by `Dot`.** `grammar/Dot` renders `aria-hidden="true"`,
  so the accessible name for a severity or a lifecycle state is the wrapper's duty. `AttentionQueue.tsx`
  wraps it in a `severityMark` span carrying `role="img"` + `aria-label="Severity: <severity>"`;
  `LifecycleList.tsx`'s `data-testid="task-state"` span carries the same kind of label with NO role and
  is correct only because it sits inside React Aria's `role="option"`, whose name-from-content absorbs
  it. Drop the role from the AttentionQueue wrapper and the severity leaves the accessibility tree
  entirely — `aria-label` on a bare `<span>` names a `generic`, which ARIA prohibits (axe-core
  `aria-prohibited-attr`, `serious`) and no screen reader announces. Any new panel that renders a `Dot`
  inherits this: supply a role that can hold a name, or sit inside one.
- **Two vocabularies reach one dot, and only one of them is the document's.** Both Operations row
  builders compute `lifecycle?.state ?? statusVariant(doc.status)` (`LifecycleList.tsx` `docRow` L595,
  `seriesRow` L644; `lifecycleRow` L717 passes `lifecycle.state` straight through), so a bound lifecycle
  hands `Dot` the RAW server state string and `statusVariant` only ever sees `TaskDocNode.status` /
  `SeriesNode.status` — whose entire vocabulary is `tasks/document.py::DocStatus`
  (planning · inProgress · Completed), assigned verbatim by `snapshots.py` at both build sites. That is
  why L4 could delete its `blocked` / `paused` / `abandoned` arms with no behaviour change: they sat on
  the right of the `??` and no served payload could enter them. Adding an `awaiting-developer` arm here
  would repeat the same defect — the live state already arrives on the left.
- **`awaiting-developer` is a rendered Operations state.** The lifecycle vocabulary is six states
  composed from named halves server-side (`observer/lifecycle_state.py`: `LiveState` + `TerminalState`,
  with `State = Literal[LiveState, TerminalState]` and `check_state_partition` refusing at import any
  state filed on neither side); `awaiting-developer` is LIVE, not terminal. `LifecycleList.test.tsx`
  pins the handover rather than the paint: an `awaiting-developer` row's mark must equal a bare
  `<Dot variant="awaiting-developer">` and must NOT equal what an unrecognised variant renders, and a
  `paused` row's mark must differ from an `abandoned` row's in the same list.
- **Rollup buckets are derived, not restated.** `Metrics extends LifecycleStateCounts` in the mirror and
  the bucket field names come from `ACTIVE_STATES` through `StateCountField<>`, so a seventh state adds
  a REQUIRED field and every object claiming to be a `Metrics` stops compiling until it counts it. The
  panels suites stopped hand-listing buckets: `LifecycleList.test.tsx` and `DetailPanel.test.tsx` build
  metrics with `metricsFor(lifecycles)`, the client twin of `reducer.py::_metrics`.

`DetailPanel`'s sub-task index now renders two different server rows. `SubTaskIndex` takes
`SubTaskRow`, the union of `TaskSubTaskRefNode` and `SeriesSubTaskNode` — two `extra="forbid"` server
models that share five fields and differ in exactly one each. Only `TaskSubTaskRefNode` declares
`linkedLifecycleId`, so the cross-series `→` jump is reachable only from a master task document; the
branch is guarded by
`"linkedLifecycleId" in ref` and is structurally unreachable for a series rendered through
`seriesAsMasterDoc`. Only `SeriesSubTaskNode` declares `createdAt`, so creation ordering moved OFF the
index — where it could never have sorted a master's rows — and onto `seriesAsMasterDoc`, the one path
whose rows carry the field; `snapshots.py::_series_subtask_nodes` has normally already applied it, and
both sides skip the sort unless every row carries a `createdAt`.

**What the fixture conversion does and does not pin.** `EventRiver.test.tsx`, `RailChat.test.tsx` and
`SessionComposer.test.tsx` no longer author wire nodes: every projection node comes from
`dashboard/src/test/fixtures/wire.ts`, whose bases are assembled from `dashboard/src/fixtures/snapshot.json`
and annotated with the mirror type, so a fixture that compiles is a shape the MIRROR can produce. Be
exact about the reach — `wire.ts` and `snapshot.json` are hand-maintained fixture/sample artifacts,
while `types/projection.ts` is generated and stale-checked from the Pydantic projection schema.
`tsc -b` binds `test/fixtures/wire.ts` to that generated mirror (annotated bases,
`Overrides<O, Node>` at every call site, `test/wireFixtureGuard.test.ts` refusing one-token opt-outs),
and `test/contract.test.ts` measures how completely `snapshot.json` exercises it in three type-level
directions plus runtime vocabulary assertions. The producer-to-TypeScript contract is held by the
generator and its stale check; the manual boundary is sample coverage.

## 260731-EFA-L7 — Conversation Split Absorbed

The panels route absorbed the L7 live-thinking change on top of the L8 split: the session-cockpit conversation family carries the coalesced live-thinking indicator and its pins; the over-limit dashboard files were split by L8 and the armed file-size rail now covers this route's TS/TSX.

## L23 Engine Room Admission Evidence

Panel-level operations now expose the control plane's source-lineage state as a
diagnostic fact. Rendering stays read-only and uses the projected summary for
operator context; recovery remains a backend worktree operation.

## 260815-DAG-L14 Detail-Panel Route

`detail-panel/` threads `docPathForRef` so typed `masterRef` sprint rows open their commanded
master document (the sprint → master leg of the drill-down); the reader renders `MasterRefIndexRow`
for projected targets and falls back for unprojected ones.


## 260815-DAG-L12 Route Impact

New child route [sprint-graph](sprint-graph/overview.md): the optional sprint execution graph wave-grid view (≤3 boxes per row, ellipsized leaf lines, atomic lumps, textual predecessor labels, narrow single-column fallback). `detail-panel/taskReader.tsx` mounts graph content when present and mounts the sprint-scoped `CloseoutQueue` independently, so graph-less atomic-sequential sprints still expose scheduling state (L12-R5); `detail-panel/model.ts` `MasterDocView` carries optional `executionGraphView` (L12-R4).

## 260821-CLIVE Projection And Discard Panels

`CloseoutQueue` renders the producer's disposable service/source/problem/member projection. Typed
`invalid-empty` source problems include their repair action; the browser does not reconstruct
readiness or mutate queue state. Graph presence is not a prerequisite for this scoped projection.

The detail reader has a separate `Discarded before start` audit section with reason, timestamp, and
proof fingerprint. `LifecycleList` appends `N discarded` beside ordinary done/total progress. Both
surfaces preserve the same boundary: audited removal stays visible but never counts as completion.


## 260815-DAG Master Full-Gate Repair Route Impact

`session-cockpit` test suites (BusPane, ChatsStageBody, ConversationSurface, stageSurface) now flush the virtualizer scroll-observer debounce in an async `afterEach` before jsdom teardown.


## 260831-CCR-L23 Task-Artifact Reader Routing

L23 routed task-local requirement packets through the existing reader chrome: `DetailPanel.tsx`,
`taskReader.tsx`, `TaskNotes.tsx`, and the takeover now carry the shared discriminated
`TaskArtifactReaderTarget` (kind notes/requirements); the task reader mounts the
`TaskRequirementLinks` provider so task prose and References can open registered
`requirements/...` packets in the internal reader. The notes-reader child route owns the
viewer change; file-level detail lives in the panel sidecars.

## Update History

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 route impact: recorded the requirement-artifact routing through the detail panel, task reader, and TaskNotes (shared `TaskArtifactReaderTarget` + `TaskRequirementLinks` provider).

- 2026-08-31T09:06+02:00 — 260821-ARSPAWN-L5 A005 citation reconciliation refreshed
  the contextual-chat route citations after reviewed source movement; the panels-route ownership
  contract is unchanged. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Recorded projection-only closeout rendering, typed invalid-empty repair
  evidence, graph-less sprint visibility, and distinct discard-before-start audit/progress behavior.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: session-cockpit tests gained async `afterEach` virtualizer-debounce flushes. Verified at code commit e5cb139f.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   L12 adds the sprint-graph child route; DetailPanel mounts the wave-grid view plus the scoped closeout queue on the sprint page. Verified at code commit b7f2c8e2.

- 2026-08-20T05:06+02:00 — 260815-DAG-L14 route impact: the detail panel opens commanded master
  documents from typed `masterRef` rows. Verified at code commit 8071a644.


- 2026-08-18T13:00+02:00 — No route impact: 260815-DAG-L8 added the closeout-queue projection surface; route purpose unchanged.

- 2026-08-15T02:16:50+02:00 — No route impact: panel test fixtures were extended with the required
  empty `executionWaves` cell after TaskDocNode gained the field. No panel behavior changed in L1.

- 2026-08-14T06:25+02:00 — No route impact: L23's final dashboard delta is confined to the
  session-cockpit child route (shared sprint/master/leaf fixture coverage, rail width containment,
  and deterministic fake-timer cleanup). The panels inventory and ownership remain unchanged;
  verification stays closeout-owned.

- 2026-08-13T12:26+02:00 — L23 live-progress clarification: Hangar now displays the plane-owned
  lifecycle `currentCommand` in the existing operation badge using responsive single-line ellipsis
  plus a full-value title; focused render coverage pins the projection boundary. Verification
  provenance remains closeout-owned.

- 2026-08-13T09:05+02:00 — No route impact: L23's current source delta changes backend lifecycle,
  lineage, runtime packaging, and tests only; `dashboard/src/panels/` has no changed source path and
  its eight-panel UI model remains unchanged. Verification provenance remains closeout-owned.
- 2026-08-12T20:20+02:00 — L23 curator: documented panel routing of source-lineage admission evidence; verification remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator route review: L23 makes Hangar expose optional durable lifecycle-operation kind, status, and phase as a compact enclosure badge without inventing an operation when none is projected. Verification provenance remains closeout-owned.

- 2026-08-12T04:04+02:00 — Recorded the shared-panel startup invariant exposed by the live dashboard
  repair: an always-mounted Zustand consumer must return a referentially stable selector fallback
  before the first projection. Verification metadata remains pinned until governed closeout.

- 2026-08-11T23:40+02:00 — No route impact: helper extractions in `HighlightComposer.tsx`,
  `RailChat.tsx`, and detail-panel state preserve explicit reliable submission, structural
  document-and-role selection, and pure selected-task projection. Verification metadata remains
  pinned until governed closeout.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled the panels route with the
  document-and-role cockpit control surface; affected child overviews own the exact UI behavior.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded sprint-group panel projection and the legacy
  migration boundary. Verification metadata remains pinned until closeout.

- 2026-08-09T22:22+02:00 — No route impact: a test-only scroll-memory teardown repair is
  confined to the conversation timeline fixtures and suites. Panel production surfaces and
  hierarchy remain unchanged; detail lives in the conversation overview.

- 2026-08-09T20:25+02:00 — 260713-TES-L5F2 route impact: replaced shared-panel lifecycle-gate
  answer fixtures with lifecycle-free exact-session interaction-response coverage.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 route impact: route body reviewed and updated for the supervisor -> agent-notifier rename (see the route-specific body section above); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 route impact (trace delta): recorded the conversation split absorption and the file-size rail coverage. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: added the L8 Split Layout section (kebab-case folders, canonical entries, parts/styles modules). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T15:29:35+02:00 — 260731-EFA-L6 S18-B11 same-reviewer residual correction: rebound Chats mount/props, lifecycle navigation/reader ownership, and served-fixture seeding to the packet-specified operative spans. Verification metadata unchanged.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: corrected panel-route provenance: panels
  consume a generated schema mirror, while fixture builders and the manual snapshot remain measured
  consumers of it. New ranges are explicit scoped fixer output.

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the two
  `observer/projection.py` citations inside the 12:20 entry below, after that module was
  restructured. `L542-L559` → `L552-L569` (`TaskSubTaskRefNode`, ending on `linkedLifecycleId`
  L569) and `L624-L639` → `L634-L649` (`SeriesSubTaskNode`, ending on `createdAt` L649). No body
  claim changed.

- 2026-08-01T14:05+02:00 — 260731-EFA-L4 curator (correction pass), body only. "What the fixture
  conversion does and does not pin" said *"`fixture ⊆ mirror` is what the dashboard tests enforce.
  `mirror ⊆ server` is enforced by nothing"* — the outer two nodes of a four-node chain, which reads as
  though nothing measures the mirror against the snapshot. It does: `test/contract.test.ts` measures
  `types/projection.ts` against `fixtures/snapshot.json` in three TYPE-level directions
  (`mirror ⊇ served`, `served ⊇ mirror`, `fixture ⊇ mirror` — L29-L53) plus runtime `VOCABULARIES`
  assertions (L269, L348, L368) for the string unions `resolveJsonModule` widens to `string`. The
  paragraph now names all three links and states the unheld one as **`snapshot.json` ↔
  `observer/projection.py`, by hand** rather than as "`mirror ⊆ server`" — one letter from
  "`mirror ⊆ served`", which *is* enforced. Also brought the no-generator claim to the strength the
  evidence carries: no in-repo generator **and no in-repo mechanism keeping the two sides in step**.
  Same correction applied to the 12:20 entry's restatement below. No component claim, table row, or
  verification field changed.

- 2026-08-01T12:20+02:00 — 260731-EFA-L4 route impact (wire contracts and typed vocabularies): added
  the "Typed Vocabulary Route Impact" section. Both component changes in this route are real, not
  incidental. `AttentionQueue.tsx` gained the `role="img"` `severityMark` wrapper because `Dot` is
  `aria-hidden` and a bare-span `aria-label` names a `generic` (ARIA-prohibited; axe-core
  `aria-prohibited-attr`, `serious`) — recorded as a route-wide rule with the reason `LifecycleList`
  needs no role (React Aria `role="option"` name-from-content). `LifecycleList.tsx`'s `statusVariant`
  lost its `blocked`/`paused`/`abandoned` arms; I verified this is behaviour-identical by reading both
  call sites (`docRow` L595, `seriesRow` L644 — `lifecycle?.state ?? statusVariant(...)`, so the live
  state never reaches the map) and the input vocabulary end to end
  (`tasks/document.py::DocStatus` L30 = planning/inProgress/Completed → `snapshots.py` `status=doc.status`
  at L1304 for `SeriesNode` and L1398 for `TaskDocNode`). Recorded `awaiting-developer` as a LIVE state
  of the server-side partition (`observer/lifecycle_state.py`) with the two new `LifecycleList.test.tsx`
  handover regressions, `Metrics extends LifecycleStateCounts` with `metricsFor` replacing hand-listed
  buckets, and the `SubTaskRow` union with the two `extra="forbid"` server models it unions
  (`projection.py` L552-L569 `TaskSubTaskRefNode` — no `createdAt`; L634-L649 `SeriesSubTaskNode` — no
  `linkedLifecycleId`), which is why the `→` cross-series jump is master-task-doc-only and why the
  creation sort moved to `seriesAsMasterDoc`. Stated the fixture chain's honest reach: `wire.ts` and
  `snapshot.json` are hand-maintained with no generator anywhere in this repository, the fixture→mirror
  and mirror→snapshot links are both test-enforced, and the `snapshot.json` ↔ `observer/projection.py`
  crossing is held by nothing. (This bullet originally read "`fixture ⊆ mirror` is test-enforced and
  `mirror ⊆ server` is enforced by nothing", which dropped the middle link; corrected in the 14:05
  entry.) Added four two-cell
  `Repo-Internal References` rows (this table is two columns; no ranges added to it). Evidence: the six
  suites over this route's files run green (106 tests). Verification metadata pinned until closeout
  stamps the commit.

- 2026-07-30T12:51+02:00 — No route-model impact for 260727-CHATS-IM-L2. The
  Engine Room effects-root isolation is governed by the `engine-room/` child overview and the
  selected-child history surface by `session-cockpit/`; the panels inventory and ownership split
  remain unchanged. Verification metadata remains pinned until closeout.

- 2026-07-24T13:17:17Z — Curator: documented cross-panel persistent-subtree memoization and the
  current evidence/placement conventions introduced by this route's owned sources. Verification
  metadata remains pre-commit.

- 2026-07-21T11:30+02:00 — No route impact: the `dashboard/src/panels` route model is unchanged by
  260718-CHATS-L5F (half-time functional fixes, PASS-WITH-NOTES). No DIRECT `panels/` child changed;
  the leaf's single panels-tree edit is `session-cockpit/SessionsView.tsx` (the R9 focused-seat
  live-turn merge), governed by the [session-cockpit/](session-cockpit/overview.md) child route and
  recorded there and in its sidecar. Verification metadata advances with closeout stamping only.
  260718-CHATS-L5P (cockpit chrome visual polish, PASS-WITH-NOTES; dashboard-only, zero backend edits).
  Two DIRECT `panels/` children got styling polish captured in their own sidecars, not this route body:
  `SessionComposer.tsx` — the editor frame joins the terminal `well` (FB7.1) + gains a `:focus-within`
  amber ring (V4), the footer hint is capability-derived on legacy-raw terminal seats (V9), `draft saved`
  is exception-only (V14), and the send button holds width/single-line under the inspector (V3);
  `Terminal.tsx` — the host `background` `#070b0f` literal migrated to the `well` token (V31). The bulk of
  the leaf's chrome polish lives under [session-cockpit/](session-cockpit/overview.md) (its "Cockpit chrome
  conventions" section). Verification metadata unchanged.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 route impact (structured Chats renderer, reviewer FINAL
  PASS): corrected the stale shared-panel claims — the controlled-session runner line-log is now the
  read-only terminal-diagnostics drawer + legacy-raw body (the structured `ConversationSurface` is the
  controlled default), and UA-1 history/index/resume is landed as a reconstructable projection with no
  durable browser conversation index. The two new `conversation/` and `conversation-library/`
  grandchild routes are governed by the [session-cockpit](session-cockpit/overview.md) overview; this
  compact parent's route inventory is otherwise unchanged. `SessionComposer.tsx`'s L4 change is a
  presentation-only hint-line regrouping (no authority change). Verification metadata remains pinned
  pending L4 candidate closeout.

- 2026-07-18T15:22+02:00 — FEUI-MX-FIX-2: recorded visible create failures and accepted-row gates
  for HighlightComposer and RailChat, including zero context delivery and zero private row/focus
  mutation on failure. Verification metadata remains pinned pending candidate closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded xterm-preserving boot reattach, bounded chooser
  recovery, and empty-narrow entrance preservation. Verification metadata remains pinned pending
  candidate closeout.

- 2026-07-18T07:22+02:00 — 260715-FEUI-L8 strategic refactor: reduced this packed parent to
  composition boundaries, made session-cockpit the sole Chats owner, routed data-plane detail to
  the new data overview, and recorded legacy retirement without claiming the future structured
  conversation UI. Metadata remains pinned to the leaf base.

- 2026-07-18T00:08+02:00 — 260715-FEUI-L7 curator closeout delta: replaced the interim inspector
  scaffolding with the stable-mounted Evidence/Capabilities/Bus host, documented explicit mark-seen
  and post-removal residual behavior, separated exact-session capability truth, recorded fleet Bus
  sender-only reply and entry-state/virtualization invariants, and added the honest ordered StatusLine.
  Detailed component and test routing remains in the `session-cockpit/` child overview.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: replaced current bracketed/draft-paste
  descriptions for SessionComposer, RailChat leaf context, and HighlightComposer with the shared
  epoch-bound reliable-submit path, provenance, create-ready handling, and the raw-PTY boundary.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 route impact: the `session-cockpit/` child route gains
  `ModelEffortControl`, `AcceptanceChip`, `CockpitLiveRegions`, and `SetOutcomeToasts` with their
  focused suites; existing HeaderStrip/SeatInspector/SessionRail/SessionsView surfaces gain the
  one control, collapsed acknowledging ledger, worded rail attention/named dots, cycle-effort,
  queued hint, watchers, and persistent outcome plumbing. Pure policy and I/O remain in the L4
  `data/` layer named above. No other panel or MCP package-data route changed because the worker
  did not run dashboard bundle sync. Verification metadata is pinned to the contract base until
  code commit.
- 2026-07-17T06:30+02:00 — 260715-FEUI-L3 route impact (capability catalog client and launch
  flow): the `session-cockpit/` child route gains its LAUNCH layer — `LaunchFlow.tsx` (the
  palette-opened catalog-driven launch overlay) + `FailedLaunchBanner.tsx` (verbatim failed-seat
  refusal surface) with their jsdom suites; `SessionsView` registers `session.launch` and mounts
  both (pure appends); `HeaderStrip`/`SeatInspector` derive the R7 evidence tier from row
  control-state truth and render `grammar/EvidenceBadge`; `SessionStage`'s empty-state copy
  points at the palette launcher. No OTHER panel changed in this leaf (Chats/Terminal untouched).
  Detail lives in the `session-cockpit/` overview and the touched sidecars. Verification
  metadata pinned to the leaf base until closeout stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 route impact (PTY stage surface, structured
  interactions, session lifecycle actions): the `session-cockpit/` child route gains
  `PtySurface`/`InteractionBar`/`WorkingLine`/`StopResidualNotes`/`lifecycleCopy` (+ four jsdom
  suites) — the stage body is filled with keep-alive real xterm panes (DOM renderer by
  measurement) and the gate-only interaction bar; `Terminal.tsx` gains additive optional props
  (renderer seam with lazy webgl escalation, screenReaderMode live options mutation, observe-only
  harvesting hooks, keyEventFilter, onResizeCols, ariaLabel) with byte-compatible defaults for
  the legacy call sites, plus a guaranteed named `role="group"` landmark (sessionId fallback);
  `Chats.tsx`/`RailChat.tsx` pass real `ariaLabel`s at their Terminal call sites (one prop per
  call site — review F6). No panel was removed; per-file detail lives in the sidecars and the
  `session-cockpit/` overview. Verification metadata pinned to the leaf base until closeout
  stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 route impact (session data layer, rail, and stage
  container): the `session-cockpit/` child route is FILLED — `SessionRail`/`SessionStage`/
  `HeaderStrip`/`StateDot`/`SeatInspector` (+ two jsdom suites) land and `SessionsView` becomes
  the once-derived model/rollup seam with smart-default focus, focus handoff, and dynamic palette
  commands; `Chats.tsx` hands its 2.5s catalog poll to the shared `data/catalogPoll.ts` driver
  (consumer semantics byte-equivalent); `file-viewer/FileViewer.tsx` gains a reviewer-accepted
  one-line defensive repos-catalog guard. Detail lives in the `session-cockpit/` overview and the
  touched sidecars; no panel was removed. Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.
- 2026-07-17T00:30+02:00 — 260715-FEUI-L1 route impact: the route gains the **`session-cockpit/`**
  child route — the Sessions cockpit view shell (rail/stage/inspector PanelGroup + narrow rules +
  ~80-col floor chip + rail calibration), the non-portal cmdk CommandPalette (commands/keys pages
  from one options source), and the useKeyboardZones tinykeys binding — registered in
  `cockpit/Cockpit.tsx` as the fourth keep-alive full-bleed layer. Panel content is labeled
  scaffolding for L2/L4/L5/L6/L7. Added the bullet + child-route link; no existing panel changed.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.

- 2026-07-12T17:50+02:00 — 260712-TRH-L6 route impact: documented the new Operations chat-activity indicator,
  shared Chats catalog ownership, exact-leaf-first/lifecycle-fallback identity, deterministic multi-seat
  precedence, static inbox acknowledgment state, missing/landed/stale omission behavior, and the three
  independent signaling axes. No new dashboard route was introduced. Reviewer F1–F6 are recorded as
  follow-up residuals in the relevant sidecars.
- 2026-07-12T13:36+02:00 — No route impact: 260712-TRH-L2 body review confirms the `DetailPanel` change-set entry and `panels/changeset` child-route refinements do not alter the broader panels inventory or navigation model. Verification metadata remains pinned until closeout.
- 2026-07-12T12:58+02:00 — 260712-TRH-L3 route impact: refreshed the existing `LifecycleList.tsx`
  route model for BY REPO-only persisted sprint/master disclosure, independent nested collapse,
  selection-safe native controls, and unchanged BY PHASE/total-count semantics. No new route or entity
  was introduced; the two concrete helper modules are covered by file sidecars.
- 2026-07-12T12:55+02:00 — No additional route impact from 260712-TRH-L2: its `DetailPanel` change-set entry and `panels/changeset` child-route refinements do not alter the broader panels inventory or navigation model. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-12T12:07+02:00 — 260712-TRH-L1 route impact: added the body-state data hook and made
  `DetailPanel` defer notes plus reader/enclosure change-set requests until visible body hydration
  succeeds or fails. Summary fallback and panel inventory remain intact; verification metadata stays
  pinned until closeout.

- 2026-07-10T21:52+02:00 — 260707-HFX2-L21 route impact: the existing Chats full-bleed layout now
  has a bounded, persisted, pointer/keyboard-resizable session-tree rail. Panel inventory and routing
  are unchanged; focused coverage pins restoration, ARIA values, drag, arrow steps, and persistence.
  Verification metadata remains pinned to the task base until closeout.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 panels route impact: added explicit seat-role picker,
  pair-aware attach/move, and binding-first rail/fleet rendering; no route layout change.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16 route impact: refreshed the existing SessionList and
  DetailPanel responsibilities for complete spawn forests, manager-only collapse, bounded hover-
  recoverable rows, merged task bodies, explicit summary fallback, and one implementation-step list.
  Panel inventory/routing is unchanged. Verification metadata stays pinned until closeout.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6 route impact: migrated `DetailPanel` to fetch only
  the displayed task body on demand, cache it by path/revision, and keep summary fallback behavior;
  test fetch doubles now serve that endpoint. Verification metadata remains pinned until closeout
  stamps the eventual L13 code commit.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 route impact (landed chat archive + group cleanup):
  `Chats.tsx` and `SessionList.tsx` gain a collapsed "landed archive" group for `status:"landed"`
  rows (role/leaf/master/label/turn-state/landed-reason/timestamp/provenance surfaced, non-live but
  inspectable) plus a "Close landed archive" group-cleanup control (backend-rechecked, reports
  closed/skipped); `Terminal.tsx` gains a `readOnly` prop so a landed seat's terminal stays viewable
  without accepting input. No new panel module or routing change — per-file detail lives in each
  file's own sidecar. Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-08T04:25+02:00 — 260707-HFX-L12 route impact (docs-parity fold-in, master-exit Finding
  3): `SessionList`'s `ROLE_VALUES`/`roleChip` registry gains `designer` (gold) and
  `system-specialist` (cyan), matching the existing four-tier color convention (no new token) —
  both roles were already spawnable but rendered as the muted base chip; the panels route inventory
  itself is unchanged (same mechanism, two more registered Literal members). Verification metadata
  pinned until closeout stamps the HFX-L12 commit.
- 2026-07-07T23:55+02:00 — 260707-HFX-L6 route impact: `SessionList`/`Chats`
  role rendering and the dormant `FlowTab` model now carry architect/curator seats, matching the
  architect/default developer-facing split and curator closeout chain while keeping the panels route
  inventory unchanged. Verification metadata pinned until closeout stamps the HFX-L6 commit.
- 2026-07-07T14:00+02:00 — agent-orchestration L17 route impact: the route gains the **`notes-reader/`**
  child route (the Notes Reader takeover — a notes-tree rail + a content pane that REUSES the File Viewer
  `DualPane`, over the unchanged L9 `/api/notes/*` API). `TaskNotes.tsx` becomes the compact ENTRY SURFACE
  only (its inline reader retired; list + references now call `onOpenNotes`), `DetailPanel.tsx` threads
  `onOpenNotes` to it, and `LifecycleList.tsx`'s `gateHint` drops the wait-loop `ask` fallback (durable gate
  kind only). Added the `notes-reader/` bullet + child-route link, rewrote the `TaskNotes` bullet, and
  de-staled the `DetailPanel`/`LifecycleList` bullets. Verification metadata pinned until closeout stamps the
  L17 commit.
- 2026-07-07T10:55+02:00 — L15 route impact (body): the four age panels' served-ages local-advance pattern documented. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:40+02:00 — 260703-L15 route impact (small): the four age-display panels
  (`Hangar.tsx`, `AttentionQueue.tsx`, `MemoryMirror.tsx`, `LifecycleList.tsx`) now advance served
  ages locally — `servedAgeSeconds(node, …Seconds, nowMs)` + a panel-level `useNowMs()` 10 s tick
  (`data/servedAges.ts`) — because the L15 change gate stopped re-serving nodes whose only
  movement is their age. No layout/behavior change otherwise; the panels route model is unchanged.
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:57:24+02:00 — 260703-L14 route impact (visual hierarchy + chat grouping): the tasks tab
  gained the orchestration tier (gold/purple V4 command rows over `TaskDocNode.orchestrates`, N-depth
  `BY REPO` hierarchy, 22px indent grammar, `grammar/RankBadge` insignia — see `LifecycleList.tsx`),
  and the Chats sidebar gained the G1 command tree (`SessionList` collapsible groups over the new
  `data/sessionGroups` model threaded by `Chats.tsx`, spawn-role chips from the catalog's
  AR_SPAWN_ROLE). The GOLD tier is orchestration-gated (D3): the orchestration row and the sprint deck appear only when an orchestration task exists; master grouping + the landed archive are the chats pane's BASELINE organization (grouping-always, owner-ratified at review L14R-1), mirroring the tasks tab's master>leaf nesting. The tasks tab itself renders flat runs exactly as before.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T15:40+02:00 — 260703-L12 route impact (three-party loops, canvas ride-along): `flowModels.ts` gains the STRATEGIST model (FLOW_MODELS census 7 → 8; placed between designer and orchestrator) and loop-doctrine lines on the manager/worker/reviewer/comms/orchestrator drawings; `FlowTab.test.tsx` grows to 11 cases (strategist model + cross-model loop invariants). FlowTab.tsx itself is unchanged (pure renderer over the registry). Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T12:10+02:00 — 260703-L10 route impact (small): the FlowTab canvas was verified against the converged `l-01-agent-lifecycles` doctrine (S2 reduced to verification after L8 shipped the redraw); the one residual vocabulary drift fixed is the designer model's reframe-agreement node phase label, `"frame"` → `"reframe"`. Tests (41 files / 385) stay green — no invariant string changed. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-06T10:30+02:00 — L11 adversarial-review follow-up: the anchor fallback annotation is deterministic (greatest lastEventTs), closing L11R-2. Verification metadata pinned until closeout stamps the L11 commit.
- 2026-07-06T02:50+02:00 — 260703-L9 route impact (friction F-M): the route gains `TaskNotes.tsx`
  (+ its component suite), the read-only coordination-notes surface — series notes list over
  `/api/notes/*`, opened notes rendered as formatted markdown (sidecar treatment), and task-doc
  references resolved into openable links; `DetailPanel.tsx`'s `TaskReader` delegates its
  References section to it and `MasterOverview` appends it. Verification metadata pinned until
  closeout stamps the L9 commit.
- 2026-07-06T02:45+02:00 — 260703-L11 route impact (tasks tab shows worktree truth): `Hangar` and
  `LifecycleList` visibility flipped from cleanup-state proxies to the shared `hasLiveWorktree`
  existence rule over the new `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags — a
  reopened contract stays hidden until `worktree_start` recreates its worktrees; `LifecycleList` adds
  the one-row-per-`enclosureId` identity rule with `lifecycleForEnclosure` annotating the single doc row (deterministically: greatest `lastEventTs` wins the anchor fallback, L11R-2)
  instead of duplicating the leaf as a lifecycle card. Verification metadata pinned until closeout
  stamps the L11 commit.
- 2026-07-05T19:55+02:00 — 260703-L8 route impact (cycle 7, AR4-3/AR4-4): the seam-channel sentence rescoped to what the canvas draws — the manager raise node now names `enclosure="<master task name>"` as the exact address integration enforcement matches the gate by (AR4-4), so the enclosure clause is true as-drawn; the cycle-6 owner follow-up's "exactly … integration enforces the verdict by master identity" overclaim is dropped (enforcement itself is not a drawn node). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:25+02:00 — 260703-L8 route impact (cycle 6, owner follow-up): body de-staled — the FlowTab paragraph's leftover build-job/frame tail (deleted models, the "8 static models" reference row, the "other seven" phrasing) replaced with the converged 7-model census and the exact ruled seam channel (wait=false raise, enclosure address, packet-carried gateId, identity-addressed enforcement). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 — 260703-L8 route impact (cycle 6, small): the flowModels seam nodes now draw the ruled channel exactly — the manager's raise carries wait=false with the returned gateId riding the packet, and the orchestrator decides by the packet-carried gateId; FlowTab tests pin the new prose. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:32+02:00 — 260703-L8 route impact (small): the FlowTab registry now draws the converged lifecycle doctrine — ROUTER model (three conditions + D·P·O event loop + the invariant ladder) replaces the retired FRAME and BUILD-JOB models; worker/manager/orchestrator/reviewer/comms models redrawn to the ruled seam semantics; FlowTab tests rewritten (9). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:31+02:00 - L3 route impact: task-row pickup feedback now
  mirrors message-kind and hosted-delivery metadata from `AgentPickupNode`.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T09:40+02:00 — 260703-L0 (Canvas & playground) route impact: reworked the `FlowTab.tsx` bullet
  from the dormant single-model Lifecycle Flow diagnostic into the **lifecycle-design canvas** — a pure
  segment renderer + radiogroup model nav (still zero store reads) over the **new `flowModels.ts`**
  flow-model registry (8 static models: build-job · frame · designer · orchestrator · manager · worker ·
  reviewer · comms, encoding the orchestration series' agreed invariants). The build-job model preserves
  the task-26 chain and stays the `next_step.py` SPEC; the source is now **mounted dev-only at `/dev/flows`**
  via `dev/DevApp.tsx` (kept out of the cockpit `View` union per task 29) and covered by the new
  `FlowTab.test.tsx`. Added `panels/flowModels.ts.md` + `panels/FlowTab.test.tsx.md` sidecars. Verification
  metadata pinned until closeout stamps the L0 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: LifecycleList excludes abandoned enclosures from the active rows and drops the -rN startsWith doc-admission heuristic (task_reopen keeps leaf ids stable).
- 2026-07-02T21:45+02:00 — L10 route impact: `LifecycleList`'s `enclosureForDoc` admission is now
  case-insensitive on every leafId comparison (stem, doc id, and the lifecycle-guarded reopen-suffix
  rule) — enclosure leaf ids are slugified lowercase while doc ids are authored uppercase, so active
  series leaf docs failed the admission and rendered as doc-less runtime rows with no task content and
  no viewed-leaf chat chain. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-02T20:55+02:00 — L8-r1 route correction (developer feedback): the direct leaf-chat paste is
  now triggered by the visible "Add to chat" pill CLICK instead of firing automatically on selection —
  the auto-paste made the interaction invisible and pasted unintended highlights. The pill stays for
  every selection with one consistent label; only the post-click routing differs (direct draft paste vs
  generic composer), and an unconfirmed direct paste opens the composer. Verification metadata pinned
  until closeout stamps the L8-r1 commit.
- 2026-07-02T20:15+02:00 — L8 route impact: highlight handling split into a **direct leaf-chat draft
  paste** primary path (selection inside the viewed leaf's task reader + active rail chat + bound leaf
  chat → `pasteDraftToSession`, no popover, popover fallback on failed paste) with the generic
  `HighlightComposer` popover as fallback only; `GateResponder` lost its message-only **Chat** mode
  (durable approve/reject/dismiss remain); `DetailPanel` no longer raises the responder for proto
  `ask`-only items and tags the task-doc reader with `data-task-leaf-key`. Covered by the updated
  `HighlightComposer/DetailPanel/GateResponder` tests and `selection.test.ts`. Verification metadata
  pinned until closeout stamps the L8 commit.
- 2026-07-02T17:04+02:00 — L9 route impact: extended the existing `Chats.tsx` / `RailChat.tsx` route model
  for hosted chat leaf reassignment. Attached chats keep the picker as a move control, successful moves
  emit `"leaf"` catalog invalidations and draft the destination leaf context, and out-of-session catalog
  changes live-refresh through BroadcastChannel or polling. Verification metadata pinned until closeout
  stamps the L9 commit.
- 2026-07-02T16:35+02:00 — Reopened L6 wheel-precedence route impact: the shared `Terminal` wrapper now
  defers wheel input to xterm's native mouse-report path whenever the attached app tracks the mouse
  (`term.modes.mouseTrackingMode !== "none"`). Combined with the backend's per-session tmux `mouse on`,
  wheel scrolling works for both normal-buffer TUIs (tmux copy-mode pane history — Codex) and
  mouse-aware alternate-screen TUIs (pass-through — Claude Code); synthesized PageUp/PageDown remains
  only as the mouse-less alternate-buffer fallback. `pasteDraftToSession` deliveries are now
  echo-confirmed with boot-deadline retries (`pasteAndConfirm`), fixing the leaf-context draft silently
  discarded by a booting Claude Code. Verification metadata pinned until closeout stamps the follow-up
  commit.
- 2026-07-02T15:03+02:00 — Reopened L6 served-page route impact: live 8770 inspection showed Codex-style
  chat panes in xterm's alternate buffer with no viewport scrollback, so the shared `Terminal` wrapper now
  keeps normal-buffer viewport scrolling but maps alternate-buffer wheel movement to PageUp/PageDown
  navigation. Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-02T14:28+02:00 — Reopened L6 route impact: the existing shared `Terminal` wrapper now captures
  wheel input, swallows partial pixel deltas, and routes accumulated movement to xterm viewport scrolling,
  preventing mouse wheel movement from becoming PTY up/down input in Chats and right-rail panes. No new
  route or panel surface was added; verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-02T13:07+02:00 — Reopened L6 route impact: leaf-context handoff remains in the existing
  `RailChat` route, but now pastes the packet as editable draft input instead of submitting it. The shared
  `Terminal` wrapper also enables xterm scrollback for Chats and right-rail panes. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-07-01T01:19+02:00 — L6 route impact: extended the `Chats.tsx` / `RailChat.tsx` route-model
  description with bind-time leaf context handoff. The route still owns the existing hosted chat surfaces;
  `RailChat` now sends a projected context package only after start-on-leaf or successful free-chat attach,
  using `taskDocuments` plus `engineProcesses` for task/worktree facts. Verification metadata pinned until
  closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up route impact: reshaped the **`RailChat`** route-model description — it is now a
  per-(leaf, role) **chat (agent harness) + terminal (shell) vertical split** with a harness-choice start
  picker (`fetchHarnesses`), a separate ＋ Terminal, and an independent **terminate** per pane (replacing the
  pre-fix single "＋ Start chat for this leaf"); added `RailChat.test.tsx` coverage. The Chats/`SessionList`
  leaf key now comes from the **displayed** leaf via `DetailPanel.onViewLeaf` (not the master selection),
  and `SessionList` rows gained a hover `title` (full label + bound leaf, fix 4). Verification metadata
  pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat) route impact: added **`RailChat.tsx`** (the single-instance right-rail
  leaf chat the cockpit `RailToggle` swaps in for the Event River, reusing the shared `Terminal` +
  `SessionComposer` + connection registry) to the Route Model, and extended the **Chats** bullet with
  leaf-keyed attachment — `Chats` gains an "Attach to leaf" control (`attach-leaf`, `200` bind / `409`
  "leaf already has a chat") + a bound-leaf badge, and `SessionList` gains a `leafNameFor` per-row leaf
  label (task-doc title, fallback leaf id). Verification metadata pinned until closeout stamps the L5
  commit.
- 2026-06-29T23:00+02:00 — No route impact: L4a added change-set buttons on the task-document reader
  (`DetailPanel`'s `DocChangeSetBar` — series on a master, committed/working on a leaf) and refined the
  `changeset/` child route (leaf committed/working views + a diff-highlight rectangle). The `panels/`
  route model — the panel list + the `file-viewer/`/`changeset/` child routes — is unchanged; the detail
  lives in the `DetailPanel.tsx` sidecar and the `changeset/` overview. Verification metadata pinned until
  closeout stamps the L4a commit.
- 2026-06-29T16:40+02:00 — Operations Integration L4 route impact: added the `changeset/` child route — the **Change-Set Viewer** screen (a task-scoped takeover over the L3 `/api/changeset/*` API; a read-only `@codemirror/merge` diff with split/inline/full-file/highlight-off toggles; a code↔sidecar partner column), opened from a `DetailPanel` change-set button as a Cockpit full-bleed takeover. See the new [changeset/ overview](changeset/overview.md). Verification metadata pinned to the task base until closeout stamps the L4 code commit.
- 2026-06-29T09:06+02:00 — Operations Integration L2 route impact: added the `file-viewer/` child route —
  the **File Viewer** centre tab (a read-only code + paired-onboarding browser over the L1 files API; a
  reusable CodeMirror dual-pane; bidirectional code↔onboarding pairing; kept mounted across tab switches).
  See the new [file-viewer/ overview](file-viewer/overview.md). Verification metadata pinned to the task
  base until closeout stamps the L2 code commit.
- 2026-06-28T16:17+02:00 — Task 35 route impact: `LifecycleList` now also admits a **reopened** leaf's
  suffixed-leaf enclosure (`leafId` = stem/`id` + cycle suffix, e.g. `…-s7`) on the combined shared-lifecycle
  + suffixed-leaf match (never a bare shared master lifecycle), and runtime-only enclosure-backed rows nest
  under their master via a computed parent key — so a re-opened/edited task no longer renders as a standalone
  phantom node. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: `EventRiver.tsx` now **virtualizes** the activity feed
  with `@tanstack/react-virtual` over the store's bounded sliding window (newest ~2000 rows), mounting
  only the visible rows (no hard display cap) while staying memory-bounded; the `/api/events` backend
  also now filters `lifecycle.heartbeat` out of the raw river, so the formatter's heartbeat hiding is
  belt-and-braces. Updated the `EventRiver.tsx` Route Model bullet. Verification metadata pinned until
  closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: `Topology.tsx` now filters to active worktree groups via
  `activeTopologyInputs` (reading the store's `activeWorktreeGroups`) before `buildTopology`. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: Event River no longer has a frontend newest-row
  cap and waits for the raw stream `ready` event before showing an empty feed, AttentionQueue
  dismiss/clear now optimistically suppresses lifecycle/gate/actionable-drift rows while writes are in
  flight, and `FlowTab.tsx` is documented as dormant because the Lifecycle Flow tab is hidden from the
  cockpit. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T05:38+02:00 — Task 29 route impact: Event River rendering now gates
  lifecycle-bound rows until lifecycle/enclosure/task-document context is available, while lifecycle-less
  workspace diagnostics can still render raw fallbacks. Verification metadata pinned until closeout
  stamps the task-29 code commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: `LifecycleList` now matches active leaf task documents
  against either the file stem or the authored `TaskDocNode.id`, restoring browser-dashboard leaf 31 under
  its parent master in Operations; the Engine Room panel route also renders expected-but-missing provider
  roles using the new provider boot-node state. Verification metadata pinned until closeout stamps the
  task-31 code commit.
- 2026-06-27T18:43+02:00 — Task 26 route impact: added the `FlowTab.tsx` **Lifecycle Flow** view to the
  panels inventory — a static (no-store) diagnostic of the build-job lifecycle in two regimes (a prose
  `RUNDOWN` front half emitted by `lifecycle_start` and a `LINEAR` worktree_start→lifecycle_end chain with
  gate `rides` annotations), wired as a full-bleed cockpit `flow` view and serving as the human-readable
  SPEC the task-27 `next_step.py` engine matches; dev frontend only (production bundle not rebuilt this
  task). Verification metadata pinned until closeout stamps the task-26 code commit.
- 2026-06-27T03:04+02:00 — Task 22 follow-up: Chats removed the local Hide row action; End is now the
  only session-list action, and id-bearing terminate invalidations remove rows across tabs without
  allowing stale catalog echoes to repaint them.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: Chats now listens for cross-tab terminal catalog
  invalidations, re-fetches durable rows when another tab opens/ends sessions, and broadcasts after
  backend-confirmed End so multiple browser tabs stay in sync.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: Chats treats End/terminate as label release, so terminated
  Claude chats do not force the next Claude label upward.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: corrected the Chats route model for mount-on-first-selection
  after refresh; hidden restored xterms no longer initialize before they are selected, and visited tabs
  still keep their xterm buffers.
- 2026-06-26T23:15+02:00 — Task 22 route impact: `Chats.tsx` and `SessionList.tsx` now expose durable
  catalog sessions, status badges/panels, last-active restore, and backend terminate for dashboard-owned
  terminals. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: `DetailPanel` master readers now show the
  server-projected `seriesTokenTotal` aggregate, with component coverage in `DetailPanel.test.tsx`.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T19:40+02:00 — Task 20 reopened: Event River route model now records
  the task-document title fallback for retained event-history rows whose
  lifecycle id no longer has a live lifecycle projection. Verification metadata
  pinned until closeout stamps the reopened task-20 code commit.
- 2026-06-26T18:14+02:00 — Task 20 route impact: Event River now includes the
  new `eventSummary.ts` formatter module and renders a readable activity feed
  over known observer events while preserving raw-event diagnostics and trust
  provenance. Verification metadata pinned until closeout stamps the task-20
  code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: `AttentionQueue` Clear now includes stale gate-only rows and sends gate-id-only cancel through the serving route.
- 2026-06-25T13:20+02:00 — Task 23/24: panels route now covers gate Dismiss/delete, attention Clear, and the `AgentPickupIndicator` waiting-for-agent/check-chat task-row feedback.
- 2026-06-25T07:26+02:00 — Task 19 gate interaction polish: `GateResponder` now has separate durable
  Yes/No decision paths and a message-only Chat path, renders readable gate previews with diagnostics
  behind details, and gives leaf prompt previews a 480px resizable area. `AttentionQueue` now renders
  lifecycle-bound rows with task id/title first. Verification metadata pinned until closeout stamps the
  code commit.
- 2026-06-25T02:53+02:00 — Operations title-overflow correction: `LifecycleList` now constrains the
  listbox/section grid tracks, row minimum widths, and secondary metadata chips so long task titles
  ellipsize inside the left rail instead of creating a horizontal scrollbar or disappearing. Detail
  lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-24T21:49+02:00 — Task 17 route correction: cleanup-completed leaf enclosures no longer count
  as active sidebar enclosures; their task docs remain reachable through master/taskdoc navigation.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:13+02:00 — Empty-state backdrop zoom-stability pass: refreshed the
  `EmptyStateBackdrop.tsx` route-model bullet for the final static direct-video contract. The shared panel
  still provides the same effects-gated boomerang-video atmosphere, but runtime zoom layers are excluded;
  the 60fps MP4 assets own the slow zoom/cadence. Detail lives in the `EmptyStateBackdrop.tsx` and
  `EmptyStateBackdrop.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-24T18:11+02:00 — Task 17 route correction: Operations and Detail now label authored leaf rows
  from the child `TaskDocNode.id`, with parent sub-task `number` only as fallback data. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:02+02:00 — Task 17 route correction: Operations and Detail now display structured
  sub-task numbers for leaf labels, while creation metadata controls ordering/placement and no filename
  parsing is introduced. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Task 17 Operations hierarchy route update: `LifecycleList` now nests
  admitted active leaves beneath their parent/root task in `BY REPO`, and `DetailPanel` gives directly
  opened leaf documents a structured parent/root backlink. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:20+02:00 — Task 17 sidebar/master navigation route correction: `LifecycleList` now scopes
  the Operations sidebar to root/master docs, enclosure-matched leaves, series fallbacks, and
  enclosure-backed runtime fallbacks, while `DetailPanel` keeps master sub-task navigation wired to the
  full projected sibling document pool. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 Operations route correction: `LifecycleList` is task-document-first
  with typed `taskdoc:` / `series:` / `lifecycle:` row keys, completed unarchived docs stay visible,
  and `DetailPanel` renders concrete selected documents before lifecycle/series fallbacks. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T15:37+02:00 — Task 17 follow-up route correction: live projection inspection showed
  `analytics.series` is the master surface while leaf rows carry parent `taskName`; the DetailPanel route
  now bridges to the master only for root task identity and otherwise requires projected leaf task docs
  for leaf reader content. Verification metadata pinned until closeout stamps the follow-up code commit.
- 2026-06-24T15:23+02:00 — Task 17 follow-up route impact: clarified the DetailPanel identity rule
  that `taskName` is parent/root-series metadata for leaf lifecycles; direct leaf task documents render
  before the folder-keyed master bridge. Verification metadata pinned until closeout stamps the
  follow-up code commit.
- 2026-06-24T13:59+02:00 — Task 17 follow-up route impact: refreshed the `DetailPanel.tsx` route model
  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.
- 2026-06-24T12:53+02:00 — Task 17 follow-up route impact: refreshed the `DetailPanel.tsx` route model
  for root master rows that select an inferred task-id lifecycle; the panel now uses projected
  enclosure `taskName` to find the folder-keyed `analytics.series` master. Verification metadata pinned
  until closeout stamps the follow-up code commit.
- 2026-06-24T12:37+02:00 — Operations title-overflow fix: refreshed the `LifecycleList.tsx` route model
  for single-line title ellipsis and native hover titles carrying the full task label plus row context.
  Detail lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 route impact: refreshed the `DetailPanel.tsx` route model for
  folder-keyed `analytics.series` master rendering, labelled master sub-task rows, structured
  creation-order sorting, and the new top Progress section in leaf readers. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Detail task-document correction: refreshed the `DetailPanel.tsx` route model
  for promoted leaf lifecycles whose visible title comes from enclosure metadata while readable content
  remains limited to matching JSON task documents. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-24T08:40+02:00 — Operations label fix: refreshed the `LifecycleList.tsx` Route Model bullet
  for enclosure/task-backed row labels, covering promoted fleeting lifecycles that should display the
  leaf enclosure name rather than the stable raw lifecycle id. Detail lives in the `LifecycleList.tsx`
  and `LifecycleList.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-24T06:26+02:00 — Engine Room official-strip aggregation: the route model now records that
  `EngineRoom.tsx` groups official workspace providers by provider label + runtime state, rendering duplicate
  same-state CGCs as counted chips with hover-title repo detail. Detail lives in the `EngineRoom.tsx` and
  `EngineRoom.test.tsx` sidecars. Verification metadata pinned until closeout stamps the official-strip
  aggregation code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: `GateResponder` now routes missing-hosted-session responses to the external operator inbox through `data/operatorInbox`, with queued/error status coverage in `GateResponder.test.tsx`. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T13:45+02:00 — Task 11: added `GateResponder.tsx` / `.test.tsx` and updated the panel route
  model for chat-routed Gate Respond. `DetailPanel` now uses the responder for durable gates and proto
  asks; `LifecycleList` shows gate badges; `Chats` / `SessionList` / `HighlightComposer` carry hosted
  chat lifecycle identity; Hangar and Engine Room diagnostics use the responder as the secondary
  worktree-gate surface. Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-23T13:35+02:00 — No route impact: slice-12 topology render fix — `Topology.tsx` made the constellation canvas absolutely-positioned (out of flow → no ResizeObserver growth loop) and rendered the `Panel` with `fill` (so it fills the slot). Behaviour-preserving layout fix; the panels route model is unchanged.
- 2026-06-23T07:25+02:00 — UI copy rename (user-facing lifecycle → task): refreshed the `LifecycleList.tsx`
  Route Model bullet for the operations panel's "Tasks" copy (header `Tasks · {n}`, empty state `No tasks.`,
  aria-labels "Group tasks by" / "Tasks") and the `DetailPanel.tsx` bullet for its task-facing placeholders
  ("Select a task to inspect…", "No task document bound to this task."). Display copy only — the unit is still
  the `lifecycle` under the hood; the eight-panel route inventory is unchanged. Detail lives in the
  `LifecycleList.tsx` / `DetailPanel.tsx` sidecars. Verification metadata pinned until closeout stamps the
  rename code commit.
- 2026-06-23T04:20+02:00 — Slice 07b polish: added the shared `EmptyStateBackdrop.tsx` panel — a faint,
  effects-gated boomerang-video atmosphere behind centered empty-state text (lifted from the engine-room
  G6 backdrop) — and wired it into `DetailPanel`'s no-selection state (battle cruiser) and `Chats`'s
  no-session state (adjutant); covered by `EmptyStateBackdrop.test.tsx`. Added a Route Model bullet for
  the new shared panel; detail lives in its sidecar + the `DetailPanel` / `Chats` sidecars. Verification
  metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-23T01:40+02:00 — No route impact: slice 07b v1 gives `EventRiver.tsx` its one per-kind treatment (a `read.packet` renders "Read: <basename>" + the read's repo + full-path-on-hover, everything else generic) and adds `EventRiver.test.tsx`; no new panel enters the route inventory and the eight-panel route model this overview describes is unchanged — detail lives in the `EventRiver.tsx` / `EventRiver.test.tsx` sidecars. Verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-22T16:00+02:00 — Route refresh (05o review round): `EngineRoom.tsx` keys its process-map canvas by the store `gen` so a dev-bench scenario switch remounts it cleanly (no cross-scenario overlay bleed), and the right-panel `BootTimeline` now renders a THREE-WAY sequence — Boot / Steady state / Tear-down — with the contract anchor leading the boot order and the abandon/conflict tear-down step states corrected; detail lives in the per-file sidecars under `panels/` and `panels/engine-room/`. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T02:44+02:00 — slice 6g: `DetailPanel` became the task-document **master-series reader** — master overview + clickable sub-task index (pinned in the sticky head + in-section), in-panel drill-in into a slice reader with the back/parent up-link in the sticky panel header, markdown-rendered prose (`grammar/Markdown`), and cross-master "→" links + parent breadcrumb that jump lifecycles (`onOpenLifecycle`). Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T15:59+02:00 — Task 6 slice 6f-1: added `HighlightComposer.tsx` (+ `data/selection.ts`) — a cockpit-wide composer a text selection raises to send a context package (selection + message) into a chat session (single/selector/create-on-Enter + ＋ new chat), reusing the live stdin channel. No silent action. Covered by `HighlightComposer.test.tsx` + `data/selection.test.ts`. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05+02:00 — Task 6 slice 6e-4: the **Chats** view's session registry moved into the `data/sessions` store, and every open session's `Terminal` now stays mounted (inactive ones hidden via CSS) so switching tabs no longer unmounts a live terminal; the backend PTY spawn (`serving/terminal.py`) gained a controlling terminal (`os.login_tty`) so tmux honors resize. Persistence covered by `Chats.test.tsx` + the new `data/sessions.test.ts`. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T06:39+02:00 — No route impact: an engine-room crash fix guards the `landing` read in `engine-room/EnclosureCanvas` (a node without the slice-5h `landing` field no longer crashes); the `panels/` route model this overview describes is unchanged — detail lives in the `engine-room/` overview + sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T05:48+02:00 — Task 6 slice 6e-3: the **Chats** view gained a `SessionComposer` (context injection) docked below the terminal — it sends a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f); covered by `SessionComposer.test.tsx`. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-19T04:38+02:00 — Task 6 slice 6e-2c: the **Chats** view's horizontal session tab strip became a left-rail **`SessionList`** switcher (extracted to a React Aria `GridList` component — single-select = active session, per-row close ✕; `SessionList.test.tsx`), and the per-harness launch buttons now share ＋ Terminal's golden look (the grey ones read as disabled). Refreshed the Chats Route Model bullet + the React Aria note. Verification metadata pinned until closeout stamps the 6e-2c code commit.
- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: the **Chats** view gained per-harness launch buttons — `fetchHarnesses` (`GET /api/harnesses`) renders a button per **detected** harness (Claude Code/Codex/Pi.dev, icon-left/name-right) beside ＋ Terminal; added `Chats.test.tsx` (detection-driven render). Refreshed the Chats Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T18:00+02:00 — No route impact: slice 5h's ledger popover threads `officialLedger` through `EngineRoom` → `EnclosureProcessMap` (resolved from `analytics.ledgers` by repo) for the official coupler; the `panels/` route model this overview describes is unchanged — detail lives in the `engine-room/` overview + the `EngineRoom.tsx` / `EnclosureProcessMap.tsx` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: the **Chats** view became a **create** surface — a "＋ Terminal" control spawns a dashboard-owned shell session via the `POST /api/terminal` opener (no longer attaching to a store lifecycle), rendered as a closable tab. Refreshed the Chats Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:50+02:00 — Task 6 slice 6e-1: added the **Chats** view (`Chats.tsx` + the lazy `Terminal.tsx` xterm wrapper) — the visible Mode B2 surface, the panels' first bidirectional-interactive surface (keystrokes/resize ↔ PTY over the `data/terminal` WebSocket). Updated the Route Model + the near-read-only invariant. Verification metadata pinned until closeout stamps the 6e-1 code commit.
- 2026-06-18T15:00+02:00 — Task 6 slice 6c Part B: `DetailPanel`'s display-only gate banner became the **Gate Review drawer** — the durable gate's decision verbs POST to `/api/actions` via the new `data/actions.ts` (the panels' first write path); the proto-gate `ask` falls back to the display banner. Verification metadata pinned until closeout stamps the 6c Part B code commit.
- 2026-06-17T22:45+02:00 — No route impact: the engine-room visual-parity pass (the 5g G6 backdrop + the restored
  SVG decal layer + the `grammar/Panel` `fill` height fix) is internal to the `engine-room/` route and the
  `grammar/Panel` primitive; the panels route model (the eight panels + their roles) this overview describes
  is unchanged — detail lives in the `engine-room/` + `grammar/` overviews and the `EngineRoom` sidecar.
- 2026-06-17T16:15+02:00 — No content impact: slice 5g G5 (Engine Room live/teardown overlays t12b/t14c/t18 +
  the green=active engine palette + the enclosure-rail scroll fix) is internal to the `engine-room/` route;
  the panels route model (the eight panels + their roles) this overview describes is unchanged — detail
  lives in the `engine-room/` overview + sidecars.
- 2026-06-16T03:50+02:00 — No content impact: slice 5f S5 added the Engine Room header's lifecycle-phase pulse (the `phaseChip` animates while the selected enclosure is in a human-gated landing phase, T12–T18) + `EngineRoom.test.tsx`; the panels route model (the eight panels + their roles) this overview describes is unchanged.
- 2026-06-16T03:35+02:00 — No content impact: slice 5f S3 added `AttentionQueue.test.tsx` (a §9 blocked-start alarm-parity render test — no `AttentionQueue` source change; the panel renders items generically by severity) and the Engine Room T4 promotion morph (internal to `engine-room/`); the panels route model this overview describes is unchanged.
- 2026-06-16T02:30+02:00 — No content impact: slice 5f S1 gave `EngineRoom.tsx` a full-width 3-zone layout (header + stack list | pod stage | boot+diagnostics-right, §4.2); the panels route model (the eight panels + their roles) this overview describes is unchanged — detail lives in the `engine-room/` overview + sidecars.
- 2026-06-16T01:55+02:00 — No content impact: slice 5f S0's Engine Room motion foundations (the `useShouldAnimate` honest-motion gate, SVG conduits, and `worktreeGroup` keying) are internal to the `engine-room/` route — captured in its overview + file sidecars; the panels route model this overview describes is unchanged.
- 2026-06-15T19:35+02:00 — slice 5e: reworked `EngineRoom.tsx` into an enclosure-centered process map
  backed by the new `engine-room/` module (pure `buildEngineRoomModel` + Panda/React Aria
  components: stack list, process map, boot timeline, diagnostics); added the `engine-room/` child route.
- 2026-06-15T17:00+02:00 — Created for slice 5d: all eight panels migrated onto the `Panel` primitive +
  co-located Panda styling, with React Aria `ListBox` (LifecycleList) and `ToggleButtonGroup`
  (pivot). Verification metadata pinned until closeout stamps the 5d code commit.
