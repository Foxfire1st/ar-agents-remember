# dashboard/src/panels/session-cockpit/conversation/InteractionItem.test.tsx

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

## Evidence

### Repo-Internal References

- The component under test. [1]
- The `ConversationItem`/`agent` ref type the fixture builds. [2]
- The `agentLabel` precedence chain whose nickname and `agent <first8>` floors are pinned here. [3]
