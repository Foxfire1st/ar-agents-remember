# dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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
| Row/cursor/key wire types this list renders (now including `ConversationLibraryAgentRow`). | `ConversationLibraryAgentRow` | dashboard/src/data/conversation-library/types.ts:39-50 |
| The A4/A5 presentation helpers (`humanizeAge`, `truncateMiddle`, `harnessLabel`). | `humanizeAge` | dashboard/src/data/conversation/format.ts:40-47 |
| The surface that owns selection/paging callbacks into the store and passes `agentsNote` through. | "agentsNote={listView.agentsNote}" | dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx:236-236 |
| The sub-agent nesting + agentsNote regression suite for this list. | "ConversationLibraryList agent nesting" | dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx:43-86 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T18:07+02:00 — 260731-EFA-L6 S18-B17 curator: rewrote the seven superseded `(L…)`
  prose line-cites as cit forms with exact frozen-source ranges (plus the `agentChild` css
  sub-reference, corrected from L72-L77 to its real 73-76), and repaired the two malformed
  Repo-Internal rows with anchors `humanizeAge` and the `"ConversationLibraryList agent nesting"`
  describe literal. Claim wording unchanged; every anchor verified verbatim in the frozen source.
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
