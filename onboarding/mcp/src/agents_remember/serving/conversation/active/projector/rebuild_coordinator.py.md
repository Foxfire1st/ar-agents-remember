# mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Native and echo channel state. | [native_ingestion.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py), [echo_ingestion.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/echo_ingestion.py) |
| Status derivation. | [status.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/status.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## 260731-EFA-L2 Current Delta

**`IngestionComponents`** (`native`, `echo`, `child_history`, `interactions`) is the coordinator's
new single collaborator argument: the four ingestion components one rebuild drives, **in the order
it must drive them**. A rebuild is not four independent refreshes — native evidence establishes the
timeline, echo ingestion fills the transcript gaps in it, child history hangs off the agents that
appeared, and the interaction projection reads what all three produced. Passing them as one set is
what keeps a coordinator from being wired to three components of this session and one of another.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `IngestionComponents` as the ordered four-component rebuild set.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the rebuild/poll
  coordinator sidecar. Verification metadata remains blank until commit.
