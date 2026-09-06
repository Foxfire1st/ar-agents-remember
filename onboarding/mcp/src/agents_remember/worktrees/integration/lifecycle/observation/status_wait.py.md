# `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py`

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | `../overview.md` |

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

## Docs References

No configured external Domain Documentation source governs this observer.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this wait observer. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wait loop and its poll clock. | `wait_for_lifecycle_change`; `LifecycleWaitClock` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:63-148 |
| Typed cursor validation and mismatch decisions. | `validate_wait_cursor`; `_cursor_wait_decision` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:87-103; mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:170-201 |
| Archived-predecessor successor proof. | `_archived_successor_fingerprint` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:249-269 |
| The shared outcome vocabulary. | `LifecycleWaitOutcome` | mcp/src/agents_remember/models/lifecycles/operation_wait.py:14-25 |
| The exact record cursor the waiter compares. | `meaningfulRevision` | mcp/src/agents_remember/models/lifecycles/operation.py:364-364 |
| The application wait controller using this loop. | `worktree_status_wait_tool` | mcp/src/agents_remember/application/lifecycle/lifecycle_status_wait.py:81-111 |

## Cross-Repo References

No cross-repository boundary is crossed by this observer.

| Finding | Anchor | Source |
| --- | --- | --- |
| The wait loop observes one repository's lifecycle journal. | `wait_for_lifecycle_change` | mcp/src/agents_remember/worktrees/integration/lifecycle/observation/status_wait.py:105-148 |

## 260831-CCR-L15 Status-Change Wait Observer

Created with the lifecycle status-change waiting tool: bounded read-only long-poll over the durable
journal whose only wake condition is a meaningful-state change, with typed refusals for wrong
cursor/generation/contract and unreadable or replaced journals.

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `meaningfulRevision` repointed to mcp/src/agents_remember/models/lifecycles/operation.py:364-364. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `LifecycleWaitOutcome` repointed to mcp/src/agents_remember/models/lifecycles/operation_wait.py:14-25. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): created
  this card for the new read-only status-change wait observer.
