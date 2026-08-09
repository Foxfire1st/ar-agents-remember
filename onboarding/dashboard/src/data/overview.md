# dashboard/src/data/ — Cockpit State And Authority Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/data/`                            |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-08-01T10:20+02:00 |
| lastVerifiedCommitHash | `fb0296562ceb29929a3675a1b0195700d23bc56a`       |
| lastVerifiedCommitDate | 2026-08-09T20:35:49+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## 260731-EFA-L8 Change

`data/terminal.ts` was refactored during the frontend-rail remediation (a
self-caught intermediate reattach-socket defect, corrected within the round; the
53-test terminal contract passes unchanged on base). `data/submissionWithdrawal.ts`
was extracted from `submissionLifecycleClient.ts`, which also replaced its
`wireFixtureGuard` cast with a validated narrow. All other data-route changes are
behavior-preserving lint remediation.

## Purpose

This route owns the browser-side state and authority boundaries consumed by the dashboard UI. It
normalizes terminal catalog rows, keeps session and per-seat cockpit state, reconciles the daemon's
catalog, drives launch/set/submit lifecycles, and exposes pure derivations for rail, task, command,
and state-grammar surfaces. Components may project these facts, but must not invent a second
catalog, delivery ledger, or lifecycle authority.

This overview is the strategic owner for the data plane so the root and panels
overviews can remain compact. It also records the retirement of the legacy `sessionGroups` model:
role/spawn hierarchy and attention are now derived by `railModel.ts`, while product-facing grouping
and rendering live in the canonical Chats cockpit's `SessionRail.tsx`.

## Runtime Identity And Recovery

- `buildIdentity.ts` owns the executing bundle fingerprint and a pure tri-state comparison with the
  server's optional shipped-dashboard identity; it never reloads the page itself.
- `harnessCatalog.ts` validates the narrow pre-session `id`/`name`/`detected` envelope and preserves
  network, HTTP, protocol, valid-empty, and ready distinctions. Request timeout, cancellation, and
  Retry belong to the dialog-local hook rather than a global store or poller.
- `terminal.ts` separates WebSocket transport loss from durable terminal exit. Only an explicit
  server exit ends the session; a boot-owned reattach consumes each identity once, rejects stale
  callbacks, and replays resize before buffered input without a timer loop.

## Authoritative Session Open

- `terminalOpen.ts` is the sole browser authority for `POST /api/terminal`. It preserves the exact
  requested identity, validates HTTP and protocol outcomes, and returns a normalized accepted
  server row or one typed failure. A raw request must return neither harness nor control state;
  contradictory server evidence fails closed.
- `terminal.ts` is now the transport/facade layer over that opener. `launchFlow.ts` delegates to the
  same authority, so the raw button, harness chooser, and contextual launch callers share one
  response grammar instead of reconstructing acceptance locally.
- `sessions.ts` materializes and broadcasts a session only from the accepted server row. Network,
  HTTP, protocol, identity, and server-declared failures leave the registry unchanged; a request is
  never enough to create a ghost row.
- The `/dev/bench` injector in `dev/cockpitScenarios.ts` supplies request-matched raw and harness
  responses through the real client boundary. It does not weaken production validation or grant a
  second open authority.

## Route Model

### Catalog And Session Identity

- `sessions.ts` owns `OpenSession`, the catalog-backed registry, live-action `activeId`, connection
  registries, leaf/lifecycle attachment patches, and cross-tab catalog-change notifications. One
  field is deliberately NOT catalog-sourced: `liveTurnWorking?` carries the
  focused seat's own conversation-projection live-turn signal, merged at the view layer only
  (`SessionsView`) — the registry itself never writes it, so the accepted-server-row materialization
  rule above is unweakened. `stateGrammar.ts`'s `seatVisualState` prefers it over the sweep-lagged
  catalog `turnState` (a streaming turn must never read settled `turn-ended`) but only AFTER the
  terminal/fault/blocked-on-human/wait guards, so it can never fake liveness over a real end state.
  The pending-interaction twin rule (review finding N1):
  `OpenSession.controlPendingInteractions?` is the ADDITIVE plural (multiplexed harness sub-agent
  pendings) beside the parent-thread singular slot, and every attention surface —
  `stateGrammar.ts`'s blocked-on-human guard, `announcer.ts`'s focused-seat suppression,
  `railModel.ts`'s question triage — derives from `sessions.ts`'s `sessionHasPendingInteraction`
  (singular slot OR non-empty plural), never the singular slot alone, or a seat blocked SOLELY on a
  sub-agent approval goes dark.
- `catalogPoll.ts` is the single catalog read/reconcile boundary. `CockpitShell` owns both its
  refcounted interval and eager/cross-tab reconciler for the shell lifetime. Remote terminate is
  removed locally and excluded from the confirming read so a stale echo cannot resurrect it.
- Cockpit inspection focus is deliberately separate from `activeId`: landed rows remain
  inspectable, but only a running row can own the action/reload route through `preferLiveSession`.
- `sessionCockpitStore.ts` owns ephemeral per-seat UI evidence, drafts, queue state, focus, poll
  health, and layout intent. The inspector's product default is closed; responsive geometry is a
  separate concern and must not rewrite deliberate operator intent.

### Reliable Submit And Authoritative Withdrawal

- `submitClient.ts` is the whole-message submission boundary. It retains exact request ids and
  drafts across route errors, distinguishes accepted/queued/rejected/unsupported truth, reconciles
  ambiguous outcomes, and politely announces focused-seat receipts.
- `submissionLifecycleClient.ts` polls authoritative submission state and owns withdrawal. Pop-back
  is not a local queue edit: the client resolves the last queued request, calls the bridge with the
  expected epoch, applies only an authoritative withdrawn result, and retains recovery/endgame
  evidence when convergence is uncertain.
- Queue, submit history, withdrawal recovery, composer draft, and rail/stage notices are projections
  of the same per-seat store. A failed or ambiguous operation must not move the active route or
  discard the operator's draft.

### Lifecycle Cleanup And Honest Residuals

- `sessionLifecycle.ts` keeps detailed terminate outcomes, focus-independent stop residuals, and
  landed-cleanup outcomes. A successful terminate may still carry an informational control-stop
  residual; it is not reclassified as failure.
- When landed cleanup returns no authoritative result, the exact `{id,label}` target snapshot is
  retained in `cleanupFailure` and remains visible/retryable outside the collapsible rail. Partial
  success keeps both closed and skipped rows/reasons.
- Exited and retired rows are catalog evidence rather than live PTYs. Landed rows remain read-only
  inspectable until authoritative cleanup removes them.

### Structured Conversation Projection

- [data/conversation](conversation/overview.md) owns the **reconstructable active-conversation
  projection**: a pure authority reducer (cursor-ordered apply, eventId+cursor dedupe, block-delta
  revision gating, gap→re-page tolerance, same-revision→reset, replace-page rehydrate — never an
  optimistic durable item) plus a thin store orchestrating page/stream/recovery/LRU. It holds only a
  browser projection rebuilt from the landed L1 page/stream contract and the L3 control routes.
- [data/conversation-library](conversation-library/overview.md) owns the **reconstructable
  previous-conversation library projection**: list/preview and the exact-open flow whose focus fires
  only on `opened` catalog proof, with the caller-stable requestId reconciled under one id.
- Both are separate, reconstructable stores (R1): reload/pages/events rebuild them from server/native
  authority; there is no IndexedDB/localStorage/SQLite conversation index and no durable browser item
  authority (the only persisted UI bit is the hide-thinking boolean). The renderer consuming them is
  the [session-cockpit/conversation](../panels/session-cockpit/conversation/overview.md) grammar.

### Controls, Keymaps, And Accessibility

- `capabilityCatalog.ts`, `setClient.ts`, and the set/launch helpers separate pre-session envelope
  truth from exact-session control truth and preserve pending/clamped/refused evidence.
- [data/keymap overview](keymap/overview.md) owns effective keyboard bindings, browser-reserved
  rejection, the immutable F6 focus escape, and Emacs/Vim composer profiles.
- `announcer.ts` is the shared polite/assertive store. Urgent transitions from one hydration are
  committed as one batch so synchronous seats cannot overwrite one another before assistive
  technology observes them.

### Dev-Bench Authority Boundary

The `/dev/bench` cockpit scenarios replace transport only. Scenario switches revoke unresolved
catalog, capability, snapshot, submission-poll, withdrawal, and connection ownership by generation
before seeding the successor fixture. These reset exports are dev-only authority seams; production
code must not use them as ordinary recovery APIs.

### 2026-07-24 Resilient Boot And Steady-State Work

- `fetchWithTimeout.ts` aborts a hung browser socket. `inflight.ts` owns only per-key single-flight
  lifetime: concurrent boot readers share result or rejection, then the identity-guarded slot clears
  on settle. Repository, harness, terminal, and capability catalogs use the pair.
- `sessions.ts` preserves state and row identity for a byte-identical catalog beat, while the
  authoritative poll still replaces any row whose content differs from a local pre-apply.
- `streamLiveness.ts` gives state and conversation EventSource channels a visible-tab watchdog: sleep
  is positive evidence, ordinary silence earns at most one quiet cycle, and never-open replacements fail
  honestly instead of retaining a live cue.
- A queued receipt is acceptance evidence rather than pre-dispatch proof. The lifecycle authority alone
  enables withdrawal; dispatching/unknown records wait for a terminal word under the bounded window.
- Every representable pending adapter interaction uses the direct exact-session route with
  bridge-epoch evidence. Structured questions send an all-or-nothing answers map; permission,
  arbitrary-choice, and composer modes send one response string. Lifecycle gates do not transport
  adapter answers.

### 260731-EFA-L4 Typed Sub-Task Rows And Mirror-Checked Fixtures

- `taskHierarchy.ts` — `ParentTaskMatch.ref` is a **`SeriesSubTaskNode`**, no longer the collapsed
  `TaskSubTaskRefNode`. Those are two distinct server models (`projection.py::TaskSubTaskRefNode`
  and `::SeriesSubTaskNode`, both `extra="forbid"`) that the browser mirror used to fold into one
  interface, and the fold was not free: it invented a `createdAt` on master rows the server never
  stamps, and lent `linkedLifecycleId` — the cross-series jump — to series rows that never carry
  one. `findParentTaskMatch` reads `series.subTasks`, so its match is a SERIES row by construction;
  the narrowed field just says so. `types/projection.ts` now declares both models plus a
  `SubTaskRow` union for the renderer that shows either.
- `orderedByCreation` is now **exported** and is this route's single creation-order sort.
  `panels/DetailPanel.tsx` carried a byte-identical second copy (its own `function
  orderedByCreation`) and now imports this one instead. The rule is **all-or-nothing**: rows are
  reordered only when EVERY row carries a `createdAt`, so a partially-stamped list keeps its
  authored order rather than sorting the stamped rows to the front. A row type that declares no
  `createdAt` at all — a master's `TaskSubTaskRefNode` — therefore passes through untouched by
  construction. It is an order-preserving safety net, not the thing that establishes the order:
  `observer/snapshots.py::_series_subtask_nodes` already applies the same all-or-nothing rule
  server-side before the rows are served.
- The route's test suites no longer author their own wire nodes. **Six** of the route's seven
  changed suites — `interactionAnswer`, `railModel`, `seatEvents`, `setClient`, `store`, and
  `taskIdentity` — now import the shared builders from `test/fixtures/wire.ts`, which removed the
  casts that let a fixture assert past the mirror (`as unknown as LifecycleProjection`,
  `as TaskDocNode`, `as ObserverEvent`, `as never`). The seventh, `taskHierarchy.test.ts`, builds no
  wire node at all — its only change is the same `TaskSubTaskRefNode` → `SeriesSubTaskNode`
  narrowing as its source. The cost of the casts is measured rather than hypothetical: a test
  asserted `refusedPolarity === "amber"` against a fixture that set the field itself on an
  `extra="forbid"` model, and three tests built a master `TaskDocNode` carrying `createdAt`, which
  no server model declares. Both compiled, because an assertion turns off excess-property checking.
- `store.test.ts` is the one suite in the route where the conversion changed what is proven, not
  just how the fixture is written. It consumed the snapshot as
  `snapshot as unknown as WorkspaceProjection` — a double cast that turned off assignability, so
  the fixture could drop a field the store reads and nothing here would notice. It now goes through
  `test/servedProjection.ts::asServedProjection`, whose parameter type is the check. Its
  hard-coded `expect(state.metrics?.lifecycleCount).toBe(2)` also became
  `FIXTURE_LIFECYCLES = projection.lifecycles.length`: the snapshot grew from two lifecycles to six
  once `contract.test.ts` began requiring every member of every closed vocabulary to be exercised,
  and six states need six lifecycles.

## Invariants And Boundaries

- **Fixtures are checked against a generated producer contract.** Every wire node a dashboard test
  builds comes from `test/fixtures/wire.ts` and is type-checked against `types/projection.ts`, which
  is generated and stale-checked from the Pydantic projection schema. `test/contract.test.ts` measures
  the separate hand-maintained sample against that mirror
  `fixtures/snapshot.json` in three directions, and `test/wireFixtureGuard.ts` sweeps the tree for
  the one-token opt-outs plain `tsc` cannot see (a cast, a `@ts-expect-error`, a literal that lost
  freshness through a variable, `Object.assign`, `JSON.parse`). `wire.ts` and `snapshot.json` remain
  hand-maintained fixture/sample artifacts, while the producer-to-TypeScript link is generated. The
  tests therefore hold fixtures and sample coverage to the generated contract; the generator and
  stale check hold the contract to the producer schema. Check it with `npm run typecheck`
  (`tsc -b`) — a bare `tsc --noEmit` proves nothing in this repo, because the root tsconfig is
  solution-style and compiles no files while still exiting 0.
- The terminal catalog and bridge responses are authoritative; browser state is a projection and
  cache, never a replacement history database.
- Session creation is response-authoritative: only a validated accepted server row may enter the
  browser registry, receive focus, or become a delivery target. Failed requests create no row.
- One shell-level catalog driver/reconciler serves every route and tab. View remounts must not create
  a second timer or listener.
- `focusedSessionId` may name a landed/ended row for inspection; `activeId` must name a live row for
  actions. Catalog hydration must not steal deliberate landed focus.
- Reliable submit and withdrawal preserve request identity. Never resend blindly after an ambiguous
  boundary and never implement pop-back as a local-only deletion.
- Operator text, agent-bus messages, lifecycle control, and adapter interaction answers remain
  distinct authority channels. The structured conversation UI consumes
  adapter-normalized history/resume from the landed L1/L2/L3 server contracts; it never scrapes or
  duplicates vendor TUIs, and it holds only a reconstructable projection — no durable browser
  conversation index and no optimistic durable item authority.
- Controlled sessions default to the structured `ConversationSurface`. The runner line-log survives
  only as the default-off read-only terminal-diagnostics drawer and the legacy-raw body. UA-1
  history/index/resume is now served by the `conversation/` and `conversation-library/` projections
  documented above.

## Hot Path Summary

1. `terminalOpen.ts` validates the sole open request and yields an accepted server row or a typed
   failure without mutating browser state.
2. `sessions.ts` commits only the accepted row; catalog reconciliation then keeps terminal truth
   current while data-layer stores derive focus, lifecycle, control, and delivery
   evidence without replacing daemon truth.
3. The canonical Chats cockpit projects those stores into rail, stage, inspector, composer, and
   status surfaces.
4. Submit, answer, set, attach, terminate, cleanup, and withdrawal operations cross their dedicated
   authority routes before local state commits.
5. Cross-tab invalidations trigger one confirming catalog read; generation guards discard results
   owned by a retired dev scenario.

## Child Route Onboarding Map

| Child route | Governing overview | Responsibility |
| --- | --- | --- |
| `dashboard/src/data/keymap/` | [keymap overview](keymap/overview.md) | Static/effective keyboard bindings, focus zones, browser safety, and composer profiles. |
| `dashboard/src/data/conversation/` | [conversation overview](conversation/overview.md) | Reconstructable active-conversation projection: pure reducer, resumable stream, store/LRU, formats. |
| `dashboard/src/data/conversation-library/` | [conversation-library overview](conversation-library/overview.md) | Reconstructable previous-conversation library projection and the exact-open resume flow. |

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Catalog and session registry | [catalogPoll.ts](catalogPoll.ts.md) · [sessions.ts](sessions.ts.md) |
| Cockpit state and announcements | [sessionCockpitStore.ts](sessionCockpitStore.ts.md) · [announcer.ts](announcer.ts.md) |
| Lifecycle and cleanup | [sessionLifecycle.ts](sessionLifecycle.ts.md) |
| Reliable submit and withdrawal | [submitClient.ts](submitClient.ts.md) · [submissionLifecycleClient.ts](submissionLifecycleClient.ts.md) |
| Control/capability truth | [capabilityCatalog.ts](capabilityCatalog.ts.md) · [setClient.ts](setClient.ts.md) |
| Role/spawn rail derivation | [railModel.ts](railModel.ts.md) |
| Runtime bundle identity | [buildIdentity.ts](buildIdentity.ts.md) |
| Bounded boot transport and single-flight ownership | [fetchWithTimeout.ts](fetchWithTimeout.ts.md) · [inflight.ts](inflight.ts.md) |
| Strict pre-session harness discovery | [harnessCatalog.ts](harnessCatalog.ts.md) |
| Authoritative terminal open | [terminalOpen.ts](terminalOpen.ts.md) · [terminal.ts](terminal.ts.md) · [sessions.ts](sessions.ts.md) · [launchFlow.ts](launchFlow.ts.md) |
| Durable terminal transport | [terminal.ts](terminal.ts.md) · [terminal.test.ts](terminal.test.ts.md) |
| Stream liveness and visible-tab wake policy | [streamLiveness.ts](streamLiveness.ts.md) · [screenWakeLock.ts](screenWakeLock.ts.md) |

## Docs References

The curator checked the memory repository's `system/sources.md`; it contains “No entries configured
yet,” so no Domain Documentation source was available for this route. The current statements were
verified from same-repository source/tests, the task/worker/reviewer records, and the recovered
same-repository history pack.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for the data route. | — | — |

## Cross-Repo References

The data route's imports and authority calls resolve inside agents-remember; no cross-repository
implementation source governs this slice. Adapter behavior is consumed through this repository's
own server contracts, so no external code path is cited as authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found for these browser state/authority modules. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Catalog/session ownership and cross-tab reconciliation. | "export function captureCatalogAuthority", "export function notifySessionCatalogChanged" | dashboard/src/data/catalogPoll.ts:44-44; dashboard/src/data/sessions.ts:113-113 |
| Per-seat UI and evidence state. | "export type EvidenceTier" | dashboard/src/data/sessionCockpitStore.ts:18-18 |
| Reliable submission and authoritative withdrawal. | "export function createFetchSubmitTransport", "export const VISIBLE_STATUS_POLL_MS" | dashboard/src/data/submissionLifecycleClient.ts:18-18; dashboard/src/data/submitClient.ts:238-238 |
| Lifecycle termination, residuals, and landed cleanup. | `startRetireResidualSweep` | dashboard/src/data/sessionLifecycle.ts:136-154 |
| Role/spawn hierarchy replacing legacy `sessionGroups`. | `sessionGroups` | dashboard/src/data/railModel.ts:119-119 |
| The single exported creation-order sort and the panel that now imports it instead of keeping a byte-identical copy. | "export function findParentTaskMatch", "export const DetailPanel" | dashboard/src/panels/detail-panel/DetailPanel.tsx:76-76; dashboard/src/data/taskHierarchy.ts:43-43 |
| The two distinct sub-task row models and their union, plus the server builder that has already ordered the series rows. | , "class _TaskDocumentLifecycleMaps:" | mcp/src/agents_remember/observer/snapshots_impl/_common.py:37-37;  |
| The generated projection mirror this route's suites build fixtures from, the manual sample used for coverage, and the fixture/projection stale gates. | "GENERATED FILE", "is NOT generated; it remains a hand-maintained", "fixture-coverage guard", "def check", "def main" | dashboard/src/test/contract.test.ts:24-24; dashboard/src/test/fixtures/wire.ts:22-22; dashboard/src/types/projection.ts:1-1; scripts/sync-projection-types.py:43-43; scripts/sync-projection-types.py:54-54 |

## Placement Decision

New overview routes for `dev/` and the cockpit-scenario files were considered. Their code is a
bounded test/fixture authority seam and remains governed by the root overview; creating another
overview would fragment the product architecture. The high-churn state/authority modules instead
receive this `data/` overview, while `keymap/` remains its own child and `session-cockpit/` remains
the UI composition owner. Detailed legacy grouping knowledge was preserved here and in the
session-cockpit overview before the six obsolete sidecars were removed.

## 260727-CHATS-IM-L2 Route Impact

Conversation roster derivation now accepts only backend-minted roster identities. Other
agent-tagged notices, including selected-child history state, remain conversation items and cannot
create duplicate seats. No catalog, submit-machine, or session-registry ownership changed.

## Update History

- 2026-08-09T19:36+02:00 — 260713-TES-L5F2 route impact: the interaction-answer authority is
  now uniformly exact-session-owned for structured and scalar payloads; lifecycle gates are not
  an adapter response fallback.
- 2026-08-08T21:20+02:00 — No route impact: 260713-TES-L1 renamed one store field
  (`supervisorHeartbeat` → `agentNotifierHeartbeat`) with a legacy-wire fallback in `applySnapshot`;
  the data route's shape and responsibilities are unchanged and the sidecar for `data/store.ts`
  carries the detail. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: added the L8 Change section (terminal refactor, submissionWithdrawal extraction, validated narrow). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact anchors and fixer-generated ranges, and deleted two rows whose onboarding-overview sources
  are not indexable; exact non-fixing check returns zero findings.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: corrected the data-route projection boundary:
  generated/stale-checked mirror, typed fixture builders, and separately measured manual sample.
  New ranges are explicit `:1-1` curator input.

- 2026-08-01T10:20+02:00 — 260731-EFA-L4 curator (route impact: one source file, one type contract
  and one shared helper): `taskHierarchy.ts` is the only non-test source this leaf changed in the
  route, and it moved twice. `ParentTaskMatch.ref` narrowed from the collapsed `TaskSubTaskRefNode`
  to `SeriesSubTaskNode` — `findParentTaskMatch` reads `series.subTasks`, so the match was always a
  series row, and the collapsed interface had been claiming a `createdAt` on master rows the server
  never stamps plus a `linkedLifecycleId` on series rows that never carry one. And
  `orderedByCreation` became exported: `panels/DetailPanel.tsx` held a byte-identical copy at the
  leaf base (`git show HEAD:…/DetailPanel.tsx` L1219-L1224 against `taskHierarchy.ts` L134-L139 —
  the same six lines) and now imports the one authority. Recorded the all-or-nothing rule and the
  fact that `observer/snapshots.py::_series_subtask_nodes` already applies it server-side, so the
  browser copy is a safety net rather than the source of the order. Also recorded the fixture
  conversion — SIX of the seven changed suites now import `test/fixtures/wire.ts`; the seventh,
  `taskHierarchy.test.ts`, builds no wire node and only follows the source's type narrowing
  (checked by grepping each file for `test/fixtures/wire`) — and singled out `store.test.ts`, the
  one suite where the conversion changed what is proven: `snapshot as unknown as
  WorkspaceProjection` became `asServedProjection(snapshot)`, and a hard-coded lifecycle count of 2
  became the fixture's own length, now 6. Recorded as an invariant exactly how far all of that
  pins anything: `fixture ⊆ mirror` is enforced (`tsc -b` plus `wireFixtureGuard.ts`), mirror-against-
  snapshot is enforced by `contract.test.ts` in three directions, and **`mirror ⊆ server` is enforced
  by nothing** — both `test/fixtures/wire.ts` and `fixtures/snapshot.json` are hand-maintained and
  no generator exists in this repository. Checks run: `npm run typecheck` (`tsc -b`) exits 0 across
  the three referenced projects; `tsc --noEmit` is NOT a check here and was not used as one. Three
  `Repo-Internal References` rows added. Verification metadata remains pinned until closeout stamps
  the commit.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: roster derivation now accepts
  only explicit backend roster identities (`codex-agent-`/`claude-agent-`), so selected-child
  history state and other agent-tagged notices remain transcript content rather than duplicate
  seats. Verification metadata remains pinned until closeout.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator (route impact: one derivation rule): recorded the
  review-N1 plural pending rule in Catalog And Session Identity — `controlPendingInteractions?` is
  the additive multiplexed sub-agent plural beside the parent-thread singular slot, and every
  attention surface derives from `sessions.ts`'s `sessionHasPendingInteraction` (singular OR
  non-empty plural) so an agent-only-blocked seat never goes dark. Detail in the
  [sessions.ts](sessions.ts.md), [stateGrammar.ts](stateGrammar.ts.md),
  [announcer.ts](announcer.ts.md), and [railModel.ts](railModel.ts.md) sidecars. Source is
  uncommitted; closeout re-stamps verification.

- 2026-07-24T13:17:50Z — Route impact: added the resilient boot/steady-state model for bounded
  transport + single-flight, no-op catalog reconciliation, one-shot SSE liveness, lifecycle-terminal
  submit settlement, and direct structured interaction answers. Added the new data file cards;
  verification metadata remains pinned until the code commit.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R9 (audit V5) live-turn seat-state
  nuance in Catalog And Session Identity — `OpenSession.liveTurnWorking?` is the single
  projection-sourced ephemeral field (view-layer merge for the focused seat only; `sessions.ts` never
  writes it, accepted-server-row materialization unweakened), and `stateGrammar.ts`'s
  `seatVisualState` prefers it over the sweep-lagged catalog `turnState` strictly after the
  terminal/fault/blocked/wait guards. Detail in the [sessions.ts](sessions.ts.md) and
  [stateGrammar.ts](stateGrammar.ts.md) sidecars; the `conversation/` child route carries the R10
  hydrate-retry truth in its own overview. Verification stays pinned until L5F closeout stamps the
  candidate commit.
- 2026-07-21T05:30+02:00 — No route impact: 260718-CHATS-L5P (cockpit chrome visual polish) touched one
  `data/` source — `conversation/format.ts` gained the `shortId` helper (R6) and its `humanizeDuration`
  became the cockpit-wide single duration authority (R5). Both are presentation conventions inside the
  `conversation/` child route (recorded in [conversation/overview.md](conversation/overview.md) and the
  `format.ts` card); the `data/` route model and every state/authority contract are unchanged.
  Verification metadata unchanged.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator (structured Chats renderer, reviewer FINAL PASS):
  added the two child routes `conversation/` (reconstructable active-conversation projection — pure
  reducer + resumable stream + store/LRU) and `conversation-library/` (reconstructable
  previous-conversation projection + exact-open flow), the Structured Conversation Projection route-
  model section, and corrected the stale invariants — the structured conversation UI is now landed and
  consumes adapter-normalized history/resume as a reconstructable projection (no durable browser
  index), and controlled sessions default to the structured surface with the line-log demoted to a
  read-only diagnostics drawer. Verification metadata remains pinned pending L4 candidate closeout.

- 2026-07-18T15:22+02:00 — FEUI-MX-FIX-2: documented `terminalOpen.ts` as the sole browser open
  authority, accepted-server-row-only registry mutation, raw-response contradiction checks, shared
  launch delegation, and request-matched dev fixtures. Verification metadata remains pinned pending
  candidate closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: added browser build identity, strict harness discovery, and
  explicit durable-terminal recovery ownership. Verification metadata remains pinned pending
  candidate closeout.

- 2026-07-18T07:22+02:00 — Created during 260715-FEUI-L8 curation to own catalog/session state,
  reliable submit and withdrawal, lifecycle cleanup, control-authority boundaries, and the
  `sessionGroups` → `railModel`/`SessionRail` duty transfer. Verification metadata remains pinned to
  the leaf base because the reviewed L8 candidate is uncommitted; closeout owns candidate stamping.
