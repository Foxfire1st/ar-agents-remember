# dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T21:59+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test. | `AgentsArea` | dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:180-396 |
| The `ConversationAgentView` shape the fixtures build. | `ConversationAgentView` | dashboard/src/data/conversation/agents.ts:58-64 |
| The surface-level focus behavior this line plugs into, incl. the ArrowDown hijack (separate suite). | "ArrowDown from the timeline moves focus into the agents line; Enter opens the menu; Enter selects" | dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:186-211 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-03T09:50+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 15 assigned citation findings (2 missing anchors, 2 malformed sources, and 11 prose citations); final scoped check is clean.

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
