# dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The sub-agents area (R7): the small persistent strip above the timeline with one
live row per roster-evidenced agent — label, status chip, and the final-message preview once
terminal. It renders ONLY from projection roster evidence (`deriveAgents`): no optimistic rows, no
polling. With no agents, or while the surface is narrow, it collapses to a single summary line
(`N agents · M running`) that expands on activation.

## Code Commentary

### Logic

- **Summary line** (L105-L110, L144-L159): `summaryText` renders `0 agents` for an empty roster
  (a STATIC `summaryStatic` span — nothing to expand, so no dead toggle) or `N agent(s) · M running`.
  With agents present the summary is a real `<button aria-expanded aria-controls>` whose click sets
  the expand `override`.
- **Narrow collapse** (L15, L112-L125, L137-L140): a `ResizeObserver` flips `narrow` below
  `NARROW_PX` (560px). The `override` state (null = no explicit operator choice) makes the default
  `expanded` iff agents exist AND the width allows; an operator toggle wins over the width heuristic.
- **Agent rows** (L160-L196): one button per agent — the ellipsized label, a status chip
  (`statusChip` + per-status `statusTone`, L78-L95), and the terminal `finalMessage` preview with
  the full text behind `title`. Row activation toggles focus: the focused row re-clicked returns
  `null` (the parent conversation); the focused row carries `aria-current="true"` and an amber
  border (`&[aria-current='true']`, L70).
- The area itself is a labeled `role="group"` (`sub-agents`, L143).

### Conventions

- **Status is never color-only (§14.2):** every chip carries its status WORD (`registered` /
  `running` / `completed` / `interrupted` / `failed` / `unknown`); the tone is reinforcement only.
- **No transitions:** a keyboard-driven expand/focus change must not animate (header contract, L6-L7).
- Chrome follows the FB7 terminal-well grammar: de-boxed lowercase buttons, `grid` borders, amber
  hover/focus accents.

### Invariants And Boundaries

- Projection-only: rows come from `deriveAgents` roster evidence passed in by the surface; this
  component never fetches, polls, or invents an optimistic row.
- The preview renders only where terminal evidence carried a `finalMessage`; it is ellipsized with
  the full text in the hover `title`.
- Focus is an operator toggle, not a navigation trap: activating the already-focused row returns to
  the parent conversation.

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
| The strip: summary/narrow collapse, per-status chips, focus-toggle rows. | L127-L199 | [AgentsArea.tsx](AgentsArea.tsx) |
| The `ConversationAgentView` rows are shaped by (`deriveAgents`). | L12 | [../../../data/conversation/agents.ts](../../../data/conversation/agents.ts) |
| The `ConversationAgentStatus` union the tones enumerate. | L13 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The surface that derives the roster, owns the effective focus, and mounts this strip. | — | [ConversationSurface.tsx](ConversationSurface.tsx) |
| The component suite pinning the rendering states. | — | [AgentsArea.test.tsx](AgentsArea.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: created the sidecar for the R7 sub-agents strip —
  one roster-evidenced row per agent (label, word-carrying status chip, terminal final-message
  preview), the `N agents · M running` summary with honest `aria-expanded` collapse (static `0 agents`
  span on an empty roster), the ResizeObserver narrow default under 560px with the operator `override`
  winning, and the aria-current focus-toggle rows. Verification is pinned to the leaf base
  (`842b487`) because the new source file is uncommitted; closeout owns its first source stamp.
