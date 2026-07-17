# mcp/src/agents_remember/serving/harness_control_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines protocol-neutral value objects and JSON projections for one hosted harness control session:
exact identity, handshake, normalized state, prompt and interaction requests, receipts,
reconciliation, transcript entries, and shutdown mode. L4 adds deliberately raw-free serializers
for the daemon's public submit and reconciliation responses.

## Code Commentary

### Logic

The normalized snapshot keeps control (`starting`, `ready`, `disconnected`, `failed`,
`unsupported`), activity, and acceptance orthogonal while retaining raw vendor detail internally.
Request ids, correlation ids, timestamps, and exact AR/session identity remain explicit.
`receipt_json` and `reconciliation_json` preserve full internal evidence for private IPC and durable
diagnostics. `public_receipt_json` and `public_reconciliation_json` expose only normalized fields and
intentionally omit `raw` from the daemon consumer contract.

### Conventions

Internal serializers preserve additive vendor evidence; public serializers are separate named
functions rather than an exclusion flag so callers cannot accidentally leak the private mapping.
Wire names are camel-case.

### Invariants And Boundaries

- Models carry protocol state; tmux pane text and terminal logs are diagnostic, not authoritative.
- Additive raw event detail is retained without guessing semantics for unknown event kinds.
- Disconnect-after-possible-send remains unknown and must be reconciled, never blindly resent.
- Public receipt/reconciliation responses retain normalized correlation and detail but never `raw`.

### Todos

None known for the L4 public serialization boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The API consumes only the public projections, while private IPC keeps full internal serializers.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The daemon submit and reconcile routes select the public raw-free serializers. | L173-L210 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |
| Private IPC still serializes full receipts and reconciliation evidence for exact-session peers. | L180-L227 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| Public route tests seed sensitive-looking raw mappings and prove they do not cross the boundary. | L166-L219 | [test_serving_harness_control_api.py](agents-remember/mcp/tests/test_serving_harness_control_api.py) |

## Cross-Repo References

No external repository boundary is implemented by these local protocol models.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

The normalized model now carries bridge epoch on prompts, receipts, and reconciliation; defines full
operation references, authority/status/batch/withdraw/event records; and separates private internal
serialization from raw-free public lifecycle projection. The public alphabet is intentionally
smaller than vendor evidence and sufficient for monotonic cockpit rendering.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: added generation-bound submit records, full operation refs,
  normalized status/withdraw DTOs, and explicit public/private serialization boundaries.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the explicit public receipt and
  reconciliation serializers that preserve normalized evidence while omitting adapter-private raw.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the normalized
  control models, identity/correlation state, raw vendor detail, and R11 draft ownership.
