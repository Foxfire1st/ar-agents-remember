# dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx

## Governing Overview

[session-cockpit/conversation-library overview](overview.md)

## Purpose

The native conversation list (design §4.4): a scrollable column of prior conversations paged by the
server-native cursor, never a locally-accumulated infinite index. Each row shows a boundary-truncated
title with the full value on hover (A5), the safe native id suffix, a humanized last-activity age
(A4), and a granular historical-completeness badge. A row is selectable for *preview only* — selecting
never opens or activates anything. A row's `agents` render as indented child rows
that select/preview/open through the exact same flow; the page's `agentsNote` renders verbatim when
the server reports (partial) agent unavailability.

## Code Commentary

### Logic

- **`completenessLabel`** cit:([`completenessLabel`], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx:79-82): reads `row.capabilities.completeness.state` and prints
  `full history` when `supported`, else `partial history` — honest per-row completeness, never a
  fabricated "complete".
- **`agentChildRow`** cit:([`agentChildRow`], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx:89-102): promotes one `ConversationLibraryAgentRow` to the
  SAME row shape the select/preview/open flow already consumes — the child's own server-minted
  `conversationKey` + `identityDigest`, its title/suffix/age, the PARENT's `capabilities` (the wire
  carries none per child; the harness read-path capabilities apply), and `agents: []` (no deeper
  nesting).
- **States** cit:(["library-list-error"], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx:126-146): typed `error` renders a `role="alert"`; an empty-while-loading row prints
  `loading <harness> history…`; a genuinely empty scope prints the A1 empty-state copy
  `No <harness> conversations in this project scope.` (no dash-chain).
- **`agentsNote`** cit:(["library-agents-note"], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx:149-153): rendered VERBATIM (data-testid `library-agents-note`)
  above the rows whenever the page's note is non-null and non-empty — the exact native reason agent
  conversations are (partially) unavailable, never silently absent.
- **Rows** cit:(["truncateMiddle(entry.title"], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx:154-197): each row is a real `<button>`; `data-selected` marks the previewed row;
  `title` carries the full untruncated title (A5) while `truncateMiddle(title, 60)` renders the
  boundary-truncated visible text; the meta line joins the completeness badge, the mono
  `…safeNativeIdSuffix`, and `humanizeAge(lastActivityAt)`. A row's `agents` render directly beneath
  it cit:([`agentChildRow`], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx:89-102) inside a `Fragment` keyed on the parent — the same row grammar plus the `agentChild`
  css cit:([`agentChild`], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx:73-76) (`2ch` inline indent, dashed border), a fixed `agent` badge, the `role` badge when
  present, suffix, and age; `data-testid="library-agent-row"`; clicking selects through
  `onSelect(agentChildRow(parent, agent))` — the identical flow, with the child's own key.
- **`Load more`** cit:(["Load more"], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx:164-164): rendered only when `nextCursor !== null`; disabled while loading —
  the R5 explicit native paging affordance (never infinite auto-scroll indexing).

### Invariants And Boundaries

- Selecting a row — parent OR agent child — is a preview action only; open/activate is
  `OpenConversationAction`'s exclusive job. A child opens through the exact same read/open path (its
  key is minted server-side, never fabricated in the browser).
- Paging is server-native cursor paging (`nextCursor`); the list is never turned into a durable local
  conversation database.
- Truncation always preserves the full value in `title` (A5); the age is always humanized (A4).
- `agentsNote` is rendered verbatim and only when non-empty; agent unavailability is never silent.
  Agent children inherit the parent's read-path capabilities (the wire carries none per child) and
  never nest further (`agents: []`).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Row/cursor/key wire types this list renders (now including `ConversationLibraryAgentRow`). [1]
- The A4/A5 presentation helpers (`humanizeAge`, `truncateMiddle`, `harnessLabel`). [2]
- The surface that owns selection/paging callbacks into the store and passes `agentsNote` through. [3]
- The sub-agent nesting + agentsNote regression suite for this list. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
