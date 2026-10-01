# mcp/src/agents_remember/serving/conversation/active/agent_history.py

## Governing Overview

[active conversation overview](overview.md)

## Purpose

Defines the selected-child history outcome returned by the active projector and constructs the
child-bound timeline item that makes native-history unavailability and recovery visible without
changing parent conversation health.

## Code Commentary

### Logic

`AgentHistoryHydration` carries one of `hydrated`, `already-hydrated`, `unavailable`, or
`not-eligible` plus exact child id and optional typed detail/code. `agent_history_state_item`
upserts the stable `agent-history:<agent-id>` row as an error on failure or a notice on recovery,
with the child `ConversationAgentRef` and native-only provenance attached.

### Conventions

The object is an active-serving result, not a transport exception and not parent status. Recovery
reuses the same stable item id so the projection store advances the existing child-local row.

### Invariants And Boundaries

- Every state row is bound to the selected child's evidence-backed agent reference.
- Unavailable/recovered state never fabricates conversation content and never becomes parent stream
  failure.
- This module does not perform native I/O, synchronization, retry, or HTTP serialization.

### Todos

None known.

## Evidence

### Docs References

`system/sources.md` has no configured Domain Documentation entries, so no live domain-documentation
pass was available.

No configured domain documentation could be checked.

### Repo-Internal References

The projector owns I/O and applies these outcomes only at the selected-child boundary; the API
serializes the same status vocabulary.

### Cross-Repo References

No cross-repository boundary is implemented here.

No meaningful cross-repo references found.
