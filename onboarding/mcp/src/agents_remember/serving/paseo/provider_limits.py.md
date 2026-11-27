# mcp/src/agents_remember/serving/paseo/provider_limits.py

## Governing Overview

[Serving overview](../overview.md)

## Purpose

The product's one judgement and single lock-holding writer of `provider-limits.json` and its sibling sidecar `provider-limit-suppressions.json`, beside `role-agents.json`.

## Code Commentary

A seat is limited, and until when, by Paseo's usage report for that seat and by nothing else: no chat text, no error string, no turn failure kind. This module judges one read and keeps one fact per report id, which every reader of the file then reads.

The judgement is conservative. A fact is set only by a successful report and an `unavailable` read never clears one; the one exception is Paseo 0.16.2's `lastSuccessful`. An `error` entry can carry the login's latest available report, which the product judges with its own fetch time. A report holds work only on an exhausted account-wide window with a future reset, and an enabled extra usage or a positive credits balance releases the seat.

`provider-limits.json` remains strictly `ar-provider-limits/v1` (zero unknown keys for mixed-version `extra="forbid"` readers). Per-window `recordedAt` timestamps and active window-scoped suppressions `(reportId, windowId, resetsAt)` are stored in the sibling `provider-limit-suppressions.json` sidecar (schema and pure helpers in `provider_limit_suppressions.py`). `_commit_pair_locked` writes both files atomically under `provider-limits.lock`, restoring the prior sidecar bytes (or unlinking a newly created sidecar) if `_write_limits` raises so the pair updates all-or-nothing. Drops are part of the same write: an entry whose `until` has passed, and an agent that left the role record, are not carried forward. Where the settings name no Paseo runtime, nothing is read or written.

Every limit write (`record_usage_reads`, `_periodic_update`, and `_apply_suppressions_locked`) projects reports through `project_reports_with_suppressions`: suppressed exhausted windows are filtered out, `report.until` is recomputed to `max(remaining.resetsAt)` on multi-window reports, and a report with no remaining unsuppressed windows is dropped while `_updated_clear_markers` stamps `clearedSeats` under the same lock. `record_usage_reads` preserves existing `recordedAt` across re-reads via `update_sidecar_for_usage_reads` and prunes expired sidecar entries.

A live report is read again when five minutes have passed since its observation or its last recorded attempt. `claim_due_reports` records the attempt under the file lock before the host call, so one claimed report survives a fresh snapshot and a failed read does not postpone the next recheck; `_periodic_update` also projects active suppressions, prunes expired sidecar entries (including sidecar pruning in its change check), drops expired or fully suppressed reports, computes `_updated_clear_markers` so a dropped live suppressed report emits `clearedSeats`, and prunes departed agent mappings with the same write.

An early release is written as a `clearedSeats` entry: the seat, the moment the last live report that held it left the file, and that report's old deadline. The marker stays while the seat is in the role record, while the old deadline plus sixty seconds has not passed, and while no limit holds the seat again; the plugin reads it to release a pending resume or parent flush without waiting for that deadline.

`suppress_provider_limits_for_live_tool_call` performs automatic window-scoped suppression for a bound MCP seat: it pre-checks lock-free, re-verifies under `provider-limits.lock`, and suppresses mapped live windows only when `_proven_active_turn_started_at` reads a complete `host-activity.json` showing the seat in `"in-turn"` or `"permission"` with `eventAt` strictly greater than the window's explicit `recordedAt` in the sidecar (failing closed on missing/idle/incomplete activity, `eventAt <= recordedAt`, or legacy records without `recordedAt`). `provider_limits_status`, `suppress_provider_limit_windows`, and `unsuppress_provider_limit_windows` own the operator CLI status read and lock-serialized suppression mutations.

## Evidence

- An error entry can carry the newest available report. The judgment uses that report and its recorded fetch time. [1]

- One due attempt is claimed under the file lock before the read, a fresh snapshot keeps the claim, and `_periodic_update` prunes expired sidecar entries and computes `_updated_clear_markers` when dropping live suppressed reports. [2]
- An early clear names the seat and the old deadline, and is kept only while the seat remains eligible and no limit returns. [3]
- `_commit_pair_locked` commits sidecar and `provider-limits.json` atomically under `provider-limits.lock` and rolls back the sidecar if `_write_limits` raises. [4]
- `suppress_provider_limits_for_live_tool_call` enforces the causal `host-activity.json` turn-start guard (`in-turn`/`permission`, `eventAt > recordedAt`) lock-free and under lock before committing auto-suppressions. [5]
- `provider_limits_status`, `suppress_provider_limit_windows`, and `unsuppress_provider_limit_windows` serve operator status and lock-serialized suppression overrides. [6]
