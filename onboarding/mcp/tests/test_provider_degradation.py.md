# mcp/tests/test_provider_degradation.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_provider_degradation.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T01:00+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_provider_degradation.py` is the failing-first suite for the 260707-HFX-L7 provider
degradation protocol: the pure classifier's hysteresis contract, and the full evaluator's
durable-event/inbox-alert/critical-failsafe behavior end to end against a real temp coordination
root.

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

`ProviderDegradationEvaluatorTests` drives `evaluate_provider_degradation` against a real
`load_test_config`-built `McpRuntimeConfig` and a temp coordination root:
- `test_critical_transition_records_event_inbox_and_failsafe_once` seeds two `running`
  `harness`-kind catalog entries (`spawn_role="orchestrator"`/`"manager"`), records two
  memory-pressure samples crossing `critical_samples=2`, patches `deliver_inbox_entry` to capture
  delivery attempts, and asserts: one durable event row with `to="critical"` and a
  `criticalFailsafe.action == "provider_watchers stop"`; the injected `stop_provider_stacks` fake
  called exactly once (not on the second same-state evaluation); the persisted state file matches;
  exactly one `degradation-alert` inbox row per catalogued session (`orchestrator-1`/`manager-1`);
  and — the R2 fix this test was extended to cover — exactly 2 delivery attempts, one per
  recipient, proving the hosted-delivery side effect actually runs (closes reviewer F1).
- `test_critical_stop_failure_still_records_event_inbox_and_state` (R2, new) makes the injected
  stopper raise `RuntimeError("docker stop failed")` and asserts the event, inbox rows, and
  persisted `critical` state all still land, with `criticalFailsafe.result` carrying
  `{"ok": False, "errorType": "RuntimeError", "error": "...docker stop failed..."}` — proving the
  degradation record survives a teardown failure (closes reviewer F2).
- `test_recovery_transition_survives_restart_and_posts_role_addressed_all_clear` drives a
  degraded→healthy round trip with no catalogued sessions (role-fallback `agentId=None` rows) and
  asserts two ordered event rows (`degraded` then `healthy`) plus role-addressed all-clear inbox
  rows for both `orchestrator` and `manager`.

### Conventions

Real temp-rooted `McpRuntimeConfig` via `load_test_config`/`config_payload` (writes an actual
`.codex/mcp/settings.json` and calls `load_config`), matching the test-writing style in
`test_config.py`; no mocking of the config layer. `record_memory_sample` and `read_event_rows` are
small local helpers building/reading the real `ProviderMetricsStore`/`ProviderDegradationStore`
files. `unittest.mock.patch` is used only for the `deliver_inbox_entry` delivery-capture seam, not
for the store/config layers.

### Invariants And Boundaries

- The classifier tests must stay side-effect-free (no store/inbox I/O) so they pin the pure
  hysteresis contract independent of the evaluator's durability/delivery machinery.
- The evaluator tests must prove durability (event + state survive) even when the injected
  stopper or the delivery seam misbehaves — that is the point of the R2 additions.
- Delivery-attempt assertions must count exactly one per role-addressed recipient, not per alert
  target, so a delivery-parity regression (queue-only alerts) fails loudly here first.

### Todos

- A test driving the failsafe through the real `_stop_provider_stacks` → `provider_watchers_tool`
  line (rather than the injected stub) remains open per reviewer F3 (accepted, optional).

## Docs References

No external documentation governs this suite; it is a repository-internal failing-first test
file for a repository-internal protocol.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking; the protocol is repo-internal doctrine. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The detector and evaluator under test. | `classify_degradation`; `evaluate_provider_degradation` | mcp/src/agents_remember/providers/degradation.py:268-323; mcp/src/agents_remember/providers/degradation.py:326-345 |
| The settings dataclass this suite constructs directly to tune thresholds per test. | `ProviderDegradationSettings` | mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py:36-55 |
| The metrics store/schema rows the classifier tests construct as fixtures. | `PROVIDER_INDEX_STATE_SCHEMA`; `ContainerSample`; `MetricsSnapshot` | mcp/src/agents_remember/providers/metrics.py:63-63; mcp/src/agents_remember/providers/metrics.py:146-157; mcp/src/agents_remember/providers/metrics.py:160-176 |
| The terminal catalog entries seeded as alert recipients. | "def from_json(cls" | mcp/src/agents_remember/models/terminal_catalog.py:80-510 |
| The operator inbox store read back to assert alert rows/roles/responses. | `OperatorInboxStore` | mcp/src/agents_remember/controlplane/operator_inbox_store.py:53-251 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Test-only, repository-local fixtures and imports. | n/a | n/a |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 1 repeated path:start-end Citation objects from 1 same-claim citation group(s) at card line(s) 101; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T22:20+02:00 — 260731-EFA-L6 W2-B05 curator: curated 3 repo-internal citation rows; deleted 1 unsupported external task-requirement row under the 2026-08-02 14:10 ruling; scoped citation check now passes.
- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 touched this suite only through the
  `deliver_inbox_entry` parameter-object change plus `ruff format` reflow. That function now takes
  an `InboxDeliveryLog` (store, entry, timestamp, redelivery floor) as its first positional
  argument, so the local `deliver_entry` capture double became `def deliver_entry(log, **kwargs)`
  recording `{"log": log, **kwargs}` and returning `log.entry`, and the recipient assertion reads
  `attempt["log"].entry.agentId` instead of `attempt["entry"].agentId`. Three assertions were
  re-wrapped for line length with no change of operand. Checked every claim this card makes about
  that test: the patch target is still `agents_remember.providers.degradation.deliver_inbox_entry`,
  the double is still the only mocked seam, the attempt count is still exactly 2, and the asserted
  recipient set is still `{"orchestrator-1", "manager-1"}` — so the delivery-parity invariant this
  card calls out still fails loudly here first. The card names neither the double's signature nor
  the former `entry=` keyword, and it carries no line citations, so nothing needed re-anchoring.

- 2026-07-08T01:00+02:00 — 260707-HFX-L7 curator memory pass: created after the builder R1 pass
  (hysteresis/streak/index-lag classifier tests, the critical-transition evaluator test) plus the
  R2 manager-recovery additions (delivery-attempt assertions closing reviewer F1, the stop-failure
  durability test closing F2). Verification metadata pinned until closeout stamps the HFX-L7
  commit.
