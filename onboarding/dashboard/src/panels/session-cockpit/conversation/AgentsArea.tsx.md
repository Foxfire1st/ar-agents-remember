# dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T21:59+02:00 |
| lastVerifiedCommitHash | `a401e3dba0bc6e9723451edbfdefb8d77c42945d` |
| lastVerifiedCommitDate | 2026-07-27T00:27:33+02:00|
| governingOverview | `overview.md` |

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
  view, the ellipsized `viewing <label>` note (L78-L82). The separate `← back to parent
  conversation` button (L84-L98, L331-L340) renders beside the line while focused — the old
  surface-owned focus bar is gone; the line owns the whole affordance row.
- **Menu state** (L190-L218): `open` + `activeId`; `resolvedActiveId` recomputes the active option
  against the LIVE roster — a stale id (an agent the roster dropped while the menu was open)
  resolves to the first option, the honest recompute. `openMenu` starts the active option on the
  currently-viewed agent (else the first); `selectAgent` focuses the chosen agent — re-selecting
  the already-viewed agent is a close, not a redundant focus write/announcement.
- **Effects** (L222-L236): DOM focus lands on the listbox on open (its ring +
  `aria-activedescendant` carry the active option — no per-option focus movement); every active
  change scrolls the active option into view (`scrollIntoView({block:"nearest"})` —
  aria-activedescendant moves no DOM focus, so the browser never does this); a roster that empties
  while the menu is open closes honestly.
- **Line keys** (`onLineKeyDown` L238-L265): Enter/Space/ArrowDown toggle the menu
  (preventDefault suppresses the native button-activation click); ArrowUp from the closed line
  returns focus to the timeline's tabbable row — symmetric with the surface's ArrowDown hijack
  that moves focus INTO the line (the surface owns that half; this component exposes the line via
  `data-agents-line`, L316); Escape on the closed line in an agent view returns to the parent
  conversation (the menu owns Esc while open).
- **Menu keys** (`onMenuKeyDown` L267-L296): ArrowUp/ArrowDown move the active descendant with
  wrap-around, Enter selects the active option, Escape closes returning focus to the line, Tab
  dismisses without the focus return (the browser's own order moves on).
- **The listbox overlay** (L343-L395): a fixed backdrop (outside click closes with focus return)
  plus the `role="listbox"` panel (`menu` L100-L122 — maxHeight scroll, `tabIndex={-1}`,
  `aria-activedescendant={optionId(resolvedActiveId)}`), one `role="option"` row per agent
  (`option` L123-L139, `aria-selected` on the active) carrying the ellipsized label, the
  word-carrying status chip, and the terminal `finalMessage` preview with full text in `title`.
- The area itself is a labeled `role="group"` (`sub-agents`, L299).

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
| The line + listbox menu: state, effects, both keymaps, the overlay JSX. | L180-L395 | [AgentsArea.tsx](AgentsArea.tsx) |
| The `ConversationAgentView` rows are shaped by (`deriveAgents`). | L18 | [../../../data/conversation/agents.ts](../../../data/conversation/agents.ts) |
| The `ConversationAgentStatus` union the tones enumerate. | L19 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The surface that derives the roster, owns the effective focus and the ArrowDown-into-the-line hijack, and mounts this strip. | — | [ConversationSurface.tsx](ConversationSurface.tsx) |
| The component suite pinning the line/menu states and the keyboard contract. | — | [AgentsArea.test.tsx](AgentsArea.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: rewrote the card for the one-compact-line
  rework — the per-agent rows and the ResizeObserver narrow collapse are gone; the line carries
  the tone-colored count chip plus the viewing note/back-to-parent affordance (the surface's focus
  bar is deleted), and the roster lives in a new listbox menu (click/Enter/Space/ArrowDown open,
  aria-activedescendant arrow navigation with wrap + scroll-into-view on every active change,
  Enter/click select with the already-viewed re-select collapsing to a close, Esc/backdrop/Tab
  dismiss, ArrowUp from the closed line returning focus to the timeline, stale active id and
  emptying roster recomputing honestly). Verification stays pinned (uncommitted); closeout
  re-stamps.
- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: created the sidecar for the R7 sub-agents strip —
  one roster-evidenced row per agent (label, word-carrying status chip, terminal final-message
  preview), the `N agents · M running` summary with honest `aria-expanded` collapse (static `0 agents`
  span on an empty roster), the ResizeObserver narrow default under 560px with the operator `override`
  winning, and the aria-current focus-toggle rows. Verification is pinned to the leaf base
  (`842b487`) because the new source file is uncommitted; closeout owns its first source stamp.
