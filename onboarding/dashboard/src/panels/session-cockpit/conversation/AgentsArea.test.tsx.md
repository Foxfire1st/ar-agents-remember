# dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The `AgentsArea` component suite (R7, reworked): it pins the one-compact-line contract — never one
row per agent at any roster size — the tone-colored count chip and the in-line viewing
note/back-to-parent affordance, and the listbox menu's full keyboard/aria contract (open,
arrow navigation with wrap + scroll-into-view, Enter/click select, Esc/backdrop dismiss).

## Code Commentary

### Logic

- **Fixtures** (cit:([`agent`, `renderArea`, `line`], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:12-14; dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:16-25; dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:27-29)): an `agent()` factory defaulting to `status: "running"`, a `renderArea`
  helper with a spy `onFocusAgent`, and a `line()` accessor for the `conversation-agents-line`
  testid.
- **Empty roster** (cit:(["shows a static '0 agents' line for the empty roster — no dead toggle"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:36-43)): the line is `0 agents` rendered as a SPAN — nothing to open, so no
  dead toggle (`aria-haspopup` absent) — and no menu mounts.
- **One line at any size** (cit:(["renders ONLY the compact count line"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:45-55)): a 20-agent roster renders ONLY the compact line
  (`20 agents · 10 running`) — no per-agent options, no menu.
- **Open on Enter** (cit:(["opens the menu on Enter with listbox aria"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:57-94)): the line reports `aria-haspopup="listbox"` + honest
  `aria-expanded`; Enter opens the menu with `role="listbox"`, DOM focus on the listbox, one
  `role="option"` per agent, word-carrying status chips in order, the final-message preview ONLY
  where terminal evidence carried it, and the first option as initial `aria-activedescendant` /
  `aria-selected`.
- **Open on click, click-select** (cit:(["opens the menu on click; clicking an option selects like Enter"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:96-108)): clicking the line opens; clicking an option selects
  like Enter (focus callback, menu closed, focus back on the line).
- **Arrow navigation** (cit:(["navigates the menu with ArrowUp/ArrowDown (wrapping) and selects the active option on Enter"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:110-134)): ArrowUp/ArrowDown move `aria-activedescendant` with
  wrap-around both ways; Enter selects the active option and returns focus to the line.
- **Scroll-into-view** (cit:(["scrolls the active option into view on every active change (20-agent roster)"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:136-162)): on a 20-agent roster every active change calls
  `scrollIntoView` on the active option — open, arrow moves, and the wrap to the last option.
- **Dismissals** (cit:(["Escape closes the menu without selecting and returns focus to the line"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:164-183)): Escape closes without selecting and returns focus to the line; a
  backdrop click does the same.
- **Agent-view line** (cit:(["shows the viewing note + back-to-parent affordance on the line while an agent view is active"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:185-191)): while focused, the line carries `viewing scout` and the
  back-to-parent button fires the focus callback with `null`.
- **Viewed-agent start + re-select** (cit:(["starts the menu's active option on the currently viewed agent; re-selecting it just closes"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:193-205)): the menu's initial active option is the
  currently-viewed agent; re-selecting it does NOT re-fire the focus callback — it just closes.
- **Closed-line Escape** (cit:(["Escape on the closed line returns an active agent view to the parent"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx:207-211)): Escape on the closed line in an agent view returns to the
  parent conversation.

### Invariants And Boundaries

- The suite renders the real component with derived-shape fixtures; it never asserts styling — the
  pinned contract is structure, words, and callback semantics.
- The terminal-preview assertion guards the evidence-only rule: a non-terminal option carries no
  preview element at all.
- The one-line contract is pinned at 20 agents: the roster size must never grow the chrome outside
  the menu.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The component under test. [1]
- The `ConversationAgentView` shape the fixtures build. [2]
- The surface-level focus behavior this line plugs into, incl. the ArrowDown hijack (separate suite). [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
