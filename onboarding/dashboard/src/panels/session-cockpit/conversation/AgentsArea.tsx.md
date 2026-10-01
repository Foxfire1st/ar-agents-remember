# dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The sub-agents area (R7, reworked): ONE compact line above the timeline — always, never one row
per agent (the Claude Code sub-agent navigation model). The line carries the tone-colored count
chip (`N agents · M running`), plus `viewing <label>` and a back-to-parent affordance while an
agent view is active. Activating the line opens the agent menu: a small listbox overlay with one
option per roster agent (label, word-carrying status chip, terminal final-message preview). It
renders ONLY from projection roster evidence (`deriveAgents`): no optimistic rows, no polling.

## Code Commentary

### Logic

- **The compact line** (L299-L344, `summaryText` L173-L178): an empty roster renders a STATIC
  `lineStatic` span (`0 agents` — nothing to open, so no dead toggle, L59-L62); otherwise a real
  `<button aria-haspopup="listbox" aria-expanded aria-controls>` carrying the count chip
  (`countChip` + `countTone` active/idle by whether anything is running, L64-L77) and, in an agent
  view, the ellipsized `viewing <label>` note cit:(["conversation-agent-focus-note"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:286-286). The separate `← back to parent
  conversation` button (L84-L98, L331-L340) renders beside the line while focused — the old
  surface-owned focus bar is gone; the line owns the whole affordance row.
- **Live-roster state** cit:(["{open && resolvedActiveId !== null ? ("], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:190-202; dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:233-233): a stale active id resolves to the first live agent.
- **Open action** cit:(["const openMenu = () => {"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:199-199; dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:402-402) => {"]"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:199-199): opening starts from the focused/first agent.
- **Selection and focus return** cit:(["const closeMenu = (returnFocus: boolean) => {", "const selectAgent = (agentId: string) => {"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:407-407; dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:411-411): selection focuses a changed agent and closes with focus return.
- **Active-option visibility** cit:(["useEffect(() => { if (!open || resolvedActiveId === null) return;", "[id='", "scrollIntoView({ block: \"nearest\" })", "[open"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:424-429): the guarded effect scrolls the option resolved from the active id into view whenever either dependency changes.
- **Line keys** cit:(["onKeyDown={onLineKeyDown}"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:197-197; dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:219-219): Enter/Space/ArrowDown toggle the menu
  (preventDefault suppresses the native button-activation click); ArrowUp from the closed line
  returns focus to the timeline's tabbable row — symmetric with the surface's ArrowDown hijack
  that moves focus INTO the line (the surface owns that half; this component exposes the line via
  `data-agents-line`, L316); Escape on the closed line in an agent view returns to the parent
  conversation (the menu owns Esc while open).
- **Menu keys** cit:(["onKeyDown={onMenuKeyDown}"], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:198-198; dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:240-240): ArrowUp/ArrowDown move the active descendant with
  wrap-around, Enter selects the active option, Escape closes returning focus to the line, Tab
  dismisses without the focus return (the browser's own order moves on).
- **The listbox overlay** cit:([`AgentsArea`], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:180-396): a fixed backdrop (outside click closes with focus return)
  plus the `role="listbox"` panel (`menu` L100-L122 — maxHeight scroll, `tabIndex={-1}`,
  `aria-activedescendant={optionId(resolvedActiveId)}`), one `role="option"` row per agent
  (`option` L123-L139, `aria-selected` on the active) carrying the ellipsized label, the
  word-carrying status chip, and the terminal `finalMessage` preview with full text in `title`.
- The area itself is a labeled `role="group"` (`aria-label="sub-agents"`) cit:(["aria-label=\"sub-agents\""], dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:205-205).

### Conventions

- **Status is never color-only (§14.2):** every chip carries its status WORD (`registered` /
  `running` / `completed` / `interrupted` / `failed` / `unknown`); the tone is reinforcement only.
- **No transitions:** a keyboard-driven open/focus change must not animate (header contract).
- Chrome follows the FB7 terminal-well grammar: de-boxed lowercase buttons, `grid` borders, amber
  hover/focus accents.
- The menu is a genuine ARIA listbox: DOM focus on the listbox, `aria-activedescendant` +
  `aria-selected` for the active option, never roving per-option focus.

### Invariants And Boundaries

- Projection-only: options come from `deriveAgents` roster evidence passed in by the surface; this
  component never fetches, polls, or invents an optimistic row.
- The area is ONE line at every roster size and every width — per-agent rows never render outside
  the menu (the old narrow-collapse ResizeObserver is deleted).
- The preview renders only where terminal evidence carried a `finalMessage`; it is ellipsized with
  the full text in the hover `title`.
- The menu owns its keys while open (arrow navigation stops propagation); the closed line yields
  ArrowUp to the timeline-return path and Escape to the agent-view return, never trapping the
  operator.
- A stale active id recomputes to the first option; an emptying roster closes the menu — the
  listbox never points at an agent the roster no longer carries.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The line + listbox menu: state, effects, both keymaps, the overlay JSX. [1]
- The `ConversationAgentView` rows are shaped by (`deriveAgents`). [2]
- The `ConversationAgentStatus` union the tones enumerate. [3]
- The surface that derives the roster, owns the effective focus and the ArrowDown-into-the-line hijack, and mounts this strip. [4]
- The component suite pinning the line/menu states and the keyboard contract. [5]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
