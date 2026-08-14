# mcp/src/agents_remember/serving/harness_adapters.py

| Field                  | Value                                                     |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/serving/harness_adapters.py`       |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-10T13:03+02:00                                      |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
per-harness delivery-adapter behavior; this file is same-repository runtime plumbing (the leaf task
doc's R2 is the source of truth), same posture as `pane_signals.py`/`turn_state.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines a per-harness delivery adapter; the leaf task doc (R2) and this implementation are the source of truth. | `HarnessAdapter` | mcp/src/agents_remember/serving/harness_adapters.py:14-25 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `get_adapter` is the sole entry point `serving.injector.deliver` calls to resolve per-harness behavior for the blocked-check and post-submit-confirmation corroboration. | `deliver` | mcp/src/agents_remember/serving/injector.py:60-134 |
| `boot_ready`/`composer_state` compose `turn_state.classify_turn_state`/`turn_state.boot_ready` and `pane_signals.classify_pane_signal`/`pane_signals.composer_state`/`pane_signals.blocked_reason_label` — the single source of truth for every pattern table. | `classify_turn_state`; `boot_ready` | mcp/src/agents_remember/serving/turn_state.py:157-171; mcp/src/agents_remember/serving/turn_state.py:174-177 |
| Fixtures for both harnesses across boot/ready/mid-turn/chip-stacked/quota-modal, plus the registry fallback behavior. | `### Logic` | onboarding/mcp/tests/test_harness_adapters.py.md:22-42 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local delivery adapter. | — | — |

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 1 repeated path:start-end Citation objects from 1 same-claim citation group(s) at card line(s) 65; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 2 citation entries (4 findings) and deleted the single empty/unanchorable row under the 2026-08-02T14:10 ruling; remaining citation result is zero.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 removal round: deleted boot/composer/mid-turn/turn-start
  delivery signatures. The adapter now labels only final failure captures; harness JSONL owns all
  submitted acceptance. Verification metadata remains pinned until closeout stamps the eventual
  L15 code commit.

- 2026-07-08T22:30+02:00 — Created for 260707-HFX2-L3 (paste injector hardening, R2): the one
  per-harness adapter interface — `HarnessAdapter` (boot_ready, composer_state, mid_turn,
  mid_turn_behavior, blocked_reason, turn_started), `get_adapter` registry with graceful fallback,
  named `CLAUDE_CODE_ADAPTER`/`CODEX_ADAPTER`/`GENERIC_ADAPTER` instances, and the NEW-HARNESS
  CHECKLIST docstring (R4: a future harness is one adapter registration, never a new delivery path).
  Composes existing classifiers only; adds no new pattern table of its own. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L3 commit.
