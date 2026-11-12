# `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py`

## Governing Overview

[Lifecycle Operation Integration overview](../overview.md)

## Purpose

Read-only bounded wait on lifecycle meaningful-state changes (CCR-R15). The wait is addressed by
canonical contract, operation kind, expected public generation, and an opaque typed afterRevision
(the durable meaningful-state cursor of a prior snapshot). It never accepts an operation key or
PID, never acquires the lifecycle/queue/gate/worker authority, and never writes the journal: every
read goes through `LifecycleOperationStore.read` (lock-free), so waiters can neither block
writers nor mutate state.

## Code Commentary

### Logic

`LifecycleWaitClock` owns the poll cadence (`DEFAULT_POLL_SECONDS` = 0.05) and
the transport cannot be coerced into an unbounded sleep
(`MAX_WAIT_SECONDS` = 60.0 hard cap regardless of the requested bound).
`validate_wait_cursor` returns the typed wrong-cursor refusal for a zero/negative cursor
(a caller without a prior snapshot gets a typed refusal instead of a schema error).
`wait_for_lifecycle_change` loops the bounded long-poll realization: it re-reads the
journal and compares the record's `meaningfulRevision` against the waited cursor; a lower
cursor is a wrong-cursor refusal, a higher cursor on the same generation is the changed outcome, a
generation successor wakes an old-generation wait with explicit successor information (proved
against the archived predecessor's successor fingerprint, capped at 4 MiB of archive), and a
timeout returns unchanged as a normal outcome — never a failure. Wrong contract/generation and
unreadable/replaced journals refuse typed.

### Conventions

Cursor semantics follow CCR-R15 exactly: meaningfulRevision advances only for generation,
status/phase, disposition, approval claim, irreversible boundary, mutation evidence, typed
actionable failure, result, cancellation/recovery, or finalization changes; heartbeat age,
unchanged current command, log growth, queue changes, and repeated snapshots advance only
recordRevision and never wake a waiter.

### Invariants And Boundaries

- The wait is read-only: no prompts, retries, cancels, or journal writes.
- Successor detection is proved from the archived predecessor's successor fingerprint.
- Timeout is unchanged, never failure; every refusal names the exact next read-only snapshot
  action.

### Todos

None.

## Evidence

### Docs References

No configured external Domain Documentation source governs this observer.

No configured external source governs this wait observer.

### Repo-Internal References

- The wait loop and its poll clock. [1]
- Typed cursor validation and mismatch decisions. [2]
- Archived-predecessor successor proof. [3]
- The shared outcome vocabulary. [4]
- The exact record cursor the waiter compares. [5]
The application wait controller that used this loop was deleted with the door/operation plane (commit `41b0812e`).

### Cross-Repo References

No cross-repository boundary is crossed by this observer.

- The wait loop observes one repository's lifecycle journal. [6]

## 260831-CCR-L15 Status-Change Wait Observer

Created with the lifecycle status-change waiting tool: bounded read-only long-poll over the durable
journal whose only wake condition is a meaningful-state change, with typed refusals for wrong
cursor/generation/contract and unreadable or replaced journals.
