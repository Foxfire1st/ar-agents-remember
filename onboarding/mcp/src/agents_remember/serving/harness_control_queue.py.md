# mcp/src/agents_remember/serving/harness_control_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:00+02:00 |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661` |
| lastVerifiedCommitDate | 2026-07-14T10:43:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Implements the bridge's bounded ordered command runner and bounded receipt/reconciliation ledger.

## Code Commentary

Terminal and durable messages enter the same queue as whole commands. Submit, respond, reconcile,
resolve, and stop commands are executed by one runner against the single adapter. Unexpected
adapter errors resolve the active future and fail the bridge; runner exit drains remaining commands
with explicit errors. Unsupported submissions use the same reserve/evict limit as supported ones,
while in-flight reservations are protected.

## Invariants And Boundaries

- Queue order is message-level, never keystroke-level.
- A receipt records acceptance, not completion; unknown remains unresolved until reconciliation.
- Ledger and command/subscriber paths are bounded by configured limits.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Queue owner. | [harness_control_bridge.py](harness_control_bridge.py) |
| Submission and reconciliation models. | [harness_control_models.py](harness_control_models.py) |
| Scaling and lifecycle tests. | [test_harness_control.py](../../../tests/test_harness_control.py) |

## Update History

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for ordered command
  execution, stranded-await failure handling, and bounded unsupported receipt retention.
