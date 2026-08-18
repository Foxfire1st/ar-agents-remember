# mcp/src/agents_remember/worktrees/organizational_completion_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/organizational_completion_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-17T12:09+02:00 |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad` |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Publishes the final organizational leaf integration from the closeout queue into the sprint super under one integration authority, pinning final-versus-nonfinal scope.

## Code Commentary

### Logic

`preview_organizational_completion` reads the exact final-leaf decision for the integration dry-run. `publish_queue_candidate_integration_result_under_authority` runs the publication under the integration authority lock; when a completion plan exists it re-validates the durable full-gate certification and publishes the master completion marker only after the certified ref movement succeeded (`returncode == 0`). `organizational_completion_scope_block` refuses a final/non-final classification change between preflight and protected publication. `_require_completed_integration_recovery` proves the finalized contract, durable operation record, and queue-completion intent before re-consuming a completed integration.

### Invariants And Boundaries

- Every irreversible publication re-verifies the exact candidate, commits, and completion scope.
- The queue candidate's immutable claim is retained through Git recovery of torn ref state.
- A completed organizational master must carry its durable full-gate certification.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Final/non-final scope drift is refused before protected publication. | `organizational_completion_scope_block` | mcp/src/agents_remember/worktrees/organizational_completion_integration.py:58-78 |
| Dry-run reads the exact final-leaf decision. | `preview_organizational_completion` | mcp/src/agents_remember/worktrees/organizational_completion_integration.py:81-119 |
| Leaf landing publication pins scope and publishes the master marker. | `publish_queue_candidate_integration_result_under_authority` | mcp/src/agents_remember/worktrees/organizational_completion_integration.py:122-186 |
| Completed-integration recovery re-proves the finalized contract and durable removal intent. | `_require_completed_integration_recovery` | mcp/src/agents_remember/worktrees/organizational_completion_integration.py:189-254 |
| Recovery candidate keeps its immutable queue claim. | `_require_integration_recovery_candidate` | mcp/src/agents_remember/worktrees/organizational_completion_integration.py:305-336 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for organizational completion queue-to-repository publication.
