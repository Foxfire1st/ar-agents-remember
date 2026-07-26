# dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/AgentsArea.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The `AgentsArea` component suite (R7): it pins the strip's rendering states — one
live row per roster-evidenced agent with label + status chip + terminal preview, the static collapsed
summary on an empty roster, the honest `aria-expanded` expand/collapse toggle, and row activation
driving the focus callback both ways.

## Code Commentary

### Logic

- **Fixtures** (L11-L24): an `agent()` factory defaulting to `status: "running"` and a `renderArea`
  helper with a spy `onFocusAgent`.
- **Empty roster** (L31-L37): the summary is `0 agents` rendered as a SPAN — nothing to expand, so
  no dead toggle — and no rows mount.
- **Row rendering** (L39-L61): three agents yield three rows, the summary reads `3 agents · 1
  running`, the chips carry their status words in order, and the final-message preview renders ONLY
  where terminal evidence carried it (one preview, full text also in `title`). jsdom's ResizeObserver
  never fires, so the area is never narrow: expanded by default.
- **Focus marking** (L63-L66): the focused agent's row carries `aria-current="true"`.
- **Summary toggle** (L68-L80): the summary button reports an honest `aria-expanded`; clicking it
  collapses the rows away and restores them on re-click.
- **Focus callback** (L82-L91): activating a row calls `onFocusAgent` with that agent id; activating
  the already-focused row calls it with `null` (back to the parent conversation).

### Invariants And Boundaries

- The suite renders the real component with derived-shape fixtures; it never asserts styling — the
  pinned contract is structure, words, and callback semantics.
- The terminal-preview assertion guards the evidence-only rule: a non-terminal row carries no
  preview element at all.

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
| The component under test. | L9 | [AgentsArea.tsx](AgentsArea.tsx) |
| The `ConversationAgentView` shape the fixtures build. | L8 | [../../../data/conversation/agents.ts](../../../data/conversation/agents.ts) |
| The surface-level focus behavior this strip plugs into (separate suite). | — | [ConversationAgentFocus.test.tsx](ConversationAgentFocus.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: created the sidecar for the R7 AgentsArea suite —
  the static `0 agents` summary (no dead toggle), one row per agent with word-carrying chips and the
  terminal-only preview, honest `aria-expanded` collapse, `aria-current` focus marking, and the
  row-activation focus toggle (focus agent / back to parent). Verification is pinned to the leaf base
  (`842b487`) because the new source file is uncommitted; closeout owns its first source stamp.
