# mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py

## Governing Overview

[Lifecycle operation integration overview](../overview.md)

## Purpose

Publishes cancellation for an admitted direct-landing generation after checking its retained closing receipt and exact Git evidence.

## Code Commentary

### Logic

The public control owner admits the addressed direct generation. The helper checks receipt readability, proves that the generation published no Git output, records its cancelled outcome and settles the direct closing. Its retained door and organizational-repair branches handle their matching stored evidence shapes.

**A cancelled direct landing restores the history file it closed (MIK-R09, leaf 260928-MIK-L09; review R1 F3, R2-5).** A direct landing on converted memory closes the leaf's history file before its journal generation exists and keeps that closing in a per-generation receipt (`worktrees/knowledge_gate.keep_direct_closing`). For a `direct-landing` record, `cancel_operation` now:

- first runs `_require_readable_direct_closings`, before Git cancellability proof or cancellation publication: an unreadable or malformed receipt raises `LifecycleControlError` `direct-landing-closing-receipt-unreadable` (next action `developer-decision`), naming the file and how to clear it (`_closing_refusal`), so the closing is never silently lost;
- after the cancelled outcome is published, runs `_restore_direct_closing`, which settles the receipts with this generation as `cancelled` (`settle_direct_closing`): the file is restored to its previous bytes only while it is still exactly what the closing wrote, so a later edit is never overwritten;
- does the same on a repeated cancel of an already-cancelled generation (`_terminal_cancel_projection`, not on a dry run).

Cancellation requires proof that this generation published no Git output before it restores the closing. The receipt helpers act only on direct-landing records.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Cancellation is journaled and generation-specific. Ambiguous or proven commit output requires recovery in the retained generation.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- A cancelled direct landing never leaves the leaf's history file closed by a commit that did not happen, and never
  overwrites a later edit (MIK-R09). Proved by `test_cancelling_the_generation_restores_the_file_it_closed_but_never_a_later_edit`
  and `test_an_unreadable_closing_receipt_is_a_named_refusal_at_apply_and_at_cancel` (the named refusal occurs before Git cancellability proof).

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.


- Cancellation checks the kept receipt before proving no Git output and publishing the cancelled generation. [1]


### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.


- Cancellation checks the kept receipt before proving no Git output and publishing the cancelled generation. [2]

- A direct landing's kept closing: checked before anything moves, restored once cancelled (MIK-R09). [3]

- A repeated cancel restores too. [4]

- The cancel restores the file but never a later edit. [5]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.


- Cancellation checks the kept receipt before proving no Git output and publishing the cancelled generation. [6]
