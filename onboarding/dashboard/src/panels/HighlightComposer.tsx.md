# dashboard/src/panels/HighlightComposer.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

The slice-6f **"send a context package by highlighting"** composer, migrated by FEUI-L5 to the
reliable whole-message submission path. Every selection raises the same
small **Add to chat** pill — a selection alone never sends anything (the L8-r1 correction: the earlier
auto-paste-on-selection was invisible and fired on unintended highlights). The pill click now always
opens the generic composer stage (the older direct leaf-chat target was removed with the rail panel
by MIK-R95 rule 8), and
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

The direct leaf-chat branch and its pre-projection task-document fallback (`EMPTY_TASK_DOCUMENTS`) were removed with the old rail panel (MIK-R95 rule 8). The surviving composer is still always mounted, and its state is snapshot-driven; it keeps no module-level task-document selector and cannot force React into an external-store update loop.

### Logic

Driven by `useSelectionCapture()` (`data/selection`) — renders `null` with no snapshot. The pill click opens the composer stage; `send` resolves the chosen target and delivers the context with `source: "highlight"` through the shared reliable client. Accepted/queued commits finish, while rejection, route error or unresolved endgame keeps the selection and retains the generic composer with honest recovery copy. The removed direct path (`directLeafChat`/`directSubmit`) acted on a rail leaf chat that no longer exists.

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

The surviving path keeps the no-silent-action invariant: a selection only raises the pill, and nothing is
submitted before an explicit click, with one consistent
"Add to chat" label. The composer persists until
outside-click/Escape or Send in fallback mode (snapshot-driven, not live-selection-driven). Delivery
uses the reliable native-control submission client, never PTY paste. With a selected lifecycle,
unrelated open chats are not offered; the create target becomes the routeable chat. Before analytics
exists, selector fallbacks must remain referentially stable so this always-mounted surface cannot
create a `useSyncExternalStore` update loop.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The mouse-up selection snapshot it attaches to, including optional task leaf metadata. [1]
- Session creation supplies only accepted server ids; task-document lookup supplies structurally routed targets. [2]
- Reliable highlight submission, readiness, same-id retry, and endgame reconciliation. [3]
- Harness discovery supplies detected create options. [4]

- The behavior tests cover fallback routing through the generic composer. [6]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

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

## MIK-R95 Direct Leaf-Chat Target Removed

Rule 8 removed the old rail panel, and the composer's direct-target branch went with it: `directLeafChatFor`, `runningHarnessSession`, the `leafChatActive`/`viewedLeafKey`/`taskDocuments` inputs and the direct-submit plumbing are gone, so the pill click always opens the composer stage and delivery uses the same reliable client and target list as before. No selection is sent without the explicit click.
