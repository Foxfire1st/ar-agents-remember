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

- **Fixture** cit:([`interactionItem`], dashboard/src/panels/session-cockpit/conversation/InteractionItem.test.tsx:11-25): an `interactionItem()` factory — lane `interaction`, phase `waiting`, a
  single text prompt block — with the `agent` ref attached only when supplied.
- **Label fallback** cit:([`agentLabel`], dashboard/src/data/conversation/agents.ts:30-38): with no nickname/role/path bound, the badge falls back to
  `agent <first8>` (`agent abcdef12`) — the `agentLabel` precedence chain's floor.
- **Badge absent** cit:([`interactionItem`, "render(<InteractionItem item={interactionItem()} />)", "toBeNull"], dashboard/src/panels/session-cockpit/conversation/InteractionItem.test.tsx:11-25; dashboard/src/panels/session-cockpit/conversation/InteractionItem.test.tsx:49-50): a parent-conversation interaction (no agent ref) renders no badge at
  all.

### Invariants And Boundaries

- The suite pins the badge as bound-evidence-only: attribution is never invented for a
  parent-conversation interaction, and never omitted when an agent ref is bound.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test. | `InteractionItem` | dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:73-101 |
| The `ConversationItem`/`agent` ref type the fixture builds. | `ConversationItem`; `agent` | dashboard/src/data/conversation/types.ts:158-176 |
| The `agentLabel` precedence chain whose nickname and `agent <first8>` floors are pinned here. | `agentLabel` | dashboard/src/data/conversation/agents.ts:30-38 |

## Update History

- 2026-08-04T13:49:32+02:00 — 260731-EFA-L6 S18-B02 curator: extended the badge-absence claim through the no-agent render and null assertion and regenerated the final range with the scoped fixer.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: created the sidecar for the R7 interaction-badge
  suite — badge present with the asking agent's label, the `agent <first8>` fallback when no
  nickname/role/path is bound, and badge absent for a parent-conversation interaction. Verification
  is pinned to the leaf base (`842b487`) because the new source file is uncommitted; closeout owns
  its first source stamp.
