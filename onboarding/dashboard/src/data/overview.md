# dashboard/src/data/ — Cockpit State And Authority Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/data/`                            |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-09-22T11:00:00+02:00 |
| lastVerifiedCommitHash | `f141d164265e926be9249acf6ae680ccf9ffae61` |
| lastVerifiedCommitDate | 2026-09-22T12:24:11+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l45-ar` uncommitted source; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l3`, uncommitted; base `d80a0513e928ef29a973527d09597c82c96fde87` |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5` |
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Current Structural Identity Contract

`taskIdentity.ts` derives canonical references from projected real task documents. `sessions.ts`
stores document+role binding separately from runtime correlation, and `railModel.ts` constructs the
default Chats hierarchy from task containment. `terminal.ts` posts structural assignment; leaf keys
remain display/context helpers and never serve as hosted-seat addresses.

## Purpose

### 260731-EFA-L23 Route Delta

L23 extends the route's volatile-age contract with lifecycle-operation `elapsedSeconds`: server and client strip the same field so operation clocks do not churn structurally unchanged enclosure rows.

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

The shared `dashboardStore.reset()` is the one full dashboard-projection reset used by
`ScenarioPlayer`. Its single Zustand transaction increments `gen` once and restores every
scenario-owned projection to its clean initial value, including `closeoutQueues`. This is dev/test
scenario infrastructure: production does not call `reset()`, and production snapshot/delta queue
ingestion, ordering/filtering, scheduling, and lifecycle authority remain unchanged.

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

TES-L6 adds sprint-qualified command-seat projection here: terminal rows carry stored
repository+sprint provenance, `railModel.ts` groups architect/orchestrator/manager by that pair,
and unbound historical rows remain in a migration-only bucket. For concurrent-sprint grouping or
ownership-display bugs, start with `sessions.ts`, `railModel.ts`, and their focused tests.

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
| Catalog/session ownership and cross-tab reconciliation. | "export function captureCatalogAuthority", "export function notifySessionCatalogChanged" | dashboard/src/data/catalogPoll.ts:44-44; dashboard/src/data/sessions.ts:116-116 |
| Per-seat UI and evidence state. | "export type EvidenceTier" | dashboard/src/data/sessionCockpitStore.ts:18-18 |
| Reliable submission and authoritative withdrawal. | "export function createFetchSubmitTransport", "export const VISIBLE_STATUS_POLL_MS" | dashboard/src/data/submissionLifecycleClient.ts:18-18; dashboard/src/data/submitClient.ts:238-238 |
| Lifecycle termination, residuals, and landed cleanup. | `startRetireResidualSweep` | dashboard/src/data/sessionLifecycle.ts:136-154 |
| Structural task hierarchy and diagnostic spawn ancestry are built as separate models. | `buildRailModel`; `buildSpawnTree` | dashboard/src/data/railModel.ts:408-434; dashboard/src/data/railModel.ts:462-484 |
| The shared creation-order helper sorts only when every row has createdAt; unstamped task-document rows retain input order. | `orderedByCreation` | dashboard/src/data/taskHierarchy.ts:145-150 |
| The one full scenario-store reset restores every projected collection, including `closeoutQueues`, in one transaction and is invoked by the development scenario player. | `dashboardStore`; `reset`; `ScenarioPlayer` | dashboard/src/data/store.ts:55-55; dashboard/src/data/store.ts:329-401; dashboard/src/dev/ScenarioPlayer.tsx:21-107 |
| Series sub-task rows carry optional creation time; task-document sub-task references have a separate shape and share a union for readers. | "export interface SeriesSubTaskNode"; "export interface TaskSubTaskRefNode"; "export type SubTaskRow" | dashboard/src/types/projection.ts:560-560; dashboard/src/types/projection.ts:792-792; dashboard/src/types/projection.ts:814-814; dashboard/src/types/projection.ts:838-838 |
| The server series builder sorts only fully stamped rows before projection. | `_series_subtask_nodes` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:302-319 |
| The generated projection mirror this route's suites build fixtures from, the manual sample used for coverage, and the fixture/projection stale gates. | "GENERATED FILE", "is NOT generated; it remains a hand-maintained", "fixture-coverage guard", "def check", "def main" | dashboard/src/test/contract.test.ts:24-24; dashboard/src/test/fixtures/wire.ts:22-22; dashboard/src/types/projection.ts:1-1; scripts/sync-projection-types.py:46-46; scripts/sync-projection-types.py:57-57 |

## Current Requirement Artifact Boundary

`requirements.ts` reads registered requirement documents using a canonical task selector plus document identity; it does not expose arbitrary-path reads. `taskArtifacts.ts` owns the shared target union so notes and requirement documents carry distinct selectors through the same reader surface. Structured requirement rendering retains the backing document identity rather than treating an arbitrary Markdown link as registered authority.

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

## 260831-CCR-L23 Task-Local Requirements Client

L23 added the task-local requirement-packet client to this route: `data/requirements.ts`
(typed `listRequirements`/`readRequirement` over `/api/requirements/{list,read}` plus the
reserved `requirements/` address/reference resolvers) and the shared
`data/taskArtifacts.ts` discriminated reader target (`TaskArtifactReaderTarget`: notes vs
requirements with the task-document selector). Consumers: the requirement-link provider, the
notes-reader viewer, TaskNotes references, and detail-panel task prose.

## 260915-KS-L22 The Read-Only Intent-Review Client

This route gained one client module, `data/review.ts`, and the property that makes it belong here at
all is a restraint: it reads and it stores nothing. It is the same-origin client for
`GET /api/review/intent` and it mirrors `data/changeset.ts` in shape — a `base` argument defaulting
to same-origin, requests built through the shared `qs` helper and errors thrown as the shared
`FilesApiError` from `getJson`. Where its sibling differs is what it does with the answer: the
module's own header states that the surface exposes no submission control, so no function in it writes
anything.

**It now exports two calls, one per reviewer route, and the second one is what a task view needs
first.** `intentReview(repo, master, leaf, selectorKind, selectorId)` renders one comparison;
`intentReviewEntries(repo, master, leaf)` asks which subjects that comparison can be opened on, taking
the **task context and nothing else** because a selector is precisely what it is being asked for. The
entry call's own comment records how a caller must read its answer: a refused read is "a normal outcome
(no live candidate, no dataset yet): it yields no entry and the caller renders no button, which is the
existing `live && selectorId` semantics and stays correct". That is why the task view can now offer
the reviewer at all — the reviewed subject it needs is a **recorded identity inside the candidate the
server resolved**, and this client is the only legitimate source of it. Its `ReviewEntry` interface has
no path field on purpose, and its `ReviewEntryListResult` is a typed envelope whose refused form
carries a `refusal` and no entries rather than throwing, so "cannot answer" and "no subject here" stay
different facts at the client boundary too.

It mutates no store. This route's data modules are where browser projection state is normalized,
reconciled and retained; `review.ts` sits deliberately outside that pattern — it exports no store, no
slice, no reducer and no subscription, so a review never enters the cockpit's dashboard store and can
never be read back as browser state. Every value it returns is the server's typed result mapped
field-for-field: a field the server omits is optional here rather than defaulted, which is what keeps
an unresolved reference unresolved on the client instead of rendering as an empty string or a
fabricated attribution.

The comparison request it builds names canonical task context and one recorded subject only — `repo`,
`master`, `leaf`, `selectorKind`, `selectorId` — and never a filesystem path, so the browser cannot
choose which dataset is reviewed. Its selector union is closed at the two kinds the transport admits
(`invariant` and `family`), so the client cannot ask for a subject the server would refuse by having
some other kind mapped onto one. The entry request names **no subject at all**, which is the other half
of the same rule: it asks the server to select one. The file's own card carries the type-by-type
detail.

| Finding | Anchor | Source |
| --- | --- | --- |
| The route's read-only client and its comparison call. | "export const intentReview = (" | dashboard/src/data/review.ts:328-342 |
| **The entry call: the task context alone, because a selector is what it is being asked for.** | "export const intentReviewEntries = (" | dashboard/src/data/review.ts:369-377 |
| **The reviewed subject as the server selected it — the entry's only legitimate selector source, with no path field on purpose.** | `ReviewEntry` | dashboard/src/data/review.ts:344-353 |
| **The entry read's typed envelope, whose refused form carries a refusal and no entries rather than throwing.** | `ReviewEntryListResult` | dashboard/src/data/review.ts:355-363 |
| The endpoint the comparison call reaches, with no path among its parameters. | `review` | dashboard/src/data/review.ts:1-9; dashboard/src/data/review.ts:1-10 |
| The closed selector union, the two kinds the server admits. | "export type ReviewSelectorKind" | dashboard/src/data/review.ts:14-14 |
| The no-store-mutation boundary, stated in the module header. | "NO store mutation" | dashboard/src/data/review.ts:4-4 |
| The typed result the client returns unchanged. | "export interface ReviewResult {" | dashboard/src/data/review.ts:315-321 |
| The field-for-field mirror of the server's review payload. | "export interface ReviewPayload {" | dashboard/src/data/review.ts:292-304 |

## Update History
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "export const intentReview = (" repointed to dashboard/src/data/review.ts:271-271. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "export const intentReviewEntries = (" repointed to dashboard/src/data/review.ts:312-312. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "export interface ReviewResult {" repointed to dashboard/src/data/review.ts:258-258. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "export interface ReviewPayload {" repointed to dashboard/src/data/review.ts:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **this route's reviewer client gained the entry read, which is what makes the task-view entry reachable.** `intentReviewEntries(repo, master, leaf)` takes the task context and nothing else — a selector is precisely what it is being asked for — and returns a typed `ReviewEntryListResult` whose refused form carries a `refusal` and no entries rather than throwing, so a refused read is a normal outcome the caller renders as no button. The card also records `ReviewEntry`, whose own comment states it is "the ONLY legitimate source of the entry's selector" and that there is "no path field here on purpose", and it corrects the L22 sentence that said the module exports "one exported call": it now exports two, one per reviewer route. No verification stamp was advanced.
- 2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **added the L22 section** — `data/review.ts`, the read-only client for `GET /api/review/intent`, its closed two-member selector union, and the no-store-mutation boundary it holds (no store, slice, reducer or write is exported). Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns that stamp.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_series_subtask_nodes` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:302-319. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `_series_subtask_nodes` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:302-319. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `SubTaskRow` in the row 324 of this card from dashboard/src/types/projection.ts:792-792 to dashboard/src/types/projection.ts:838, the extent of the construct the claim is about (the checker named line(s) [838] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `SubTaskRow` in the row 324 of this card from dashboard/src/types/projection.ts:560-566 to dashboard/src/types/projection.ts:838, the extent of the construct the claim is about (the checker named line(s) [838] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `SeriesSubTaskNode` in the row 324 of this card from dashboard/src/types/projection.ts:838 to dashboard/src/types/projection.ts:560-566, the extent of the construct the claim is about (the checker named line(s) [560] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `SubTaskRow` in the row 324 of this card from dashboard/src/types/projection.ts:560-560 to dashboard/src/types/projection.ts:838, the extent of the construct the claim is about (the checker named line(s) [838] as its live location)

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 3 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T10:16+02:00 — 260913-LCA-L10 curator: re-anchored one citation into `snapshots_impl/_task_documents.py` after that file grew by 52–57 lines for the tolerant read edge (the server series builder `_series_subtask_nodes` moved 260-277 → 314-333; the cited file changed, this route's own sources did not). No dashboard source, renderer, or fixture is in that change set, so the route's behavior and ownership contract are unchanged. Verification metadata unchanged; no verification stamp advanced.



- 2026-09-05T07:20+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Added the registered requirement artifact boundary and repaired creation-order/model evidence to the real owners. Verification records source review, not execution or acceptance.
- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 route impact: recorded the new `requirements.ts` client + `taskArtifacts.ts` artifact-target type modules. File-level detail in the new data cards.


- 2026-08-31T09:06+02:00 — 260821-ARSPAWN-L5 A005 citation reconciliation refreshed
  route citations after reviewed source movement; the data-route ownership contract is unchanged.
  Verification remains closeout-owned.

- 2026-08-24T12:59+02:00 — 260821-DAGQC-L3 curator: recorded the route-level dev/test invariant
  that the one canonical dashboard reset is total over scenario-owned projections, including
  `closeoutQueues`, in one Zustand transaction. Production snapshot/delta queue ingestion,
  ordering/filtering, scheduling, and lifecycle authority remain unchanged. Verification metadata
  remains pinned until governed closeout stamps the code commit.

- 2026-08-18T13:00+02:00 — No route impact: 260815-DAG-L8 added the closeout-queue projection surface; route purpose unchanged.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator route review: L23 extends the route's volatile-age contract with lifecycle-operation `elapsedSeconds`: server and client strip the same field so operation clocks do not churn structurally unchanged enclosure rows. Verification provenance remains closeout-owned.

- 2026-08-11T23:40+02:00 — No route impact: the `railModel.ts` helper split preserves this route's
  canonical task-document hierarchy, role-altitude placement, and spawn-provenance separation.
  Verification metadata remains pinned until governed closeout.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled this route with the
  task-document-addressed dashboard data changes; current bodies and file cards now describe
  canonical `TaskDocumentRef` identity without treating a leaf key as agent routing authority.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: added the sprint-qualified command-group hot path and
  migration-only legacy boundary. Verification metadata remains pinned until closeout.

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

## 260921-ICR-L2 The Review Client Mirrors The Inventory And Asks For The Task's Own Review

**Route meaning changed: `data/review.ts` can now express a review that compared nothing.** The client
gained the inventory's three interfaces — `ReviewChangedFile` (the raw path, its status, its content kind
and the reason an unknown is unknown), `ReviewUnrepresentablePath` (the exact bytes of a name the surface
cannot carry as text) and `ReviewSourceInventory` (state, entries, count, detail, partial flag, command,
both tree ids and the byte-form remainder) — and `ReviewSourcePane.inventory` is now required and first.
`ComparisonIdentity` gained `knowledge_compared` with its three knowledge-half digests optional,
`ReviewKnowledgePane` gained `selection_state`/`selection_detail`, `ReviewStaleness.state` gained
`not_compared`, and `ReviewPayload.comparison` became optional. `intentReview` now sends **no selector
parameters at all** when there is none, which is the task-context request. The module's own rule — a
field the server omits is absent here rather than defaulted — now covers an entire absent identity, and
no fallback value was introduced for it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The inventory's wire types, including the byte form of a name this surface cannot print.** | `ReviewChangedFile`; `ReviewUnrepresentablePath`; `ReviewSourceInventory` | dashboard/src/data/review.ts:144-154; dashboard/src/data/review.ts:156-161; dashboard/src/data/review.ts:169-179; dashboard/src/data/review.ts:164-164; dashboard/src/data/review.ts:191-191; dashboard/src/data/review.ts:189-189; dashboard/src/data/review.ts:202-202 |
| **The comparison identity that states whether knowledge was compared, and the staleness union that gained the task-context state.** | `ComparisonIdentity`; `ReviewStaleness` | dashboard/src/data/review.ts:36-49; dashboard/src/data/review.ts:277-282; dashboard/src/data/review.ts:56-56; dashboard/src/data/review.ts:297-297; dashboard/src/data/review.ts:321-321 |
| The payload whose comparison may be absent, and the pane that says which question was answered. | `ReviewPayload`; `ReviewKnowledgePane` | dashboard/src/data/review.ts:292-304; dashboard/src/data/review.ts:99-113; dashboard/src/data/review.ts:119-119; dashboard/src/data/review.ts:318-318; dashboard/src/data/review.ts:312-312; dashboard/src/data/review.ts:339-339 |
| **The request that omits the selector when there is none — the task-context entry.** | `intentReview` | dashboard/src/data/review.ts:323-342; dashboard/src/data/review.ts:348-348 |
| The surface that consumes the new types and renders the inventory — whose rows, since `260921-ICR-L3`, also open into the entry's content. | `Inventory`; `SourceContent` | dashboard/src/panels/review/ReviewSurface.tsx:291-335; dashboard/src/panels/review/ReviewSurface.tsx:214-260; dashboard/src/panels/review/ReviewSurface.tsx:8-8; dashboard/src/panels/review/ReviewSurface.tsx:49-49; dashboard/src/panels/review/ReviewSurface.tsx:277-277 |

## 260921-ICR-L3 The Expansion Wire Types And The One Call That Reads Its Refusal

**Route meaning extended, narrowly: the review client can now open one listed entry, and it does so
through the one function that deliberately steps outside this route's error idiom.** `data/review.ts`
grew 320 → **414 lines** and gained four interfaces and a third request:

- `ReviewSourceSideState` — the closed six-member literal a side's `state` may be (`present`, `absent`,
  `binary`, `symlink`, `submodule`, `unavailable`) — and `ReviewSourceSide`, which carries that state
  with an optional `text`. The optionality is the route's own missing-side rule applied to content:
  `text` is present only for the two textual states, so a missing or unrenderable side can never arrive
  as an empty document and the renderer can never manufacture one.
- `ReviewSourceExpansion` — both sides, both generation ids, the three-member `currentness` with its
  detail, `path_bound` (`requested_generation` / `leaf_change_set`) with its detail, and the
  `reference`/`command` — and `ReviewSourceContentResult`, the envelope whose `state` is `"content"`
  with an `expansion` or `"refused"` with a `refusal`.
- `reviewSourceContent(repo, master, leaf, path, beforeCodeTreeId, afterCodeTreeId, base = "")`, which
  is the only function in this client that does **not** go through `getJson`. On this route a typed
  refusal is a *normal* answer — a path outside the measured change set, a baseline that is not this
  leaf's recorded one — and the transport carries it as the typed refusal in the body **with** a
  400/404 status, which `getJson`'s throw-on-non-OK behaviour would turn into a transport error. So the
  function `fetch`es the URL directly, decodes the body whatever the status was, returns it as the typed
  result when `body.state` is `"content"` or `"refused"`, and throws `FilesApiError` only for a body
  that is not this route's answer at all (an unwired process, a proxy error).

**The generation is an input, and that is the property the whole expansion rests on.**
`beforeCodeTreeId`/`afterCodeTreeId` are the ids the inventory published to this client, and the
function sends them back — in that camelCase spelling, which is the spelling the route binds — so the
content a reader opens is the content of the generation they were looking at, never re-resolved from
whatever the leaf holds by the time the request lands. The client resolves no path and no tree of its
own, and its own comment states that boundary. `intentReview` and `intentReviewEntries` are unchanged by
this leaf: the comparison request still names a task context and one recorded subject, and the entry
request still names the task context alone.

The consumer is the `panels/` route's Source pane, which mounts the new renderer beneath an openable
inventory row; the file's own card carries the type-by-type detail.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The six-member state literal and the side value whose optional `text` is present only for the two textual states, so no missing or unrenderable side can arrive as an empty document.** | `ReviewSourceSideState`; `ReviewSourceSide` | dashboard/src/data/review.ts:192-213 |
| **The expansion value: both sides, both generation ids, the three-member currentness, and the `path_bound` that says which measured change set admitted the path.** | `ReviewSourceExpansion` | dashboard/src/data/review.ts:214-238 |
| **The source-content envelope whose two states are the two answers this route gives, a refusal being a normal one.** | `ReviewSourceContentResult` | dashboard/src/data/review.ts:240-246 |
| **The one call that reads its typed body whatever the HTTP status was, and the only one here that does not go through `getJson`.** | `reviewSourceContent` | dashboard/src/data/review.ts:379-414 |
| **The generation as an input: the caller's two published tree ids, echoed back in the spelling the route binds.** | `beforeCodeTreeId`; `afterCodeTreeId` | dashboard/src/data/review.ts:389-405; dashboard/src/data/review.ts:416-416; dashboard/src/data/review.ts:426-426; dashboard/src/data/review.ts:415-415; dashboard/src/data/review.ts:425-425 |
| The consumer that mounts the renderer beneath an openable row, at the inventory's own two tree ids. | `SourceContent`; `review-inventory-open` | dashboard/src/panels/review/ReviewSurface.tsx:214-260; dashboard/src/panels/review/ReviewSurface.tsx:8-8; dashboard/src/panels/review/ReviewSurface.tsx:49-49; dashboard/src/panels/review/ReviewSurface.tsx:277-277 |
| The renderer the expansion's fields feed, and its three state-decided branches. | `Sides`; `review-source-no-diff-claimed` | dashboard/src/panels/review/SourceContent.tsx:76-112 |

## 260921-ICR-L16 The Review Route Gets Its Own Transport Owner

The review reads' transport now has **one owner on this route**: `data/reviewTransport.ts` (196 lines,
new in this leaf). The review routes answer with their typed result and map a refusal onto the
change-set routes' `400`/`404`/`503` idiom, so a refusal arrives as a **non-2xx response whose body is
still this route's typed answer** — and the shared `getJson`, which reads only `body.status` and throws,
dropped every one of them before a reader could see it. A reader saw `404 Not Found` where the route had
published a missing dataset, its reason and the initialization action. `getReviewJson(url)` is the fix:
one GET, the body read whatever the status, and **a body carrying this route's `state` IS the answer**
(payload, subject list or typed refusal); anything else is a named failure.

`data/review.ts` stays this client's public entry and becomes a thin delegator: its three read functions
(`intentReview`, `intentReviewEntries`, `reviewSourceContent`) call `getReviewJson`, and the module
**re-exports** the moved surface, so `panels/review/*` and `panels/detail-panel/changeSetBar.tsx` keep
importing one public entry and no existing importer changed its path. The decode that used to be inline in
`reviewSourceContent` is now that one implementation, so `grep -rn "api/review/intent" dashboard/src`
finds the route URL only in the two review client modules. Line counts: `review.ts` 414 → 428.

The failure vocabulary is closed and deliberately wider than the six states the requirement names:
`not-initialized`, `unavailable-history`, `validation`, `authority` and `network` are the route's own
words, `not-found` and `domain-refused` carry the remaining codes verbatim rather than guessing them into
a state, and `unreadable` names "an HTTP response this route did not produce" while `network` names "no
HTTP response at all". `TOKEN_BY_CODE` is the **only** code→state table in `dashboard/src`, and
`reviewFailureToken` carries an unknown code as `domain-refused` instead of inventing a state for it — so
the entry bar and the surface cannot come to disagree about what a code means. `loading` and `known-empty`
are deliberately **not** failure members: they are not failures and are rendered as themselves.

Unrelated clients' semantics are untouched, and that is asserted rather than asserted-about: `getJson`
still throws on a non-2xx and still drops the body for the routes that use it, which the case module pins
against the **identical** response. The change-set client (`data/changeset.ts` → `getJson` →
`/api/changeset/task`) therefore still swallows its own refusal detail; that is a different route, client
and owner, and it is **routed to R12/R24**, recorded here rather than fixed.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one GET whose body is the answer whatever the status, and which returns a typed result only for a body carrying this route's `state`.** | `getReviewJson` | dashboard/src/data/reviewTransport.ts:158-171 |
| **The only code→state table in this route, with an unknown code carried verbatim rather than guessed into a state.** | `TOKEN_BY_CODE`; `reviewFailureToken` | dashboard/src/data/reviewTransport.ts:70-98 |
| **The comparison and entry reads and the expansion read, all delegating to the one decode.** | `intentReview`; `intentReviewEntries`; `reviewSourceContent` | dashboard/src/data/review.ts:348-364; dashboard/src/data/review.ts:392-399; dashboard/src/data/review.ts:410-427; dashboard/src/data/review.ts:348-348 |
| **The shared client whose semantics are unchanged, and the change-set client that still inherits them.** | `getJson`; `FilesApiError`; `leafChangeset` | dashboard/src/data/files.ts:76-97; dashboard/src/data/changeset.ts:135-144 |

## 260921-ICR-L13 The Master Client Is Generation-Bound

This route's change-set client is now generation-bound for master nets. `data/changeset.ts`
grew 120 → **155 lines**: `MasterNetPins` (four optional wire params) freezes a request to the
listed generation with unset pins omitted, `MasterNetGeneration` (four commits + digest) is
what the list response publishes beside `currentness` and `scope: "integrated"`, leaf rows
carry optional `state`, and `masterChangeset`/`masterFileDiff` thread the pins. The leaf and
task helpers are unchanged. The swallowed-refusal-debt sentence above still holds — this leaf
changes what a successful master read carries, not what a failed one reports — and stays
**routed to R12/R24**. `data/changeset.ts`'s card carries the body update and citation
re-derivation.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The generation pins, the published generation identity, and the pins threaded through both master reads.** | `MasterNetPins`; `MasterNetGeneration`; `masterFileDiff` | dashboard/src/data/changeset.ts:46-46; dashboard/src/data/changeset.ts:52-52; dashboard/src/data/changeset.ts:112-112 |

## Update History
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **route body updated — the master client is generation-bound (new section above).** No review-client fact changed; the R16 routed-debt sentence stands. The one row into the moved client is re-derived (`leafChangeset` `:100-108` → `:135-144`). No verification stamp was advanced; the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **route body updated.** The route gained the review reads' one transport owner, `data/reviewTransport.ts`, and `data/review.ts` became a delegator plus re-exporter (414 → 428 lines). The section above records the defect the owner closes (the typed refusal in the body of a non-2xx response was unreachable through `getJson`), the rule that makes the decode correct (a body carrying this route's `state` IS the answer, whatever the status), the closed failure vocabulary with `unreadable` (a response this route did not produce) and `network` (no response at all) as the two honest fallbacks rather than guessed states, and the boundary that unrelated clients are untouched. It also records, as **routed rather than fixed**, the change-set client's own swallowed refusal detail to R12/R24. **No verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **route body updated, and citation re-derivation of the L2 record above forced by this leaf's change to its cited file.** Added the `260921-ICR-L3` section: `data/review.ts` gained the source-expansion wire types (`ReviewSourceSideState`, `ReviewSourceSide`, `ReviewSourceExpansion`, `ReviewSourceContentResult`) and `reviewSourceContent(...)`, and grew 320 → **414 lines**. The section records the one property a reader of this route has to carry away, because it is the exception to the route's own error idiom: `reviewSourceContent` is the only function in this client that does **not** go through `getJson`, because on the source-content route a typed refusal is a *normal* answer carrying a 400/404 status and `getJson`'s throw-on-non-OK behaviour would turn it into a transport error — so it decodes the body whatever the status was, returns it typed when `body.state` is `"content"` or `"refused"`, and throws `FilesApiError` only for a body that is not this route's answer. `intentReview` and `intentReviewEntries` are unchanged. **Citation accounting:** every row of the `260921-ICR-L2` section above cites `data/review.ts` by line and this leaf moved them all, so each was re-derived against this candidate — the inventory types `143-154`/`155-167`/`168-178` → `144-154`/`156-161`/`169-179`, `ComparisonIdentity`/`ReviewStaleness` `35-48`/`220-225` → `36-49`/`277-282`, `ReviewPayload`/`ReviewKnowledgePane` `235-247`/`98-114` → `292-304`/`99-113`, and `intentReview` `271-290` → `323-342` — as were the L22 section's nine rows, whose new values are `1-9`, `13-14`, `16-21`, `23-27`, `29-49`, `51-63`, `65-85`, `87-97`, `99-113`/`181-190`/`267-275`, `114-126`, `128-135`, `248-253`/`255-265`, `277-282`/`284-290`, `292-304`/`306-313`/`315-321`, `323-342`, `344-353`, `355-363`, `365-377`, and the consumed-client row now names `ReviewSurface.tsx:482-549` and `:214-260`. The five rows of the L3 section above are the ones this leaf added. **No verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, code base `702714fc`): **route body updated.** The review client mirrors the new wire shape — the inventory types, an optional comparison identity, the `not_compared` and selection states — and `intentReview` now sends no selector at all when there is none, which is what makes the task-context review reachable from the browser. The section is appended at the end of this route's narrative, and the three rows of this document that cited `data/review.ts` by line were re-derived against the candidate in the same pass. **No verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp.
