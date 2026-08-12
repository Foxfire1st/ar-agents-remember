# dashboard/src/panels/HighlightComposer.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/HighlightComposer.tsx`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T23:40+02:00 |
| lastVerifiedCommitHash | `65cb81f7de4db13c0627264fec1eb46f444e0ee3`       |
| lastVerifiedCommitDate | 2026-08-12T04:57:26+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels overview](overview.md)

## Purpose

The slice-6f **"send a context package by highlighting"** composer, migrated by FEUI-L5 to the
reliable whole-message submission path. Every selection raises the same
small **Add to chat** pill — a selection alone never sends anything (the L8-r1 correction: the earlier
auto-paste-on-selection was invisible and fired on unintended highlights). What differs is what the
pill CLICK does. When the captured selection came from the displayed task leaf and the right rail is
actively showing that leaf's live chat, the click submits the context through the same reliable
session-text client rather than PTY paste. Otherwise the click opens the generic composer stage, and
Send delivers to a chosen/open/new chat, waiting for a newly created bridge to become ready when
necessary. The composer lives on a snapshot from
`useSelectionCapture`, so clicking into the message box never dismisses it. Mounted once in
`CockpitShell`; lifecycle-aware target filtering still limits generic open-chat targets to sessions
tagged with `selectedLifecycleId` when present. Request ids, ambiguous response loss, and endgame
copy follow the same no-blind-resend contract as the shared composer.

## Code Commentary

### FEUI MX-FIX-2 Create-Result Gate

When the chosen target requires a new harness session, `send()` now branches on the discriminated
create result. A failure renders `terminalOpenFailureMessage(result)` and returns before readiness,
submission, route change, or selection clearing. Only `result.session.id` from an accepted server
row reaches `waitForSubmissionReady` and the reliable submit path.

### Stable Pre-Projection Store Snapshot

The dashboard mounts this composer before the first analytics projection can arrive. Its
`useDashboard` task-document selector therefore falls back to the module-level
`EMPTY_TASK_DOCUMENTS` array, whose identity stays stable while the store is unchanged. Returning a
fresh `[]` from the selector violates React's external-store snapshot contract and causes an empty
dashboard to loop through forced store rerenders until React raises maximum-update-depth error 185.

### Logic

Driven by `useSelectionCapture()` (`data/selection`) — renders `null` with no snapshot. If
`selection.leafKey` equals the `viewedLeafKey` supplied by `CockpitShell`, `leafChatActive` is true, and
`findSessionForLeaf(viewedLeafKey, "chat")` finds a live chat, that session becomes `directLeafChat`:
the pill's `onPress` then calls `directSubmit(id)` behind a `sendingRef` in-flight guard. It submits
the context with `source: "highlight"` through the shared reliable client; accepted/queued commits
finish, while rejection, route error, or unresolved endgame keeps the selection and opens/retains the
generic composer with honest recovery copy. Without a `directLeafChat`, the pill click opens the
composer stage as before.

The fallback path uses a fixed-position 0-area `<span>` at the snapshot rect as the React Aria
`Popover` trigger. The `Popover` is controlled (`isOpen` while a snapshot exists) and
`onOpenChange(false)` (outside-click / Escape) → `dismiss()` = `clear()` + back to the pill. A `mode`
(`"pill" | "composer"`), reset to `"pill"` whenever the snapshot changes, drives the stages: **pill** is
a single **Add to chat** button; **composer** renders the captured selection (`<pre>`), the **target
control**, an autofocused message `TextField`/`TextArea` (**Enter = send + submit**, **Shift+Enter =
newline**), and **Send**.

**Target** — one React Aria `ToggleButtonGroup` lists running harness chats **and** a create option per
**detected** harness (`fetchHarnesses` on mount: ＋ Claude Code / ＋ Codex / …). Raw terminals are not
submission targets. The default is the active routed chat, else the first routed chat, else the first
detected harness create option.
When `selectedLifecycleId` is set, "open chats" means sessions whose `lifecycleId` matches; create
targets pass that lifecycle to `createSession`.
**`send()`** resolves the selected target: an open chat → `setActive` + deliver; a create option →
`createSession(prefix, "harness", harnessId, selectedLifecycleId?)`, then waits for native submission
readiness. Only an accepted server row supplies the id. `submitSessionText` owns the exact request id,
highlight provenance, route-error retry, and ambiguous endgame reconciliation. `finish()` dismisses,
activates the target, and invokes `onSent` only after accepted/queued truth; every other outcome leaves
route, selection, and operator composer draft intact.

### Conventions

React Aria primitives (`Popover`/`Dialog`/`Button`/`TextField`/`TextArea`/`ToggleButton(Group)`) +
co-located Panda `css` (the amber/grid cockpit look) — the cockpit's first overlay. The pill is a quiet
content-sized grid-bordered bar (`dialogPill`); the composer is a **fixed-width** box (`dialogComposer`,
so it never tracks the selection's width) with the amber active border. The message `TextArea` has a
5rem min-height + a vertical resize handle. `data-highlight-composer` marks the dialog so
`data/selection` ignores selections + mouse-ups inside it.

### Invariants And Boundaries

Both paths keep the no-silent-action invariant: a selection only raises the pill, and nothing is
submitted before an explicit click. The direct path acts on the pill click alone only when the
selected DOM was tagged with the same leaf the visible rail chat is serving, and keeps one consistent
"Add to chat" label. The composer persists until
outside-click/Escape or Send in fallback mode (snapshot-driven, not live-selection-driven). Delivery
uses the reliable native-control submission client, never PTY paste. With a selected lifecycle,
unrelated open chats are not offered; the create target becomes the routeable chat. Before analytics
exists, selector fallbacks must remain referentially stable so this always-mounted surface cannot
create a `useSyncExternalStore` update loop.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The mouse-up selection snapshot it attaches to, including optional task leaf metadata. | `SelectionContext` | dashboard/src/data/selection.ts:9-16 |
| Session creation supplies only accepted server ids; task-document lookup supplies structurally routed targets. | `createSession`; `findSessionForTask` | dashboard/src/data/sessions.ts:561-573; dashboard/src/data/sessions.ts:783-802 |
| Reliable highlight submission, readiness, same-id retry, and endgame reconciliation. | `submitSessionText`; `retryRouteFailure`; `keepWaitingForSubmit`; `waitForSubmissionReady` | dashboard/src/data/submitClient.ts:828-873; dashboard/src/data/submitClient.ts:889-907; dashboard/src/data/submitClient.ts:921-949; dashboard/src/data/submitClient.ts:952-976 |
| Harness discovery supplies detected create options. | `fetchHarnesses` | dashboard/src/data/terminal.ts:391-393 |
| Cockpit supplies `viewedLeafKey` and whether the right rail is actively showing chat. | "leafKey={viewedLeafKey}" | dashboard/src/cockpit/Cockpit.tsx:687-687 |
| The behavior tests cover direct leaf paste and fallback routing. | "direct leaf pill click submits through /submit; selection alone never acts"; "keeps a rejected direct submit visible with the verbatim detail" | dashboard/src/panels/HighlightComposer.test.tsx:380-420; dashboard/src/panels/HighlightComposer.test.tsx:422-457 |
| The pre-projection task-document selector uses one stable empty snapshot, and its focused regression rejects React's uncached-snapshot warning. | `EMPTY_TASK_DOCUMENTS`; "keeps the pre-projection task-document snapshot stable" | dashboard/src/panels/HighlightComposer.tsx:52-55; dashboard/src/panels/HighlightComposer.test.tsx:140-153 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

Highlight delivery now calls the reliable session-text client with `highlight` provenance. Existing
targets submit through the exact bridge; newly created targets wait for submission readiness. A
possible-post-write loss stays ambiguous and enters the same reconcile/endgame UI instead of falling
back to paste or minting a second request.

## FEUI-L8 Reviewed Candidate Delta

Target selection is provisional. `finish` commits `activeId` and calls `onSent(sessionId)` only after accepted/queued reliable delivery; every refusal or ambiguous endgame leaves the operator's current route/focus untouched.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Current L5I Maintenance

The persistent highlight composer is now memoized. Unchanged shell props on a cockpit view switch
skip its subtree while its own local and store-backed state still updates normally.

## Update History

- 2026-08-12T04:04+02:00 — Documented the stable pre-projection task-document snapshot that prevents
  the always-mounted composer from entering React's external-store update loop; added the focused
  empty-analytics regression evidence. Verification metadata remains pinned until governed closeout.

- 2026-08-11T23:40+02:00 — No content impact: `directLeafChatFor` now delegates the running-harness
  validation, but direct highlight submission still requires the current structurally selected
  chat and the reliable explicit-click path described above. Verification metadata remains pinned
  until governed closeout.

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `HighlightComposer.tsx` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 5 citation claims; scoped recheck clean (0 findings).

- 2026-07-24T13:17:17Z — Curator: documented the persistent-composer memo boundary; verification
  fields remain pre-commit.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: gated new-target highlight delivery on the accepted
  server session id and surfaced typed open failure before readiness or submit. Verification
  metadata remains pinned until closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: replaced highlight PTY paste with reliable, provenance-aware
  create-ready submission and no-resend endgame handling.

- 2026-07-02T20:55+02:00 — L8-r1 correction (developer feedback): the direct leaf-chat path no longer
  auto-pastes on selection and no longer hides the pill — every selection raises the same "Add to chat"
  pill, and only the pill CLICK routes: direct draft paste when the obvious leaf-chat target exists
  (selector/message box skipped), generic composer otherwise; an unconfirmed direct paste opens the
  composer. Restores the visible-intentional-interaction invariant the auto-paste had broken.
  Verification metadata pinned until closeout stamps the L8-r1 commit.
- 2026-07-02T16:18+02:00 — L8: added the direct leaf-chat draft-paste route. When the selection's
  captured `leafKey` matches the displayed leaf and the right rail is actively showing that leaf's live
  chat, the component calls `pasteDraftToSession` and renders no Add-to-chat UI; unconfirmed draft paste
  falls back to the generic composer. The generic path still uses `deliverToSession` and submits only on
  explicit Send.
- 2026-06-23T13:45+02:00 — Task 11: `HighlightComposer` accepts `selectedLifecycleId`; open-chat
  targets are filtered to sessions tagged with that lifecycle, and create targets pass the lifecycle
  to `createSession` so new hosted chats become routeable for Gate Respond. Verification metadata pinned
  until closeout stamps the task-11 code commit.
- 2026-06-19T15:59 — Created for task 6 slice 6f-1: the two-stage highlight→context-package composer — an "Add to chat" pill on a mouse-up selection → a fixed-width composer box (snapshot-driven so clicking into it doesn't dismiss it; 5rem-min resizable message box; Enter=send+submit / Shift+Enter=newline). The target control lists open chats + a create option per **detected harness** (＋ Claude Code / ＋ Codex / ＋ Terminal), defaulting to an agent not a shell; delivery dismisses the composer immediately and runs in the **background**, gated on the harness being ready (`sendWhenReady` → `whenReady`) so a fresh agent doesn't drop the package mid-boot (two stdin frames: bracketed paste + Enter). Verification metadata pinned until closeout stamps the 6f-1 code commit.
