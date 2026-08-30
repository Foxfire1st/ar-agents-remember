# mcp/src/agents_remember/application/worktree_tool_requests.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/worktree_tool_requests.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:43+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Application layer](overview.md)

## Purpose

Owns the immutable request concepts and shared defaults used by the worktree application entry
points. The extraction keeps argument meaning in one typed module while `worktree_tools.py` remains
the operation-composition facade.

## Code Commentary

`TaskIdentity`, `TaskBases`, and `StartExecution` describe task creation. `OperationControlRequest`
describes one public lifecycle-control request and normalizes public JSON-shaped caller, grade, and
admission values into their canonical models. `CloseoutCommitMessages` remains separate from
`CloseoutApproval`, so a preview cannot look approved merely because it carries commit text.
`FinalizeTaskDocs` names only the task-document addresses reconciled by finalization.

The defaults are real typed instances: ordinary callers share the repository-default task bases,
normal start execution, preview-only closeout approval, and no-task-doc finalization values.
`LifecycleControlAction` is imported from the integration control owner rather than re-declared at
the application boundary.

## Invariants And Boundaries

- This module owns request data and input normalization; it performs no Git, filesystem, journal,
  queue, or task-document mutation.
- `CloseoutApproval` and `CloseoutCommitMessages` must remain distinct types.
- Public JSON reconstruction is bounded to the three canonical models in
  `OperationControlRequest.__post_init__`; unknown compatibility shapes are not inferred.
- Callers use these exact types and defaults; they must not re-derive equivalent dictionaries.

## Docs References

No external Domain Documentation source is configured. These are repository-owned application
contracts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Task-start concepts and shared defaults have one definition. | `TaskIdentity`; `TaskBases`; `StartExecution`; `DEFAULT_TASK_BASES`; `DEFAULT_START_EXECUTION` | mcp/src/agents_remember/application/worktree_tool_requests.py:15-63 |
| Lifecycle control reconstructs only canonical typed public values. | `OperationControlRequest` | mcp/src/agents_remember/application/worktree_tool_requests.py:66-95 |
| Closeout approval, messages, and finalization documents remain separate concepts. | `CloseoutCommitMessages`; `CloseoutApproval`; `FinalizeTaskDocs` | mcp/src/agents_remember/application/worktree_tool_requests.py:98-128 |
| The worktree facade's start, operation-control, and closeout entry points consume the extracted request types. | `worktree_start_tool`; `worktree_operation_control_tool`; `worktree_closeout_apply_tool` | mcp/src/agents_remember/application/worktree_tools.py:125-222; mcp/src/agents_remember/application/worktree_tools.py:524-538; mcp/src/agents_remember/application/worktree_tools.py:705-725 |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-26T10:44:52+02:00 — No request behavior change: closeout-source models moved into their package and `LifecycleControlAction` now comes from the canonical operation-kind model owner.

- 2026-08-24T21:43+02:00 — Created for the hard-limit repair that extracted typed worktree request
  concepts from `worktree_tools.py` without changing their public behavior.