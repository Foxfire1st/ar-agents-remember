# mcp/src/agents_remember/worktrees/modules/start_result.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/start_result.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T05:26Z |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038` |
| lastVerifiedCommitDate |  2026-08-14T08:23:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree modules overview](overview.md)

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
enclosure identity fields.

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
| Real starts distinguish terminal start from background provider setup while preserving task-addressed guidance. | `started_result` | mcp/src/agents_remember/worktrees/modules/start_result.py:16-50 |
| Preview builds the explicit apply packet and common task identity without mutation. | `_start_preview_result`; `_start_result_facts` | mcp/src/agents_remember/worktrees/modules/start_result.py:53-116 |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-14T05:26Z — Created for the L23 final candidate after start-result projection was
  extracted from the start coordinator. Verification remains closeout-owned.
