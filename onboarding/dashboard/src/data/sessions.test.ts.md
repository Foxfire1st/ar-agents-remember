# dashboard/src/data/sessions.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessions.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T16:02+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Unit tests for the `sessions` store (slice 6e-4): they pin the registry contract consumed by the
canonical session cockpit, contextual `RailChat`, highlight delivery, and gate routing — `add`
labels by lowest available per-prefix ordinal and activates, `close` forgets and
clears the active pointer only when the closed id was active, `setActive` repoints.
The reopened-L6 pass pins `pasteDraftToSession`'s confirmed-delivery contract under fake timers:
`"delivered"` only once the fake connection's `lastOutputAt` advances (the draft echo) with one paste
and no Enter, and `"unconfirmed"` with bounded retries and still no `\r` when nothing ever echoes.
Task 11 adds lifecycle identity tests for attach, clear, uniqueness, and lookup by lifecycle id. Task 22
adds catalog-hydration tests for server-owned sessions, live-only lifecycle routing, status-driven
focus changes, API-row conversion, and `createSession` sending label/lifecycle metadata to the opener.
Since 260715-FEUI-L2 the three exact-shape `toEqual` API-row conversion fixtures (the terminal row,
the harness row, and the landed row) also demand the mapped **`createdAt`** field —
`fromTerminalSessionInfo` now carries it for the cockpit's smart-focus/jump ordering fallbacks, so
the shape assertions were STRENGTHENED by one required-correct field each (no assertion weakened;
mapping behavior otherwise unchanged, reviewer-verified line-by-line).
It also covers the tab-sync helpers that broadcast id-bearing catalog invalidations after persisted
backend changes. Slice L5 adds the parallel **leaf identity** tests: `setLeaf`/`findSessionForLeaf`
advisory uniqueness, freeing a leaf after the owner exits, clearing a binding, and `leafKey` mapping
through `fromTerminalSessionInfo`. The L5 fix pass makes that uniqueness **role-scoped** (per leaf+role):
the advisory-reject case exercises two same-role chat sessions, `findSessionForLeaf` accepts an optional
role filter, and the catalog-row mapping case carries a `kind: "terminal"` row.
The reopened L6 follow-up adds draft-paste coverage for leaf context: `pasteDraftToSession` must sanitize
and bracket the package without adding the submit/Enter step that `deliverToSession` performs. L9 extends
the catalog-sync coverage so a remote `"leaf"` invalidation is delivered with the moved session id, while
this tab's own catalog broadcast remains ignored by subscribers.

## Code Commentary

### FEUI MX-FIX-2 Zero-Ghost Regression Matrix

The create suite now returns an accepted server row rather than a boolean and proves exact-one
materialization/broadcast on success. Network, HTTP, harness-refusal, missing-body, malformed-body,
and contradictory raw-harness responses each leave `sessions=[]`, `activeId=null`, and the catalog
broadcast list empty. The Round 1 identity correction is pinned at the store boundary as well as in
the parser suite.

### FEUI-L9R Reviewed Candidate Delta

The local `TerminalConnection` fake now supplies the additive `reattach()` interface and returns
`false`. Session-store behavior is otherwise unchanged; this is an intentional interface-seam
update, not restart-behavior coverage.

### 260707-HFX2-L17 Client Pair-State Regressions

Tests cover `seatRole` hydration, binding-first role derivation, explicit selection for an untyped
chat, same-role replacement on assignment, and preservation of different-role seats sharing one
leaf.

### Logic

Drives `sessionStore.getState()` directly (no React): asserts `add(prefix, id)` appends
`{id, label: "${prefix} ${n}"}` using the lowest available live ordinal for that prefix, and sets
`activeId`; that `close` removes the session and nulls `activeId` only when the closed id was active;
and that `setActive` repoints. Task 11 cases assert `add(prefix, id, lifecycleId)`, `setLifecycle`,
clearing, duplicate lifecycle ownership, and `findSessionForLifecycle`. Resets the store between cases.
Slice L5 cases assert `setLeaf` binds a `leafKey`; a second `setLeaf` for the same leaf on a different
**live, same-role** session is rejected as a no-op (the role-scoped advisory uniqueness — both
`add("Chat", …)` rows are chat-role since `add` sets no `kind`) while the same leaf can be re-bound once
the prior owner is `exited`/`terminated` (free-after-exit, via `findSessionForLeaf` resolving only live
rows); `setLeaf(id, null)` clears the binding; and `fromTerminalSessionInfo` carries `leafKey` onto a
`kind: "terminal"` store row. L9 adds `applyLeafAssignment` coverage proving a server-authoritative move can
override a stale same-role local owner after the backend accepts the assignment. (`findSessionForLeaf` now accepts an optional role filter; the per-(leaf,
role) cross-role coexistence is pinned server-side in `test_terminal_catalog.py` / `test_terminal_ws.py`.)
Task 22 cases assert `hydrate` preserves a preferred live active id
and updates `count`, exited rows do not resolve through `findSessionForLifecycle`, `setStatus` moves
focus away from an exited active session, terminated rows release their chat labels after local removal,
`fromTerminalSessionInfo` maps API rows to store rows, and `createSession` POSTs the generated
label/lifecycle before registering only the accepted server-owned running row. The catalog-sync suite stubs `BroadcastChannel` with `FakeBroadcastChannel`, asserts subscribers
receive another tab's L9 `"leaf"` event with its `sessionId` while ignoring this tab's own `"create"`
broadcast, and asserts `createSession` broadcasts `"create"` only after an accepted result; the
MX-FIX-2 table proves every failure class leaves registry, active id, and broadcasts empty. A
second suite
(slice 6f) covers the **connection
registry + delivery**: with a controllable fake `TerminalConnection`, `sendToSession` queues into
`pending` and flushes in order on `registerConnection`; `deliverToSession` waits for a late
registration (the create-then-send race), then injects exactly ONE
`bracketedPaste(sanitizeForInjection(text))` (sanitized AND wrapped) and resolves `"delivered"` once
the fake's output clock advances past the post-CR-echo baseline; and a never-registering session
resolves `"unconfirmed"` (never hangs) after the connection timeout (driven with fake timers). The L6
follow-up adds a paired draft case that registers a live fake connection, calls `pasteDraftToSession`, and
asserts the only injected input is the sanitized bracketed paste — no trailing newline or confirmation
submit. **HFX2-L11** adds two `status:"landed"` cases: hydrating a `"landed"` row still resolves
`findSessionForLifecycle` as `undefined` (landed is deliberately not a live/routable status, alongside
`"exited"`), and hydrating a `"landed"` owner on a leaf frees that leaf immediately so a fresh session can
bind it (`findSessionForLeaf` returns `undefined` for a landed owner, then a new `add`+`setLeaf` succeeds) —
plus a `fromTerminalSessionInfo` conversion case round-tripping the full landing-provenance field set
(`landedAt`/`landedReason`/`landedEdge`/`spawnedBySession`/`spawnedByLifecycle`/`spawnedLabel`/`turnState`/
`turnStateChangedAt`) from catalog JSON into the store row shape unchanged.

### Conventions

Vanilla-store testing — exercise `getState()` actions and assert the next state, no renderer.

### Invariants And Boundaries

Pure state tests; no DOM, no real backend. `BroadcastChannel` and `fetch` are stubbed when catalog-sync
or opener behavior is under test. Mounted-but-hidden terminal persistence is covered by
`session-cockpit/PtySurface.test.tsx`, `session-cockpit/SessionsView.test.tsx`, and the Cockpit S5
route test; the deleted `panels/Chats.test.tsx` is not a current coverage owner. The draft-paste
regression stays at the connection seam, where the suite can prove no submit input was appended.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

### 2026-07-24 Curator Delta

New reconciliation cases assert zero subscriber work for an identical poll, stable references for
unchanged rows in a mixed payload, and replacement of an optimistic local patch by the next catalog row.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The catalog-change helper accepts and forwards the L9 `"leaf"` reason for reassignment invalidation. | L32-L85 | [data/sessions.ts](sessions.ts) |
| The L9 store test proves server-authoritative `applyLeafAssignment` overrides a stale same-role local owner. | L202-L212 | [sessions.test.ts](sessions.test.ts) |
| The catalog-sync test now receives a remote `"leaf"` event and ignores the sender tab's own broadcast. | L315-L336 | [sessions.test.ts](sessions.test.ts) |
| The store and delivery helpers under test, including the separate draft-paste and submit-and-confirm paths. | L433-L459 | [data/sessions.ts](sessions.ts) |
| The connection-registry suite covers pending sends, submit-and-confirm delivery, draft paste without Enter, and timeout behavior. | L364-L417 | [sessions.test.ts](sessions.test.ts) |
| `PtySurface` pins visited-pane identity and hidden keep-alive behavior across focus changes and transient handoff. | L87-L160 | [PtySurface.test.tsx](../panels/session-cockpit/PtySurface.test.tsx) |
| `SessionsView` pins the full cockpit composition, hidden keyboard boundary, and focus/inspection handoff. | L65-L108; L279-L319; L647-L674 | [SessionsView.test.tsx](../panels/session-cockpit/SessionsView.test.tsx) |
| Cockpit S5 pins the one persistent `sessions-view` owner behind the Chats product label. | L640-L667 | [Cockpit.test.tsx](../cockpit/Cockpit.test.tsx) |

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-24T13:17:50Z — Added catalog reconciliation identity regression coverage. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: replaced the deleted Chats test/view ownership with the
  current session-cockpit consumers and the `PtySurface`, `SessionsView`, and Cockpit S5 keep-alive
  coverage chain. Verified against code commit `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: added exact accepted-row creation and the zero-ghost
  failure table, including the Round 1 contradictory raw harness/control response; no failed open
  can mutate, activate, or advertise. Verification metadata remains pinned until closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: documented the inert fake connection seam for the new explicit
  reattach method; verification metadata remains pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2: three exact-shape `toEqual` catalog-conversion fixtures
  gained the one `createdAt` field `fromTerminalSessionInfo` now maps (needed by the cockpit's
  smart-focus/jump ordering fallbacks) — assertions STRENGTHENED (one more correct field
  demanded), none weakened; reviewer-verified line-by-line. Verification metadata pinned to the
  leaf base until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added binding-role helper, hydration, and pair-scoped
  assignment regressions including different-role coexistence.

- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive): added coverage confirming `isLiveSession`
  stays `status==="running"` only (a landed row is deliberately NOT "live") and pins the new
  `status:"landed"` shape (landing provenance fields) round-tripping through the session data layer
  consistently with the terminal-catalog model. Verification metadata pinned until closeout stamps
  the 260707-HFX2-L11 commit.
- 2026-07-02T17:04+02:00 — L9: updated catalog-sync coverage to assert remote `"leaf"` invalidations for
  moved hosted chats are delivered with their session id while local broadcasts are still ignored, and
  added `applyLeafAssignment` coverage for server-authoritative moves over stale local owners. Verification
  metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — Reopened L6 paste-loss fix: the `pasteDraftToSession` case now runs under
  fake timers and pins confirmed-delivery semantics — `"delivered"` only after the fake connection's
  `lastOutputAt` advances (the draft echo), one paste and no Enter; a new case pins `"unconfirmed"`
  after the 30s boot deadline with retries and still no `\r`. Verification metadata pinned until
  closeout stamps the follow-up commit.
- 2026-07-02T13:07+02:00 — Reopened L6 follow-up: added a regression case for `pasteDraftToSession`.
  The fake connection receives exactly one sanitized bracketed paste and no submit input, proving leaf
  context can land as editable draft text. Verification metadata pinned until closeout stamps the follow-up
  commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: clarified that the store's leaf uniqueness is now **role-scoped** — the
  advisory-reject case exercises two same-role (chat) sessions, `findSessionForLeaf` gained an optional
  role filter, and the catalog-row mapping case uses a `kind: "terminal"` row. The cross-role (chat +
  terminal share a leaf) coexistence is pinned in the Python catalog/route tests. Verification metadata
  pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added leaf-identity coverage for the session store — `setLeaf` binding,
  advisory uniqueness reject against a live owner, free-after-exit re-binding once the owner is
  exited/terminated, `setLeaf(id, null)` clearing, and `fromTerminalSessionInfo` `leafKey` mapping.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-27T03:04+02:00 — Task 22 follow-up: removed hidden-live reservation coverage with the Hide
  state, and updated catalog-sync assertions to require `sessionId` on create/terminate broadcasts.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: added `BroadcastChannel` fake coverage for catalog-change
  subscription/broadcast behavior and for `createSession` broadcasting `"create"` only after the backend
  opener succeeds. Verification metadata pinned until closeout stamps the task-22 follow-up code commit.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: changed session-label tests from monotonic/global ordinal
  coverage to per-prefix lowest-available allocation, including terminated rows releasing labels and
  hidden live rows reserving labels until hydration.
- 2026-06-26T23:05+02:00 — Task 22: added catalog hydration, live-only lifecycle lookup, status focus
  handoff, API-row conversion, and createSession opener-metadata coverage. Verification metadata pinned
  until closeout stamps the task-22 code commit.
- 2026-06-23T13:45+02:00 — Task 11: added lifecycle identity tests for route lookup, one owning session
  per lifecycle, and explicit tag clearing. Verification metadata pinned until closeout stamps the
  task-11 code commit.
- 2026-06-19T20:30 — Task 6 slice 6f: added the connection-registry + `deliverToSession` suite (a fake `TerminalConnection`: `sendToSession` pending-queue flush on register, the create-then-send race resolving once registered with one sanitized+wrapped paste injected, and the bounded-wait timeout resolving `"unconfirmed"` instead of hanging). Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-19T14:05 — Created for task 6 slice 6e-4: unit tests for the new session store (add/close/setActive + ordinal stability). Verification metadata pinned until closeout stamps the 6e-4 code commit.
