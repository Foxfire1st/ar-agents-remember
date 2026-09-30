# mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash |  `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate |  2026-09-30T21:09:40+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `cancel_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py:74-106 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `cancel_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py:74-106 |
| A direct landing's kept closing: checked before anything moves, restored once cancelled (MIK-R09). | `_restore_direct_closing`; `_require_readable_direct_closings`; `_closing_refusal` | mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py:147-176 |
| A repeated cancel restores too. | `_terminal_cancel_projection` | mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py:109-144 |
| The cancel restores the file but never a later edit. | `test_cancelling_the_generation_restores_the_file_it_closed_but_never_a_later_edit` | mcp/tests/test_knowledge_gate_routes.py:448-469 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `cancel_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py:74-106 |

## Update History

- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** Logic and Invariants record the direct-landing hook of review R1 F3 and R2-5: for a `direct-landing` record, cancellation refuses first on an unreadable closing receipt (`direct-landing-closing-receipt-unreadable`, before anything is terminated or published) and, once the cancellation is published (or on a repeated cancel), restores the history file the landing closed, never over a later edit. Three rows added. The whole-function rows were normalised by the installed fixer.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py` changed since
  the recorded verification commit. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the door is read live and the task-publication lock is gone).
  Re-read the card: it names neither construct and its whole-file range still matches. No wording
  changed; verification metadata remains closeout-owned.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
