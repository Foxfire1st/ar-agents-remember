# dashboard/src/data/sessions.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessions.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`       |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

## Purpose

Owns the browser's catalog-backed hosted-session registry and connection registry. Structural seat
binding is carried as a canonical task-document reference plus role; session and lifecycle ids remain
runtime correlation and do not define the seat.

## Code Commentary

### Logic

`OpenSession` mirrors the terminal catalog's structural binding. Store mutations clear duplicate live
occupants only for the same task-document-and-role pair, and `applyTaskAssignment` atomically applies
the server-accepted binding. `findSessionForTask` resolves one live occupant by structural address.
Catalog hydration maps `taskDocumentRef`, role, replacement, provenance, control, and terminal truth
without deriving identity from labels or spawn ancestry. The separate connection registry remains an
imperative PTY transport seam.

### Conventions

`seatRole` is current binding; `spawnRole` is provenance. Lifecycle lookup remains for runtime UI
correlation, while Chats grouping and targeting use task-document identity.

### Invariants And Boundaries

- Seat uniqueness is scoped to one task document and one role.
- A replacement session may occupy the same structural seat without changing its address.
- Browser state never manufactures sprint/master anchor leaves.
- Raw connection transport is not reliable structural-message delivery.

### Todos

None.

## Docs References

No Domain Documentation source is configured; repository source and tests govern this card.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The client row carries structural binding separately from runtime identity. | `OpenSession` | dashboard/src/data/sessions.ts:29-83 |
| Assignment updates and uniqueness use task-document plus role. | `applyTaskAssignment` | dashboard/src/data/sessions.ts:168-176; dashboard/src/data/sessions.ts:480-506 |
| Live lookup resolves the current occupant of a structural seat. | `findSessionForTask` | dashboard/src/data/sessions.ts:561-576 |
| Catalog hydration preserves the server-owned structural row. | `fromTerminalSessionInfo` | dashboard/src/data/sessions.ts:631-655 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T14:29+02:00 — Re-read `applyTaskAssignment` against the current L19 source and
  regenerated its citation around the public declaration and implementation; verification
  metadata remains unchanged for governed closeout.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded the sprint-provenance projection used by the
  rail and flow surfaces. Verification metadata remains pinned until closeout stamps the code
  commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T17:52+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 1 citation finding. The `RailChat`
  raw-connection-registry row now spans both `registerConnection` mounts
  (`RailChat.tsx:505-524; 559-559`), so the visible and hidden keep-alive registrations and the anchor
  sit inside the cited ranges. Scoped recheck clean.

- 2026-08-03T02:31+02:00 — W3-B01 curator: curated 15 table source citations across 13 Repo-Internal rows and 2 prose citations, replacing malformed links and unanchored claims with exact current source anchors. Verification metadata remains unchanged for closeout.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the fix-round review-N1 plural pending
  change. `OpenSession` gains the additive `controlPendingInteractions?` (multiplexed harness
  sub-agent pendings; the singular slot stays the parent-thread entry), mirrored by
  `fromTerminalSessionInfo` only-when-set; added the two sanctioned pending-state reads —
  `sessionHasPendingInteraction` (singular OR non-empty plural; the single derivation every
  attention surface must use so an agent-only-blocked seat never goes dark) and
  `sessionPendingInteractionPayload` (singular first, else first plural entry). Also re-stamped
  the stale `sessions.ts` self-citation ranges (catalog-change helpers, label allocator,
  setLeaf/applyLeafAssignment, paste/deliver) to the current source. Source is uncommitted;
  closeout re-stamps verification.

- 2026-07-24T13:17:50Z — Documented identity-preserving authoritative catalog reconciliation.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R9 UI-only field
  `OpenSession.liveTurnWorking?` — the focused seat's conversation-projection live-turn signal that
  `stateGrammar.seatVisualState` prefers over the lagging catalog `turnState`. Documented that it is
  NOT a catalog field, is never mapped by `fromTerminalSessionInfo`, is set only by `SessionsView`
  for the focused seat, and non-focused rows keep catalog turn-state. Source uncommitted; closeout
  re-stamps verification.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: replaced retired `<Chats>` connection/create/PTY
  ownership with the landed split: `RailChat` alone registers raw connections; `RailChat`,
  `HighlightComposer`, and `ChatContextBar` call `createSession`; `SessionsView`/`PtySurface` own the
  canonical full-page keep-alive path. Completed the external production `sessionStore.getState()`
  census with `GateResponder` and classified development-only `cockpitScenarios` separately. The
  former uncommitted-candidate note is now explicitly historical after landing. Verified against code commit
  `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: made `createSession` fail closed around the sole
  discriminated opener; only the accepted server row can be upserted, activated, or broadcast, and
  every failed result leaves the session store unchanged. Verification metadata remains pinned
  until closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 (R4/S2): `OpenSession` extended to the full catalog
  mirror (`createdAt`, retirement provenance, spawn level + source, requested model/effort,
  liveness evidence) with `fromTerminalSessionInfo` mapping the new fields when present, and the
  `patch` action added as the seat-event pre-apply seam (poll stays authoritative). Verification
  metadata pinned to the leaf base until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: refreshed hosted protocol projection and delivery boundary.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added authoritative binding-role state and helpers,
  made advisory/apply assignment pair-scoped, preserved different-role owners, and required
  explicit role choice for an untyped hand-opened chat.

- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): `OpenSession` and
  `fromTerminalSessionInfo` now carry landed provenance, and live-session tests treat
  `status:"landed"` as non-live. Landed rows remain in the store for inspection but release labels,
  lifecycle routing, and leaf ownership like exited rows. Verification metadata remains pinned until
  closeout stamps the HFX2-L11 commit.

- 2026-07-06T23:56:54+02:00 — 260703-L14 (visual hierarchy + chat grouping): `OpenSession` gained
  `spawnRole?` (the AR_SPAWN_ROLE recorded on the backend catalog row — the command-tree grouping
  key + role chip), carried through `fromTerminalSessionInfo` when present; no store action reads
  or mutates it. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-02T17:04+02:00 — L9: added `"leaf"` as a first-class terminal-catalog invalidation reason and
  clarified that hosted chat leaf moves update this store only after server success or catalog rehydrate.
  The `leafKey` uniqueness guard remains advisory and role-scoped, while `applyLeafAssignment` applies
  server-confirmed moves so stale local owners cannot veto the accepted catalog result. Verification
  metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — Reopened L6 paste-loss fix: `pasteDraftToSession` no longer fire-and-forgets —
  it delegates to `data/terminal.ts`'s `pasteAndConfirm` (echo-confirmed, quiet-gated attempts retried
  over a 30s boot deadline) so a draft dropped into a booting Claude Code is retried instead of silently
  lost, and `"delivered"` is only reported once the composer echoed the paste. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-07-02T13:07+02:00 — Reopened L6 follow-up: added the draft-paste delivery seam for leaf-context
  handoff. `pasteDraftToSession` uses the existing connection wait and sanitizing bracketed-paste path but
  deliberately does not call the submit/confirm loop, so an operator can append their own instruction
  before pressing Enter. Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: leaf uniqueness is now per **(leaf, role)**. Added `SessionRole` +
  `sessionRole(session)` (a `kind:"terminal"` shell is a terminal, any harness is a chat, mirroring the
  backend `role_for_kind`); the `setLeaf` advisory guard is role-scoped (a chat and a terminal can both
  bind one leaf), and `findSessionForLeaf(leafKey, role?)` gained an optional role filter so the leaf's chat
  and terminal resolve independently. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added durable leaf identity to the session registry. `OpenSession`
  gained an optional `leafKey` (qualified leaf id); `setLeaf(id, leafKey|null)` binds/clears it with an
  advisory local-uniqueness guard (server `409 leaf-taken` is the real arbiter) and a `clearLeaf` helper;
  `findSessionForLeaf(leafKey)` returns the single live bound session; `fromTerminalSessionInfo` maps
  `leafKey`; and `createSession` takes a `leafKey` it forwards to the opener and stamps on the row.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-27T03:04+02:00 — Task 22 follow-up: removed the hidden-live label reservation state now that
  the UI no longer exposes Hide, and extended catalog-change broadcasts with `sessionId` so other tabs
  can remove the terminated row deterministically before rehydrating.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: added `BroadcastChannel` catalog-change helpers and made
  `createSession` broadcast a `"create"` invalidation only after the backend opener succeeds. Other tabs
  subscribe through `Chats` and re-fetch the durable catalog instead of sharing local store state.
  Verification metadata pinned until closeout stamps the task-22 follow-up code commit.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: replaced the old monotonic/global label-counter model
  with per-prefix lowest-available labels. Locally hidden live rows reserve their label until refresh,
  while terminated/exited rows release it so new Claude chats can restart at `Claude Code 1`.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: updated the store comments/docs for mount-on-first-selection
  terminal attachment; restored inactive rows wait until visible, while visited rows remain mounted.
- 2026-06-26T23:05+02:00 — Task 22: extended `OpenSession` with kind/harness/status, added
  `upsert`/`hydrate`/`setStatus` and catalog-row conversion, made lifecycle lookup ignore
  exited/terminated rows, and changed `createSession` to send the generated label/lifecycle to the
  backend opener before registering a running row. Verification metadata pinned until closeout stamps
  the task-22 code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: corrected the external-chat boundary now that non-hosted chats use the operator inbox path instead of a future inbox/poll placeholder. No source change in `sessions.ts`; this is current-state memory correction after task 10 completed the fallback.
- 2026-06-23T13:45+02:00 — Task 11: added hosted chat ⇄ lifecycle identity. `OpenSession` now carries
  optional `lifecycleId`; `add`/`createSession` accept it, `setLifecycle` attaches/clears it, and
  `findSessionForLifecycle` gives the Gate Respond path one chat target per lifecycle. Also refreshed
  the delivery commentary to describe `deliverToSession`'s confirmed bracketed-paste path. Verification
  metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-19T15:59 — Task 6 slice 6f-1: made the store the cockpit-wide **inject seam** — added a non-reactive connection registry (`registerConnection` / `sendToSession`, with a `pending` queue for the create-then-send race), `createSession` (the shared spawn), and `sendWhenReady` (waits for the connection + the harness's `whenReady` before injecting, so a fresh agent doesn't drop the package mid-boot). `<Chats>` now registers connections here instead of a local ref. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05 — Created for task 6 slice 6e-4: the session registry extracted from `Chats` local state into a module-level zustand store (`sessions`/`activeId`/`count` + `add`/`close`/`setActive`, `useSessions` selector hook) so the session list is shared + testable and `Chats` can keep every session's terminal mounted. Verification metadata pinned until closeout stamps the 6e-4 code commit.
