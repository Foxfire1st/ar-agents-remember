# mcp/tests/test_provider_degradation.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_provider_degradation.py` retains the 260707-HFX-L7 classifier hysteresis and evaluator event/state/critical-failsafe fixtures against a temporary coordination root. R113 removed the terminal recipient catalog, inbox delivery/alerts and role-addressed all-clear assertions; their earlier failing-first/R2 attribution is historical, not current coverage. The injected stopper does not establish real container shutdown or hosted notification.

## Code Commentary

### Logic

`ProviderDegradationClassifierTests` drives `classify_degradation` directly (no store/inbox side
effects):
- `test_hysteresis_requires_sustained_bad_and_sustained_healthy_samples` proves the core
  hysteresis contract the task's failing-first requirement names: one degraded row from healthy
  stays `healthy`; two degraded rows (meeting `degraded_samples=2`) advance to `degraded`; one
  degraded + one healthy row from `degraded` stays `degraded` (recovery needs a full healthy
  run); two healthy rows (meeting `healthy_samples=2`) recover to `healthy`.
- `test_setup_failure_streak_uses_central_metric_rows` proves a trailing streak of
  `provider-setup-summary`-shaped failure rows drives state via `_setup_failure_streak`,
  independent of container/index evidence.
- `test_index_staleness_rows_drive_degraded_and_critical_states` proves `PROVIDER_INDEX_STATE_SCHEMA`
  rows drive both the commit-lag threshold path (`behindFiles` count) and the sustained-age lag
  path (`staleIndex.served` + row age in minutes) to `degraded`/`critical`.

`ProviderDegradationEvaluatorTests` drives `evaluate_provider_degradation` using temporary config/store files and injected stop actions:
- `test_critical_transition_records_event_and_failsafe_once` asserts a critical event and matching state/last-event ID, one injected stop call, and no second same-state event. It has no catalog or delivery-count assertion.
- `test_critical_stop_failure_still_records_event_and_state` makes the stopper raise `RuntimeError("docker stop failed")` and verifies the persisted critical event/state and structured failsafe failure. Its current durability claim concerns the stopper failure, not an inbox/delivery failure.
- `test_recovery_transition_survives_restart` asserts degraded-to-healthy event ordering using `unreachable_stopper`, which raises if the critical branch unexpectedly runs. The current body does not restart the process or assert all-clear recipients; the method name is not additional evidence.
Earlier R2 F1/F2 claims described removed notification assertions; this narrower current inventory does not reopen or regrade those historical CODE findings.

### Conventions

Real temp-rooted `McpRuntimeConfig` via `load_test_config`/`config_payload` (writes an actual
`.codex/mcp/settings.json` and calls `load_config`), matching the test-writing style in
`test_config.py`; no mocking of the config layer. `record_memory_sample` and `read_event_rows` are
small local helpers building/reading the real `ProviderMetricsStore`/`ProviderDegradationStore`
files. The current suite has no delivery mock; injected stop functions isolate the external teardown boundary. These are temporary fixture settings, not permission to mutate real user settings.

### Invariants And Boundaries

- The classifier tests must stay side-effect-free (no store/inbox I/O) so they pin the pure
  hysteresis contract independent of the evaluator's durability/delivery machinery.
- The retained evaluator cases establish event/state persistence with an injected stopper, including a stopper failure. R113's removed notification/delivery seams are not covered by these assertions.
- No fresh execution, live container stop, hosted delivery or whole-candidate acceptance is claimed by this static card reconciliation.

### Todos

The earlier reviewer F3 accepted an optional suggestion for a test through `_stop_provider_stacks` → `provider_watchers_tool` instead of an injected stub. That route is historical: the provider tools were removed, and the current evaluator requires its runtime caller to supply a `ProviderStopper`. The earlier acceptance is preserved as review history, not a current test recipe or a new test obligation. Existing classifier/evaluator safety and injected-stopper limits remain unchanged.

## Evidence

### Docs References

No external documentation governs this suite; it is a repository-internal failing-first test
file for a repository-internal protocol.

No relevant documentation found after checking; the protocol is repo-internal doctrine.

### Repo-Internal References

- The detector and evaluator under test. [1]
- The settings dataclass this suite constructs directly to tune thresholds per test. [2]
- The metrics store/schema rows the classifier tests construct as fixtures. [3]
- The three current evaluator cases pin one-shot injected failsafe/event/state persistence, stop-failure durability, and degraded/healthy event ordering, with no terminal catalog/inbox/delivery assertions. [6]

### Cross-Repo References

No meaningful cross-repo references found.

Test-only, repository-local fixtures and imports.

- The current evaluator requires a supplied ProviderStopper and does not import an agent tool; the retained evaluator fixtures inject that boundary, so the former MCP-tool test route is historical. [7]

## Historical optional F3 suggestion

These former current claims are retained as history, not as instructions or present implementation evidence.

> - A test driving the failsafe through the real `_stop_provider_stacks` → `provider_watchers_tool`
>   line (rather than the injected stub) remains open per reviewer F3 (accepted, optional).
