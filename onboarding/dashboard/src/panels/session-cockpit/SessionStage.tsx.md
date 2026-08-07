# dashboard/src/panels/session-cockpit/SessionStage.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionStage.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **SessionStage container** is the fixed header/surface/composer boundary. It renders the
`HeaderStrip` (or the explained no-focus identity) in `data-stage-header`, forwards the view-owned
`headerExtra` and `controlPopover` bridge, and renders `children`. `SessionsView` owns the
content below `ChatsStageBody`: it chooses `ConversationWorkingLine` for live harness conversations
or `WorkingLine` otherwise, followed by `InteractionBar` and `SessionComposer`. The handoff
message is an assistive `role="status"` note via `handoffNote`, not visible amber chrome.

## Code Commentary

### Logic

- **Header row**: `data-stage-header` with `tabIndex={-1}` is the F6/composer-Esc focus landing
  from L1; it hosts `HeaderStrip` for the focused seat or the explained no-focus identity.
  `headerExtra` renders view-owned chips after the strip, and `controlPopover` is forwarded
  unchanged to `HeaderStrip` so palette commands open the same mounted control.
- **Handoff note (F17)**: the one-line `role="status"` note is supplied through `handoffNote` and
  remains available to assistive technology rather than standing visual chrome.
- **View-owned working content**: `SessionsView` chooses `ConversationWorkingLine` or `WorkingLine`
  below `ChatsStageBody`; `SessionStage` does not own a `workingLine` prop.
- **Children**: the PTY surface/composer passed from `SessionsView`.

### Invariants And Boundaries

- The layer order is RULED (§1.2): header → working-line slot → surface → composer; L6/L5 fill
  slots, never reorder.
- The container never invents identity: no focused seat ⇒ the explained hint, not a blank.
- `data-stage-header` must stay on the header element — the keymap focus contract targets it.
- `controlPopover` is state plumbing only; this container never mounts a second control or owns
  snapshot/set behavior.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixed header, empty identity, handoff status, and popover bridge. | `SessionStage`; "data-stage-header"; `handoffNote` | dashboard/src/panels/session-cockpit/SessionStage.tsx:33-43; dashboard/src/panels/session-cockpit/SessionStage.tsx:46-102 |
| The header line rendered for the focused seat. | `HeaderStrip` | dashboard/src/panels/session-cockpit/HeaderStrip.tsx:88-169 |
| `SessionStage` owns the fixed header and the child stage-body slot below it. | `SessionStage` | dashboard/src/panels/session-cockpit/SessionStage.tsx:46-102 |
| `SessionsView` supplies `ChatsStageBody` to that child slot. | "cockpit={data.focused ? data.perSession[data.focused.id] : undefined}"; "onToggleDiagnostics={handlers.toggleChatsDiagnostics}" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:291-291; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:260-260 |
| `SessionsView` chooses `ConversationWorkingLine` when the focused live conversation is a harness. | "focused.kind === \"harness\" && focusedConversationLive"; "<ConversationWorkingLine" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:194-194; skills/w-02-light-task-workflow/master-template.md:93-93; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:195-195 |
| `SessionsView` chooses `WorkingLine` in the other branch of that focused-conversation condition. | "focused.kind === \"harness\" && focusedConversationLive"; "data-testid=\"sessions-stage\"" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:194-194; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:286-286 |
| `SessionsView` places `InteractionBar` after the selected harness/non-harness working-line slot. | "data-slot=\"working-line\""; "focused.kind === \"harness\" && focusedConversationLive" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:190-190; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:194-194; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:195-215 |
| The focus selectors that target `data-stage-header`. | "[data-stage-header]" | dashboard/src/data/keymap/focus.ts:32-32 |
| `SessionStage` exposes the assistive handoff status when a handoff note exists. | "handoff ?"; "role=\"status\"" | dashboard/src/panels/session-cockpit/SessionStage.tsx:94-95 |
| The `HeaderStrip` suite asserts no `WorkingLine` slot in `SessionStage` chrome, covers handoff, and covers explained empty identity. | "reserves NO WorkingLine slot"; "shows the focus-handoff note" | dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx:119-130; dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx:132-147 |

## Current L5I Maintenance

Stage actions now live beside the title in the `headerActions` slot. The old StatusLine action bar
is retired, and the working-line slot moves beneath the conversation surface and above the composer.
The focus-handoff message remains available to assistive technology but is no longer standing visual
chrome after a chat ends.

## Update History

- 2026-08-04T16:40:00+02:00 — 260731-EFA-L6 S18-B12 curator correction (reviewer-BLOCK repair): separated `SessionStage` chrome/body-slot ownership from `SessionsView` child placement; the `ChatsStageBody` nesting now cites the continuous 1112-1195 owner span and the working-line/InteractionBar ordering the continuous 1209-1232 branch span; the scoped fixer confirmed the final ranges with no writes.
- 2026-07-24T13:17:17Z — Curator: documented title-row action placement, working-line relocation,
  and screen-reader-only handoff copy; verification fields remain pre-commit.

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R2 added the optional controlled-popover bridge and
  forwarded it to HeaderStrip; stage order and ownership remain unchanged. Verification metadata
  is pinned to the contract base until code commit.
- 2026-07-17T06:10+02:00 — 260715-FEUI-L3: one string literal — the empty-stage identity now
  points at the palette's "Launch session…" command (the old "launch from Chats (cockpit
  launcher: L5)" copy became false the moment L3 shipped the launcher). Structure untouched.
  Verification metadata pinned to the leaf base until closeout stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6: the reserved WorkingLine slot is FILLED — the ONE
  additive optional `workingLine` prop (the slot's only tenant) renders L6's turn theater inside
  `data-slot="working-line"`; layer order, empty identity, and handoff note unchanged.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S5 (R9/R10/F17): the stage container with
  the ruled layer order, the always-on header hosting HeaderStrip or the explained no-focus
  identity, the F17 handoff note, and the reserved zero-height WorkingLine slot for L6.
  Verification metadata pinned to the leaf base until closeout stamps the L2 code commit.
