# mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
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

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the rebuild/poll
  coordinator sidecar. Verification metadata remains blank until commit.
