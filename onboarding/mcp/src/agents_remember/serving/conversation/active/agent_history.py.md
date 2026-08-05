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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The projector owns I/O and applies these outcomes only at the selected-child boundary; the API
serializes the same status vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |

## Cross-Repo References

No cross-repository boundary is implemented here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-08-04T13:00:51+02:00 — 260731-EFA-L6 S18-B11 curator: reconciled the projector/API/test ledger, converted the package-split history citation, and supplied scoped fixer input for generated ranges. Verification metadata unchanged.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the cross-file citation after the `active/projector.py` to `active/projector/` package split. The typed-native-history catch and unavailable/recovered row minting are owned by `ChildHistoryProjection._hydrate` cit:([`_hydrate`], mcp/src/agents_remember/serving/conversation/active/projector/child_history.py:99-137).

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: created strict 1:1 onboarding for the
  child-local hydration result and stable unavailable/recovered projection row. Verification
  metadata remains blank because the new source is uncommitted.
