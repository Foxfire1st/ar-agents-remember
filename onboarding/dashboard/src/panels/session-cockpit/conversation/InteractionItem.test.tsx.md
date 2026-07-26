# dashboard/src/panels/session-cockpit/conversation/InteractionItem.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/InteractionItem.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The `InteractionItem` agent-badge suite (R7): an interaction-lane item carrying an
agent ref (a sub-agent's multiplexed approval request) badges WHO is asking, from the bound evidence
only; a parent-conversation interaction stays unbadged.

## Code Commentary

### Logic

- **Fixture** (L11-L25): an `interactionItem()` factory — lane `interaction`, phase `waiting`, a
  single text prompt block — with the `agent` ref attached only when supplied.
- **Badge present** (L32-L39): an item carrying `{ agentId: "t-1", nickname: "scout" }` renders the
  `interaction-agent-badge` with the nickname label.
- **Label fallback** (L41-L46): with no nickname/role/path bound, the badge falls back to
  `agent <first8>` (`agent abcdef12`) — the `agentLabel` precedence chain's floor.
- **Badge absent** (L48-L51): a parent-conversation interaction (no agent ref) renders no badge at
  all.

### Invariants And Boundaries

- The suite pins the badge as bound-evidence-only: attribution is never invented for a
  parent-conversation interaction, and never omitted when an agent ref is bound.

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
| The component under test. | L9 | [InteractionItem.tsx](InteractionItem.tsx) |
| The `ConversationItem`/`agent` ref type the fixture builds. | L8 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The `agentLabel` precedence chain whose nickname and `agent <first8>` floors are pinned here. | — | [../../../data/conversation/agents.ts](../../../data/conversation/agents.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: created the sidecar for the R7 interaction-badge
  suite — badge present with the asking agent's label, the `agent <first8>` fallback when no
  nickname/role/path is bound, and badge absent for a parent-conversation interaction. Verification
  is pinned to the leaf base (`842b487`) because the new source file is uncommitted; closeout owns
  its first source stamp.
