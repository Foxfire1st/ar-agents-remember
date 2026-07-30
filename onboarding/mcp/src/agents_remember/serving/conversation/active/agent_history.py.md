# mcp/src/agents_remember/serving/conversation/active/agent_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/agent_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

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

## Docs References

`system/sources.md` has no configured Domain Documentation entries, so no live domain-documentation
pass was available.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The projector owns I/O and applies these outcomes only at the selected-child boundary; the API
serializes the same status vocabulary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The projector catches only typed native-history outcomes and mints unavailable/recovered rows under the apply lock. | L502-L586 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |
| The active route serializes status, exact child id, detail, and code. | L153-L187 | [api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |
| Projection regressions prove local failure, sibling continuity, same-child singleflight, capacity refusal, and revision-two recovery. | L677-L1052 | [test_conversation_projector_codex_agents.py](agents-remember/mcp/tests/test_conversation_projector_codex_agents.py) |

## Cross-Repo References

No cross-repository boundary is implemented here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: created strict 1:1 onboarding for the
  child-local hydration result and stable unavailable/recovered projection row. Verification
  metadata remains blank because the new source is uncommitted.
