# mcp/src/agents_remember/providers/degradation.py

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

### 260731-EFA-L5 The Event Log Is On `ar-durable-store/1.0`

`degradation-events.jsonl` had the same shape as the six `controlplane/` logs — an unlocked
`open("a")` append beside a `compact_events` whole-file read-filter-rewrite, and a `.compact.tmp`
name with no pid in it — and it was left off the contract's first pass on the strength of nothing
but its directory.

**It has ONE writer today, and that was refused as an argument.** `evaluate_provider_degradation`
has exactly one production caller, the dashboard's `_metrics_loop`, and it is the only thing that
appends an event, compacts the log or writes the state document. That is the same argument this leaf
already refused for `attention_dismissals.py` and `supervisor_signals.py` — and refused for a
measured reason, since the draft that left those two unlocked on the strength of single-writer
measured 31.45% loss on attention-dismissals. **"Only one process writes this file" is a deployment
fact; the lock is about the file.**

**On the loss numbers: record the direction, not a rate.** This module's docstring states 72.75% /
71.75% / 73.00% at 2 appenders and 800 events; `tests/test_provider_store_durability.py`
re-measured against a `git archive` of the base commit after fixing the harness's scratch directory
and got 3.00-7.50% at the shipped profile and 7.00-7.12% at the same 2×800 shape, and that file
explicitly says the pacing behind the originals was never recorded and the figures should be read as
direction only. **This card asserts no rate.** What is stable: *this store lost records at the base
commit and loses none now* — and the zero is an assertion, not prose. `ProviderStoreDurabilityTests`
pins `lost == 0`, `torn_lines == 0` and `stragglers == []` over `attempted == 200` (the shipped
`STRESS_PROFILE`: 4 appenders × 50) for this store and its sibling, plus `lost == 0` over the forced
single-record window. Zero loss at the 2-appender/800-record shape — four times the volume — is also
reported, but narratively rather than as an assertion.

**Ownership: `PROVIDER_DEGRADATION_OWNERSHIP`**, declared beside the store for the same reason
`providers/metrics.py` declares its own (`durable_store.py`'s register is the contract for the six
control-plane logs, not a directory of every store in the tree; the contract is imported, never
re-implemented). `writers=("dashboard",)`, `compaction_owner="dashboard"`, enforced structurally —
`compact_events` is called from one place, immediately after the append it bounds. It did **not**
earn the operator-inbox's `compaction_owner=None` exception: that store earned `None` because both
processes must physically remove rows, and nothing in the MCP process removes a degradation event or
writes one, so a single owner was available and therefore required.

The single writer is, however, why `check_declared_writer` earns its place here rather than being a
formality: with `writers=("dashboard",)` this is the one store in the provider pair where the check
can actually fire, and it fires the moment the MCP process starts evaluating degradation. It is
**not** why the log is safe — the lock is unconditional.

**What changed in each write:**

- `append_event(event)` stamps `schemaVersion` and appends under the log's lock. The stamp is added
  **here, at the only write**, because that is the only moment the information exists: this log is
  an audit trail kept for a thousand events and nothing reads it back today, so a row written
  without its version could never be told apart from a future one. A reader added later must apply
  `durable_store.schema_version_supported` — unknown major refused, unknown minor accepted, absent
  means 1.0, which is what lets an existing file load unchanged.
- `compact_events(retain_rows=…)` holds the lock across the read, the filter **and** the rewrite.
  Rarity is not serialization: the append that races this rewrite is the one that just caused the
  state change this compaction is bounding, so the window is not merely open — it is the window the
  store spends its whole life in. The reclaim drops rows **by age and never by content** (the lines
  are kept raw), so a row no reader could parse survives here instead of being silently deleted by
  the rewrite.
- `write_state(state)` goes through `rewrite_lines` — pid-scoped temp, fsynced file and directory —
  because `degradation-state.json.tmp` was the second unscoped temp name in this pair, and two
  writers sharing it hand one of them a `FileNotFoundError`.

**Be precise about what the lock does in `write_state`.** This document is not a record log: it is
recomputed in full every evaluation and replaced, so there is no read-modify-write of stored rows
for a lock to make atomic. The lock is **not** claimed to make `read_state` → `write_state` one
transaction — it is not; that span belongs to `evaluate_provider_degradation` and to its single
caller. What it does is serialize two republications and satisfy `rewrite_lines`' refusal to rewrite
a path whose lock the caller is not holding. It is also why this document carries **no**
`schemaVersion`: the stamp is a per-*record* fact and this file holds no records.

### 260731-EFA-L2 Transition Identity And Inbox Objects

**`_DegradationTransition(event_id, previous, state, at)`** is the identity of one degradation
state change; everything else in the emitted event is the *evidence* that justifies it. That split
is the signature: `_build_event(transition, evidence, *, rows, metric_store)`. The emitted event
payload (`schema`, `id`, `at`, `from`, `to`, `affectedStacks`, `evidence`, `metrics`) is unchanged.

`_post_degradation_alerts` builds its inbox rows through the controlplane's parameter objects —
`create_operator_inbox_entry(InboxMessage(ask=…, response=…, message_kind="degradation-alert"),
entry_id=…, now=…, routing=InboxRouting(address=InboxAddress(...)), poster=InboxPoster(...))` —
matching `controlplane/operator_inbox_records.py`'s current API. The posted rows are identical.

### 260707-HFX2-L17 Current-Role Degradation Recipients

Provider degradation recipient discovery uses `binding_role`, making a hand-opened seat explicitly
attached as orchestrator/manager discoverable and avoiding phantom absence caused by missing
`spawnRole`. The degradation state machine and thresholds are unchanged.

### 260707-HFX2-L12 CS-6 Update

`ProviderDegradationStore` now has a bounded event-log compactor retaining the newest degradation events, and `evaluate_provider_degradation()` compacts after writing a state-change event so the provider alert audit log cannot grow forever.

### Logic

`ProviderDegradationStore` persists two durable artifacts under
`<coordinationRoot>/logs/observer/providers/`: `degradation-state.json` (`ar-provider-degradation-state/v1`,
replaced whole) and `degradation-events.jsonl` (`ar-provider-degradation-event/v1`,
append-only) — so the state machine survives a daemon restart (task requirement: "state machine
survives daemon restart (durable events)"). **Since 260731-EFA-L5 both go through
`ar-durable-store/1.0`**: every write holds its own path's lock and uses the contract's pid-scoped,
fsynced `rewrite_lines` rather than a hand-rolled `.tmp` + `os.replace` — see the L5 section above,
including what the lock in `write_state` does and does not promise.

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
`"healthy"`** with no evidence (`classify_degradation:225-226`) — disclosed as benign today only
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

- **Every write to either artifact holds that path's lock, and single-writer is not the reason.**
  The lock is unconditional for the same reason it is on `attention_dismissals.py` and
  `supervisor_signals.py`, which are also single-writer today: one process writing a file is a
  deployment fact, not a structural one, and an unlocked draft of that pair measured 31.45% loss.
- **`compact_events` holds the lock across read, filter and rewrite, and drops rows by age only.**
  The append that races it is the one that caused the state change it is bounding, so rarity is not
  serialization; keeping the lines raw means an unparseable row is retained rather than silently
  deleted by a rewrite.
- **`write_state`'s lock serializes republications; it does not make `read_state` → `write_state` a
  transaction.** That span belongs to `evaluate_provider_degradation` and its single caller. The
  state document holds no records and therefore carries no `schemaVersion`.
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

## Evidence

### Docs References

The developer plan-gate ruling (folded into the task doc's `objective` and `decisions[]`) is the
authoritative design source for this protocol; it is a task artifact, not published product
documentation, so it is cited as a repo-internal reference below rather than here.

No external/product documentation governs this protocol; it is a repository-internal doctrine and detector.

### Repo-Internal References

- The provider-only detector/response entry point implemented by this module. [1]
- The central provider metrics store this detector reads (`PROVIDER_METRICS_SCHEMA`, `PROVIDER_INDEX_STATE_SCHEMA`, container/index-state row shapes). [2]
- The always-legal provider stop path the critical failsafe calls; never gated by provider launch authority (containment R1). [3]
- The critical-failsafe wiring supplies the stop action directly from the dashboard loop. [4]

- The store this module appends/compacts durable inbox rows through. [6]
- The hosted-session delivery helper the R2 fix now calls per alert row for parity with `operator_inbox_post_payload`. [7]
- The terminal catalog this module reads to resolve running orchestrator/manager sessions by current binding role. [8]
- `providerDegradation` settings this module consumes (thresholds, `fail_safe_enabled`, `recent_sample_limit`). [9]
- `_metrics_loop` — the sole production caller: `metrics_store.record`, `evaluate_provider_degradation` and `metrics_store.compact` on one 30s tick. This is why the dashboard is the declared compaction owner of both provider stores, and it is where the ownership is enforced structurally. [10]

- `ar-durable-store/1.0`: `exclusive_access`, `append_line`, `rewrite_lines`, `read_log_text`, `SCHEMA_VERSION`, `schema_version_supported`, and the `StoreOwnership` record `PROVIDER_DEGRADATION_OWNERSHIP` instantiates. Cited by symbol so later additions do not change the claim. [12]
- The sibling provider store put on the same contract in the same change. [13]
- The provider-store durability suite: `lost == 0`, `torn_lines == 0` and `stragglers == []` over the forced single-record window for both provider stores, asserted rather than restated as a base-commit rate. [14]
- The attention-dismissal control-plane log whose unlocked draft measured 31.45% loss — the precedent that refused "one writer" as a reason not to lock. [15]
- The supervisor-signal control-plane log whose unlocked draft measured 31.45% loss — the precedent that refused "one writer" as a reason not to lock. [16]

### Cross-Repo References

No meaningful cross-repo references found.

This protocol is providers-only this iteration; Sentry integration is a future detection source in a separate task (`260703_spotlight-dev-observability`), not yet a cross-repo/cross-system boundary this module touches.


## Current Durable-Store Lock Composition

The provider store continues to use the same durable append/rewrite contract. Its exclusion
owner validates the checkout target before shared kernel locking and maps lock-capability
failures into the existing durable error family. This source verification does not change the
provider thresholds, hysteresis or failsafe behavior.

- Store exclusion keeps checkout coordination ahead of the shared kernel primitive. [17]


## Current Investigator contract impact

Current alert/inbox vocabulary addresses Investigator. The degradation protocol’s samples, thresholds, alert state and remediation/order boundaries are preserved by the canonical naming change; historical task and quoted ruling words retain the earlier spelling. A broader concern role does not authorize a provider restart forbidden by alert state.

- This source owns the stated current Investigator scope or canonical vocabulary. [18]


## Refreshed current evidence

- The inbox record schema (`system-specialist` in `AgentRole`, `degradation-alert` in `InboxMessageKind`) this module posts against — vocabulary in models/operator_inbox.py since L9. [5]
- Failing-first tests pinning hysteresis, inbox delivery parity, and failsafe-stop-failure durability. [11]
