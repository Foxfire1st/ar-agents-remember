# dashboard/src/data/ — Cockpit State And Authority Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/data/`                            |

## Governing Overview

[dashboard/src overview](../overview.md)

## 260928-MIK-L33 The Family Mirror Carries The Change Facts Of A Tree Comparison

[`reviewFamily.ts`](reviewFamily.ts.md) mirrors MIK-R33's change facts
(`models/knowledge/review_change_kinds.py`): `ReviewChangeKind`, `ReviewChangeFact`, `ReviewChangeMark`,
`ReviewMemberChange` (one member occurrence by the roster's `member_id`, with its three facts, `proof`, `text_differs`,
`range_unresolved`, the server-derived `primary` and `marks`, and `evidence`, `unknown_reasons` and
`membership_reasons` kept apart) and `ReviewFamilyChanges` (the guarantee's fact, the optional `members_total`, the
returned occurrences), carried on `ReviewFamilyContextEntry.change_kinds` for a tree comparison only. The
transport casts the body as before; an omitted field stays `undefined`, and a rendering (`panels/review/changeTriage.ts`)
never recomputes a fact. The five new types are imported from `reviewFamily.ts` directly, not re-exported through
`review.ts`. The keymap child route gains the reviewer's zone and chords (its overview's MIK-L33 section).

- The mirrored change types and the entry's optional facts. [1]

## 260928-MIK-L34 One File's Classification As A Single Read, For The Per-Hunk Intent Markers

[`reviewLane.ts`](reviewLane.ts.md) gains `readFileClassification(repo, master, leaf, comparison, path)`: the same
`file=<path>` read of the tree view route as `useReviewFileClassification`, as a promise rather than a hook, resolving
to `ready` or `unavailable` (a thrown transport error becomes `unavailable` with the owner's problem, never a
rejection). Its one caller is the per-hunk intent markers' scope (`panels/review/intentMarkerScope.ts`, MIK-R34),
which keeps one answer per changed path for the surface on screen, so a file opened again, in another pane or card,
asks nothing. Every mark is built from this answer unchanged (ruling 2026-09-30T16:19:34 Q2 kept MIK-R32's response
as it is). A dataset review names no comparison, so the scope asks nothing.

- One file's classification as a single read; a transport failure is `unavailable`. [2]
- The scope that keeps it per surface, only for a tree comparison. [3]

## 260928-MIK-L32 The Unexplained-Changes Lane Adapter, And The Entry's Count On The Summary

One new adapter, [`reviewLane.ts`](reviewLane.ts.md) (carded, governed here), carries the server's one classification
of a tree comparison's changed paths (MIK-R32, `models/knowledge/review_lane.py`) as types, snake_case as served, and
reads it through the tree view route: `useReviewLane` asks `lane=files` for the two destinations (`Unexplained
changes`, `Unknown attribution`) and every measured path's bucket (`paths`, which the source explorer's labels and the
technical details take on a tree comparison: rulings 2026-09-30T12:19:20 Q1 and 13:07:38 F1), and
`useReviewFileClassification` asks `file=<path>` for one changed path's hunks, classes, links and reasons. Each answer
is kept with the URL it answers, so a superseded answer never draws; an answer without the value it was asked for
reads `unavailable`, never an empty lane. A dataset review names no tree comparison, so both hooks ask nothing. The
surface makes the one lane read and hands it down.

[`reviewIntentSummary.ts`](reviewIntentSummary.ts.md) now carries `attribution`, the lane's file-level count
(`ReviewLaneSummary`), from the same summary response, on the counted/partial state and on the refused state alike
(ruling Q6); the entry therefore never asks for it more eagerly than for the intent counts (MIK-R32 rule 9).

- The adapter's own statement: the server classifies once and this file only carries the answer. [4]
- The two reads; none for a dataset review. [5]
- The summary carries the lane's count on both answered states. [6]

## 260928-MIK-L29 The Knowledge Reader Adapter And Its Shareable Address

One new adapter, [`knowledgeReader.ts`](knowledgeReader.ts.md) (carded, governed here), serves the dashboard's
Knowledge area (MIK-R29, `panels/knowledge-reader/`): the answer types of every reader view (the selection block with
`codeTree`, `codeSource`, `codeNote` and `pinnedCommit`; the bounded directory's `children` and `subtree`; subtree pages
with their continuation; truth views with `outgoingState` and a timeline whose sources carry their own states; the
selector's `commitsState`), the reads of `/api/knowledge/reader/<view>`, and the reader's address. **The address is
the URL hash** (`#knowledge?repo&commit&path|id|census|view…`), because production serves only `/`: `parseReaderHash`
reads it (any other hash is `null`) and `readerHash` writes it with commit and path or ID always spelled out, so every
link is a navigation and a view can be shared (rule 5). `readerGet` returns every typed answer whatever its HTTP
status, including a 400 `invalid-request`, and throws only on a transport failure or a body with no state (a 503
from a process without the reader), so a refusal is shown as what it is and never as an empty view. The keys are the
backend's camelCase document keys; the adapter issues GETs only.

- The shareable hash, read and written. [7]
- A typed answer returned whatever its status; only transport failures throw. [8]
- The selection block every answer carries. [9]

Since `260928-MIK-L37` the adapter's `IncomingLink` carries `sourceSubject`: the record a `history_row` source is
about, which the truth view links to, because a row has no page of its own (MIK-R29 rule 5).

- An incoming link may carry the record its history-row source is about. [59]

## 260928-MIK-L31 The Tree View Adapter Reads A Selection's Entries, And One Wire Casing

[`reviewTrees.ts`](reviewTrees.ts.md) now carries what the reviewer's focused expression cards need (MIK-R31):
`ReviewTreeEntry` and `ReviewTreeEntrySide` (each realization and proof entry located on both code sides, with the
range state, the bounded excerpt, the authored role and rationale or facet, and the MIK-R03 state), `invariants=`
on the request (ruling 2026-09-30T05:36:19 Q2), `treeComparisonNumber` (the payload's own `review:trees:<n>`, whose
absence marks a dataset review), `useReviewTreeEntries` (one selection's entries, kept with the question they
answer) and an `enabled` flag on `useReviewTrees`, which the workspace passes only for a tree comparison and pins to
the payload's comparison number (review F11). **Every key is snake_case** (MIK-L25 review F9, settled by L31: the
server re-keys the owners' camelCase documents), and the worklist's items and history rows are named types with
MIK-R11's `planning` mark. The panel and the cards now render this view (`panels/review/LeafKnowledgeChanges.tsx`,
`ExpressionCards.tsx`). **Candidate invariant (not ingested): dataset reviews make no tree read.**

The real body ([`reviewTrees.captured.json`](reviewTrees.captured.json.md)) was re-captured from L31's scratch leaf
(comparison 1, the planned marks and `planned_untouched` items of its two declared effects), and
[`reviewTrees.test.ts`](reviewTrees.test.ts.md) asserts no camelCase key anywhere in it. The transport test's
expansion refusal ([`reviewTransport.test.ts`](reviewTransport.test.ts.md)) was re-measured on the real route
(MIK-R31 rule 6, ICR-L43 review R2 O2).

- The entry types. [10]
- The comparison a payload names, and one selection's entries. [11]
- No camelCase key in the real body. [12]

## 260928-MIK-L25 The Tree View Adapter, And The Landed Review Over Trees

[`reviewTrees.ts`](reviewTrees.ts.md) (new, carded and governed here) is the client of `GET /api/review/trees`
(MIK-R25): the four Git trees and their pinning refs, each knowledge side's state (`available`,
`unavailable-history`, `legacy-unavailable`) and index state, the reopened code sides (review F4), the Git diff of
the memory trees grouped by record and by source path, MIK-R03 currentness per side, and the MIK-R08 worklist view.
`reviewTreesRead` keeps `trees`, `not-converted` and a refusal apart and reports anything else as unreadable in the
shared review vocabulary; `useReviewTrees` drops a superseded answer. The landed adapters (`review.ts`,
`reviewFamily.ts`) are unchanged: for a converted leaf only their data source changed (rule 6).

At L25 no component rendered this view — the panel for rules 2 and 3 was carried to L31/L32 (ruling
2026-09-29T22:22:37 Q2), and the mixed key casing the types mirrored was carried to L31 (review F9); both are
settled by L31 (above). Its cases
([`reviewTrees.test.ts`](reviewTrees.test.ts.md)) run over the real captured body
([`reviewTrees.captured.json`](reviewTrees.captured.json.md)) of the worker's converted scratch leaf, recaptured
under the directory-name refs (ruling 2026-09-30T02:32:42 (a)).

- The tree view's answer and the request, addressed by number, `recorded` or (since L31) a selection's invariants, never by path. [13]
- Three answers kept apart. [14]

## 260921-ICR-L44 The Family Mirror Carries Each Source's Locator, Ranges And State

`reviewFamily.ts` mirrors the server's member-source reference with three new declarations —
`ReviewSourceLocator` (the server's `file` / `line_range` / `symbol` locator kinds),
`ReviewSourceLineRange` and `ReviewSourceLocatorState` — and `ReviewFamilyMemberSource` now carries an
optional `locator` (travelling with the address), required `resolved_ranges` and `locator_state`, and
required `role`/`rationale`. `review.ts` re-exports the three new types with the rest of the family
vocabulary. The review transport casts bodies to these types without a runtime decoder, so the mirror is
the whole client-side contract; no rendering reads the new fields yet.

- The three locator declarations. [15]
- The member source carrying them. [16]

## Recorded reviewer catalogue

useReviewCatalogue.ts owns the reviewer's catalogue read (since `260921-ICR-L47` the task entry no longer reads it; it reads the changed-intent summary through reviewIntentSummary.ts instead). The read is keyed on the comparison's identity, preserves complete recorded subjects, counts and distinct failure states, and suppresses rows from another comparison while the current one is pending. intentEntryRevalidation.tsx holds the entry's re-validation generation (re-show, return from the reviewer, reviewer refresh), with no event system.

- `useReviewCatalogue` owns the behavior described above. [17]
- The entry's summary read and its re-validation generation. [18]

## 260921-ICR-L32 The Change-Set Read Carries Its Refusal Instead Of Discarding It

The live-leaf "committed" change-set read used to swallow its own refusal detail, so a refused read rendered
byte-identically to an unanswered one — the defect `260921-ICR-L16` routed here and R12/R24 both landed
without taking. `260921-ICR-L32` applies the R16 treatment to this client: the rejection handler in
`data/changeset.ts` no longer clears the counters and stops, it carries the refusal's own code and reason
through to the caller, and `files.ts` follows the same shape for the reader. A read that is still in flight
is a **third** state and is reported as one (`data-review-state="loading"` with its own sentence), so
"loading", "refused with a named code and reason", and "answered with counts" are three distinguishable
renderings rather than two. The owning route's cases assert the rendered code, the rendered reason, and that
the control still opens what it names.

## 260921-ICR-L25 The Change-Set Client Carries The Leaf View's Own Recordedness

`data/changeset.ts`'s `TaskChangeset` gained the leaf view's `state`/`stateDetail`, and they are what
keep an **unrecorded** range apart from a **measured empty** one (register B6). A `committed` read of a
live leaf has no landed commit to read yet; the serving route answers that state in the body rather
than refusing it with a `404`, because a `404` for a state the change-set bar probes on **every** live
leaf is a browser console error on the page whose accepted criterion is zero. The client's part is
deliberately thin and that is the point: both fields are **optional** (so the enclosure-scoped
`taskChangeset` and the master read are untouched), and `stateDetail` is the server's own sentence
carried to the caller **verbatim** rather than summarised here — one vocabulary, not two. The rendering
consequence belongs to the owning route: `panels/detail-panel/changeSetBar.tsx` shows
`unrecorded` as its own state and **withholds the `+0 −0` total**, since a zero of nothing is not a
measurement.

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
| Review client family mirror | [reviewFamily.ts](reviewFamily.ts.md) |

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it contains “No entries configured
yet,” so no Domain Documentation source was available for this route. The current statements were
verified from same-repository source/tests, the task/worker/reviewer records, and the recovered
same-repository history pack.

No relevant domain documentation was found for the data route.

### Cross-Repo References

The data route's imports and authority calls resolve inside agents-remember; no cross-repository
implementation source governs this slice. Adapter behavior is consumed through this repository's
own server contracts, so no external code path is cited as authority.

No applicable cross-repository source was found for these browser state/authority modules.

### Repo-Internal References

- Catalog/session ownership and cross-tab reconciliation. [19]
- Per-seat UI and evidence state. [20]
- Reliable submission and authoritative withdrawal. [21]
- Lifecycle termination, residuals, and landed cleanup. [22]
- Structural task hierarchy and diagnostic spawn ancestry are built as separate models. [23]
- The shared creation-order helper sorts only when every row has createdAt; unstamped task-document rows retain input order. [24]
- The one full scenario-store reset restores every projected collection, including `closeoutQueues`, in one transaction and is invoked by the development scenario player. [25]
- Series sub-task rows carry optional creation time; task-document sub-task references have a separate shape and share a union for readers. [26]
- The server series builder sorts only fully stamped rows before projection. [27]
- The generated projection mirror this route's suites build fixtures from, the manual sample used for coverage, and the fixture/projection stale gates. [28]

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

- The route's read-only client and its comparison call. [29]
- **The entry call: the task context alone, because a selector is what it is being asked for.** [30]
- **The reviewed subject as the server's catalogue lists it — presence beside the label, the count field deleted (`ICR-R09@v1`), still the entry's only legitimate selector source, with no path field on purpose.** [31]
- **The entry read's typed envelope, whose refused form carries a refusal and no entries rather than throwing, and whose answered form carries the labelled totals of the whole catalogue.** [32]
- The endpoint the comparison call reaches, with no path among its parameters. [33]
- The closed selector union, the two kinds the server admits. [34]
- The no-store-mutation boundary, stated in the module header. [35]
- The typed result the client returns unchanged. [36]
- The field-for-field mirror of the server's review payload. [37]

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

- **The inventory's wire types, including the byte form of a name this surface cannot print.** [38]
- **The comparison identity that states whether knowledge was compared, and the staleness union that gained the task-context state.** [39]
- The payload whose comparison may be absent, and the pane that says which question was answered. [40]
- **The request that omits the selector when there is none — the task-context entry.** [41]
- The surface that consumes the new types and renders the inventory — whose rows, since `260921-ICR-L3`, also open into the entry's content. [42]

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
  detail, `path_bound` (`requested_generation` / `leaf_change_set`) with its detail, `admission`
  (`changed` / `attributed_unchanged`, since 260921-ICR-L43) with its detail, and the
  `reference`/`command`; `status` is `ReviewFileStatus | "unchanged"` because an attributed unchanged
  path is expansion-only context and never an inventory entry — and `ReviewSourceContentResult`, the envelope whose `state` is `"content"`
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

- **The six-member state literal and the side value whose optional `text` is present only for the two textual states, so no missing or unrenderable side can arrive as an empty document.** [43]
- **The expansion value: both sides, both generation ids, the three-member currentness, and the `path_bound` that says which measured change set admitted the path.** [44]
- **The source-content envelope whose two states are the two answers this route gives, a refusal being a normal one.** [45]
- **The one call that reads its typed body whatever the HTTP status was, and the only one here that does not go through `getJson`.** [46]
- **The generation as an input: the caller's two published tree ids, echoed back in the spelling the route binds.** [47]
- Central expression cards and optional inline inventory expansion mount source content at the inventory exact tree IDs. [48]
- The renderer the expansion's fields feed, and its three state-decided branches. [49]

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

- **The one GET whose body is the answer whatever the status, and which returns a typed result only for a body carrying this route's `state`.** [50]
- **The only code→state table in this route, with an unknown code carried verbatim rather than guessed into a state.** [51]
- The comparison, catalogue and source-expansion clients delegate to the shared decoder. [52]
- **The shared client whose semantics are unchanged, and the change-set client that still inherits them.** [53]

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

- **The generation pins, the published generation identity, and the pins threaded through both master reads.** [54]

## 260921-ICR-L10 The Review Client Carries A Page, And One Normaliser Owns The Two Spellings Of "No Page"

`260921-ICR-L10` (`ICR-R10@v1`, complete bounded pagination) gives this route's review client the page
contract it was missing. `data/review.ts` gained `ReviewPagedCollection` (the two bounded collections,
named rather than inferred **because their cursors are different documents**), the `ReviewCollectionPage`
interface with the server's own counts, its opaque `continuation`, the active `scope` and the
`total_basis` field that says whether `total` counts the whole selection or the selection this walk still
covers, and a separate `page_refusal` on the payload for a requested page the owner could not serve.

The request gained `pageOf`, `continuation` and `pageSize`, and the client gained four small pure
functions rather than any page logic in components: `continuationOf` (what a control may offer),
`pageBounds` (one sentence per collection, worded from the basis), `carriedPage` and `RESET_GLOSS`.

**`carriedPage` is the fix a later reader must not undo.** The route serializes with
`exclude_none=True`, so a refused page **omits** the `page` key instead of sending `page: null`; a
consumer comparing `payload.page !== null` therefore never fires for a real response. One normaliser
collapses `undefined` and `null` into one value and every consumer reads through it, so the spelling of
"no page" is not a per-component decision. The reset gloss is worded from the refusal's own code, so a
cursor that is merely foreign is never called a moved comparison.

The client never constructs or parses a cursor: it echoes the server's own token back, which is what
keeps the two owners' walks distinct on the wire.

## 260921-ICR-L26 The Review Client Mirrors The Applicability Vocabulary

`260921-ICR-L26` (`ICR-R26@v1` — subject and comparison isolation on the server) reaches this route as a
**mirror, not a behaviour**: `dashboard/src/data/review.ts` (565 → 618 lines) gains the three interfaces
of the attribution half — `ReviewDisplayedApplicability` (the treatment one displayed record earned,
with its true subject and the exact references it was decided from), `ReviewContextRecord` (the labelled
context row: true subject, the recorded relationship that reached it, author/role and references, and no
judgment content) and `ReviewApplicabilitySummary` (one collection's six-way count) — plus an optional
`applicability` field on the five display types that carry a supplied record, and optional `context` and
`applicability` collections on both panes.

**Both new pane fields are optional, and the mirror keeps that.** A payload published before these
labels existed carries none of them and this client renders it unchanged: absent means "this body states
no label", never "this record is unrelated" and never "nothing was filtered". `state` is the closed
four-member union of **displayed** treatments; `context` and `unrelated` are deliberately not members, so
a name that looks like one of these unions cannot drift from the model's own vocabulary.

## 260921-ICR-L12 The Client Mirrors The One Record The Server Admits

`260921-ICR-L12` (`ICR-R12@v1`) adds one type and one optional argument to this route's review
client: `ReviewHistory = "recorded"` and `intentReview(..., history?: ReviewHistory)`. The type carries
the **one** value the server admits, so the client mirror cannot drift from the request model's own
literal and a caller cannot ask for a comparison the leaf does not hold.

**The live query string is unchanged.** `intentReview` appends `params.history` only when the argument
is defined, so every existing caller builds byte-identically the URL it built before — a property the
mounted case for the live read pins by asserting the parameter's absence rather than trusting the
branch. The record is part of the question the surface asks, which is why it is a parameter of the read
rather than a field applied to the result it returns.

## 260921-ICR-L17 The Review Client Names The Refresh Parameter Once

`260921-ICR-L17` (`ICR-R17@v1`) changes one module on this route, `data/review.ts`, in three ways:

- **a ninth `intentReview` argument** — `previousBindingDigest`, the comparison the reader was already
  looking at, carried only by a read that replaces a display. It is the *previous* identity and never a
  substitute for the current one, and the read still renders the resolved candidate's own comparison.
- **`reviewQuery`** — the query string assembled in one function, so adding a parameter cannot quietly
  raise the client's branch count and the two spellings of "absent" (`undefined`, and the empty string a
  form sends) are collapsed once.
- **`PREVIOUS_BINDING_QUERY`** — the one declaration of the wire name the server admits
  (`serving/review.py`, alias `previousBindingDigest`). It is declared once because a second spelling at
  a call site is how a refresh silently stops carrying the identity it is measured against.

Nothing else on this route changed: no other client, no transport rule and no store shape.

## 260921-ICR-L24 The Family Mirror Module And The Collection A Cursor-Less Request May Not Name

**Route meaning extended: the review client's family half is now a mirror module of its own, and the
page contract learned one collection a request may not name without a cursor.**
`dashboard/src/data/reviewFamily.ts` is new and carries the typed per-family contract `ICR-R31@v1`
publishes — the family context, the guarantee a family revision authored, the roster page and the member
rows — and `data/review.ts` re-exports every name in it, so the review payload still has one public entry
and no importer changed its path.

Three facts a reader of this route has to carry away, because each one is a place the client could have
said something the server did not:

- **`ReviewPagedCollection` gained `family_members`, and the union stays the server's own.** The member is
  listed because the SERVER accepts it; narrowing the client's union would misdescribe the wire, so the
  type is a mirror rather than the set of things this client offers.
- **`REVIEW_WALKABLE_COLLECTIONS` is the set a request may name with NO cursor, and `family_members` is
  deliberately not in it.** It is not one walk but the set of per-family roster walks a response composed,
  so a cursor-less request for it addresses no single page and the server refuses it. The family walk is
  instead continued from the cursor each family's own roster page published — the exclusion states what
  the server does with the request, not a restriction this client invented.
- **`ReviewPayload.family_context` is optional, and its ABSENCE is its own fact.** The route composes a
  family context on every answer it returns, so a body without the key did not come from this route (a
  capture recorded before the field existed, a hand-written body). It is never a measured zero and never
  rendered as `no_family_recorded`, which asserts that the recorded scope was read and held no family.

- **The new family mirror module, and the re-export that keeps `data/review.ts` the route's one public entry.** [55]
- **The bounded-collection union that lists `family_members` because the server accepts it, and the mirror that never narrows it.** [56]
- **The set a request may name with no cursor, and the reason `family_members` is not in it.** [57]
- **The optional family context whose absence says the body did not come from this route.** [58]
