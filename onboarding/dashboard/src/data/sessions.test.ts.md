# dashboard/src/data/sessions.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Unit tests for the `sessions` store (slice 6e-4): they pin the registry contract consumed by the
canonical session cockpit, highlight delivery, and gate routing — the removed contextual `RailChat`
also consumed it before MIK-R95 — `add`
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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No relevant domain documentation was found for this file.

### Repo-Internal References

- The catalog-change helper accepts and forwards the L9 `"leaf"` reason for reassignment invalidation. [1]
- The store test proves server-authoritative `applyTaskAssignment` overrides a stale same-role local occupant of the document-owned seat. [2]
- The catalog-sync test now receives a remote `"leaf"` event and ignores the sender tab's own broadcast. [3]
- The store and delivery helpers under test, including the separate draft-paste and submit-and-confirm paths. [4]
- The connection-registry suite covers pending sends, submit-and-confirm delivery, draft paste without Enter, and timeout behavior. [5]
- `PtySurface` pins visited-pane identity and hidden keep-alive behavior across focus changes and transient handoff. [6]
- `SessionsView` pins the full cockpit composition, hidden keyboard boundary, and focus/inspection handoff. [7]
- Cockpit S5 pins the one persistent `sessions-view` owner behind the Chats product label. [8]

#### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
