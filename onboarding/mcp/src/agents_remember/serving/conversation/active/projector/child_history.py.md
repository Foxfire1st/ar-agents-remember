# mcp/src/agents_remember/serving/conversation/active/projector/child_history.py

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

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Public `AgentHistoryHydration` records status/detail/code, and `agent_history_state_item` renders unavailable/recovered child-local rows. [1]

| Concurrent reconnect requests share one active projector and return the same page/events/`child_history` object. | `test_concurrent_reconnect_replaces_a_retired_projector_once` | mcp/tests/test_active_projector_singleflight.py:24-94 |

### Cross-Repo References

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
