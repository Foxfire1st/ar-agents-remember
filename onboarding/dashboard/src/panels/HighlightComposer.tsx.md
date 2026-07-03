# dashboard/src/panels/HighlightComposer.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/HighlightComposer.tsx`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-02T20:55+02:00                           |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`       |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The slice-6f **"send a context package by highlighting"** composer. Every selection raises the same
small **Add to chat** pill — a selection alone never sends anything (the L8-r1 correction: the earlier
auto-paste-on-selection was invisible and fired on unintended highlights). What differs is what the
pill CLICK does. When the captured selection came from the displayed task leaf and the right rail is
actively showing that leaf's live chat, the click pastes the context block directly into that chat's
draft with no target selector, no message box, and no Enter/submission. Otherwise the click opens the
generic composer stage, and Send delivers to a chosen/open/new chat. The composer lives on a snapshot from
`useSelectionCapture`, so clicking into the message box never dismisses it. Mounted once in
`CockpitShell`; lifecycle-aware target filtering still limits generic open-chat targets to sessions
tagged with `selectedLifecycleId` when present.

## Code Commentary

### Logic

Driven by `useSelectionCapture()` (`data/selection`) — renders `null` with no snapshot. If
`selection.leafKey` equals the `viewedLeafKey` supplied by `CockpitShell`, `leafChatActive` is true, and
`findSessionForLeaf(viewedLeafKey, "chat")` finds a live chat, that session becomes `directLeafChat`:
the pill's `onPress` then calls `directPaste(id)` —
`pasteDraftToSession(id, buildContextPackage({selectionText}))` behind a `sendingRef` in-flight guard
(the pill disables while `status === "sending"`) — and clears the selection after a confirmed draft
paste, never entering the composer stage. An unconfirmed direct paste opens the generic composer for
the same selection instead of dying silently. Without a `directLeafChat`, the pill click opens the
composer stage as before.

The fallback path uses a fixed-position 0-area `<span>` at the snapshot rect as the React Aria
`Popover` trigger. The `Popover` is controlled (`isOpen` while a snapshot exists) and
`onOpenChange(false)` (outside-click / Escape) → `dismiss()` = `clear()` + back to the pill. A `mode`
(`"pill" | "composer"`), reset to `"pill"` whenever the snapshot changes, drives the stages: **pill** is
a single **Add to chat** button; **composer** renders the captured selection (`<pre>`), the **target
control**, an autofocused message `TextField`/`TextArea` (**Enter = send + submit**, **Shift+Enter =
newline**), and **Send**.

**Target** — one React Aria `ToggleButtonGroup` lists open chats **and** a create option per
**detected** harness (`fetchHarnesses` on mount: ＋ Claude Code / ＋ Codex / …) plus a plain `＋
Terminal` shell. The default is the active chat, else the first open chat, else the first create option
— a detected harness (an agent), **never silently a shell**, so the package doesn't go into the void.
When `selectedLifecycleId` is set, "open chats" means sessions whose `lifecycleId` matches; create
targets pass that lifecycle to `createSession`.
**`send()`** resolves the selected target: an open chat → `setActive` + deliver; a create option →
`createSession(prefix, "harness"|"terminal", harnessId?, selectedLifecycleId?)` then deliver. The
always-sendable minimum holds because there is always a default. Send builds the package, resolves the
target, and calls `deliverToSession(id, pkg)`, which bracket-pastes and submits through the terminal
confirmation path; on `delivered`, `finish()` dismisses and `onSent?.()` switches to Chats. Direct
leaf-chat paste deliberately uses `pasteDraftToSession`, not `deliverToSession`, so it never synthesizes
Enter.

### Conventions

React Aria primitives (`Popover`/`Dialog`/`Button`/`TextField`/`TextArea`/`ToggleButton(Group)`) +
co-located Panda `css` (the amber/grid cockpit look) — the cockpit's first overlay. The pill is a quiet
content-sized grid-bordered bar (`dialogPill`); the composer is a **fixed-width** box (`dialogComposer`,
so it never tracks the selection's width) with the amber active border. The message `TextArea` has a
5rem min-height + a vertical resize handle. `data-highlight-composer` marks the dialog so
`data/selection` ignores selections + mouse-ups inside it.

### Invariants And Boundaries

Both paths keep the no-silent-action invariant: a selection only raises the pill, and nothing is pasted
or sent before an explicit click. The L8 direct path acts on the pill click alone — only when the
selected DOM was tagged with the same leaf the visible rail chat is serving — drafts without ever
synthesizing Enter, and keeps one consistent "Add to chat" label. The composer persists until
outside-click/Escape or Send in fallback mode (snapshot-driven, not live-selection-driven). Delivery
reuses the live B2 `{type:stdin}` channel via `data/sessions` — no new transport, not ACP. With a
selected lifecycle, unrelated open chats are not offered; the create target becomes the routeable chat.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The mouse-up selection snapshot it attaches to, including optional task leaf metadata. | L9-L44 | [data/selection.ts](../data/selection.ts) |
| The inject seams: `pasteDraftToSession` for no-submit direct leaf paste and `deliverToSession` for fallback send+submit. | L403-L431 | [data/sessions.ts](../data/sessions.ts) |
| `bracketedPaste` + `fetchHarnesses` (package wrap + harness create options). | — | [data/terminal.ts](../data/terminal.ts) |
| Cockpit supplies `viewedLeafKey` and whether the right rail is actively showing chat. | L491-L499 | [cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |
| The behavior tests cover direct leaf paste and fallback routing. | L132-L163 | [HighlightComposer.test.tsx](HighlightComposer.test.tsx) |

## Update History

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
