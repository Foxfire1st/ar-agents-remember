# mcp/tests/test_structural_dispatch_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_structural_dispatch_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash |  `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Forces spawn-and-pinned-brief recovery at durable boundaries. Failure before append retires only a proven unbriefed generation; post-append compaction failure preserves/reuses the briefed generation; receipt-binding ambiguity is reconciled rather than rolled back. A reviewer from another parent is neither reused nor retired, and terminal failed briefing replaces only that exact generation.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pre append failure retires only the proven unbriefed generation | `test_pre_append_failure_retires_only_the_proven_unbriefed_generation` | mcp/tests/test_structural_dispatch_recovery.py:82-95 |
| Post append compaction failure keeps and reuses the briefed generation | `test_post_append_compaction_failure_keeps_and_reuses_the_briefed_generation` | mcp/tests/test_structural_dispatch_recovery.py:97-116 |
| Receipt bind failure is unknown not rollback and retry repairs it | `test_receipt_bind_failure_is_unknown_not_rollback_and_retry_repairs_it` | mcp/tests/test_structural_dispatch_recovery.py:118-138 |
| Live reviewer from another parent is not reused or retired | `test_live_reviewer_from_another_parent_is_not_reused_or_retired` | mcp/tests/test_structural_dispatch_recovery.py:140-171 |
| Terminal failed brief retires and replaces that generation | `test_terminal_failed_brief_retires_and_replaces_that_generation` | mcp/tests/test_structural_dispatch_recovery.py:173-195 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-31T13:42+02:00 — A005 closeout repair added direct coverage for the sole unstamped
  legacy leaf-reviewer parent meaning exposed by the changed-unit gate.

- 2026-08-31T09:02+02:00 — 260821-ARSPAWN-L5 A005 citation reconciliation refreshed
  source ranges after the reviewed recovery suite moved; no semantic onboarding claim changed.
  Verification remains closeout-owned.

- 2026-08-26T16:03+02:00 — Post-failure repair: added the bounded second-generation refusal, failed
  retirement, receipt-repair disappearance, legacy occupancy, and direct rollback edge matrix. No
  certifying test execution is claimed.


- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: created for commit-point-aware dispatch recovery
  proof. Verification remains closeout-owned.
