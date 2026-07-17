# mcp/src/agents_remember/serving/harness_control_ipc.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_ipc.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides user-private Unix-domain-socket IPC for one exact-session bridge, with bounded JSON-line
requests and explicit snapshot, live advertise, model/effort set, submit, respond, reconcile,
transcript, and stop actions.

## Code Commentary

### Logic

Endpoint names hash the complete control identity. Runtime directories are `0700`, sockets `0600`,
and non-socket replacements are refused. Every request validates protocol and identity before
dispatch. `advertise`, `set-model`, and `set-effort` serialize the bridge's normalized capability
and `SetResult` types; submit and reconcile retain full internal receipt evidence. After accepted
dispatch, narrow peer-loss exceptions are contained while the bridge remains the truth owner.

### Conventions

The wire is one bounded JSON object per line. Actions are kebab-case; payload field names are the
normalized camel-case names. The socket transports commands but does not decide acceptance.

### Invariants And Boundaries

- Same-user filesystem permissions are the local endpoint security boundary.
- Exact catalog/session identity is required on every request.
- Dispatch, identity, protocol, request validation, serialization, cancellation, and unrelated
  failures remain authoritative and loud. Only the two concrete peer-disconnect classes are
  contained after accepted dispatch; this is not a broad connection-error or fallback boundary.
- A delayed reply disconnect leaves an ambiguous accepted submission reconcilable through the bridge;
  it does not retry or silently degrade the request.
- Advertise and set address the exact running adapter instance; pre-session discovery does not use
  this socket.
- Endpoint transport is replaceable behind the protocol contract.

### Todos

None known for the L4 private IPC action set.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The bridge supplies ordered native truth and the blocking client applies first-byte retry safety.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The bridge exposes live advertise and ordered setter operations only while running. | L158-L202 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The blocking client validates exact identity and distinguishes pre-write from post-write loss. | L58-L88; L205-L280 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| IPC tests pin capability actions, setters, same-id submit retention, response loss, and reconciliation. | L988-L1285 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |

## Cross-Repo References

No external repository boundary is implemented by the local exact-session socket.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

IPC dispatch now carries epoch/source through submit and exposes reconcile, resolve-operation,
authority, bounded status, and withdraw actions. Cockpit-only disclosure is enforced before raw-free
serialization; request ids and operation refs are validated structurally. Typed busy/conflict/epoch
errors retain their meaning across the private socket boundary.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: documented lifecycle IPC actions, epoch/source validation,
  cockpit privacy, bounded batches, and typed error preservation.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented exact-session advertise and set
  actions, normalized serialization, and retained private receipt evidence for ambiguity closure.
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: documented narrow post-dispatch peer-disconnect
  containment during reply and close lifecycle, with delayed-reply reconciliation preserved.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for private exact-identity
  IPC, permissions, bounded messages, and explicit control operations.
