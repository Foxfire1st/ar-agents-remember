# dashboard/src/panels/AgentPickupIndicator.tsx

## Purpose

Task-row feedback for pending dashboard responses that have not yet been consumed by an agent.

## Governing Overview

[panels overview](overview.md)

## Code Commentary

Renders static inbox delivery/acknowledgment state for an `AgentPickupNode`. Fresh pending rows show a
bordered delivery marker and `brief unacknowledged` for dispatch briefs or `message unacknowledged` for
other messages. The exact `deliveryState` remains in the title; overdue `check-chat` rows keep the
dismiss action. There is no model-busy spinner, Motion dependency, generation inference, or second
poller. Dismiss calls `dismissOperatorInboxEntry(entryId)` and means developer-cleared warning, not
agent pickup.

## Invariants And Boundaries

- The component is driven by backend projection state, not local click memory.
- Dismiss means developer-cleared warning, not agent pickup.
- Inbox acknowledgment is independent from live hosted-chat `turnState`; an idle chat may sit beside a pending or overdue inbox row.
