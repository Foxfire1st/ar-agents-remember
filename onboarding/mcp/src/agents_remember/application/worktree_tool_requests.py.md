# mcp/src/agents_remember/application/worktree_tool_requests.py

## Governing Overview

[Application layer](overview.md)

## Purpose

Owns the immutable request concepts and shared defaults used by the worktree application entry
points. The extraction keeps argument meaning in one typed module while `worktree_tools.py` remains
the operation-composition facade.

## Code Commentary

### Logic

`CloseoutCommitMessages` and `OperationControlRequest` expose only code and memory subjects.
`LandedCommits` records the landed code SHA and optional memory-content SHA; it carries no ledger
output. Approval, candidate admission, generation checks, and corrective dispositions retain their
separate typed meanings.

`TaskIdentity`, `TaskBases`, and `StartExecution` describe task creation. `OperationControlRequest`
describes one public lifecycle-control request and normalizes public JSON-shaped caller, grade, and
admission values into their canonical models. `CloseoutCommitMessages` remains separate from
`CloseoutApproval`, so a preview cannot look approved merely because it carries commit text.
`FinalizeTaskDocs` names only the task-document addresses reconciled by finalization.

The defaults are real typed instances: ordinary callers share the repository-default task bases,
normal start execution, preview-only closeout approval, and no-task-doc finalization values.
`LifecycleControlAction` is imported from the integration control owner rather than re-declared at
the application boundary.

### Conventions

Keep request concepts immutable and approval separate from commit text; normalize only the canonical typed public values.

### Invariants And Boundaries

- This module owns request data and input normalization; it performs no Git, filesystem, journal,
  queue, or task-document mutation.
- `CloseoutApproval` and `CloseoutCommitMessages` must remain distinct types.
- Public JSON reconstruction is bounded to the three canonical models in
  `OperationControlRequest.__post_init__`; unknown compatibility shapes are not inferred.
- Callers use these exact types and defaults; they must not re-derive equivalent dictionaries.

### Todos

No additional file-local TODO is established by this candidate review.

## Evidence

### Docs References

No external Domain Documentation source is configured. These are repository-owned application
contracts.

No configured external domain-documentation source applies.

### Repo-Internal References

- Raw closeout/control messages and landed commits contain only code/memory values. [1]
- Task-start concepts and shared defaults have one definition. [2]
- Lifecycle control reconstructs only canonical typed public values. [3]
- Closeout approval, messages, and finalization documents remain separate concepts. [4]
- Start consumes its extracted request type. [5]
- Operation control consumes its extracted request type. [6]
- The start tool consumes the request types this module extracts. [7]
- Closeout apply consumes its extracted request type. [8]

### Cross-Repo References

No cross-repository boundary is owned here.


No separate external implementation source applies to this file.
