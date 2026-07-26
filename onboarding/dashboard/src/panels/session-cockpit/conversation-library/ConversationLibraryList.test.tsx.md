# dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+02:00 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation-library overview](overview.md)

## Purpose

The regression suite for the library list's harness sub-agent grouping — the tests
that lock the nested-child-row contract and the `agentsNote` capability-honesty render. It mounts the
real `ConversationLibraryList` via `@testing-library/react` with fixture rows, so it proves the
rendered DOM and the selection payload without a server.

## Code Commentary

### Logic

Helpers: `capabilities()` builds an all-`supported` `HistoryCapabilities` block; `row(overrides)`
builds a parent `ConversationLibraryRow`; the `AGENT` constant is one `ConversationLibraryAgentRow`
fixture (own key `key-agent-1`, role `explorer`); `renderList(rows, agentsNote?)` mounts the list with
a spy `onSelect`. `afterEach` cleans up. The four cases prove:

- **child rows render under the parent with label + suffix** (L64-L73): `library-agent-row` carries
  the child title, the mono `…AG3NT1` suffix, and the `explorer` role badge; the parent
  `library-row` renders unchanged, without the agent badge.
- **a child selects through the same flow with its own server-minted key** (L75-L86): clicking the
  child calls `onSelect` once with a promoted row whose `conversationKey`/`identityDigest` are the
  CHILD's, `agents` is `[]` (no deeper nesting), and `capabilities` follow the parent's read path.
- **no child rows without agents** (L88-L91): a row with no `agents` renders no
  `library-agent-row` at all.
- **agentsNote verbatim when present, nothing when absent** (L93-L105): the exact note string
  renders in `library-agents-note`; with `null` the testid is absent from the DOM.

### Invariants And Boundaries

- The suite is the durable guard on the sub-agent grouping contract: a regression that drops the child-row grammar,
  fabricates a child key client-side, lets children nest, decouples the child's capabilities from the
  parent's read path, or silently swallows the `agentsNote` breaks it.
- Fixtures assert the wire honesty the list relies on: the child's key is server-minted (the test
  never constructs one through any browser-side minting path), and the note is compared
  string-for-string (verbatim, never paraphrased).

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
| The list component under test (child-row grammar, `agentChildRow`, agentsNote render). | L14 | [ConversationLibraryList.tsx](ConversationLibraryList.tsx) |
| The wire types the fixtures build (`ConversationLibraryRow`, `HistoryCapabilities`, `LibraryConversationKey`). | L9-L13 | [../../../data/conversation-library/types.ts](../../../data/conversation-library/types.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T15:40+02:00 — 260718-CHATS-L7 curator: created the sidecar for the sub-agent nesting
  suite — indented child rows with label/suffix/role badges, same-flow selection with the child's
  own server-minted key (parent-inherited capabilities, no deeper nesting), no-child-rows-without-
  agents, and the verbatim/absent `agentsNote` proof. Verification is pinned to the leaf base
  (`842b487`) because the new source file is uncommitted; closeout owns its first source stamp.
