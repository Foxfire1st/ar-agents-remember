# mcp/src/agents_remember/serving/harness_control_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:00+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the vendor-neutral `HarnessProtocolAdapter` contract, explicit adapter registry, unsupported
adapter behavior, and normalized event reducer used by one hosted control bridge.

## Code Commentary

The protocol covers start/handshake, snapshot/subscription, correlated submit/respond/reconcile,
and shutdown. Registry absence is an explicit `unsupported` state; there is no pane, regex, or log
timing fallback. The reducer enforces exact identity and monotonic event sequence, fails malformed
known events, and preserves raw detail for additive unknown events.

## Invariants And Boundaries

- One bridge owns one adapter; later leaves register vendor factories explicitly.
- Capability and protocol-version mismatches fail before the bridge adopts state.
- Possible-send disconnects stay ambiguous and never trigger automatic duplicate submission.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Normalized contract models. | [harness_control_models.py](harness_control_models.py) |
| Bridge lifecycle and queue. | [harness_control_bridge.py](harness_control_bridge.py) |
| Conformance coverage. | [test_harness_control.py](../../../tests/test_harness_control.py) |

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the explicit
  adapter protocol, registry, unsupported path, handshake gate, and event reduction rules.
