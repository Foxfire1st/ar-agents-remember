# dashboard/src/panels/session-cockpit/ChatContextBar.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatContextBar.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical host composition delegates launch through the session view. | `onLaunchChat` | dashboard/src/panels/session-cockpit/ChatContextBar.tsx:71-71 |
| The server-first task-seat operation exposes its result type and catalog-authoritative assignment action. | `applyTaskAssignment`; `AttachTaskResult` | dashboard/src/data/sessions.ts:169-176; dashboard/src/data/terminal.ts:483-495 |
| Session changes are broadcast through the catalog notification helper. | `notifySessionCatalogChanged` | dashboard/src/data/sessions.ts:113-126 |

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

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `ChatContextBar.tsx` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T11:32:09+02:00 — 260731-EFA-L6 S18-B02 curator: narrowed claims to positive local ownership and generated final citation ranges with the scoped fixer.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: removed obsolete `shortId` ownership from the
  live contract. The file currently owns creation and selected-session actions, not task-id badge
  rendering. The new self-citation was normalized by the scoped fixer.

- 2026-08-03T05:04+02:00 — 260731-EFA-L6 W3-B10 curator: repaired 2 table citations and 1 prose citation, normalized the scoped source paths, audited the interface extents, and reanchored the sole-launch composition row to the `onLaunchChat` binding in `SessionsView`; the localized subject-binding repair generated `SessionsView.tsx:1069-1069`, while the stale `shortId()` ownership claim remains the sole Tier-3 finding in this card.

- 2026-07-24T13:17:17Z — Curator: corrected launch-versus-focused-session action ownership and
  title-row placement; verification fields remain pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded V8 (Browse history always present,
  disabled-with-reason on ineligible focus — no teleport) and R6 (task/lifecycle badges rendered via
  `shortId` with the full value in the `title`). Corrected the L4 delta's "offered ONLY for a controlled
  harness session" phrasing. Sole-launch-entrance invariant unchanged. Verification pinned to the leaf
  base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 (structured Chats renderer, reviewer FINAL PASS): recorded
  the additive optional `onBrowseHistory` callback + controlled-session `Browse history` action that
  opens the in-stage history library; no new launch path or focus authority. Verification metadata
  remains pinned to the leaf base until closeout.
- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: moved raw creation into the duty bar, surfaced typed
  failures locally, and emitted a focus callback only for the accepted server id. Verification
  metadata remains pinned until closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the chooser entrance's explicit accessible name and
  sole-launch-path boundary; verification metadata remains pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — Created for the FEUI-L8 legacy-Chats duty transfer; verification metadata
  remains blank until commit.
