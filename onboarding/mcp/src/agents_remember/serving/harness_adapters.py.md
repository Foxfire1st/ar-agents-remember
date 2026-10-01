# mcp/src/agents_remember/serving/harness_adapters.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`harness_adapters.py` is the failure-diagnostic adapter for the one log-verified delivery path.
It may label a final pane capture as a quota/permission modal, but it never decides boot readiness,
composer state, turn start, knob truth, or delivery acceptance. Harness-owned JSONL is the only
submitted-acceptance authority.

## Code Commentary

### Logic

`HarnessAdapter` stores only `harness_id` and exposes `blocked_reason(pane_text)`. That method
delegates to `pane_signals.classify_pane_signal` and `blocked_reason_label`, returning a structured
modal reason only for a final failure capture. `get_adapter` preserves named Claude/Codex/generic
instances and returns a lightweight adapter for unknown ids; no screen grammar can turn an input
into an acknowledged delivery.

### Conventions

The adapter owns no regex table. Modal patterns remain in `pane_signals.py`; acceptance parsing
lives separately in `harness_logs.py` and is never reached through this diagnostic interface.

### Invariants And Boundaries

- `HarnessAdapter` is stateless/pure: no I/O, catalog access, acceptance polling, or retries.
- A blocked label may enrich a failure result; it must never override positive/negative harness-log
  evidence or grant `submitted:true`.
- Boot/composer/turn/knob screen grammars removed by L15 must not be reintroduced here.

### Todos

Modal labels remain best-effort failure diagnostics; no correctness claim depends on them.

## Evidence

### Docs References

No relevant external documentation found after checking the repo Domain Documentation for
per-harness delivery-adapter behavior; this file is same-repository runtime plumbing (the leaf task
doc's R2 is the source of truth), same posture as `pane_signals.py`/`turn_state.py`.

- No external/domain document defines a per-harness delivery adapter; the leaf task doc (R2) and this implementation are the source of truth. [1]

### Repo-Internal References

- `get_adapter` is the sole entry point `serving.injector.deliver` calls to resolve per-harness behavior for the blocked-check and post-submit-confirmation corroboration. [2]
- `boot_ready`/`composer_state` compose `turn_state.classify_turn_state`/`turn_state.boot_ready` and `pane_signals.classify_pane_signal`/`pane_signals.composer_state`/`pane_signals.blocked_reason_label` — the single source of truth for every pattern table. [3]


### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary owns or consumes this local delivery adapter.

#### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.
