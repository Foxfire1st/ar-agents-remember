# mcp/src/agents_remember/serving/harness_control_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:00+02:00 |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661` |
| lastVerifiedCommitDate | 2026-07-14T10:43:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the protocol-neutral value objects and JSON projections for one hosted harness control
session: exact identity, handshake, normalized control/activity/acceptance state, prompt and
interaction requests, receipts, reconciliation, transcript entries, and shutdown mode.

## Code Commentary

The normalized snapshot keeps control (`starting`, `ready`, `disconnected`, `failed`, `unsupported`),
activity (`idle`, `running`, `blocked`, `settling`, `unknown`), and acceptance orthogonal while
retaining raw vendor detail. Request ids, vendor correlation ids, timestamps, and exact AR/session
identity remain explicit. `UncommittedDraft` is surface-owned: R11 requires an automated delivery
to be a whole ordered message that cannot inject into, submit, or discard a human draft.

## Invariants And Boundaries

- Models carry protocol state; tmux pane text and terminal logs are diagnostic, not authoritative.
- Additive raw event detail is retained without guessing semantics for unknown event kinds.
- Disconnect-after-possible-send remains unknown and must be reconciled, never blindly resent.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Adapter boundary and event reducer. | [harness_control_adapter.py](harness_control_adapter.py) |
| Bridge and ordered delivery owner. | [harness_control_bridge.py](harness_control_bridge.py) |
| Surface-owned draft contract. | [harness_terminal_surface.py](harness_terminal_surface.py) |
| Leaf requirements and R11 ruling. | [task doc](../../../../../../../../../../tasks/agents-remember/260713_protocol-backed-harness-adapters/01_control-bridge-and-state-contract.json) |

## Update History

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the normalized
  control models, identity/correlation state, raw vendor detail, and R11 draft ownership.
