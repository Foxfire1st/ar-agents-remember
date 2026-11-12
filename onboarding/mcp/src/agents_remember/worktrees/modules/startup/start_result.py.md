# mcp/src/agents_remember/worktrees/modules/startup/start_result.py

## Governing Overview

[worktree modules overview](../overview.md)

## Purpose

Construct the terminal wire result for one worktree-start attempt. The module separates result
projection from start mutation so previews and completed starts share one fact set while retaining
different recovery guidance.

## Code Commentary

### Logic

`started_result` returns either the preview builder or a completed `started` result and adjusts the
summary when provider setup continues asynchronously. `_start_preview_result` builds the exact
task-addressed apply call, omitting a source branch only for a not-yet-materialized parent and
preserving caller-owned recovery inputs. `_start_result_facts` emits the common contract and
enclosure identity fields and, since 260815-DAG-L13, appends a `staleSeriesArtifact` fact when the
start ignored a terminal series contract artifact under an organizational master (L13-R5b — the
artifact no longer owns anything, so the start reports it instead of refusing).

### Conventions

Results use `WorktreeCommandResult`; phase moves use `next_guidance`, while the preview's explicit
apply action uses `recovery_guidance`.

### Invariants And Boundaries

- Preview never mutates and returns `would-start` plus a complete apply packet.
- Real start returns `started` even when provider setup continues in the background.
- Common contract identity is rendered once for both paths.
- This module does not create worktrees, write contracts, or launch providers.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References

- Real starts distinguish terminal start from background provider setup while preserving task-addressed guidance. [1]
- Preview builds the explicit apply packet and common task identity without mutation. [2]

### Cross-Repo References

No cross-repository boundary is owned here.

### 260821-CLIVE Start Result Evidence

`StartedWorktreeState` now carries the prepared memory-state facts alongside code and provider
state. Successful and converged start responses also expose bounded `projectionEffects` from any
authoritative lifecycle task restamp. These effects are follow-up scheduling results, not part of
whether the start contract/worktrees were accepted.
