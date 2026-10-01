# dashboard/src/panels/session-cockpit/SessionStage.tsx

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

## Evidence

### Repo-Internal References

- The fixed header, empty identity, handoff status, and popover bridge. [1]
- The header line rendered for the focused seat. [2]
- `SessionStage` owns the fixed header and the child stage-body slot below it. [3]
- `SessionsView` supplies `ChatsStageBody` to that child slot. [4]
- `SessionsView` chooses `ConversationWorkingLine` when the focused live conversation is a harness. [5]
- `SessionsView` chooses `WorkingLine` in the other branch of that focused-conversation condition. [6]
- `SessionsView` places `InteractionBar` after the selected harness/non-harness working-line slot. [7]
- The focus selectors that target `data-stage-header`. [8]
- `SessionStage` exposes the assistive handoff status when a handoff note exists. [9]
- The `HeaderStrip` suite asserts no `WorkingLine` slot in `SessionStage` chrome, covers handoff, and covers explained empty identity. [10]

## Current L5I Maintenance

Stage actions now live beside the title in the `headerActions` slot. The old StatusLine action bar
is retired, and the working-line slot moves beneath the conversation surface and above the composer.
The focus-handoff message remains available to assistive technology but is no longer standing visual
chrome after a chat ends.
