# mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Serializes initial hydration, page assembly, incremental polling, status observation, and
submission-provenance resolution.

## Code Commentary

### Logic

`ensure_hydrated` is singleflight behind a hydration lock. `_rebuild` resets every component,
captures adapter identity before mapping, walks native parent history where supported, then polls
evidence/echo/native continuation/provenance and observes a fresh snapshot. Page and poll paths
run behind the shared apply lock, so each returned page pairs an atomic item window with its event
cursor and current status. Provenance reads are capped at 64 pending request ids per cycle.

### Conventions

The coordinator decides operation order but does not own source watermarks, canonical store state,
or child-history task state.

### Invariants And Boundaries

- One hydration runs at a time.
- Page items and returned event cursor describe the same locked projection state.
- `total_items` is reported only when all parent authority windows are complete.
- Child refresh reuses the hydrated graph and its shared apply lock.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Native polling establishes the timeline and native continuation is then followed by echo polling for transcript gaps; the coordinator composes them in order. [1]
- Echo polling fills transcript gaps in the ordered rebuild. [2]
- Conversation status is derived by the status service. [3]

### Cross-Repo References

No meaningful cross-repository references found.

## 260731-EFA-L2 Current Delta

**`IngestionComponents`** (`native`, `echo`, `child_history`, `interactions`) is the coordinator's
new single collaborator argument: the four ingestion components one rebuild drives, **in the order
it must drive them**. A rebuild is not four independent refreshes — native evidence establishes the
timeline, echo ingestion fills the transcript gaps in it, child history hangs off the agents that
appeared, and the interaction projection reads what all three produced. Passing them as one set is
what keeps a coordinator from being wired to three components of this session and one of another.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
