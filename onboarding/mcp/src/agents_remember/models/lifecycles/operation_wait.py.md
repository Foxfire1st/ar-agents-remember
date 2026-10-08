# `mcp/src/agents_remember/models/lifecycles/operation_wait.py`

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

The retained value vocabulary of the read-only lifecycle status-change wait: LifecycleWaitOutcome and its named constants. These declarations describe the wait controller's outcomes; the former worktree_status_wait application/tool and WorktreeStatusWaitResponse consumer were removed and are not a current mounted wire route.

## Code Commentary

### Logic

`LifecycleWaitOutcome` distinguishes coherent outcomes (`changed`,
`unchanged`, `successor`) from typed read-only refusals
(`wrong-contract`, `no-operation`, `wrong-generation`,
`wrong-cursor`, `journal-replaced`, `journal-unreadable`, and
`projection-incoherent`). The module exports one constant per outcome
(`OUTCOME_CHANGED`, `OUTCOME_UNCHANGED`, `OUTCOME_SUCCESSOR`,
`OUTCOME_NO_OPERATION`, `OUTCOME_WRONG_GENERATION`,
`OUTCOME_WRONG_CURSOR`, `OUTCOME_JOURNAL_REPLACED`,
`OUTCOME_JOURNAL_UNREADABLE`, `OUTCOME_WRONG_CONTRACT`) so the application
layer never spells raw string literals.

### Conventions

Coherent outcomes return a snapshot plus the next meaningful cursor; every refusal is read-only and
never recommends a mutating action.

### Invariants And Boundaries

- The outcome Literal is the single shared wait vocabulary across layers and tests.
- `projection-incoherent` (CCR-R18) refuses when the record advanced but its public
  projection is incoherent: no snapshot and no mutating recommendation is returned.

### Todos

None.

## Evidence

### Docs References

No configured external Domain Documentation source governs this internal vocabulary.

No configured external source governs this strict wait vocabulary.

### Repo-Internal References

- The one typed wait-outcome Literal and its constants. [1]
- The read-only bounded wait loop returning these outcomes. [2]
The application controller that translated outcomes into the public response, and the `worktree_status_wait` tool it served, were deleted with the door/operation plane (commit `41b0812e`).
- The durable cursor the waiters compare. [4]

### Cross-Repo References

No cross-repository wait vocabulary is defined here.

- The vocabulary is one repository's lifecycle wait contract. [5]

## 260831-CCR-L15 Wait Outcome Vocabulary

Created with the lifecycle status-change waiting tool: coherent reads return a snapshot plus the
next meaningful cursor; every other outcome is a typed read-only refusal, and the
`projection-incoherent` member (CCR-R18) covers the record-advanced-but-projection-
incoherent case without recommending mutation.
