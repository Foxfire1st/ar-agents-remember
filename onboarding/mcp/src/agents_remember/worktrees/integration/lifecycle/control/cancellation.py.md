# mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:27+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../../overview.md` |

## Governing Overview

[worktree integration overview](../../overview.md)

## Purpose

Owns the mutating cancellation transaction for one durable lifecycle generation. It proves and
terminates retained worker authority, publishes the cancelled journal outcome, and—for closeout or
direct landing—atomically returns the claimed door to a new waiting generation.

## Code Commentary

### Logic

`cancel_operation` first handles already-terminal cases, then terminates the worker, proves the Git
state is cancellable, and publishes the result. Closeout/direct-landing cancellation re-reads the
configured contract under the task-publication lock, verifies the exact claimed door owner, records
write-ahead door intent in the journal, and completes the successor publication. Integration
cancellation also completes any admitted organizational repair. Worker authority is not released
until exit evidence is durable.

### Conventions

Cancellation is same-generation recovery, not deletion. Dry runs project the legal result without
publishing journal, door, worker, or organizational mutations. Typed `LifecycleControlError`
results carry the task-addressed next action when exact authority cannot be proven.

### Invariants And Boundaries

- A closeout/direct-landing generation may publish a successor only while it owns the exact claimed
  door generation and operation key.
- Worker PID authority remains retained until bounded exit proof exists; ambiguous termination is
  actionable state, not permission to continue.
- Completed generations cannot be rewritten as cancelled; retire or supersede owns that decision.
- Queue state cannot substitute for the journal, configured contract, door claim, or Git evidence.
- Cancellation never edits task planning as a substitute for lifecycle repair.

### Todos

None recorded.

## Docs References

No configured external Domain Documentation source governs this repository-internal transaction.

## Repo-Internal References

The source defines the complete cancellation mutation boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Cancellation orders terminal handling, worker exit, Git proof, journal publication, and projection. | `cancel_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py:67-97 |
| Terminal cancellation is idempotent while a completed generation refuses cancellation. | `_terminal_cancel_projection` | mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py:100-133 |
| Closeout/direct-landing cancellation publishes a waiting successor only under the exact claimed owner. | `_publish_cancelled_outcome`; `_require_cancelled_door_owner` | mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py:136-217 |
| Worker authority is released only after bounded termination evidence proves exit. | `_terminate_worker` | mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py:262-302 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: created for the extracted cancellation transaction and verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this provenance does not certify the red Dagger gate.
