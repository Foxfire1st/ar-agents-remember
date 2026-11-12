# mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py

## Governing Overview

[Lifecycle operation integration overview](../overview.md)

## Purpose

Executes cancellation for one durable lifecycle generation, including worker termination and organizational repair.

## Code Commentary

### Logic

It validates cancel authority, requests/observes worker termination, resolves door/queue ownership, publishes cancelled outcomes, and completes or records repair failure.

**A cancelled direct landing restores the history file it closed (MIK-R09, leaf 260928-MIK-L09; review R1 F3, R2-5).** A direct landing on converted memory closes the leaf's history file before its journal generation exists and keeps that closing in a per-generation receipt (`worktrees/knowledge_gate.keep_direct_closing`). For a `direct-landing` record, `cancel_operation` now:

- first runs `_require_readable_direct_closings`, before anything is terminated or published: an unreadable or malformed receipt raises `LifecycleControlError` `direct-landing-closing-receipt-unreadable` (next action `developer-decision`), naming the file and how to clear it (`_closing_refusal`), so the closing is never silently lost;
- after the cancelled outcome is published, runs `_restore_direct_closing`, which settles the receipts with this generation as `cancelled` (`settle_direct_closing`): the file is restored to its previous bytes only while it is still exactly what the closing wrote, so a later edit is never overwritten;
- does the same on a repeated cancel of an already-cancelled generation (`_terminal_cancel_projection`, not on a dry run).

Cancellation needs its no-output proof, so no memory commit exists when the file is restored. Other operation kinds are untouched.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Cancellation is journaled and generation-specific; it cannot erase unresolved worker, mutation, publication, or organizational-repair evidence.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- A cancelled direct landing never leaves the leaf's history file closed by a commit that did not happen, and never
  overwrites a later edit (MIK-R09). Proved by `test_cancelling_the_generation_restores_the_file_it_closed_but_never_a_later_edit`
  and `test_an_unreadable_closing_receipt_is_a_named_refusal_at_apply_and_at_cancel` (the worker is never terminated).

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The module's concrete API, control flow, and validation boundary are implemented here. [2]
- A direct landing's kept closing: checked before anything moves, restored once cancelled (MIK-R09). [3]
- A repeated cancel restores too. [4]
- The cancel restores the file but never a later edit. [5]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [6]
