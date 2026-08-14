# dashboard/src/panels/RailChat.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/RailChat.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T23:40+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels overview](overview.md)

## Purpose

Hosts Chats over the task-document hierarchy. It selects the current occupant of a structural
document-and-role seat, supports task assignment, and keeps free-chat/terminal behavior outside the
task hierarchy.

## Code Commentary

### Logic

The session hook joins a selected `TaskDocumentRef` to live catalog sessions and role. Task-bound
launches pass that reference into the opener; assignment resolves the selected leaf document and
posts the reference plus role. Leaf keys remain only for legacy context-package content and display.
The rendered panel uses the current occupant id for transport after structural selection.

### Conventions

Task-document selection comes from the projected real document. Free chat is represented by an
unbound chat session, not by a manufactured task address.

### Invariants And Boundaries

- Task-bound chat selection never searches globally by role.
- Replacement keeps the same task-document-and-role selection.
- Free chat and shell terminal affordances are not inserted into the structural task tree.
- Runtime ids remain behind the selected occupant/transport seam.

### Todos

Leaf-key context packaging remains a non-addressing presentation path and should stay clearly
separated from structural seat lookup.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selected structural identity resolves the current live chat occupant. | `useRailChatSessions` | dashboard/src/panels/RailChat.tsx:355-432 |
| Task assignment derives and sends a real task-document reference. | "function useRailChatAttach(" | dashboard/src/panels/RailChat.tsx:506-540 |
| The panel accepts structural task identity separately from leaf display context. | `RailChatImpl` | dashboard/src/panels/RailChat.tsx:545-644 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T23:40+02:00 — No content impact: the lint-only extraction of props, harness
  detection, sprint-role start, and termination helpers preserves structural document-and-role
  selection, current-occupant transport, assignment, and free-chat boundaries. Verification
  metadata remains pinned until governed closeout.

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `RailChat.tsx` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B19 curator: replaced the `n/a` table rows with
  exact anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-24T13:17:17Z — Curator: documented the rail-chat memo boundary; verification fields
  remain pre-commit.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: gated contextual raw/harness creation and leaf-context
  delivery on an accepted server row and added a visible typed failure alert. Verification metadata
  remains pinned until closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: migrated rail composition and leaf-context delivery to the
  shared reliable client with source-aware draft boundaries.

- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (review finding F6, one-prop call-site change): both
  `<Terminal>` mounts (the chat slot and the split terminal `Pane`) now pass
  ``ariaLabel={`terminal: ${session.label}`}`` so the terminal's `role="group"` landmark carries
  a real name in the rail surface (Terminal.tsx also guarantees a sessionId fallback). No other
  rail behavior changed. Verification metadata pinned to the leaf base until closeout stamps the
  L6 code commit.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: made rail attach/move role-explicit, preserved
  pair-scoped local state, and displayed current seat identity in pane headers.

- 2026-07-02T17:04+02:00 — L9: kept the picker visible for attached chats as a move control. Successful
  moves use `applyLeafAssignment`, broadcast `"leaf"`, preserve the live terminal session, and draft the
  destination leaf's context; `leaf-taken` still avoids local mutation and context injection. Verification
  metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T13:07+02:00 — Reopened L6 follow-up: changed leaf-context handoff from submit delivery to
  draft paste. `deliverLeafContext` now calls `pasteDraftToSession`, so the packet lands in the selected
  chat input without pressing Enter and the operator can add their own instruction before submitting.
  Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-01T01:19+02:00 — L6: added bind-time leaf context handoff. `RailChat` now accepts
  `engineProcesses` beside `taskDocuments`, builds a projected leaf context packet from the selected/picked
  `leafKey`, and injects it through `deliverToSession` after start-on-leaf or a successful free-chat
  attach. Rejected attaches and free/off-leaf chat creation do not send a packet; unconfirmed delivery
  surfaces `rail-leaf-context-note`. Verification metadata pinned until closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: reshaped the rail chat from a single per-leaf session into a **chat + terminal
  split**. The start affordance is now a **harness choice** (a `＋ {harness}` button per detected harness via
  `fetchHarnesses`, opening an agent chat with `createSession(…, "harness", …)`) plus a separate **＋ Terminal**
  (a `kind:"terminal"` shell); the leaf's slots resolve role-scoped via `findSessionForLeaf(leafKey, role)` /
  `sessionRole` and render as a vertical split (chat top, terminal below). Each `Pane` gained a **terminate**
  control (via `terminateTerminalSession`, broadcasting a catalog change) and a **truncating, `title`-bearing
  header** (hover reveal); hidden keep-alive layers survive leaf switches. Verification metadata pinned until
  closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): created the single-instance right-rail leaf chat — resolves a leaf's
  bound running session by `leafKey`, reuses the shared `Terminal` + `SessionComposer` + connection
  registry so it surfaces the same session as the Chats page, keeps previously-surfaced sessions
  mounted-but-hidden across leaf switches, and offers "＋ Start chat for this leaf" (opening a session
  carrying the `leafKey`) when none is bound. Verification metadata pinned until closeout stamps the L5
  commit.
