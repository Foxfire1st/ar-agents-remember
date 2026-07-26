# dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T21:59+02:00 |
| lastVerifiedCommitHash | `a401e3dba0bc6e9723451edbfdefb8d77c42945d` |
| lastVerifiedCommitDate | 2026-07-27T00:27:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The `AgentsArea` component suite (R7, reworked): it pins the one-compact-line contract — never one
row per agent at any roster size — the tone-colored count chip and the in-line viewing
note/back-to-parent affordance, and the listbox menu's full keyboard/aria contract (open,
arrow navigation with wrap + scroll-into-view, Enter/click select, Esc/backdrop dismiss).

## Code Commentary

### Logic

- **Fixtures** (L12-L33): an `agent()` factory defaulting to `status: "running"`, a `renderArea`
  helper with a spy `onFocusAgent`, and a `line()` accessor for the `conversation-agents-line`
  testid.
- **Empty roster** (L36-L43): the line is `0 agents` rendered as a SPAN — nothing to open, so no
  dead toggle (`aria-haspopup` absent) — and no menu mounts.
- **One line at any size** (L45-L55): a 20-agent roster renders ONLY the compact line
  (`20 agents · 10 running`) — no per-agent options, no menu.
- **Open on Enter** (L57-L94): the line reports `aria-haspopup="listbox"` + honest
  `aria-expanded`; Enter opens the menu with `role="listbox"`, DOM focus on the listbox, one
  `role="option"` per agent, word-carrying status chips in order, the final-message preview ONLY
  where terminal evidence carried it, and the first option as initial `aria-activedescendant` /
  `aria-selected`.
- **Open on click, click-select** (L96-L108): clicking the line opens; clicking an option selects
  like Enter (focus callback, menu closed, focus back on the line).
- **Arrow navigation** (L110-L134): ArrowUp/ArrowDown move `aria-activedescendant` with
  wrap-around both ways; Enter selects the active option and returns focus to the line.
- **Scroll-into-view** (L136-L162): on a 20-agent roster every active change calls
  `scrollIntoView` on the active option — open, arrow moves, and the wrap to the last option.
- **Dismissals** (L164-L183): Escape closes without selecting and returns focus to the line; a
  backdrop click does the same.
- **Agent-view line** (L185-L191): while focused, the line carries `viewing scout` and the
  back-to-parent button fires the focus callback with `null`.
- **Viewed-agent start + re-select** (L193-L205): the menu's initial active option is the
  currently-viewed agent; re-selecting it does NOT re-fire the focus callback — it just closes.
- **Closed-line Escape** (L207-L211): Escape on the closed line in an agent view returns to the
  parent conversation.

### Invariants And Boundaries

- The suite renders the real component with derived-shape fixtures; it never asserts styling — the
  pinned contract is structure, words, and callback semantics.
- The terminal-preview assertion guards the evidence-only rule: a non-terminal option carries no
  preview element at all.
- The one-line contract is pinned at 20 agents: the roster size must never grow the chrome outside
  the menu.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | L10 | [AgentsArea.tsx](AgentsArea.tsx) |
| The `ConversationAgentView` shape the fixtures build. | L9 | [../../../data/conversation/agents.ts](../../../data/conversation/agents.ts) |
| The surface-level focus behavior this line plugs into, incl. the ArrowDown hijack (separate suite). | — | [ConversationAgentFocus.test.tsx](ConversationAgentFocus.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: rewrote the card for the reworked suite — the
  old per-agent-row/expand-collapse pins are replaced by the one-compact-line contract (20-agent
  roster still one line), the listbox open/aria/focus pins, wrapping arrow navigation with the
  scroll-into-view spy, Enter/click/Esc/backdrop select-and-dismiss semantics, the viewed-agent
  initial active option with re-select-as-close, the in-line viewing note + back-to-parent
  affordance, and the closed-line Escape return. Verification stays pinned (uncommitted);
  closeout re-stamps.
- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: created the sidecar for the R7 AgentsArea suite —
  the static `0 agents` summary (no dead toggle), one row per agent with word-carrying chips and the
  terminal-only preview, honest `aria-expanded` collapse, `aria-current` focus marking, and the
  row-activation focus toggle (focus agent / back to parent). Verification is pinned to the leaf base
  (`842b487`) because the new source file is uncommitted; closeout owns its first source stamp.
