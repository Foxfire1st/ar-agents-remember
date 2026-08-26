# mcp/tests/test_structural_dispatch_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_structural_dispatch_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T16:03+02:00 |
| lastVerifiedCommitHash |  `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate |  2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces the durable commit boundary and retry behavior of the canonical spawn-and-pinned-brief
transaction.

## Code Commentary

### Logic

The cohort distinguishes a failed inbox append from failures after append. It proves that a
pre-append failure retires the positively unbriefed generation; compaction failure after append
preserves and reuses the durably briefed generation; receipt-binding uncertainty refuses without
rollback and repairs on retry; and a terminally failed brief permits replacement. Additional edges force missing or already-terminal
rollback targets, two changing generations, failed retirement, receipt-repair disappearance, and
legacy occupancy so each ambiguous state refuses rather than publishing or cleaning up again.

### Conventions

Tests patch the actual production owner seam (`OperatorInboxStore`, `DispatchBriefReceiptStore`, or `TerminalCatalog`) and inspect
real temporary catalog/inbox state, rather than fabricating only a returned status.

### Invariants And Boundaries

- Inbox append is the durable commit point.
- Unknown or post-append state never authorizes destructive rollback.
- Retry converges on the original occupant when its brief is viable.
- Only positively terminal/unbriefed evidence permits retirement and a new generation.
- One call observes at most two generations and never publishes a third.
- Receipt repair that loses its occupant and failed retirement both refuse reconciliation.

### Todos

None.

## Docs References

No Domain Documentation source is configured; this is repository-owned recovery proof.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A failed append retires only the proven unbriefed generation. | `test_pre_append_failure_retires_only_the_proven_unbriefed_generation` | mcp/tests/test_structural_dispatch_recovery.py:77-90 |
| Post-append compaction failure preserves the brief and converges on retry. | `test_post_append_compaction_failure_keeps_and_reuses_the_briefed_generation` | mcp/tests/test_structural_dispatch_recovery.py:92-111 |
| Receipt-write uncertainty refuses without rollback and the next call repairs it. | `test_receipt_bind_failure_is_unknown_not_rollback_and_retry_repairs_it` | mcp/tests/test_structural_dispatch_recovery.py:113-133 |
| Receipt and rollback edge branches are explicit and non-destructive when evidence disappears. | `test_receipt_and_unbriefed_rollback_edges_are_explicit`; `test_receipt_repair_disappearance_and_legacy_occupancy_refuse` | mcp/tests/test_structural_dispatch_recovery.py:140-183; mcp/tests/test_structural_dispatch_recovery.py:237-278 |
| Two changed generations and failed retirement refuse without a third publication. | `test_two_changed_generations_refuse_without_publishing_a_third`; `test_failed_generation_that_cannot_retire_is_a_reconciliation_refusal` | mcp/tests/test_structural_dispatch_recovery.py:186-204; mcp/tests/test_structural_dispatch_recovery.py:207-234 |
| Terminal failed-brief evidence permits retirement and replacement. | `test_terminal_failed_brief_retires_and_replaces_that_generation` | mcp/tests/test_structural_dispatch_recovery.py:281-303 |

## Cross-Repo References

No cross-repository dependency governs this test module.

## Update History

- 2026-08-26T16:03+02:00 — Post-failure repair: added the bounded second-generation refusal, failed
  retirement, receipt-repair disappearance, legacy occupancy, and direct rollback edge matrix. No
  certifying test execution is claimed.


- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: created for commit-point-aware dispatch recovery
  proof. Verification remains closeout-owned.
