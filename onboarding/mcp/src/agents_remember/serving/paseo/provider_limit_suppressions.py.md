# mcp/src/agents_remember/serving/paseo/provider_limit_suppressions.py

## Governing Overview

[Serving overview](../overview.md)

## Purpose

Defines the sibling sidecar schema (`ar-provider-limit-suppressions/v1`) and pure window-projection, expiry-pruning, causal-selection, and operator-command helpers for window-scoped provider-limit suppressions. Keeps `provider-limits.json` strictly `ar-provider-limits/v1` for mixed-version `extra="forbid"` readers while owning no disk writes.

## Code Commentary

`ProviderLimitSuppressions` stores two immutable lists beside `provider-limits.json` in `provider-limit-suppressions.json`:

- `recordedWindows` (`RecordedLimitWindow`): records when AR first observed each active exhausted `(reportId, windowId, resetsAt)` window (`recordedAt`), using UTC-normalized `window_key(report_id, window_id, resets_at)` tuples.
- `suppressedWindows` (`SuppressedLimitWindow`): records active suppressions with `source` (`"auto-tool-call"` or `"operator"`), `suppressedAt`, and optional causal evidence (`agentId`, `turnStartedAt`, `callAt`, `recordedAt`).

`read_provider_limit_suppressions` reads the sidecar and returns `EMPTY_PROVIDER_LIMIT_SUPPRESSIONS` on `OSError` or `ValidationError` so a missing legacy sidecar never hides a live v1 limit.

`project_reports_with_suppressions` is the single shared window-filtering helper used on every limit write. It removes any window with `resetsAt <= now` or whose UTC-normalized key is in `live_suppressed_keys(sidecar, now)`, recomputes `report.until` to `max(window.resetsAt for window in remaining)` when a multi-window report still has unsuppressed windows, and drops the report when no unsuppressed exhausted windows remain. Reports with an empty `windows` tuple pass through unchanged until `report.until <= now`.

`update_sidecar_for_usage_reads` preserves existing `recordedAt` timestamps across usage re-reads so 5-minute rechecks and sibling turn ends never bump `recordedAt` forward, stamps newly judged windows at `now`, and drops expired entries (`resetsAt <= now`). `prune_sidecar` drops expired entries and stale `recordedWindows` no longer present in live reports, returning the identical `sidecar` object when unchanged so quiet periodic ticks avoid disk writes.

`auto_suppression_candidates` enforces the causal turn-start guard over a bound seat's mapped reports: it selects only live unsuppressed windows whose explicit `recordedAt` is strictly less than `turn_started_at` (`turn_started_at > recorded_at`), failing closed whenever `recordedAt is None` (legacy v1 records without a sidecar) or `turn_started_at <= recorded_at`.

Operator CLI helpers (`validate_selector`, `build_status_payload`, `select_operator_suppressions`, `partition_suppressions_for_unsuppress`, `missing_suppression_refusal`, `suppress_success_result`, `unsuppress_success_result`) resolve `--report [--window]` or `--agent [--window]` selectors into typed `ProviderLimitCommandResult` payloads (exit codes `0` or `2`), refusing missing/conflicting selectors, non-live reports/windows, multi-window `--report` calls missing `--window`, and unmatched `unsuppress` targets by name.

## Relationships

- Imported by `mcp/src/agents_remember/serving/paseo/provider_limits.py`, which remains the sole lock-holding writer of both `provider-limits.json` and `provider-limit-suppressions.json` under `provider-limits.lock`.
- `SuppressionSelector` and `ProviderLimitCommandResult` cross the CLI adapter boundary into `mcp/src/agents_remember/cli/provider_limit_hold.py`.
- Consumes v1 limit models (`ProviderLimits`, `ProviderLimitReport`, `ProviderLimitWindow`) from `mcp/src/agents_remember/observer/provider_limits.py` without modifying their `extra="forbid"` schema.

## Evidence

- Defines the `ar-provider-limit-suppressions/v1` sidecar models (`RecordedLimitWindow`, `SuppressedLimitWindow`, `ProviderLimitSuppressions`) with `extra="forbid"`. [1]
- Shared projection helper filters suppressed windows by `(report_id, window_id, resetsAt)`, recomputes `report.until`, and drops empty reports. [2]
- Preserves existing `recordedAt` across re-reads, stamps newly judged windows, and prunes expired sidecar entries without mutating unchanged snapshots. [3]
- Selects automatic suppression candidates only when explicit `recordedAt` strictly precedes `turn_started_at`, failing closed on legacy or non-later timestamps. [4]
- Resolves operator `status`, `suppress`, and `unsuppress` selectors and produces exit-2 named refusals for non-live reports/windows or omitted multi-window selectors. [5]
