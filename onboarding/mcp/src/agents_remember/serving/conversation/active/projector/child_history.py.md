# mcp/src/agents_remember/serving/conversation/active/projector/child_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/child_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Public `AgentHistoryHydration` records status/detail/code, and `agent_history_state_item` renders unavailable/recovered child-local rows. | `AgentHistoryHydration`; `agent_history_state_item` | mcp/src/agents_remember/serving/conversation/active/agent_history.py:19-26; mcp/src/agents_remember/serving/conversation/active/agent_history.py:29-70 |

| Concurrent reconnect requests share one active projector and return the same page/events/`child_history` object. | `test_concurrent_reconnect_replaces_a_retired_projector_once` | mcp/tests/test_active_projector_singleflight.py:24-94 |

## Cross-Repo References

No meaningful cross-repository references found.

## 260731-EFA-L2 Current Delta

The constructor is now `ChildHistoryProjection(spine, readers, native)`:

- `spine: SessionProjectionSpine` supplies the parent thread id, bridge epoch, controlled session,
  mapper, mutation stream, agent authority, evidence refs, apply lock and clock — see
  [wiring.py](wiring.py.md). `parent_thread_id` and `bridge_epoch` are now derived from the
  identity by the spine's own properties rather than passed in.
- `readers: BridgeReaders` supplies the native-page reader (the whole read surface is substituted as
  one set).
- `native: NativeEvidenceIngestion` stays an explicit collaborator, because it is this component's
  peer rather than shared machinery.

Behaviour, hydration ordering and the walked/failures/inflight bookkeeping are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: split hydration-result and regression-test ownership, restoring the public row renderer and concurrent reconnect return-value spans.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: constructor now takes `SessionProjectionSpine` + `BridgeReaders` (plus the native ingestion peer); parent thread id and epoch come from the spine.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the selected-child
  history sidecar and recorded its demand, singleflight, capacity, and failure-containment
  boundaries. Verification metadata remains blank until commit.
