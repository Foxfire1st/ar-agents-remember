# mcp/tests/test_l23_notifier_batch_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l23_notifier_batch_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate |  2026-08-12T17:53:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This focused regression suite proves batched notifier expiry preparation fails closed when durable rows cannot be structurally addressed to their current task owner.

## Code Commentary

### Logic

The parameterized test builds findings with absent sources, missing rows, owner mismatches, and unavailable structural addresses, then verifies no ambiguous batch transition is emitted.

### Conventions

Minimal typed fixtures isolate the structural-address decision from unrelated notifier behavior.

### Invariants And Boundaries

- An unaddressable row is never guessed or sent to a stale runtime identity.
- Batch expiry remains tied to canonical task topology and owner role.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this internal control-plane regression.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is needed for the repository-owned addressing rule. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| All unaddressable batched-expiry cases fail closed. | `test_batched_expiry_preparation_fails_closed_on_unaddressable_rows` | mcp/tests/test_l23_notifier_batch_edges.py:25-68 |

## Cross-Repo References

No cross-repository boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| The regression uses local control-plane records and task topology only. | `_finding`; `test_batched_expiry_preparation_fails_closed_on_unaddressable_rows` | mcp/tests/test_l23_notifier_batch_edges.py:8-68 |

## Update History

- 2026-08-12T15:19+02:00 — Created for L23 notifier batch addressing edge coverage; verification provenance remains closeout-owned.
