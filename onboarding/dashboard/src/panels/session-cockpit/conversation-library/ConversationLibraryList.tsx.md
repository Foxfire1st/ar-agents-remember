# dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+02:00 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

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

- **`completenessLabel`** (L79-L82): reads `row.capabilities.completeness.state` and prints
  `full history` when `supported`, else `partial history` — honest per-row completeness, never a
  fabricated "complete".
- **`agentChildRow`** (L89-L102): promotes one `ConversationLibraryAgentRow` to the
  SAME row shape the select/preview/open flow already consumes — the child's own server-minted
  `conversationKey` + `identityDigest`, its title/suffix/age, the PARENT's `capabilities` (the wire
  carries none per child; the harness read-path capabilities apply), and `agents: []` (no deeper
  nesting).
- **States** (L126-L146): typed `error` renders a `role="alert"`; an empty-while-loading row prints
  `loading <harness> history…`; a genuinely empty scope prints the A1 empty-state copy
  `No <harness> conversations in this project scope.` (no dash-chain).
- **`agentsNote`** (L149-L153): rendered VERBATIM (data-testid `library-agents-note`)
  above the rows whenever the page's note is non-null and non-empty — the exact native reason agent
  conversations are (partially) unavailable, never silently absent.
- **Rows** (L154-L197): each row is a real `<button>`; `data-selected` marks the previewed row;
  `title` carries the full untruncated title (A5) while `truncateMiddle(title, 60)` renders the
  boundary-truncated visible text; the meta line joins the completeness badge, the mono
  `…safeNativeIdSuffix`, and `humanizeAge(lastActivityAt)`. A row's `agents` render directly beneath
  it (L174-L195) inside a `Fragment` keyed on the parent — the same row grammar plus the `agentChild`
  css (L72-L77: `2ch` inline indent, dashed border), a fixed `agent` badge, the `role` badge when
  present, suffix, and age; `data-testid="library-agent-row"`; clicking selects through
  `onSelect(agentChildRow(parent, agent))` — the identical flow, with the child's own key.
- **`Load more`** (L198-L202): rendered only when `nextCursor !== null`; disabled while loading —
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
| Row/cursor/key wire types this list renders (now including `ConversationLibraryAgentRow`). | L14-L19 | [../../../data/conversation-library/types.ts](../../../data/conversation-library/types.ts) |
| The A4/A5 presentation helpers (`humanizeAge`, `truncateMiddle`, `harnessLabel`). | L12 | [../../../data/conversation/format.ts](../../../data/conversation/format.ts) |
| The surface that owns selection/paging callbacks into the store and passes `agentsNote` through. | L137-L150 | [ConversationLibrarySurface.tsx](ConversationLibrarySurface.tsx) |
| The sub-agent nesting + agentsNote regression suite for this list. | — | [ConversationLibraryList.test.tsx](ConversationLibraryList.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T15:40+02:00 — 260718-CHATS-L7 curator: refreshed for the harness sub-agent grouping —
  `agentChildRow` promotion (child's own server-minted key + parent's read-path capabilities,
  `agents: []`), indented dashed child rows with `agent`/role badges, and the verbatim `agentsNote`
  render; all line citations re-stamped against the post-L7 source and the new test file added to the
  references. The L7 source is uncommitted, so lastVerifiedCommit* stays on the prior stamp and
  closeout re-stamps verification.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the native
  cursor-paged conversation list — preview-only rows, boundary-truncated title with full-value
  affordance (A5), humanized age (A4), per-row completeness badge, and explicit `Load more` native
  paging. Verification is pinned to the leaf base (`0be0099`) because the new source file is
  uncommitted; closeout owns its first source stamp.
