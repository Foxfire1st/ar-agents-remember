# dashboard/src/ — Mission-Control Cockpit Frontend Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/`                                 |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`       |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[agents-remember root overview](../../overview.md)

## Purpose

The dashboard frontend is the operator-facing React cockpit. It projects server-composed observer,
task, provider, terminal-catalog, adapter, and control evidence into Operations, Chats, Detail,
Engine Room, file/notes/change-set readers, and supporting panels.

FEUI-L8 deliberately separates strategic ownership:

- [data overview](data/overview.md) — catalog/session state, reliable submit and withdrawal,
  lifecycle cleanup, controls, announcements, and authority boundaries.
- [panels overview](panels/overview.md) — shared panel composition.
- [session-cockpit overview](panels/session-cockpit/overview.md) — the sole full-page Chats product.
- Existing focused child overviews under data, grammar, and panels own their routes. The bounded
  `cockpit/` and `dev/` source slices remain governed here rather than gaining thin overview files.
- [e2e-chats overview](../e2e-chats/overview.md) — the durable, opt-in Chats end-to-end suite
  (260718-CHATS-L5F R7/FB5) is a **sibling** route to `dashboard/src/` (it lives at
  `dashboard/e2e-chats/`, not under `src/`): it boots an isolated real dashboard daemon from the
  worktree and drives the real installed harnesses through this cockpit. Governed by its own route
  overview under the root; linked here for discoverability.

## FEUI-L9R Runtime Truth Repair

Runtime identity crosses this route in three separate ways. The server advertises the fingerprint
of its shipped dashboard while the executing bundle carries its own build-time fingerprint; only a
definite mismatch offers an explicit reload, and absence remains unknown. A new serving boot may
cause exactly one chooser catalog reread and one explicit terminal-socket reattach, but neither is
coupled to SSE loss or a background retry loop. Reattach preserves the mounted xterm and durable
tmux session; transport close alone is not terminal exit.

## FEUI-MX-FIX-2 Authoritative Session Open

Every browser create entrance now converges on `data/terminalOpen.ts`, the sole client for
`POST /api/terminal`. The opener validates exact request/response identity and accepts only the
server row it returns; raw responses that claim harness/control state are contradictions. The
session store commits and broadcasts only an accepted row, while callers display typed failures and
withhold focus, readiness, submit, and contextual delivery. Request-shaped local rows are not an
alternate success path.

The dev cockpit scenarios replace transport with request-matched raw and harness responses through
the real client seam. They remain fixtures governed by this root overview, not a production authority
or a reason to create a separate `dev/` overview for two files.

## Layered Architecture

1. Types mirror server wire/projection shapes; they do not infer missing evidence.
2. Data modules normalize, reconcile, and retain browser projection state around explicit server
   authorities.
3. Grammar primitives provide shared state words, badges, panels, and markdown treatment.
4. Panels compose focused operator surfaces over the shared stores.
5. CockpitShell owns navigation, persistent keep-alive layers, selection routing, and shell-wide
   drivers.

The terminal catalog and adapter/control routes remain authoritative. Browser state may cache and
project them, but is not a replacement conversation-history database.

## Route Model

### Operations

Operations remains the initial destination. Its task list, detail reader, attention, diagnostics,
and contextual RailChat retain their existing contracts. RailChat is useful task-local context, not
a second full-page chat destination.

### Chats

FEUI-L8 removes the legacy Chats/SessionList path and the separate Sessions navigation concept.
CockpitShell exposes one Chats item backed by the persistent session-cockpit layer. That layer keeps
the mechanics built through L1–L7 — role/spawn rail, reliable composer and authoritative pop-back,
interaction answers, lifecycle controls, evidence/capabilities/bus, and status — while adding L8
hardening, accessibility, scenarios, and product-duty transfer.

Since 260718-CHATS-L4 the controlled-session stage body is the structured `ConversationSurface`, not
a PTY: `ChatsStageBody` selects the structured surface (default), the in-stage history library, or
the legacy-raw PTY, and owns the default-off read-only terminal-diagnostics drawer. The exact-turn
interrupt is wired into the WorkingLine as the `conversation.stop` chord. The inspector is
supplementary evidence, closed by default, toggleable, and responsive without overwriting deliberate
user intent. The stage is the primary space.

### Other Full-Page Surfaces

Detail/Operations takeovers, Engine Room, File Viewer, Notes Reader, Change-Set Viewer, and dev-only
design/bench routes retain their existing focused overviews. The L8 split does not introduce another
production view.

## Product Truth And Conversation Boundary (structured renderer landed in 260718-CHATS-L4)

The canonical Chats stage now renders the **structured conversation surface** for controlled
sessions: a harness-neutral grammar over a reconstructable browser projection of the landed L1/L2/L3
adapter-normalized contracts. The controlled runner line-log survives only as the default-off
read-only terminal-diagnostics drawer; legacy raw sessions still host the vendor TUI. This is the one
shared visual message roof across Claude, Codex, and Pi, with visible harness identity and
capability reasons.

The two capabilities are both served and stay distinct: the **active transcript**
([data/conversation](data/conversation/overview.md) + the `conversation/` grammar) and the
**previous-conversation library/index** ([data/conversation-library](data/conversation-library/overview.md)
+ the `conversation-library/` browser). Both obtain normalized history/index/resume from the server
contracts and hold only a projection/cache — no durable browser conversation database (R1). UA-1 is
no longer absent. Two forward constraints remain L5 hardening: interrupt capability gating is
attempt-and-reflect on the L3 evidence until a control-capabilities GET or L1-view refresh lands, and
the measured virtualization/scale baseline plus the E1/E2 environmental faults are enumerated in the
`conversation/` L5-Facing Register.

Harness sub-agents are now a first-class additive layer on both capabilities. The active-transcript
data plane carries per-item agent refs (evidence-bound identity, absent on parent items) and keeps
the operator's agent-lane focus outside the projection so it survives LRU eviction and is
re-validated against the live roster. The library groups sub-agent conversations as child rows
under their parent and renders the server's verbatim `agentsNote` when agent history is (partially)
unavailable. Pending interactions are multiplexed: an additive plural wire slot carries sub-agent
approvals alongside the parent's singular slot, and every attention surface — rail badge,
announcer, seat visual grammar, and the palette's question triage — derives from the combined set
via one shared predicate, so a seat blocked solely on a sub-agent approval never goes dark; the
adapter-bound agent label names who is asking, never a fabricated name.

User submissions, agent-to-agent bus messages, lifecycle/control commands, and adapter-interaction
answers remain distinct paths. The original orchestration failure mode was collisions caused by
routing agent communication through the same paste/input channel as operator typing; the dashboard
must not recreate that coupling.

## Invariants And Boundaries

- Operations is the default and there is exactly one full-page Chats destination.
- The shell owns one catalog poll/reconciler for its lifetime. Views do not create competing feeds.
- Focus/inspection may name a landed row; only a live row owns action routing and reload preference.
- Reliable submit and withdrawal preserve request/epoch identity and never blind-resend or locally
  fake an authoritative result.
- Session open is accepted-response-authoritative: failed requests cause no registry row, focus
  movement, readiness transition, or dependent delivery.
- PTYs stay mounted across focus and transient handoff gaps; ended rows never create a live socket.
- Inspector visibility is optional presentation. Core Chats actions remain usable with it closed.
- State words and evidence remain explicit; absent transport/capability/history facts are not
  inferred.
- No Domain Documentation source is configured; direct source/tests, reviewed task evidence, and
  recovered same-repository history are the authority for FEUI-L8 curation.

## Child Route Onboarding Map

| Child route | Governing overview |
| --- | --- |
| `data/` | [Cockpit state and authority](data/overview.md) |
| `panels/` | [Panel composition](panels/overview.md) |
| `grammar/` | [Grammar](grammar/overview.md) |
| `cockpit/` | File cards governed by this overview; shell ownership starts at [Cockpit.tsx](cockpit/Cockpit.tsx.md). |
| `dev/` | File cards governed by this overview; dev scenario authority starts at [cockpitScenarios.ts](dev/cockpitScenarios.ts.md). |
| root ambient types | [vite-env.d.ts](vite-env.d.ts.md) declares the dashboard build fingerprint consumed by the data layer. |

## Docs References

The curator checked `system/sources.md`; it contains no configured Domain Documentation entries.
The L8 architecture statements were verified from repository-local source/tests, task/reports, and
the recovered same-repository history pack.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found for `dashboard/src`. | Source discovery checked | — |

## Cross-Repo References

No cross-repository implementation is imported as the dashboard authority. Historical Toad/T3
references informed product framing only; current code truth stays in agents-remember.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository implementation source governs this route. | Import and history review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shell navigation, default, persistent layers, and shared drivers. | [cockpit/Cockpit.tsx](cockpit/Cockpit.tsx) |
| State and authority architecture. | [data overview](data/overview.md) |
| Panel composition. | [panels overview](panels/overview.md) |
| Sole Chats route, deletion map, and future boundary. | [session-cockpit overview](panels/session-cockpit/overview.md) |
| Dev scenario authority and end-to-end states. | [dev/cockpitScenarios.ts](dev/cockpitScenarios.ts) |

## 260718-CHATS-L5I Current Route Impact

The cockpit now treats a focused chat or terminal as a persistent operator surface rather than disposable tab content: switch and hidden-view transitions preserve mounted identity, scroll/selection/geometry state, and only resume visible-only work when appropriate. Its global data consumers also adopt bounded stream/watchdog, single-flight, timeout, build-identity, and wake-lock behavior. Detailed mechanics remain owned by the existing `data/`, `panels/`, and nested session-cockpit overviews; this route records only the shared frontend consequence.

## Update History

- 2026-07-26T18:30+02:00 — 260718-CHATS-L7 curator: added one paragraph to the Product Truth And
  Conversation Boundary section covering the sub-agent surface — additive per-item agent refs and
  the LRU-surviving agent-lane focus in the conversation data plane, library child rows plus the
  verbatim `agentsNote`, and multiplexed pending interactions feeding all attention chrome through
  one shared predicate with the adapter-bound agent label. No route composition or authority model
  changed; detail lives in the `data/` and `panels/session-cockpit/` child overviews. Verification
  metadata remains pre-commit; closeout re-stamps.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the shared dashboard/src route for the whole frontend change without modifying nested overview ownership. Verification metadata remains pre-commit.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: added a discoverability pointer to the new
  sibling [e2e-chats overview](../e2e-chats/overview.md) — the durable, opt-in Chats E2E suite
  (R7/FB5) that boots an isolated real dashboard daemon from the worktree and drives the real
  installed harnesses through this cockpit. The suite lives at `dashboard/e2e-chats/` (a sibling of
  `src/`, governed by its own route overview under the root); the `dashboard/src/` route model is
  otherwise unchanged. Verification metadata pinned; the L5F change is uncommitted and closeout
  re-stamps.
- 2026-07-21T05:30+02:00 — No route impact: the `dashboard/src` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`) is unchanged by 260718-CHATS-L5P (cockpit chrome visual
  polish, PASS-WITH-NOTES; dashboard-only, zero backend edits). The two app-wide `dashboard/src/`-direct
  CSS/token changes are captured at the child/sidecar level, not in this route body (which has no styling
  section): (1) `index.css` gained an unlayered `word-break: normal` root override on `html, body,
  [data-view="sessions"]` that neutralizes `@webtui/css`'s inherited `word-break: break-all` app-wide
  (RV-1, LOAD-BEARING — a third-party scoped reset in a lower layer silently defeated every
  component-level `overflow-wrap` patch; the test is computed-value verification; raw-id spans keep
  explicit `break-all`) — recorded in the `index.css` sidecar and the `panels/session-cockpit/` overview's
  "Cockpit chrome conventions" section; (2) `styles/tokens.css` + `panda.config.ts` gained the `well`
  (`#070b0f`) terminal-well token (the xterm pty inset, FB7.1) — recorded in the `tokens.css` sidecar. The
  regenerated `package_data/dashboard/` bundle is shipped output governed by the mcp overview's sync
  mechanism, not an mcp source contract. Verification metadata unchanged.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 route impact (structured Chats renderer; reviewer FINAL
  PASS, 26/26 findings closed): `data/` gains the reconstructable `conversation/` and
  `conversation-library/` projection child routes; `panels/session-cockpit/` gains `ChatsStageBody`
  and the `conversation/` + `conversation-library/` grandchild renderer routes (structured
  `ConversationSurface` is the controlled-session default; the runner line-log is demoted to the
  default-off read-only terminal-diagnostics drawer + legacy-raw body; the exact-turn interrupt rides
  the WorkingLine as the `conversation.stop` chord). Rewrote the Product-Truth/Conversation-Boundary
  and Chats sections: UA-1 history/index/resume is now landed as a reconstructable projection with no
  durable browser conversation index. Additive edits also touched `SessionsView`/`WorkingLine`/
  `ChatContextBar`/`PtySurface`/`SessionComposer`/`data/keymap` (detail in those sidecars). The
  synchronized `package_data/dashboard/` bundle is regenerated shipped output governed by the mcp
  overview's sync mechanism, not an mcp source contract. Verification metadata remains pinned pending
  L4 candidate closeout.

- 2026-07-18T15:22+02:00 — FEUI-MX-FIX-2: recorded the sole authoritative browser opener,
  accepted-server-row-only materialization, contradiction handling, and request-matched dev fixture
  seam; corrected route ownership so bounded cockpit/dev files remain governed here. Verification
  metadata remains pinned pending candidate closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: added bundle comparison, bounded boot-owned reread/reattach,
  explicit reload, and durable-session transport boundaries. Verification metadata remains pinned
  pending candidate closeout.

- 2026-07-18T07:22+02:00 — 260715-FEUI-L8 strategic refactor: split data authority and canonical
  Chats detail into focused child overviews, recorded one Chats/Operations-default product truth,
  and preserved the future adapter-normalized conversation/history boundary without claiming UA-1.
  Metadata remains pinned to the leaf base.

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 route impact: the existing
  `panels/session-cockpit/` child route gains the stable-mounted three-pane inspector, complete
  evidence/capability/Bus surfaces, sender-only reverse reply, shared accessible virtualization,
  and honest StatusLine; `types/projection.ts` gains optional pickup owner/redelivery facts and
  `test/fixtures/busScenarios.ts` adds coherent/legacy wire cases. Detailed organization remains
  in the focused child overview rather than further loading this packed root file. Verification
  metadata remains pinned to the leaf base until closeout.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: replaced stub/paste current-state claims with
  the shared CodeMirror reliable-submit path, central evidence fold, epoch/request transport,
  authoritative status/withdraw/pop-back, revision-safe recovery, and bounded retention. Recorded
  `dashboard/src/data` route pressure for the final master route-architecture pass rather than
  inventing a non-mirrored route during this leaf.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 route impact (live set controls; final reviewer PASS
  after three fix rounds): `data/` gains the exact-session capability, five-state acceptance,
  serialized pair, sole I/O driver, chip/copy, and announcer modules; the cockpit store gains
  typed snapshot/echo/route/pair evidence; `panels/session-cockpit/` gains the live control,
  accepting chip, ledger/rail attention, persistent background toasts, queued hint, and dual live
  regions; capability fixtures gain clamp/queue/unknown readback sequences. Six nonblocking sev-4
  observations remain preserved in file cards. Verification metadata is pinned to the contract
  base until code commit.
- 2026-07-17T06:25+02:00 — 260715-FEUI-L3 route impact (capability catalog client and launch
  flow; review FINAL PASS after two fix rounds; 66 files / 753 tests green): `data/` gains the
  launch layer — `capabilityCatalog.ts` (memory-only envelope store, drop-on-error, verbatim
  errors, honest refresh semantics), `launchEvidence.ts` (the pure tier machine; Claude launch
  pairs never readback), `launchFlow.ts` (pure launch machines + the classifying open client),
  all + suites; `types/` gains `harnessCapabilities.ts` + `terminalOpen.ts` (the capability and
  open wire mirrors; `terminalCatalog.ts` untouched); `grammar/` gains `EvidenceBadge.tsx`
  (+ test); `test/fixtures/` gains the R3 contract pack (`capabilityEnvelopes`,
  `controlMessages`, `openResponses`) + `test/contractCapabilities.test.ts`;
  `panels/session-cockpit/` gains `LaunchFlow` + `FailedLaunchBanner` and derives the R7
  evidence tier from control-state truth (see that overview); `data/terminal.ts` extends the
  open POST with the model/effort selection. Upstream ask: an operator retire actor identity if
  provenance-recording retire is wanted from the dashboard. Verification metadata pinned to the
  leaf base until closeout stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 route impact (PTY stage surface, structured
  interactions, session lifecycle actions; review FINAL PASS after a 1×sev-3 + 5×sev-4 fix
  round, all CLOSED): `data/` gains the interaction/lifecycle layer — `interactionAnswer.ts`
  (the SOLE gate-channel answer path), `sessionLifecycle.ts` (detailed terminate/cleanup +
  residual notice store + the focus-independent retire-residual sweep), `ptyHarvest.ts`
  (client-side legacy-raw OSC/bell/title harvesting), all + suites; `actions.ts` gains
  `postGateDecisionDetailed`, `terminal.ts` the additive `onSocketState`;
  `panels/session-cockpit/` gains PtySurface/InteractionBar/WorkingLine/StopResidualNotes/
  lifecycleCopy (see that overview); `panels/Terminal.tsx` gains additive optional props (DOM
  default, lazy webgl escalation, live screenReaderMode, harvesting hooks, named `role="group"`
  landmark); `test/fixtures/catalogRows.ts` appends the `L6_*` rows (FLEET byte-identical);
  `dev/` gains `/dev/pty-bench` (`PtyRenderBench.tsx` + `lineLogFixture.ts`; driver at
  `dashboard/e2e/ptyRenderBench.mjs`). Two exact-pinned deps entered `package.json`:
  `@xterm/addon-webgl` (lazy escalation chunk, loaded only if the renderer constant flips) and
  `@xterm/addon-serialize` (bench probe only — evaluated cheap-enough, deliberately NOT adopted
  in product code until an LRU cap or the pane-freeze repaint package defines the discipline).
  Verification metadata pinned to the leaf base until closeout stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 route impact (session data layer, rail, and stage
  container; review FINAL PASS): `data/` gains the sessions-cockpit data layer —
  `catalogPoll.ts` (the poll driver hoisted OUT of Chats; Chats is now a consumer),
  `seatEvents.ts` (the gated `/api/events` seat reconciler; poll stays authoritative),
  `stateGrammar.ts` (the one dot grammar + 2.4 s pulse ruling), `railModel.ts` (the ruled
  hierarchy/attention/joins), `sessionCockpitStore.ts` (per-seat honesty-invariant client state),
  all + suites; `types/` gains `terminalCatalog.ts` (the full catalog wire mirror,
  `data/terminal.ts` re-exports); `test/fixtures/` is the new shared-fixture home
  (`catalogRows.ts`); `panels/session-cockpit/` gains the rail/stage/inspector components (see
  that overview); `sessions.ts`/`stream.ts`/`commands.ts`/`index.css` extended as their sidecars
  describe; plus a reviewer-accepted one-line defensive fix in `panels/file-viewer/FileViewer.tsx`.
  Open sev-3 developer ruling: status-chip vocabulary width (`stale`/`exited`/`retired`/
  `starting`). Verification metadata pinned to the leaf base until closeout stamps the L2 code
  commit.
- 2026-07-17T00:30+02:00 — 260715-FEUI-L1 route impact (view shell, WebTUI spike, keyboard/palette
  foundation): the cascade gained the `webtui` layer slot (S1, OQ-D = adopt — `styles/webtui.css`
  is the one mapping file, build-time scoped under `[data-view="sessions"]`, spike assertions kept
  in `test/webtuiSpike.test.ts`); `cockpit/Cockpit.tsx` registered the full-bleed keep-alive
  **Sessions** view; `panels/` gained the **`session-cockpit/`** child route and `data/` gained
  `commands.ts`, `sessionLayout.ts`, and the **`keymap/`** child route (the PTY reserved set with
  the R6 chord replacement Ctrl+Alt+[ / ] → Ctrl+Alt+PageUp/PageDown and five-source verification
  records); `styles/tokens.css` gained `--muted`. Four exact-pinned deps entered `package.json`
  (`@webtui/css@0.1.9`, `cmdk@1.1.1`, `tinykeys@4.0.0`, dev `postcss-prefix-selector@2.1.1`).
  Detail lives in the `panels/session-cockpit/` + `data/keymap/` overviews and the touched
  sidecars. Verification metadata pinned to the task base until closeout stamps the L1 code
  commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-12T18:00+02:00 — 260712-TRH-L7: paired the landing-freshness body update with this history entry; projection landing refs remain visible and age-labeled when stale, while Engine Room motion is limited to observed refs and remote observation stays server-side.

- 2026-07-12T16:45+02:00 — 260712-TRH-L1 reopened-memory refresh: clarified stable path/revision
  request identity, separate body storage plus current-summary merge, late-response discard,
  terminal failure semantics, composition regression coverage, and the pre-existing scalar
  staleness window. Verification metadata remains blank until closeout stamps the code commit.

- 2026-07-12T13:36+02:00 — No route impact: 260712-TRH-L2 body review confirms the changeset refinements remain inside the existing `data/changeset` and `panels/changeset` surfaces; the `dashboard/src` route model and top-level organization are unchanged. Verification metadata remains pinned until closeout.
- 2026-07-12T12:55+02:00 — No additional route impact from 260712-TRH-L2: its changeset refinements stay inside the existing `data/changeset` and `panels/changeset` surfaces; the dashboard/src route model and top-level organization remain unchanged. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-12T12:07+02:00 — 260712-TRH-L1 dashboard-source route impact: added the focused
  `data/useTaskDocumentBody.ts` state seam and documented complete visible task content as the first
  reader request priority. Notes and change-set counters resume after success or fallback; no new
  frontend route was created. Verification metadata remains pinned until closeout.

- 2026-07-10T21:59+02:00 — 260707-HFX2-L21 dashboard-source route impact: documented the
  persisted, bounded Chats sidebar and its pointer/keyboard separator. The behavior stays inside the
  existing `panels/` route and preserves terminal working width without animating direct manipulation.
  Verification metadata remains pinned until closeout.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 dashboard-source route impact: documented explicit
  role claim, binding-first client identity, pair-scoped assignment/rendering, and the
  source/build/serve package boundary. Verification metadata remains pinned until closeout.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16 route impact: documented repo-qualified sprint
  grouping, complete spawn-edge forest rendering, bounded/hover-complete rail rows, honest on-demand
  task-body fallback, and single-rendered implementation steps. No new route was created.
  Verification metadata stays pinned until closeout stamps the eventual L16 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6 route impact: added the on-demand task-document data
  adapter and `bodyRevision` wire field; full reader bodies no longer ride the always-on projection.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T14:05+02:00 — No route impact: 260707-HFX2-L11 (landed chat archive + group cleanup)
  extends `data/{sessionGroups,sessions,terminal}.ts` (new `"landed"` status, landing provenance
  fields, `cleanupLandedTerminalSessions()`) and `panels/{Chats,SessionList,Terminal}.tsx` (landed
  archive group, group-cleanup control, read-only landed terminals). This is data-shape and panel
  behavior content, not a change to this route's own module layout or routing; per-file detail lives
  in the already-updated `dashboard/src/data/` and `dashboard/src/panels/` sidecars/sub-overview.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 route impact (dead-seat storm observability, R6):
  `SupervisorHeartbeat` now includes pending/redeliverable inbox backlog counts and last sweep
  duration; `data/store.ts` compares those fields in `heartbeatEquals`; and
  `cockpit/Cockpit.tsx` renders them in the top-bar `SupervisorHeartbeatBadge` beside heartbeat age.
  Verified with dashboard typecheck and `src/data/store.test.ts`. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 route impact (supervisor sweep, R5): `cockpit/Cockpit.tsx`
  gains `SupervisorHeartbeatBadge` in the `TopBar` (beside `ServingBuildStamp`); `data/store.ts`
  gains the `supervisorHeartbeat` field, deliberately excluded from the change-gate `unchanged`
  check so the live tick age still applies on a content-unchanged reconnect; `types/projection.ts`
  gains the `SupervisorHeartbeat` type and optional `WorkspaceProjection.supervisorHeartbeat?` — a
  second app-injected, non-`projection.py` field alongside `servingBuild?`. No route/component-tree
  shape change beyond the one new top-bar badge. **Known limitation (builder-flagged, unverified
  in this environment):** these TS changes are unverified by `tsc`/a build (no `dashboard/
  node_modules` installed); a follow-up should run the dashboard's own build/test suite once
  available. Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-07T23:55+02:00 — 260707-HFX-L6 route impact: the `data/sessionGroups`
  model and terminal data mirror now include architect/curator role provenance so Chats grouping and
  row chips can represent the split developer-facing architect, backend orchestrator, and curator
  closeout seat without changing the cockpit route structure. Verification metadata pinned until
  closeout stamps the HFX-L6 commit.
- 2026-07-07T14:00+02:00 — agent-orchestration L17 route impact: `panels/` gains the **`notes-reader/`**
  child route (the Notes Reader takeover, reusing the File Viewer `DualPane` over the unchanged L9
  `/api/notes/*` API), and `cockpit/Cockpit.tsx` gains a second full-bleed takeover hosting it (retained
  mounted-hidden after Back so selection survives back/forward). `panels/TaskNotes.tsx` becomes the compact
  entry surface (inline reader retired) and `panels/LifecycleList.tsx`'s gate chip drops the wait-loop `ask`
  fallback. Details in the `panels/` + `panels/notes-reader/` overviews and the touched sidecars.
  Verification metadata pinned until closeout stamps the L17 commit.
- 2026-07-07T05:38+02:00 — 260703-L15 route impact (long-session memory): `data/` gains
  `servedAges.ts` (+ suite; the volatile-age mirror, stable equality, arrival anchors, display
  ticker); `store.ts` apply paths became identity-preserving/change-gated (zero writes on idle
  payloads) and carry `servingBuild`; `types/projection.ts` mirrors the app-injected
  `ServingBuild`; `cockpit/Cockpit.tsx` renders the muted serving-build stamp; the four
  age-display panels advance served ages locally. NOTE: `data/` has no route overview of its own —
  this file governs it directly, so the genuine body update lives here (same call as L14).
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:57:36+02:00 — 260703-L14 route impact (visual hierarchy + chat grouping): `data/` gains
  `sessionGroups.ts` (+ unit suite, the G1 command-tree derivation) and `taskHierarchy.ts` gains the
  orchestration-command helpers; `grammar/` gains `RankBadge.tsx` (+ test, the V4 chevron insignia);
  `types/projection.ts` mirrors `TaskDocNode.orchestrates?`; `styles/tokens.css` gains the six
  gold/purple tier vars (mirrored as Panda tokens in `panda.config.ts`). Behavior detail lives in the
  `panels/`/`grammar/` overviews and the changed sidecars. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T15:40+02:00 — No route impact: 260703-L12's dashboard change is content-only inside `panels/` — `flowModels.ts` gains the STRATEGIST model (8-model census) and loop-doctrine lines, `FlowTab.test.tsx` grows to 11 cases; the dashboard/src route model, data layer, and grammar this overview describes are unchanged — detail lives in the `panels/` overview and the two file sidecars. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T12:10+02:00 — No route impact: 260703-L10's dashboard change is a single phase-label string inside `panels/flowModels.ts` (designer `frame` → `reframe`); the dashboard/src route model, data layer, and grammar this overview describes are unchanged — detail lives in the `panels/` overview and the `flowModels.ts` sidecar. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-06T03:25+02:00 — 260703-L11 route impact: `data/selectors.ts` gains the shared
  `hasLiveWorktree` tasks-surface visibility rule and `types/projection.ts` mirrors the new required
  `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags; `dev/fixtures.ts` and the
  `topology`/`panels` test fixtures default them `true`. The Hangar/LifecycleList behavior change is
  documented at the panels route. Verification metadata pinned until closeout stamps the L11 commit.
- 2026-07-06T03:00+02:00 — 260703-L9 route impact (friction F-M): `data/` gains `notes.ts` (+ unit
  suite), the third serving read client — `listNotes`/`readNote` over the shared `getJson`/`qs`
  transport plus the pure `resolveNoteReference` — feeding the new task-reader notes view
  (`panels/TaskNotes.tsx`); the `data/` route-model bullet now names it beside `files.ts` and
  `changeset.ts`. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-05T19:55+02:00 — No route impact: the dashboard/src route model is unchanged — the cycle-7 manager-raise-node enclosure addition is documented at the panels route (260703-L8 cycle 7).
- 2026-07-05T19:10+02:00 — No route impact: the dashboard/src route model is unchanged — the cycle-6 seam-node prose update is documented at the panels route (260703-L8 cycle 6).
- 2026-07-05T18:24+02:00 — No route impact: dev-only index label aligned with the converged canvas (DevApp.tsx); no production route or component change (260703-L8 cycle 5).
- 2026-07-05T16:32+02:00 — No route impact: the dashboard/src route model is unchanged — the FlowTab redraw is documented at the panels route (260703-L8 cycle 4).
- 2026-07-04T12:31+02:00 - L3 route impact: dashboard data/types now mirror
  agent-to-agent inbox metadata and hosted-delivery state for `AgentPickupNode`
  and `/api/operator-inbox`. Verification metadata pinned until closeout stamps
  the L3 commit.
- 2026-07-04T10:05+02:00 — 260703-L0 route impact (small): `dev/` gained the `/dev/flows` lifecycle-design
  canvas route (DevApp mounts the generalized `panels/FlowTab` over the new `panels/flowModels.ts` registry);
  detail lives in the `panels/` overview and the file sidecars. Verification metadata pinned until closeout
  stamps the L0 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: reopened leaves render as planned doc rows via the stable leaf id; abandoned enclosures leave the active operations rows (see panels/LifecycleList).
- 2026-07-02T20:15+02:00 — L8 route impact (small): `data/selection.ts` selections now carry the
  qualified `leafKey` when anchored inside a task reader marked `data-task-leaf-key`, and
  `cockpit/Cockpit.tsx` threads `viewedLeafKey` + `leafChatActive` into `HighlightComposer` so the
  direct leaf-chat paste path can resolve its target. The route structure is otherwise unchanged;
  behavior detail lives in the `panels/` overview and file sidecars. Verification metadata pinned until
  closeout stamps the L8 commit.
- 2026-07-02T17:04+02:00 — No route impact: L9 extends the existing `data/sessions.ts` and
  `panels/Chats.tsx` / `RailChat.tsx` routes so hosted chats can move between durable leaves after
  creation, and open dashboard tabs rehydrate `"leaf"` catalog invalidations or polling refreshes. The
  `dashboard/src/` route model is unchanged; detail lives in the `panels/` overview and changed sidecars.
  Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — No route impact: the reopened-L6 wheel/paste fixes stay inside `panels/` and
  `data/`. `panels/Terminal.tsx` yields wheel to xterm mouse reporting when the app tracks the mouse;
  `data/terminal.ts` gained `pasteAndConfirm` (echo-confirmed, boot-deadline-retried draft paste) and
  `data/sessions.ts`'s `pasteDraftToSession` delegates to it. The `dashboard/src/` route model is
  unchanged. Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-02T15:03+02:00 — No route impact: the L6 alternate-buffer wheel follow-up stays inside the
  existing shared `Terminal` wrapper under `panels/`. Normal-buffer scrollback still uses xterm viewport
  scrolling, while alternate-buffer hosted agent TUIs receive PageUp/PageDown wheel steps instead of
  xterm Up/Down history input. The `dashboard/src/` route model is unchanged. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-07-02T13:16+02:00 — Reopened L6 route impact/no route impact: the follow-up stays inside the
  existing `cockpit/` + `panels/` + `data/` model, but `data/sessions.ts` now separates leaf-context
  draft paste from submit so `RailChat` can place context in the selected hosted chat without pressing
  Enter. Chat scrollback remains documented in the `panels/` overview and `Terminal.tsx` sidecar. The
  `dashboard/src/` route model is unchanged; verification metadata pinned until closeout stamps the L6
  follow-up commit.
- 2026-07-01T01:19+02:00 — No route impact: L6 adds bind-time leaf context handoff inside the existing
  `cockpit/` + `panels/` + `data/` model. `CockpitShell` passes `analytics.engineProcesses` to the existing
  right-rail `RailChat`, and `RailChat` injects a projected leaf context package when a chat is started on a
  displayed leaf or a free chat is successfully attached. The `dashboard/src/` route model is unchanged;
  detail lives in the `panels/` overview and the `Cockpit.tsx`/`RailChat.tsx`/`RailChat.test.tsx` sidecars.
  Verification metadata pinned until closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — No route impact: L5 (Sidebar chat) adds leaf-keyed attachment + a right-rail River⇄Chat
  toggle. The change lives in `cockpit/Cockpit.tsx` (a `railView` toggle + `selectedLeafKey` derivation),
  `data/` (`sessions.ts` leaf binding, `terminal.ts` `attach-leaf` client, `taskIdentity.ts` leaf-key
  helpers), and `panels/` (the new `RailChat.tsx`, plus `Chats.tsx`/`SessionList.tsx` leaf-attach + name
  label) — all within the already-documented `panels/` route. The `dashboard/src/` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged; detail lives in the `panels/` overview
  and the `cockpit/`/`data/`/`panels/` file sidecars. Verification metadata pinned until closeout stamps
  the L5 commit.
- 2026-06-29T23:00+02:00 — No route impact: L4a refines the already-documented `panels/changeset/`
  sub-route (leaf committed/working change-set views, a diff-highlight rectangle, a live working-view
  auto-refresh), adds the doc-reader change-set bars in `panels/DetailPanel.tsx` + leaf helpers in
  `data/changeset.ts`, and changes `cockpit/Cockpit.tsx` so the change-set takeover overlays (rather than
  replaces) the railed body so the back link returns to the leaf it was opened from. The `dashboard/src/`
  route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged; detail lives in the `panels/`
  + `panels/changeset/` overviews and the `Cockpit.tsx`/file sidecars. Verification metadata pinned until
  closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — No route impact: the L4 follow-up refines the already-documented `panels/changeset/` sub-route — the series/master change-set is now the NET inspectable diff (was accumulated-only) — plus shared code-view polish (`codemirrorTheme` comment/punctuation readability, `DiffPane` split-diff scroll). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged; detail lives in the `panels/changeset/` overview + the file sidecars. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — Operations Integration L4 (Change-Set Viewer) route impact: `cockpit/Cockpit.tsx`
  gained a `changeSet` **TAKEOVER** (a `DetailPanel` change-set button replaces the railed Operations body
  with a full-bleed `<ChangeSetViewer>`; a back link restores it); a new **`panels/changeset/`** sub-route
  lands — the Change-Set Viewer screen (a read-only `@codemirror/merge` diff over the L3 `/api/changeset/*`
  API, reusing the L2 `FilePane`); and `data/` gains the `changeset.ts` serving client (sharing `files.ts`'s
  `getJson`/`qs`/`FilesApiError`). Detail in the `panels/` + new `panels/changeset/` overviews and sidecars.
  Verification metadata pinned to the task base until closeout stamps the L4 code commit.
- 2026-06-29T09:06+02:00 — Operations Integration L2 (File Viewer) route impact: `cockpit/Cockpit.tsx`
  registers a new full-bleed **File Viewer** view (`"files"` in the `View` union + the `fullBleed` set, a
  `VIEWS` tab between Operations and Engine Room), **kept mounted** (CSS-hidden) like Chats so its
  repo/scope/open-file/tree state survives a tab switch; and a new **`panels/file-viewer/`** sub-route
  lands — a read-only code+onboarding dual-pane (two Headless Tree explorers, a read-only CodeMirror 6
  pane, bidirectional code↔onboarding pairing) that is the first consumer of the L1 read-only files API,
  plus the reusable `FilePane`/`DualPane` for the L4 Change-Set Viewer. Detail in the `panels/` + new
  `panels/file-viewer/` overviews and sidecars. Verification metadata pinned until closeout stamps the L2
  code commit.
- 2026-06-28T16:17+02:00 — Task 35 route impact: `panels/LifecycleList.tsx` reopen-task nesting — the
  Operations list admits a reopened leaf's suffixed enclosure by shared lifecycle + suffixed-leaf shape and
  nests doc-less enclosure-backed runtime rows under their master, ending the standalone-phantom row. No
  other `dashboard/src` route structure changed. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: the raw Event River store (`data/store.ts`) now keeps a
  bounded **sliding window** of the newest ~2000 rows (memory-bounded rather than the unbounded
  session-growth the prior text described), which `EventRiver` virtualizes over so there is still no hard
  display cap. Refreshed the `data/` Route Model bullet's event-store description. Verification metadata
  pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: the `topology/` view became an active-enclosure constellation
  (lifecycle/task rim removed, each enclosure folds in its 1:1 lifecycle, `activeTopologyInputs` filters to
  the served active set, basename `groupKey` join fixes the latent task-12-S1 provider join); `types/projection.ts`
  mirrors the new required `activeWorktreeGroups`, and `data/store.ts` + `data/stream.ts` thread it through.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: the cockpit now hides the former Lifecycle Flow
  tab, the raw Event River waits for the backend `ready` event before rendering an empty history, and
  frontend storage no longer truncates received Event River rows. Attention queue dismiss/clear actions
  optimistically suppress visible rows while the backend physically removes or acknowledges the source,
  including targetless actionable-drift notices. Verification metadata pinned until closeout stamps the
  task-29 code commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: projection types now mirror the provider boot-node
  `missing` state, letting Engine Room render expected-but-absent provider roles distinctly from
  configured/observed provider rows. Operations task grouping also accepts the authored task-document id
  when matching a leaf document to its enclosure, so leaf 31 stays nested under the browser-dashboard
  master even when the task JSON file stem is descriptive. Verification metadata pinned until closeout
  stamps the task-31 code commit.
- 2026-06-27T18:43+02:00 — Task 26 route impact: `cockpit/Cockpit.tsx` registers a new full-bleed
  **Lifecycle Flow** view — `"flow"` in the `View` union + the `fullBleed` set, a `VIEWS` tab second
  after Operations, and a `ViewBody` case rendering `<FlowTab />` from `panels/FlowTab.tsx`. FlowTab is
  a /dev-stage diagnostic visualizing the build-job lifecycle (the task-27 next-step engine spec); the
  production bundle was not rebuilt this task. Verification metadata pinned until closeout stamps the
  task-26 code commit.
- 2026-06-27T03:04+02:00 — Task 22 follow-up: `data/sessions.ts` removed the hidden-label reservation
  state with the Hide UI path, and terminal catalog create/terminate broadcasts now carry the changed
  `sessionId` so other tabs can remove ended rows deterministically.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: `data/sessions.ts` now broadcasts backend-persisted
  terminal catalog create/terminate invalidations across browser tabs, while `data/terminal.ts` exposes a
  nullable catalog fetch so receivers can distinguish empty success from fetch failure.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: `data/sessions.ts` now allocates session labels from the
  lowest available live per-prefix ordinal, then releases End/terminated labels.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: the Chats view now mounts restored sessions on first
  selection and keeps visited terminals mounted while hidden, avoiding broken hidden xterm hydration for
  restored Claude/Codex sessions after refresh without losing tab-switch buffers.
- 2026-06-26T23:15+02:00 — Task 22 route impact: the Chats data/panel route now hydrates
  dashboard-owned terminal sessions from `/api/terminal/sessions`, tracks running/exited/terminated
  catalog status, restores the last active session, and routes explicit End through backend terminate.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: frontend projection types mirror
  `SeriesNode.seriesTokenTotal`, and DetailPanel master readers display the server-composed aggregate.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T19:40+02:00 — Task 20 reopened route impact: `data/taskIdentity.ts`
  now participates in Event River lifecycle-label fallback by exposing direct
  task-document title labels for lifecycle-only history rows. Detailed behavior
  lives in the data helper and panel formatter sidecars. Verification metadata
  pinned until closeout stamps the reopened task-20 code commit.
- 2026-06-26T18:23+02:00 — No route impact: task 20 adds Event River readable-feed
  formatting inside `dashboard/src/panels/` (`EventRiver.tsx`, `eventSummary.ts`, and tests). The
  `dashboard/src/` route model remains cockpit/grammar/panels/data/dev; detailed behavior lives in
  the panels overview and file sidecars. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: frontend data/panels now support gate-id-only Clear for stale gate rows while keeping normal decisions lifecycle-targeted.
- 2026-06-25T13:20+02:00 — Task 23/24: frontend route now includes gate dismissal, attention clear, inbox-warning deletion, and `AgentPickupNode` projection types.
- 2026-06-25T07:26+02:00 — Task 19 gate interaction polish: `dashboard/src/` now treats Gate Respond as
  three explicit paths — Yes/No record targeted durable gate decisions through `data/actions`, while Chat
  remains message-only through hosted chat or the operator inbox. The data route also adds
  `actions.test.ts` coverage. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:11+02:00 — Task 17 route correction: `TaskDocNode.id` is now mirrored in the projection
  types and used by `data/taskHierarchy.ts`, `LifecycleList`, and `DetailPanel` as the authored leaf
  display number; parent sub-task `number` remains fallback data. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T18:02+02:00 — Task 17 route correction: `data/taskHierarchy.ts`, `LifecycleList`, and
  `DetailPanel` now use structured task metadata for visible leaf labels while keeping creation
  metadata as the ordering source. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Task 17 Operations hierarchy route update: added `data/taskHierarchy.ts` as
  the shared structured parent-series helper behind BY REPO leaf indentation and direct leaf parent
  backlinks. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 Operations route correction: dashboard selection is now typed
  (`taskdoc:` / `series:` / `lifecycle:`), task documents can be listed/read before lifecycle binding,
  and projection types mirror optional `TaskDocNode.lifecycleId`. Detail lives in `data/taskIdentity.ts`,
  `LifecycleList.tsx`, `DetailPanel.tsx`, and `types/projection.ts` sidecars. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 route impact: projection types now mirror task/series
  `createdAt`, `SeriesNode`, and `Analytics.series`, and dev fixtures default `series: []` in the
  analytics shape. DetailPanel-specific behavior is recorded in the panels overview and sidecars.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Data route addition: added `taskIdentity.ts` to the route model as the
  shared lifecycle label/direct-task-document helper used by Operations and Detail. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: dashboard projection types now carry explicit `enclosureId`, `leafId`, and `taskRoot` fields, and Engine Room renders the projected integration/source branch instead of hardcoding `main`. Detail lives in the `types/projection.ts`, engine-room fixture, and `EnclosureCanvas.tsx` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:31+02:00 — Clarified Task 12 S2 topology wording: repo-scoped GrepAI dots come from
  addressable `targetRepos` inside one aggregate provider instance, while worktree providers remain
  bound by `worktreeGroup`. Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2 route impact: `topology/model.ts` now includes repo-covered
  workspace providers in the repo ring and parents provider satellites by `worktreeGroup`, then `repoId`,
  then workspace core; `types/projection.ts` clarifies the binding comments and `model.test.ts` covers
  repo-scoped parenting plus precedence. Verification metadata pinned until closeout stamps the S2 code
  commit.
- 2026-06-23T16:02+02:00 — Task 12 S1 route impact: `topology/model.ts` now records worktree
  groups while building topology nodes and parents worktree-scoped providers to the owning worktree
  node, with fallback/workspace providers staying on the workspace core. `topology/model.test.ts`
  adds pure-model coverage for matching, fallback, and workspace-provider behavior. No backend
  projection shape change; per-repo main-stack provider placement remains deferred to S2.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: `data/operatorInbox.ts` joined the data route and `GateResponder` now falls back to `POST /api/operator-inbox` for lifecycles without a hosted chat session, preserving the agent-owned gate-release model. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T14:31+02:00 — Task 11 route impact: `dashboard/src/` now treats gate response as a
  hosted-chat direct-inject surface instead of the old developer gate-decision `/api/actions` drawer.
  `cockpit/Cockpit.tsx` threads selected lifecycle identity into Chats and HighlightComposer,
  `data/sessions.ts` owns lifecycle-tagged hosted sessions, and `panels/GateResponder.tsx` is the shared
  Respond control used by DetailPanel plus secondary engine-room/Hangar gate surfaces.
- 2026-06-23T13:35+02:00 — No route impact: slice-12 topology render-robustness — `topology/constel.ts` gained a file sidecar (the renderer now paints synchronously on resize/update, not rAF-only) and `panels/Topology.tsx` made the canvas absolutely-positioned + the `Panel` `fill`. Behaviour-preserving render/layout fixes within the existing `dashboard/src` route model; no structural change.
- 2026-06-22T11:00 — No route impact: slice 05o T7B–T18's `dashboard/src/`-direct changes are `dev/scenarios.ts`
  gaining six more failure-mode timelines (`seed-fault` T9B, `reindex-reroute` T9C, `provider-block` T7B,
  `live-sync` T12B, `integration-conflict` T14C, `abandon` T18) and `types/projection.ts` gaining the
  `refusedPolarity` edge field + a `refused` state — both additive within the existing `dev/`/`data/` route model
  (named `erFrame`-wrapped `Scenario`s + projection-type fields, not a shape change). The renderer primitives
  (refused-conduit flash, moved-badge, engine-dropout) and the six wirings are internal to `panels/engine-room/`
  (its overview + sidecars). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is
  unchanged. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T01:40 — No route impact: slice 05o T1B's only `dashboard/src/`-direct change is the `dev/`
  scenario player — `dev/scenarios.ts` gains the `stale-base` preflight→fast-forward failure-mode timeline (F0→F8,
  + `dev/scenarios.test.ts` a case) — which is data within the existing `dev/` route model, not a shape change.
  The T1B renderer primitives (the pruned `main` node), the indicator anchoring / z-order fixes, the
  `FleetingEnclosure` box, and the alert transitions are internal to `panels/engine-room/`, and the §10 spec note
  is under the sibling `docs/design/engine-room/`; the `dashboard/src/` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail in those overviews + sidecars.
  Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — No route impact: slice 05o T3B's only `dashboard/src/`-direct change is the `dev/`
  scenario player — `dev/scenarios.ts` gains the `memory-block` failure-mode timeline (+ `dev/scenarios.test.ts`
  a case) — which is data within the existing `dev/` route model, not a shape change. The failure-mode renderer
  primitives (scan ring, ghosted lane), fixtures, and the engine-gauge polish are internal to
  `panels/engine-room/`, and the §10 spec section is under the sibling `docs/design/engine-room/`; the
  `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail in those
  overviews + sidecars. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T23:35+02:00 — slice 05k tear-down + design-review refinements: the only `dashboard/src/`-direct
  change is `index.css` deleting the `@keyframes powerup` (the last engine-room canvas keyframe — the
  indexing→nominal engine flash, now a Motion opacity pulse on the charge rect). All the rest — the tear-down
  dispose sequence + power-down diagnostics, the second-loop engine-fill fix, the three-column re-spacing, the
  closeout-train breadcrumb, and the memory integration arrow — is internal to `panels/engine-room/` (its
  overview + sidecars). The `cockpit/`/`grammar/`/`panels/`/`data/`/`dev/` route model is unchanged. (Separately,
  `docs/design/` was brought into onboarding scope — a sibling route, not under `dashboard/src/`.) Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-21T09:57+02:00 — slice 05n (engine-room DrawSVG/MotionPath migration): the only `dashboard/src/`-direct
  change is `test/setup.ts` adding a jsdom **SVG-geometry stub** (`getBBox`/`getTotalLength`/`getPointAtLength`)
  so the engine-room GSAP DrawSVG/MotionPath plugins construct under the effects-on GSAP-gate test. The render
  rework (draw-on → DrawSVG one-shot, packet → MotionPath, the `flowConduit` recipe) is internal to
  `panels/engine-room/` (its overview + sidecars). The `dashboard/src/` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged. Verification metadata pinned until closeout
  stamps the 05n commit.
- 2026-06-21T02:44+02:00 — slice 6g: the cockpit gained **task-document navigation** — `panels/DetailPanel` renders a series **master** (overview + clickable sub-task index) with in-panel **drill-in** into each slice (the back/parent up-link in the sticky panel header), **markdown-rendered** task prose via the new `grammar/Markdown` primitive, and **cross-master "→" navigation** that jumps between series lifecycles (`onOpenLifecycle`). Detail in the `grammar/` + `panels/` overviews. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-21T02:26+02:00 — slice 05k (engine-room motion → GSAP/Motion): the only `dashboard/src/`-direct
  change is `index.css` deleting the nine engine-room canvas `@keyframes` (`chargeSweep`/`conduitDraw`/`pktRun`/
  `attnBreath`/`stopFlash`/`closeoutSweep`/`warpSurgeUp`/`warpSurgeDown`/`landingIn`) that prior slices parked
  in the effects layer; the engine-room canvas motion now runs on GSAP timelines (`useEngineTimeline`) + Motion,
  CSS static (the app-wide `crt-overlay`/`flicker`/`pulse` keyframes stay). The render rework + the new hook are
  internal to `panels/engine-room/` (its overview + sidecars). The `cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`
  route model is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T23:58+02:00 — slice 5i: the `dev/` sub-route gained the **scenario player** — new
  `dev/scenarios.ts` (timeline model) + `dev/ScenarioPlayer.tsx` (transport) + `dev/scenarios.test.ts`, with
  `dev/Bench.tsx` reworked from the static gallery into a scenario picker + player and `dev/fixtures.ts`
  extracting the shared `engineRoomProjection` wrap; `dev/Bench.tsx` also gained a sidecar (a prior gap). The
  only other `dashboard/src/`-direct change is the `index.css` `landingIn` keyframe (engine-room landing-tail
  detail). The engine-room render rework is internal to `panels/engine-room/` (its overview + sidecars). The
  `cockpit/`/`grammar/`/`panels/`/`data/` route model is otherwise unchanged. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-19T15:59 — Task 6 slice 6f-1: the cockpit gained the **highlight → context-package** composer — `panels/HighlightComposer.tsx` (mounted in `CockpitShell`) + the `data/selection.ts` selection hook; a text selection raises it to send the selection + a message into a chat session's stdin (the `data/sessions` store became the cockpit-wide inject seam; `data/terminal.ts` buffers pre-open stdin for create-then-send). No silent action; reuses the live B2 channel (not ACP). Detail in the `panels/` + `data/` sidecars. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: terminal/session **hardening** — the open-session registry moved into a new `data/sessions` Zustand store, and a live terminal now survives both a cockpit *view* switch (`cockpit/Cockpit.tsx` keeps `<Chats>` mounted, hidden via CSS) and a *session-tab* switch (`panels/Chats.tsx` keeps every session's `<Terminal>` mounted) instead of being unmounted; the backend PTY spawn (`serving/terminal.py`) gained a controlling terminal so tmux honors resize, and `data/terminal.ts` replays the first winsize on socket open. Detail in the `data/` + `panels/` sidecars. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T05:48 — Task 6 slice 6e-3: the **Chats** terminal gained **context injection** — a `SessionComposer` (React Aria `TextField`/`TextArea` + `Button`) docked below the terminal injects a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f). Refreshed the Behavior layer. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-19T06:39+02:00 — No route impact: an engine-room crash fix relaxes `EngineProcessNode.landing` to optional (`landing?:`) in `types/projection.ts` so the canvas tolerates a pre-5h/persisted projection that omits it; the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail in the `types/projection.ts` sidecar. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T04:38 — Task 6 slice 6e-2c: the **Chats** view's open sessions moved into a dedicated left-rail **`SessionList`** switcher (a React Aria `GridList` — single-select = active session, per-row close ✕), replacing the horizontal tab strip; the launch controls stay in the top strip and the harness buttons now share ＋ Terminal's golden look. Refreshed the Behavior layer (the switcher's `GridList`) + the `panels/` route-model line. Verification metadata pinned until closeout stamps the 6e-2c code commit.
- 2026-06-18T21:27 — No route impact: a dev-bench review-ergonomics pass collapsed the `/dev/bench` gallery strip into a compact `<select>` picker + trimmed the 6 `engine-boot-*` step tabs and the unused `engine-empty` fixture (mirroring task 5's `b3f2491`). All internal to the DEV-only `dev/` harness (dropped from the production bundle); the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) this overview describes is unchanged — detail in the `dev/` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:27 — Task 6 slice 6e-2b: the **Chats** view gained per-harness launch buttons — `data/terminal.ts` `fetchHarnesses` (`GET /api/harnesses`) drives a detection-driven button per *installed* harness (Claude Code / Codex / Pi.dev) beside ＋ Terminal. Detail in the `panels/` overview + the `Chats.tsx`/`terminal.ts` sidecars. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T21:25+02:00 — No route impact: slice 5h Tier 2's only `dashboard/src/`-direct change is mirroring the four optional `LedgerRefNode` fields (`codeSubject?`/`codeDate?`/`memorySubject?`/`memoryDate?`) in `types/projection.ts`; the 6-column popover render lives in `panels/engine-room/` (its overview + sidecars). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T17:40 — Task 6 slice 6e-2a: the **Chats** view became a **create** surface — "＋ Terminal" spawns a dashboard-owned session via the new `data/terminal.ts` `openTerminalSession` → the `POST /api/terminal` opener (no longer just attaching to a store lifecycle). Detail in the `panels/` overview + the `Chats.tsx`/`terminal.ts` sidecars. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:50 — Task 6 slice 6e-1: the cockpit gained its first **interactive terminal** — a full-bleed **Chats** view (`panels/Chats.tsx` + the lazy `panels/Terminal.tsx` xterm wrapper) over the new `data/terminal.ts` Mode B2 WebSocket client (binary PTY bytes in, `{type:stdin|resize}` out), reachable from the cockpit mode bar. **Corrected the stale "Read-only — no POST" invariant** (write surfaces have existed since 6c; 6e adds the bidirectional terminal). Dev bench supplies a mock socket so it renders without a backend; the real launch is 6e-2. Verification metadata pinned until closeout stamps the 6e-1 code commit.
- 2026-06-18T18:00+02:00 — No route impact: slice 5h's ledger popover mirrors `LedgerRefNode` + the additive `LedgerNode.rows` / `EngineProcessNode.ledgerRows`/`ledgerRowCount` fields in `types/projection.ts` and wires the demo `analytics.ledgers` in `dev/fixtures.ts`; the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail lives in the `engine-room/` overview + the `types/projection.ts` sidecar. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:00 — Task 6 slice 6c Part B: the cockpit gained its **one write** — `DetailPanel`'s Gate Review drawer POSTs a developer gate decision to `/api/actions` via the new `data/actions.ts` (+ a `gate-review` bench scene in `dev/fixtures.ts`). The rest stays read-only. Verification metadata pinned until closeout stamps the 6c Part B code commit.
- 2026-06-18T14:05 — No route impact: task 6 slice 6c Part A only extended the projection **type mirror** (`types/projection.ts` gained `GateNode` + the optional `LifecycleProjection.gate`); the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`) is unchanged. The gate review **drawer** (`panels/DetailPanel.tsx` + `data/`) lands in 6c Part B — surfaced here then. Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T15:50+02:00 — No route impact: the 5h cleanup pass's only `dashboard/src/`-direct change is `dev/fixtures.ts` filtering the `engine-boot-*` frames out of the bench gallery tab strip (a DEV-harness curation); the rest is render polish internal to `panels/engine-room/` (conduit wiring + backdrop vignette + a dropped fixture). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail lives in the `engine-room/` overview + sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T13:01+02:00 — No route impact: the 5h coupler fix's only `dashboard/src/`-direct change is the `index.css` `warpSurgeUp`/`warpSurgeDown` keyframes (the coupler warp-core surge, frozen by `effects=off`); the render lives in `panels/engine-room/`. The `dashboard/src/` route model is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T11:55+02:00 — No route impact: slice 5h H2's only `dashboard/src/`-direct change is the `index.css` `closeoutSweep` keyframe (the closeout-train fill, frozen by the `effects=off` rule); the render lives in `panels/engine-room/` (its overview + sidecars). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`) is unchanged. Verification metadata pinned until closeout stamps the 5h H2 code commit.
- 2026-06-18T08:51+02:00 — No route impact: slice 5h H1 mirrors `LandingRefNode` + the additive `EngineProcessNode.landing` / `integrationStrategy` fields in `types/projection.ts` (and adds landing fixtures under `panels/engine-room/`); the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`) this overview describes is unchanged — detail lives in the `engine-room/` overview + the `types/projection.ts` sidecar. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-17T22:45 — No route impact: the engine-room visual-parity pass (the 5g G6 blueprint backdrop + the
  cockpit Effects/Calm toggle, the `engine-room/` SVG decal layer, and the `grammar/Panel` `fill` height fix)
  is internal to those sub-routes; the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`)
  this overview describes is unchanged — detail lives in those overviews + sidecars.
- 2026-06-17T16:15 — No route impact: slice 5g G5 lands the Engine Room live/teardown states
  (t12b/t14c/t18) + a green=active engine palette + a left-rail scroll fix — all internal to
  `panels/engine-room/` — plus an `index.css` `stopFlash` keyframe. The `dashboard/src/` route model
  (`panels/`/`grammar/`/`data/`/`cockpit/`) is unchanged; detail lives in the `engine-room/` overview +
  sidecars. Verification metadata pinned until closeout stamps the G5 code commit.
- 2026-06-17T14:00 — No route impact: `index.css` gained the `attnBreath` keyframe (the failure-overlay
  attention-badge breathing, 5g G3). Engine-room detail (surfaced in the `panels/engine-room` overview);
  the dashboard/src architecture this overview describes is unchanged. Verification metadata pinned until
  closeout stamps the G3 commit.
- 2026-06-17T13:30 — No route impact: `index.css` gained the Engine Room pod-stage motion keyframes
  (`chargeSweep` / `conduitDraw` / `pktRun`, 5g G2) + a `conduit-packet` freeze rule. These are engine-room
  detail (surfaced in the `panels/engine-room` overview); the dashboard/src architecture this overview
  describes is unchanged. Verification metadata pinned until closeout stamps the G2 commit.
- 2026-06-16T02:30 — slice 5f S1: the cockpit shell's machine-map views (Engine Room / Topology) go
  full-bleed (rails hidden, §4.1); added the dashboard suite's first component-render test
  (`cockpit/Cockpit.test.tsx`) and the shared jsdom stubs in `test/setup.ts`. The `dashboard/src/`
  route model is otherwise unchanged (detail in the `cockpit/` + `engine-room/` sidecars/overviews).
  Verification metadata pinned until closeout stamps the S1 code commit.
- 2026-06-15T19:35 — No route impact: slice 5e adds the `panels/engine-room/` sub-route (its own route overview + file sidecars) plus `types/projection.ts` / `dev/fixtures.ts` changes; the `dashboard/src/` route model this overview describes (the `panels/` / `grammar/` / `data/` / `cockpit/` split) is unchanged — detail lives in the `panels/` + `engine-room/` overviews and the file sidecars.
- 2026-06-15T17:00 — Created for slice 5d: the frontend re-architecture (Panda + React Aria,
  layered). Documents the layered styling architecture, the grammar/panels split, and the read-only
  boundary. Verification metadata pinned until closeout stamps the 5d code commit.
