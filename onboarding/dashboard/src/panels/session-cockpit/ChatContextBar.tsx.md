# dashboard/src/panels/session-cockpit/ChatContextBar.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatContextBar.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
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

### 260718-CHATS-L5P Delta (V8 persistence + R6 short ids)

- **V8 — Browse history persists** (L158-L178): the `Browse history` button is now ALWAYS rendered when
  `onBrowseHistory` exists, and is `disabled`-with-reason (`Browse history needs a running harness chat
  focused`) when the focused row is not a running harness chat — it no longer unmounts/teleports on a
  focus change (the toolbar never reflows, muscle memory holds). This supersedes the "offered ONLY for a
  controlled harness session" reading below. The `action` recipe gained a muted `_disabled` state +
  `whiteSpace:nowrap`.
- **R6 — short task ids** (L182-L200): a long task/lifecycle id renders through `shortId()`
  (`data/conversation/format`) as a `…SUFFIX` badge with the full `task <id>` value in the `title` — the
  bar never leaks a 26-char raw ULID.

### Invariants And Boundaries

This remains one launch entrance. It does not create harness-specific launch buttons or bypass the
canonical LaunchFlow. Local lifecycle routing is not durable server authority; leaf ownership is
server-authoritative, with no optimistic mutation or hidden 409 refusal. Failed raw opens neither
create nor focus a session. Library-level affordances (Browse history) stay present and disable with a
reason rather than teleporting on focus (V8); raw ids display as short suffixes with the full value in a
tooltip (R6).

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | Source discovery checked | — |

## Cross-Repo References

The bar composes repository-local task/session helpers and same-origin terminal routes; no cross-repository implementation governs it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical host and sole-launch-path composition. | L928-L958 | [SessionsView.tsx](SessionsView.tsx) |
| Session patch/broadcast and server leaf route. | L1-L80 | [../../data/sessions.ts](../../data/sessions.ts) · [../../data/terminal.ts](../../data/terminal.ts) |

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
