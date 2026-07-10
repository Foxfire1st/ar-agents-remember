# mcp/src/agents_remember/providers/degradation.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/providers/degradation.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `fdff55f2921d7aaa8ba240c11087d02c15a170d7` |
| lastVerifiedCommitDate | 2026-07-10T15:53:23+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md) — `providers/` has no route-local overview of its own; the
`mcp/` package overview is the governing pillar for `providers/`, `mcp/`, and `kernel/`.

## Purpose

`degradation.py` is the 260707-HFX-L7 provider-only degradation protocol: a detector/state
machine over the central provider metrics log (`providers/metrics.py`) plus the response
protocol the developer plan-gate ruling required — durable state-change events, role-addressed
inbox alerts (orchestrator + active managers) with role-appropriate standing instructions, and
the critical-threshold failsafe that stops provider stacks through the always-legal teardown
path. It is deliberately isolated from `serving/app.py` so the sampling loop calls one focused
function (`evaluate_provider_degradation`) after each metrics sample, and is shaped so a later
Sentry-based detector (260703_spotlight-dev-observability) can replace/feed detection without
redoing the response protocol (task doc `08_degradation-protocol-and-system-specialist.json`,
objective).

## Code Commentary

### 260707-HFX2-L17 Current-Role Degradation Recipients

Provider degradation recipient discovery uses `binding_role`, making a hand-opened seat explicitly
attached as orchestrator/manager discoverable and avoiding phantom absence caused by missing
`spawnRole`. The degradation state machine and thresholds are unchanged.

### 260707-HFX2-L12 CS-6 Update

`ProviderDegradationStore` now has a bounded event-log compactor retaining the newest degradation events, and `evaluate_provider_degradation()` compacts after writing a state-change event so the provider alert audit log cannot grow forever.

### Logic

`ProviderDegradationStore` persists two durable artifacts under
`<coordinationRoot>/logs/observer/providers/`: `degradation-state.json` (`ar-provider-degradation-state/v1`,
atomic replace-write) and `degradation-events.jsonl` (`ar-provider-degradation-event/v1`,
append-only) — so the state machine survives a daemon restart (task requirement: "state machine
survives daemon restart (durable events)").

`evaluate_provider_degradation(config, *, stop_provider_stacks=None)` is the entry point `app.py`
calls once per sampling tick. It reads the persisted previous state, reads the recent metrics
tail (`ProviderMetricsStore.read_recent(limit=settings.recent_sample_limit)`), and classifies a
new state via `classify_degradation`. It emits work **only on a state change** (hysteresis
already resolved the transition inside `classify_degradation`) — on a transition it builds a
durable event (`_build_event`: id, `from`/`to`, affected stacks, evidence, and a metrics snapshot
including current/recent-index/tail rows for forensic replay), runs the critical failsafe when
transitioning into `critical` with `fail_safe_enabled`, appends the event, and posts inbox
alerts. It always rewrites the persisted state (even on a same-state tick, to advance
`lastEvaluatedAt`).

`classify_degradation(rows, previous_state, settings, *, now)` is the pure state-machine decision
(the ONE function the failing-first unit tests drive directly). It windows the tail to
`max(degraded_samples, critical_samples, healthy_samples)` rows, collects per-row evidence
(`_row_evidence` dispatches on `row["schema"]`: `PROVIDER_METRICS_SCHEMA` → `_container_evidence`
(memory-ratio + restart-loop signal), `PROVIDER_INDEX_STATE_SCHEMA` → `_index_evidence`
(watcher-lag commit count + sustained-age lag), plus `_probe_evidence` on any row carrying a
latency field), and separately folds in `_setup_failure_streak` (a trailing streak over
`provider-setup-summary`-shaped rows). `_candidate_level` resolves the next state: a "sustained"
evidence reason (age-based lag, setup-failure streak) short-circuits straight to that level
regardless of sample count; otherwise `_threshold_level` requires `critical_samples` /
`degraded_samples` rows at-or-above the corresponding level in the tail before advancing, and
`_has_healthy_tail` requires a full trailing run of `healthy_samples` healthy rows before
recovering — this is the hysteresis the task's failing-first test proves ("threshold crossing
emits exactly one alert per state change"). An **empty metrics log short-circuits straight to
`"healthy"`** with no evidence (`classify_degradation:199-200`) — disclosed as benign today only
because the sampler always writes a metrics row immediately before invoking the evaluator
(decision log 2026-07-08T00:20, item 1); a genuinely missing/truncated log would skip the
`healthySamples` hysteresis gate on an all-clear.

`_post_degradation_alerts(config, event)` posts one `create_operator_inbox_entry(...,
message_kind="degradation-alert")` per recipient for each of `_ALERT_TARGETS` (`orchestrator` →
`ORCHESTRATOR_DEGRADATION_INSTRUCTION` "dispatch system-specialist, read the report, fix or
stop"; `manager` → `MANAGER_DEGRADATION_INSTRUCTION` "no provider starts, no kill authority,
escalate"), addressed via `_role_recipients` (every `running` `harness`-kind catalog entry whose
`spawn_role` matches, else `[None]` — a role-fallback row with no `agentId`, matching
`list_pending`'s role filter). **R2 fix (delivery parity, closes reviewer F1):** for each
recipient the function now runs the same side-effect sequence
`operator_inbox_post_payload`/`deliver_inbox_entry` carries — `store.append(entry)` →
`store.compact(now=...)` → `deliver_inbox_entry(store=store, catalog=catalog, host=host,
paster=paster, entry=entry, submit=True)` — building one `TerminalCatalog`/`TerminalHost`/
`TerminalPaster` per alert batch. Before the fix the function only appended the row directly to
`OperatorInboxStore`, so a running orchestrator/manager session got no stdin paste and only saw
the alert at its next explicit `operator_inbox_poll`; `deliver_inbox_entry` records
`no-hosted-session` for a dead/uncatalogued recipient, so a role-fallback row (no `agentId`)
stays durably pollable rather than erroring.

`_stop_provider_stacks(config)` is the production critical-failsafe stopper:
`provider_watchers_tool(config, action="stop", dry_run=False)` — the always-legal stop path (never
gated by provider launch authority; task requirement: "never violates L1's read-only status
guarantee"). `_run_critical_failsafe(stopper, config)` **(R2 fix, closes reviewer F2)** wraps the
stopper call and captures any exception into `{"ok": False, "errorType": ..., "error": ...}`
instead of letting it propagate — a raising teardown no longer erases the durable event, the
inbox alerts, or the state write; the caller still sees the failure recorded inside
`event["criticalFailsafe"]["result"]`. The failsafe only fires **on the transition into
`critical`**, not on every later tick while already critical (decision log 2026-07-08T00:20, item
1) — this avoids a stop-loop but means a stack that re-enters `critical` without first dropping
below it will not re-trigger a second stop from the same durable event.

### Conventions

Dataclasses (`ProviderDegradationState`, `DegradationEvidence`) mirror the frozen-record style
used across `providers/metrics.py` and `controlplane` records; `to_payload()` methods produce the
camelCase wire shape. `ProviderStopper` is an injectable `Callable[[McpRuntimeConfig], dict]` so
tests substitute a fake stopper without touching `provider_watchers_tool`/docker.

### Invariants And Boundaries

- One durable event per state transition; same-state ticks never re-emit or re-alert (hysteresis
  is resolved before this module sees the transition).
- The critical failsafe runs on transition-into-`critical` only, gated by
  `settings.fail_safe_enabled`; it never runs on a same-state critical tick.
- A raising stopper must never erase the durable event/alerts/state write — capture the failure
  into the event's `criticalFailsafe.result` instead (R2).
- Alert delivery must carry the same side effects `operator_inbox_post_payload` carries
  (durable append, compaction, hosted delivery attempt) — a direct store write alone is a
  fail-open surface for exactly the sessions the protocol exists to reach (R2, reviewer
  candidate catalog CS-6).
- The setup-failure-streak and probe-latency evidence paths are intentionally producer-less this
  iteration: `providers/setup_reporting.py` summaries are not written to `ProviderMetricsStore`
  and nothing writes `probeLatencyMs`/`probeLatencySeconds` rows yet. They are the designated
  Sentry-replaceable seams (decision log 2026-07-08T00:20, item 2) — do not assume these five
  settings keys are live without a producer.
- `classify_degradation` must stay a pure function over `(rows, previous_state, settings, now)` —
  it is the unit under test for the hysteresis/threshold contract independent of the store/inbox
  side effects.

### Todos

- Wire a producer for `provider-setup-summary` rows and probe-latency rows into
  `ProviderMetricsStore` (or replace both with Sentry-sourced rows) so those two evidence paths
  stop being inert.
- Add a test that drives the failsafe through the real `provider_watchers_tool(action="stop",
  dry_run=False)` line instead of a stubbed callable (reviewer F3, accepted-open, optional).

## Docs References

The developer plan-gate ruling (folded into the task doc's `objective` and `decisions[]`) is the
authoritative design source for this protocol; it is a task artifact, not published product
documentation, so it is cited as a repo-internal reference below rather than here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/product documentation governs this protocol; it is a repository-internal doctrine and detector. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The developer plan-gate ruling defining the detector/response protocol, the providers-only scope, and the Sentry-replaceable seam requirement this module is shaped around. | objective; decisions[] | [08_degradation-protocol-and-system-specialist.json](ar-coordination/tasks/agents-remember/260707_hotfix-orchestration-stack/08_degradation-protocol-and-system-specialist.json) |
| The central provider metrics store this detector reads (`PROVIDER_METRICS_SCHEMA`, `PROVIDER_INDEX_STATE_SCHEMA`, container/index-state row shapes). | whole module | [metrics.py](metrics.py) |
| The always-legal provider stop path the critical failsafe calls; never gated by provider launch authority (containment R1). | action="stop" | [provider_tools.py](../controllers/provider_tools.py) |
| The inbox record schema (`system-specialist` `AgentRole`, `degradation-alert` `InboxMessageKind`) this module posts against. | L19-L33 | [operator_inbox_records.py](../controlplane/operator_inbox_records.py) |
| The store this module appends/compacts durable inbox rows through. | whole module | [operator_inbox_store.py](../controlplane/operator_inbox_store.py) |
| The hosted-session delivery helper the R2 fix now calls per alert row for parity with `operator_inbox_post_payload`. | whole module | [inbox_delivery.py](../serving/inbox_delivery.py) |
| The terminal catalog this module reads to resolve running orchestrator/manager sessions by current binding role. | whole module | [terminal_catalog.py](../serving/terminal_catalog.py) |
| `providerDegradation` settings this module consumes (thresholds, `fail_safe_enabled`, `recent_sample_limit`). | whole module | [../mcp/provider_degradation_settings.py](../mcp/provider_degradation_settings.py.md) |
| The serving sampling loop that invokes `evaluate_provider_degradation` once per tick after recording a metrics sample. | L455-L458 (app.py) | [app.py](../serving/app.py.md) |
| Failing-first tests pinning hysteresis, inbox delivery parity, and failsafe-stop-failure durability. | whole module | [../../../tests/test_provider_degradation.py](../../../tests/test_provider_degradation.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This protocol is providers-only this iteration; Sentry integration is a future detection source in a separate task (`260703_spotlight-dev-observability`), not yet a cross-repo/cross-system boundary this module touches. | n/a | n/a |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: switched live orchestrator/manager recipient discovery
  to binding identity; no route-level degradation-protocol change.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 curator memory pass: created after the builder R1 pass
  plus the R2 manager-recovery fix round (hosted-delivery parity closing reviewer F1, failsafe
  stop-failure capture closing F2) and the R2 delta-verify PASS. Verification metadata pinned
  until closeout stamps the HFX-L7 commit.
