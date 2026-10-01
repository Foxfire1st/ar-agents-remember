# mcp/src/agents_remember/serving/codex_agent_lifecycle.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Centralizes authority ordering for status changes in the Codex adapter's bounded child registry.

## Code Commentary

### Logic

`merge_agent_status` prevents history or generic thread state from reopening a terminal child;
only an explicit later `turn/started` can prove a new lifecycle. `completed_turn_status` maps
Codex terminal spellings into the public completed/failed/interrupted roster vocabulary.

### Conventions

Authority ordering is shared by live notifications and history reconstruction rather than
duplicated in adapter branches.

### Invariants And Boundaries

- Terminal status is monotonic absent an explicit new turn.
- Cancelled and interrupted normalize to `interrupted`.
- Failed and errored normalize to `failed`.
- Unknown terminal spellings settle as `completed` only at the already-terminal turn boundary.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Adapter registry applies the shared ordering. [1]


### Cross-Repo References

The status spellings originate in Codex app-server evidence, but no external Domain Documentation
source was configured for this pass.
