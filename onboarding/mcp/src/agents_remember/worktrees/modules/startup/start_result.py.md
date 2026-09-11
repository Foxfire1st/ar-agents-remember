# mcp/src/agents_remember/worktrees/modules/startup/start_result.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/startup/start_result.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T15:04+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Real starts distinguish terminal start from background provider setup while preserving task-addressed guidance. | `started_result` | mcp/src/agents_remember/worktrees/modules/startup/start_result.py:16-50 |
| Preview builds the explicit apply packet and common task identity without mutation. | `_start_preview_result`; `_start_result_facts` | mcp/src/agents_remember/worktrees/modules/startup/start_result.py:53-116 |

## Cross-Repo References

No cross-repository boundary is owned here.

## 260821-CLIVE Start Result Evidence

`StartedWorktreeState` now carries the prepared memory-state facts alongside code and provider
state. Successful and converged start responses also expose bounded `projectionEffects` from any
authoritative lifecycle task restamp. These effects are follow-up scheduling results, not part of
whether the start contract/worktrees were accepted.

## Update History

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: documented memory state and post-task-publication projection effects in start results. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/modules/startup/start_result.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: `_start_result_facts` now reports an ignored terminal
  series-contract artifact under an organizational master as a `staleSeriesArtifact` fact.
  Verification remains closeout-owned.

- 2026-08-14T05:26Z — Created for the L23 final candidate after start-result projection was
  extracted from the start coordinator. Verification remains closeout-owned.
