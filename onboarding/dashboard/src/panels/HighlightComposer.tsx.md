# dashboard/src/panels/HighlightComposer.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/HighlightComposer.tsx`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-23T13:45+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The slice-6f **"send a context package by highlighting"** composer — **two stages**, like a code
editor's selection toolbar: (1) selecting cockpit content (on mouse-up) raises a small **"Add to
chat"** pill anchored to it; (2) clicking the pill opens the composer box, which **stays open** until
the operator clicks outside it or Sends. The composer lives on a *snapshot* of the selection
(`useSelectionCapture`), so clicking into the message box never dismisses it. The target control offers
the open chats **and** a create option per detected harness, so a new chat is an agent (not a shell
into the void). A selection only ever *raises* the pill; nothing reaches an agent until Send (the
**no-silent-action** invariant). Mounted once in `CockpitShell`. 6f-1 covers text; entity-aware repo
inference (6f-2) and image paste (6f-3) follow. Task 11 adds lifecycle-aware target filtering: when
`selectedLifecycleId` is present, open-chat targets are limited to sessions already tagged with that
lifecycle, and create targets tag the new hosted chat.

## Code Commentary

### Logic

Driven by `useSelectionCapture()` (`data/selection`) — renders `null` with no snapshot. A
fixed-position 0-area `<span>` at the snapshot rect is the React Aria `Popover` `triggerRef`; the
`Popover` is controlled (`isOpen` while a snapshot exists) and `onOpenChange(false)` (outside-click /
Escape) → `dismiss()` = `clear()` + back to the pill. A `mode` (`"pill" | "composer"`), reset to
`"pill"` whenever the snapshot changes, drives the stages: **pill** is a single **Add to chat** button;
**composer** renders the captured selection (`<pre>`), the **target control**, an autofocused message
`TextField`/`TextArea` (**Enter = send + submit**, **Shift+Enter = newline**), and **Send**.

**Target** — one React Aria `ToggleButtonGroup` lists open chats **and** a create option per
**detected** harness (`fetchHarnesses` on mount: ＋ Claude Code / ＋ Codex / …) plus a plain `＋
Terminal` shell. The default is the active chat, else the first open chat, else the first create option
— a detected harness (an agent), **never silently a shell**, so the package doesn't go into the void.
When `selectedLifecycleId` is set, "open chats" means sessions whose `lifecycleId` matches; create
targets pass that lifecycle to `createSession`.
**`send()`** resolves the selected target: an open chat → `setActive` + deliver; a create option →
`createSession(prefix, "harness"|"terminal", harnessId?, selectedLifecycleId?)` then deliver. The always-sendable minimum
holds because there is always a default. Send builds the package, resolves the target, then immediately calls `finish()` (`dismiss()` +
`onSent?.()` — the composer closes + switches to Chats) and delivers in the **background** so the
operator isn't blocked: **`deliverPackage(id, pkg)`** `await`s `sendWhenReady(id, bracketedPaste(pkg))` —
which waits for the session's terminal to register **and** its harness to look ready (so a fresh agent
doesn't drop the package mid-boot) — then `sendToSession(id, "\r")` (the Enter that submits). The
package is the message, then a `--- from the dashboard ---` rule + the selection.

### Conventions

React Aria primitives (`Popover`/`Dialog`/`Button`/`TextField`/`TextArea`/`ToggleButton(Group)`) +
co-located Panda `css` (the amber/grid cockpit look) — the cockpit's first overlay. The pill is a quiet
content-sized grid-bordered bar (`dialogPill`); the composer is a **fixed-width** box (`dialogComposer`,
so it never tracks the selection's width) with the amber active border. The message `TextArea` has a
5rem min-height + a vertical resize handle. `data-highlight-composer` marks the dialog so
`data/selection` ignores selections + mouse-ups inside it.

### Invariants And Boundaries

No silent action: a selection raises only the **pill**; the composer opens on an explicit click, and
only an explicit Send injects. The composer persists until outside-click/Escape or Send
(snapshot-driven, not live-selection-driven). Delivery reuses the live B2 `{type:stdin}` channel via
`data/sessions.sendToSession` (a brand-new session's connection buffers until its WebSocket opens) — no
new transport, not ACP. Presentational state only (mode / draft / target); session lifecycle stays in
`data/sessions`. With a selected lifecycle, unrelated open chats are not offered; the create target
becomes the routeable chat.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The mouse-up selection snapshot it attaches to. | — | [data/selection.ts](../data/selection.ts) |
| The inject seam + `createSession` it drives. | — | [data/sessions.ts](../data/sessions.ts) |
| `bracketedPaste` + `fetchHarnesses` (package wrap + harness create options). | — | [data/terminal.ts](../data/terminal.ts) |
| Where it is mounted (cockpit-wide). | — | [cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |
| The behavior tests. | — | [HighlightComposer.test.tsx](HighlightComposer.test.tsx) |

## Update History

- 2026-06-23T13:45+02:00 — Task 11: `HighlightComposer` accepts `selectedLifecycleId`; open-chat
  targets are filtered to sessions tagged with that lifecycle, and create targets pass the lifecycle
  to `createSession` so new hosted chats become routeable for Gate Respond. Verification metadata pinned
  until closeout stamps the task-11 code commit.
- 2026-06-19T15:59 — Created for task 6 slice 6f-1: the two-stage highlight→context-package composer — an "Add to chat" pill on a mouse-up selection → a fixed-width composer box (snapshot-driven so clicking into it doesn't dismiss it; 5rem-min resizable message box; Enter=send+submit / Shift+Enter=newline). The target control lists open chats + a create option per **detected harness** (＋ Claude Code / ＋ Codex / ＋ Terminal), defaulting to an agent not a shell; delivery dismisses the composer immediately and runs in the **background**, gated on the harness being ready (`sendWhenReady` → `whenReady`) so a fresh agent doesn't drop the package mid-boot (two stdin frames: bracketed paste + Enter). Verification metadata pinned until closeout stamps the 6f-1 code commit.
