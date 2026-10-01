# dashboard/src/panels/session-cockpit/ChatContextBar.tsx

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Carries product duties formerly stranded in the retired Chats route into the canonical cockpit:
launch Chat/Terminal, show task/leaf context, route an existing row locally to a lifecycle, and
authoritatively attach or move a running row to a leaf.

## Code Commentary

### FEUI MX-FIX-2 Raw Open Ownership

The duty bar now owns raw-terminal creation so it can branch at the authority result. It renders
`chats-session-open-error` for a typed failure and calls `onSessionOpened` only with the accepted
server id. This keeps visible failure and focus beside the triggering control; request ids never
become focus ids by assumption.

### FEUI-L9R Reviewed Candidate Delta

The compact `＋ Chat` control now exposes the accessible name
`New chat — choose Claude, Codex, or Pi`. The visual label remains terse, while assistive and
role-based browser selection identifies that the control opens the one harness chooser. It does not
create direct per-harness buttons or introduce another launch path.

New launches inherit the selected lifecycle through the server route. Existing lifecycle attachment
remains explicitly local because no server endpoint exists. Leaf attach/move calls the daemon first,
patches the registry only on success, broadcasts a `leaf` invalidation, and renders same-role conflict
without changing the row.

### Logic

The bar combines the sole chooser entrance with current task, lifecycle, leaf, and attachment
context. Raw creation crosses `createSession`, renders failure locally, and emits only the accepted
server id; harness creation remains in the canonical LaunchFlow.

### Conventions

Compact visible labels may use an explicit accessible name when the action's full meaning would not
fit the bar; stable data attributes remain the browser-test seam.

### 260718-CHATS-L5P Delta (V8 persistence) And Current Action Ownership

- **V8 — Browse history persists** — cit:([`ChatSessionActions`, "Browse history needs a running harness chat focused"], dashboard/src/panels/session-cockpit/ChatContextBar.tsx:132-206): the `Browse history` button is now ALWAYS rendered when
  `onBrowseHistory` exists, and is `disabled`-with-reason (`Browse history needs a running harness chat
  focused`) when the focused row is not a running harness chat — it no longer unmounts/teleports on a
  focus change (the toolbar never reflows, muscle memory holds). This supersedes the "offered ONLY for a
  controlled harness session" reading below. The `action` recipe gained a muted `_disabled` state +
  `whiteSpace:nowrap`.
- **Current ownership** — cit:([`ChatContextBar`; `ChatSessionActions`], dashboard/src/panels/session-cockpit/ChatContextBar.tsx:74-117; dashboard/src/panels/session-cockpit/ChatContextBar.tsx:132-206): this file owns the Chat/Terminal creation bar and selected-session actions, including
  history plus server-first leaf attach/move. Task-id abbreviation and badge rendering are outside this
  component's current ownership.

### Invariants And Boundaries

This remains one launch entrance. It does not create harness-specific launch buttons or bypass the
canonical LaunchFlow. Local lifecycle routing is not durable server authority; leaf ownership is
server-authoritative, with no optimistic mutation or hidden 409 refusal. Failed raw opens neither
create nor focus a session. Library-level affordances (Browse history) stay present and disable with a
reason rather than teleporting on focus (V8). Task-id abbreviation and badge rendering are outside
this component's current ownership.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Evidence

### Repo-Internal References

- Canonical host composition delegates launch through the session view. [1]
- The server-first task-seat operation exposes its result type and catalog-authoritative assignment action. [2]
- Session changes are broadcast through the catalog notification helper. [3]

## 260718-CHATS-L4 Reviewed Candidate Delta (Browse history)

Additive (+14): an optional `onBrowseHistory` callback and a `Browse history` action. It opens the
in-stage previous-conversation library (the `SessionsView` `chats.browseHistory` stage mode /
`ConversationLibrarySurface`); it does not create a session, mint a focus id, or add a second launch
path. The sole-launch-entrance and accepted-row-only invariants are unchanged. *(L5P update: this action
is now ALWAYS present and disabled-with-reason on an ineligible focus, per the V8 delta above — no longer
conditionally unmounted.)*

## Current L5I Maintenance

The rail context bar now owns creation only. Focused-session actions—history browsing and server-first
leaf attach/move—are extracted to `ChatSessionActions` on the stage title row, where their object is
visible. Ineligible actions retain their disabled placement/reason rather than moving unpredictably.
