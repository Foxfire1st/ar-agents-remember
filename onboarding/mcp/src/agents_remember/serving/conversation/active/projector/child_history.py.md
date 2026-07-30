# mcp/src/agents_remember/serving/conversation/active/projector/child_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/child_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Provides bounded, selected-child native-history hydration without making child history part of
every parent page.

## Code Commentary

### Logic

`ChildHistoryProjection.refresh` admits only a live, non-parent child on a native-page harness.
Requests for the same thread share one shielded task; at most 64 distinct child walks can be in
flight. The walk pages one thread, removes roster rows, scopes native item ids to the child, binds
agent identity, suppresses proven live twins, and applies results under the shared lock.

Typed native-history capacity or availability errors project one child-local unavailable row.
A successful retry replaces that state with a recovered row. Parent projection and sibling
hydrations remain usable.

### Conventions

Selection is the demand signal. No background loop walks every child.

### Invariants And Boundaries

- A child is hydrated at most once per projector unless an earlier attempt failed.
- Concurrent requests for one child share exactly one source walk.
- Cancelling one waiter does not cancel shared hydration.
- Child failures never gap or close the parent stream.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public hydration result and unavailable/recovered rows. | [agent_history.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/agent_history.py) |
| Production and singleflight regressions. | [test_codex_history_production_path.py](agents-remember/mcp/tests/test_codex_history_production_path.py), [test_active_projector_singleflight.py](agents-remember/mcp/tests/test_active_projector_singleflight.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the selected-child
  history sidecar and recorded its demand, singleflight, capacity, and failure-containment
  boundaries. Verification metadata remains blank until commit.
